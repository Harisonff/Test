


label village_build_start:

    scene black
    scene villagemap_day_base
    with dissolve

    menu:
        "Is it day or night?"
        "night":


            $ bk3_day = False
        "day":
            $ bk3_day = True








screen bk3_buildspot:




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



label sector_allocation:


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
                        jump bk3_village_background
                    else:

                        "you need {b}5 wood{/b} and {b}5 steel{/b} to build this!"
                        "you have [bk3_wood] wood and [bk3_steel] steel."
                        jump sector_allocation
                "tavern (locked)":

                    if not bk3_store_built:
                        "you need to build a store!"
                        jump sector_allocation
                    else:
                        "under development."
                        jump bk3_village_background

                "brothel (locked)" if suki_hypno ==0 or brothel_built:
                    "not yet available."
                    jump sector_allocation

                "brothel" if suki_free and not brothel_built:
                    if bk3_wood >=5 and bk3_steel >=5:
                        $ brothel_building = 1
                        $ brothel_built = True
                        $ bk3_wood -=5
                        $ bk3_steel -=5
                        call screen bk3_buildspot
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
                        "you work into the night, building the brothel."
                        jump bk3_village_background
                    else:

                        "you need {b}5 wood{/b} and {b}5 steel{/b}."
                        "you have [bk3_wood] wood and [bk3_steel] steel."
                        jump bk3_village_background

                "hospital (locked)" if not hospital_build or hospital_built:
                    "test"

                "hospital" if hospital_build and not hospital_built:
                    if bk3_wood >=5 and bk3_steel >=5:
                        $ hospital_building = 1
                        $ hospital_built = True
                        $ bk3_wood -=5
                        $ bk3_steel -=5
                        call screen bk3_buildspot
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
                        jump bk3_village_background
                    else:

                        "you need {b}5 wood{/b} and {b}5 steel{/b}."
                        "you have [bk3_wood] wood and [bk3_steel] steel."
                        jump bk3_village_background
                "back":
                    jump sector_allocation
        "upgrade":

            menu:
                "house" if avatar_shack ==2 and brothel_building >=3 and bk3_slave == True:
                    if obsidian >=1 and bk3_wood >=10 and bk3_steel >=10:
                        $ obsidian -=1
                        $ bk3_wood -=10
                        $ bk3_steel -=10
                        $ avatar_shack = 3
                        jump bk3_village_background
                    else:
                        "you need {b}1 obsidian, 10 wood, and 10 steel{/b} to upgrade your house!"
                        "you have [obsidian] obsidian, [bk3_wood] wood, and [bk3_steel] steel."
                        jump sector_allocation

                "house" if avatar_shack < 2 and bk3_slave == True:
                    if obsidian >=1 and bk3_wood >=10 and bk3_steel >=10:
                        $ obsidian -=1
                        $ bk3_wood -=10
                        $ bk3_steel -=10
                        $ avatar_shack = 2
                        jump bk3_village_background
                    else:
                        "you need {b}1 obsidian, 10 wood, and 10 steel{/b} to upgrade your house!"
                        "you have [obsidian] obsidian, [bk3_wood] wood, and [bk3_steel] steel."
                        jump sector_allocation

                "tavern" if tavern_shack ==1 and bk3_slave == True:
                    if obsidian >=1 and bk3_wood >=10 and bk3_steel >=10:
                        $ obsidian -=1
                        $ bk3_wood -=10
                        $ bk3_steel -=10
                        $ tavern_shack = 2
                        jump bk3_village_background
                    else:
                        "you need {b}1 obsidian, 10 wood, and 10 steel{/b} to upgrade the tavern!"
                        "you have [obsidian] obsidian, [bk3_wood] wood, and [bk3_steel] steel."
                        jump sector_allocation

                "tavern" if tavern_shack ==2 and avatar_shack >=3 and bk3_slave == True:
                    if obsidian >=1 and bk3_wood >=10 and bk3_steel >=10:
                        $ obsidian -=1
                        $ bk3_wood -=10
                        $ bk3_steel -=10
                        $ tavern_shack = 3
                        jump bk3_village_background
                    else:
                        "you need {b}1 obsidian, 10 wood, and 10 steel{/b} to upgrade the tavern!"
                        "you have [obsidian] obsidian, [bk3_wood] wood, and [bk3_steel] steel."
                        jump sector_allocation

                "shop (locked)" if shop_building ==2:
                    "test"

                "shop" if avatar_shack >=2 and shop_building < 2:
                    if obsidian >=1 and bk3_wood >=10 and bk3_steel >=10:
                        $ obsidian -=1
                        $ bk3_wood -=10
                        $ bk3_steel -=10
                        $ shop_building = 2
                        jump bk3_village_background
                    else:
                        "you need {b}1 obsidian, 10 wood, and 10 steel{/b} to upgrade the shop!"
                        "you have [obsidian] obsidian, [bk3_wood] wood, and [bk3_steel] steel."
                        jump sector_allocation

                "brothel (locked)" if not bk3_tylee_surprise:
                    "test"

                "brothel" if bk3_tylee_surprise and brothel_building <2:
                    if obsidian >=1 and bk3_wood >=10 and bk3_steel >=10:
                        $ obsidian -=1
                        $ bk3_wood -=10
                        $ bk3_steel -=10
                        $ brothel_building = 2
                        jump bk3_village_background
                    else:
                        "you need {b}1 obsidian, 10 wood, and 10 steel{/b} to upgrade the shop!"
                        "you have [obsidian] obsidian, [bk3_wood] wood, and [bk3_steel] steel."
                        jump sector_allocation

                "brothel" if peasant_slut_hired and brothel_building <=2:
                    if obsidian >=1 and bk3_wood >=10 and bk3_steel >=10:
                        $ obsidian -=1
                        $ bk3_wood -=10
                        $ bk3_steel -=10
                        $ brothel_building = 3
                        jump bk3_village_background
                    else:
                        "you need {b}1 obsidian, 10 wood, and 10 steel{/b} to upgrade the shop!"
                        "you have [obsidian] obsidian, [bk3_wood] wood, and [bk3_steel] steel."
                        jump sector_allocation

                "hospital" if hospital_upgrade_talk and hospital_building == 1:
                    if obsidian >=1 and bk3_wood >=10 and bk3_steel >=10:
                        $ obsidian -=1
                        $ bk3_wood -=10
                        $ bk3_steel -=10
                        $ hospital_building = 2
                        jump bk3_village_background
                    else:
                        "you need {b}1 obsidian, 10 wood, and 10 steel{/b} to upgrade the shop!"
                        "you have [obsidian] obsidian, [bk3_wood] wood, and [bk3_steel] steel."
                        jump sector_allocation

                "hospital" if hospital_building == 2:
                    if obsidian >=1 and bk3_wood >=10 and bk3_steel >=10:
                        $ obsidian -=1
                        $ bk3_wood -=10
                        $ bk3_steel -=10
                        $ hospital_building = 3
                        jump bk3_village_background
                    else:
                        "you need {b}1 obsidian, 10 wood, and 10 steel{/b} to upgrade the shop!"
                        "you have [obsidian] obsidian, [bk3_wood] wood, and [bk3_steel] steel."
                        jump sector_allocation
                "back":

                    jump bk3_village_background
        "back":

            jump bk3_village_background


    menu:
        "The avatar's shack is.."
        "in it's first stage":
            $ avatar_shack = 1
            "and is placed..."
            call screen bk3_buildspot
        "in it's second stage":
            $ avatar_shack = 2
            "and is placed..."
            call screen bk3_buildspot
        "in it's third stage":
            $ avatar_shack = 3
            "and is placed..."
            call screen bk3_buildspot
        "dude it doesn't even exist!":
            $ avatar_shack = 0
            $ _return = 0


    if _return == 1:
        $ avatar_shack_xpos = 6
        $ avatar_shack_ypos = 85
        $ position_1 = True
    elif _return == 2:
        $ avatar_shack_xpos = 342
        $ avatar_shack_ypos = 84
        $ position_2 = True
    elif _return == 3:
        $ avatar_shack_xpos = 675
        $ avatar_shack_ypos = 80
        $ position_3 = True
    elif _return == 4:
        $ avatar_shack_xpos = 6
        $ avatar_shack_ypos = 295
        $ position_4 = True
    elif _return == 5:
        $ avatar_shack_xpos = 680
        $ avatar_shack_ypos = 300
        $ position_5 = True
    elif _return == 6:
        $ avatar_shack_xpos = 5
        $ avatar_shack_ypos = 519
        $ position_6 = True
    elif _return == 7:
        $ avatar_shack_xpos = 340
        $ avatar_shack_ypos = 520
        $ position_7 = True
    elif _return == 8:
        $ avatar_shack_xpos = 675
        $ avatar_shack_ypos = 510
        $ position_8 = True
    else:
        pass









    "where to put the hospital?"


    menu:
        "The hospital is.."
        "in it's first stage":
            $ hospital_building = 1
            call screen bk3_buildspot
        "in it's second stage":
            $ hospital_building = 2
            call screen bk3_buildspot
        "in it's third stage":
            $ hospital_building = 3
            call screen bk3_buildspot
        "dude it doesn't even exist!":
            $ hospital_building = 0
            $ _return = 0



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









    menu:
        "The shop is.."
        "in it's first stage":
            $ shop_building = 1
            "and is placed..."
            call screen bk3_buildspot
        "in it's second stage":
            $ shop_building = 2
            "and is placed..."
            call screen bk3_buildspot
        "in it's third stage":
            $ shop_building = 3
            "and is placed..."
            call screen bk3_buildspot
        "dude it doesn't even exist!":
            $ shop_building = 0
            $ _return = 0



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











    menu:
        "The tavern is.."
        "in it's first stage":
            $ tavern_shack = 1
            "and is placed..."
            call screen bk3_buildspot
        "in it's second stage":
            $ tavern_shack = 2
            "and is placed..."
            call screen bk3_buildspot
        "in it's third stage":
            $ tavern_shack = 3
            "and is placed..."
            call screen bk3_buildspot
        "dude it doesn't even exist!":
            $ tavern_shack = 0
            $ _return = 0



    if _return == 1:
        $ tavern_shack_xpos = 6
        $ tavern_shack_ypos = 85
        $ position_1 = True
    elif _return == 2:
        $ tavern_shack_xpos = 342
        $ tavern_shack_ypos = 84
        $ position_2 = True
    elif _return == 3:
        $ tavern_shack_xpos = 675
        $ tavern_shack_ypos = 80
        $ position_3 = True
    elif _return == 4:
        $ tavern_shack_xpos = 6
        $ tavern_shack_ypos = 295
        $ position_4 = True
    elif _return == 5:
        $ tavern_shack_xpos = 680
        $ tavern_shack_ypos = 300
        $ position_5 = True
    elif _return == 6:
        $ tavern_shack_xpos = 5
        $ tavern_shack_ypos = 519
        $ position_6 = True
    elif _return == 7:
        $ tavern_shack_xpos = 340
        $ tavern_shack_ypos = 520
        $ position_7 = True
    elif _return == 8:
        $ tavern_shack_xpos = 675
        $ tavern_shack_ypos = 510
        $ position_8 = True







label bk3_village_background:
    if bk3_loveroute:
        jump love_bk3_village_background
    $ tophs_home_access = True
    scene black
    show screen earth_money_date
    if caught_peeking:
        $ caught_peeking1 = True
        $ bk3_day = True

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
                show expression "ebackgrounds/village/buildings/shack/shack02.png":
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

    if bk3_handjob ==2:
        show toki toki02
        show toki_angry
        with dissolve
        k3 "see! it's a mess!"
        y "calm down."
        y "i need to take a closer look."
        scene tracks_toph with Dissolve(1)
        hide toki_angry
        y "hmmm..."
        show ctc
        pause
        hide ctc
        y "yeah... this isn't good."
        y "there's this one big track in the middle... like they were dragging something."
        show toki toki01
        show toki_angry
        with dissolve
        k3 "we need to follow it!"
        y "...i know."
        y "you stay here, i'll take care of it."
        show toki toki02
        hide toki_angry
        show toki_surprised
        with dissolve
        k3 "please be careful, aang."
        y "...no."
        y "{i}they{/i} had better be careful."
        y "if she is harmed... at all..."
        y "someone's head is getting smooshed."
        show toki toki01
        hide toki_surprised
        with dissolve
        k3 "i believe in you!"
        scene black with Dissolve(1)
        $ bk3_handjob = 3
        jump rescue_toph_tunnels

    if toph_tunnel_training ==2:
        y "finally!"
        y "that was not the earthbending training i wanted."
        y "toph is gonna get an ass-full. i mean, an earful."
        y "...."
        y "i'm gonna yell at her."
        "you walk up to toph's house and bang on the door."
        y "....."
        y "hello?"
        "you knock on the door again."
        "there's no answer."
        y "i'm not afraid to barge in!"
        y "....okay, i'm a little afraid."
        y "but i'll do it anyway!"
        "you hear footsteps approach from inside the house."
        "after a moment, the door opens."
        show toki toki01 with Dissolve(1.0)
        k3 "hello, aang."
        y "what..."
        y "why are you here, katara?"
        k3 "i've been working on something for you."
        y "...okay..."
        k3 "toph visited me today, and we talked... and she asked for my help."
        k3 "come in and see."
        $ toph_tunnel_training = 3
        jump toph_anal1

    if naga_toph_old == 4:
        show toju toju02 with dissolve
        ju "hey. boss man."
        y "stay... stay away..."
        ju "yeah... so what the hell was that?"
        y "...what?"
        show toju toju01 with dissolve
        ju "You came into the tavern and started yelling at me."
        y "i did?"
        ju "yeah, you kept yelling \"mai\" and some other nonsense."
        ju "every time i said something, you just... spazzed out at me."
        show toju toju02 with dissolve
        ju "if you're not getting enough sleep, you should change that."
        ju "see you later, boss."
        hide toju with dissolve
        y "....what's happening with me?"
        $ naga_toph_old = 5

    if naga_toph_old == 1:
        y "what the fuck!?"
        t "aang?"
        y "No, no, no, stay away from me, you-"
        show toi toi09 with dissolve
        t "is something wrong?"
        t "i heard you yelling from-"
        y "what the hell was that?"
        y "why were you old?"
        t "what?"
        t "oh, when i took that potion after the train?"
        t "i honestly forgot-"
        y "No, just now!"
        y "when we spoke!"
        t "we... didn't just speak."
        t "i don't think we've even talked today, aang."
        y "what... but... but..."
        t "go get some rest."
        hide toi toi09 with dissolve
        y "......"
        y "something's wrong."
        $ naga_toph_old = 2

    if earthbending ==6 and not eb6_self_convo:
        y "well, my earthbending is definitely stronger."
        y "i wonder if i can break deeper into the tunnels?"
        y "i should go down to that maze and see if there's a wall i can break through."
        $ eb6_self_convo = True
        $ maze_sections = 1

    if laogai_travel and not first_maze_key:
        show thankful_girl with dissolve
        girl "av... avatar?"
        y "yeah?"
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
        hide thankful_girl with dissolve
        y "where.... was she hiding it?"
        hide toi toi09 with dissolve
        $ first_maze_key = True
        jump bk3_village_background

    if first_maze_girl and not first_maze_girl_escape:
        show toi toi09 with dissolve
        t "get her inside."
        y "okay, hold on-"
        "you drop the unconcious girl on the ground."
        with vshake
        show toi toi06 with dissolve
        t "hey!"
        y "what the hell is going on?"
        y "we're having a nice, happy day at the lake, and suddenly we're in dark, creepy of tunnels..."
        y "...i'm fighting very violent chicks...."
        y "...and rescuing a naked slave from a maze."
        y "what the fuck have i gotten in to?"
        show toi toi05 with dissolve
        t "well, i don't know!"
        show toi toi09 with dissolve
        t "let's just help this girl, and maybe she can tell us what's going on."
        t "in the meantime, we can't go back there."
        y "don't tell me what to do."
        t "i thought you didn't want to go back there anyway."
        y "i don't. but i don't want to be told what to do, either."
        show toi_blink with dissolve
        t "whatever."
        t "just bring her inside."
        jump inside_tophs_home

    if earthbending ==3 and not first_lake_visit:
        show toi toi02 with dissolve
        t "well, that was fun..."
        show toi toi09 with dissolve
        t "though it took a weird turn at the end there."
        show toi toi04 with dissolve
        t "goodnight, aang."
        hide toi toi04 with dissolve
        $ first_lake_visit = True
        scene black with dissolve
        "you head home for the night."
        jump bk3_next

    if caught_peeking:
        yc "ow...."
        y "that little tart knocked me out!"
        y "...."
        y "at least I'm well rested..."
        $ caught_peeking = False
        $ caught_peeking1 = False
        jump bk3_next

    if tavern_shack ==1 and not bk3_tavern_built:
        $ bk3_tavern_built = True
        jump bk3_village_background

    if bk3_tavern_built1 and not bk3_tavern_built2:
        play sound "audio/construction2.mp3"
        "building the tavern takes you well into the night."
        show toi toi02 with dissolve
        t "finally."
        y "that was exhausting..."
        t "yeah, but now we've got a place for people to stay."
        y "great. who's gonna manage it?"
        show toi_blink with dissolve
        t "well, you, duh."
        y "uh... i don't know about that."
        show toi toi06
        hide toi_blink
        with dissolve
        t "i'm getting sick of your attitude, aang."
        show toi toi05 with dissolve
        t "you need to man up."
        $ bk3_tavern_built2 = True
        show toi_blink with dissolve
        t "we're gonna do some important training tomorrow, so rest up."
        hide toi_blink
        hide toi toi05
        with dissolve
        jump bk3_village_background

    if avatar_shack ==1 and not village_dev_explain:
        $ village_dev_explain = True
        jump bk3_village_background

    if village_dev_explain1 and not village_dev_explain2:
        play sound "audio/construction2.mp3"
        "you work on your house until night."
        show toi toi02
        show toi_blink
        with dissolve
        t "nicely done, aang."
        y "...my house is tiny."
        hide toi_blink with dissolve
        t "right now, yeah."
        t "but we'll make it nicer later."
        t "we've got to get some other stuff going on in this village."
        y "why?"
        show toi toi06 with dissolve
        t "well-"
        show toi toi09
        show prisonbitch_idle
        with Dissolve(0.3)
        strangegirl "help m-"
        y "ah!"
        y "i... who even are you?"
        strangegirl "help me, please...."
        y "seriously, who are you?"
        strangegirl "i escaped... i just need... rest..."
        t "you can stay in my house for now. it's over there."
        hide prisonbitch_idle
        with dissolve
        "without another word, the girl trudges off towards toph's house."
        y "....."
        y "who the heck was that?"
        show toi_blink with dissolve
        t "i don't know, but... people have been coming through here and trying to hide in the ruins."
        show toi toi06
        hide toi_blink
        with dissolve
        t "but we destroyed the ruins."
        t "i've talked with a few before you came back, and..."
        show toi toi09 with dissolve
        t "we have to help them."
        y "she said she \"escaped\"."
        y "do you know what she was talking about?"
        show toi_blink with dissolve
        t "a few of them have mentioned something like that, but won't give me any details."
        y "okay, so what do i need to do?"
        show toi toi06
        hide toi_blink
        with dissolve
        t "we need to build a place for them to stay, and get some food."
        t "we need a tavern."
        t "plus, we're terrible cooks so..."
        y "yeah, i don't {i}relish{/i} the idea of eating what-"
        show toi toi09
        show toi_blink
        with dissolve
        t "no, aang. just... no."
        y "aw."
        hide toi_blink with dissolve
        t "i've made some temporary shelter for most of them, but... it's not very comfortable."
        t "so we're gonna need {b}5 wood{/b} and {b}5 steel{/b} to build a basic tavern."
        menu:
            "why should i care?":
                y "and i should care because...."
                show toi toi06 with dissolve
                t "because i care!"
                y "pfft."
                t "......"
                show toi toi09 with dissolve
                t "i can't... offer you anything right now, aang."
                t "but please. it's really important to me that we do this."
                y "....oh, alright."
                t "thanks."
            "i will, for you":

                y "anything for you, toph. you know that."
                show toi_blush with dissolve
                t "i... oh."
                show toi_blink with dissolve
                t "well... thank you."

        show toi toi04
        hide toi_blush
        hide toi_blink
        with dissolve
        t "now get some rest... training continues in the morning!"
        y "*groan...*"
        show toi_blink with dissolve
        t "don't be a baby."
        $ village_dev_explain2 = True
        hide toi toi04
        hide toi_blink
        with dissolve
        $ quest5 = True
        $ bk3_wood -=5
        $ bk3_steel -=5

    call screen bk3_village_pick



screen bk3_village_pick:

    imagemap:
        ground "ebackgrounds/village/earth_village_pick_idle.png"
        hover "ebackgrounds/village/earth_village_pick.png"







        if avatar_shack > 0 and avatar_shack_access:
            hotspot (avatar_shack_xpos, avatar_shack_ypos, 300, 190) clicked Jump("inside_avatar_shack")

        if hospital_building > 0 and hospital_building_access:
            hotspot (hospital_building_xpos, hospital_building_ypos, 300, 190) clicked Jump("inside_hospital_building")

        if shop_building > 0 and shop_building_access:
            hotspot (shop_building_xpos, shop_building_ypos, 300, 190) clicked Jump("inside_shop_building")

        if tophs_home > 0 and tophs_home_access:
            hotspot (340, 290, 300, 190) clicked Jump("inside_tophs_home")

        if tavern_shack > 0 and tavern_shack_access:
            hotspot (tavern_shack_xpos, tavern_shack_ypos, 300, 190) clicked Jump("inside_tavern_shack")

        if brothel_building > 0 and brothel_building_access:
            hotspot (brothel_building_xpos, brothel_building_ypos, 300, 190) clicked Jump("inside_brothel_building")

        if bk3_day and bk3_village_access:
            imagebutton idle "bk3/icons/bk3_basingse_off.png" hover "bk3/icons/bk3_basingse_on.png" xpos 0.25 ypos 0 action Jump("basingse_day1")




        if village_store_build:
            imagebutton idle "bk3/icons/build_icon_off.png" hover "bk3/icons/build_icon_on.png" xpos 0.77 ypos 0 action Jump("sector_allocation")

        if bk3_day and laogai_travel:
            imagebutton idle "bk3/icons/bk3_maze_off.png" hover "bk3/icons/bk3_maze_on.png" xpos 0.18 ypos 0 action Jump("bk3_maze_start1")

        add "emberisland_cloud1"

label inside_avatar_shack:
    scene black
    scene inside_shack
    with Dissolve(0.2)
    if jin_hypno ==8:
        $ jin_hypno = 9
        show tojn tojn25 with dissolve
        jin "hello, lee."
        y "that is my name, yes."
        y "i am he."
        y "not somebody else who has brainwashed you into giving up that sweet pussy."
        show tojn tojn28 with dissolve
        jin "what?"
        show tojn tojn27 with dissolve
        jin "I know that...."
        show tojn tojn26 with dissolve
        jin "i was thinking... i know we barely know each other..."
        jin "but..."
        show tojn tojn27 with dissolve
        jin "...my body feels on fire when i'm around you..."
        jin "...when i think of you..."
        show tojn tojn28 with dissolve
        jin "I want... you inside of me."
        y "i can make that happen!"
        jin "...but we can't."
        y ".....what?"
        jin "I can move in with you, and i desperately, desperately want you..."
        show tojn tojn27 with dissolve
        jin "but i just can't go farther with you, i'm sorry."
        jin "I can't even tell you why."
        y "what? that wasn't planned for-"
        y "oh."
        y "i'm an idiot."
        show tojn tojn23 with dissolve
        jin "what?"
        y "[trigger]."
        show tojn tojn20
        show tojn_hypno_eyes
        with dissolve
        y "right, okay."
        y "i forgot to turn off the \"don't have sex with lee\" rule."
        y "and now, since i'm lee (in her mind, anyway), it's not a risk any more."
        y "so..."
        y "jin."
        y "you can now have sex with lee."
        y "repeat."
        jin "i... can now... have sex... with lee..."
        y "good."
        y "[trigger]."
        show tojn tojn23
        hide tojn_hypno_eyes
        with dissolve
        jin "what the...."
        jin "...."
        show tojn tojn28 with dissolve
        jin "{size=+10}fuck."
        jin "{size=+10}me."
        y "...."
        jin "{size=+10}fuck me."
        jin "{size=+10}{b}now."
        hide tojn with dissolve
        show tojn tojn32 with dissolve
        show ctc
        pause
        hide ctc
        jin "get over here."
        y "I... you got it."
        jump jin_sex1

    if bk3_tylee_met and not bk3_tylee_surprise:
        show tf with dissolve
        ty "hi!"
        y "ah! fuck!"
        y "do you want to give me a heart attack!?"
        ty "of course not, silly."
        ty "i like you."
        y "you don't know who i am."
        ty "...sure i do."
        ty "you're the avatar."
        y "i... well, yeah."
        y "so what do you want with me, ty... er... you?"
        show tfa with dissolve
        ty "well... azula's being mean."
        ty "i don't like when she's mean."
        hide tfa with dissolve
        ty "so i'm keeping myself busy."
        ty "i'm also looking for some fun."
        show tf2 with dissolve
        ty "give me a good time and i won't tattle on you, 'kay?"
        y "uh... yeah, that sounds good."
        hide tf2 with dissolve
        ty "great! i'm ty lee!"
        ty "where should i sleep?"
        y "uh... what?"
        ty "i need a place to stay."
        y "well there isn't room here..."
        y "wait, i've got an idea."
        y "come with me."
        ty "okay!"
        scene black with dissolve
        stop music
        play music "audio/Smooth Lovin.mp3"
        scene black
        scene inside_brothel_1
        show tosi tosi01
        show tf:
            xzoom -1.0
        with dissolve
        suki "hey, what's-"
        show tosi tosi03
        with dissolve
        suki "oh hell no!"
        y "what?"
        ty "hi again!"
        suki "this bitch and her friends got me thrown into those stupid tunnels!"
        suki "seriously, get her out of here before i kick her ass."
        show tf2:
            xzoom -1.0
        with dissolve
        ty "just try it!"
        ty "hee hee."
        y "come on, she's not here to cause trouble..."
        y "right?"
        ty "right!"
        y "see?"
        y "and she needs a place to stay, so i figured this would be a good spot."
        suki "the brothel?"
        y "well she said she's looking for fun..."
        hide tf2 with dissolve
        ty "i did!"
        y "what's more fun than a brothel?"
        suki "......."
        suki "we don't have enough rooms for both of us here."
        suki "upgrade the brothel, and.... maybe."
        ty "fun!"
        ty "i'll go wander around until you get this place ready for me!"
        ty "bye!"
        hide tf with dissolve
        suki "seriously... i hate her."
        hide tosi tosi03 with dissolve
        y "guess i gotta upgrade the brothel..."
        $ bk3_tylee_surprise = True
        jump bk3_village_background

    if not bk3_day:
        menu:
            "sleep":
                jump bk3_next

            "naga sleep" if naga_toph_old >=8 and not nagina_free:
                if toph_tunnel_training >=4:
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
                    if nagas_eyes == 1 and not tiny_naga_addressed:
                        $ tiny_naga_addressed = True
                        y "whoa, what's going on?"
                        "{i}i have shrunk to this size to conserve my energy."
                        y "and it's just adorable."

                    y "I guess we're not doing a blowjob in your current form, huh?"
                    "{i}there are other thingsss we can do..."
                    y "oh?"
                    "{i}yesss..."
                    y "you know what? let's test that."
                    show tonc tonc00 with Dissolve(1.5)
                    y "i want to see where this goes."
                    hide tonc_floats

                    show tonc_tail:
                        xpos 340 ypos 220
                        linear 2.0 ypos 230
                        linear 1.7 ypos 220
                        repeat
                    hide tonc
                    show tonc tonc01
                    with Dissolve(1.0)
                    "{i}very well...."
                    "{i}here...."
                    y "you're so... tiny!"
                    y "what can you even do?"
                    "{i}i could try... mmmm...."

                    $ nagachibi_head = 'down'

                    show tonc tonc100
                    "{i}thisss...."
                    show ctc
                    pause
                    hide ctc
                    "{i}sssee? I can give you a titjob..."
                    y "..uh, well it certainly {i}reminds{/i} me of a titjob."
                    y "i can feel your little snake tits on my cock, anyway."
                    y "but...."
                    $ nagachibi_head = 'up'
                    "{i}yesss?"
                    y "How about letting your tail help out?"
                    "{i}you wisssh me to ussse my tail?"
                    show tonc_tail:
                        alpha 0.0
                    show expression "bk3/naga/titjob/tail1.png":
                        xpos 520 ypos 280 xzoom 1.0

                        linear 1.0 xzoom 0.9 xpos 530 ypos 270
                        linear 1.0 xzoom 1.0 xpos 520 ypos 280
                        repeat
                    show expression "bk3/naga/titjob/tail1a.png":
                        ypos 0
                        linear 1 ypos 10
                        linear 1 ypos 0
                        repeat
                    with Dissolve(1.5)


                    "{i}like thisss?"
                    show ctc
                    pause
                    hide ctc
                    y "that. is. excellent."
                    $ nagachibi_head = 'down'
                    "{i}okay..."
                    y "You're the world's cutest boa constrictor."
                    y "If they sold your kind in petshops, Snake racism would be a thing of the past."
                    "{i}......"
                    y "you're not secretly planning to strangle me in my sleep, right?"
                    y "I wonder if Shady sells iron chokers... just to be on the safe side."
                    $ nagachibi_head = 'up'
                    "{i}hissss..."
                    y "oh, right, you're in my head."
                    y "non-corporeal, as it were."
                    y "so that wouldn't work."
                    $ nagachibi_head = 'down'
                    show ctc
                    pause
                    hide ctc
                    y "......."
                    y "You aren't trying to squeeze the life out of my penis are you?"

                    $ nagachibi_head = 'up'

                    "{i}I'm trying to sssqueeze {b}sssomething{/b} out of it...."
                    show tonc tonc07 with dissolve
                    "{i}And I can alssso lick your cock like nobody elssse can...."
                    y "with cute little laps?"
                    $ nagachibi_head = 'down'
                    with dissolve
                    "{i}no, from the inssside."
                    y "wha-?"
                    show tonc tonc101
                    ya "HnnnnnG!!"
                    show ctc
                    pause
                    hide ctc
                    "{i}yesss cum for me..."
                    ya "wha.. what the... the... hnng..."
                    "{i}cum, child..."
                    show ctc
                    pause
                    hide ctc
                    show tonc tonc07
                    with dissolve
                    "{i}Hmm ssstrangling your cock while doing thisss..."
                    "{i}...preventsss me from going any deeper..."
                    y "...uh... I like it that way."
                    y "I'm entirely okay with you not going dee-"
                    show tonc tonc101

                    hide expression "bk3/naga/titjob/tail1.png"
                    hide expression "bk3/naga/titjob/tail1a.png"

                    show tonc_tail:
                        alpha 1.0
                        xpos 340 ypos 220
                        linear 2.0 ypos 230
                        linear 1.7 ypos 220
                        repeat
                    with dissolve
                    ya "-eeeeeeperr!!!"
                    show ctc
                    pause
                    hide ctc
                    ya "Let's go back to you giving a titjob!"
                    ya "Like... right now!"
                    show tonc tonc07 with dissolve
                    "{i}very well...."
                    show tonc tonc100 with dissolve
                    y "...better... much better..."

                    $ nagachibi_head = 'up'
                    "{i}You're sssuch a little girl."
                    y "now, that's my kind of dirty talk!"
                    show tonc tonc07 with dissolve
                    "{i}....what isss wrong with you?"
                    y "I'mma bout to cum!"


                    menu:
                        "cum all over her tiny snake body":
                            ya "hngh!"
                            "{i}yesss! cum on m-"
                            play sound "audio/splurt2.ogg"
                            show expression "bk3/naga/titjob/spermshot.png"
                            $ renpy.pause(0.3)



                            hide expression "bk3/naga/titjob/spermshot.png"

                            hide tonc
                            hide tonc_tail

                            show tonc_floats_spermedon:
                                parallel:
                                    xpos 300
                                    linear 8.2 xpos 120
                                    linear 7.0 xpos 300
                                    repeat
                                parallel:
                                    ypos 50
                                    linear 2.0 ypos 80
                                    linear 2.4 ypos 50
                                    repeat

                            show tonc tonc00
                            with Dissolve(1.5)

                            "{i}...like drinking from a fire hydrant..."
                            show ctc
                            pause
                            hide ctc
                            scene black with Dissolve(1.5)
                            jump bk3_next
                        "cum in her mouth":

                            show tonc tonc06
                            show tonc_swallows2:
                                ypos 0
                                linear 0.5 ypos 7
                                linear 0.8 ypos 0
                                repeat
                            with Dissolve(1.5)

                            show tonc_tail:
                                xpos 340 ypos 230
                                linear 0.8 ypos 190
                                linear 0.7 ypos 230
                                repeat

                            y "You want my cum?"
                            "{i}yesss.... give...."
                            y "Here it comes!"
                            y "Swallow every last drop of it!"
                            play sound "audio/splurt2.ogg"
                            "{i}*gulp* *gulp*"
                            ya "fuck!"
                            ya "take it, snake slut!"
                            play sound "audio/splurt3.ogg"
                            show tonc_swallows:
                                ypos 0
                                linear 0.5 ypos 7
                                linear 0.8 ypos 0
                                repeat
                            hide tonc_swallows2
                            with vshake
                            "{i}gnk!"
                            y "ngh!"
                            "{i}*gulp* *gulp* *gulp*"
                            show ctc
                            pause
                            hide ctc
                            play sound "audio/splurt1.ogg"
                            "{i}*gulp* *gulp* *gulp* *gulp* *gulp*"
                            hide tonc_swallows
                            hide tonc
                            hide tonc_tail
                            show tonc_floats_fatbelly:
                                parallel:
                                    xpos 300
                                    linear 8.2 xpos 120
                                    linear 7.0 xpos 300
                                    repeat
                                parallel:
                                    ypos 50
                                    linear 2.0 ypos 80
                                    linear 2.4 ypos 50
                                    repeat
                            show tonc tonc00
                            with Dissolve(1.5)
                            "{i}ssso... ssso full..."
                            "{i}how... ssso much..."
                            "{i}burp, this isssn't good for my figure..."
                            "{i}...or my buoyancy..."
                            show ctc
                            pause
                            hide ctc
                            scene black with Dissolve(1.5)
                            jump bk3_next
                else:

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

                    show ctc
                    pause
                    hide ctc

                    "{i}i will comfort you...."
                    show tonb tonb03 with Dissolve(1.5)
                    show ctc
                    pause
                    hide ctc
                    "{i}don't fight me, avatar..."
                    "{i}thisss isss jussst a dream..."
                    show tonb tonb04 with Dissolve(1.5)
                    "{i}ssso enjoy the experience..."
                    show ctc
                    pause
                    hide ctc
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
                    show tonb tonb100
                    "{i}sluurp..."
                    show ctc
                    pause
                    hide ctc
                    "{i}suck... gulp... sluurp..."
                    show ctc
                    pause 
                    hide ctc
                    show tonb tonb102
                    show ctc
                    pause
                    hide ctc
                    "{i}slluuurp... sluuuurp"
                    show ctc
                    pause
                    hide ctc
                    y "I'm getting... i'm getting close..."
                    y "I'm gonna-"
                    scene black with Dissolve(1.5)
                    jump bk3_next

            "jin sex (night version)" if jin_hypno ==9:
                show tojn tojn29 with dissolve
                jin "hello, my love."
                jin "wanna fill my up?"
                jump jin_sex2

            "hypnosis room" if avatar_shack >=2:
                jump hypnosis_room

            "extra room" if avatar_shack <2:
                "your house isn't big enough for this!"
                jump inside_avatar_shack
            "exit":

                jump bk3_village_background
    else:
        menu:
            "wait until night":
                $ bk3_day = False
                jump bk3_village_background

            "hypnosis room" if avatar_shack >=2:
                jump hypnosis_room

            "extra room" if avatar_shack <2:
                "your house isn't big enough for this!"
                jump inside_avatar_shack

            "jin sex (day version)" if jin_hypno ==9:
                show tojn tojn29 with dissolve
                jin "hello, lee."
                jin "do you need a quickie, handsome?"
                jump jin_sex3
            "exit":

                jump bk3_village_background






label inside_hospital_building:
    if earthbending >=15:
        if not hospital_upgrade_talk:
            stop music
            play music "audio/Komiku_-_10_-_Something_to_save.mp3"
            scene black
            scene inside_hospital
            show toki toki01
            with dissolve
            k3 "hey, aang. we need to talk."
            k3 "but first, I need your help."
            y "with what?"
            k3 "i get the sense that we're going to be leaving soon, and the hospital is in pretty poor shape."
            k3 "i'd like to get it fully upgraded so that the people here can take care of themselves."
            k3 "can you do that for me?"
            y "and what do i get?"
            k3 "my appreciation... and some answers."
            k3 "now... will you help me?"
            menu:
                "yes":
                    y "yeah, alright."
                    y "i'll help."
                    k3 "oh, thank you!"
                    k3 "you're the best, aang!"
                    k3 "you'll need some obsidian, of course..."
                    k3 "i bet if you look around in the tunnels you can find some!"
                    k3 "oh, and I know there are some quests at the tavern..."
                    k3 "i bet at least one of those will have obsidian as a reward."
                    k3 "good luck!"
                    $ hospital_upgrade_talk = True
                    jump bk3_village_background
                "no":

                    y "not really feeling like it."
                    k3 "well. come back when you are."
                    jump bk3_village_background

        if hospital_upgrade_talk:
            if hospital_building <3:
                stop music
                play music "audio/Komiku_-_10_-_Something_to_save.mp3"
                scene black
                scene inside_hospital
                show toki toki01
                with dissolve
                k3 "hey, aang! please upgrade the hospital all the way."
                k3 "then we'll talk more."
            else:
                if bk3_handjob >=1:
                    pass
                else:
                    stop music
                    play music "audio/Komiku_-_10_-_Something_to_save.mp3"
                    scene black
                    scene inside_hospital
                    show toki toki01
                    with dissolve
                    k3 "hey, aang!"
                    k3 "you've upgraded the hospital all the way!"
                    k3 "you're amazing!"
                    k3 "alright, i promised we'd talk."
                    k3 "so, here it goes..."
                    k3 "wait."
                    k3 "let me get more comfortable."
                    jump bk3_katara_handjob

    if toph_katara_chair ==6 or toph_katara_chair ==7:
        "there's a note on the door...."
        "\"thanks for getting the key delivered! come to toph's sometime during the day!\"\n- katara"
        $ toph_katara_chair = 7
        y "this scavenger hunt better not end in a kiss on the cheek."
        jump bk3_village_background

    if toph_katara_chair >=2 and toph_katara_chair < 6:
        show screen earth_money_date
        stop music
        play music "audio/Komiku_-_10_-_Something_to_save.mp3"
        scene black
        scene inside_hospital
        show toki toki01
        with dissolve
        k3 "have you found that key?"
        y "oh, right. sure."
        k3 "thanks!"
        jump bk3_village_background

    if toph_katara_chair ==1:
        show screen earth_money_date
        stop music
        play music "audio/Komiku_-_10_-_Something_to_save.mp3"
        scene black
        scene inside_hospital
        show toki toki01
        with dissolve
        k3 "hey, aang!"
        y "yo, toph said you wanted to see me."
        y "what's up?"
        k3 "well, it's a little embarassing, but I lost the key to this cupboard."
        y "i... okay. great."
        y "let me guess what you want from me."
        k3 "the cupboard has a surprise in it... that you might enjoy."
        k3 "if you can help me find the key, i'll show it to you."
        y ".....fine."
        y "where should i start?"
        k3 "i don't know."
        k3 "it must be in the village though, i haven't been anywhere else."
        $ toph_katara_chair = 2
        jump bk3_village_background

    if naga_toph_old == 6:
        show screen earth_money_date
        stop music
        play music "audio/Komiku_-_10_-_Something_to_save.mp3"
        scene black
        scene inside_hospital
        show tolf tolf01
        with dissolve
        lf "avatar."
        y "long... feng."
        y "to what do i owe the-"
        y "wait. is this real?"
        lf "you think you can take this city from me?"
        y "um..."
        show tolf tolf02 with dissolve
        lf "i {i}am{/i} this city!"
        lf "without me, there is nothing!"
        y "does it matter if i respond?"
        lf "i'm going to rip your heart out!"
        with sshake
        "Long feng moves quickly, slashing at you with a knife taken from the folds of his robe."
        "you sense it coming and move just in time to avoid a direct hit, but the blade slices across your chest."
        "you stumble backward as long feng moves again."
        with sshake
        "he brings the knife point down on you as you kick at his chest."
        show tolf_blink
        with sshake
        lf "mghph!"
        "he manages to dig the blade into your right thigh as he topples forward."
        "you yell out, shuffling backwards, adrenaline blotting out much of the pain."
        hide tolf_blink with dissolve
        "as long feng comes at you again, you stomp your left foot down and twist up your arms-"
        "-pulling the earth up below him."
        hide tolf with sshake
        "you push your arms outward in a swift, confident motion, which forces him through the door of the hospital."

        "you wait for a moment, before hearing quickly approaching footsteps."
        ya "come on... come on you bastard..."
        show toki toki04
        show toki_angry
        with dissolve
        k3 "what is all that racket?"
        k3 "who-"
        hide toki_angry
        show toki_surprised
        with dissolve
        k3 "aang!"
        "seeing katara, the pain you were avoiding comes rushing to the surface, and you collapse."
        show toki toki03
        with dissolve
        k3 "aang! i've got you!"
        "katara reaches out to you..."
        scene black with dissolve
        "...as you fade from consciousness."
        $ naga_toph_old = 7
        show ctc
        pause
        hide ctc
        "some time passes...."
        show toki toki01
        with dissolve
        k3 "aang...."
        k3 "aang, wake up...."
        scene inside_hospital
        hide toki
        show toki toki01
        with dissolve
        k3 "are you awake?"
        y "what... where am i?"
        k3 "you're in the hospital."
        k3 "i've patched you up, but... what happened?"
        y "i got in a fight."
        k3 "here? with who?"
        y "don't worry about it."
        y "am i good to go?"
        k3 "i've healed your wounds, but..."
        k3 "i'm worried about you."
        y "and i'm worried about you."
        y "in more ways than one."
        k3 "what?"
        y "you know more than you should and don't have a good explanation."
        k3 "i... i can promise i'm here for you."
        y "not good enough."
        k3 "I... i can't. not yet."
        k3 "i made a promise."
        y "to who?"
        k3 "i can't... oh, please don't make me."
        k3 "i'm sorry."
        y "fine."
        y "thanks for healing me."
        k3 "wait, don't go..."
        $ naga_toph_old = 7
        jump bk3_village_background


    if earth_riddles ==2:
        hide screen earth_money_date
        stop music fadeout 2
        scene black with dissolve
        play music "audio/Unwritten Return.mp3"
        scene inside_hospital
        show tokt tokt10
        with dissolve
        k3 "welcome, aang."
        show ctc
        pause
        hide ctc
        k3 "i see you got my notes!"
        t "it was not *hic* my idea!"
        y "have you guys been drinking?"
        k3 "...we're not drunk."
        y "that's reassuring."
        k3 "look, there's something we want to show you."
        y "really?"
        k3 "yeah."
        k3 "toph?"
        show tokt tokt11 with dissolve
        t "we've all been going through a... stressful time..."
        t "and katara's been showing *hic* me how to unwind..."
        t "and we... just want to know what you want from us."
        y "what i want from you?"
        t "yeah..."
        t "you're in charge, so..."
        t "what...?"
        y "....."
        y "well... the photo of you two kissing doesn't cut it any more, girls."
        y "I need the real thing."
        k3 "okay...!"
        show tokt tokt16 with dissolve
        "*smooch*"
        show ctc
        pause
        hide ctc
        k3 "mmhmmm..."
        show tokt tokt12 with Dissolve(1.5)
        y "damn..."
        y "you girls are horny, huh?"
        t "mmghm.... *hic*... ngh..."
        show ctc
        pause
        hide ctc
        y "beautiful..."
        show ctc
        pause
        hide ctc
        y "i think that you girls..."
        y "...need a little release."
        y "I'm going to walk you through it, so just relax..."
        y "you're already naked, which is a perfect start."
        y "I'm just going to sit down here..."
        scene black
        scene ceiling_1
        with dissolve
        show tokt tokt01
        with dissolve
        y "fantastic view."
        y "okay, start rubbing those twats!"
        k3 "yes, love..."
        show tokt tokt02
        t "....love?"
        k3 "i... it was a... shut up..."
        show ctc
        pause
        hide ctc
        t "...am i doing it right?"
        k3 "you look so pretty, toph..."
        t "I do?"
        k3 "yes... with your pretty little pussy..."
        k3 "i've never seen one so perfect..."
        t "I wish... i wish i knew what yours was like...."
        k3 "toph..."
        k3 "give me your hand?"
        t "um.... okay...."
        show tokt tokt03 with dissolve
        k3 "now... close your eyes..."
        show tokt_blink_toph with dissolve
        k3 "now, with your other hand..."
        k3 "reach out, and..."
        show tokt tokt05 with dissolve
        t "ohh..."
        show ctc
        pause
        hide ctc
        t "is this... your..."
        t "it's so soft... and smooth..."
        show tokt_blink_katara with dissolve
        k3 "ahh... ah..."
        t "ka-katara? are you okay?"
        k3 "y-yes... ah... it's... ah..."
        k3 "your fingers... on my pussy... feel so..."
        k3 "well, here..."
        show tokt tokt06
        hide tokt_blink_toph
        with dissolve
        t "oh!"
        t "oh, katara... you're... you understand what i..."
        t "what i need..."
        show tokt tokt03
        show tokt_wetness
        show tokt tokt07
        hide tokt_blink_katara
        t "here...."
        k3 "ahh... ah..."
        t "yes..."
        show tokt_blink_katara
        show tokt_blink_toph
        with dissolve
        k3 "ohhh... i... here it... nnngh... don't... ahh..."
        t "yes... yes... yes...! yes! yes!"
        k3 "I'm gonna-"
        t "me too...!"
        with vshake
        t "aahhhh!!"
        k3 "aahh!!!!"
        y "fuck!"
        y "move those hands away, girls!"
        show tokt tokt03
        y "HNnngg! Here it comes!!"
        play sound "audio/splurt2.ogg"
        show expression "bk3/toph/mastur_kat/sperm.png"
        show expression "bk3/toph/mastur_kat/white.png"
        hide expression "bk3/toph/mastur_kat/white.png" with Dissolve(2.0)

        y "Aaaahh!!"
        y "Swap some spit girls."
        show expression "bk3/toph/mastur_kat/black.png" with Dissolve(1.5)
        hide tokt tokt02
        hide expression "bk3/toph/mastur_kat/sperm.png"
        hide tokt_fluid_katara
        hide tokt_fluid_toph

        show expression "ebackgrounds/inside_hospital.jpg"


        show tokt tokt13:
            xpos 0
            linear 3.0 xpos 10
            linear 3.0 xpos 0
            repeat

        show expression "bk3/toph/mastur_kat/kiss_hands.png"

        y "Two beautiful girls covered with my sperm kissing each other... life is good."
        show ctc
        pause
        hide ctc
        hide expression "bk3/toph/mastur_kat/kiss_hands.png"
        hide tokt tokt13
        show tokt tokt14
        show expression "bk3/toph/mastur_kat/kiss_hands.png"
        y "Goodnight, girls."
        show ctc
        pause
        hide ctc
        hide expression "ebackgrounds/ceiling_1.jpg"
        $ earth_riddles +=1
        jump bk3_village_background


    if toph_footjob:
        if toph_blackmail ==6:
            if bk3_day:
                y "katara told me to come back at night."
                jump bk3_village_background
            else:
                hide screen earth_money_date
                y "alright, i think she's in there."
                scene black
                stop music
                play music "audio/Komiku_-_10_-_Something_to_save.mp3"
                scene inside_hospital
                show toki toki01
                show toi toi09:
                    xzoom -1.0 xpos 150
                with dissolve
                k3 "be free, toph."
                k3 "stop living by the rules everyone else sets."
                k3 "do something wild."
                t "i..."
                y "looks like it's getting good."
                "you hear footsteps and clanking armor approach..."
                y "oh, shit! guards! hide!"
                scene black with dissolve
                "you and june hide around the corner of the building."
                g2 "look, we just need a disguise, i'm telling you."
                g1 "and {i}i'm{/i} telling {i}you{/i} that we need to get the fuck out of here."
                g1 "have you seen these earth soldiers?"
                g1 "these guys actually care!"
                g1 "we can't compete with that!"
                g2 "all you do is talk about the dai lee-"
                g1 "oh, right, {i}that's{/i} what they're called."
                g2 "don't act like you don't know what they're called."
                g2 "you talk about them all the time."
                g2 "what do they have that i don't? huh?"
                g2 "i fed you soup last night!"
                g1 "i didn't ask you to do that! i was asleep!"
                g2 "i just wanted to take care of you!"
                g1 "by drowning me!?"
                g2 "it was just broth! it's good for you."
                g1 "i. was. asleep. you fucking weirdo."
                g2 "i bet you wouldn't call the dai lee weirdos."
                g1 "because they'd kick my ass, probably."
                g2 "oh. i get it now."
                g2 "i'm not man enough for you."
                g1 "i... what? can we just tell the captain that the city's been successfully infiltrated?"
                g2 "wait, it has? by who?"
                g1 "by the fire nation."
                g2 "really? when?"
                g1 "you never listen. i share and i share-"
                g1 "no! i'm not getting sucked into this!"
                g1 "leave me alone!"
                g2 "Jeff! wait! i'm coming! i packed soup!"
                "the two guards scuttle off."
                y ".....i feel nostalgic."
                y "oh, shit, did we miss it?"
                scene black
                stop music
                play music "audio/Komiku_-_10_-_Something_to_save.mp3"
                with dissolve
                "you peek in through the window with your camera and notice toph and katara have progressed quickly..."
                show toph_katara_kiss
                show windowlickscene:
                    xzoom -1.0
                show ctc
                pause
                hide ctc
                y "hot damn."
                y "now i just have to take a quick photo..."
                scene black
                show photo_blackmail
                with flash
                show ctc
                pause
                hide cc
                y "there's all the evidence we need."
                "there's a flutter of movement inside..."
                scene black with dissolve
                y "you quickly hide back around the building as toph runs out."
                "after waiting a few minutes to make sure the coast is clear, you enter the hospital."
                scene black
                scene inside_hospital
                show toki toki01
                show toju toju02:
                    xzoom -1.0 xpos 150
                with dissolve
                y "what was that about?"
                k3 "she gave in and became afraid."
                k3 "did you get the picture?"
                y "I did indeed."
                k3 "and june here saw it all as well?"
                ju "i did."
                k3 "perfect."
                k3 "get some rest."
                k3 "you now have some leverage."
                scene black with dissolve
                "you head home for the night."
                $ toph_blackmail +=1
                jump bk3_next

        if toph_blackmail ==5:
            show screen earth_money_date
            stop music
            play music "audio/Komiku_-_10_-_Something_to_save.mp3"
            scene black
            scene inside_hospital
            show toki toki01
            show toju toju02:
                xzoom -1.0 xpos 150
            with dissolve
            k3 "it's about time."
            ju "what am i doing here?"
            k3 "you're going to be a witness to something."
            k3 "aang, here. take this."
            "katara hands you a camera."
            y "do you... know what this is?"
            k3 "yes, and they're very hard to come by."
            k3 "only the magazine industry has these right now, so take care of it."
            k3 "take a photo at the right moment, and toph will be right where you want her."
            k3 "she's coming by later tonight."
            if bk3_day:
                k3 "wait until evening, then come here."
            if not bk3_day:
                k3 "she could be here any moment... go outside and check back, quickly!"
            $ toph_blackmail +=1
            jump bk3_village_background

        if toph_blackmail ==4:
            "katara isn't here at the moment...."
            jump bk3_village_background

        if toph_blackmail ==3:
            show screen earth_money_date
            stop music
            play music "audio/Komiku_-_10_-_Something_to_save.mp3"
            scene black
            scene inside_hospital
            show toki toki01
            with dissolve
            k3 "good, you're here."
            k3 "it's time for the next step in blackmailing toph."
            y "you've really jumped on board this train."
            y "i'm a little surprised, to be honest."
            k3 "i'm just here to help."
            k3 "look, i'm going to invite toph at night."
            k3 "you need to get another witness."
            k3 "someone other than suki."
            k3 "got it?"
            y "get a witness other than suki."
            y "got it."
            k3 "i have to go hunt down an item."
            y "an... item?"
            k3 "yes. go get that witness."

            $ toph_blackmail +=1
            jump bk3_village_background

        if toph_blackmail ==2:
            show screen earth_money_date
            stop music
            play music "audio/Komiku_-_10_-_Something_to_save.mp3"
            scene black
            scene inside_hospital
            show toki toki01
            show tosi tosi10:
                xzoom -1.0 xpos 150
            with dissolve
            y "alright we're here-"
            y "suki, when did you get changed?"
            suki "i'm not surprised you didn't notice, i'm trained in stealth as well as combat."
            y "...fair enough."
            y "so what's the plan."
            k3 "i'm meeting toph down at the beach."
            k3 "follow me and stay hidden."
            k3 "oh, and just for fun...."
            k3 "when we're at the beach, what size boobs do you want me to have?"
            menu:
                "small":
                    $ boobs = 'small'
                "medium":
                    $ boobs = 'medium'
                "big":
                    $ boobs = 'big'

            k3 "done!"
            k3 "come on."
            scene black with dissolve
            $ toph_blackmail +=1
            jump toph_swim_blackmail

        if toph_blackmail ==1:
            show screen earth_money_date
            stop music
            play music "audio/Komiku_-_10_-_Something_to_save.mp3"
            scene black
            scene inside_hospital
            show toki toki01
            with dissolve
            k3 "go find someone to witness toph and me at the beach."
            jump bk3_village_background

        if toph_blackmail == 0:
            show screen earth_money_date
            stop music
            play music "audio/Komiku_-_10_-_Something_to_save.mp3"
            scene black
            scene inside_hospital
            show toki toki01
            with dissolve
            k3 "hey, aang! what's up?"
            y "um... i think i fucked up with toph."
            show toki toki02 with dissolve
            k3 "okay... what did you do?"
            y "she's... super pissed at me."
            y "she's figured out i'm tricking her, and doesn't seem likely to... help me anymore."
            y "learning earthbending or otherwise."
            y "which is crazy, because she was clearly enjoying it at the end!"
            y "i mean... she asked to see my dick!"
            y "any thoughts?"
            show toki_blink with dissolve
            k3 "hmm...."
            k3 "well, i think it's clear she's interested in sexual activities..."
            k3 "but really doesn't like being tricked into it."
            k3 "i think we just need to give her a reason to give in."
            k3 "you need leverage."
            y "leverage?"
            k3 "you'll need to have a way to blackmail her."
            y "...blackmail her? how?"
            k3 "well... she's worried about her parents finding her."
            k3 "that's a huge concern of hers."
            k3 "like... number one concern."
            hide toki_blink with dissolve
            k3 "she afraid of them finding her and taking her freedom away... locking her in a figurative box."
            y "i guess...."
            y "can't i just kill a mooselion or something?"
            y "i've gotten pretty good at that."
            k3 "No, Aang. Too much is at stake here."
            k3 "In fact, just this probably won't be enough."
            y "i'm sure it-"
            show toki_angry with dissolve
            k3 "that's not going to be enough, aang!"
            y "...what?"
            hide toki_angry with dissolve
            k3 "toph is... stubborn."
            k3 "{i}very{/i} stubborn."
            k3 "she might be willing to risk going back to her parents just to spite you."
            k3 "so you're going to need additional leverage."
            y "okay... like what?"
            k3 "well...."
            show toki_blink with dissolve
            k3 "in toph's home city of gaoling, there's... a forbidden activity."
            k3 "an activity that is met with being imprisoned for life."
            y "i'm listening.... what is it?"
            hide toki_blink with dissolve
            k3 "girl on girl."
            y "....girl on girl?"
            y "wait... being a lesbian is illegal?"
            y "but... that's the best!"
            y "it's practically art!"
            k3 "all the same, that's the case."
            k3 "if toph was caught engaging in a lesbian act, she would be imprisoned for life."
            k3 "and toph values freedom above all else."
            y "okay... okay..."
            y "so she definitely wouldn't risk her parents finding her if prison is the result."
            y "so now i've got to find someone willing to...."
            k3 "....."
            y "hey. so. katara..."
            show toki_blink with dissolve
            k3 "yes, i'll do it."
            hide toki_blink with dissolve
            k3 "luckily, i already started buttering her up, remember?"
            y "wait... is this the thing i was going to ask you?"
            show toki_smile
            show toki_blink
            with dissolve
            k3 "maaaybe...."
            y "how did you know? i didn't even know!"
            hide toki_blink with dissolve
            k3 "heehee."
            hide toki_smile with dissolve
            k3 "this is going to take some coordination, though."
            k3 "first, go get a witness and come back here."
            k3 "once you've gotten someone, you can follow toph and i to the beach, and spy on us."
            k3 "got it?"
            y "yeah, but..."
            y "i'm feeling really guilty about this."
            show toki_blink with dissolve
            k3 "*sigh...*"
            k3 "look, we're protecting the world."
            k3 "and toph's actually into it, anyway."
            hide toki_blink with dissolve
            k3 "we just have to help her see that giving into her... desires... is the most beneficial course."
            k3 "she may fight it, and she may act like she doesn't like it..."
            k3 "but trust me, give her a reason, and she'll start caving."
            y "...okay. i'll trust you."
            k3 "good."
            k3 "now what are you going to do?"
            y "i need to get someone to come spy on you and toph, and come back here."
            k3 "exactly."
            $ toph_blackmail +=1
            k3 "good luck!"
            jump bk3_village_background


    if market_stroll ==2:
        if suki_hospital == 3:
            show screen earth_money_date
            stop music
            play music "audio/Komiku_-_10_-_Something_to_save.mp3"
            scene black
            scene inside_hospital
            show toki toki01
            with dissolve
            k3 "let me make sure you're healthy, aang."
            k3 ".....there you go."
            $ bk3_fire_remaining = bk3_moves
            $ bk3_water_remaining = bk3_moves
            $ bk3_ypos_lifebar_player = 0
            k3 "at least {i}try{/i} not to get hurt."
            k3 "want to buy any potions?"
            jump bk3_village_hospital_menu

        if suki_hospital ==2:
            show screen earth_money_date
            stop music
            play music "audio/Komiku_-_10_-_Something_to_save.mp3"
            scene black
            scene inside_hospital
            show toki toki01
            show tosi tosi01:
                xzoom -1.0
            with dissolve

            if avatar_shack >= 2:
                if not suki_hypno_talk:
                    y "hey, i've got the hypnosis room up and functional."
                    y "want to stop by, suki?"
                    show tosi_smile:
                        xzoom -1.0
                    suki "sure, let's do it."
                    suki "i'll come by later."
                    $ hypnoroom = "suki"
                    $ suki_hypno_talk = True
                    jump bk3_village_background
                else:
                    show screen earth_money_date
                    stop music
                    play music "audio/Komiku_-_10_-_Something_to_save.mp3"
                    scene black
                    scene inside_hospital
                    show toki toki01
                    show tosi tosi01:
                        xzoom -1.0
                    with dissolve
                    menu:
                        "talk to suki":
                            suki "what's up?"
                            menu:
                                "hypno-room appointment":
                                    if suki_hypno_today:
                                        y "(i already hypnotized her once today, i shouldn't push it...)"
                                        y "nevermind."
                                        suki "okay."
                                        jump bk3_village_background
                                    else:
                                        if suki_hypno >=4:
                                            y "up for another session?"
                                            suki "not right now.... hey, have you seen any brothels around?"
                                            jump bk3_village_background
                                        if hypnoroom == "none":
                                            y "i think you should come by my place and we'll do some hypno therapy."
                                            suki "hmm... okay, aang!"
                                            $ hypnoroom = "suki"
                                            jump bk3_village_background
                                        if hypnoroom == "suki":
                                            y "I'm still waiting on you to get over to the hypno-room."
                                            suki "well, i'm waiting on you for the same thing!"
                                            y "oh. erm. whatever."
                                            jump bk3_village_background
                                        else:
                                            y "crap, i've got a session with june to do first."
                                            y "nevermind, suki."
                                            suki "oh... okay."
                                            jump bk3_village_background
                                "run the brothel" if brothel_built:

                                    if suki_hypno >=4:
                                        y "suki."
                                        suki "yes?"
                                        y "[trigger]."
                                        show tosi_hypno_eyes:
                                            xzoom -1.0
                                        with dissolve
                                        suki "......."
                                        y "you will run the brothel."
                                        suki "i will run the brothel."
                                        y "good girl."
                                        y "get over there right now."
                                        suki "yes, sir. thank you, sir."
                                        hide tosi_hypno_eyes
                                        hide tosi tosi01
                                        with dissolve
                                        $ suki_hospital = 3
                                        y "sweet."
                                        k3 "well... that's coming along well."
                                        y "right?"
                                        y "actually, i think you and i need to talk soon."
                                        y "about what's going on-"
                                        k3 "goodnight, aang."
                                        hide toki toki01 with dissolve
                                        y ".........."
                                        y "fine. later, then."
                                        $ suki_brothel = True
                                        jump bk3_village_background

                                    if suki_hypno >=1:
                                        y "suki, i need someone to run the brothel."
                                        y "you in?"
                                        show tosi_angry:
                                            xzoom -1.0
                                        with dissolve
                                        suki "of course not!"
                                        menu:
                                            "try again later":
                                                y "aw..."
                                                jump inside_hospital_building
                                            "\"[trigger]\"":
                                                pass
                                        y "[trigger]."
                                        hide tosi_angry
                                        show tosi_hypno_eyes:
                                            xzoom -1.0
                                        with dissolve
                                        suki "......."
                                        y "you will run the brothel."
                                        suki "i... will run...."
                                        suki "nnn... no.... wh..."
                                        hide tosi_hypno_eyes
                                        show tosi_blink:
                                            xzoom -1.0
                                        with dissolve
                                        suki "what's going on...?"
                                        y "aw..."
                                        y "don't worry about it."
                                        jump inside_hospital_building

                                    if suki_hypno < 1:
                                        show tosi_angry:
                                            xzoom -1.0
                                        with dissolve
                                        suki "no way!"
                                        y "aw..."
                                        jump inside_hospital_building
                                "back":
                                    jump inside_hospital_building
                        "talk to katara":

                            k3 "let me make sure you're healthy, aang."
                            k3 ".....there you go."
                            $ bk3_fire_remaining = bk3_moves
                            $ bk3_water_remaining = bk3_moves
                            $ bk3_ypos_lifebar_player = 0
                            k3 "at least {i}try{/i} not to get hurt."
                            k3 "want to buy any potions?"
                            jump bk3_village_hospital_menu
                        "exit":

                            jump bk3_village_background
            else:

                k3 "let me make sure you're healthy, aang."
                k3 ".....there you go."
                $ bk3_fire_remaining = bk3_moves
                $ bk3_water_remaining = bk3_moves
                $ bk3_ypos_lifebar_player = 0
                k3 "at least {i}try{/i} not to get hurt."
                k3 "want to buy any potions?"
                jump bk3_village_hospital_menu

        if suki_hospital ==1:
            stop music
            play music "audio/Komiku_-_10_-_Something_to_save.mp3"
            scene black
            scene inside_hospital
            show toki toki02
            with dissolve
            k3 "welcome back."
            k3 "suki! look who's here!"
            show toki_blink
            show tosi tosi01:
                xzoom -1.0
            with dissolve
            suki "oh, hi."
            suki "um... katara told me i have you to thank for rescuing me."
            y "well-"
            suki "i had some crazy hallucinations in the tunnels."
            y "hallucinations?"
            y "like what?"
            suki "well, it's embarrassing, but..."
            show tosi_blush:
                xzoom -1.0
            show tosi_blink:
                xzoom -1.0
            with dissolve
            suki "i had this crazy dream that we did something... sexual."
            y "really? weird!"
            y "what was it?"
            hide tosi_blink
            with dissolve
            suki "I don't really want to get into it, i'm just glad it wasn't real."
            y "well...."
            suki "what?"
            y "it might have been."
            hide toki_blink
            show toki_angry
            with dissolve
            k3 "aang...."
            y "it could have been feng."
            hide toki_angry

            show toki_blink
            with dissolve
            k3 "oh."
            show tosi tosi03:
                xzoom -1.0
            with dissolve
            suki "oh?"
            y "yeah, it was him that chained you up, right?"
            y "maybe... he did some weird things to you while you were down there."
            y "look, i'm working on this hypnosis room for my house."
            y "i think i can help undo feng's influence on you."
            y "you don't want to start giving blowjobs at a snap of fingers, right?"
            suki "i definitely don't want that to happen."
            show tosi tosi01:
                xzoom -1.0
            with dissolve
            suki "so... yeah, i'll take you up on that."
            y "great. get some rest, i'll check in with you later."
            suki "thanks, aang!"
            $ suki_hospital = 2
            jump bk3_village_background

        if suki_free and suki_hospital ==0:
            stop music
            play music "audio/Komiku_-_10_-_Something_to_save.mp3"
            scene black
            scene inside_hospital
            show toki toki01
            with dissolve
            k3 "hey, aan-"
            show toki toki04
            show toki_surprised
            with dissolve
            k3 "suki!"
            show toki toki03
            show toki_angry
            with dissolve
            k3 "help me put down over here!"
            show black with dissolve
            show ctc
            pause
            hide ctc
            hide black
            show toki toki02
            with dissolve
            k3 "so, what the hell happened!?"
            y "she ate a bunch of magic mushrooms and went crazy."
            y "she thought i was long feng and attacked me."
            hide toki_angry with dissolve
            k3 "she attacked you?"
            hide toki_surprised with dissolve
            k3 "i'm impressed, she's a formidable opponent."
            show toki_blink with dissolve
            k3 "now what did you do?"
            y "what? i didn't-"
            show toki_angry
            hide toki_blink
            with dissolve
            k3 "{i}what did you do?"
            if suki_sexual_favor:
                y "i..."
                y "...."
                y "...i may have rubbed my dick on her face...."
                y "and then jizzed on it."
                show toki_blink with dissolve
                k3 "damn it, aang!"
                k3 "........"
                hide toki_blink with dissolve
                k3 "........."
                show toki toki01
                hide toki_angry
                show toki_smile
                with dissolve
                k3 "aw, i can't stay mad at you."
                show toki_blink with dissolve
                k3 "you were just doing what came naturally."

            if not suki_sexual_favor:
                y "nothing!"
                k3 "....."
                show toki toki01
                hide toki_angry
                show toki_smile
                with dissolve
                k3 "okay, i believe you."
            k3 "well..."
            hide toki_blink
            hide toki_smile
            show toki toki02
            with dissolve
            k3 "i'll take care of her."
            yc "she's going to be {i}pissed{/i} at me when she wakes up."
            show toki_blink with dissolve
            k3 "i said i'd take care of her."
            y "don't... don't kill her."
            y "i try not to kill anything with nipples."
            hide toki_blink with dissolve
            k3 "...you know men have nipples, right?"
            y "they {i}do{/i}!?"
            ya "shit!"
            k3 "....you have nipples! why would you think that-"
            ya "i thought i was unique because i'm the avatar!"
            ya "i've been a chick! i assumed it was spill-over!"
            k3 "i don't have time for this, aang."
            k3 "i'll make sure suki is okay and... understands... her situation."
            y "okay, i'm still confused about what that means, but i'm just going to trust you."
            k3 "good plan."
            show toki_blink with dissolve
            k3 "now scoot!"
            scene black with dissolve
            "you head home for the night."
            $ suki_hospital = 1
            jump bk3_next


        if toph_massage ==3:
            stop music
            play music "audio/Komiku_-_10_-_Something_to_save.mp3"
            scene black
            scene inside_hospital
            show toki toki01
            with dissolve
            k3 "what's up, sexy?"
            y "first: i like that."
            y "second: i need your help with toph."
            show toki toki02
            show toki_blink
            with dissolve
            k3 "*sigh...*"
            k3 "what do you need?"
            y "i need you to waterbend her boobs bigger for a very short amount of time."
            hide toki_blink
            with dissolve
            k3 "....what?"
            y "you want me to do... what i have to, right?"
            k3 "....well...yes..."
            y "okay, seriously, what do you know about my mission?"
            show toki_blink with dissolve
            k3 ".....i know that you're trying to stop the fire nation-"
            y "no, my other mission."
            hide toki_blink with dissolve
            k3 "............"
            k3 ".........................."
            show toki_blink with dissolve
            k3 "what other mission?"
            y "okay, fine, be that way."
            y "will you help?"
            k3 "yes, hold on, i'll do it from here...."
            show toki toki03
            show toki_blink
            with dissolve
            with vshake
            show ctc
            pause
            hide ctc
            k3 ".............there."
            hide toki_blink with dissolve
            k3 "her breasts are currently large."
            k3 "i don't intend to do this regularly for you."
            show toki toki02 with dissolve
            k3 "so make the most of this."
            y "I will!"
            k3 "good luck."
            $ toph_massage +=1
            jump bk3_village_background

        show screen earth_money_date
        stop music
        play music "audio/Komiku_-_10_-_Something_to_save.mp3"
        scene black
        scene inside_hospital
        show toki toki01
        with dissolve
        k3 "let me make sure you're healthy, aang."
        k3 ".....there you go."
        $ bk3_fire_remaining = bk3_moves
        $ bk3_water_remaining = bk3_moves
        $ bk3_ypos_lifebar_player = 0
        k3 "at least {i}try{/i} not to get hurt."
        k3 "want to buy any potions?"
        jump bk3_village_hospital_menu

        label bk3_village_hospital_menu:
            menu:
                "iroh's missing panties" if iroh_panty_hunt ==2:
                    y "hey... any chance you stole iroh's panties?"
                    k3 "he wears panties?"
                    y "no, he just steals them."
                    k3 "that seems... not better."
                    y "i don't... i'm not justifying it."
                    y "have you seen them or not?"
                    k3 "nope, sorry."
                    y "alright..."
                    jump bk3_village_hospital_menu

                "blowjob" if earthbending >= 4:
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
                            jump bk3_village_background
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
                            jump bk3_village_background
                "life potion - 30":

                    if emoney >=30:
                        $ emoney -=30
                        $ bk3_lifepotions += 1
                        play sound "audio/win2.mp3"
                        "you got a life potion!"
                        jump bk3_village_hospital_menu
                    else:
                        "not enough money..."
                        jump bk3_village_hospital_menu
                "mana potion - 20":

                    if emoney >=20:
                        $ emoney -=20
                        $ bk3_manapotions += 1
                        play sound "audio/win2.mp3"
                        "you got a mana potion!"
                        jump bk3_village_hospital_menu
                    else:
                        "not enough money..."
                        jump bk3_village_hospital_menu
                "no thanks":

                    k3 "okay..."
                    jump bk3_village_background

    if market_stroll ==1:
        if not bk3_day:
            "the doors are locked."
            jump bk3_village_background
        else:

            stop music
            play music "audio/Komiku_-_10_-_Something_to_save.mp3"
            scene black
            scene inside_hospital
            show toi toi04:
                xzoom -1.0
            show thankful_girl
            with dissolve
            t "hey, aang."
            "girl" "hello, aang! ready for our walk?"
            y "yeah, but..."
            y "look, i haven't said anything, but..."
            y "you know you're naked, right?"
            "girl" "oh, i'm a nudist."
            "girl" "this is how we are intended to be."
            y "...with your tits out?"
            "girl" "yes."
            y "well, whatever milks your udders."
            "girl" "....."
            t "let's go."
            jump follow_feng

    if got_posters and market_stroll <1:
        stop music
        play music "audio/Komiku_-_10_-_Something_to_save.mp3"
        scene black
        scene inside_hospital
        show toi toi04:
            xzoom -1.0
        show thankful_girl
        with dissolve
        t "hey, you're back."
        t "any luck?"
        y "yeah, here."
        "you hand the poster to the girl."
        "girl" "oh... this... yes... it's... coming back..."
        "girl" "i... did see this."
        "girl" "i remember... darkness... and stone..."
        y "the tunnels."
        "girl" "yes, i suppose."
        t "that's great news!"
        y "how?"
        t "now we know where appa is."
        y "i guess so."
        y "also, i ran into joo dee."
        y "she's acting super weird."
        y "even weirder than usual."
        t "hmm..."
        t "well, if she makes life difficult for us, we can always punch her."
        y "that's... one option. sure."
        t "so, girl, you don't remember anything before the tunnels?"
        "girl" "no, i'm afraid."
        t "hmmmm...."
        y "what?"
        t "i think you should take her to the market tomorrow."
        y "really? why?"
        t "the last thing she remembers is walking the city streets before being captured."
        t "maybe walking in the market will trigger her memories."
        y "guess it's worth a try."
        y "wanna go for a walk tomorrow?"
        "girl" "okay."
        y "guess i'll see you back here tomorrow."
        y "we'll start here and walk over there."
        "girl" "okay. see you then."
        $ market_stroll = 1
        $ bk3_day = False
        jump bk3_village_background


    if get_posters and not got_posters:
        stop music
        play music "audio/Komiku_-_10_-_Something_to_save.mp3"
        scene black
        scene inside_hospital
        show toi toi09:
            xzoom -1.0
        show thankful_girl
        with dissolve
        t "go get those posters from our house in the city."
        jump bk3_village_background

    if heal_maze_girl and not get_posters:
        stop music
        play music "audio/Komiku_-_10_-_Something_to_save.mp3"
        scene black
        scene inside_hospital
        show toi toi09:
            xzoom -1.0
        show toki toki01
        with dissolve
        k3 "okay, let's see what we can do here..."
        show toki toki03
        show toki_blink
        with dissolve
        show ctc
        pause
        hide ctc
        scene black with dissolve
        "katara works carefully, and the girl's fever breaks."
        scene black
        scene inside_hospital
        show toi toi09:
            xzoom -1.0
        show toki toki01
        with dissolve
        k3 "there..."
        k3 "that should do it."
        k3 "i'll leave her in your hands, but..."
        k3 "....don't stress her too hard."
        k3 "she needs some recovery time."
        hide toki toki01 with dissolve
        t "....."
        show toi toi01:
            xzoom -1.0
        with vshake
        t "wake up, girl!"
        y "easy, toph."
        show thankful_girl with dissolve
        "girl" "where... am i?"
        show toi toi09:
            xzoom -1.0
        with dissolve
        y "you're in a hospital."
        y "that we built."
        y "specifically for you."
        y "so.... you are fucking welcome for that."
        "girl" "thank you..."
        t "what can you remember?"
        "girl" "nothing..."
        "girl" "the last thing i remember was walking through the city, and then... waking up here."
        y "we found you in some tunnels."
        y "do you not remember that?"
        "girl" "no... i'm sorry."
        "girl" "...wait."
        "girl" "i remember.. something white and fluffy..."
        show toi toi04:
            xzoom -1.0
        with dissolve
        t "appa!"
        t "it must be!"
        "girl" "i'm sorry, it's all so blurry..."
        show toi toi50:
            xzoom -1.0
        with dissolve
        t "aang, i think we still have some posters back at our house in the city."
        y "the one we got kicked out of?"
        t "yeah. go back and grab one of those."
        t "it might jog her memory."
        y "....that's cool, i'm not terrified of waking up brainwashed under a lake or anything."
        y "i'll go by myself."
        t "good."
        y "......."
        $ get_posters = True
        jump bk3_village_background
    "the doors are locked."
    jump bk3_village_background

label inside_tophs_home:
    if bk3_handjob >=1:
        if appa_free and not toph_free:
            y "i need to rescue toph from the tunnels."
            jump bk3_village_background
        if toph_free and not appa_free:
            y "i need to rescue appa from the tunnels."
            jump bk3_village_background
        if not toph_free and not appa_free:
            y "i've got to rescue toph."
            jump bk3_village_background

    if toph_footjob:

        if toph_blackmail ==7:
            hide screen earth_money_date
            show toi toi07 with dissolve
            t "hey, kata-"
            show toi toi06 with dissolve
            t "oh. it's you."
            t "what do you want?"
            y "I just want to talk."
            t "not interested."
            y "trust me, you want to hear this."
            y "and you want to hear it in privacy."
            t "...."
            t "fine, come in."
            scene black with dissolve
            if bk3_day:
                scene bg_bk3_tophome_day
            if not bk3_day:
                scene bg_bk3_tophome_night
            show toi toi06
            with dissolve
            t "alright, i let you in."
            t "what do you want?"
            y "i want you to keep helping me."
            y "believe it or not... us... working together... helps."
            y "so... i want another footjob."
            show toi toi05 with dissolve
            t "get out of my house!"
            y "no."
            t "then i'm gonna bust your face in."
            y "no. you won't."
            t "...what?"
            y "*sigh...*"
            y "well, if you're not willing to help me freely..."
            y "....your parents miss you dearly, you know."
            show toi toi06 with dissolve
            t "what did you say?"
            y "i was just thinking... maybe i should let them know where you are."
            y "so they can come and get you."
            y "since you're not actually interested in helping the avatar."
            show toi toi05 with dissolve
            t "that wasn't helping!"
            t "that was... well, i don't know what it was!"
            y "so you don't want them to know where you are?"
            show toi toi06 with dissolve
            t "no, i don't want them to know where i am!"
            y "then you should... keep helping me."
            t "......."
            t "................"
            t "no."
            t "no, i'm not going to let you... use me..."
            t "just because my parent's will-"
            y "find out you're nakedly kissing girls?"
            show toi toi10 with dissolve
            t "I...."
            show toi toi06
            show toi_blush
            with dissolve
            t "how did you find out about that!?"
            y "katara told me."
            show toi toi05
            hide toi_blush
            show toi_blush
            with dissolve
            t "what!?"
            t "she wouldn't!"
            y "well, she did."
            show toi toi10
            hide toi_blush
            with dissolve
            t "no...."
            y "and i have two witnesses..."
            y "and a picture."
            y "so..."
            y "i'll let you decide what you want."
            y "help the avatar? or be imprisoned for life?"
            show toi toi05 with dissolve
            t "you...."
            show toi toi11
            with dissolve
            t "you monster...."
            y "you've left me no choice."
            t "how could katara-"
            y "hey. focus."
            y "stop crying."
            menu:
                "shove her to the floor":
                    "you forcibly shove toph to the floor."
                "demand she sit":
                    y "sit!"
            $ toph_blackmail +=1
            jump toph_footjob2


        if toph_blackmail <=6:
            "you knock but get no answer."
            y "i should see katara about getting some leverage on toph."
            jump bk3_village_background

    if market_stroll ==2:

        if not bk3_day:
            if toph_blackmail ==8:
                if earthbending >=11 and not toph_blowjob:
                    jump toph_blowjob1
                if earth_riddles >=3 and not toph_sex:
                    jump toph_sex1
                if toph_drink_talk and toph_public >=10 and not toph_drunk1:
                    jump toph_drinking

                hide screen earth_money_date
                scene black
                scene bg_bk3_tophome_night
                show toi toi04
                with dissolve
                if toph_slut >=5 and nagina_free:
                    if not toph_slut_news:
                        $ toph_slut_news = True
                        "toph is now a full slut!"
                        t "hey, sexy!"
                        t "need your cock sucked?"
                        $ toph_greeting = True
                    else:
                        t "hey, sexy!"
                        t "need your cock sucked?"
                        $ toph_greeting = True
                else:
                    if not toph_greeting:
                        t "hey, [bk3name]!"
                        t "what's up?"
                        $ toph_greeting = True

                menu:

                    "toph broken status" if nagina_free:
                        if toph_slut <=4:
                            "[toph_slut]/5"
                        else:
                            "toph is a full slut!"
                        jump inside_tophs_home
                    "refer to me as...":
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
                            "user input":

                                $ bk3name = renpy.input("(enter name)", default='aang', allow=None, exclude='{}', length=25, with_none=None, pixel_width=None)
                                $ bk3name = bk3name.strip()
                                if bk3name == "":
                                    $ bk3name="aang"
                        t "of course... [bk3name]."
                        jump inside_tophs_home
                    "tit massage":

                        $ toph_greeting = False
                        jump tit_massages
                    "titfuck":

                        $ toph_greeting = False
                        "have katara bend toph's tits before fucking them?"
                        menu:
                            "small tits":
                                $ toph_boobjob_tits = 'small'
                                jump toph_titfuck2
                            "big tits":

                                $ toph_boobjob_tits = 'big'
                                jump toph_titfuck2
                    "footjob (version 1)":

                        $ toph_greeting = False
                        if not toph_slut_news:
                            if not toph_footslut1:
                                $ toph_footslut1 = True
                                $ toph_slut +=1
                            jump toph_footjob1_2
                        else:
                            jump toph_footjob1_3
                    "footjob (version2)":

                        $ toph_greeting = False
                        if not toph_slut_news:
                            if not toph_footslut2:
                                $ toph_footslut2 = True
                                $ toph_slut +=1
                            jump toph_footjob2_2
                        else:
                            jump toph_footjob2_3

                    "blowjob" if toph_blowjob:
                        $ toph_greeting = False
                        if not toph_slut_news:
                            if not toph_blowslut:
                                $ toph_blowslut = True
                                $ toph_slut +=1
                            jump toph_blowjob2
                        else:
                            jump toph_blowjob3

                    "sex" if toph_sex:
                        $ toph_greeting = False
                        if not toph_slut_news:
                            if not toph_sexslut:
                                $ toph_sexslut = True
                                $ toph_slut +=1
                            jump toph_sex2
                        else:
                            jump toph_sex3

                    "anal" if toph_tunnel_training >=3:
                        $ toph_greeting = False
                        if not toph_slut_news:
                            if not toph_analslut:
                                $ toph_analslut = True
                                $ toph_slut +=1
                            jump toph_anal2
                        else:
                            jump toph_anal3
                    "exit":

                        $ toph_greeting = False
                        jump bk3_village_background

            menu:
                "visit toph" if earthbending >=5:
                    hide screen earth_money_date
                    if nagina_free:
                        hide screen earth_money_date
                        show bg_bk3_tophome_day
                        show toi toi50
                        with dissolve
                        t "whenever you're ready to leave this place for good, go visit the palace."
                        t "but make sure you've talked to everyone... you never know who has something new going on."
                    if earthbending >=9 and not toph_footjob:
                        show toi toi04 with dissolve
                        t "come on in."
                        jump toph_footjob1

                    if earthbending >=7 and toph_massage >=4 and not toph_titjob:
                        t "come on in...."
                        $ toph_boobjob_tits = 'small'
                        jump toph_titfuck

                    if toph_titjob:
                        menu:
                            "titfuck":
                                "have katara bend toph's tits before fucking them?"
                                menu:
                                    "small tits":
                                        $ toph_boobjob_tits = 'small'
                                        jump toph_titfuck2
                                    "big tits":

                                        $ toph_boobjob_tits = 'big'
                                        jump toph_titfuck2
                            "tit massage":

                                pass
                            "exit":

                                jump bk3_village_background

                    if toph_massage >=5:
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

                    if toph_massage ==4:
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
                        show toma_angry
                        hide toma_smile
                        with dissolve
                        t "what!?"
                        y "not yet, anyway."
                        y "we'll need to keep working on them if they're going to get bigger."
                        show toma_uncertain
                        hide toma_angry
                        with dissolve
                        t "oh."
                        t "then.... go ahead."
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
                        t "this is still so embarassing"
                        show toma_kneadtits:
                            ypos 20
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
                        show toma_scissortits:
                            ypos 20
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
                        y "...with something special this time."
                        show toma toma03 with dissolve
                        t "....what?"
                        y "well...."
                        "you pull your cock out of your pants."
                        show toma_angry
                        hide toma_uncertain
                        with dissolve
                        t "what's going on, aang? did you... did you do something...?"
                        t "what are you going to do?"
                        y "what i have to."
                        y "i don't want to do this either, but we don't have much of a choice."
                        t "what... what is it?"
                        y "the special ingredient.... is sperm."
                        t ".........."
                        show toma_uncertain
                        hide toma_angry
                        show toma_blink
                        with dissolve
                        t "fine, but i'm going to look away...."
                        t "...it's not like i can see it anyway."
                        y "no, you have to."
                        hide toma_blink with dissolve
                        t "what? why?"
                        y "because we're doing this for you, and it's part of the whole experience."
                        y "if i have to do this, you have to face me."
                        y "in fact... i want you to say please."
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
                        t "i'm going to kick your butt, you pansy-"

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


                    if toph_massage ==3:
                        y "toph decided to stop the massages."
                        y "i'm going to need to convince katara to bend toph's boobs larger briefly..."
                        y "...so it seems like it's having an effect."
                        jump bk3_village_background

                    if toph_massage ==2:

                        hide screen earth_money_date
                        show toi toi09
                        with dissolve
                        t "come on in..."
                        hide toi toi09 with dissolve
                        scene black
                        scene bg_bk3_tophome_night
                        show toi toi09
                        with dissolve
                        t "so-"
                        y "tonight we're going a step further."
                        show toi_blush with dissolve
                        t "we... we are?"
                        show toi_blink
                        hide toi_blush
                        show toi_blush
                        with dissolve
                        y "yes, you need to take your shirt off if we're going to start seeing some change."
                        show toi toi06
                        with dissolve
                        t "......."
                        show toi toi09
                        show toi_blink
                        with dissolve
                        t "i'm not sure about that..."
                        hide toi_blink with dissolve
                        y "fine, i'll go-"
                        t "wait!"
                        scene black
                        scene bg_bk3_tophome_night

                        show toma toma01
                        show toma_blink_ani
                        with dissolve
                        t "If you need to..."
                        t "........."
                        hide toma toma01
                        hide toma_blink_ani
                        with dissolve
                        $ toph_massage_nude = True
                        show toma toma01
                        show toma_blink_ani
                        with dissolve
                        t "go.... go ahead...."
                        show ctc
                        pause
                        hide ctc
                        y "arms up, toph."
                        show toma toma03 with dissolve
                        t "o-okay."
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
                        t "so what are-"
                        show toma_kneadtits
                        with dissolve
                        t "...oh...uh..."
                        show ctc
                        pause
                        hide ctc
                        t "i'm not sure this is helping."
                        show ctc
                        pause
                        hide ctc
                        y "trust me, we're getting close."
                        show toma toma01 with dissolve
                        t "..........."
                        show ctc
                        pause
                        hide ctc
                        y "yeah..."
                        show toma_scissortits
                        hide toma_kneadtits
                        show ctc
                        pause
                        hide ctc
                        show toma_blink with dissolve
                        t "ow... mmmgh..."
                        y "did you just moan?"
                        show toma toma03
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


                        y "now i just need to give them a rub down."
                        show toma_rubtits:
                            ypos 0
                            linear 2.0 ypos -30
                            ypos -30
                            linear 2.0 ypos 0
                            repeat

                        show ctc
                        pause
                        hide ctc
                        "after you finish slapping toph's little tits, you rub them eagerly."
                        "her soft, tiny breasts move under the firm pressure of your hands."
                        hide toma_rubtits with dissolve

                        t "that's it!"


                        show toma toma01
                        hide toma_uncertain
                        show toma_angry
                        hide toma_blink
                        with Dissolve(1.0)
                        t "no more!"
                        y "...what?"
                        show expression "screen_red.png":
                            alpha 1.0
                            linear 2.0 alpha 0.0
                        show toma toma25
                        hide toma_smile
                        ya "oww!!!"
                        t "you have cold hands! and i'm not seeing any improvement!"
                        show toma toma26
                        t "this is obviously a waste of time."
                        hide expression "screen_red.png"
                        show toma_uncertain with dissolve
                        t "I'm... sorry i bothered you with this, aang."
                        hide toma toma26
                        hide toma_uncertain
                        hide toma_angry
                        hide toma_blush
                        hide toma_blink_ani
                        with dissolve
                        $ toph_massage +=1
                        $ toph_massaged = True
                        y "....shit."
                        y "maybe i can get katara to help me with toph."
                        y "I think katara's at the hospital."
                        scene black with dissolve
                        "you go home for the night."
                        jump bk3_next

                    if toph_massage >0 and toph_massage <=1:

                        hide screen earth_money_date
                        show toi toi09
                        with dissolve
                        t "come on in..."
                        hide toi toi09 with dissolve
                        scene black
                        scene bg_bk3_tophome_night
                        show toi toi09
                        with dissolve
                        t "..........."
                        t "so...."
                        show toi_blush with dissolve
                        t "do you want to..."
                        show toi_blink
                        hide toi_blush
                        show toi_blush
                        with dissolve
                        t "...give me another breast massage?"
                        show toi toi06
                        with dissolve
                        t "......."
                        show toi toi09
                        show toi_blink
                        with dissolve
                        t "i wish they bigger..."
                        hide toi_blink with dissolve
                        y "hmm...."
                        y "I'll get started."
                        y "come over here."
                        t ".........."
                        scene black
                        scene bg_bk3_tophome_night
                        show toma toma01
                        show toma_blink_ani
                        with dissolve
                        t "so...."
                        show ctc
                        pause
                        hide ctc
                        t "....what are we doing?"
                        y "i need you to put your arms up."
                        show toma toma03 with dissolve
                        y "yeah, like that."
                        hide toma_angry
                        hide toma_blush
                        show toma_uncertain
                        show toma_blush
                        with dissolve
                        t "I... i want big ones, like katara...."
                        show toma_blink with dissolve
                        y "i'll do my best."
                        hide toma_blink with dissolve
                        t "............"
                        show toma toma03 with dissolve
                        t "so what are-"
                        show toma_kneadtits
                        with dissolve
                        t "...oh...uh..."
                        show ctc
                        pause
                        hide ctc
                        t "i'm not sure this is helping."
                        show ctc
                        pause
                        hide ctc
                        y "trust me, it'll take a bunch of sessions, but it'll work."
                        show toma toma01 with dissolve
                        t "..........."
                        show ctc
                        pause
                        hide ctc
                        y "yeah..."
                        show toma_scissortits
                        hide toma_kneadtits
                        show ctc
                        pause
                        hide ctc
                        t "you're... kind of... pinching my... nipples..?"
                        show toma toma03
                        show toma_angry
                        show toma_blink
                        with dissolve
                        t "is... this really needed...?"
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

                                menu:
                                    "give her another five slaps for good measure":

                                        $ titslap_counter = 5
                                    "This should be enough":
                                        pass


                        y "now i just need to give them a rub down."
                        show toma_rubtits:
                            ypos 0
                            linear 2.0 ypos -30
                            ypos -30
                            linear 2.0 ypos 0
                            repeat

                        show ctc
                        pause
                        hide ctc
                        "after you finish slapping toph's little tits, you rub them eagerly."
                        "her soft, tiny breasts move under the firm pressure of your hands."
                        hide toma_rubtits with dissolve

                        y "Looks like my work here is done! For now."


                        show toma toma01
                        hide toma_uncertain
                        show toma_smile
                        hide toma_blink
                        with Dissolve(1.0)
                        t "Thanks Aang, i... i hope i'll get some big breasts..."
                        t "but one last thing..."
                        show expression "screen_red.png":
                            alpha 1.0
                            linear 2.0 alpha 0.0
                        show toma toma25
                        hide toma_smile
                        ya "oww!!!"
                        t "WARN ME NEXT TIME YOU PINCH MY NIPPLES!"
                        show toma toma26
                        y "......"
                        y "But it felt good, right?"
                        t "That's beside the point."
                        y "okay, well, you be mad about me helping you, and i'll see you later."
                        hide expression "screen_red.png"
                        show toma_uncertain with dissolve
                        t "I'm... sorry, aang."
                        y "no worries, i'll see you later."
                        $ toph_massage +=1
                        $ toph_massaged = True
                        scene black with dissolve
                        "you head home for the night."
                        jump bk3_next

                    if toph_massage ==0:
                        $ toph_massaged = True
                        hide screen earth_money_date
                        show toi toi09
                        with dissolve
                        t "come on in..."
                        hide toi toi09 with dissolve
                        scene black
                        scene bg_bk3_tophome_night
                        show toi toi09
                        with dissolve
                        t "..........."
                        y "what's up?"
                        t "so...."
                        show toi_blush with dissolve
                        t "did you see..."
                        show toi_blink
                        hide toi_blush
                        show toi_blush
                        with dissolve
                        t "...anything? down at the lake?"
                        y "you mean your itty bitty titties?"
                        show toi toi06
                        with dissolve
                        t "......."
                        show toi toi09
                        show toi_blink
                        with dissolve
                        t "i wish they were bigger..."
                        hide toi_blink with dissolve
                        t "i'd give anything to have them be as big as katara's."
                        t "she won't waterbend my boobs bigger, though."
                        show toi_blink with dissolve
                        y "hmm...."
                        y "I might be able to do something about them."
                        hide toi_blink with dissolve
                        t "can you bend my boobs bigger?"
                        y "no, but i have a more... natural, traditional, solution."
                        y "it'll even feel good."
                        y "come over here."
                        t ".........."
                        scene black
                        scene bg_bk3_tophome_night
                        show toma toma01
                        show toma_blink_ani
                        with dissolve
                        t "so...."
                        show ctc
                        pause
                        hide ctc
                        t "....what are we doing?"
                        y "i need you to put your arms up."
                        show toma toma03 with dissolve
                        t "like this?"
                        y "yeah, like that. so i can grab your b-"
                        show toma toma05
                        show toma_angry
                        show toma_blush
                        with dissolve
                        t "what!?"
                        y "that's how it's done."
                        t "you can't... can't..."
                        y "do you want to keep your tiny, embarrassing tits forever?"
                        hide toma_angry
                        hide toma_blush
                        show toma_uncertain
                        show toma_blush
                        with dissolve
                        t "no..."
                        t "I... i want big ones, like katara...."
                        show toma_blink with dissolve
                        t "i'm tired of being looked at like... like..."
                        hide toma_blink with dissolve
                        t "...like i'm not an adult!"
                        t "it's not fair."
                        y "well, i'm trying to help."
                        t ".....okay."
                        t "............"
                        show toma toma03 with dissolve
                        t "so what are-"
                        show toma_kneadtits
                        with dissolve
                        t "...oh...uh..."
                        show ctc
                        pause
                        hide ctc
                        t "are you sure this will help?"
                        show ctc
                        pause
                        hide ctc
                        y "which one of us is an all-knowing monk?"
                        show toma toma01 with dissolve
                        t ".....neither of us?"
                        y "well, i know what i'm doing so shush."
                        y "and i need you to put your arms back up."
                        show toma toma03 with dissolve
                        show ctc
                        pause
                        hide ctc
                        y "yeah..."
                        show toma_scissortits
                        hide toma_kneadtits
                        show ctc
                        pause
                        hide ctc
                        t "you're... kind of... pinching my... nipples..?"
                        show toma_angry
                        show toma_blink
                        with dissolve
                        t "is... this really needed...?"
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

                                menu:
                                    "give her another five slaps for good measure":

                                        $ titslap_counter = 5
                                    "This should be enough":
                                        pass


                        y "now i just need to give them a rub down."
                        show toma_rubtits:
                            ypos 0
                            linear 2.0 ypos -30
                            ypos -30
                            linear 2.0 ypos 0
                            repeat

                        show ctc
                        pause
                        hide ctc
                        "after you finish slapping toph's little tits, you rub them eagerly."
                        "her soft, tiny breasts move under the firm pressure of your hands."
                        hide toma_rubtits with dissolve

                        y "Looks like my work here is done! For now."


                        show toma toma01
                        hide toma_uncertain
                        show toma_smile
                        hide toma_blink
                        with Dissolve(1.0)
                        t "Thanks Aang, I'm sure I'll get some massive udders!"
                        t "one last thing..."
                        show expression "screen_red.png":
                            alpha 1.0
                            linear 2.0 alpha 0.0
                        show toma toma25
                        hide toma_smile
                        ya "oww!!!"
                        t "WARN ME NEXT TIME YOU PINCH MY NIPPLES!"
                        show toma toma26
                        y "......"
                        y "But it felt good, right?"
                        t "That's beside the point."
                        y "okay, well, you be mad about me helping you, and i'll see you later."
                        hide expression "screen_red.png"
                        show toma_uncertain with dissolve
                        t "I'm... sorry, aang."
                        y "no worries, i'll see you later!"
                        $ toph_massage +=1
                        scene black with dissolve
                        "you head home for the night."
                        jump bk3_next

                "knock" if earthbending <5:
                    "you knock on the door."
                    show toi toi09 with dissolve
                    t "aang, if i'm going to be your earthbending teacher, we have to have some boundaries."
                    t "I'll see you tomorrow."
                    hide toi toi09 with dissolve
                    jump bk3_village_background
                "peek on toph":

                    hide screen earth_money_date
                    y "no harm in a quick peek through the window..."
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
                    jump bk3_village_background
                "exit":

                    jump bk3_village_background


        if bk3_day:

            if earthbending ==4:

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
                t "you've got {i}stuff{/i} aang!"
                t "well done..."
                t "you're an earthbender."
                show toi_blink
                with dissolve
                t "a baby one, but you took your first steps today."
                hide toi_blink
                show toi toi04
                with dissolve
                t "i guess that \"positive reinforcement\" thing really does work for you."
                show toi toi09 with dissolve
                t "....come see me tonight, if you want."
                $ earthbending = 5
                jump bk3_village_background

            if earthbending ==5 and toph_massage <5:
                y "weird, her door is locked."
                y "i hope i can still visit her at night."
                y "I should keep trying that."
                jump bk3_village_background

            if earthbending ==5 and toph_massage >=5:
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
                y "well I wasn't...."
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

                t "there you go!"

                show toi toi08 with dissolve
                t "here's a boulder."
                show earth_attack1 with moveintop
                play sound "audio/thud.mp3"
                with vshake
                y "my arm hurts....."
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

                label earth_clicer_win:
                    if bk3_loveroute:
                        jump earth_clicer_win2
                    hide screen earth_clicker
                    show toi toi07 with dissolve

                    t "nicely done!"
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
                        "lemme grab your boobs!":

                            t "oh... um..."
                            y "come on, we do it all the time!"
                            y "look, it makes me happy {i}and{/i} it helps your boobs grow."
                            y "we both win."
                            t "..............."
                            t "fine."
                            y "woo!"
                            t "but i'm not taking them out here... it's too public."
                            t "we'll go inside."
                            $ toph_massage_nude = False
                            show toma toma01 with dissolve
                            t "you can either see them or grab them over my shirt, not both."
                            t "which do you want?"
                            menu:
                                "knead them":
                                    ya "gimme the titties!"
                                    show toma toma02 with dissolve
                                    t "okay, go ahead...."
                                    show toma_kneadtits_1
                                    show ctc
                                    pause
                                    hide ctc
                                    t "having fun?"
                                    y "yeah, these are great!"
                                    show toma_blink
                                    show toma_blush
                                    with dissolve
                                    t "......"
                                    t "mmmmm...."
                                    y "i think that's enough."
                                    hide toma_kneadtits_1 with dissolve
                                    show toma_uncertain
                                    hide toma_blink
                                    hide toma_blush
                                    show toma_blush
                                    with dissolve
                                    t "oh, i..."
                                    ym "what's that?"
                                    t "are you... you know... sure?"
                                    y "well-"
                                    show toma_angry
                                    hide toma_uncertain
                                    hide toma_blush
                                    show toma_blush
                                    with dissolve
                                    t "nevermind!"
                                "topless":

                                    y "show me show me!"
                                    t "okay, then...."
                                    $ toph_massage_nude = True
                                    show toma_blush with dissolve
                                    show ctc
                                    pause
                                    hide ctc
                                    y "noice. toit."
                                    t "....what?"
                                    y "just talking to myself."
                                    menu:
                                        "that's enough":
                                            y "alright, i'm good."
                                            $ toph_massage_nude = False
                                        "grab them":

                                            y "i'm just gonna...."
                                            show toma_kneadtits_1
                                            $ renpy.pause(1.0)
                                            show toma_angry
                                            show toma_blush
                                            with dissolve
                                            t ".........."
                                            t "....what the {i}heck{/i} do you think you're doing!?"
                                            y "just reeeeaaaal quick...."
                                            show ctc
                                            pause
                                            hide ctc
                                            show toma_blink with dissolve
                                            show ctc
                                            pause
                                            hide ctc
                                            t "i... said..."
                                            hide toma_blink
                                            show expression "screen_red.png":
                                                alpha 1.0
                                                linear 2.0 alpha 0.0
                                            show toma toma25
                                            ya "oww!!!"
                                            t "...don't!"
                                            y "fine, i'll stop."
                                            show toma toma26 with dissolve
                                            t "......"
                                            t "you're still going!"
                                            y "fine!!"
                                            hide toma_kneadtits_1 with dissolve
                                            y "spoilsport."


                    t "i'll... see you later, aang."
                    jump bk3_village_background

            if earthbending ==6:
                if suki_free:
                    hide screen earth_money_date
                    scene bg_bk3_tophome_day
                    show toi toi11
                    with dissolve
                    t "*sniff...*"
                    y "toph?"
                    t "aang?"
                    show toi toi06
                    show toi_tears
                    with dissolve
                    t "what are you doing here?"
                    y "just checking to see about training, but... what's wrong?"
                    show toi toi11
                    hide toi_tears
                    with dissolve
                    t "i... just heard a rumor about my parents."
                    y "Your parents?"
                    t "yeah, they... they're looking for me."
                    t "they want me to come home."
                    t "they think i'm some weak, scared child..."
                    show toi toi05
                    show toi_tears
                    with dissolve
                    t "and i'm not!"
                    show toi_blink with dissolve
                    t "why can't they see that?"
                    t "i have to hide from them!"
                    t "if they find out where i am...."
                    y "well, you've always seemed pretty strong to me, if it matters."
                    y "i mean, you've been kicking my ass basically every day."
                    hide toi_blink
                    show toi toi04
                    with dissolve
                    t "i have, haven't i?"
                    t "thanks aang, you always know what to say."
                    y "wanna go bust some shit up?"
                    t "...yeah."
                    t "yeah i really do."
                    scene black with dissolve
                    "you go out with toph, and bust some shit up."
                    scene bg_bk3_tophome_day
                    show toi toi07
                    with dissolve
                    t "-and she sat right on it!"
                    t "man, people are dumb."
                    y "I know, right?"
                    show toi toi09 with dissolve
                    t "hey, aang..."
                    t "i really don't want my parents to know where i am."
                    y "good to know."
                    t "and you did well today with your earthbending training."
                    show toi_blush with dissolve
                    t "come by later for... positive reinforcement."
                    y "you sure this doesn't have anything to do with giving you bigger breasts?"
                    show toi toi05 with dissolve
                    t "no!"
                    t "maybe!"
                    t "shut up!"
                    t "just come over!"
                    hide toi toi09
                    hide toi_blush
                    with dissolve
                    $ earthbending +=1
                    jump bk3_village_background
                else:


                    y "huh, her door is locked."
                    y "maybe i should see what i can find in the tunnels."
                    y "i think i remember a wall that seemed breakable...."
                    jump bk3_village_background

            if earthbending ==7:
                if toph_titjob:
                    hide screen earth_money_date
                    scene bg_bk3_tophome_day
                    show toi toi04
                    t "is that you, aang?"
                    menu:
                        "yes":
                            y "you know it."
                        "no":

                            y "....no?"
                            show toi toi06 with dissolve
                            t "you have timid baby steps, i know it's you."
                            show toi toi04 with dissolve

                    t "i'm bored."
                    t "wanna go swimming?"
                    menu:
                        "sure":
                            show toi toi07 with dissolve
                            t "great!"
                            t "i'll get katara and meet you there."
                            hide toi toi07 with dissolve
                            jump earthbending_7_training
                        "maybe later":


                            show toi toi06 with dissolve
                            t "oh.... okay."
                            jump bk3_village_background
                else:

                    show toi toi04 with dissolve
                    t "hey, aang. i'm busy right now."
                    t "come see me tonight if you want."
                    hide toi toi04 with dissolve
                    jump bk3_village_background

            if earthbending ==8:
                if suki_hypno >=5 and june_hypno >=4:
                    show toi toi04 with dissolve
                    t "hey, come on!"
                    y "what's up now?"
                    t "we're meeting katara at the lake!"
                    y "really? word."
                    t "....."
                    y "what? i'm hip."
                    t "you're... really not."
                    y "aww."
                    jump earth_train_8
                else:
                    y "hmmm... i could train with toph..."
                    y "but i think i should spend some time hypnotizing suki and june first."
                    jump bk3_village_background

            if earthbending ==9:
                if not toph_footjob:
                    show toi toi04 with dissolve
                    t "hey, aang. i'm busy right now."
                    t "come see me tonight if you want."
                    hide toi toi04 with dissolve
                    jump bk3_village_background
                else:

                    if toph_blackmail ==8:
                        show toi toi09 with dissolve
                        t "h...hey aang."
                        t "i don't... really feel like training..."
                        y "toph, i know things are a little... stressful right now..."
                        y "but you help me. and i need you to do it."
                        y "i don't expect you to understand, but if i'm going to save the world, i need your training."
                        t "......"
                        show toi toi06 with dissolve
                        t "...whatever."
                        t "today we'll work on turning rock into quicksand."
                        with sshake
                        play sound "audio/win2.mp3"
                        "you train with toph and your earthbending improves!"
                        "you might be able to access more sections of the tunnels...."
                        $ earthbending +=1
                        $ maze_sections = 2
                        $ bk3_day = False
                        jump bk3_village_background

                    if toph_blackmail ==7:
                        y "she doesn't seem to be here right now."
                        y "i should come back tonight."
                        jump bk3_village_background

                    if toph_blackmail <=6:
                        y "the door's locked."
                        y "i should talk to katara."
                        jump bk3_village_background

            if earthbending ==10:
                if not prisonbitch_freed:
                    y "her door is locked..."
                    y "i think i'm strong enough to break more walls in the tunnels."
                    y "i should get down there and see what's up."
                    jump bk3_village_background

                show toki toki01 with dissolve
                k3 "aang-"
                y "katara? what are you doing here?"
                k3 "you can't let toph stay upset."
                k3 "you need to convince her that helping you is in the best interest of everyone, not just because she's blackmailed."
                y "i mean... i thought it was the plan..."
                show toki toki02
                show toki_angry
                with dissolve
                k3 "well, {i}yes{/i}, but only as extra ammunition."
                k3 "you need her to remember that you guys are friends, and that taking care of you is..."
                hide toki_angry
                show toki_blink
                with dissolve
                k3 "...her obligation."
                hide toki_blink with dissolve
                k3 "put her in her place, but remind her that it's not all negative."
                k3 "meet me at the beach with her."
                k3 "tell her that we need to talk this out."
                k3 "i have a plan... just roll with it when you get there, okay?"
                y "if you think that's best."
                k3 "i do."
                y "then i will."
                hide toki toki02 with dissolve
                "you knock on toph's door."
                show toi toi09 with dissolve
                t "......."
                t "hi aang."
                y "hey toph."
                y "katara... wants the three of us to talk."
                t "i'm not... interested."
                y "come on. we need to get this sorted."
                t "...."
                show toi toi06
                show toi_blink
                with dissolve
                t "fine."
                t "where are we going?"
                y "just follow me."
                $ earthbending +=1
                jump toph_reconciliation

            if earthbending ==11:
                if not toph_blowjob:
                    jump toph_blowjob1
                else:

                    show toi toi09 with dissolve
                    t "hey, aang."
                    t "what is it?"
                    y "i just... i want to say i'm sorry about the whole... blackmail thing."
                    y "That was..."
                    show toi toi06 with dissolve
                    t "...pretty messed up of you guys!"
                    show toi toi09 with dissolve
                    t "But I can sorta understand Katara's reasoning."
                    y "You... can?"
                    show toi_blink with dissolve
                    t "I've been wondering about it."
                    t "She lost her mom, Aang."
                    t "in the most horrible way possible because of the fire nation."
                    hide toi_blink with dissolve
                    t "She's pretty much desperate to prevent anything like that happening ever again."
                    t "She has been having nightmares lately about... that time."
                    t "Did you know that?"
                    y "I... didn't."
                    show toi_blink with dissolve
                    t "And since you're a complete failure at bending the normal way..."
                    y "hey!"
                    t "She probably felt you guys had no other choice."
                    t "That's at least what i think."
                    y "well-"
                    hide toi_blink
                    show toi toi05
                    with dissolve
                    t "...that doesn't explain why {i}you're{/i} acting like a jackass, though!"
                    y "Sorry!"
                    y "It's just... I'm... feeling more and more... unrestrained... when it comes to sex lately."
                    show toi toi09 with dissolve
                    t "....hmmmm...."
                    t " Well, it's not like I'm not curious about it, too..."
                    show toi toi04
                    show toi_blush
                    show toi_blink
                    with dissolve
                    t "dirty talk can be... exciting."
                    t "and... just the feeling of your hard co-"
                    show toi toi09
                    hide toi_blink
                    with dissolve
                    t "Ahum, anyway..."
                    t "i'll hold up my end of the deal, if you hold up yours."
                    y "...what?"
                    show toi toi06
                    show toi_blink
                    with dissolve
                    t "that's the deal right?"
                    t "i... help you out, and you... don't tell my parents."
                    hide toi_blink
                    with dissolve
                    t "right?"
                    y "Um. right."
                    t "fine, then."
                    t "let's get to it."
                    y "to... what?"
                    show toi toi05 with dissolve
                    t "training!"
                    t "and i'm gonna stop going easy on you."
                    y "you were... going easy on me?"
                    show toi toi04
                    show toi_blink
                    hide toi_blush
                    with dissolve
                    t "yeah, and that ends today."
                    y "....."
                    y "fuck."
                    play sound "audio/win2.mp3"
                    "you train with toph and increase your earthbending skill!"
                    $ earthbending +=1
                    $ bk3_day = False
                    jump bk3_village_background

            if earthbending ==12:
                $ maze_sections = 3
                show toi toi50 with dissolve
                t "hey."
                show toi toi51 with dissolve
                t "today, we're gonna learn how to close cracks."
                y "oh man.... the amount of jokes i could... this is like the motherload of joke setups..."
                t "pay attention!"
                t "when you come across a crack-"
                y "fill it?"
                t "...."
                t "focus on the crack!"
                y "stop wearing pants!"
                t "darn it, aang! I'm trying to teach you here!"
                y "and i'm trying to learn! bend over!"
                t "....."
                with sshake
                ya "aahhh...!! what's-"
                t "i'm putting you in a crack."
                y "i mean... i'd love to be in your crack...."
                ym "i was just hoping it would be under different circumstances...."
                with sshake
                ya "aaaaahhhhh!!!!!!!!"
                with sshake
                ya "butthole!!!!!"
                hide toi with sshake
                play sound "audio/win2.mp3"
                "your earthbending skill increased!"
                "you learned how to close cracks!"
                y "i think there was a place in the tunnels with some cracks and steam that i couldn't get through before..."
                $ earthbending +=1
                jump bk3_village_background

            if earthbending ==13:
                if earth_riddles ==0:
                    "\"toph's at the beach with me - katara\""
                    y "oh, nice - they remembered toph's illiterate."
                    y "it's easy to forget she's blind sometimes."
                    scene black with dissolve
                    scene lake_laogai_1 with dissolve
                    y "hey, girls-"
                    y "-there's no one here."
                    y "what."
                    y "oh, there's a note..."
                    "\"aang: here, you leave with what you bring,\n though it's rarely ever the same thing.\""
                    y "really? a riddle?"
                    y "don't they know the writer's been awake for 40 hours?"
                    y "....okay, fine. i guess i've got to figure out the location."
                    y "\"here, you leave with what you bring,\n though it's rarely ever the same thing.\""
                    menu:
                        "hear it again":
                            y "\"here, you leave with what you bring,\n though it's rarely ever the same thing.\""
                        "i got it":
                            pass
                    $ earth_riddles = 1
                    jump bk3_village_background
                else:
                    if not naga_eyes:
                        y "i think i should explore the tunnels some more..."
                        jump bk3_village_background

                    if naga_eyes and not first_naga_bj:
                        y "i think i need to rest for a night before i get more training."
                        jump bk3_village_background

                    if first_naga_bj and naga_toph_old ==0:
                        scene black
                        scene bg_bk3_tophome_day
                        show toi toi61
                        with dissolve
                        t "oh... hello, young'un."
                        y "wha... wha..."
                        y "what did you do!?"
                        y "why are you old?"
                        show toi_old_sad with dissolve
                        t "well, that's hurtful..."
                        hide toi_old_sad
                        show toi_old_happy
                        with dissolve
                        t "even the greatest earthbender can't stop time."
                        t "but i'm so very happy to see you again."
                        y "\"again\"... okay, what's happening?"
                        y "there's... something very wrong here."
                        t "hmm? of course there is."
                        t "now..."
                        t "would you like to see me naked?"
                        t "to remember the good old days?"
                        menu:
                            "....sure, why not":
                                t "fine, then."
                                show toi toi66
                                hide toi_old_happy
                                with dissolve
                                t "well? what do you think?"
                                show ctc
                                pause
                                hide ctc
                                y "......"
                                y "{size=+7}why are you so old!?"
                                show toi toi65 with dissolve
                                t "there's no need to hurt my feelings."
                                show toi toi66 with dissolve
                                t "come on, let's have some fun!"
                            "what!? no!":

                                show toi_old_sad
                                hide toi_old_happy
                                with dissolve
                                t "there's no need to hurt my feelings."
                                show toi_old_happy
                                hide toi_old_sad
                                with dissolve
                                t "come on, let's have some fun!"

                        ya "aaaahhhh!!!!!"
                        $ naga_toph_old = 1
                        jump bk3_village_background

                    if naga_toph_old < 8:
                        y "I think i need to figure out what's going on in my head first..."
                        jump bk3_village_background
                    else:

                        if toph_sex and toph_clean_sex:
                            if toph_katara_chair < 7:
                                hide screen earth_money_date
                                scene bg_bk3_tophome_day
                                show toi toi04
                                t "hey aang."
                                t "katara wanted to talk to you."
                                if toph_katara_chair ==0:
                                    $ toph_katara_chair +=1
                                if toph_katara_chair >=1:
                                    pass
                                jump bk3_village_background

                            if toph_katara_chair ==7:
                                jump toph_katara_chair_sex

                            if toph_katara_chair >=8:
                                if not toph_drink_talk:
                                    hide screen earth_money_date
                                    scene bg_bk3_tophome_day
                                    show toi toi04
                                    show toki toki01:
                                        xzoom -1.0
                                    k3 "hey aang!"
                                    k3 "i was just trying to get toph to go out and relax with you some time."
                                    t "i don't know...."
                                    t "alcohol gets me really... loose."
                                    t "and i'm tiny, so it hits me fast..."
                                    t "i'll see you guys later though."
                                    hide toi toi04
                                    with dissolve
                                    hide toki toki01 with dissolve
                                    show toki toki01 with dissolve
                                    k3 "look, i think you need to take toph out, get her to relax."
                                    k3 "she's still too uptight."
                                    y "and how do i get that to happen?"
                                    y "you heard her."
                                    k3 "hmmm...."
                                    k3 "Toph's afraid she'll do something embarrasing in public when drinking too much..."
                                    k3 "...so desensitizing her to that fear will take away her resistance to drinking!"
                                    k3 "which may lead to her doing embarrassing things!"
                                    k3 "you guys are running scams in the market, right?"
                                    y "sometimes."
                                    k3 "and you're doing some, hmm, lewder distractions?"
                                    k3 "like handjobs?"
                                    y "damn girl, you are informed."
                                    k3 "just get her to do public acts like handjobs or wearing a bikini during scams."
                                    k3 "increase her public willingness to like... 10."
                                    k3 "that should get her sufficiently willing to go out drinking."
                                    y "okay, how many do i still need to do?"
                                    k3 "she's at [toph_public]."
                                    $ toph_drink_talk = True
                                    if toph_public >=10:
                                        k3 "oh, wow, you've already done enough."
                                        k3 "maybe visit her in the evening."
                                        k3 "good luck!"
                                        hide toki toki01 with dissolve
                                        jump bk3_village_background

                                    k3 "get to 10 and visit her in the evening, and you should be good."
                                    k3 "good luck!"
                                    hide toki toki01 with dissolve
                                    jump bk3_village_background
                                else:

                                    if toph_public >=10:
                                        if not toph_drunk1:
                                            hide screen earth_money_date
                                            show toki toki01
                                            with dissolve
                                            k3 "hey!"
                                            k3 "you've gotten toph to [toph_public] lewd public willingness."
                                            k3 "oh, wow, you've already done enough."
                                            k3 "maybe visit her in the evening."
                                            k3 "good luck!"
                                            hide toki toki01 with dissolve
                                            jump bk3_village_background
                                        else:
                                            "you knock loudly on toph's door."
                                            show toi toi10
                                            show toi_blink
                                            with dissolve
                                            t "uughhh...."
                                            t "don't... so loud..."
                                            y "are you gonna invite me in?"
                                            t "I... fine..."
                                            scene black
                                            scene bg_bk3_tophome_day
                                            show toi toi09
                                            with dissolve
                                            y "you look a little rough."
                                            t "....you talk too much."
                                            y "what's wrong?"
                                            t "i'm still... hungover, i think..."
                                            y "still?"
                                            show toi toi05
                                            show toi_blush
                                            with dissolve
                                            t "i'm tiny, okay!?"
                                            show toi toi06 with dissolve
                                            t "you should feel bad for letting me get that drunk!"
                                            y "yeah.... but i don't."
                                            t "......"
                                            hide toi_blush
                                            show toi_blink
                                            with dissolve
                                            t "is there a reason you're here?"
                                            y "yeah, i need to get better at earthbending."
                                            y "i feel like... i've progressed some, but not enough."
                                            hide toi_blink
                                            show toi toi09
                                            with dissolve
                                            t "oh?"
                                            y "yeah, i think i need a particularly awesome lesson..."
                                            y "followed by some particularly awesome \"encouragement\"."
                                            show toi toi06 with dissolve
                                            t "yeah, i suppose if i don't have a say."
                                            y "you do... but there will probably be consequences..."
                                            show toi_blink with dissolve
                                            t "what do you want?"
                                            y "well, you brought up an interesting idea while we were drinking..."
                                            hide toi_blink
                                            show toi toi09
                                            with dissolve
                                            t "i did?"
                                            y "yeah..."
                                            y "anal."
                                            show toi toi06
                                            show toi_blush
                                            with dissolve
                                            t "i did not!"
                                            y "yes, you did."
                                            y "i think you really want to try it."
                                            show toi toi05 with dissolve
                                            t "no, i don't!"
                                            t "...shut up!"
                                            y "well... if you're not willing to admit it..."
                                            y "let's pretend it's because i'm blackmailing you..."
                                            y "...and you don't really have a choice."
                                            hide toi_blush
                                            show toi toi06
                                            with dissolve
                                            t "....you really want to..."
                                            t "...do that?"
                                            y "anal? yeah."
                                            y "and you want it, too."
                                            show toi toi05 with dissolve
                                            t "no, i don't!"
                                            show toi toi06 with dissolve
                                            t "but if i don't have a choice..."
                                            y "oh, and an awesome training session."
                                            t "i've been-"
                                            y "no, a good one."
                                            y "your lessons are hard and boring."
                                            t "hey!"
                                            y "come on, give me something cool!"
                                            y "teach me to make dirt tornadoes!"
                                            y "or... rock spikes!"
                                            t "....i think i have just the thing."
                                            y "sweet, let's go."
                                            scene black with dissolve
                                            jump toph_maze_training


                                    if toph_public <=9:
                                        hide screen earth_money_date
                                        show toki toki01
                                        with dissolve
                                        k3 "hey!"
                                        k3 "you've gotten toph to [toph_public] lewd public willingness."
                                        k3 "you just need 10."
                                        k3 "get her to give you some more public handjobs or wear a bikini and visit her in the evening, and you should be good."
                                        k3 "good luck!"
                                        hide toki toki01 with dissolve
                                        jump bk3_village_background

                        if toph_sex and not toph_clean_sex:
                            jump toph_clean_fuck
                        else:

                            y "the door's locked right now."
                            y "maybe i should get a little farther with toph first."
                            jump bk3_village_background

            if earthbending==14:
                if toph_tunnel_training >=4:
                    hide screen earth_money_date
                    show bg_bk3_tophome_day
                    show toi toi02
                    with dissolve
                    t "hey, twinkletoes!"
                    y "....."
                    ya "that's it!"
                    ya "you're going to treat me with some fucking respect!"
                    show toi toi09 with dissolve
                    t "what?"
                    t "where did this come from?"
                    y "i'm done being gentle with you."
                    y "you should know by now that there are consequences."
                    ya "can't you see that i'm the fucking avatar!?"
                    t "uhh..."
                    show toi toi100
                    t "...."
                    t "no."
                    show toi toi04 with dissolve
                    y "....you're right. your eyes are fucking useless."
                    y "since you're not using them, i'm gonna cum in them."
                    show toi toi06 with dissolve
                    t "what?"
                    y "get on the floor and open your big, useless fucking eyes."
                    t "......."
                    t "that's a little too far-"
                    y "i don't give a shit."
                    y "get on your knees."
                    t ".....no."
                    y "what was that?"
                    t "no."
                    t "it's not like you can actually make me."
                    t "you just have blackmail."
                    y "fine. outside. now."
                    y "we'll settle this."
                    t "settle what?"
                    y "who's the better earthbender."
                    y "i'm a quick learner, and i'm going to wear your ass like a hat."
                    y "a juicy, juicy hat."
                    t "...."
                    y "was that too weird?"
                    y "that felt weird."
                    t "so... let me get this straight..."
                    t "you want to fight me?"
                    t "for real?"
                    y "yeah."
                    t "......."
                    show toi toi07 with dissolve
                    t "ha!"
                    t "fat chance, twinkletoes!"
                    t "you don't stand a chance against me."
                    y "willing to put it to the test, short stuff?"
                    show toi toi05 with dissolve
                    t "don't call me that!"
                    y "oh? well how about {i}bitch{/i}."
                    t "hey!"
                    y "get outside, you little whore."
                    t "you're in for it now, aang."
                    t "I'm not going easy on you any more."
                    hide bg_bk3_tophome_day
                    hide toi
                    show toph_body_cloth:
                        xpos 50
                    with Dissolve(1)
                    t "you might have power over me, aang, but you'll never be as {i}powerful{/i} as me."
                    show body_rock:
                        xpos 50
                    hide toph_body_cloth
                    with vshake
                    t "here i come!"
                    show big_rock:
                        around (.5, .5) alignaround (.5, .5) xalign .1 yalign .5
                        rotate 0
                        linear 10 rotate 360
                        repeat
                    with moveinbottom
                    y "get some!"
                    show ctc
                    pause
                    hide ctc
                    show body_rock:
                        linear 1.0 xpos -500
                    show big_rock:
                        linear 1.0 xpos 500
                    $ renpy.pause(0.25)
                    play sound "audio/earth.wav"
                    scene black
                    with flash
                    scene bg_training_0 with Dissolve(1.5)
                    $ earthbending = 15
                    jump toph_rockbound
                else:
                    y "the door's locked right now."
                    y "maybe i should get a little farther with toph first."
                    jump bk3_village_background

            if earthbending >=15:
                if toph_mom_fucked:
                    if not toph_mom_fucked2:
                        pop "i've decided to stay here for a little longer."
                        pop "in order to convince toph to come home."
                        pop "and if you're going to force me to have sex-"
                        y "say what now?"
                        pop "i guess i don't have a choice."
                        y "....."
                        y "you're a horny broad, aren't you?"
                        pop "well, i never!"
                        $ toph_mom_fucked2 = True
                    menu:
                        "Fuck poppy beifong":
                            jump tophmomfuck2
                        "train with (and facefuck) toph":

                            hide screen earth_money_date
                            show bg_bk3_tophome_day
                            show toi toi50
                            with dissolve
                            t "hello, [bk3name]!"
                            t "come back for more training?"
                            t "let's go outside."
                            t "by the way... you should speak with katara."
                            t "she mentioned she had something to tell you."
                            y "okay, i will."
                            y "but first...."
                            jump toph_rockbound2
                        "back":

                            jump bk3_village_background

                if nagina_free:
                    hide screen earth_money_date
                    show bg_bk3_tophome_day
                    show toi toi50
                    with dissolve
                    t "hey, you!"
                    t "i'm glad you came by."
                    t "i'm super horny and was thinking-"
                    "*knock knock*"
                    y "....were you expecting company?"
                    t "no..."
                    $ toph_mom_fucked = True
                    jump tophmomfuck

                "train with toph? (and fuck her face?)"
                menu:
                    "give [bk3name] what he needs":
                        hide screen earth_money_date
                        show bg_bk3_tophome_day
                        show toi toi50
                        with dissolve
                        t "hello, [bk3name]!"
                        t "come back for more training?"
                        t "let's go outside."
                        if bk3_handjob <1:
                            t "by the way... you should speak with katara."
                            t "she mentioned she had something to tell you."
                            y "okay, i will."
                            y "but first...."
                        jump toph_rockbound2
                    "nah":

                        y "maybe later."
                        jump bk3_village_background

                jump bk3_village_background


    if heal_maze_girl:
        scene black
        scene bg_bk3_tophome_night
        with dissolve
        y "i should go to the hospital."
        jump bk3_village_background

    if hospital_built and not heal_maze_girl:
        scene black
        scene bg_bk3_tophome_night
        show toi toi04:
            xzoom -1.0
        show toki toki02
        with dissolve
        y "hey, i built the-"
        t "i know, and i found katara."
        k3 "i'll do my best to heal her."
        t "let's get over to the hospital right away."
        $ heal_maze_girl = True
        jump bk3_village_background

    if hospital_build and not hospital_built:
        scene black
        scene bg_bk3_tophome_night
        show toi toi09
        with dissolve
        t "please build us a hospital, aang."
        jump bk3_village_background

    if first_maze_girl and not first_maze_girl_escape:
        $ first_maze_girl_escape = True
        scene black
        scene bg_bk3_tophome_night
        show toi toi09
        with dissolve
        y "ugh..."
        with vshake
        "you drop the girl onto a makeshift bed."
        "girl" "mummble..."
        y "...did she just say \"mumble\"?"
        y "nobody actually says \"mumble\"."
        t "she's got a fever."
        y "how do you know that?"
        y "oh, don't tell me! the old \"finger in the butt\" technique."
        y "i've definitely done my share of pretending to be a doctor-"
        t "no, she's really burning up."
        t "we need to build a hospital out here."
        t "please."
        t "i'll stay here with her while you get it taken care of."
        t "...although I guess I can meet you in the market to run some scams if you need it."
        t "just come back here when the hospital is built."
        $ hospital_build = True
        jump bk3_village_background


    if village_dev_explain2:
        if not bk3_day:
            menu:
                "knock":
                    "you knock on the door."
                    show toi toi09 with dissolve
                    t "aang, if i'm going to be your earthbending teacher, we have to have some boundaries."
                    t "I'll see you tomorrow."
                    hide toi toi09 with dissolve
                    jump bk3_village_background
                "peek on toph":

                    y "no harm in a quick peek through the window..."
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
                    jump bk3_village_background
                "exit":

                    jump bk3_village_background


        if bk3_day:
            if not bk3_tavern_built:

                if bk3_wood >=5 and bk3_steel >=5:
                    show toi toi07 with dissolve
                    t "you brought the materials!"
                    y "how... can you tell?"
                    show toi toi09

                    with dissolve
                    t "i'm blind, but i'm not {i}blind{/i}, aang."
                    y "i... that doesn't mean anything."
                    show toi_blink with dissolve
                    t "i see with my feet, aang."
                    t "your footsteps are heavier."
                    hide toi_blink
                    show toi toi08
                    with dissolve
                    t "so let's get this tavern set up!"
                    jump build_tavern1

            if earth_training:
                show toi toi09 with dissolve
                t "you've already trained today."
                show toi toi04
                show toi_blink
                with dissolve
                t "you're not ready for more yet."
                hide toi_blink with dissolve
                t "come back tomorrow."
                hide toi toi04 with dissolve
                jump bk3_village_background

            if earthbending ==0:
                show toi toi02 with dissolve
                t "let's start your training."
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
                scene villagemap_day_base
                if position_1 == True:
                    show expression "ebackgrounds/village/roads/road_1.png"
                if position_2 == True:
                    show expression "ebackgrounds/village/roads/road_2.png"
                if position_3 == True:
                    show expression "ebackgrounds/village/roads/road_3.png"
                if position_4 == True:
                    show expression "ebackgrounds/village/roads/road_4.png"
                if position_5 == True:
                    show expression "ebackgrounds/village/roads/road_5.png"
                if position_6 == True:
                    show expression "ebackgrounds/village/roads/road_6.png"
                if position_7 == True:
                    show expression "ebackgrounds/village/roads/road_7.png"
                if position_8 == True:
                    show expression "ebackgrounds/village/roads/road_8.png"
                if avatar_shack == 1:
                    show expression "ebackgrounds/village/buildings/shack/shack01.png":
                        xpos avatar_shack_xpos ypos avatar_shack_ypos
                if tavern_shack == 1:
                    show expression "ebackgrounds/village/buildings/tavern/shack01.png":
                        xpos tavern_shack_xpos ypos tavern_shack_ypos

                with dissolve
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
                show toi_blink
                show big_rock at truecenter with moveinright
                with sshake
                "toph drops a massive boulder on you that you can barely hold."
                show toi toi01
                with dissolve
                t "keep your knees high, twinkle toes!"
                y "this seems so unnecessary!"
                hide toi_blink
                with dissolve
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
                t "fine, we'll continue this tomorrow."
                $ earthbending = 1

                hide toi toi04 with dissolve
                $ earth_training = True
                jump bk3_village

            if earthbending ==1:

                show toi toi02
                with dissolve
                t "ready to train some more?"
                y "no..."
                show toi toi07 with dissolve
                t "that's the spirit!"
                y "....you're a cruel person."
                show toi toi04 with dissolve
                t "tell you what... i'll apologize to you..."
                y "thank you-"
                t "-if you can stop me."
                y "wh... what? stop you?"
                hide toi toi04 with dissolve
                show toph_body_cloth with dissolve
                t "i'm gonna come at you like a rock-covered train."
                y "i... really don't like the sound of that..."
                show body_rock
                hide toph_body_cloth
                with dissolve

                y "nononononono...."
                t "get some!!"
                hide body_rock
                with moveoutleft
                with sshake
                y "fuuuu-"
                show black with sshake
                hide black with dissolve
                yc "uuughhh..."
                show toi toi06
                show toi_blink
                with dissolve
                t "what was {i}that{/i}?"
                t "i expect better effort from the avatar."
                yc "....i'll take a bacon scrambler, thank you...."
                hide toi_blink
                show toi toi01
                with dissolve
                t "shape up, aang!"
                t "you perpetual disappointment!"
                y "you... are the rudest..."
                show toi toi06 with dissolve
                t "get out of my sight until you're willing to actually give this a try."
                y "i... am... trying..."
                hide toi toi06 with dissolve
                $ earthbending =2
                y "....."
                y "this is not going well."
                $ earth_training = True
                jump bk3_village_background

            if earthbending ==2 and not bk3_tavern_built:
                show toi toi06 with dissolve
                t "we need 5 wood and 5 steel to build a tavern."
                t "get to it!"
                hide toi toi06 with dissolve
                jump bk3_village_background

            if earthbending ==2 and bk3_tavern_built:
                if not toph_swim_talk:
                    show toi toi02
                    show toi_blink
                    with dissolve
                    t "time for-"
                    y "nah."
                    show toi toi09
                    hide toi_blink
                    with dissolve
                    t "...what?"
                    y "i think we need a little break."
                    t "...."
                    show toi toi04 with dissolve
                    t "...yeah, that sounds good."
                    y "really? you're not gonna go all \"drill sergeant\" on me?"
                    t "i think you're right."
                    show toi_blink with dissolve
                    t "besides, the way we're currently training isn't working at all."
                    t "there's a lake nearby."
                    hide toi_blink
                    $ toph_swim_talk = True

                show toi toi07
                with dissolve
                t "wanna go for a swim?"
                menu:
                    "swim":
                        jump toph_swim
                    "not yet":


                        y "not right now."
                        show toi toi09
                        with dissolve
                        t "oh..."
                        t "well, i still think it's a good idea, so let me know when you're ready."
                        jump bk3_village_background

            if earthbending ==3 and not village_store_start:
                scene black
                scene bg_bk3_tophome_day
                show toi toi09
                with dissolve
                t "aang."
                y "what it do, girl?"
                t "what?"
                t "anyway, look, i've been thinking-"
                y "never a good sign with you."
                show toi toi06 with dissolve
                t "would you just shut it?"
                show toi toi09 with dissolve
                t "we need a store here."
                y "a store? why?"
                t "we need to get some income flowing into the village."
                t "obviously, as head of the village, you'd receive some of that income to use as you please."
                y "...well sign me right the fuck up."
                show toi toi02 with dissolve
                t "i'm glad you said that."
                t "once again, you're gonna need {b}5 wood{/b} and {b}5 steel{/b}."
                t "come back to me once you have that."
                $ village_store_start = True
                jump bk3_village_background

            if earthbending ==3 and village_store_start:
                if bk3_wood >=5 and bk3_steel >=5 or village_store_build:
                    if village_store_build:
                        if not bk3_store_built:
                            scene black
                            scene bg_bk3_tophome_day
                            show toi toi06
                            with dissolve
                            t "you need to build that store, aang."
                            hide toi toi06 with dissolve
                            jump bk3_village_background
                        else:
                            if after_store_training:
                                scene black
                                scene bg_bk3_tophome_day
                                show toi toi02
                                with dissolve
                                t "ready for some more training?"
                                menu:
                                    "not now":
                                        y "can we do it later?"
                                        show toi toi06 with dissolve
                                        t "it's really important that you learn how to earthbend, aang."
                                        show toi toi04
                                        show toi_blink
                                        with dissolve
                                        t "but if you wanna fight ozai and die, that's your call."
                                        jump bk3_village_background
                                    "sure, let's do it":

                                        jump after_store_train
                            else:

                                scene black
                                scene bg_bk3_tophome_day
                                show toi toi02
                                with dissolve
                                t "nicely done, aang!"
                                t "this place is really starting to come together."
                                y "except there's no shopkeeper..."
                                show toi_blink with dissolve
                                t "one thing at a time."
                                hide toi_blink with dissolve
                                t "anyway, i think it's time for some more training!"
                                menu:
                                    "not now":
                                        y "can we do it later?"
                                        show toi toi06 with dissolve
                                        t "it's really important that you learn how to earthbend, aang."
                                        show toi toi04
                                        show toi_blink
                                        with dissolve
                                        t "but if you wanna fight ozai and die, that's your call."
                                        $ after_store_training = True
                                        jump bk3_village_background
                                    "sure, let's do it":

                                        jump after_store_train
                    else:

                        scene black
                        scene bg_bk3_tophome_day
                        show toi toi02
                        with dissolve
                        t "great! you've got it!"
                        y "...it freaks me out when you do that."
                        show toi_blink with dissolve
                        t "sorry, not sorry."
                        hide toi_blink
                        show toi toi09
                        with dissolve
                        t "okay, so, i can't hold your hand every time you try to build or upgrade a building."
                        t "from now on, you need to build from the village map."
                        show blackveil with dissolve
                        show build_icon_off:
                            xpos 0.77
                        with dissolve
                        "you can now use the \"build\" icon."
                        show build_icon_on:
                            xpos 0.77
                        with dissolve
                        "from the village map, click the icon to manage the village's buildings."
                        "you can build and upgrade buildings from this menu."
                        hide build_icon_on with dissolve
                        hide blackveil
                        hide build_icon_off
                        with dissolve
                        $ village_store_build = True
                        t "come back when you've built the store."
                        jump bk3_village_background
                else:
                    scene black
                    scene bg_bk3_tophome_day
                    show toi toi09
                    with dissolve
                    t "go get {b}5 wood{/b} and {b}5 steel{/b} so we can build a store!"
                    hide toi toi09 with dissolve
                    jump bk3_village_background


    scene black
    scene bg_bk3_tophome_day
    show toi toi02
    with dissolve
    t "hey! have you bought the materials we need for your house?"
    if house_wood and house_steel:
        jump build_shack1
    else:
        y "Um... no?"
        show toi toi06 with dissolve
        t "i-"
        show toi_blink with dissolve
        t "well, whatever."
        show toi toi04 with dissolve
        t "i'll be here whenever you figure it out."
        jump bk3_village_day




label inside_shop_building:
    stop music
    play music"audio/Carpe Diem.mp3"
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
            jump bk3_village_shop_menu

            label bk3_village_shop_menu:
                menu:
                    "random trap - 2 crapples":
                        if crapples <2:
                            "not enough crapples! you need to win them from trainers in the arena!"
                            jump bk3_village_shop_menu
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
                            jump bk3_village_shop_menu

                    "saucy trap - 5 crapples" if shop_building <2:
                        girl "i gave you my only saucy crab trap, i don't have the resources to find better crabs."
                        girl "but..."
                        girl "if you help me upgrade the shop, i'll be able to start stocking saucy crabtraps!"
                        girl "think about it!"
                        jump bk3_village_shop_menu

                    "saucy trap - 5 crapples" if shop_building >=2:
                        if crapples <5:
                            "not enough crapples! you need to win them from trainers in the arena!"
                            jump bk3_village_shop_menu
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
                            jump bk3_village_background

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
                                    jump bk3_village_shop_menu
                                else:
                                    "not enough money..."
                                    jump bk3_village_shop_menu
                            "crab health potion - 20":
                                if emoney >=20:
                                    play sound "audio/win2.mp3"
                                    $ emoney -=20
                                    $ arena_potion +=1
                                    "keep your crabs healthy!"
                                    jump bk3_village_shop_menu
                            "smelling salts - 15":

                                if emoney >=15:
                                    play sound "audio/win2.mp3"
                                    $ emoney -=15
                                    $ arena_salts +=1
                                    "cures confusion when used!"
                                    jump bk3_village_shop_menu
                                else:
                                    "not enough money..."
                                    jump bk3_village_shop_menu
                            "------(locked)":

                                "test"
                            "------(locked)":

                                "test"
                            "------(locked)":

                                "test"
                            "------(locked)":

                                "test"
                            "cancel":

                                jump bk3_village_shop_menu

                    "buy items" if shop_building >=2:
                        jump bk3_village_shop_item_menu

                        label bk3_village_shop_item_menu:
                            menu:
                                "crab pocket - 15":
                                    girl "used to catch crabs!"
                                    menu:
                                        "buy":
                                            if emoney >=15:
                                                play sound "audio/win2.mp3"
                                                $ emoney -=15
                                                $ arena_pocket +=1

                                                jump bk3_village_shop_item_menu
                                            else:
                                                "not enough money..."
                                                jump bk3_village_shop_item_menu
                                        "buy 5 - 65":
                                            if emoney >=75:
                                                play sound "audio/win2.mp3"
                                                $ emoney -=75
                                                $ arena_pocket +=5

                                                jump bk3_village_shop_item_menu
                                            else:
                                                "not enough money..."
                                                jump bk3_village_shop_item_menu
                                        "back":
                                            jump bk3_village_shop_item_menu
                                "crab health potion - 20":

                                    girl "keep your crabs healthy!"
                                    menu:
                                        "buy":
                                            if emoney >=20:
                                                play sound "audio/win2.mp3"
                                                $ emoney -=20
                                                $ arena_potion +=1
                                                jump bk3_village_shop_item_menu
                                            else:
                                                "not enough money..."
                                                jump bk3_village_shop_item_menu
                                        "buy 5 - 80":
                                            if emoney >=80:
                                                play sound "audio/win2.mp3"
                                                $ emoney -=80
                                                $ arena_potion +=5
                                                jump bk3_village_shop_item_menu
                                            else:
                                                "not enough money..."
                                                jump bk3_village_shop_item_menu
                                        "exit":

                                            jump bk3_village_shop_item_menu
                                "smelling salts - 15":
                                    girl "cures confusion when used!"
                                    menu:
                                        "buy":
                                            if emoney >=15:
                                                play sound "audio/win2.mp3"
                                                $ emoney -=15
                                                $ arena_salts +=1

                                                jump bk3_village_shop_item_menu
                                            else:
                                                "not enough money..."
                                                jump bk3_village_shop_item_menu
                                        "back":
                                            jump bk3_village_shop_item_menu
                                "antidote - 15":
                                    girl "cures posion when used!"
                                    menu:
                                        "buy":
                                            if emoney >=15:
                                                play sound "audio/win2.mp3"
                                                $ emoney -=15
                                                $ arena_antidote +=1
                                                "cures posion when used!"
                                                jump bk3_village_shop_item_menu
                                            else:
                                                "not enough money..."
                                                jump bk3_village_shop_item_menu
                                        "exit":
                                            jump bk3_village_shop_item_menu
                                "steroids - 15":
                                    girl "cures weak when used!"
                                    menu:
                                        "buy":
                                            if emoney >=15:
                                                play sound "audio/win2.mp3"
                                                $ emoney -=15
                                                $ arena_steroid +=1
                                                "cures weak when used!"
                                                jump bk3_village_shop_item_menu
                                            else:
                                                "not enough money..."
                                                jump bk3_village_shop_item_menu
                                        "exit":
                                            jump bk3_village_shop_item_menu
                                "cure-all - 80":
                                    girl "cures your crab of all diseases (and status effects). Ironic."
                                    menu:
                                        "buy":

                                            if emoney >=80:
                                                play sound "audio/win2.mp3"
                                                $ emoney -=80
                                                $ cureall +=1
                                                jump bk3_village_shop_item_menu
                                            else:
                                                "not enough money..."
                                                jump bk3_village_shop_item_menu
                                        "exit":
                                            jump bk3_village_shop_item_menu
                                "rarity stone - 2 crapples":
                                    girl "rarity stones make your crabs more powerful and harder to remove!"
                                    menu:
                                        "buy":
                                            if crapples >=2:
                                                $ crapples -=2
                                                $ rarity_stones += 1
                                                play sound "audio/win2.mp3"
                                                "you got a rarity stone!"
                                                jump bk3_village_shop_item_menu
                                            else:
                                                "not enough crapples..."
                                                jump bk3_village_shop_item_menu
                                        "exit":
                                            jump bk3_village_shop_item_menu



                                    jump bk3_village_shop_item_menu
                                "cancel":
                                    jump bk3_village_shop_menu
                    "exit":

                        girl "come back soon!"
                        jump bk3_village_background

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















































































        scene black
        scene inside_shop
        with dissolve
        "this store has no shopkeeper yet."
        jump bk3_village_background



label inside_tavern_shack:






    stop music
    play music "audio/Achaidh Cheide.mp3"

    if bk3_day:
        scene inside_tavern_day with dissolve
    if not bk3_day:
        scene inside_tavern_night with dissolve

    if naga_toph_old == 3:
        show mf with dissolve
        y "hey, ju-"
        ya "mai!?"
        y "what... how... why are you here?"
        m "you left me."
        m "you abandoned me."
        y "i had to, i didn't-"
        y "....wait, that hasn't happened yet."
        y "and... i had a different body."
        y "how do you know it's... me?"
        if thief >= zuko:
            m "you haven't changed."
            m "you had it all to yourself and it wasn't enough."
            m "do you regret leaving us?"
        else:
            m "you haven't changed, zuko."
            y "i was never zuko."
            y "I was always me."
            y "i just... didn't know it."
            show mf2
            hide mf
            with dissolve
            if azula_chosen:
                m "you had azula all to yourself and it wasn't enough."
                m "do you regret leaving her?"
            if mai_chosen:
                m "you had me all to yourself and it wasn't enough."
                m "do you regret leaving me?"
            if zuko_end:
                m "you had azula and i all to yourself and it wasn't enough."
                m "do you regret leaving us?"

        y "i had to... it wasn't... i don't have a lot of say when it comes to this stuff."
        show mka
        hide mf2
        hide mf
        with dissolve
        if thief >= zuko:
            m "you will never leave me again."
        else:
            m "you will never leave me again, zuko."

        y "you... this... has to be a figment of my imagination."
        y "you're not real."
        y "how could you be?"
        with sshake
        "mai throws a dagger that lightly grazes your arm."
        "as you look down, you see yourself bleeding."
        y "oh."
        y "huh."
        y "um."
        y "rain check?"
        show mfa
        hide mka
        with dissolve
        m "{size=+7}{i}{b}get out of my shop!!"
        y "well, i'm gonna go."
        "dodging another knife, you flee the tavern."
        "she doesn't seem to follow you."
        y "what the hell was that...?"
        $ naga_toph_old = 4
        jump bk3_village_background

    if toph_blackmail ==5:
        show toju toju01 with dissolve
        ju "shouldn't we be meeting katara?"
        jump bk3_village_background

    if toph_blackmail ==4:
        show toju toju01 with dissolve
        ju "avatar."
        ju "do you need something?"
        y "[trigger]."
        show toju_hypno_eyes with dissolve
        y "you are going to come with me to see katara."
        ju "i am going to come with you to see katara."
        y "[trigger]."
        hide toju_hypno_eyes with dissolve
        ju "i... think i should go with you."
        y "great. let's go visit katara."
        $ toph_blackmail +=1
        jump bk3_village_background

    if not earth_tavern_start:
        y "okay... tavern. right."
        y "uh... i don't know anything about running a tavern."


    if june_free and not june_convo:
        show toju toju01 with dissolve
        ju "hey. you."
        y "who-"
        y "oh... you're the chick i rescued from the maze."
        show toju toju02 with dissolve
        ju "that's right... and we're {i}never{/i} gonna speak of that again."
        if june_money:
            y "what about that money you offered me?"
            ju "I... oh, fine."
            ju "here."
            $ emoney +=40
            play sound "audio/win2.mp3"
            "you got 40 coins!"
        else:

            y "fine by me."

        y "so, what are you doing here?"
        show toju toju01
        show toju_blink
        with dissolve
        ju "well, i don't seem to have anywhere to go."
        ju "so i thought i'd stay here in the tavern."
        show toju toju02
        hide toju_blink
        with dissolve
        ju "that's all right, isn't it?"
        menu:
            "sure... if you're willing to work":
                y "fine, but...."
            "flash me and we're even":

                y "show me your tits and you can stay... for the day."
                show toju toju01 with dissolve
                ju "hmmm...."
                show toju_blink with dissolve
                ju "...have you met my ride?"
                y "what?"
                show toju toju02 with dissolve
                ju "because when he misbehaves..."
                show toju toju03
                hide toju_blink
                with dissolve
                ju "i put him in his place."
                ju "and i will do the same to you if you ever suggest that again."
                y "fine, but..."

        y "i need a bartender."
        show toju toju01 with dissolve
        ju "do i look like a bartender to you?"
        y "......"
        y "yeah."
        show toju toju04 with dissolve
        ju "you..."
        show toju toju02
        show toju_blink
        with dissolve
        ju "you seem to misunderstand-"
        y "lady! do you want to stay here or not?"
        show toju toju04
        hide toju_blink
        with dissolve
        ju "I-"
        ju "........"
        show toju toju01
        show toju_blink
        with dissolve
        ju "Hmph."
        ju "i guess i don't have a choice."
        hide toju_blink
        show toju toju02
        with dissolve
        ju "i'll work here..."
        show toju_blink with dissolve
        ju "but i'm not wearing some ridiculous wench outfit, understand?"
        hide toju_blink with dissolve
        y "you'll do what i-"
        show toju toju01
        show toju_blink
        with dissolve
        ju "now, i think i'll take a look at my accomodations."
        hide toju toju01
        hide toju_blink
        with dissolve
        y "......"
        y "that's gonna be fun."
        $ june_convo = True
        jump bk3_village_background

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
                    jump inside_tavern_shack
            $ bk3_bar_wins = 0
            jump earth_tavern
        "talk to bartender" if not june_free:
            "you don't have a bartender yet!"
            jump inside_tavern_shack

        "talk to june" if june_free:
            hide screen earth_money_date
            if june_convo_today:
                y "I've already talked with her today, i'll check in with her tomorrow."
                jump inside_tavern_shack

            if june_talk >=7 and not june_convo_today:
                play sound "audio/money.mp3"
                $ randcoin = renpy.random.randint(11, 21)
                $ emoney += randcoin
                "june gave you half her tips!"
                "you got [randcoin] coins!"

            if wench_outfit and not june_wench_no:
                show toju toju02 with dissolve
                ju "what's up?"
                y "so i bought this outfit-"
                ju "yeah... i'm not wearing some wench dress."
                ju "do i look like a whore?"
                y "i mean..."
                ju "watch yourself."
                y "you watch {i}yourself{/i}!"
                ju "whatever. i'm not wearing that."
                $ june_wench_no = True
                $ june_convo_today = True
                jump inside_tavern_shack

            if june_talk ==0:
                show toju toju02 with dissolve
                ju "yes?"
                y "having any trouble?"
                ju "not particularly-"
                show toju toju03 with dissolve
                ju "hey! you! cut that out and i'm going to feed you to my pet outside!"
                ju "......"
                show toju toju02
                with dissolve
                ju "that's what i thought."
                y "........."
                y "so... no problems then."
                show toju toju01
                show toju_blink
                with dissolve
                ju "not right now."
                y "great. can you make me a drink?"
                hide toju_blink with dissolve
                ju "hmm... i don't think so."
                ju "bye."
                hide toju toju01 with dissolve
                y "*growl*"
                $ june_talk =1
                $ june_convo_today = True
                jump inside_tavern_shack

            if june_talk ==1:
                show toju toju01
                with dissolve
                y "june, make me a drink."
                ju "well, avatar, let m put it this way..."
                ju "no."
                y "...."
                ju "no hard feelings, but getting people drinks...."
                show toju_blink with dissolve
                ju "that's just not something i do."
                y "...that's an interesting point except that you agreed to work here."
                ju "hm. i did."
                ju "whadda ya know."
                y "..........."
                hide toju_blink with dissolve
                ju "oh, that guy looks like he's willing to gamble with a girl."
                ju "excuse me i need to make a quick coin."
                hide toju toju01
                with dissolve
                $ june_talk +=1
                $ june_convo_today = True
                jump inside_tavern_shack
            if june_talk ==2:
                show toju toju02
                with dissolve
                ju "what now?"
                y "well that's a little rude, considering i'm letting you stay here."
                ju "sure."
                ju "now what is it?"
                y "...."
                y "i'm working on this hypno room in my house to undo long feng's hypnosis."
                y "you should stop by."
                show toju_blink with dissolve
                ju "yeah... i've not sure i actually need that."
                y "....what."
                ju "i've been fine. no problems."
                hide toju_blink with dissolve
                ju "so, don't worry about it. thanks though."
                hide toju toju01 with dissolve
                $ june_talk +=1
                $ june_convo_today = True
                jump inside_tavern_shack
            if june_talk ==3 and suki_hypno ==0:
                show toju toju01
                with dissolve
                y "june, have you given any more thought to the hypno room?"
                ju "yeah, and i don't really need it. but thanks."
                ju "why don't you test out your room on someone else?"
                ju "maybe i'll test it after that."
                $ june_convo_today = True
                jump inside_tavern_shack

            if june_talk ==3 and suki_hypno >=1:
                show toju toju01
                with dissolve
                ju "ugh, what is it?"
                y "hey, don't talk to me like that. i'm your boss."
                show toju_blink with dissolve
                ju "yeah, sure. what is it?"
                y "look, suki came by and tested out the room."
                hide toju_blink with dissolve
                ju "that so?"
                y "it is, and it worked great. she's already feeling better."
                ju "hmm....."
                ju "alright, what can it hurt?"
                ju "i'll come by."
                if hypnoroom == "none":
                    $ hypnoroom = "june"
                    y "great, see you there."
                if hypnoroom == "june":
                    y "I'm still waiting on you to get over to the hypno-room."
                    ju "well, i'm waiting on you for the same thing."
                    y "oh. erm. whatever."
                else:
                    y "oh, wait, i have an appointment there already."
                    y "i'll take care of that first, then come tell you when it's free."
                    ju "...sure, whatever."
                $ june_talk +=1
                $ june_convo_today = True
                jump inside_tavern_shack

            if june_talk ==4 and june_hypno ==0:
                show toju toju01
                with dissolve
                ju "what is it?"
                y "you should come by the hypno room."
                ju "....alright, what can it hurt?"
                ju "i'll come by."
                if hypnoroom == "none":
                    $ hypnoroom = "june"
                    y "great, see you there."
                if hypnoroom == "june":
                    y "I'm still waiting on you to get over to the hypno-room."
                    ju "well, i'm waiting on you for the same thing."
                    y "oh. erm. whatever."
                else:
                    y "oh, wait, i have an appointment there already."
                    y "i'll take care of that first, then come tell you when it's free."
                    ju "...sure, whatever."
                $ june_convo_today = True
                jump inside_tavern_shack

            if june_talk ==4 and june_hypno ==1:
                show toju toju02
                with dissolve
                ju "hi there."
                ju "If you need a drink, you know where they are."
                y "....."
                ya "(don't strangle her....)"
                y "well, are you ready for another hypno session?"
                ju "i thought we covered this... it's not really for me."
                y "oh, i'm sorry to hear that."
                y "[trigger]."
                show toju toju01
                show toju_hypno_eyes
                with dissolve
                y "good girl."
                menu:
                    "get naked":
                        ju "n...nnn....."
                        hide toju_hypno_eyes with Dissolve(1.0)
                        ju "wh...what's going on?"
                        y "oh. um."
                        show toju_blink with dissolve
                        ju "i have... a headache..."
                        ju "i think i need to lie down."
                        hide toju toju01 with dissolve
                        y "ah, balls."
                        $ june_convo_today = True
                        jump inside_tavern_shack
                    "kneel":

                        ju "y-yes..."
                        show toju_hypno_eyes:
                            ypos 750
                            linear 1.0 ypos 900
                        show toju toju01:
                            ypos 750
                            linear 1.0 ypos 900
                        $ renpy.pause(1,hard=True)
                        ym "perfect."
                        y "*ahem*"
                        y "[trigger]."
                        hide toju_hypno_eyes with Dissolve(1.0)
                        ju "wha... what?"
                        show toju toju01:
                            ypos 900
                        show expression "bk3/june/idles/angry.png":
                            ypos 180
                        with dissolve
                        ju "what the hell?"
                        y "what are you doing?"
                        ju "what are {i}you{/i} doing!?"
                        y "just standing here. you just knelt down in front of me."
                        y "you haven't been blowing the customers, have you?"
                        show toju toju04
                        hide expression "bk3/june/idles/angry.png"
                        with dissolve
                        ju "I... i don't know....!"
                        hide toju toju04
                        show toju toju01
                        show toju_blink
                        with Dissolve(1.0)
                        ju "....avatar, i have decided to take you up on your hypnotic sessions."
                        y "oh, have you?"
                        ju "i... do not wish this to happen again."
                        hide toju toju01
                        hide toju_blink
                        with dissolve
                        y "it's working....."
                        $ june_talk +=1
                        $ june_convo_today = True
                        jump inside_tavern_shack

            if june_talk ==5 and june_hypno ==1:
                show toju toju01
                with dissolve
                ju "yes?"
                y "come by the hypno room for another session."
                ju "very well."
                if hypnoroom == "none":
                    $ hypnoroom = "june"
                    y "great, see you there."
                if hypnoroom == "june":
                    y "I'm still waiting on you to get over to the hypno-room."
                    ju "well, i'm waiting on you for the same thing."
                    y "oh. erm. whatever."
                else:
                    y "oh, wait, i have an appointment there already."
                    y "i'll take care of that first, then come tell you when it's free."
                    ju "...."
                $ june_convo_today = True
                jump inside_tavern_shack

            if june_talk ==5 and june_hypno ==2:
                if not wench_outfit:
                    y "(i should get a wench outfit before i talk to her again.)"
                    jump inside_tavern_shack
                if wench_outfit:
                    show toju toju02
                    with dissolve
                    ju "hello, ma-"
                    ju "...avatar."
                    ym "(she almost said \"master\"! it's working!)"
                    y "i brought your new uniform."
                    ju "my new..."
                    show toju toju03 with dissolve
                    ju "no. fucking. way."
                    ju "avatar."
                    y "(wait... did it not work?)"
                    ya "put it on."
                    ju "......."
                    ju "fine! but i'm changing in the back!"
                    hide toju toju03 with dissolve
                    y "holy shit, it worked."
                    y "i mean... she's a little feisty about it, but still-"
                    show toju toju11 with Dissolve(1.0)
                    show ctc
                    pause
                    hide ctc
                    ju "here, you bastard."
                    y "whoo!"
                    y "nice!"
                    show toju toju09
                    show toju_blink
                    with dissolve
                    ju "well... i will admit that i pull it off."
                    ym "no need for that yet."
                    show toju toju08
                    hide toju_blink
                    with dissolve
                    ju "what!?"
                    show toju toju11 with dissolve
                    ju "that will {i}never{/i} happen."
                    y "calm your tits, girl."
                    y "and serve some drinks."
                    ju "ugh, i'm going to my room."
                    hide toju toju11 with dissolve
                    $ june_talk +=1
                    $ june_convo_today = True
                    jump inside_tavern_shack

            if june_talk ==6 and june_hypno ==2:
                show toju toju09
                with dissolve
                ju "yes?"
                y "come by the hypno room for another session."
                ju "very well."
                if hypnoroom == "none":
                    $ hypnoroom = "june"
                    y "great, see you there."
                if hypnoroom == "june":
                    y "I'm still waiting on you to get over to the hypno-room."
                    ju "well, i'm waiting on you for the same thing."
                    y "oh. erm. whatever."
                else:
                    y "oh, wait, i have an appointment there already."
                    y "i'll take care of that first, then come tell you when it's free."
                    ju "...."
                $ june_convo_today = True
                jump inside_tavern_shack

            if june_talk ==6 and june_hypno ==3:
                show toju toju12
                with dissolve
                ju "hello, avatar."
                ju "I'm glad-"
                show toju toju11 with dissolve
                ju "i'm glad to see y-"
                show toju toju12 with dissolve
                ju "I'm glad to see you."
                y "(....what was that?)"
                ju "i was thinking..."
                show toju_blink with dissolve
                ju "you've been very kind to let me stay, so i figured i'd split my tips with you."
                ju "it's only fair, since i'm staying here for free."
                hide toju_blink with dissolve
                ju "so, here you go."
                $ emoney +=17
                play sound "audio/money.mp3"
                "you got 17 coins!"
                y "neat."
                ju "now, if you'll excuse me, there's a customer over there that i need to serve."
                ju "he's-"
                show toju toju11 with dissolve
                ju "he's handsome and i need to be nice to hi-"
                show toju toju12 with dissolve
                ju "-to be nice to him."
                ju "bye!"
                hide toju toju12 with dissolve
                y "....what is happening with her?"
                y "i guess she's trying to fight it."
                $ june_talk +=1
                $ june_convo_today = True
                jump inside_tavern_shack

            if june_talk ==7 and june_hypno ==3:
                show toju toju09
                with dissolve
                ju "yes?"
                y "come by the hypno room for another session."
                ju "very well."
                if hypnoroom == "none":
                    $ hypnoroom = "june"
                    y "great, see you there."
                if hypnoroom == "june":
                    y "I'm still waiting on you to get over to the hypno-room."
                    ju "well, i'm waiting on you for the same thing."
                    y "oh. erm. whatever."
                else:
                    y "oh, wait, i have an appointment there already."
                    y "i'll take care of that first, then come tell you when it's free."
                    ju "...."
                $ june_convo_today = True
                jump inside_tavern_shack

            if june_talk ==7 and june_hypno ==4:
                show toju toju09
                with dissolve
                ju "hello, ava-"
                ya "[trigger]."
                show toju toju10
                show toju_hypno_eyes
                with Dissolve(1.0)
                ya "take out your fucking tits."
                show toju toju11
                hide toju_hypno_eyes
                show toju_hypno_eyes
                with Dissolve(1.0)
                ju "hnn....nn...gh...."
                ya "do it!"
                show toju toju12
                hide toju_hypno_eyes
                show toju_hypno_eyes
                with Dissolve(1.0)
                ju "of... course..."
                show toju toju13
                hide toju_hypno_eyes
                show toju_hypno_eyes
                with dissolve
                ju ".........."
                ju "...................."
                show toju toju16
                hide toju_hypno_eyes
                show toju_hypno_eyes
                with Dissolve(1.0)
                show ctc
                pause
                hide ctc
                y "grab them."
                show toju toju17
                hide toju_hypno_eyes
                show toju_hypno_eyes
                with dissolve
                show ctc
                pause
                hide ctc
                ju "yes... m-mas.... sir..."
                y "play with your big, juicy fucking tits!"
                show toju toju100
                hide toju_hypno_eyes
                show toju_hypno_eyes
                show ctc
                pause
                hide ctc
                y "you're a slut."
                ju "I'm... a slut..."
                y "a useless fucking bitch."
                ju "i'm... a useless... fucking... bitch..."
                y "now i'm going to wake you up."
                y "when i do, you're going to keep playing with them, and you're going to thank me."
                ju "i will... keep playing... and thank you..."
                y "[trigger]."
                show toju toju17
                hide toju_hypno_eyes
                with dissolve
                show ctc
                pause
                hide ctc
                ju "wha..."
                y ".....yes?"
                ju ".............."
                show toju toju100
                show ctc
                pause
                hide ctc
                y "good girl."
                y "i think that's enough."
                show toju toju16 with dissolve
                y "put them away."
                show toju toju13 with dissolve
                ju "of course."
                show toju toju12 with dissolve
                ju "have a good-"
                show toju toju11 with dissolve
                ju "a good ni-"
                show toju toju12 with dissolve
                ju "a good night. and thank you."
                hide toju toju12 with dissolve
                $ june_talk +=1
                $ june_convo_today = True
                jump inside_tavern_shack

            if june_talk ==8 and june_hypno ==4:
                show toju toju09
                with dissolve
                ju "always nice to see you, avatar."
                y "come by the hypno room for another session."
                ju "very well."
                if hypnoroom == "none":
                    $ hypnoroom = "june"
                    y "great, see you there."
                if hypnoroom == "june":
                    y "I'm still waiting on you to get over to the hypno-room."
                    ju "well, i'm waiting on you for the same thing."
                    y "oh. erm. whatever."
                else:
                    y "oh, wait, i have an appointment there already."
                    y "i'll take care of that first, then come tell you when it's free."
                    ju "...."
                $ june_convo_today = True
                jump inside_tavern_shack

            if june_talk ==8 and june_hypno ==5:
                show toju toju12
                with dissolve
                ju "always nice to see you."
                y "hey june."
                y "as your boss, i'm worried about your hygiene."
                show toju toju11 with dissolve
                ju "that doesn't really seem like your concern, avatar."
                y "I disagree."
                ju "i don't care what-"
                y "[trigger]."
                show toju toju12
                show toju_hypno_eyes
                with dissolve
                ju "...."
                y "show me your cunt."
                ju "........."
                $ june_pubes = 'bush'
                show toju toju18
                show toju_panties
                with dissolve
                show ctc
                pause
                hide ctc
                y "that's what i thought. bush."
                y "drop your panties."
                ju "....."
                show toju_panties:
                    ypos 720
                    linear 4.0 ypos 770
                show ctc
                pause
                hide ctc
                y "yeah..."
                menu:
                    "shave it":
                        $ temp_boolean = 1
                        y "when i wake you up, you're going to go to the back and shave your pussy."
                        y "understand?"
                        ju "shave... my... pussy..."
                    "keep it":
                        $ temp_boolean = 2
                        y "when i wake you up, you're going to want to keep that bush."
                        y "understand?"
                        ju "keep... my... pussy... hairy..."

                y "good girl."
                y "oh, and leave your panties back there."
                y "you won't need them any more."
                y "[trigger]."
                hide toju_hypno_eyes with dissolve
                ju "what the..."
                show toju_blush with dissolve
                ju "i... have to go take care of something...."
                hide toju_blush
                hide toju_panties
                hide toju toju18
                with dissolve
                y "....."
                y ".........."
                if temp_boolean ==1:
                    $ june_pubes = 'shaven'
                else:
                    $ june_pubes = 'bush'
                show toju toju12
                show toju_blush
                with dissolve
                ju "i... have something to show you."
                if june_pubes == 'shaven':
                    show toju toju23 with dissolve
                else:
                    show toju toju18 with dissolve
                show ctc
                pause
                hide ctc
                ju "is it... to your liking?"
                y "yes, indeed."
                ju "i'm glad."
                y "now go take care of your customers."
                ju "yes, mas... sir."
                hide toju toju23
                hide toju toju18
                hide toju_blink
                with dissolve
                $ june_talk +=1
                $ june_convo_today = True
                jump inside_tavern_shack

            if june_talk ==9 and june_hypno ==5:
                show toju toju12
                with dissolve
                ju "hello."
                y "come by the hypno room for another session."
                ju "very well."
                if hypnoroom == "none":
                    $ hypnoroom = "june"
                    y "great, see you there."
                if hypnoroom == "june":
                    y "I'm still waiting on you to get over to the hypno-room."
                    ju "well, i'm waiting on you for the same thing."
                    y "oh. erm. whatever."
                else:
                    y "oh, wait, i have an appointment there already."
                    y "i'll take care of that first, then come tell you when it's free."
                    ju "...."
                $ june_convo_today = True
                jump inside_tavern_shack

            if june_talk ==9 and june_hypno ==6:
                show toas toas03:
                    xpos 400
                    linear 1.0 xpos 0
                $ renpy.pause(1,hard=True)
                show ctc
                pause
                hide ctc
                ju "let's see... he wanted a water and-"
                show toas toas04 with dissolve
                ju "oh!"
                ju "what-"
                show toas toas05 with dissolve
                show ctc
                pause
                hide ctc
                ju "av... avatar...!"
                ju "what are you doing!?"
                show toas_restrain with dissolve
                show toas toas05:
                    xpos 0
                show ctc
                pause
                hide ctc
                ju "ohh... f... fuck...."
                y "you like having your cunt on display?"
                ju "ngh..."
                y "does the filthy little wench like putting her pussy on display?"
                ju "f...fuck..."
                y "well, i have good news, slut."
                y "i'm going to spank your thick, juicy ass."
                y "right here in the middle of the room."
                ju "........."
                show toas_ass_slap
                y "ready?"
                ju "....yes...."
                y "what?"
                ju "spank my ass, boss!"
                hide toas_ass_slap
                $ generic_counter = 0
                show toas_assblush:
                    alpha 0.0
                    linear 3.0 alpha 1.0
                while generic_counter <= 3:

                    show toas_ass_slap:
                        xpos 480 ypos 300
                    play sound "audio/slap.mp3"
                    show toas_blink
                    pause 0.2
                    hide toas_blink
                    $ generic_counter += 1
                    pause 0.5
                    if generic_counter == 4:
                        ju "oh fuck, yes!"
                        y "look at your waitress, everybody!"
                        y "she's a filthy fucking slut."
                        ju "*mmm....* *ngh...*"
                        y "this perfect, big, firm ass..."
                        menu:
                            "slap some more":
                                $ generic_counter = 0
                            "I'm done":
                                show toas_assblush:
                                    linear 3.0 alpha 0.0

                hide toas_ass_slap
                hide toas_restrain with Dissolve(1.5)
                show toas_handrub
                show ctc
                pause
                hide ctc
                ju "what are you..."
                ju "oh, av..."
                ju "oh yes..."
                ju "oh, spirits..."
                show toas_blink with dissolve
                ju "i'm... i'm going to..."
                ju "keep... keep rubbing..."
                hide toas_blink
                show toas_restrain
                with dissolve
                ju "don't... don't stop..."
                ju "ahh... ahhhhh...."
                show toas_blink with vshake
                ju "{size=+5}fffuuucck!"
                ju "......"
                ju "st...stop... please..."
                hide toas_handrub with dissolve
                ju "........"
                hide toas_blink with dissolve
                ju "thank.... thank you....."
                show toas toas04 with dissolve
                y "i'll see you later, bitch."
                ju "....ungh...."
                $ june_talk +=1
                $ june_convo_today = True
                jump inside_tavern_shack

            if june_talk ==10 and june_hypno ==6:
                show toju toju12
                with dissolve
                ju "hello."
                y "come by the hypno room for another session."
                ju "very well."
                if hypnoroom == "none":
                    $ hypnoroom = "june"
                    y "great, see you there."
                if hypnoroom == "june":
                    y "I'm still waiting on you to get over to the hypno-room."
                    ju "well, i'm waiting on you for the same thing."
                    y "oh. erm. whatever."
                else:
                    y "oh, wait, i have an appointment there already."
                    y "i'll take care of that first, then come tell you when it's free."
                    ju "...."
                $ june_convo_today = True
                jump inside_tavern_shack

            if june_talk ==10 and june_hypno ==7:
                show toju toju16 with dissolve
                ju "hello!"
                y "what are you doing?"
                ju "what?"
                show toju toju17 with dissolve
                ju "oh, sorry!"
                show toju toju100
                show ctc
                pause
                hide ctc
                y "is there a reason why you're... dressed this way?"
                ju "is it not satisfactory?"
                show toju toju17 with dissolve
                ju "i suppose... yes... i should undress, shouldn't i?"
                hide toju toju17 with dissolve
                if june_pubes == 'shaven':
                    show toju toju21 with dissolve
                else:
                    show toju toju19 with dissolve
                show ctc
                pause
                hide ctc
                y "huh."
                y "that is better."
                if june_pubes == 'shaven':
                    show toju toju22 with dissolve
                else:
                    show toju toju20 with dissolve
                ju "thanks."
                ju "well, i guess i'll serve some tables."
                hide toju toju22
                hide toju toju20
                with dissolve
                show toas toas01:
                    xpos 400
                    linear 1.0 xpos 0
                $ renpy.pause(1, hard=True)
                show ctc
                pause
                hide ctc
                ju "those idiots left me with their mess..."
                show toas toas02
                ju "um... avatar...?"
                show ctc
                pause
                hide ctc
                ju "you're... looking a little..."
                show toas_ass_slap
                ju "what are you gonna-"
                show toas_restrain
                show toas toas02:
                    xpos 0
                hide toas_ass_slap
                $ generic_counter = 0
                show toas_assblush:
                    alpha 0.0
                    linear 3.0 alpha 1.0
                while generic_counter <= 3:

                    show toas_ass_slap:
                        xpos 480 ypos 300
                    play sound "audio/slap.mp3"
                    show toas_blink
                    pause 0.2
                    hide toas_blink
                    $ generic_counter += 1
                    pause 0.5
                    if generic_counter == 4:
                        ju "fuck yes!"
                        y "you're a filthy fucking slut."
                        ju "*mmm....* *ngh...*"
                        y "this perfect, big, firm ass..."
                        menu:
                            "slap some more":
                                $ generic_counter = 0
                            "I'm done":
                                show toas_assblush:
                                    linear 3.0 alpha 0.0

                hide toas_ass_slap
                hide toas_restrain with Dissolve(1.5)
                show toas_handrub
                show ctc
                pause
                hide ctc
                ju "nghh..."
                show toas_blink with dissolve
                ju "i'm... going to..."
                ju "keep... keep rubbing..."
                hide toas_blink
                show toas_restrain
                with dissolve
                ju "don't...s-stop..."
                ju "ahh... ahhhhh...."
                show toas_blink with vshake
                ju "{size=+5}fffuuucck!"
                ju "......"
                ju "st...stop... please..."
                hide toas_handrub with dissolve
                ju "........"
                hide toas_blink with dissolve
                ju "thank.... thank you....."
                y "i'll see you later, bitch."
                ju "....ungh...."
                $ june_convo_today = True
                $ june_talk +=1
                jump inside_tavern_shack

            if june_talk >=11 and june_hypno >=7:
                show toju toju16 with dissolve
                ju "hello!"
                show toju toju17 with dissolve
                show toju toju100
                show ctc
                pause
                hide ctc
                ju "is this satisfactory?"
                y "well..."
                show toju toju16 with dissolve
                jump june_stuff_menu

                label june_stuff_menu:
                    menu:
                        "iroh's missing panties" if iroh_panty_hunt ==2:
                            y "did you take iroh's panties?"
                            ju "....i've done many things in my life...."
                            ju "but i can promise you..."
                            ju "with absolute surety..."
                            ju "i have zero interest in that."
                            y "sounds like you've got a beef with him?"
                            ju "he comes in every once in a while."
                            ju "he's... a little handsy."
                            y "right..."
                            y "well, thanks anyway."
                            jump june_stuff_menu
                        "about your bush...":

                            menu:
                                "clean shaven":
                                    $ june_pubes = 'shaven'
                                    ju "yes, sir."
                                    jump june_stuff_menu
                                "bush":
                                    $ june_pubes = 'bush'
                                    ju "yes, sir."
                                    jump june_stuff_menu
                        "undress":
                            ju "i suppose... yes... i should undress, shouldn't i?"
                            hide toju toju16 with dissolve
                            if june_pubes == 'shaven':
                                show toju toju21 with dissolve
                            else:
                                show toju toju19 with dissolve
                            show ctc
                            pause
                            hide ctc
                            y "that's way better."
                            if june_pubes == 'shaven':
                                show toju toju22 with dissolve
                            else:
                                show toju toju20 with dissolve
                            ju "thanks."
                            show ctc
                            pause
                            hide ctc
                            y "alright, put your clothes back on."
                            ju "....very well."
                            hide toju toju21
                            hide toju toju19
                            hide toju toju22
                            hide toju toju20
                            with dissolve
                            show toju toju16 with dissolve
                            jump june_stuff_menu
                        "serve tables":

                            menu:
                                "nude":
                                    ju "well, i guess i'll serve some tables."
                                    hide toju toju22
                                    hide toju toju20
                                    hide toju toju16
                                    with dissolve
                                    show toas toas01:
                                        xpos 400
                                        linear 1.0 xpos 0
                                    $ renpy.pause(1, hard=True)
                                    show ctc
                                    pause
                                    hide ctc
                                    ju "those idiots left me with their mess..."
                                    show toas toas02
                                    ju "um... avatar...?"
                                    show ctc
                                    pause
                                    hide ctc
                                    ju "you're... looking a little..."
                                    show toas toas02:
                                        xpos 0
                                "clothed":

                                    ju "well, i guess i'll serve some tables."
                                    hide toju toju22
                                    hide toju toju20
                                    hide toju toju16
                                    with dissolve
                                    show toas toas03:
                                        xpos 400
                                        linear 1.0 xpos 0
                                    $ renpy.pause(1, hard=True)
                                    show ctc
                                    pause
                                    hide ctc
                                    ju "those idiots left me with their mess..."
                                    show toas toas04 with dissolve
                                    ju "um... avatar...?"
                                    show toas toas05 with dissolve
                                    ju "oh!"
                                    ju "that's... that's a little breezy..."
                                    show toas toas04:
                                        xpos 0
                                    show ctc
                                    pause
                                    hide ctc

                            show toas_ass_slap
                            ju "what are you gonna-"
                            show toas_restrain
                            hide toas_ass_slap
                            $ generic_counter = 0
                            show toas_assblush:
                                alpha 0.0
                                linear 3.0 alpha 1.0
                            while generic_counter <= 3:

                                show toas_ass_slap:
                                    xpos 480 ypos 300
                                play sound "audio/slap.mp3"
                                show toas_blink
                                pause 0.2
                                hide toas_blink
                                $ generic_counter += 1
                                pause 0.5
                                if generic_counter == 4:
                                    ju "fuck yes!"
                                    y "you're a filthy fucking slut."
                                    ju "*mmm....* *ngh...*"
                                    y "this perfect, big, firm ass..."
                                    menu:
                                        "slap some more":
                                            $ generic_counter = 0
                                        "I'm done":
                                            show toas_assblush:
                                                linear 3.0 alpha 0.0

                            hide toas_ass_slap
                            hide toas_restrain with Dissolve(1.5)
                            show toas_handrub
                            show ctc
                            pause
                            hide ctc
                            ju "nghh..."
                            show toas_blink with dissolve
                            ju "i'm... going to..."
                            ju "keep... keep rubbing..."
                            hide toas_blink
                            show toas_restrain
                            with dissolve
                            ju "don't...s-stop..."
                            ju "ahh... ahhhhh...."
                            show toas_blink with vshake
                            ju "{size=+5}fffuuucck!"
                            ju "......"
                            ju "st...stop... please..."
                            ju "it's... sensitive..."
                            hide toas_handrub with dissolve
                            ju "........"
                            hide toas_blink with dissolve
                            ju "thank.... thank you....."
                            y "i'll see you later, bitch."
                            ju "....ungh...."
                            $ june_convo_today = True
                            jump inside_tavern_shack
                        "get squanchy":

                            if june_hypno <=9:
                                if get_squanchy_talk:
                                    y "(i think she needs more hypnosis sessions.)"
                                    jump june_stuff_menu
                                else:
                                    y "get on my squanch!"
                                    ju "um... that's... a little much, i think."
                                    ju "i'm mean, you're my employer..."
                                    y "[trigger]."
                                    show toju_hypno_eyes
                                    with dissolve
                                    ju "...."
                                    y "squanch on my dick!"
                                    ju "....n-no...."
                                    y "damn."
                                    y "guess she needs more hypnosis sessions."
                                    y "[trigger]."
                                    hide toju_hypno_eyes with dissolve
                                    $ get_squanchy_talk = True
                                    jump june_stuff_menu
                            else:
                                menu:
                                    "thigh job":
                                        $ june_convo_today = True
                                        y "i'm going to fuck your thick thighs, june."
                                        ju "right now?"
                                        ju "but I'm... in the middle of my workday."
                                        y "yeah, right now."
                                        y "take your clothes off and get in the back."
                                        y "....and wait there."
                                        ju "......"
                                        show toju_blink with dissolve
                                        ju "mmmm...."
                                        ju "....okay."
                                        hide toju
                                        hide toju_blink
                                        with Dissolve(1.0)
                                        y "I'll give her a minute to get ready."
                                        y "......"
                                        y ".............."
                                        y "......................"
                                        ya "{i}{size=+10}ready or not here i come!"
                                        scene black
                                        scene inside_tavern_1
                                        show tojf tojf21
                                        with Dissolve(1.5)
                                        show ctc
                                        pause
                                        hide ctc
                                        ju "there you are."
                                        y ".....holy fuck."
                                        show ctc
                                        pause
                                        hide ctc
                                        ju "so... i'm gonna make you cum with my thighs?"
                                        y "th-that's the plan."
                                        y "(i'm fucking stuttering?)"
                                        y "(damn, this chick is out of my league...)"
                                        ju "well, what are you waiting for?"
                                        show tojf tojf20_2 with dissolve
                                        ju "come on, big boy."
                                        show ctc
                                        pause
                                        hide ctc
                                        ju "don't be shy..."
                                        ju "get a good look."
                                        ju "do you like what you see?"
                                        menu:
                                            "you disgust me":
                                                y "you only have one decent pair of lips..."
                                                y "so stop talking."
                                                show tojf_face_enjoy with dissolve
                                                ju "hngh...."
                                            "you're a goddess":

                                                y "you're gorgeous."
                                                show tojf_blink with dissolve
                                                ju "hmph."
                                                ju "and here i thought you were different..."
                                        hide tojf_face_enjoy
                                        hide tojf_blink
                                        with dissolve
                                        ju "pull out your cock."
                                        show tojf tojf20_1 with dissolve
                                        show ctc
                                        pause
                                        hide ctc
                                        ju "*mmmm...*"
                                        show tojf_blink with dissolve
                                        ju "hey, you know what would be hot?"
                                        hide tojf_blink with dissolve
                                        ju "if you... you know... called me names."
                                        show tojf_blink with dissolve
                                        ju "just... owned me, you know?"
                                        show tojf tojf13 with dissolve
                                        ju "will you do that?"
                                        hide tojf_blink with dissolve
                                        ju "ha... oh my..."
                                        ju "it looks like that got you ready..."
                                        ju "well... no reason to wait..."
                                        ju "unless you don't think i'm worth the semen...."
                                        menu:
                                            "squeeze my cock!":
                                                y "wrap your fat fucking legs around my cock."
                                                ju "yes, master...."
                                                $ june_thigh_boss = True
                                            "please, mistress...":

                                                y "mistress.... please...."
                                                show tojf_blink with dissolve
                                                ju "ugh...."
                                                ju "you disgust me."
                                                $ june_thigh_boss = False

                                        show tojf tojf21
                                        show expression "bk3/june/anal/cover_dick.png":
                                            xpos 473 ypos 460
                                        show expression "bk3/june/anal/cover_thighs.png"
                                        with Dissolve(1.0)
                                        show ctc
                                        pause
                                        hide ctc
                                        if june_thigh_boss:
                                            ju "in... insult me."
                                        else:
                                            ju "you worthless dog."
                                        show expression "bk3/june/anal/cover_dick.png":
                                            xpos 473 ypos 460
                                            linear 1.5 ypos 400
                                            easeout 1.0 ypos 460
                                            repeat
                                        show ctc
                                        pause
                                        hide ctc
                                        if june_thigh_boss:
                                            y "this cunt is all you're good for, slut."
                                            ju "hngh.... while you take advantage of me."
                                        else:
                                            hide tojf_blink with dissolve
                                            ju "....humping just like a dog."
                                            ju "you mewling, useless worm."

                                        if june_thigh_boss:
                                            y "your fat thighs almost redeem your sick needs."
                                            ju "mmm... yes..."
                                            ju "you're right, i am sick..."
                                            ju "please.... take your time...."
                                            ju "enjoy.... enjoy my fat legs.... rub my slit...."
                                        else:

                                            ju "you don't deserve this."
                                            ju "however... i may let you finish..."
                                            show tojf_blink with dissolve
                                            ju "if you beg."
                                            ju "properly."
                                        menu:
                                            "shut up!":
                                                ya "shut up!"
                                                hide tojf_blink
                                                ya "my cock is so slathered in your cunt juices, i need to concentrate or i'll slip out."
                                                show tojf_face_enjoy with dissolve
                                                ju "hnnngh..."
                                                ju "so hot."
                                                $ june_thigh_boss = True
                                            "you're incredible, i don't deserve you":

                                                y "you're amazing, so sexy and-"
                                                hide tojf_blink
                                                ju "be quiet."
                                                ju "i demand you speed up."
                                                $ june_thigh_boss = False
                                                show tojf_blink

                                        show expression "bk3/june/anal/cover_dick.png":
                                            xpos 473 ypos 460
                                            linear 0.8 ypos 400
                                            easeout 0.55 ypos 460
                                            repeat
                                        show ctc
                                        pause
                                        hide ctc
                                        ju "don't you... dare stop..."
                                        if june_thigh_boss:
                                            ju "because i'm your bitch-"
                                            ju "-nnghh..."
                                            y "you... just got... fuck... a lot wetter..."
                                        else:
                                            ju "you're just a little bitch."
                                            y "you... you're... fuck... so wet..."

                                        y "June... you slut..."
                                        y "you thick, sexy, slut..."
                                        y "fuck... i'm..."
                                        show expression "bk3/june/anal/cover_dick.png":
                                            xpos 473 ypos 460
                                            linear 0.5 ypos 400
                                            easeout 0.3 ypos 460
                                            repeat
                                        show ctc
                                        pause
                                        hide ctc
                                        hide tojf_blink
                                        hide tojf_face_enjoy
                                        ju "you gonna cum?"
                                        ju "you gonna cum for me?"
                                        ju "gimme that cum."
                                        ju "gimme that cum!"
                                        ju "{size=+7}gimme that cum!"
                                        y "slut!"
                                        play sound "audio/splurt2.ogg"
                                        show expression "bk3/june/anal/cover_dick.png":
                                            xpos 473 ypos 460
                                        show expression "bk3/june/anal/cover_sperm.png"
                                        show tojf_face_enjoy
                                        with flash
                                        ju "yes!"
                                        y "ngh!"
                                        play sound "audio/splurt3.ogg"
                                        with flash
                                        y "anh...."
                                        ju "mm...."
                                        ju "that was... surprising..."
                                        hide tojf_face_enjoy with dissolve
                                        ju "are you warm in there?"
                                        ju "trapped between my thighs?"
                                        show tojf_blink with dissolve
                                        ju "i guess i should let you go..."
                                        hide expression "bk3/june/anal/cover_dick.png"
                                        hide expression "bk3/june/anal/cover_thighs.png"
                                        hide expression "bk3/june/anal/cover_sperm.png"
                                        show expression "bk3/june/anal/cover_sperm.png":
                                            ypos -50
                                        hide tojf_blink
                                        show tojf tojf20_1
                                        with dissolve
                                        show ctc
                                        pause
                                        hide ctc
                                        ju "mmm..."
                                        ju "thank... you."
                                        ju "this was... amazing."
                                        ju "come see me... um..."
                                        ju "any time."
                                        $ june_thighs = True
                                        scene black with Dissolve(1.5)
                                        "worn out, you head home for the night."
                                        $ bk3_day = False
                                        jump bk3_next
                                    "fuck":

                                        $ june_convo_today = True
                                        if june_hypno >=11 and june_thighs:
                                            $ june_fucked = True
                                            y "i'm going to put my cock inside you."
                                            ju "don't tease me..."
                                            y "get naked and go in the back."
                                            ju "why don't i start here?"
                                            hide toju toju16 with dissolve
                                            if june_pubes == 'shaven':
                                                show toju toju22 with dissolve
                                            else:
                                                show toju toju20 with dissolve
                                            show ctc
                                            pause
                                            hide ctc
                                            ju "come quick...."
                                            hide toju toju22
                                            hide toju toju20
                                            with dissolve
                                            scene black with dissolve
                                            scene inside_tavern_1
                                            show tojf tojf21
                                            with dissolve
                                            ju "i'm ready for you, avatar."
                                            y "you say that now..."
                                            y "now, let's see that kitty."
                                            show tojf tojf20_2 with dissolve
                                            ju "you mean this?"
                                            show ctc
                                            pause
                                            hide ctc
                                            ju "so... are you... gonna take out your cock?"
                                            y "yeah. obviously. shush."
                                            show tojf tojf20_1 with dissolve
                                            ju "mmmm... is that really going up inside me?"
                                            y "you better believe it."
                                            y "so where do you want it?"
                                            ju "would you... put it..."
                                            show tojf_blink with dissolve
                                            ju "...in my ass?"
                                            ju "i want to be degraded."
                                            ju "I want to be owned."
                                            hide tojf_blink
                                            ju "I want you to fill me in the most private, forbidden, untouched places."
                                            y "really? well, if you insist..."
                                            y "lift your pussy a bit higher."
                                            ju "...."
                                            show tojf tojf20 with dissolve
                                            ju "okay..."
                                            show ctc
                                            pause
                                            hide ctc
                                            ju "why-"
                                            show tojf_finger_solo with dissolve
                                            ju "...don't be naughty, now..."
                                            ju "that's not the right hole..."
                                            show ctc
                                            pause
                                            hide ctc
                                            y "do you really think i'm not going to play with this beautiful pussy while i have the chance?"
                                            y "besides, we need to get you nice and relaxed...."
                                            show tojf_fingerin
                                            hide tojf_finger_solo
                                            show tojf_face_enjoy with dissolve
                                            ju "hgh...ohh..."
                                            show ctc
                                            pause
                                            hide ctc
                                            y "where's my finger?"
                                            ju "In... inside me..."
                                            ju "you're finger-fucking my cunt..."
                                            ju "and it's... ah... ah... goood..."
                                            y "well...."
                                            y "now that we've got you nice and wet..."
                                            hide tojf_fingerin with Dissolve(1.2)
                                            hide tojf_face_enjoy
                                            show tojf tojf17 with Dissolve(1.2)
                                            y "you're going to lubricate my cock."
                                            show tojf tojf13 with dissolve
                                            ju "{i}finally."
                                            show tojf tojf101
                                            ju "here..."
                                            show ctc
                                            pause
                                            hide ctc
                                            ju "rub my pussy juice on my asshole... with your cock..."
                                            ju "mmm... you're... such a tease..."
                                            ju "you're about to be in here..."
                                            show tojf_blink with dissolve
                                            ju "you can come... in... whenever you want..."
                                            y "fuck... you have a great little cunt, slut."
                                            hide tojf_blink with dissolve
                                            ju "mmmhmm..."
                                            y "alright, i thnk that's enough..."
                                            show tojf tojf17 with dissolve
                                            y "ready?"
                                            show tojf_blink with dissolve
                                            ju "i thi-"
                                            show tojf tojf05
                                            hide tojf_blink
                                            with dissolve
                                            ju "hnaahh....."
                                            show ctc
                                            pause
                                            hide ctc
                                            ju "fu...fu...{size=+5}fuck!"
                                            ya "god damn that's tight!"
                                            ya "shit!"
                                            ju "don't... don't move yet..."
                                            ju "let me... adjust... a little..."
                                            show tojf tojf04 with dissolve
                                            show ctc
                                            pause
                                            hide ctc
                                            ju "ahh.... fu...."
                                            ju "........"
                                            show tojf tojf01
                                            show tojf_blink
                                            with vshake
                                            ju "ahhh...!!"
                                            y "nngh...."
                                            show ctc
                                            pause
                                            hide ctc
                                            ju "my... my fucking asshole... it's..."
                                            ju "ahh... it's so... ow... fuck... good..."
                                            ju "just... just don't... don't move..."
                                            ju "I'll... i'll do it..."
                                            show tojf tojf102
                                            show ctc
                                            pause
                                            hide ctc
                                            y "damn you're a firm little whore..."
                                            y "it's almost like you haven't had a cock up here before."
                                            ju "i... haven't..."
                                            hide tojf_blink with dissolve
                                            ju "so... ungh... painful... but..."
                                            ju "so... goood..."
                                            ju "more... i need..."
                                            ju "I need..."
                                            show ctc
                                            pause
                                            hide ctc
                                            show tojf tojf103
                                            ju "{size=+7}more!"
                                            show ctc
                                            pause
                                            hide ctc
                                            ju "yes! yes!"
                                            ju "yes, avatar! fuck me!"
                                            ju "fuck my stupid butthole!"
                                            ju "I'm not letting you out of my ass until you fill it!"
                                            show ctc
                                            pause
                                            hide ctc
                                            show tojf tojf104
                                            show ctc
                                            pause
                                            hide ctc
                                            ju "i'm going to ride you until you give me your load!"
                                            ju "deep in my asshole!"
                                            ju "do it!"
                                            ju "do it, avatar!"
                                            show ctc
                                            pause
                                            hide ctc
                                            show tojf tojf105
                                            show ctc
                                            pause
                                            hide ctc
                                            ju "cum in your bitch!"
                                            ju "cum in your disgusting whore!"
                                            y "fuck, i'm..."
                                            ju "there's... there's so much cock up my ass!"
                                            y "I'm gonna cum!"
                                            ju "yes! yes! do it!"
                                            menu:
                                                "cum in ass":
                                                    show tojf tojf02
                                                    ju "fuck!"
                                                    play sound "audio/splurt2.ogg"
                                                    with flash
                                                    ju "ohh!"
                                                    play sound "audio/splurt3.ogg"
                                                    with flash
                                                    ju "it's... it's inside me!"
                                                    ju "your semen is inside-"
                                                    play sound "audio/splurt2.ogg"
                                                    with flash
                                                    y "nngh...."
                                                    ju "I can just tell there's gonna be a mess...."
                                                    show tojf tojf20
                                                    show tojf_spermass
                                                    with Dissolve(1.0)
                                                    ju "mmmm...."
                                                    hide tojf_face_enjoy
                                                    ju "how does it look?"
                                                    show ctc
                                                    pause
                                                    hide ctc
                                                    y "...messy."
                                                    ju "good."
                                                    ju "there's just something so... satisfying..."
                                                    ju "about taking a load of hot cum up my ass."
                                                    ju "i feel... empty without your cock up there, though..."
                                                    ju "wanna go again?"
                                                    y "i think i need to recover..."
                                                    ju "aw..."
                                                    ju "okay, well... i'll see you later right?"
                                                    y "of course. you've got an ass that needs filling."
                                                    show tojf_blink with dissolve
                                                    ju "mmmmm..."
                                                    scene black with dissolve
                                                    "worn out, you head home for the night."
                                                    jump bk3_next
                                                "cum outside":


                                                    show tojf tojf13
                                                    show tojf_face_enjoy
                                                    ju "fuck!"
                                                    play sound "audio/splurt2.ogg"

                                                    show expression "bk3/june/anal/sperm1.png"
                                                    with flash
                                                    show ctc
                                                    pause
                                                    hide ctc
                                                    ju "ohh!"
                                                    play sound "audio/splurt3.ogg"
                                                    show expression "bk3/june/anal/sperm2.png"

                                                    with flash
                                                    show ctc
                                                    pause
                                                    hide ctc
                                                    ju "it's... it's on me!"
                                                    ju "your semen is on-"
                                                    play sound "audio/splurt2.ogg"
                                                    show expression "bk3/june/anal/sperm3.png"
                                                    show tojf tojf20_1
                                                    with flash
                                                    show ctc
                                                    pause
                                                    hide ctc
                                                    y "nngh...."
                                                    ju "this is such a mess...."
                                                    ju "i really wanted it inside me, but..."
                                                    ju "mmmm...."
                                                    ju "how does it look?"
                                                    show ctc
                                                    pause
                                                    hide ctc
                                                    y "...messy."
                                                    hide tojf_face_enjoy with dissolve
                                                    ju "good."
                                                    ju "there's just something so... refreshing..."
                                                    ju "about being covered in semen."
                                                    ju "i feel... empty without your cock up there, though..."
                                                    ju "wanna go again?"
                                                    y "i think i need to recover..."
                                                    ju "aw..."
                                                    ju "okay, well... i'll see you later right?"
                                                    y "of course. you've got an ass that needs filling."
                                                    show tojf_blink with dissolve
                                                    ju "mmmmm..."
                                                    scene black with dissolve
                                                    "worn out, you head home for the night."
                                                    jump bk3_next
                                        else:

                                            if june_hypno <=10:
                                                y "let's fuck!"
                                                ju "you're cute, but no."
                                                y "[trigger]."
                                                show toju_hypno_eyes
                                                with dissolve
                                                y "i wanna put my weiner in you."
                                                ju "....n-no...."
                                                y "man..."
                                                y "she probably needs more hypnosis."
                                                y "[trigger]."
                                                hide toju_hypno_eyes with dissolve
                                                jump june_stuff_menu
                                            if not june_thighs:
                                                y "let's fuck!"
                                                ju "you're cute, but no."
                                                y "[trigger]."
                                                show toju_hypno_eyes
                                                with dissolve
                                                y "i wanna put my weiner in you."
                                                ju "....n-no...."
                                                y "man..."
                                                y "maybe i should warm her up to it with a simpler sex act first..."
                                                y "[trigger]."
                                                hide toju_hypno_eyes with dissolve
                                                jump june_stuff_menu


                        "hypno sessions" if get_squanchy_talk:
                            if june_hypno >=11:
                                y "(I don't think she needs any more hypnosis.)"
                                jump june_stuff_menu

                            if june_hypno <=10 or june_thighs:
                                y "come by the hypno room for another session."
                                ju "very well."
                                if hypnoroom == "june":
                                    y "actually, I'm still waiting on you to get over to the hypno-room."
                                    ju "well, i'm waiting on you for the same thing."
                                    y "oh. erm. right."
                                if hypnoroom == "none":
                                    $ hypnoroom = "june"
                                    y "great, see you there."
                                if hypnoroom == "suki":
                                    y "oh, wait, i have an appointment there already."
                                    y "i'll take care of that first, then come tell you when it's free."
                                    ju "...."
                                $ june_convo_today = True
                                jump inside_tavern_shack
                        "exit":

                            $ june_convo_today = True
                            jump bk3_village_background

        "host a quest" if tavern_shack <2:
            "your tavern isn't big enough for this yet!"
            jump inside_tavern_shack
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
                "fuck june's face?"
                menu:
                    "blowjob":
                        jump june_bj1
                    "exit":

                        jump inside_tavern_shack
        "exit":

            stop music 
            play music "audio/Bumba Crossing.mp3"
            jump bk3_village_background


label build_shack1:
    y "yup."
    t "about time."
    t "let's go build you a shack."
    $ avatar_shack = 1
    scene black
    scene villagemap_day_base
    show toi toi04
    with dissolve
    t "pick wherever you want, and we'll put it there."
    t "we'll make this a great village, one building at a time."
    y "why let me decide?"
    show toi_blink with dissolve
    t "well... you're the avatar. i figure you're naturally gifted at bringing people together..."
    t "so you'd know how to build a village."
    hide toi_blink with dissolve
    t "and besides, i don't care enough."
    t "now pick the spot for your house!"
    hide toi toi04 with dissolve
    call screen bk3_buildspot


    if _return == 1:
        $ avatar_shack_xpos = 6
        $ avatar_shack_ypos = 85
        $ position_1 = True
    elif _return == 2:
        $ avatar_shack_xpos = 342
        $ avatar_shack_ypos = 84
        $ position_2 = True
    elif _return == 3:
        $ avatar_shack_xpos = 675
        $ avatar_shack_ypos = 80
        $ position_3 = True
    elif _return == 4:
        $ avatar_shack_xpos = 6
        $ avatar_shack_ypos = 295
        $ position_4 = True
    elif _return == 5:
        $ avatar_shack_xpos = 680
        $ avatar_shack_ypos = 300
        $ position_5 = True
    elif _return == 6:
        $ avatar_shack_xpos = 5
        $ avatar_shack_ypos = 519
        $ position_6 = True
    elif _return == 7:
        $ avatar_shack_xpos = 340
        $ avatar_shack_ypos = 520
        $ position_7 = True
    elif _return == 8:
        $ avatar_shack_xpos = 675
        $ avatar_shack_ypos = 510
        $ position_8 = True
    jump bk3_village_background

label build_tavern1:
    $ tavern_shack = 1
    t "choose the spot for the tavern."
    hide toi toi04 with dissolve
    $ bk3_wood -=5
    $ bk3_steel -=5
    scene black
    scene villagemap_day_base
    with dissolve
    call screen bk3_buildspot


    if _return == 1:
        $ tavern_shack_xpos = 6
        $ tavern_shack_ypos = 85
        $ position_1 = True
    elif _return == 2:
        $ tavern_shack_xpos = 342
        $ tavern_shack_ypos = 84
        $ position_2 = True
    elif _return == 3:
        $ tavern_shack_xpos = 675
        $ tavern_shack_ypos = 80
        $ position_3 = True
    elif _return == 4:
        $ tavern_shack_xpos = 6
        $ tavern_shack_ypos = 295
        $ position_4 = True
    elif _return == 5:
        $ tavern_shack_xpos = 680
        $ tavern_shack_ypos = 300
        $ position_5 = True
    elif _return == 6:
        $ tavern_shack_xpos = 5
        $ tavern_shack_ypos = 519
        $ position_6 = True
    elif _return == 7:
        $ tavern_shack_xpos = 340
        $ tavern_shack_ypos = 520
        $ position_7 = True
    elif _return == 8:
        $ tavern_shack_xpos = 675
        $ tavern_shack_ypos = 510
        $ position_8 = True
    jump bk3_village_background


label hypnosis_room:
    scene black
    scene hypno_room2
    with dissolve
    if hypnoroom == "none":
        y "none of the girls are scheduled to come here."
        menu:
            "exit":
                jump bk3_village_background

    if hypnoroom == "jin":
        if jin_hypno ==6:
            show tojn tojn20 with dissolve
            jin "hey, i'm ready!"
            y "great, go ahead and get in the chair."
            jin "okay!"
            hide hypno_room2
            scene black
            with dissolve
            scene hypno_room1
            show tohy jin01
            with Dissolve(1.5)
            y "make yourself comfortable while i set up the equipment."
            show hypno_rail with Dissolve(1.5)
            y "okay, here we go."
            show expression "bk3/hypno/jin/sclera.png"
            show tohy_jin_eyewest
            show tohy_jin_eyeeast
            show expression "bk3/hypno/jin/eyes_mask.png"
            show hypno_ball:
                alpha 1.0
                xpos 800 ypos 300
                linear 2.0 xpos -100 ypos 260
                alpha 0.0
                pause 2.0
                repeat
            show tohy_jin_blink
            $ renpy.pause(2,hard=True)
            show ctc
            pause
            hide ctc
            y "Focus on the light and listen to my voice."


            hide tohy_jin_eyewest
            hide tohy_jin_eyeeast

            hide expression "bk3/hypno/jin/sclera.png"
            hide expression "bk3/hypno/jin/eyes_mask.png"
            show tohy jin02
            with Dissolve(2.0)


            "Okay I won't need these anymore."

            hide hypno_ball
            hide hypno_glowspot
            hide hypno_rail with Dissolve(2.0)

            y "alright, jin..."
            y "take your clothes off."
            show tohy jin04 with dissolve
            y "good."
            y "now...."
            if ajala_jin_hypno ==0 or ajala_jin_hypno ==1:
                y "(here goes nothing...)"
                y "when you see me..."
                y "you will think..."
                y "...that i am Lee."
                y "that guy you have the hots for."
                y "(it's actually zuko... but she doesn't need to know that.)"
                jin "......."
                y "did you hear me?"
                jin ".............."
                y "...."
                y "okay... i'll say it again."
                y "you will think that {i}i{/i} am Lee."
                y "do you understand?"
                jin "......"
                jin "n... no..."
                y "what?"
                y "you shouldn't be able to disagree..."
                y "we've done enough of these that this should work."
                y "hmm... i should talk to Ajala."
                y "ajala may know what to do."
                if joodee_fuck <=1:
                    y "wait... why haven't I had sex with joodee yet?"
                    y "maybe I should work on fucking her before asking ajala about jin."
                    y "she looks... fertile."
                    y "...where'd that thought come from?"
                    y "whatever. i need to do things in the right order."
                    y "joodee, here i... come."
                    y "heh."

                $ ajala_jin_hypno = 1

            elif ajala_jin_hypno ==2:
                y "let's see about using this hypno prototype."
                "you attach the prototype to your current setup."
                y "\"put the trädel in the stålstycke.\""
                y "what the..."
                y "is this elvish?"
                y "who made this? ikea?"
                y "......"
                y "\"made by ikea\"."
                y "......"
                y "....goddamn it."
                "you try your best to assemble the thing."
                y "i think that's it?"
                "you hear a faint whirring noise as it boots up."
                y "that's a good sign."
                y "okay, it says \"enter command and pull lever\"."
                y "seems simple enough."
                y "...and there's four levers."
                y "and none of them are labelled."
                y "of course."
                y "guess i'll just pull one and hope for the best."
                $ ajala_jin_hypno +=1
                y "you will now think i'm lee!"
                menu:
                    "lever":
                        pass
                    "lever":
                        pass
                    "lever":
                        pass
                    "lever":
                        pass

                "*bbzzzzwrrr....*"
                y "come on..."
                jin "i... will... love..."
                y "yes, come on..."
                jin "....to clean...and to cook..."
                y "...."
                y "well that's... nice, but not what i was going for-"
                "the machine shuts down with a little sad jingle."
                y "what!? oh, no you don't!"
                menu:
                    "kick it":
                        y "come on, you piece of {i}skit{/i}!"
                    "gently pet it":

                        y "wake up... come on... daddy needs a new bitch..."

                "you notice a sticker on the side."
                y "hmm?"
                "\"only works once per day."
                y "...."
                y "damn it, ikea. you ass."
                y "...fine."
                y "we're done for now."

            elif ajala_jin_hypno ==3:
                y "okay, let's try this hypno prototype again."
                "you hear a faint whirring noise as it boots up."
                y "sweet."
                y "okay, gotta \"enter command and pull lever\"."
                y "only three levers left."
                y "guess i'll just pull one and hope for the best."
                $ ajala_jin_hypno +=1
                y "you will now think i'm lee!"
                menu:
                    "lever":
                        pass
                    "lever":
                        pass
                    "lever":
                        pass

                "*bbzzzzwrrr....*"
                y "come on..."
                jin "i... will... love..."
                y "yes, come on..."
                jin "....accordion..."
                y "that's... that's not even close!"
                y "come on!"
                "the machine shuts down with a little sad jingle."
                y "god... damn it."

            elif ajala_jin_hypno ==4:
                y "okay, let's try this hypno prototype again."
                "you hear a faint whirring noise as it boots up."
                y "sweet."
                y "okay, gotta \"enter command and pull lever\"."
                y "only two levers left."
                y "guess i'll just pull one and hope for the best."
                $ ajala_jin_hypno +=1
                y "you will now think i'm lee!"
                menu:
                    "lever":
                        pass
                    "lever":
                        pass

                "*bbzzzzwrrr....*"
                y "come on..."
                jin "i..."
                y "yes, come on..."
                jin "...am stan..."
                y "what?"
                y "no!"
                jin "...sports..."
                y "damn it! jin, come back!"
                jin "...bitches..."
                y "i hope this one's temporary..."

            elif ajala_jin_hypno ==5:
                y "okay, let's try this hypno prototype again."
                "you hear a faint whirring noise as it boots up."
                y "sweet."
                y "okay, gotta \"enter command and pull lever\"."
                y "only one levers left."
                y "this better do it."
                $ ajala_jin_hypno +=1
                y "you will now think i'm lee!"
                menu:
                    "lever":
                        pass

                "*bbzzzzwrrr....*"
                y "come on..."
                jin "i..."
                jin "...you..."
                jin "...are lee..."
                y "yes!"
                y "success!"
                y "holy shit, it finally worked!"

            y "okay, put your clothes back on."
            show tohy jin02 with dissolve
            y "when I snap my fingers, you are going to want to return for more hypnosis."
            jin "more...."
            y "right."
            y "3..."
            y "2..."
            y "1..."
            play sound "audio/fingersnap.mp3"

            show tohy jin01 with Dissolve(2.0)
            if ajala_jin_hypno ==6:
                scene black with dissolve
                scene hypno_room2
                show tojn tojn20
                with dissolve

                y "how do you feel?"
                jin "like...."
                show tojn tojn23 with dissolve
                jin "....lee?"
                jin "why are you here...?"
                show tojn tojn24
                show expression "bk3/jin/idles/fl_blink.png"
                with dissolve
                jin "uunnnhh... fuuuuck..."
                y "(yes... yes!)"
                y "what's wrong?"
                jin "my... my body... is..."
                jin "n...nothing..."
                show tojn tojn25
                hide expression "bk3/jin/idles/fl_blink.png"
                with dissolve
                jin "i'm... unh... happy to... happy to see... ahh... ah..."
                jin "you... i need... i..."
                show tojn tojn23
                show expression "bk3/jin/idles/fl_blink.png"
                show expression "bk3/jin/idles/fl_blush.png"
                with dissolve
                jin "fuuuuckk...."
                y "how about i let you go for now?"
                show tojn tojn24
                hide expression "bk3/jin/idles/fl_blush.png"
                hide expression "bk3/jin/idles/fl_blink.png"
                show expression "bk3/jin/idles/fl_blush.png"
                with dissolve
                jin "hnh... you..."
                jin "you look ni... ah... ngh..."
                show expression "bk3/jin/idles/fl_blink.png"
                with dissolve
                y "go on..."
                jin "o...okay..."
                hide tojn
                hide expression "bk3/jin/idles/fl_blink.png"
                hide expression "bk3/jin/idles/fl_blush.png"
                with dissolve
                "jin hurries out, her legs closely pressed together."
                y "this.... is going to be amazing."
                $ bk3_day = False
                $ hypnoroom = "none"
                $ jin_hypno = 7
                jump bk3_village_background

            if ajala_jin_hypno ==5:
                y "...jin?"
                jin "who's jin?"
                jin "i'm stan. get it right."
                y "*groan*"
                y "stupid machine... why is that even an option?"
                jin "why is what an op-"
                jin "wha..."
                jin "where am i?"
                y "...stan?"
                jin "who?"
                jin "i'm jin, remember?"
                y "oh, thank the spirits."
                jin "i'm definitely feeling a pint and a steak though."
                y "....i can work with that."
                jin "let me know when i can come back."
                jin "bye!"
                hide tohy with dissolve
                $ bk3_day = False
                $ hypnoroom = "none"
                jump bk3_village_background

            jin "uhh.... hey!"
            y "how do you feel?"
            jin "fine."
            jin "i definitely feel like there's more to do, though."
            jin "let me know when i can come back."
            jin "bye!"
            hide tohy with dissolve
            $ bk3_day = False
            $ hypnoroom = "none"
            jump bk3_village_background

        if jin_hypno ==5:
            show tojn tojn20 with dissolve
            jin "hey, i'm ready!"
            y "great, go ahead and get in the chair."
            jin "okay!"
            hide hypno_room2
            scene black
            with dissolve
            scene hypno_room1
            show tohy jin01
            with Dissolve(1.5)
            y "make yourself comfortable while i set up the equipment."
            show hypno_rail with Dissolve(1.5)
            y "okay, here we go."
            show expression "bk3/hypno/jin/sclera.png"
            show tohy_jin_eyewest
            show tohy_jin_eyeeast
            show expression "bk3/hypno/jin/eyes_mask.png"
            show hypno_ball:
                alpha 1.0
                xpos 800 ypos 300
                linear 2.0 xpos -100 ypos 260
                alpha 0.0
                pause 2.0
                repeat
            show tohy_jin_blink
            $ renpy.pause(2,hard=True)
            show ctc
            pause
            hide ctc
            y "Focus on the light and listen to my voice."


            hide tohy_jin_eyewest
            hide tohy_jin_eyeeast

            hide expression "bk3/hypno/jin/sclera.png"
            hide expression "bk3/hypno/jin/eyes_mask.png"
            show tohy jin02
            with Dissolve(2.0)


            "Okay I won't need these anymore."

            hide hypno_ball
            hide hypno_glowspot
            hide hypno_rail with Dissolve(2.0)

            y "alright, jin..."
            y "take your clothes off."
            show tohy jin04 with dissolve
            y "good."
            y "now...."
            y "when you see Lee, your pussy will start gushing."
            jin "pussy... gushing..."
            y "that's right."
            y "but you will {i}not{/i} act on it."
            jin "i will not... act on... gushing... pussy..."
            y "(oh, i have plans for you... but you'll find that out soon...)"
            y "good."
            y "now put your clothes back on."
            show tohy jin02 with dissolve
            y "when I snap my fingers, you are going to want to return for more hypnosis."
            jin "more...."
            y "right."
            y "3..."
            y "2..."
            y "1..."
            play sound "audio/fingersnap.mp3"

            show tohy jin01 with Dissolve(2.0)
            jin "uhh.... hey!"
            y "how do you feel?"
            jin "great!"
            jin "i definitely feel like there's more to do, though."
            y "well, if that's what you want."
            jin "it is!"
            jin "let me know when i can come back."
            jin "bye!"
            hide tohy with dissolve
            "jin became more submissive!"
            $ bk3_day = False
            $ jin_hypno +=1
            $ hypnoroom = "none"
            jump bk3_village_background

        if jin_hypno ==4:
            show tojn tojn20 with dissolve
            jin "hey, i'm ready!"
            y "great, go ahead and get in the chair."
            jin "okay!"
            hide hypno_room2
            scene black
            with dissolve
            scene hypno_room1
            show tohy jin01
            with Dissolve(1.5)
            y "make yourself comfortable while i set up the equipment."
            show hypno_rail with Dissolve(1.5)
            y "okay, here we go."
            show expression "bk3/hypno/jin/sclera.png"
            show tohy_jin_eyewest
            show tohy_jin_eyeeast
            show expression "bk3/hypno/jin/eyes_mask.png"
            show hypno_ball:
                alpha 1.0
                xpos 800 ypos 300
                linear 2.0 xpos -100 ypos 260
                alpha 0.0
                pause 2.0
                repeat
            show tohy_jin_blink
            $ renpy.pause(2,hard=True)
            show ctc
            pause
            hide ctc
            y "Focus on the light and listen to my voice."


            hide tohy_jin_eyewest
            hide tohy_jin_eyeeast

            hide expression "bk3/hypno/jin/sclera.png"
            hide expression "bk3/hypno/jin/eyes_mask.png"
            show tohy jin02
            with Dissolve(2.0)


            "Okay I won't need these anymore."

            hide hypno_ball
            hide hypno_glowspot
            hide hypno_rail with Dissolve(2.0)

            y "alright, jin..."
            y "take your clothes off."
            show tohy jin04 with dissolve
            y "good."
            y "you are going to start confusing love and lust."
            jin "confuse... love... and... lust..."
            y "when you are horny, you will think that is love..."
            y "and when you feel love, you will feel an overwhelming desire to pleasure that person."
            y "but you will {b}not{/b} act on it. yet."
            jin "i will not... act on... desire to... pleasure..."
            y "good."
            y "now put your clothes back on."
            show tohy jin02 with dissolve
            y "when I snap my fingers, you are going to want to return for more hypnosis."
            jin "more...."
            y "right."
            y "3..."
            y "2..."
            y "1..."
            play sound "audio/fingersnap.mp3"

            show tohy jin01 with Dissolve(2.0)
            jin "uhh.... hey!"
            y "how do you feel?"
            jin "great!"
            jin "i definitely feel like there's more to do, though."
            y "well, if that's what you want."
            jin "it is!"
            jin "let me know when i can come back."
            jin "bye!"
            hide tohy with dissolve
            "jin became more submissive!"
            $ bk3_day = False
            $ jin_hypno +=1
            $ hypnoroom = "none"
            jump bk3_village_background

        if jin_hypno ==3:
            show tojn tojn20 with dissolve
            jin "hey, i'm ready!"
            y "great, go ahead and get in the chair."
            jin "okay!"
            hide hypno_room2
            scene black
            with dissolve
            scene hypno_room1
            show tohy jin01
            with Dissolve(1.5)
            y "make yourself comfortable while i set up the equipment."
            show hypno_rail with Dissolve(1.5)
            y "okay, here we go."
            show expression "bk3/hypno/jin/sclera.png"
            show tohy_jin_eyewest
            show tohy_jin_eyeeast
            show expression "bk3/hypno/jin/eyes_mask.png"
            show hypno_ball:
                alpha 1.0
                xpos 800 ypos 300
                linear 2.0 xpos -100 ypos 260
                alpha 0.0
                pause 2.0
                repeat
            show tohy_jin_blink
            $ renpy.pause(2,hard=True)
            show ctc
            pause
            hide ctc
            y "Focus on the light and listen to my voice."


            hide tohy_jin_eyewest
            hide tohy_jin_eyeeast

            hide expression "bk3/hypno/jin/sclera.png"
            hide expression "bk3/hypno/jin/eyes_mask.png"
            show tohy jin02
            with Dissolve(2.0)


            "Okay I won't need these anymore."

            hide hypno_ball
            hide hypno_glowspot
            hide hypno_rail with Dissolve(2.0)

            y "alright, jin..."
            y "take your clothes off."
            show tohy jin04 with dissolve
            y "good."
            y "you will now get wet whenever i am rude or insulting to you."
            jin "wet... when... insulted..."
            y "great."
            y "now put your clothes back on."
            show tohy jin02 with dissolve
            y "when I snap my fingers, you are going to want to return for more hypnosis."
            jin "more...."
            y "right."
            y "3..."
            y "2..."
            y "1..."
            play sound "audio/fingersnap.mp3"

            show tohy jin01 with Dissolve(2.0)
            jin "uhh.... hey!"
            y "how do you feel?"
            jin "great!"
            jin "i definitely feel like there's more to do, though."
            y "well, if that's what you want."
            jin "it is!"
            jin "let me know when i can come back."
            jin "bye!"
            hide tohy with dissolve
            "jin became more submissive!"
            $ bk3_day = False
            $ jin_hypno +=1
            $ hypnoroom = "none"
            jump bk3_village_background

        if jin_hypno ==2:

            show tojn tojn20 with dissolve
            jin "hey, i'm ready!"
            y "great, go ahead and get in the chair."
            jin "okay!"
            hide hypno_room2
            scene black
            with dissolve
            scene hypno_room1
            show tohy jin01
            with Dissolve(1.5)
            y "make yourself comfortable while i set up the equipment."
            show hypno_rail with Dissolve(1.5)
            y "okay, here we go."
            show expression "bk3/hypno/jin/sclera.png"
            show tohy_jin_eyewest
            show tohy_jin_eyeeast
            show expression "bk3/hypno/jin/eyes_mask.png"
            show hypno_ball:
                alpha 1.0
                xpos 800 ypos 300
                linear 2.0 xpos -100 ypos 260
                alpha 0.0
                pause 2.0
                repeat
            show tohy_jin_blink
            $ renpy.pause(2,hard=True)
            show ctc
            pause
            hide ctc
            y "Focus on the light and listen to my voice."


            hide tohy_jin_eyewest
            hide tohy_jin_eyeeast

            hide expression "bk3/hypno/jin/sclera.png"
            hide expression "bk3/hypno/jin/eyes_mask.png"
            show tohy jin02
            with Dissolve(2.0)


            "Okay I won't need these anymore."

            hide hypno_ball
            hide hypno_glowspot
            hide hypno_rail with Dissolve(2.0)

            y "alright, jin..."
            y "you are now comfortable with nudity."
            jin "i am... i'm now..."
            y "you like being naked."
            jin "i like... i don't... i like..."
            y "you like being naked."
            jin "i like...."
            jin "........"
            jin "being... naked..."
            y "good."
            y "now stand up."

            hide tohy_jin_blink

            hide tohy
            hide expression "ebackgrounds/hypno_room1.jpg"
            show expression "ebackgrounds/hypno_room2.jpg"
            with Dissolve(2.0)

            show tojn tojn20
            show tojn_hypno_eyes
            y "get comfortable."

            show tojn tojn21 with Dissolve(2.0)
            show ctc
            pause
            hide ctc
            y "what are you?"
            jin "i... am... comfortable..."
            y "cool, okay sit in the chair again."

            hide tojn tojn21
            hide tojn_hypno_eyes



            hide expression "ebackgrounds/hypno_room2.jpg"

            show expression "ebackgrounds/hypno_room1.jpg"
            show tohy jin04
            with Dissolve(2.0)
            show ctc
            pause
            hide ctc
            y "since you are now comfortable with nudity..."
            y "you will be willing to undress when i ask it of you."
            jin "willing... to... undress..."
            y "and you will be more submissive to any other requests."
            jin "submissive..."
            y "nice."
            y "now put your clothes back on."
            show tohy jin02 with dissolve
            y "when I snap my fingers, you are going to want to return for more hypnosis."
            jin "more...."
            y "right."
            y "3..."
            y "2..."
            y "1..."
            play sound "audio/fingersnap.mp3"

            show tohy jin01 with Dissolve(2.0)
            jin "uhh.... hey!"
            y "how do you feel?"
            jin "great!"
            jin "i definitely feel like there's more to do, though."
            y "well, if that's what you want."
            jin "it is!"
            jin "let me know when i can come back."
            jin "bye!"
            hide tohy with dissolve
            "jin became more submissive!"
            $ bk3_day = False
            $ jin_hypno +=1
            $ hypnoroom = "none"
            jump bk3_village_background

        if jin_hypno ==1:
            show tojn tojn20 with dissolve
            jin "hey, i'm ready!"
            y "great, go ahead and get in the chair."
            jin "okay!"
            hide hypno_room2
            scene black
            with dissolve
            scene hypno_room1
            show tohy jin01
            with Dissolve(1.5)
            y "make yourself comfortable while i set up the equipment."
            show hypno_rail with Dissolve(1.5)
            y "okay, here we go."
            show expression "bk3/hypno/jin/sclera.png"
            show tohy_jin_eyewest
            show tohy_jin_eyeeast
            show expression "bk3/hypno/jin/eyes_mask.png"
            show hypno_ball:
                alpha 1.0
                xpos 800 ypos 300
                linear 2.0 xpos -100 ypos 260
                alpha 0.0
                pause 2.0
                repeat
            show tohy_jin_blink
            $ renpy.pause(2,hard=True)
            show ctc
            pause
            hide ctc
            y "Focus on the light and listen to my voice."


            hide tohy_jin_eyewest
            hide tohy_jin_eyeeast

            hide expression "bk3/hypno/jin/sclera.png"
            hide expression "bk3/hypno/jin/eyes_mask.png"
            show tohy jin02
            with Dissolve(2.0)


            "Okay I won't need these anymore."

            hide hypno_ball
            hide hypno_glowspot
            hide hypno_rail with Dissolve(2.0)

            y "alright, jin..."
            y "when you hear me say {b}[trigger]{/b}, you will become submissive to my requests."
            jin "i will... be... submissive..."
            y "nice, nice."
            y "when I snap my fingers, you are going to want to return for more hypnosis."
            jin "more...."
            y "right."
            y "3..."
            y "2..."
            y "1..."
            play sound "audio/fingersnap.mp3"

            show tohy jin01 with Dissolve(2.0)
            jin "uhh.... hey!"
            y "how do you feel?"
            jin "great!"
            jin "i definitely feel like there's more to do, though."
            y "well, if that's what you want."
            jin "it is!"
            jin "let me know when i can come back."
            jin "bye!"
            hide tohy with dissolve
            "jin became more submissive!"
            $ bk3_day = False
            $ jin_hypno +=1
            $ hypnoroom = "none"
            jump bk3_village_background


        if jin_hypno ==0:
            show tojn tojn20 with dissolve
            jin "he-hello?"
            y "hey there!"
            y "welcome... take a seat."
            jin "okay...."
            hide hypno_room2
            scene black
            with dissolve
            scene hypno_room1
            show tohy jin01
            with Dissolve(1.5)
            y "make yourself comfortable while i set up the equipment."
            jin "okay..."
            jin "I'm a little nervous!"
            jin "I hope it doesn't show too badly."
            y "you're fine."
            y "aaaand here we go..."
            show hypno_rail with Dissolve(1.5)
            y "a lamp will move along this rail, please follow it with your eyes while listening to my voice."
            jin "o-okay..."
            y "okay, here we go."
            show expression "bk3/hypno/jin/sclera.png"
            show tohy_jin_eyewest
            show tohy_jin_eyeeast
            show expression "bk3/hypno/jin/eyes_mask.png"
            show hypno_ball:
                alpha 1.0
                xpos 800 ypos 300
                linear 2.0 xpos -100 ypos 260
                alpha 0.0
                pause 2.0
                repeat
            show tohy_jin_blink
            $ renpy.pause(2,hard=True)
            show ctc
            pause
            hide ctc
            y "Focus on the light and listen to my voice."


            hide tohy_jin_eyewest
            hide tohy_jin_eyeeast

            hide expression "bk3/hypno/jin/sclera.png"
            hide expression "bk3/hypno/jin/eyes_mask.png"
            show tohy jin02
            with Dissolve(2.0)


            "Okay I won't need these anymore."
            hide hypno_ball
            hide hypno_glowspot
            hide hypno_rail with Dissolve(2.0)
            $ temp_boolean1 = False
            $ temp_boolean2 = False
            while not temp_boolean1 or not temp_boolean2:
                menu:
                    "How often do you masturbate?" if not temp_boolean1:
                        jin "Once a day."
                        jin "Sometimes twice."
                        y "okay, great. that's..."
                        jin "I really like to rub my clit with objects this one guy uses."
                        y "say what now?"
                        jin "what now."
                        y "stop... being sassy."
                        y "I meant... tell me more about that guy."
                        jin "He works at the Jasmine Dragon."
                        y "Are you talking about that old guy!?"
                        jin "No, but I think they're family."
                        jin "He has a big burn scar on the left side of his face."
                        y "...."
                        y "(well, i certainly know that guy....)"
                        y "So.. what kind of objects?"
                        jin "Whatever I can get my hands on."
                        $ temp_boolean1 = True
                    "What is your biggest sexual fantasy" if not temp_boolean2:
                        jin "To be watched having sex."
                        $ temp_boolean2 = True

            "now stand up."

            hide tohy_jin_blink

            hide tohy
            hide expression "ebackgrounds/hypno_room1.jpg"
            show expression "ebackgrounds/hypno_room2.jpg"
            with Dissolve(2.0)
            show tojn tojn20
            show tojn_hypno_eyes
            with dissolve
            y "take off your clothes."
            jin "nnn...nnnooo...."
            y "yeah, i figured."
            y "worth a shot though."
            y "alright, sit back down."
            hide tojn
            hide tojn_hypno_eyes
            hide expression "ebackgrounds/hypno_room2.jpg"

            show expression "ebackgrounds/hypno_room1.jpg"
            show tohy jin02
            with Dissolve(2.0)
            y "okay, jin, when i snap my fingers, you are going to feel amazing."
            y "you're going to feel like a weight has been lifted off of your shoulders..."
            y "...but that there is more still there."
            y "you're going to have this nagging sensation in the back of your mind that someone is trying to control you."
            y "...and i am the only one who can help you."
            y "You'll forget what happened here and return to your normal state of mind in..."
            y "3..."
            y "2..."
            y "1..."
            play sound "audio/fingersnap.mp3"

            show tohy jin01 with Dissolve(2.0)
            jin "whoa...."
            y "how do you feel?"
            jin "amaz... amazing!"
            jin "what did you do?"
            y "i just undid some of the underlying brainwashing."
            y "i think there's still some hiding in there though."
            jin "yeah, i agree..."
            jin "i'm glad we did this!"
            jin "let me know when i can come back!"
            jin "bye!"
            hide tohy with dissolve
            "jin became more submissive!"
            $ bk3_day = False
            $ jin_hypno +=1
            $ hypnoroom = "none"
            jump bk3_village_background

    if hypnoroom == "june":
        if june_thighs:
            show toju toju02 with dissolve
            ju "hello, handsome."
            show toju_blink with dissolve
            ju "i'll just take a seat..."
            hide hypno_room2
            scene black
            with dissolve
            scene hypno_room1
            hide toju_blink
            hide toju toju02
            show tohy june01
            with Dissolve(1.5)
            ju "let's begin."
            show ctc
            pause
            hide ctc
            y "just relax."
            show hypno_rail with Dissolve(1.5)
            y "here we go...."
            show expression "bk3/hypno/june/sclera.png"
            show tohy_june_eyeeast
            show expression "bk3/hypno/june/eyes_mask.png"
            show hypno_ball:
                alpha 1.0
                xpos 800 ypos 300
                linear 2.0 xpos -100 ypos 260
                alpha 0.0
                pause 2.0
                repeat

            show tohy_june_blink
            $ renpy.pause(2,hard=True)
            show ctc
            pause
            hide ctc
            y "Focus on the light and listen to my voice."
            hide tohy_june_eyeeast

            hide expression "bk3/hypno/june/sclera.png"
            hide expression "bk3/hypno/june/eyes_mask.png"
            show tohy june02
            with Dissolve(2.0)
            y "okay, let's put these away..."
            hide hypno_ball
            hide hypno_rail
            with dissolve
            y "take off your clothes."
            show tohy june03 with dissolve
            show ctc
            pause
            hide ctc
            y "june, you are going to be more submissive."
            y "you want to please me sexually."
            y "you will get wet from degredation."
            y "do you understand?"
            ju "I will become more... submissive."
            ya "good!"
            y "put your clothes back on."
            show ctc
            pause
            hide ctc
            show tohy june02 with dissolve
            y "now, you'll forget what happened here and return to your normal state of mind in..."
            y "3... 2... 1..."
            play sound "audio/fingersnap.mp3"

            show tohy june01 with Dissolve(1.5)
            ju "wha..."
            ju "ah, yes."
            ju "thank you for your help."
            y "you're welcome."
            scene hypno_room2 with Dissolve(1.0)
            show toju toju01
            show toju_blink
            with dissolve
            ju "goodbye for now."
            hide toju toju01
            hide toju_blink
            with dissolve
            "june became more submissive!"
            $ bk3_day = False
            $ june_hypno +=1
            $ hypnoroom = "none"
            jump bk3_village_background

        if june_hypno >=7 and june_hypno <=10:
            show toju toju02 with dissolve
            ju "hello, handsome."
            show toju_blink with dissolve
            ju "i'll just take a seat..."
            hide hypno_room2
            scene black
            with dissolve
            scene hypno_room1
            hide toju_blink
            hide toju toju02
            show tohy june01
            with Dissolve(1.5)
            ju "let's begin."
            show ctc
            pause
            hide ctc
            y "just relax."
            show hypno_rail with Dissolve(1.5)
            y "here we go...."
            show expression "bk3/hypno/june/sclera.png"
            show tohy_june_eyeeast
            show expression "bk3/hypno/june/eyes_mask.png"
            show hypno_ball:
                alpha 1.0
                xpos 800 ypos 300
                linear 2.0 xpos -100 ypos 260
                alpha 0.0
                pause 2.0
                repeat

            show tohy_june_blink
            $ renpy.pause(2,hard=True)
            show ctc
            pause
            hide ctc
            y "Focus on the light and listen to my voice."
            hide tohy_june_eyeeast

            hide expression "bk3/hypno/june/sclera.png"
            hide expression "bk3/hypno/june/eyes_mask.png"
            show tohy june02
            with Dissolve(2.0)
            y "okay, let's put these away..."
            hide hypno_ball
            hide hypno_rail
            with dissolve
            y "take off your clothes."
            show tohy june03 with dissolve
            show ctc
            pause
            hide ctc
            y "june, you are going to be more submissive."
            y "you want to please me sexually."
            y "you will get wet from degredation."
            y "do you understand?"
            ju "I will become more... submissive."
            ya "good!"
            y "put your clothes back on."
            show ctc
            pause
            hide ctc
            show tohy june02 with dissolve
            y "now, you'll forget what happened here and return to your normal state of mind in..."
            y "3... 2... 1..."
            play sound "audio/fingersnap.mp3"

            show tohy june01 with Dissolve(1.5)
            ju "wha..."
            ju "ah, yes."
            ju "thank you for your help."
            y "you're welcome."
            scene hypno_room2 with Dissolve(1.0)
            show toju toju01
            show toju_blink
            with dissolve
            ju "goodbye for now."
            hide toju toju01
            hide toju_blink
            with dissolve
            "june became more submissive!"
            $ bk3_day = False
            $ june_hypno +=1
            $ hypnoroom = "none"
            jump bk3_village_background

        if june_hypno ==6:
            show toju toju02 with dissolve
            ju "hello, handsome."
            show toju_blink with dissolve
            ju "i'll just take a seat..."
            hide hypno_room2
            scene black
            with dissolve
            scene hypno_room1
            hide toju_blink
            hide toju toju02
            show tohy june01
            with Dissolve(1.5)
            ju "let's begin."
            show ctc
            pause
            hide ctc
            y "just relax."
            show hypno_rail with Dissolve(1.5)
            y "here we go...."
            show expression "bk3/hypno/june/sclera.png"
            show tohy_june_eyeeast
            show expression "bk3/hypno/june/eyes_mask.png"
            show hypno_ball:
                alpha 1.0
                xpos 800 ypos 300
                linear 2.0 xpos -100 ypos 260
                alpha 0.0
                pause 2.0
                repeat

            show tohy_june_blink
            $ renpy.pause(2,hard=True)
            show ctc
            pause
            hide ctc
            y "Focus on the light and listen to my voice."
            hide tohy_june_eyeeast

            hide expression "bk3/hypno/june/sclera.png"
            hide expression "bk3/hypno/june/eyes_mask.png"
            show tohy june02
            with Dissolve(2.0)
            y "okay, let's put these away..."
            hide hypno_ball
            hide hypno_rail
            with dissolve
            y "take off your clothes."
            show tohy june03 with dissolve
            y "june, you are going to be more submissive."
            y "you are going to start serving drinks naked."
            y "you will get wet from degredation."
            y "do you understand?"
            ju "I will become more... submissive."
            ya "good!"
            y "put your clothes back on."
            show tohy june02 with dissolve
            y "now, you'll forget what happened here and return to your normal state of mind in..."
            y "3... 2... 1..."
            play sound "audio/fingersnap.mp3"

            show tohy june01 with Dissolve(1.5)
            ju "wha..."
            ju "ah, yes."
            ju "thank you for your help."
            y "you're welcome."
            scene hypno_room2 with Dissolve(1.0)
            show toju toju01
            show toju_blink
            with dissolve
            ju "goodbye for now."
            hide toju toju01
            hide toju_blink
            with dissolve
            "june became more submissive!"
            $ bk3_day = False
            $ june_hypno +=1
            $ hypnoroom = "none"
            jump bk3_village_background

        if june_hypno ==5:
            show toju toju02 with dissolve
            ju "hello, handsome."
            show toju_blink with dissolve
            ju "i'll just take a seat..."
            hide hypno_room2
            scene black
            with dissolve
            scene hypno_room1
            hide toju_blink
            hide toju toju02
            show tohy june01
            with Dissolve(1.5)
            ju "let's begin."
            show ctc
            pause
            hide ctc
            y "just relax."
            show hypno_rail with Dissolve(1.5)
            y "here we go...."
            show expression "bk3/hypno/june/sclera.png"
            show tohy_june_eyeeast
            show expression "bk3/hypno/june/eyes_mask.png"
            show hypno_ball:
                alpha 1.0
                xpos 800 ypos 300
                linear 2.0 xpos -100 ypos 260
                alpha 0.0
                pause 2.0
                repeat

            show tohy_june_blink
            $ renpy.pause(2,hard=True)
            show ctc
            pause
            hide ctc
            y "Focus on the light and listen to my voice."
            hide tohy_june_eyeeast

            hide expression "bk3/hypno/june/sclera.png"
            hide expression "bk3/hypno/june/eyes_mask.png"
            show tohy june02
            with Dissolve(2.0)
            y "okay, let's put these away..."
            hide hypno_ball
            hide hypno_rail
            with dissolve
            y "take off your clothes."
            show tohy june03 with dissolve
            y "june, you are going to be more submissive."
            y "you are going to accept what i do."
            y "you will get wet from degredation."
            y "do you understand?"
            ju "I will become more... submissive."
            ya "good!"
            y "put your clothes back on."
            show tohy june02 with dissolve
            y "now, you'll forget what happened here and return to your normal state of mind in..."
            y "3... 2... 1..."
            play sound "audio/fingersnap.mp3"

            show tohy june01 with Dissolve(1.5)
            ju "wha..."
            ju "ah, yes."
            ju "thank you for your help."
            y "you're welcome."
            scene hypno_room2 with Dissolve(1.0)
            show toju toju01
            show toju_blink
            with dissolve
            ju "goodbye for now."
            hide toju toju01
            hide toju_blink
            with dissolve
            "june became more submissive!"
            $ bk3_day = False
            $ june_hypno +=1
            $ hypnoroom = "none"
            jump bk3_village_background

        if june_hypno ==4:
            show toju toju02 with dissolve
            ju "hello, handsome."
            show toju_blink with dissolve
            ju "i'll just take a seat..."
            hide hypno_room2
            scene black
            with dissolve
            scene hypno_room1
            hide toju_blink
            hide toju toju02
            show tohy june01
            with Dissolve(1.5)
            ju "let's begin."
            show ctc
            pause
            hide ctc
            y "just relax."
            show hypno_rail with Dissolve(1.5)
            y "here we go...."
            show expression "bk3/hypno/june/sclera.png"
            show tohy_june_eyeeast
            show expression "bk3/hypno/june/eyes_mask.png"
            show hypno_ball:
                alpha 1.0
                xpos 800 ypos 300
                linear 2.0 xpos -100 ypos 260
                alpha 0.0
                pause 2.0
                repeat

            show tohy_june_blink
            $ renpy.pause(2,hard=True)
            show ctc
            pause
            hide ctc
            y "Focus on the light and listen to my voice."
            hide tohy_june_eyeeast

            hide expression "bk3/hypno/june/sclera.png"
            hide expression "bk3/hypno/june/eyes_mask.png"
            show tohy june02
            with Dissolve(2.0)
            y "okay, let's put these away..."
            hide hypno_ball
            hide hypno_rail
            with dissolve
            y "do you still have that bush?"
            ju "yes..."
            y "hmmm..."
            menu:
                "shave it":
                    $ june_pubes = 'shaven'
                    y "i think we'll have to do something about that."
                    y "a proper whore keeps herself smooth and clean."
                "keep it":
                    $ june_pubes = 'bush'
                    y "good."
                    y "keep it."

            y "june, you are going to be more submissive."
            y "do you understand?"
            ju "I will become more... submissive."
            ya "good!"
            y "now, you'll forget what happened here and return to your normal state of mind in..."
            y "3... 2... 1..."
            play sound "audio/fingersnap.mp3"

            show tohy june01 with Dissolve(1.5)
            ju "wha..."
            ju "ah, yes."
            ju "thank you for your help."
            y "you're welcome."
            scene hypno_room2 with Dissolve(1.0)
            show toju toju01
            show toju_blink
            with dissolve
            ju "goodbye for now."
            hide toju toju01
            hide toju_blink
            with dissolve
            "june became more submissive!"
            $ bk3_day = False
            $ june_hypno +=1
            $ hypnoroom = "none"
            jump bk3_village_background

        if june_hypno ==3:
            show toju toju02 with dissolve
            ju "we have to stop meeting like this."
            y "do we?"
            ju "haahaa... aren't you a treat?"
            show toju_blink with dissolve
            ju "i'll just take a seat..."
            hide hypno_room2
            scene black
            with dissolve
            scene hypno_room1
            hide toju_blink
            hide toju toju02
            show tohy june01
            with Dissolve(1.5)
            ju "let's begin."
            show ctc
            pause
            hide ctc
            y "just relax."
            show hypno_rail with Dissolve(1.5)
            y "here we go...."
            show expression "bk3/hypno/june/sclera.png"
            show tohy_june_eyeeast
            show expression "bk3/hypno/june/eyes_mask.png"
            show hypno_ball:
                alpha 1.0
                xpos 800 ypos 300
                linear 2.0 xpos -100 ypos 260
                alpha 0.0
                pause 2.0
                repeat

            show tohy_june_blink
            $ renpy.pause(2,hard=True)
            show ctc
            pause
            hide ctc
            y "Focus on the light and listen to my voice."
            hide tohy_june_eyeeast

            hide expression "bk3/hypno/june/sclera.png"
            hide expression "bk3/hypno/june/eyes_mask.png"
            show tohy june02
            with Dissolve(2.0)
            y "okay, let's put these away..."
            hide hypno_ball
            hide hypno_rail
            with dissolve
            y "june, you are going to be more submissive."
            y "do you understand?"
            ju "I will become more... submissive."
            y "you will start calling me \"master\"."
            ju "i will start c-calling you m-mast... mast...ma....nnnn..."
            ya "god damn it! why is that so hard?"
            ya "you know what? when we talk again, i'm going to have a command for you, and you're going to do it."
            ya "you're a wench. a submissive, slutty wench."
            ya "say it!"
            ju "i'm... a submissive, sl-slutty w....we...wench."
            ya "good!"
            y "now, you'll forget what happened here and return to your normal state of mind in..."
            y "3... 2... 1..."
            play sound "audio/fingersnap.mp3"

            show tohy june01 with Dissolve(1.5)
            ju "wha..."
            ju "ah, yes."
            ju "thank you for your help."
            y "you're welcome, get out."
            ju "...."
            scene hypno_room2 with Dissolve(1.0)
            show toju toju01
            show toju_blink
            with dissolve
            ju "very well."
            hide toju toju01
            hide toju_blink
            with dissolve
            "june became more submissive!"
            $ bk3_day = False
            $ june_hypno +=1
            $ hypnoroom = "none"
            jump bk3_village_background

        if june_hypno ==2:
            show toju toju02 with dissolve
            ju "hey there, big boy."
            ju "ready to get this started?"
            y "definitely."
            y "take a seat."
            show toju_blink with dissolve
            ju "sigh..."
            ju "fine."
            hide hypno_room2
            scene black
            with dissolve
            scene hypno_room1
            hide toju_blink
            hide toju toju02
            show tohy june01
            with Dissolve(1.5)
            ju "well, i'm here."
            show ctc
            pause
            hide ctc
            ju "what now?"
            y "just make yourself comfortable while i set up the equipment."
            show hypno_rail with Dissolve(1.5)
            y "here we go...."
            y "A lamp will move along this rail, please follow it with your eyes while listening to my voice."
            ju "this seems idiotic."
            y "Okay, here we go."
            show expression "bk3/hypno/june/sclera.png"
            show tohy_june_eyeeast
            show expression "bk3/hypno/june/eyes_mask.png"
            show hypno_ball:
                alpha 1.0
                xpos 800 ypos 300
                linear 2.0 xpos -100 ypos 260
                alpha 0.0
                pause 2.0
                repeat

            show tohy_june_blink
            $ renpy.pause(2,hard=True)
            show ctc
            pause
            hide ctc
            y "Focus on the light and listen to my voice."
            hide tohy_june_eyeeast

            hide expression "bk3/hypno/june/sclera.png"
            hide expression "bk3/hypno/june/eyes_mask.png"
            show tohy june02
            with Dissolve(2.0)
            y "okay, let's put these away..."
            hide hypno_ball
            hide hypno_rail
            with dissolve
            y "june, i'm sick of your attitude."
            ju "...."
            y "you're going to start being nicer to me."
            y "and our customers."
            y "i mean, fuck, you yell at them when you should be flirting with them!"
            y "actually, that's a good idea."
            y "you're going to start being nicer {i}in general{/i}, and flirt with the customers."
            ju "I will... be... nicer... and flirt... with customers..."
            y "...and give me some of your tips when i talk to you."
            ju "and... give you... some of my... tips..."
            y "good girl."
            y "you are becoming more submissive to my requests."
            ju "i am becoming... more su-submissive..."
            y "excellent."
            y "now, you'll forget what happened here and return to your normal state of mind in..."
            y "3... 2... 1..."
            play sound "audio/fingersnap.mp3"

            show tohy june01 with Dissolve(1.5)
            ju "wha..."
            ju "ah, yes."
            ju "i assume you did something?"
            y "we made some progress, but we have a long way to go."
            ju "*sigh...*"
            scene hypno_room2 with Dissolve(1.0)
            show toju toju01
            show toju_blink
            with dissolve
            ju "very well."
            hide toju toju01
            hide toju_blink
            with dissolve
            "june became more submissive!"
            $ bk3_day = False
            $ june_hypno +=1
            $ hypnoroom = "none"
            jump bk3_village_background

        if june_hypno ==1:
            show toju toju02 with dissolve
            ju "hey there, big boy."
            ju "ready to get this started?"
            y "definitely."
            y "take a seat."
            show toju_blink with dissolve
            ju "sigh..."
            ju "fine."
            hide hypno_room2
            scene black
            with dissolve
            scene hypno_room1
            hide toju_blink
            hide toju toju02
            show tohy june01
            with Dissolve(1.5)
            ju "well, i'm here."
            show ctc
            pause
            hide ctc
            ju "what now?"
            y "just make yourself comfortable while i set up the equipment."
            show hypno_rail with Dissolve(1.5)
            y "here we go...."
            y "A lamp will move along this rail, please follow it with your eyes while listening to my voice."
            ju "this seems idiotic."
            y "Okay, here we go."
            show expression "bk3/hypno/june/sclera.png"
            show tohy_june_eyeeast
            show expression "bk3/hypno/june/eyes_mask.png"
            show hypno_ball:
                alpha 1.0
                xpos 800 ypos 300
                linear 2.0 xpos -100 ypos 260
                alpha 0.0
                pause 2.0
                repeat

            show tohy_june_blink
            $ renpy.pause(2,hard=True)
            show ctc
            pause
            hide ctc
            y "Focus on the light and listen to my voice."
            hide tohy_june_eyeeast

            hide expression "bk3/hypno/june/sclera.png"
            hide expression "bk3/hypno/june/eyes_mask.png"
            show tohy june02
            with Dissolve(2.0)
            y "okay, let's put these away..."
            hide hypno_ball
            hide hypno_rail
            with dissolve
            y "june, you will call me \"master\"."
            ju "mas....mast....nnnn.....mas....nnnn..."
            ya "damn it, girl! stop fighting it!"
            y "....you know what?"
            y "next time we speak, i'm going to tell you to wear a wench dress, and you're going to do it."
            y "got it?"
            ju "y...ye..."
            ya "say it!"
            ju "y...yes..."
            ju "i will... wear the... wench... dress..."
            y "good girl."
            y "you will also become more submissive to my requests."
            ju "i w-will be... more su-submissive..."
            y "excellent."
            y "now, you'll forget what happened here and return to your normal state of mind in..."
            y "3... 2... 1..."
            play sound "audio/fingersnap.mp3"

            show tohy june01 with Dissolve(1.5)
            ju "wha..."
            ju "ah, yes."
            ju "i assume you did something?"
            y "we made some progress, but we have a long way to go."
            ju "*sigh...*"
            scene hypno_room2 with Dissolve(1.0)
            show toju toju01
            show toju_blink
            with dissolve
            ju "very well."
            hide toju toju01
            hide toju_blink
            with dissolve
            y "awesome."
            $ bk3_day = False
            $ june_hypno +=1
            $ hypnoroom = "none"
            $ june_wench_no = True
            jump bk3_village_background

        if june_hypno == 0:
            hide screen earth_money_date
            "you hear a firm knock on the door."
            y "come in."
            show toju toju02 with dissolve
            ju "hey there, big boy."
            ju "ready to get this started?"
            y "definitely."
            y "take a seat."
            show toju_blink with dissolve
            ju "sigh..."
            ju "fine."
            hide hypno_room2
            scene black
            with dissolve
            scene hypno_room1
            hide toju_blink
            hide toju toju02
            show tohy june01
            with Dissolve(1.5)
            ju "well, i'm here."
            show ctc
            pause
            hide ctc
            ju "what now?"
            y "just make yourself comfortable while i set up the equipment."
            show hypno_rail with Dissolve(1.5)
            y "here we go...."
            y "A lamp will move along this rail, please follow it with your eyes while listening to my voice."
            ju "this seems idiotic."
            y "Okay, here we go."
            show expression "bk3/hypno/june/sclera.png"
            show tohy_june_eyeeast
            show expression "bk3/hypno/june/eyes_mask.png"
            show hypno_ball:
                alpha 1.0
                xpos 800 ypos 300
                linear 2.0 xpos -100 ypos 260
                alpha 0.0
                pause 2.0
                repeat

            show tohy_june_blink
            $ renpy.pause(2,hard=True)
            show ctc
            pause
            hide ctc
            y "Focus on the light and listen to my voice."
            hide tohy_june_eyeeast

            hide expression "bk3/hypno/june/sclera.png"
            hide expression "bk3/hypno/june/eyes_mask.png"
            show tohy june02
            with Dissolve(2.0)
            y "okay, let's put these away..."
            hide hypno_ball
            hide hypno_rail
            with dissolve
            y "(i should test that it's working...)"
            jump june_hypno_menu

            label june_hypno_menu:
                menu:
                    "How often do you masturbate?" if not june_hypno_1:
                        ju "A few times a week."
                        $ june_hypno_1 = True
                        jump june_hypno_menu
                    "What's your biggest sexual fantasy?" if not june_hypno_2:
                        ju "To be dominated, and treated like a wench by a strong, demanding man."
                        $ june_hypno_2 = True
                        jump june_hypno_menu
                    "continue" if june_hypno_1 and june_hypno_2:
                        pass

                y "good..."
                y "now, when you hear me say {b}[trigger]{/b}, you will become submissive to my requests."
                y "now say, \"yes, master\"."
                ju "y-yes... m-ma......"
                ju ".......mas......."
                ju "...n...nnn...."
                y "hmm. willful."
                y "we'll work on that later."
                y "but i think we've made a good start."
                y "you'll forget what happened here and return to your normal state of mind in..."
                y "3... 2... 1..."
                play sound "audio/fingersnap.mp3"

                show tohy june01 with Dissolve(1.5)
                ju "wha..."
                ju "oh, right."
                ju "are you quite finished?"
                ju "those lights were pretty, but quite ineffective."
                y "well... it didn't work."
                ju "i didn't think so."
                y "we'll need quite a few more sessions before we can really-"
                ju "no... i don't think so."
                y "....what?"
                scene hypno_room2 with Dissolve(1.0)
                show toju toju01
                show toju_blink
                with dissolve
                ju "we gave it a try, and i think that's what counts."
                y "but you need-"
                ju "have a nice.... evening, avatar."
                hide toju toju01
                hide toju_blink
                with dissolve
                y "oh... she's going to regret that."
                y "that's for damn sure."
                $ bk3_day = False
                $ june_hypno +=1
                $ hypnoroom = "none"
                jump bk3_village_background

    if hypnoroom == "suki":
        if suki_hypno >=10:
            $ hypnoroom = 'none'
            "suki's busy at the brothel."
            jump bk3_village_background

        if suki_hypno ==9:
            if suki_final_hypno:
                show tosi tosi01 with dissolve
                suki "hey, i'm here."
                y "good, take a seat."
                hide hypno_room2
                scene hypno_room1
                hide tosi_blink
                hide tosi tosi01
                show tohy suki01
                with Dissolve(1.5)
                suki "let's do this."
                y "give me a moment....."
                show hypno_rail with Dissolve(1.5)
                y "okay, here we go."
                show expression "bk3/hypno/suki/sclera.png"
                show tohy_suki_eyewest
                show tohy_suki_eyeeast
                show expression "bk3/hypno/suki/eyes_mask.png"
                show hypno_ball:
                    alpha 1.0
                    xpos 800 ypos 300
                    linear 2.0 xpos -100 ypos 260
                    alpha 0.0
                    pause 2.0
                    repeat
                show tohy_suki_blink
                $ renpy.pause(2,hard=True)
                show ctc
                pause
                hide ctc
                hide tohy_suki_eyewest
                hide tohy_suki_eyeeast

                hide expression "bk3/hypno/suki/sclera.png"
                hide expression "bk3/hypno/suki/eyes_mask.png"
                show tohy suki02
                hide hypno_ball
                hide hypno_rail
                with Dissolve(1.5)
                y "why don't you go ahead and lose those clothes."

                hide expression "ebackgrounds/hypno_room2.jpg"

                show tohy suki03
                with Dissolve(1.5)
                show ctc
                pause
                hide ctc
                y "suki, you want to be fucked."
                suki ".............."
                y "suki, repeat it."
                suki "i want... i want..."
                y "you want to be fucked."
                suki "i... nnn... nnooo..."
                ya "you want to be fucked, suki!"
                ya "say it!"
                suki "i... i..."
                suki "i want..."
                suki "want to be..."
                ya "fucked, suki. fucked."
                suki "........."
                suki "....fucked."
                y "now, say the whole thing."
                suki "i want... to be... fucked."
                y "good!"
                y "now put your clothes back on."
                show tohy suki02 with dissolve
                y "You'll forget what happened here and return to your normal state of mind in..."
                y "3... 2... 1..."
                play sound "audio/fingersnap.mp3"

                show tohy suki01 with Dissolve(1.0)
                suki "so, are we going to get started?"
                "you've convinced suki to be more submissive!"
                $ suki_hypno +=1
                $ hypnoroom = "none"
                $ bk3_day = False
                $ suki_hypno_today = True
                $ hypnoroom = 'none'
                jump bk3_village_background
            else:
                "suki's busy at the brothel."
                jump bk3_village_background

        if suki_hypno ==8:
            show tosi tosi01 with dissolve
            suki "hey, i'm here."
            y "good, take a seat."
            hide hypno_room2
            scene hypno_room1
            hide tosi_blink
            hide tosi tosi01
            show tohy suki01
            with Dissolve(1.5)
            suki "let's do this."
            y "give me a moment....."
            show hypno_rail with Dissolve(1.5)
            y "okay, here we go."
            show expression "bk3/hypno/suki/sclera.png"
            show tohy_suki_eyewest
            show tohy_suki_eyeeast
            show expression "bk3/hypno/suki/eyes_mask.png"
            show hypno_ball:
                alpha 1.0
                xpos 800 ypos 300
                linear 2.0 xpos -100 ypos 260
                alpha 0.0
                pause 2.0
                repeat
            show tohy_suki_blink
            $ renpy.pause(2,hard=True)
            show ctc
            pause
            hide ctc
            hide tohy_suki_eyewest
            hide tohy_suki_eyeeast

            hide expression "bk3/hypno/suki/sclera.png"
            hide expression "bk3/hypno/suki/eyes_mask.png"
            show tohy suki02
            hide hypno_ball
            hide hypno_rail
            with Dissolve(1.5)
            y "why don't you go ahead and lose those clothes."

            hide expression "ebackgrounds/hypno_room2.jpg"

            show tohy suki03
            with Dissolve(1.5)
            show ctc
            pause
            hide ctc
            y "suki, i'm going to help you practice getting fucked."
            suki ".............."
            y "suki, repeat it."
            suki "i will.... practice... getting... fucked..."
            y "good!"
            y "now put your clothes back on."
            show tohy suki02 with dissolve
            y "You'll forget what happened here and return to your normal state of mind in..."
            y "3... 2... 1..."
            play sound "audio/fingersnap.mp3"

            show tohy suki01 with Dissolve(1.0)
            suki "so, are we going to get started?"
            "you've convinced suki to be more submissive!"
            $ suki_hypno +=1
            $ hypnoroom = "none"
            $ bk3_day = False
            $ suki_hypno_today = True
            jump bk3_village_background

        if suki_hypno ==7:
            show tosi tosi01 with dissolve
            suki "hey, i'm here."
            y "good, take a seat."
            hide hypno_room2
            scene hypno_room1
            hide tosi_blink
            hide tosi tosi01
            show tohy suki01
            with Dissolve(1.5)
            suki "let's do this."
            y "give me a moment....."
            show hypno_rail with Dissolve(1.5)
            y "okay, here we go."
            show expression "bk3/hypno/suki/sclera.png"
            show tohy_suki_eyewest
            show tohy_suki_eyeeast
            show expression "bk3/hypno/suki/eyes_mask.png"
            show hypno_ball:
                alpha 1.0
                xpos 800 ypos 300
                linear 2.0 xpos -100 ypos 260
                alpha 0.0
                pause 2.0
                repeat
            show tohy_suki_blink
            $ renpy.pause(2,hard=True)
            show ctc
            pause
            hide ctc
            hide tohy_suki_eyewest
            hide tohy_suki_eyeeast

            hide expression "bk3/hypno/suki/sclera.png"
            hide expression "bk3/hypno/suki/eyes_mask.png"
            show tohy suki02
            hide hypno_ball
            hide hypno_rail
            with Dissolve(1.5)
            y "why don't you go ahead and lose those clothes."

            hide expression "ebackgrounds/hypno_room2.jpg"

            show tohy suki03
            with Dissolve(1.5)
            show ctc
            pause
            hide ctc
            y "nice."
            y "you're becoming more submissive."
            y "repeat it."
            suki "i'm becoming more submissive."
            y "good!"
            y "now put your clothes back on."
            show tohy suki02 with dissolve
            y "You'll forget what happened here and return to your normal state of mind in..."
            y "3... 2... 1..."
            play sound "audio/fingersnap.mp3"

            show tohy suki01 with Dissolve(1.0)
            suki "so, are we going to get started?"
            "you've convinced suki to be more submissive!"
            "she's more willing to do things for you!"
            $ suki_hypno +=1
            $ hypnoroom = "none"
            $ bk3_day = False
            $ suki_hypno_today = True
            jump bk3_village_background

        if suki_hypno ==6:
            show tosi tosi01 with dissolve
            suki "hey, i'm here."
            y "good, take a seat."
            hide hypno_room2
            scene hypno_room1
            hide tosi_blink
            hide tosi tosi01
            show tohy suki01
            with Dissolve(1.5)
            suki "let's do this."
            y "give me a moment....."
            show hypno_rail with Dissolve(1.5)
            y "okay, here we go."
            show expression "bk3/hypno/suki/sclera.png"
            show tohy_suki_eyewest
            show tohy_suki_eyeeast
            show expression "bk3/hypno/suki/eyes_mask.png"
            show hypno_ball:
                alpha 1.0
                xpos 800 ypos 300
                linear 2.0 xpos -100 ypos 260
                alpha 0.0
                pause 2.0
                repeat
            show tohy_suki_blink
            $ renpy.pause(2,hard=True)
            show ctc
            pause
            hide ctc
            hide tohy_suki_eyewest
            hide tohy_suki_eyeeast

            hide expression "bk3/hypno/suki/sclera.png"
            hide expression "bk3/hypno/suki/eyes_mask.png"
            show tohy suki02
            hide hypno_ball
            hide hypno_rail
            with Dissolve(1.5)
            y "why don't you go ahead and lose those clothes."

            hide expression "ebackgrounds/hypno_room2.jpg"

            show tohy suki03
            with Dissolve(1.5)
            show ctc
            pause
            hide ctc
            y "suki, you're going to run the brothel dressed as a kyoshi warrior."
            suki ".............."
            y "suki, repeat it."
            suki "i will.... run..."
            suki ".... the brothel... as a sacred.... kyoshi warrior..."
            y "good!"
            y "now put your clothes back on."
            show tohy suki02 with dissolve
            y "You'll forget what happened here and return to your normal state of mind in..."
            y "3... 2... 1..."
            play sound "audio/fingersnap.mp3"

            show tohy suki01 with Dissolve(1.0)
            suki "so, are we going to get started?"
            "you've convinced suki to be more submissive!"
            $ suki_hypno +=1
            $ hypnoroom = "none"
            $ bk3_day = False
            $ suki_hypno_today = True
            jump bk3_village_background

        if suki_hypno ==5:
            show tosi tosi01 with dissolve
            suki "hey, i'm here."
            y "good, take a seat."
            hide hypno_room2
            scene hypno_room1
            hide tosi_blink
            hide tosi tosi01
            show tohy suki01
            with Dissolve(1.5)
            suki "let's do this."
            y "give me a moment....."
            show hypno_rail with Dissolve(1.5)
            y "okay, here we go."
            show expression "bk3/hypno/suki/sclera.png"
            show tohy_suki_eyewest
            show tohy_suki_eyeeast
            show expression "bk3/hypno/suki/eyes_mask.png"
            show hypno_ball:
                alpha 1.0
                xpos 800 ypos 300
                linear 2.0 xpos -100 ypos 260
                alpha 0.0
                pause 2.0
                repeat
            show tohy_suki_blink
            $ renpy.pause(2,hard=True)
            show ctc
            pause
            hide ctc
            hide tohy_suki_eyewest
            hide tohy_suki_eyeeast

            hide expression "bk3/hypno/suki/sclera.png"
            hide expression "bk3/hypno/suki/eyes_mask.png"
            show tohy suki02
            hide hypno_ball
            hide hypno_rail
            with Dissolve(1.5)
            y "why don't you go ahead and lose those clothes."

            hide expression "ebackgrounds/hypno_room2.jpg"

            show tohy suki03
            with Dissolve(1.5)
            show ctc
            pause
            hide ctc
            y "nice."
            y "you're becoming more submissive."
            y "repeat it."
            suki "i'm becoming more submissive."
            y "good!"
            y "now put your clothes back on."
            show tohy suki02 with dissolve
            y "You'll forget what happened here and return to your normal state of mind in..."
            y "3... 2... 1..."
            play sound "audio/fingersnap.mp3"

            show tohy suki01 with Dissolve(1.0)
            suki "so, are we going to get started?"
            "you've convinced suki to be more submissive!"
            "she's more willing to do things for you!"
            $ suki_hypno +=1
            $ hypnoroom = "none"
            $ bk3_day = False
            $ suki_hypno_today = True
            jump bk3_village_background

        if suki_hypno ==4:
            show tosi tosi01 with dissolve
            suki "hey, i'm here."
            y "good, take a seat."
            hide hypno_room2
            scene hypno_room1
            hide tosi_blink
            hide tosi tosi01
            show tohy suki01
            with Dissolve(1.5)
            suki "let's do this."
            y "give me a moment....."
            show hypno_rail with Dissolve(1.5)
            y "okay, here we go."
            show expression "bk3/hypno/suki/sclera.png"
            show tohy_suki_eyewest
            show tohy_suki_eyeeast
            show expression "bk3/hypno/suki/eyes_mask.png"
            show hypno_ball:
                alpha 1.0
                xpos 800 ypos 300
                linear 2.0 xpos -100 ypos 260
                alpha 0.0
                pause 2.0
                repeat
            show tohy_suki_blink
            $ renpy.pause(2,hard=True)
            show ctc
            pause
            hide ctc
            hide tohy_suki_eyewest
            hide tohy_suki_eyeeast

            hide expression "bk3/hypno/suki/sclera.png"
            hide expression "bk3/hypno/suki/eyes_mask.png"
            show tohy suki02
            hide hypno_ball
            hide hypno_rail
            with Dissolve(1.5)
            y "why don't you go ahead and lose those clothes."

            hide expression "ebackgrounds/hypno_room2.jpg"

            show tohy suki04
            with Dissolve(1.5)
            show ctc
            pause
            hide ctc
            y "suki, you're no longer afraid of being naked."
            suki "i'm... no longer afraid of being naked."
            y "good!"
            y "now put your clothes back on."
            show tohy suki02 with dissolve
            y "You'll forget what happened here and return to your normal state of mind in..."
            y "3... 2... 1..."
            play sound "audio/fingersnap.mp3"

            show tohy suki01 with Dissolve(1.0)
            suki "so, are we going to get started?"
            "you've convinced suki to be more submissive!"
            $ suki_hypno +=1
            $ hypnoroom = "none"
            $ bk3_day = False
            $ suki_hypno_today = True
            jump bk3_village_background

        if suki_hypno ==3:
            show tosi tosi01 with dissolve
            suki "hey, i'm here."
            y "good, take a seat."
            hide hypno_room2
            scene hypno_room1
            hide tosi_blink
            hide tosi tosi01
            show tohy suki01
            with Dissolve(1.5)
            suki "let's do this."
            y "give me a moment....."
            show hypno_rail with Dissolve(1.5)
            y "okay, here we go."
            show expression "bk3/hypno/suki/sclera.png"
            show tohy_suki_eyewest
            show tohy_suki_eyeeast
            show expression "bk3/hypno/suki/eyes_mask.png"
            show hypno_ball:
                alpha 1.0
                xpos 800 ypos 300
                linear 2.0 xpos -100 ypos 260
                alpha 0.0
                pause 2.0
                repeat
            show tohy_suki_blink
            $ renpy.pause(2,hard=True)
            show ctc
            pause
            hide ctc
            hide tohy_suki_eyewest
            hide tohy_suki_eyeeast

            hide expression "bk3/hypno/suki/sclera.png"
            hide expression "bk3/hypno/suki/eyes_mask.png"
            show tohy suki02
            hide hypno_ball
            hide hypno_rail
            with Dissolve(1.5)
            y "since this is our fourth session, why don't you go ahead and lose those clothes."

            hide expression "ebackgrounds/hypno_room2.jpg"

            show tohy suki04
            with Dissolve(1.5)
            show ctc
            pause
            hide ctc
            y "nice."
            y "you're becoming more submissive."
            y "repeat it."
            suki "i'm becoming more submissive."
            y "good!"
            y "now put your clothes back on."
            show tohy suki02 with dissolve
            y "You'll forget what happened here and return to your normal state of mind in..."
            y "3... 2... 1..."
            play sound "audio/fingersnap.mp3"

            show tohy suki01 with Dissolve(1.0)
            suki "so, are we going to get started?"
            "you've convinced suki to be more submissive!"
            "she's more willing to do things for you!"
            $ suki_hypno +=1
            $ hypnoroom = "none"
            $ bk3_day = False
            $ suki_hypno_today = True
            jump bk3_village_background

        if suki_hypno ==2:
            show tosi tosi01 with dissolve
            suki "hey, i'm here."
            y "good, take a seat."
            hide hypno_room2
            scene hypno_room1
            hide tosi_blink
            hide tosi tosi01
            show tohy suki01
            with Dissolve(1.5)
            suki "let's do this."
            y "give me a moment....."
            show hypno_rail with Dissolve(1.5)
            y "okay, here we go."
            show expression "bk3/hypno/suki/sclera.png"
            show tohy_suki_eyewest
            show tohy_suki_eyeeast
            show expression "bk3/hypno/suki/eyes_mask.png"
            show hypno_ball:
                alpha 1.0
                xpos 800 ypos 300
                linear 2.0 xpos -100 ypos 260
                alpha 0.0
                pause 2.0
                repeat
            show tohy_suki_blink
            $ renpy.pause(2,hard=True)
            show ctc
            pause
            hide ctc
            hide tohy_suki_eyewest
            hide tohy_suki_eyeeast

            hide expression "bk3/hypno/suki/sclera.png"
            hide expression "bk3/hypno/suki/eyes_mask.png"
            show tohy suki02
            hide hypno_ball
            hide hypno_rail
            with Dissolve(1.5)
            y "since this is our third session, why don't you go ahead and lose those clothes."
            show tohy suki04
            with Dissolve(1.5)
            show ctc
            pause
            hide ctc
            y "nice."
            y "you're more submissive."
            y "repeat it."
            suki "i'm submissive."
            y "good!"
            y "now put your clothes back on."
            show tohy suki02 with dissolve
            y "You'll forget what happened here and return to your normal state of mind in..."
            y "3... 2... 1..."
            play sound "audio/fingersnap.mp3"

            show tohy suki01 with Dissolve(1.0)
            suki "so, are we going to get started?"
            "you've convinced suki to be a little more submissive...."
            $ suki_hypno +=1
            $ hypnoroom = "none"
            $ bk3_day = False
            $ suki_hypno_today = True
            jump bk3_village_background

        if suki_hypno ==1:
            show tosi tosi01 with dissolve
            suki "hey, i'm here."
            y "good, take a seat."
            hide hypno_room2
            scene hypno_room1
            hide tosi_blink
            hide tosi tosi01
            show tohy suki01
            with Dissolve(1.5)
            suki "let's do this."
            y "give me a moment....."
            show hypno_rail with Dissolve(1.5)
            y "okay, here we go."
            show expression "bk3/hypno/suki/sclera.png"
            show tohy_suki_eyewest
            show tohy_suki_eyeeast
            show expression "bk3/hypno/suki/eyes_mask.png"
            show hypno_ball:
                alpha 1.0
                xpos 800 ypos 300
                linear 2.0 xpos -100 ypos 260
                alpha 0.0
                pause 2.0
                repeat
            show tohy_suki_blink
            $ renpy.pause(2,hard=True)
            show ctc
            pause
            hide ctc
            hide tohy_suki_eyewest
            hide tohy_suki_eyeeast

            hide expression "bk3/hypno/suki/sclera.png"
            hide expression "bk3/hypno/suki/eyes_mask.png"
            show tohy suki02
            hide hypno_ball
            hide hypno_rail
            with Dissolve(1.5)
            y "since this is our second session, why don't you go ahead and lose those clothes."

            show tohy suki04
            with Dissolve(1.5)
            show ctc
            pause
            hide ctc
            y "nice."
            y "you're becoming more submissive."
            y "repeat it."
            suki "i'm becoming more submissive."
            y "good!"
            y "now put your clothes back on."
            show tohy suki02 with dissolve
            y "You'll forget what happened here and return to your normal state of mind in..."
            y "3... 2... 1..."
            play sound "audio/fingersnap.mp3"

            show tohy suki01 with Dissolve(1.0)
            suki "so, are we going to get started?"
            "you've convinced suki to be a little more submissive...."
            $ suki_hypno +=1
            $ hypnoroom = "none"
            $ bk3_day = False
            $ suki_hypno_today = True
            jump bk3_village_background

        if suki_hypno == 0:
            "you hear a light but firm rap on the door."
            y "come in."
            show tosi tosi01 with dissolve
            suki "hey..."
            y "suki, great."
            y "take a seat."
            show tosi_blink with dissolve
            suki "sure."
            hide hypno_room2
            scene hypno_room1
            with dissolve
            hide tosi_blink
            hide tosi tosi01
            show tohy suki01
            with Dissolve(1.5)
            show ctc
            pause
            hide ctc
            suki "like this?"
            y "perfect."
            y "just make yourself comfortable while i set up the equipment."
            show hypno_rail with Dissolve(1.5)
            y "here we go...."
            y "A lamp will move along this rail, please follow it with your eyes while listening to my voice."
            suki "...i trust you."
            y "Okay, here we go."
            show expression "bk3/hypno/suki/sclera.png"
            show tohy_suki_eyewest
            show tohy_suki_eyeeast
            show expression "bk3/hypno/suki/eyes_mask.png"
            show hypno_ball:
                alpha 1.0
                xpos 800 ypos 300
                linear 2.0 xpos -100 ypos 260
                alpha 0.0
                pause 2.0
                repeat
            show tohy_suki_blink
            $ renpy.pause(2,hard=True)
            show ctc
            pause
            hide ctc
            y "Focus on the light and listen to my voice."
            hide tohy_suki_eyewest
            hide tohy_suki_eyeeast

            hide expression "bk3/hypno/suki/sclera.png"
            hide expression "bk3/hypno/suki/eyes_mask.png"
            show tohy suki02
            with Dissolve(1.5)
            y "(i should test that it's working...)"
            y "now...."
            menu:
                "you're a cow":
                    y "you are a cow."
                    y "what is your name?"
                    suki "mooo!"
                    y "good girl."
                    y "okay, you are no longer a cow."
                    y "you are also now feeling very receptive."
                "you're a duck":

                    y "you are a duck."
                    y "what is your name?"
                    suki "quack!"
                    y "good girl."
                    y "okay, you are no longer a duck."
                    y "you are also now feeling very receptive."









            suki "i feel very receptive."
            hide hypno_ball
            hide hypno_rail
            with dissolve
            y "and i don't need these any more..."
            jump first_suki_hypno_questions

            label first_suki_hypno_questions:
                menu:
                    "How often do you masturbate?" if not first_suki_hypno_1:
                        suki "First thing in the morning, last thing in the evening."
                        $ first_suki_hypno_1 = True
                        jump first_suki_hypno_questions
                    "What is your biggest sexual fantasy?" if not first_suki_hypno_2:
                        suki "to be fucked by anonymous strangers."
                        $ first_suki_hypno_2 = True
                        jump first_suki_hypno_questions
                    "what is your biggest fear?" if not first_suki_hypno_3:
                        suki "to embarrass the noble kyoshi warrior name."
                        $ first_suki_hypno_3 = True
                        jump first_suki_hypno_questions
                    "continue" if first_suki_hypno_1 and first_suki_hypno_2 and first_suki_hypno_3:
                        pass

                y "now stand up."

                hide tohy_suki_blink

                hide tohy
                hide expression "ebackgrounds/hypno_room1.jpg"
                show expression "ebackgrounds/hypno_room2.jpg"
                with Dissolve(1.0)

                show tosi tosi01
                show tosi_hypno_eyes
                with dissolve

                y "take off your clothes."

                show tosi tosi04 with Dissolve(1.0)
                y "fuck yeah! i could get used to this."
                show ctc
                pause
                hide ctc
                y "alright, That's enough."
                y "now sit in the chair again, slut-in-training."

                hide tosi tosi01
                hide tosi_hypno_eyes
                with dissolve

                hide expression "ebackgrounds/hypno_room2.jpg"

                show expression "ebackgrounds/hypno_room1.jpg"
                show tohy suki04
                with Dissolve(1.5)
                show ctc
                pause
                hide ctc
                y "nice, okay, what else?"
                y "i don't want to do too much right away or she might get suspicious..."
                menu:
                    "get naked":
                        y "take off your clothes, suki."
                        suki "n...nno...."
                        y "alright, alright, easy."
                    "finished":

                        pass

                y "I'll count backwards from three."
                y "Oh shit... put your clothes back on first, i guess."
                show tohy suki02 with dissolve
                y "and... let's give you a trigger word..."
                menu:
                    "buttsluts":
                        $ trigger="buttsluts"
                    "squirtle":

                        $ trigger="squirtle"
                    "user input":

                        $ trigger = renpy.input("enter a trigger word", default='buttsluts', allow=None, exclude='{}', length=14, with_none=None, pixel_width=None)
                        $ trigger = trigger.strip()
                        if trigger == "":
                            $ trigger="buttsluts"

                y "sweet, okay, the trigger word is [trigger]..."
                y "You'll forget what happened here and return to your normal state of mind in..."
                y "3... 2... 1..."
                play sound "audio/fingersnap.mp3"

                show tohy suki01 with Dissolve(1.0)
                suki "so, are we going to get started?"
                y "we actually already finished."
                suki "...and? did you cure me?"
                y "not quite, but we made a start."
                suki "oh. that's good i guess."
                suki "guess i'll head back to the hospital."
                suki "see you around, aang!"
                hide tohy suki01 with dissolve
                y "oh, suki... i have such plans for you..."
                y "ew."
                y "i'm turning into a talent agent."
                $ suki_hypno = 1
                $ hypnoroom = "none"
                $ bk3_day = False
                $ suki_hypno_today = True
                jump bk3_village_background


label inside_brothel_building:
    hide screen earth_money_date
    if toph_katara_chair >=3 and toph_katara_chair <7:
        stop music
        play music "audio/Smooth Lovin.mp3"
        scene black
        scene inside_brothel_1
        show tosi tosi10
        with dissolve
        suki "have you talked to shady about that key yet?"
        y "oh, right. i'll go talk to shady."
        jump bk3_village_background

    if toph_katara_chair ==2:
        stop music
        play music "audio/Smooth Lovin.mp3"
        scene black
        scene inside_brothel_1
        show tosi tosi10
        with dissolve
        suki "hi, what can i do for you?"
        y "suki, did you ever find a key in the hospital?"
        suki "i... did."
        y "awesome!"
        y "your hesitancy makes me nervous to ask, but..."
        y "do you still have it?"
        suki "yes!"
        y "grea-"
        suki "is what i would say if i still had it."
        y "...that was mean."
        suki "sorry, couldn't resist."
        suki "but i couldn't figure out what it was for so I sold it to shady."
        y "note to self, never trust you around my things."
        suki "sorry."
        y "wait, didn't we have table coasters in here?"
        suki "is that what those were?"
        y "did you-"
        suki "i sold them."
        y "....right."
        y "guess i'll ask shady about the key."
        y "....and our coasters."
        suki "okay."
        suki "anything else?"
        ya "....condensation..."
        ya "....gonna put rings all over our damn furniture...."
        ya "....can't have nice things...."
        suki "...i guess we're done here."
        $ toph_katara_chair = 3
        jump bk3_village_background

    if suki_brothel:
        stop music
        play music "audio/Smooth Lovin.mp3"
        scene black
        scene inside_brothel_1

        if tylee_brothel_watch >= 1:
            jump brothel_main_menu

            label brothel_main_menu:
                menu:
                    "talk to suki":
                        pass
                    "talk to ty lee":

                        if ty_balance_fucked:
                            menu:
                                "?????? (locked)" if not kitten_gear:
                                    "test"
                                "kitty sex" if kitten_gear:
                                    show tfn with dissolve
                                    ty "hello, avatar!"
                                    y "wanna be a kitty?"
                                    ty "ooo! fun!"
                                    ty "you gonna give this bad pussy a pounding?"
                                    ty "come with me!"
                                    jump pussycrush
                                "balance ball sex":

                                    pass
                                "wall blowjob":

                                    ty "hey!"
                                    ty "i was feeling nostalgic for how we met, so i put a hole in a wall here."
                                    ty "come look!"
                                    jump tylee_wall_bj

                        $ ty_balancefuck_face = "eyesdown"
                        show totb totb01:
                            xpos 0
                            linear 2 xpos 4
                            linear 2 xpos 0
                            repeat
                        show ctc
                        pause
                        hide ctc
                        y "Hey, Ty... what are you doing?"
                        $ ty_balancefuck_face = "eyesup"
                        ty "Balance practice!"
                        ty "Standing on a ball for as long as i can without falling off!"
                        y "That looks really hard."
                        ty "not for me. It's just warm-up practice."
                        y "Even with that long skirt?"
                        $ ty_balancefuck_face = "eyesup"

                        ty "If needed to, I could do backflips in this!"

                        y "I see you're not wearing underwear."
                        ty "I'm not?"

                        show totb totb02
                        $ ty_balancefuck_face = "eyesdown"
                        ty "I guess I'm not!"
                        show ctc
                        pause
                        hide ctc
                        ty "Feels nice and breezy!"
                        y "Looks nice too!"
                        show totb totb03
                        y "How long can you stand like that without falling?"
                        ty "As long as I want! It's become too easy."
                        show ctc
                        pause
                        hide ctc
                        y "Wanna bet I can make it more challenging for you?"
                        if tylee_brothel_watch <=4:
                            ty "hhmmmmm...."
                            ty "i don't think that's a good idea right now."
                            ty "i mean, that sounds like fun, but i feel a little... too exposed for that."
                            ty "sorry!"
                            y "no worries."
                            y "(i should keep having her spend time with skye.)"
                            jump bk3_village_background
                        else:
                            ty "hhmmmm...."
                            $ ty_balancefuck_face = "eyesup"
                            $ ty_balance_fucked = True
                            ty "Sure!"
                            ty "But you can't tickle me!"
                            ty "Oh, and you also can't kick against the ball!"
                            y "You're making it hard."
                            y "And I'm not talking about the conditions for this little wager."
                            ty "Huh?"
                            ty "Well, you have three minutes."
                            ty "Time starts now!"
                            y "Just three?"
                            ty "Time's running!"
                            y "Okay, okay."
                            show totb totb10

                            $ ty_balancefuck_face = "surprise"
                            ty "OOooooh!"
                            show ctc
                            pause
                            hide ctc
                            "You stand behind Ty Lee and whip out your cock."
                            $ ty_balancefuck_face = "eyesdown"
                            ty "So that's your plan!"
                            y "You give up?"
                            ty "No way!"

                            show totb totb11
                            "You slowly penetrate Ty Lee's vagina, forcing yourself inside."
                            show ctc
                            pause
                            hide ctc
                            show totb totb12
                            ty "oh!"
                            show totb totb13
                            ty "ahh... ah... oh..."
                            show totb totb14
                            ty "you're... you're really going... deep..."
                            show totb totb11 with dissolve
                            y "ready to call it quits?"
                            ty "never!"
                            y "alright then...."
                            show totb totb100
                            ty "hngh... ooh!"
                            show ctc
                            pause
                            hide ctc
                            y "that not doing it, huh?"
                            ty "I... ah... told you..."
                            ty "this is... ah... easy..."
                            y "right, right..."
                            y "well how about..."

                            show totb totb101
                            y "this?"
                            ty "ahh... oof..."
                            show ctc
                            pause
                            hide ctc
                            ty "n-never!"
                            y "You're a tough opponent, Ty Lee..."
                            y "I'm impressed."
                            ty "th... ah... thank y-"
                            y "but I'm not giving up!"
                            show totb totb102
                            $ ty_balancefuck_face = "surprise"
                            ty "nngh! hey!!"
                            show ctc
                            pause
                            hide ctc
                            ty "That..."
                            ty "That's... no..."
                            $ ty_balancefuck_face = "eyesdown"
                            ty "That's... no... fair..."
                            y "i don't play fair."
                            ty "ngh! ah!"
                            show ctc
                            pause
                            hide ctc
                            $ ty_balancefuck_face = "lewd"
                            ty "That's tickling from the inside...."
                            ty "Time's up!"

                            menu:
                                "hold back":
                                    show totb totb10
                                    y "But I don't think it has been three mi-"
                                    ty "Time's up! Time's up!"
                                    ty "I'll give you a rematch later, but I uh have to go and do something now."
                                    hide totb totb10 with dissolve
                                    "Ty lee quickly runs out of the room, wobbling..."
                                    y "heh.."
                                    $ bk3_day = False
                                    jump bk3_village_background
                                "cum inside Ty Lee":

                                    show totb totb14:
                                        xpos 0
                                        linear 1 xpos 4
                                        linear 1 xpos 0
                                        repeat

                                    ty "Time's up!"
                                    y "Hnnnng!"

                                    show expression "bk3/tylee/balancefuck/womb.png"
                                    play sound "audio/splurt2.ogg"
                                    show expression "bk3/tylee/balancefuck/spermshot.png"
                                    $ renpy.pause (0.3, hard=True)
                                    hide expression "bk3/tylee/balancefuck/spermshot.png"
                                    show expression "bk3/tylee/balancefuck/sperm1.png"
                                    $ renpy.pause (0.5, hard=True)


                                    play sound "audio/splurt1.ogg"

                                    show expression "bk3/tylee/balancefuck/spermshot.png"
                                    $ renpy.pause (0.3, hard=True)
                                    hide expression "bk3/tylee/balancefuck/spermshot.png"

                                    show expression "bk3/tylee/balancefuck/sperm2.png"
                                    hide expression "bk3/tylee/balancefuck/sperm1.png"
                                    $ renpy.pause (0.5, hard=True)
                                    play sound "audio/splurt3.ogg"

                                    show expression "bk3/tylee/balancefuck/spermshot.png"
                                    $ renpy.pause (0.3, hard=True)
                                    hide expression "bk3/tylee/balancefuck/spermshot.png"

                                    show expression "bk3/tylee/balancefuck/sperm3.png"
                                    hide expression "bk3/tylee/balancefuck/sperm2.png"
                                    $ renpy.pause (0.5, hard=True)

                                    y "Hnnnnng..."
                                    show ctc
                                    pause
                                    hide ctc

                                    hide expression "bk3/tylee/balancefuck/womb.png"
                                    hide expression "bk3/tylee/balancefuck/sperm3.png"
                                    show totb totb04
                                    with dissolve
                                    show ctc
                                    pause
                                    hide ctc
                                    ty "I feel full..."
                                    y "I feel drained..."
                                    show ctc
                                    pause
                                    hide ctc
                                    ty "it is... making a mess..."
                                    y "heh..."

                                    show ctc
                                    pause
                                    hide ctc
                                    ty "I... gotta go..."
                                    hide totb
                                    with dissolve
                                    "Ty lee quickly runs out of the room, wobbling and leaking..."
                                    y "heh."
                                    $ bk3_day = False
                                    jump bk3_village_background
                    "talk to skye":

                        show sp_prisonthighs with dissolve
                        skye "hey! what's up?"
                        if ty_balance_fucked and suki_fucked:
                            if suki_hypno <=9:
                                $ suki_final_hypno = True
                                skye "hey! bad news."
                                skye "i talked to suki, and she's still a little uncomfortable with the idea of sex."
                                skye "which is weird, because i'm sure i saw you go into a room with her..."
                                y "erm..."
                                skye "anyway, you'll have to convince her, but i'm not sure how."
                                skye "good luck!"
                                hide sp_prisonthighs with dissolve
                                y "hmm... i should finish suki's hypnosis."
                                if suki_hypno ==9:
                                    y "i bet one more time will do it."
                                jump bk3_village_background

                            if not ty_suki_skye_anal:
                                y "hey, so i've fucked ty lee and suki."
                                y "and suki is finally ready to be penetrated."
                                y "do you-"
                                skye "hey! that's great!"
                                skye "i think it's time to continue their training, don't you?"
                                y "i... you... i mean... yeah."
                                y "what kind of training did you have in mind?"
                                skye "well... i haven't had anal in a long time."
                                skye "i'm really out of practice."
                                skye "and i think the girls would benefit from it as well."
                                skye "so we might as well do it together."
                                skye "especially if they're gonna be whores."
                                y "uh, they're not. just personal whores. for me."
                                skye "hmm... well... still."
                                skye "you want them to open their tight, pretty little butt holes for you, right?"
                                y "definitely."
                                skye "then come on, already."
                                skye "let's go fuck!"
                                $ ty_suki_skye_anal = True
                                jump ty_suki_skye1
                            else:
                                y "hey-"
                                skye "great, you're here!"
                                skye "wanna come fuck us?"
                                y "um. yes."
                                skye "great! come on!"
                                jump ty_suki_skye1
                        else:

                            if tylee_brothel_watch >=4:
                                if ty_balance_fucked and not suki_fucked:
                                    y "i think we should all get together... and make me jizz."
                                    skye "i don't think suki is far enough along for that."
                                    skye "you should at least, i dunno, fuck her or something first."
                                    skye "sex her up and get back to me."
                                    y "hmmm.... alright."
                                    y "anyway..."
                                if suki_fucked and not ty_balance_fucked:
                                    y "i think we should all get together... and make me jizz."
                                    skye "i don't think ty lee is far enough along for that."
                                    skye "you should at least, i dunno, fuck her or something first."
                                    skye "sex her up and get back to me."
                                    y "hmmm.... alright."
                                    y "anyway..."
                                if not suki_fucked and not ty_balance_fucked:
                                    y "i think we should all get together... and make me jizz."
                                    y "whadda ya think?"
                                    skye "i think... neither suki nor ty lee are far enough along for that."
                                    skye "you should at least, i dunno, fuck them or something first."
                                    skye "sex them up and get back to me."
                                    y "hmmm.... alright."
                                    y "anyway..."
                        y "you need to take ty lee and suki, and have them watch what you do."
                        if skye_today:
                            skye "sorry, i already did that today."
                            skye "they should really space these out until they're used to it."
                            hide sp_prisonthighs with dissolve
                            jump brothel_main_menu
                        else:
                            skye "okay!"
                            show tosi tosi10
                            show toti toti01:
                                xzoom -1.0
                            with dissolve
                            skye "let's do this!"
                            show black with dissolve
                            "you wait for skye to finish..."
                            hide black
                            show prisonthigh_sperm
                            with dissolve
                            skye "that was fun!"
                            ty "it was!"
                            suki "very... instructive."
                            skye "alright, i'm gonna go clean off before the next load arrives."
                            skye "i mean... customer."
                            hide prisonthigh_sperm
                            hide sp_prisonthighs
                            with dissolve
                            ty "i'm gonna go to my room, too."
                            hide toti with dissolve
                            suki "let me know if you'd like to speak to me."
                            hide tosi with dissolve
                            $ skye_today = True
                            $ tylee_brothel_watch += 1
                            $ bk3_day = False
                            play sound "audio/win2.mp3"
                            "ty lee and suki are a little sluttier!"
                            jump bk3_village_background
                    "exit":

                        jump bk3_village_background

        if brothel_building >=2:
            if not naga_eyes:
                show tosi tosi01 with dissolve
                y "has ty lee shown up?"
                suki "no."
                y "i wonder where she is?"
                y "I hope she's not trapped somewhere..."
            if naga_eyes and not ty_lee_brothel:
                show tosi tosi01:
                    xzoom -1.0
                with dissolve
                y "hey, suki."
                suki "what's-"
                show tf with dissolve
                ty "hey, guys!"
                y "ty lee! you made it!"
                ty "i did!"
                suki "great..."
                ty "wow... this place is a lot bigger."
                y "yup, we've got a room for you now."
                ty "aw... aren't you sweet!"
                suki "aang... do we really need-"
                y "ty lee is a guest here."
                y "and you will make sure she is treated with the utmost respect."
                y "is that understood?"
                suki ".........yes."
                y "perfect."
                y "ty lee... do you have any requests?"
                ty "well... i've been wearing the kyoshi makeup, but i don't know anything about them!"
                suki "that's obvious...."
                ty "i'd love for you to teach me, suki!"
                ty "and in return, i can teach you some chi-blocking techniques!"
                suki "that.... might not be a bad trade-off."
                y "great. ty lee, go check out your room."
                y "i need to speak with suki."
                show tf2
                hide tf
                with dissolve
                ty "okay!"
                hide tf2 with dissolve
                hide tosi tosi01 with dissolve
                show tosi tosi01 with dissolve
                suki "yes? what is-"
                y "[trigger]."
                show tosi_hypno_eyes with dissolve
                y "you are going to be ty lee's best friend."
                suki "....best....friend...."
                y "yes. and you are going to teach her the kyoshi warrior's ways."
                suki "....kyoshi...."
                y "and we are going to hire a girl to be the local slut."
                y "if we're going to have a brothel, we need at least one actual prostitute..."
                y "but i have plans for you and ty lee, so we're going to find a random slut, understood?"
                suki "random... slut... brothel..."
                y "good girl."
                y "and whenever that girl has sex, you and ty lee are to watch."
                y "ty lee needs to understand how.... normal sex is."
                y "you're going to acclimate her to sex."
                suki "acclimate... ty lee... sex..."
                y "good."
                y "[trigger]."
                hide tosi_hypno_eyes with dissolve
                suki "hey... so i was thinking..."
                suki "we should find a peasant girl to take care of the... tourists."
                suki "and i think ty lee and i should watch."
                suki "start getting used to seeing sex."
                suki "maybe you can find a girl for us?"
                suki "in the tunnels?"
                y "i think that's a great idea."
                suki "okay, then."
                suki "good luck!"
                $ ty_lee_brothel = True
                jump bk3_village_background
            if ty_lee_brothel and not peasant_slut_hired:
                if peasant_slut:
                    show sp_prisonthighs with dissolve
                    skye "hey!"
                    skye "anybody need their balls fondled?"
                    y "um."
                    y "not quite yet."
                    y "the brothel's not quite big enough yet for you."
                    y "i'll upgrade it, and get you set up with a room."
                    y "then you can start... ball fondling."
                    skye "great!"
                    skye "i'll just sleep on the floor here in the meantime."
                    skye "i'm pretty easy."
                    y "yeah, i'm getting that."
                    skye "hah! i like you."
                    skye "i bet you have a nice dick."
                    skye "show me sometime, cutie."
                    skye "bye!"
                    hide sp_prisonthighs with dissolve
                    $ peasant_slut_hired = True
                    jump bk3_village_background
                else:

                    y "(gotta remember to look in the tunnels for a strumpet.)"

            if peasant_slut_hired:
                if brothel_building ==2:
                    y "(i should look for what i need to upgrade the brothel.)"
                    y "(i bet i could find obsidian in the tunnels.)"
                else:

                    if tylee_brothel_watch <=0:
                        show sp_prisonthighs
                        show tosi tosi10
                        show toti toti01:
                            xzoom -1.0
                        with dissolve
                        skye "hey!"
                        skye "you upgraded the brothel! that's great!"

                        skye "i'm gonna go show these noobs what a dedicated girl can do with just a pussy and a dick."
                        skye "it's a simple recipe, but it makes the best dessert."
                        skye "now, scoot!"
                        show black with dissolve
                        "you wait for skye to finish..."
                        hide black
                        show prisonthigh_sperm
                        with dissolve
                        skye "hey!"
                        y "how'd they do?"
                        skye "they watched like pros!"
                        ty "that was a lot of fun!"
                        suki "i'm glad i'm not doing that, but i agree that it was.... instructive."
                        suki "i'm also glad our identities are protected by these clothes."
                        skye "alright, i'm gonna go clean off before the next load arrives."
                        skye "i mean... customer."
                        hide prisonthigh_sperm
                        hide sp_prisonthighs
                        with dissolve
                        ty "i'm gonna go to my room, too."
                        hide toti with dissolve
                        suki "let me know if you'd like to speak to me."
                        hide tosi with dissolve
                        $ tylee_brothel_watch = 1
                        $ bk3_day = False
                        jump bk3_village_background


        if toph_blackmail ==2:
            show tosi tosi01 with dissolve
            suki "why are we here?"
            suki "let's go see katara."
            jump bk3_village_background

        if toph_blackmail ==1:
            show tosi tosi01 with dissolve
            y "suki, i have a task for you."
            suki "oh, hey!"
            suki "sorry, but i'm a little busy at the mo-"
            y "[trigger]."
            show tosi_hypno_eyes with dissolve
            y "you want to come with me."
            suki "i want to come with you."
            y "[trigger]."
            hide tosi_hypno_eyes with dissolve
            suki "......"
            suki "did... did you need me to go somewhere?"
            y "as a matter of fact i did, how did you know?"
            suki "I'm... not sure."
            show tosi_smile with dissolve
            suki "just good instincts, i guess."
            y "alright, come on."
            y "we're going to see katara."
            $ toph_blackmail +=1
            jump bk3_village_background

        if not suki_brothel_talk:
            show tosi tosi01
            with dissolve
            suki "hey, aang."
            suki "you know, i'm not really sure why i started working here..."
            suki "but i really want to, for some reason."
            suki "we need to get someone to start putting out if we're gonna make this place work."
            y "how about you?"
            show tosi tosi03 with dissolve
            suki "not likely, aang!"
            y "fine. for now."
            $ suki_brothel_talk = True
            jump bk3_village_background
        else:
            if suki_hypno >=9:

                if not sp_kyoshi_dildo:
                    show tosi tosi10 with dissolve
                    menu:
                        "kyoshi outfit":
                            suki "sure thing."
                            show tosi tosi10
                        "nude":
                            suki "sure thing."
                            show tosi tosi06
                            with dissolve
                    show ctc
                    pause
                    hide ctc

                    menu:
                        "i'll meet you in the tunnels" if joodee_tits ==7:
                            suki "....okay."
                            $ joodee_tits = 8
                            jump bk3_village_background
                        "sexy time":

                            y "(i'm missing something...)"
                            y "(maybe there's an item in the tunnels that i can find and use?)"
                            jump bk3_village_background
                        "exit":

                            jump bk3_village_background

                if not suki_dildone:
                    show tosi tosi06
                    with dissolve
                    y "hey suki, i think its time we talk about your role here in the brothel."
                    show tosi_blink with dissolve
                    suki "well, i'm running it. with no girls."
                    hide tosi_blink with dissolve
                    suki "so... i think it's pretty clear where we're at."
                    y "exactly. we need to start training our first whore."
                    show tosi_blink with dissolve
                    suki "...great. whatever. who do you have in mind?"
                    y "well... you."
                    hide tosi_blink
                    show tosi_angry
                    show tosi_blush
                    with dissolve
                    suki "what!?"
                    suki "that's {i}not{/i} happening."
                    y "come on suki. you knew this was coming."
                    suki "no i didn't!"
                    y "you're working the {i}brothel{/i}."
                    y "now, come on. we need to practice getting you fucked."
                    hide tosi_angry
                    show tosi_blink
                    with dissolve
                    suki "that's not an... unreasonable suggestion..."
                    hide tosi_blink
                    show tosi_angry
                    hide tosi_blush
                    show tosi_blush
                    with dissolve
                    suki "but i'm not agreeing to fuck anyone!"
                    y "that's fine... for now."
                    suki "......."
                    y "now, put on your kyoshi makeup."
                    hide tosi_angry with dissolve
                    suki "why..."
                    y "well, do you want anyone to recognize you?"
                    suki "i mean... no..."
                    show tosi_angry with dissolve
                    suki "but i'm not fucking people!"
                    y "this is just practice."
                    suki "what!? then no!"
                    suki "and i will never, {i}ever{/i} wear my kyoshi warrior outfit for the sexual pleasure of strangers..."
                    suki "or you!"
                    suki "it is holy, it took a lifetime of training, it is an exceptionally rare honor..."
                    suki "and i will not debase myself, my culture, or my holy calling for your disgusting sexual-"
                    y "[trigger]."
                    hide tosi_angry
                    hide tosi_blush
                    show tosi_hypno_eyes
                    with dissolve
                    show ctc
                    pause
                    hide ctc
                    y "suki."
                    suki "yes."
                    y "you {i}will{/i} wear your kyoshi makeup."
                    y "you will wear it because you appreciate the anonymity."
                    y "and, you will wear it because it's sacrilegious, and you now love the thought of that."
                    suki ".......i.......nn.........."
                    y "suki."
                    suki ".....nnn......."
                    y "suki, you {i}will{/i} shove a slick dildo into your juicy, drenched pussy."
                    suki "...........nn...yyy..........."
                    y "you cannot wait for me to let your tight little cunt slurp it in and out... until you cum all over it."
                    y "and you will cum on it when i tell you to do so."
                    y "and.... you can no longer pleasure yourself."
                    y "ever."
                    y "you will only receive pleasure through the will of others."
                    y "and you will only cum when i tell you to."
                    suki "......yyy......."
                    y "do you understand?"
                    suki "i.... i.... un...."
                    suki "......"
                    y "{i}suki{/i}."
                    suki "i... understand."
                    y "good. now you're so excited to be fucked with a toy."
                    suki "I can't wait to be fucked with a toy."
                    y "[trigger]."
                    show tosi_blush
                    show tosi_blink
                    hide tosi_hypno_eyes
                    with dissolve
                    suki "what... happened...?"
                    y "what do you mean?"
                    suki "I feel...."
                    hide tosi_blink with dissolve
                    suki "nevermind."
                    suki "anyway, i think...."
                    suki "i think, if you want, we can do that."
                    y "do what?"
                    suki "you can... you know... use a dildo on me."
                    show tosi_blink with dissolve
                    suki "if you want."
                    y "oh? well, i don't know what changed your mind, but that's great."
                    y "we're going to use this...."
                    show kyoshi_dildo with dissolve
                    hide tosi_blush
                    show tosi_angry
                    with dissolve
                    suki "what!? no!"
                    hide kyoshi_dildo with dissolve
                    y "what do you mean, \"no\"?"
                    suki "i mean {b}no{/b}!"
                    suki "it's one thing to... use a toy..."
                    suki "but... not a statue of kyoshi!"
                    suki "it's sacred!"
                    suki "i'm not... i'm not okay with that!"
                    y "are you sure?"
                    y "it's sacrilegious, which you find hot... right?"
                    show tosi_blush with dissolve
                    suki "i don't know what you're talking about!"
                    suki "i would never desecrate a holy object!"
                    y "really? but this... looks exactly like a dildo."
                    y "you can't tell me you haven't used it like one."
                    suki "of course not!"
                    suki "that's the holy statue i received as graduating to a kyoshi warrior!"
                    suki "it is to remind me of my duty and sacred responsibility as-"
                    y "*sigh*"
                    suki "wh-"
                    y "[trigger]."
                    hide tosi_blush
                    hide tosi_blink
                    hide tosi_angry
                    show tosi_hypno_eyes
                    with dissolve
                    y "you will fuck your kysohi dil... erm... statue."
                    y "no, i can't even pretend, it's definitely a dildo."
                    y "you're going to be fucked by your kyoshi dildo."
                    y "say it."
                    suki "it's a kyoshi dildo, and i will be fucked by it."
                    y "good girl."
                    y "[trigger]."
                    hide tosi_hypno_eyes
                    show tosi_blush
                    with dissolve
                    y "suki?"
                    suki "i....."
                    show tosi_blink with dissolve
                    suki "want to go into the back?"
                    y "hell yeah."
                    hide tosi_blink with dissolve
                    suki "bring the..."
                    suki "......."
                    suki "kyoshi dildo."
                    $ suki_dildone = True
                    jump suki_dildo_fuck

                show tosi tosi10
                with dissolve

                menu:
                    "kyoshi outfit":
                        suki "sure thing."
                        show tosi tosi10
                    "nude":
                        suki "sure thing."
                        show tosi tosi06
                        with dissolve
                show ctc
                pause
                hide ctc

                menu:

                    "i'll meet you in the tunnels" if joodee_tits ==7:
                        suki "....okay."
                        $ joodee_tits = 8
                        jump bk3_village_background

                    "shake tits" if toph_drunk1:
                        suki "okay!"
                        hide tosi with Dissolve(1)
                        show totd totd30 with dissolve
                        show ctc
                        pause
                        hide ctc
                        suki "like what you see?"
                        show ctc
                        pause
                        hide ctc
                        show totd totd31
                        suki "get a good look, handsome..."
                        show ctc
                        pause
                        hide ctc
                        y "cheers, suki."
                        hide totd with dissolve
                        show tosi tosi06
                        show tosi_smile
                        with dissolve
                        suki "you're welcome!"
                        jump bk3_village_background
                    "fuck suki with a dildo":

                        jump suki_dildo_fuck2
                    "fuck suki with your dick":

                        if ajala_jin_lesson:
                            y "suki... i have an idea."
                            suki "what?"
                            y "i have this very {i}realistic{/i} dildo i think you should use."
                            suki "umm...."
                            y "[trigger]."
                            show tosi_hypno_eyes with dissolve
                            suki ".........."
                            "you pull out your cock."
                            y "this is a dildo."
                            suki "that is a dildo."
                            y "it's no big deal... we're going to use it just like your other dildo, okay?"
                            suki "okay..."
                            hide tosi_hypno_eyes with dissolve
                            $ suki_fucked = True
                            jump suki_dildo_fuck3

                        if not ajala_jin_lesson:
                            y "i think i should put my cock in you."
                            suki "what? don't be dumb."
                            y "[trigger]."
                            suki "...."
                            y "let's fuck."
                            suki "n...nnn....no..."
                            y "damn it."
                            y "i guess i need to be better at hypnosis training first, maybe?"
                            jump bk3_village_background

                    "hypno session" if suki_final_hypno:
                        if suki_hypno >=10:
                            y "(i think she's as brainwashed as i can make her.)"
                            y "never mind!"
                            suki "okay."
                            jump bk3_village_background
                        y "suki, i think we've almost removed all of your brainwashing."
                        y "...but we need one last session."
                        if hypnoroom == "suki":
                            y "oh, you're already scheduled."
                            y "well, i'll see you over there."
                            suki "i'll be there."
                            jump bk3_village_background

                        suki "really? but... i feel fine."
                        y "trust me on this."
                        suki "well... okay..."
                        if hypnoroom == "none":
                            $ hypnoroom = "suki"
                            y "great!"
                            y "i'll see you there!"
                            jump bk3_village_background
                        else:
                            y "oh, wait, i forgot i have someone else scheduled."
                            y "we'll do this later."
                            suki "if you say so."
                            jump bk3_village_background
                    "exit":


                        jump bk3_village_background


            if suki_hypno ==8:

                if kyoshi_outfit_talk:
                    show tosi tosi10
                    with dissolve
                    suki "hi there!"
                    menu:
                        "kyoshi outfit":
                            suki "okay!"
                        "nude":
                            show tosi tosi06
                            with dissolve
                            suki "okay!"

                    show ctc
                    pause
                    hide ctc

                    menu:
                        "follow me to the tunnels" if joodee_tits ==7:
                            suki "I'm... not ready to go back down there, i'm sorry."
                            jump bk3_village_background
                        "hypno-room appointment":

                            if suki_hypno_today:
                                y "(i already hypnotized her once today, i shouldn't push it...)"
                                y "nevermind."
                                suki "okay."
                                jump bk3_village_background
                            else:
                                if hypnoroom == "none":
                                    y "i think you should come by my place and we'll do some hypno therapy."
                                    suki "hmm... okay, aang!"
                                    $ hypnoroom = "suki"
                                    jump bk3_village_background
                                if hypnoroom == "suki":
                                    y "I'm still waiting on you to get over to the hypno-room."
                                    suki "well, i'm waiting on you for the same thing!"
                                    y "oh. erm. whatever."
                                    jump bk3_village_background
                                else:
                                    y "crap, i've got a session with june to do first."
                                    y "nevermind, suki."
                                    suki "oh... okay."
                                    jump bk3_village_background
                        "exit":
                            jump bk3_village_background

                if not kyoshi_outfit_talk:
                    show tosi tosi06
                    with dissolve
                    y "you really need to wear your kyoshi gear."
                    suki "i... can't do that."
                    suki "it's important, it's... practically sacred."
                    suki "i can't... wear it in a brothel."
                    y "well, you have to."
                    show tosi_angry with dissolve
                    suki "i really don't."
                    y "[trigger]."
                    hide tosi_angry
                    show tosi_hypno_eyes
                    with dissolve
                    y "you will start wearing your kyoshi gear in the brothel, unless i say otherwise."
                    suki "...i...understand...."
                    hide tosi tosi06 with dissolve
                    show tosi tosi10 with dissolve
                    y "hot!"
                    y "where are your fans?"
                    show tosi tosi11 with dissolve
                    y "come on, put on a show!"
                    show tosi tosi100
                    hide tosi_hypno_eyes
                    show ctc
                    pause
                    hide ctc
                    y "yes!"
                    y "now dance!"
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
                    y "hahahaha! dance for me, puppet!"
                    y "dance!"
                    y "....okay."
                    y "that's enough."
                    hide tosi tosi102 with dissolve
                    show tosi tosi10 with dissolve
                    $ kyoshi_outfit_talk = True
                    jump inside_brothel_building

            if suki_hypno ==7:
                show tosi tosi06
                with dissolve
                suki "hey, aang!"

                menu:
                    "follow me to the tunnels" if joodee_tits ==7:
                        suki "I'm... not ready to go back down there, i'm sorry."
                        jump bk3_village_background
                    "hypno-room appointment":

                        if suki_hypno_today:
                            y "(i already hypnotized her once today, i shouldn't push it...)"
                            y "nevermind."
                            suki "okay."
                            jump bk3_village_background
                        else:
                            if hypnoroom == "none":
                                y "i think you should come by my place and we'll do some hypno therapy."
                                suki "hmm... okay, aang!"
                                $ hypnoroom = "suki"
                                jump bk3_village_background
                            if hypnoroom == "suki":
                                y "I'm still waiting on you to get over to the hypno-room."
                                suki "well, i'm waiting on you for the same thing!"
                                y "oh. erm. whatever."
                                jump bk3_village_background
                            else:
                                y "crap, i've got a session with june to do first."
                                y "nevermind, suki."
                                suki "oh... okay."
                                jump bk3_village_background
                    "exit":
                        jump bk3_village_background

            if suki_hypno ==6:
                show tosi tosi01
                with dissolve
                y "suki, strip down."
                suki "oh, i don't feel comfortable."
                y "[trigger]."
                show tosi_hypno_eyes with dissolve
                y "strip."
                show tosi tosi05 with dissolve
                show ctc
                pause
                hide ctc
                y "all the way."
                show tosi tosi06 with dissolve
                show ctc
                pause
                hide ctc
                y "nice."
                menu:
                    "follow me to the tunnels" if joodee_tits ==7:
                        suki "I'm... not ready to go back down there, i'm sorry."
                        jump bk3_village_background
                    "hypno-room appointment":

                        if suki_hypno_today:
                            y "(i already hypnotized her once today, i shouldn't push it...)"
                            y "nevermind."
                            suki "okay."
                            jump bk3_village_background
                        else:
                            if hypnoroom == "none":
                                y "i think you should come by my place and we'll do some hypno therapy."
                                suki "hmm... okay, aang!"
                                $ hypnoroom = "suki"
                                jump bk3_village_background
                            if hypnoroom == "suki":
                                y "I'm still waiting on you to get over to the hypno-room."
                                suki "well, i'm waiting on you for the same thing!"
                                y "oh. erm. whatever."
                                jump bk3_village_background
                            else:
                                y "crap, i've got a session with june to do first."
                                y "nevermind, suki."
                                suki "oh... okay."
                                jump bk3_village_background
                    "exit":
                        jump bk3_village_background

            if suki_hypno ==5:
                show tosi tosi01
                with dissolve
                y "hey, suki."
                suki "what's up, aang?"
                y "open your shirt."
                suki "......"
                show tosi tosi05 with dissolve
                show ctc
                pause
                hide ctc
                y "awesome."
                menu:
                    "follow me to the tunnels" if joodee_tits ==7:
                        suki "I'm... not ready to go back down there, i'm sorry."
                        jump bk3_village_background
                    "hypno-room appointment":

                        if suki_hypno_today:
                            y "(i already hypnotized her once today, i shouldn't push it...)"
                            y "nevermind."
                            suki "okay."
                            jump bk3_village_background
                        else:
                            if hypnoroom == "none":
                                y "i think you should come by my place and we'll do some hypno therapy."
                                suki "hmm... okay, aang!"
                                $ hypnoroom = "suki"
                                jump bk3_village_background
                            if hypnoroom == "suki":
                                y "I'm still waiting on you to get over to the hypno-room."
                                suki "well, i'm waiting on you for the same thing!"
                                y "oh. erm. whatever."
                                jump bk3_village_background
                            else:
                                y "crap, i've got a session with june to do first."
                                y "nevermind, suki."
                                suki "oh... okay."
                                jump bk3_village_background
                    "exit":
                        jump bk3_village_background
            else:

                show tosi tosi01
                with dissolve
                suki "hey, aang!"
                suki "i'm trying to get this place functional."
                menu:
                    "follow me to the tunnels" if joodee_tits ==7:
                        suki "I'm... not ready to go back down there, i'm sorry."
                        jump bk3_village_background
                    "hypno-room appointment":

                        if suki_hypno_today:
                            y "(i already hypnotized her once today, i shouldn't push it...)"
                            y "nevermind."
                            suki "okay."
                            jump bk3_village_background
                        else:
                            if hypnoroom == "none":
                                y "i think you should come by my place and we'll do some hypno therapy."
                                suki "hmm... okay, aang!"
                                $ hypnoroom = "suki"
                                jump bk3_village_background
                            if hypnoroom == "suki":
                                y "I'm still waiting on you to get over to the hypno-room."
                                suki "well, i'm waiting on you for the same thing!"
                                y "oh. erm. whatever."
                                jump bk3_village_background
                            else:
                                y "crap, i've got a session with june to do first."
                                y "nevermind, suki."
                                suki "oh... okay."
                                jump bk3_village_background
                    "exit":

                        jump bk3_village_background
    else:

        scene black
        scene inside_brothel_1
        with dissolve
        y "i need to get some girls..."
        y "and someone to run this place."
        y "I bet suki would be good at that."
        jump bk3_village_background


label toph_titfuck:
    scene boobjob
    show tobj tobj03
    show tobj_pants
    with dissolve
    t "so... are you going to massage my chest again?"
    y "Sure, unless you don't want me to."
    show tobj_angry
    t "I don't want you to!"
    hide tobj_angry
    show tobj_unsure
    t "It's just that..."
    t "It has shown some really good results."
    y "Spectacular results!"

    t "Yeah....."
    y "I feel a \"but\" coming."
    hide tobj_smile
    show tobj_unsure
    t "Is it really necessary to pinch my nipples all the time?"
    t "They're getting very tender."
    t "It'd be nice if we could try something else every now and then."

    y "Yeah, you were making some strange sounds during the massage."
    hide tobj_unsure
    show tobj_angry
    show tobj_fisthit1
    pause 0.2
    hide tobj_fisthit1

    show tobj_fisthit2
    pause 0.2
    hide tobj_fisthit2
    show tobj tobj03 with hpunch


    t "No I didn't!"


    y "Okay, okay, I'm sorry."
    hide tobj_angry with Dissolve(1.2)
    y "well... I could try something a little less nipple-intensive..."
    show tobj_smile
    t "Great! Let's do that!"
    y "You don't wanna hear what it is first?"
    t "How bad could it be!"
    y "Okay, take off your shirt and put your arms up."

    show tobj tobj05 with Dissolve(1.4)
    t "Done!"
    y "You're already lying down so that's good."
    y "This will feel a bit strange at first."
    "You kneel above Toph and..."

    play sound "audio/slap.mp3"
    show tobj_dickslap_cue:
        alpha 1.0
        linear 1.0 alpha 0.0
    show tobj_staticdick
    hide tobj_smile
    pause 0.4
    show tobj_surprise
    show tobj_blush


    t "What's... that?"
    show tobj tobj04
    y "Oh come on, you know what it is."
    hide tobj_surpise
    hide tobj_blush
    show tobj_angry
    show tobj_blush
    t "What's it doing on my chest!?"
    y "It's no different than my hands."
    t "The hell it isn't!!"
    y "Look, this way you're nipples can rest easy."
    y "And because I don't have to masturbate for sperm afterwards we can finish this quickly."
    t "....."
    t "........."
    t "................"
    y "so....can I..."
    t "YOU!!"
    t "You can NEVER tell anyone about this!"
    t "Understood?"
    t "If I find out you did, I'll bury you so deep even molerats won't be able to dig you out!"
    y "My lips are sealed."
    hide tobj_angry
    show tobj_blink
    t "I must be crazy, but fine."
    t "Just start already."
    y "Okay, gently push your breasts to the center of your chest."
    hide tobj_blink
    show tobj tobj06
    t "like this?"
    y "Almost, try to make a small valley for my dick to rest in."
    show tobj_angry
    hide tobj_blush
    show tobj_blush:
        alpha 0.8
    t "If my breasts were big enough to do that all of this wouldn't be necessary!!"
    y "You're almost there. Push a little harder."
    show tobj_blink
    t "Nnnghg.."
    show tobj tobj10
    show tobj_blush:
        alpha 0.7
    y "That's it."
    hide tobj_angry with Dissolve(1.2)
    hide tobj_blink
    t "Now what?"

    y "Now I'll slowly start moving up and down while you keep your hands like that."

    hide tobj_surprise
    show tobj_blink
    t "Yeah yeah, I'm get the picture. Just do it."
    hide tobj_staticdick
    show tobj tobj101
    y "This is just... a really... efficient..."
    hide tobj_blink
    t "Boobjob?"
    show tobj_blink
    y "If it works, who cares what it's called?"
    hide tobj_blink
    t "I just don't want anyone to think I'm some sort of floozy."
    t "I'm just doing this... for the results."
    y "Of course, and that's why we promised to not tell anyone, right?"
    y "To prevent any misunderstandings."
    t "Right."

    show tobj_angry
    hide tobj_blush
    show tobj_blush:
        alpha 0.7
    t "And make sure you don't forget!"
    hide tobj_angry with Dissolve(1.4)
    t "How long are you going to do this anyway?"
    t "Your dick smells.....peculiar"
    y "It smells like aroused cock, baby!"
    t "Don't call me baby!"
    y "Alright... eehh... legally-of-consenting-age person."
    show tobj_unsure
    show tobj_blink
    hide tobj_blush
    show tobj_blush:
        alpha 0.7
    t "Just forget it... how much longer? It's starting to chafe."
    y "Oh I can fix that easily"
    show tobj tobj06
    t "You can?"
    play sound "audio/spit.mp3"
    show expression "bk3/toph/boobjob/spit.png" with Dissolve(2.0)
    y "That should help."
    hide tobj_blink
    hide tobj_unsure
    show tobj_surprise
    hide tobj_blush
    show tobj_blush:
        alpha 0.7
    t "Wha..."
    y "Here we go again."
    hide expression "bk3/toph/boobjob/spit.png"
    show tobj tobj101
    t "Ah... that's actually much better."
    hide tobj_surprise
    y "No prob."
    y "Are you ready for me to go faster now?"
    t "Yeah."
    show tobj tobj104
    y "hnnnn..."
    y "You have some... first class.. perky titties, Toph..."
    y "So soft..."
    t "They are?"
    y "soft... perky... slut tits... sliding under my hard cock."
    t "Wha...what?!"
    y "I'm almost there you pint sized slut!"
    show tobj tobj105
    y "I'm about to cum!"
    t "Get that thing out of my face!!!"

    menu:
        "disregard Toph and cum on her face":
            y "Too late!"
            show tobj tobj13

            play sound "audio/splurt2.ogg"
            show tobj_surprise
            show tobj_hairaway
            hide tobj_blush
            show tobj_blush
            show tobj_spermshot
            with dissolve
            $ renpy.pause(0.2)

            hide tobj_spermshot

            show toma_sperm1:
                xpos 90 ypos -190

            y "hnnnn..."

            t "wha...."
            show tobj_spermshot
            $ renpy.pause(0.2)
            hide tobj_spermshot
            hide toma_sperm1
            play sound "audio/splurt1.ogg"
            show toma_sperm2:
                xpos 90 ypos -190
            y "AAAh."
            t "is this..."

            show tobj_spermshot
            $ renpy.pause(0.2)
            hide tobj_spermshot
            hide toma_sperm2

            show toma_sperm3:
                alpha 0.9
                xpos 90 ypos -190
            y "Aaaaaaah!"
            hide tobj_surprise
            hide tobj_hairaway
            show tobj_angry
            hide tobj_blush
            show tobj_blush
            hide toma_sperm3
            show toma_sperm3:
                alpha 0.8
                xpos 90 ypos -190
            with dissolve
            t "Youuuu....!"
            y "Sorry! Sorry!"
            t "I'm... i'm drenched!"
            y "I... I just couldn't hold back!"
            y "You're just too damn sexy!"

            hide tobj_angry
            hide toma_sperm3
            show tobj_surprise
            show tobj_blush
            show toma_sperm3:
                alpha 0.7
                xpos 90 ypos -190
            with dissolve
            t "I'm...I'm sexy?"
            y "Super sexy!"
            hide tobj_blush
            hide toma_sperm3
            show tobj_angry
            show tobj_blush
            show toma_sperm3:
                alpha 0.6
                xpos 90 ypos -190
            with dissolve
            t ".... well that doesn't matter!"
            t "I told you not to cum on my face and you did it anyway!"
            y "That was an honest accident."
            t "And you called me a pint sized slut!!!"
            y "Don't take that seriously."
            y "It's just exciting to say dumb stuff like that in the heat of the moment."
            y "You should try it!"
            t "......"
            t "You dumbass..."
            t "Get out, Aang."



            hide toma_sperm3
        "cum on Toph's chest":

            y "Move your hands!"

            show tobj tobj05
            y "Here it comes!"
            play sound "audio/splurt2.ogg"
            show tobj_spermshot:
                xpos 10 ypos 170
            $ renpy.pause(0.2)
            hide tobj_spermshot

            show toma_sperm1:
                xpos 90 ypos -20
            y "hnnnn.."


            play sound "audio/splurt1.ogg"
            show tobj_spermshot:
                xpos 10 ypos 170
            $ renpy.pause(0.2)
            hide tobj_spermshot
            hide toma_sperm1

            show toma_sperm2:
                xpos 90 ypos -20
            y "AAAh."


            play sound "audio/splurt3.ogg"
            show tobj_spermshot:
                xpos 10 ypos 170
            $ renpy.pause(0.2)
            hide tobj_spermshot
            hide toma_sperm2

            show toma_sperm3:
                xpos 90 ypos -20
            y "Aaaaaaah!"
            show ctc
            pause
            hide ctc
            t "....nice?"

            y "oh man... that was great."
            t "Well?"
            y "Well what?"
            t "Aren't you supposed to rub the sperm over my boobs?"
            y "Oh, eh, yeah... of course."
            show toma_rubtits:
                xzoom 0.9
                yzoom 0.9
                xpos 140
                ypos 50
                linear 2.0 ypos 20

                linear 2.0 ypos 50
                repeat
            y "Aw yeah, rubbin it all over them titties."
            hide toma_rubtits
            hide toma_sperm3 with Dissolve(3.0)
            show tobj tobj04
            y "Well, that should do it."
            hide tobj_blush
            show tobj_smile
            show tobj_blush:
                alpha 0.7
            t "Thanks, Aang."


    $ toph_titjob = True
    scene black with dissolve
    "you head home for the night."
    jump bk3_next


label toph_titfuck2:
    scene boobjob
    show tobj tobj03
    show tobj_pants
    with dissolve
    t "so, are you going to massage my chest with your... thing again?"
    y "that's the plan."
    show tobj_unsure
    t "....it makes me a little uncomfortable..."
    t "but it seems to be working..."
    hide tobj_unsure
    show tobj_smile
    t "Let's do it..."
    y "Okay, take off your shirt and put your arms up."

    show tobj tobj05 with Dissolve(1.4)
    t "Done!"
    y "and your pants."
    hide tobj_smile
    show tobj_unsure
    with dissolve
    t "my... pants?"
    t "why?"
    y "the visual really helps me."
    t "but that's..."
    t "you'll see my..."
    y "i've already seen your tits."
    y "i mean if you want it to take longer..."
    t "no, i'll... i'll take them off..."
    hide tobj_unsure
    hide tobj_pants with dissolve
    show ctc
    pause
    hide ctc
    y "here we go..."

    play sound "audio/slap.mp3"
    show tobj_dickslap_cue:
        alpha 1.0
        linear 1.0 alpha 0.0
    show tobj_staticdick
    hide tobj_smile
    pause 0.4
    show tobj_surprise
    show tobj_blush


    t "........."
    show tobj tobj04 with dissolve
    y "it's alright to be intimidated."
    hide tobj_surpise
    hide tobj_blush
    show tobj_angry
    show tobj_blush
    t "stop... being weird!"
    t "....."
    t "........."
    t "................"
    t "just do it already!"
    y "Okay, gently push your breasts to the center of your chest."
    hide tobj_angry
    show tobj tobj06
    with dissolve
    t "like this?"
    y "harder!"
    show tobj_angry
    hide tobj_blush
    show tobj_blush:
        alpha 0.8
    show tobj_blink
    t "Nnnghg.."
    show tobj tobj10
    show tobj_blush:
        alpha 0.7
    y "That's it."
    hide tobj_angry with Dissolve(1.2)
    hide tobj_blink
    y "there we go..."

    hide tobj_surprise
    show tobj_blink
    t "Yeah yeah, I'm get the picture. Just do it."
    hide tobj_staticdick
    show tobj tobj101
    y "ungh... mmmgh... yeah..."
    y "mmmmm...."
    hide tobj_blink
    t "can you not... make those sounds?"
    show tobj_blink
    y "It's part of the process."
    hide tobj_blink
    t "oh... right."
    t "How long are you going to do this anyway?"
    y "until i'm done."
    show tobj_unsure
    show tobj_blink
    hide tobj_blush
    show tobj_blush:
        alpha 0.7
    t "It's starting to chafe."
    y "spit on it."
    show tobj tobj06
    t "........"
    play sound "audio/spit.mp3"
    show expression "bk3/toph/boobjob/spit.png" with Dissolve(2.0)
    y "good job, that should help."
    hide tobj_blink
    hide tobj_unsure
    show tobj_surprise
    hide tobj_blush
    show tobj_blush:
        alpha 0.7
    y "Here we go again."
    hide expression "bk3/toph/boobjob/spit.png"
    show tobj tobj101
    t "Ah... that's actually much better."
    hide tobj_surprise
    y "yeah it is."
    y "........"

    y "Are you ready for me to go faster now?"
    t "Yeah."
    show tobj tobj104
    y "hnnnn..."
    show ctc
    pause
    hide ctc
    y "You have some... great fucking tits, Toph..."
    y "So soft..."
    t "They are?"
    y "tasty little cock milkers..."

    y "hey, lift your knees up."

    t "...what?"
    y "i need a visual, like we talked about."
    t "I... um..."
    t "...okay, aang. if you say so."
    show tobj tobj101_1
    show tobj_kneesup with dissolve
    show ctc
    pause
    hide ctc
    y "(fuck!)"
    y "(i just want to lick her fucking thighs!)"
    y "that's it, you tasty little whore!"
    t "...what..?"
    show ctc
    pause
    hide ctc
    y "lift your legs up!"
    t "Wha...what?!"
    y "your legs!"
    t ".........."
    hide tobj_kneesup
    show tobj_legsup_ani
    t "like this?"
    show ctc
    pause
    hide ctc
    y "yes!"
    show ctc
    pause
    hide ctc

    menu:
        "keep fucking her tits":
            y "I'm almost there you pint sized slut!"
            show tobj tobj101_2
            y "I'm about to cum!"
            hide tobj_blush
            show tobj_angry
            show tobj_blush
            with dissolve
            t "Get that thing out of my face!!!"
        "rub her clit with your cock":

            show tobj tobj04 with dissolve
            y "*pant...* *pant...*"
            t "...aang? what are you doing?"
            t "what's wrong? is something wrong?"

            show tobj_rubcrotchslow
            show tobj_surprise with dissolve
            show ctc
            pause
            hide ctc
            show tobj_unsure
            hide tobj_surprise
            with dissolve
            t "aang...!? what... what are you doing!?"
            t "this isn't okay...!"
            show ctc
            pause
            hide ctc
            y "It's... ah... it's fine... natural... ah..."
            t "aang! i'm not sure...."
            y "lay... lay back... ungh... your pussy lips, toph... ngh..."
            show tobj tobj05 with dissolve
            t "like... this..."
            t "it's... stop... stop, aang! stop!"
            show tobj_rubcrotchfast
            hide tobj_rubcrotchslow
            y "you're so slick... and warm..."
            show ctc
            pause
            hide ctc
            t "my... breast, aang! don't forget!"
            y "right... right..."
            hide tobj_rubcrotchfast with dissolve
            y "squeeze it!"
            show tobj tobj10 with dissolve
            y "don't worry toph... i'll take good care of you."
            t "....."
            show tobj tobj101_1
            y "ohh... nngh..."
            y "that's it..."
            y "I'm almost there you pint sized slut!"
            show tobj tobj101_2
            y "I'm about to cum!"
            hide tobj_blush
            show tobj_angry
            show tobj_blush
            with dissolve
            t "Get that thing out of my face!!!"

    show tobj_kneesup
    hide tobj_legsup_ani
    with dissolve
    menu:
        "disregard Toph and cum on her face":
            y "Too late!"
            show tobj tobj13
            hide tobj_angry
            play sound "audio/splurt2.ogg"
            show tobj_surprise
            show tobj_hairaway
            hide tobj_blush
            show tobj_blush
            show tobj_spermshot
            with dissolve
            $ renpy.pause(0.2)

            hide tobj_spermshot

            show toma_sperm1:
                xpos 90 ypos -190

            y "hnnnn..."

            t "wha...."
            show tobj_spermshot
            $ renpy.pause(0.2)
            hide tobj_spermshot
            hide toma_sperm1
            play sound "audio/splurt1.ogg"
            show toma_sperm2:
                xpos 90 ypos -190
            y "AAAh."
            t "is this..."

            show tobj_spermshot
            $ renpy.pause(0.2)
            hide tobj_spermshot
            hide toma_sperm2

            show toma_sperm3:
                alpha 0.9
                xpos 90 ypos -190
            y "Aaaaaaah!"
            hide tobj_surprise
            hide tobj_hairaway
            show tobj_angry
            hide tobj_blush
            show tobj_blush
            hide toma_sperm3
            show toma_sperm3:
                alpha 0.8
                xpos 90 ypos -190
            with dissolve
            t "Youuuu....!"
            y "Sorry! Sorry!"
            t "I'm... i'm drenched!"
            y "I... I just couldn't hold back!"
            y "You're just too damn sexy!"

            hide tobj_angry
            hide toma_sperm3
            show tobj_surprise
            show tobj_blush
            show toma_sperm3:
                alpha 0.7
                xpos 90 ypos -190
            with dissolve
            t "I'm...I'm sexy?"
            y "Super sexy!"
            hide tobj_blush
            hide toma_sperm3
            show tobj_angry
            show tobj_blush
            show toma_sperm3:
                alpha 0.6
                xpos 90 ypos -190
            with dissolve
            t ".... well that doesn't matter!"
            t "I told you not to cum on my face and you did it anyway!"
            y "That was an honest accident."
            t "And you called me a pint sized slut!!!"
            y "Don't take that seriously."
            y "It's just exciting to say dumb stuff like that in the heat of the moment."
            y "You should try it!"
            t "......"
            t "You dumbass..."
            t "Get out, Aang."



            hide toma_sperm3
        "cum on Toph's chest":

            y "Move your hands!"
            hide tobj_angry with dissolve
            show tobj tobj05
            y "Here it comes!"
            play sound "audio/splurt2.ogg"
            show tobj_spermshot:
                xpos 10 ypos 170
            $ renpy.pause(0.2)
            hide tobj_spermshot

            show toma_sperm1:
                xpos 90 ypos -20
            y "hnnnn.."


            play sound "audio/splurt1.ogg"
            show tobj_spermshot:
                xpos 10 ypos 170
            $ renpy.pause(0.2)
            hide tobj_spermshot
            hide toma_sperm1

            show toma_sperm2:
                xpos 90 ypos -20
            y "AAAh."


            play sound "audio/splurt3.ogg"
            show tobj_spermshot:
                xpos 10 ypos 170
            $ renpy.pause(0.2)
            hide tobj_spermshot
            hide toma_sperm2

            show toma_sperm3:
                xpos 90 ypos -20
            y "Aaaaaaah!"
            show ctc
            pause
            hide ctc
            t "....nice?"

            y "oh man... that was great."
            t "Well?"
            y "Well what?"
            t "Aren't you supposed to rub the sperm over my boobs?"
            y "Oh, eh, yeah... of course."
            show toma_rubtits:
                xzoom 0.9
                yzoom 0.9
                xpos 140
                ypos 50
                linear 2.0 ypos 20

                linear 2.0 ypos 50
                repeat
            y "Aw yeah, rubbin it all over them titties."
            hide toma_rubtits
            hide toma_sperm3 with Dissolve(3.0)
            show tobj tobj04
            y "Well, that should do it."
            hide tobj_blush
            show tobj_smile
            show tobj_blush:
                alpha 0.7
            t "Thanks, Aang."


    $ toph_titjob = True
    scene black with dissolve
    "you head home for the night."
    jump bk3_next


label suki_dildo_fuck:
    hide screen earth_money_date
    scene black
    scene kyoshi_bed_1
    with dissolve
    $ kyoshi_suki_face = 'neat'
    $ kyoshi_suki_penetrate = 'dildo'
    $ kyoshi_suki_penetrate = "dildo"
    $ renpy.pause(0.5)
    show tosv tosv17 with dissolve
    suki "so?"
    suki "you gonna fuck me?"
    y "yeah."
    y "now lift your fucking thighs up."
    show tosv tosv15 with dissolve
    suki "how's this?"
    y "nice. you ready?"
    suki "i...."
    show tosv tosv16 with dissolve
    suki "......"
    suki "yes..."
    show tosv tosv01 with dissolve
    show ctc
    pause
    hide ctc
    y "say please."
    suki "...please..."
    show tosv tosv02 with dissolve
    suki "i feel it...."
    suki "aang, what are we-"
    show tosv tosv03
    show suki_vag_blink:
        xpos 208 ypos 85
    with dissolve
    show ctc
    pause
    hide ctc
    suki "uunhhh..."
    show tosv tosv04 with dissolve
    show ctc
    pause
    hide ctc
    suki "ohh... aang... i..."
    suki "......."
    show tosv tosv05
    hide suki_vag_blink
    with dissolve
    suki "...w...wait."
    suki "....aang, is... ngh... this really what-"
    show tosv tosv06
    with vshake
    suki "{i}aahhh....{/i}"
    show ctc
    pause
    hide ctc
    suki "ff...fu...fuck..."
    suki "it's... fuck... it's up there... shh.... ah...."
    show tosv tosv05
    show suki_vag_blink:
        xpos 208 ypos 85
    with dissolve
    suki "uhhnh...."
    show tosv tosv01
    hide suki_vag_blink
    with dissolve
    y "ready?"
    suki "for... what?"
    y "well, i'm going to fuck you with it."
    y "now that you're... warmed up."
    suki "y....yes."
    suki "please."
    show tosv tosv100
    with dissolve
    suki "ohhh.... fuck, aang...."
    show ctc
    pause
    hide ctc
    suki "i never thought.... unnhh.."
    hide suki_vag_blink with dissolve
    suki "i never thought you'd be... doing this with me.... {i}to{/i} me..."
    suki "with my kyoshi statue of all things..."
    suki "i... i love it... i fucking love it!"
    y "well then..."
    show tosv tosv101
    suki "ah!"
    show ctc
    pause
    hide ctc
    suki "yes! yes!"
    suki "fuck!"
    suki "fuck my little pussy with it!"
    suki "it feels so good!"
    suki "i want to... i already want to..."
    y "want to what?"
    suki "i already want to cu..."
    show ctc
    pause
    hide ctc
    suki "wait... i..."
    show tosv tosv101_1
    suki "why... why can't i cum...?"
    suki "ngh... uhgh... mmmnh...."
    suki "what... what is..."
    "while slamming suki's kyoshi statue in and out of her vagina, you remember the triangle hole at the bottom of the dildo."
    show kyoshi_dildo_bottom with dissolve

    if kyoshi_dildo_key:
        y "i have that triangle key... i wonder what would happen if..."
        menu:
            "use triangle key":

                show kyoshi_dildo_key
                with dissolve
                "you put the triangle key into the hole."
                hide kyoshi_dildo_bottom
                hide kyoshi_dildo_key
                with flash
                y "....."
                y "huh."
                y "doesn't look like anything-"
                $ kyoshi_suki_penetrate = "dildo_bzzz"
                "*bzzzt* *bzzzzt*"
                show tosv tosv101
                suki "aaahhhhh!!!!"
                y "are you okay?"
                "*bzzzzzt*"
                suki "it's... it's vibrating...!!"
                y "....seriously!? that's awesome!"
                suki "it's... ahh... it's too much..."
                "*bzzzzzt*"
                suki "so... goo... ff... good..."
                suki "i... i want to cum... i need..."
                $ kyoshi_suki_face = 'messy'
                show tosv tosv101_1 with dissolve
                suki "please... pleasee...."
                suki "ahh..."
            "don't use triangle key":

                hide kyoshi_dildo_bottom with dissolve
                y "I'm not going to mess with this right now..."
                suki "nnghh.... aang...."
                suki "it's... ahh... it's too much..."
                suki "so... goo... ff... good..."

    if not kyoshi_dildo_key:

        y "I don't have this key...."
        y "i wonder if it's in the tunnels somewhere?"
        hide kyoshi_dildo_bottom with dissolve
        suki "nnghh.... aang...."
        suki "it's... ahh... it's too much..."
        "*bzzzzzt*"
        suki "so... goo... ff... good..."

    show ctc
    pause
    hide ctc
    suki "please... i don't und.... understand..."
    suki "it's so...."
    y "well... are you going to be a good girl?"
    show tosv tosv101
    suki "wh....what...."
    y "are you going to be a good girl, and do as you're told?"
    suki "no... i... wh... please..."
    y "you're going to do as i say."
    y "I'm going to use your pussy as i see fit."
    suki "nngh... ah... fu..."
    y "and if i tell you to let a stranger use your pussy, even if just to slam a statue in your cunt..."
    y "you'll do it."
    suki "nngh... ah.. nnn... wh.... why...."
    y "agree...."
    suki "any... anything you... want.... please..."
    y "...i'll take it. for now."
    suki "ungh... pl... plea-"
    y "cum."
    show tosv tosv06 with vshake
    suki "{size=+5}aaaaaaahhhhhhhhhh!!!!!!!"
    with vshake
    show ctc
    pause
    hide ctc
    suki "fuuuuuuuuuuuuck......!"
    suki "..........."
    show tosv tosv04 with dissolve
    suki "i don't understand..."
    show ctc
    pause
    hide ctc
    suki "but thank-"
    y "cum."
    show tosv tosv06 with vshake
    suki "aahh!"
    suki "angh! fuck! ah!"
    suki "what..."
    y "cum."
    with vshake
    suki "nnno! ahhhh!"
    suki "nnngh!! fuuuuck!!"
    y "cum."
    with vshake
    suki "stop! st-"
    y "cum."
    with vshake
    with vshake
    suki "aaaaahhhhhhh!!!!"
    with vshake
    with vshake
    suki "nnnghhh!"
    show tosv tosv01
    show suki_vag_blink:
        xpos 208 ypos 85
    with dissolve
    y "suki?"
    y "......."
    show tosv tosv16
    hide suki_vag_blink
    with dissolve
    y "um..."
    show ctc
    pause
    hide ctc
    y "did... she pass out?"
    y "i guess i'll just let her rest..."
    show tosv tosv18 with dissolve
    y "sleep well, suki..."
    y "things are just starting for you."
    scene black with dissolve
    "tired as well, you stumble back to your house, where you sleep until the morning."
    jump bk3_next

label suki_dildo_fuck2:
    hide screen earth_money_date
    scene black
    scene kyoshi_bed_1
    with dissolve
    $ kyoshi_suki_face = 'neat'
    $ kyoshi_suki_penetrate = 'dildo'
    $ renpy.pause(0.5)
    show tosv tosv17 with dissolve
    suki "so?"
    suki "you gonna fuck me?"
    y "yeah."
    y "now lift your fucking thighs up."
    show tosv tosv15 with dissolve
    suki "how's this?"
    y "nice. you ready?"
    suki "i...."
    show tosv tosv16 with dissolve
    suki "......"
    suki "yes..."
    show tosv tosv01 with dissolve
    show ctc
    pause
    hide ctc
    y "say please."
    suki "...please..."
    show tosv tosv02 with dissolve
    suki "i feel it...."
    suki "aang, what are we-"
    show tosv tosv03
    show suki_vag_blink:
        xpos 208 ypos 85
    with dissolve
    show ctc
    pause
    hide ctc
    suki "uunhhh..."
    show tosv tosv04 with dissolve
    show ctc
    pause
    hide ctc
    suki "ohh... aang... i..."
    suki "......."
    show tosv tosv05
    hide suki_vag_blink
    with dissolve
    suki "wait!"
    suki "is this really what-"
    show tosv tosv06
    with vshake
    suki "{i}aahhh....{/i}"
    show ctc
    pause
    hide ctc
    suki "ff...fu...fuck..."
    suki "it's... fuck... it's up there... shh.... ah...."
    show tosv tosv05
    show suki_vag_blink:
        xpos 208 ypos 85
    with dissolve
    suki "uhhnh...."
    show tosv tosv01
    hide suki_vag_blink
    with dissolve
    y "ready?"
    suki "for... what?"
    y "well, i'm going to fuck you with it."
    y "now that you're... warmed up."
    suki "y....yes."
    suki "please."
    show tosv tosv100
    suki "ohhh.... fuck, aang...."
    show ctc
    pause
    hide ctc
    suki "i never thought.... unnhh.."
    hide suki_vag_blink with dissolve
    suki "i never thought you'd be... doing this with me.... {i}to{/i} me..."
    suki "with my kyoshi statue of all things..."
    suki "i... i love it... i fucking love it!"
    y "well then..."
    show tosv tosv101
    suki "ah!"
    show ctc
    pause
    hide ctc
    suki "yes! yes!"
    suki "fuck!"
    suki "it feels so good!"
    suki "i want to... i already want to..."
    y "want to what?"
    suki "i already want to cu..."
    show ctc
    pause
    hide ctc
    suki "wait... i..."
    show tosv tosv101_1
    suki "why... why can't i cum...?"
    suki "ngh... uhgh... mmmnh...."
    suki "what... what is..."
    "while slamming suki's kyoshi statue in and out of her vagina, you remember the triangle hole at the bottom of the dildo."
    show kyoshi_dildo_bottom with dissolve

    if kyoshi_dildo_key:
        y "i have that triangle key... i wonder what would happen if..."
        menu:
            "use triangle key":

                show kyoshi_dildo_key
                with dissolve
                "you put the triangle key into the hole."
                hide kyoshi_dildo_bottom
                hide kyoshi_dildo_key
                with flash
                y "....."
                y "huh."
                y "doesn't look like anything-"
                $ kyoshi_suki_penetrate = "dildo_bzzz"
                "*bzzzt* *bzzzzt*"
                show tosv tosv101
                suki "aaahhhhh!!!!"
                y "are you okay?"
                "*bzzzzzt*"
                suki "it's... it's vibrating...!!"
                y "....seriously!? that's awesome!"
                suki "it's... ahh... it's too much..."
                "*bzzzzzt*"
                suki "so... goo... ff... good..."
                suki "i... i want to cum... i need..."
                $ kyoshi_suki_face = 'messy'
                show tosv tosv101_1 with dissolve
                suki "please... pleasee...."
                suki "ahh..."
            "don't use triangle key":

                hide kyoshi_dildo_bottom with dissolve
                y "I'm not going to mess with this right now..."
                suki "nnghh.... aang...."
                suki "it's... ahh... it's too much..."
                suki "so... goo... ff... good..."

    if not kyoshi_dildo_key:

        y "I don't have this key...."
        y "i wonder if it's in the tunnels somewhere?"
        hide kyoshi_dildo_bottom with dissolve
        suki "nnghh.... aang...."
        suki "it's... ahh... it's too much..."
        "*bzzzzzt*"
        suki "so... goo... ff... good..."

    show ctc
    pause
    hide ctc
    suki "please... i don't und.... understand..."
    suki "it's so...."
    y "are you going to be a good girl, and do as you're told?"
    show tosv tosv101
    suki "i... wh... please..."
    y "I'm going to use your pussy as i see fit."
    suki "nngh... ah... fu..."
    suki "any... anything you... want.... please..."
    y "...i'll take it. for now."
    suki "ungh... pl... plea-"
    y "cum."
    show tosv tosv06 with vshake
    suki "{size=+5}aaaaaaahhhhhhhhhh!!!!!!!"
    with vshake
    show ctc
    pause
    hide ctc
    suki "fuuuuuuuuuuuuck......!"
    suki "..........."
    show tosv tosv04 with dissolve
    suki "i don't understand..."
    show ctc
    pause
    hide ctc
    suki "but thank-"
    y "cum."
    show tosv tosv06 with vshake
    suki "aahh!"
    suki "angh! fuck! ah!"
    suki "what..."
    y "cum."
    with vshake
    suki "nnno! ahhhh!"
    suki "nnngh!! fuuuuck!!"
    y "cum."
    with vshake
    suki "stop! st-"
    y "cum."
    with vshake
    with vshake
    suki "aaaaahhhhhhh!!!!"
    with vshake
    with vshake
    suki "nnnghhh!"
    show tosv tosv01
    show suki_vag_blink:
        xpos 208 ypos 85
    with dissolve
    y "suki?"
    y "......."
    show tosv tosv16
    hide suki_vag_blink
    with dissolve
    y "um..."
    show ctc
    pause
    hide ctc
    y "did... she pass out?"
    y "i guess i'll just let her rest..."
    show tosv tosv18 with dissolve
    y "sleep well, suki..."
    scene black with dissolve
    "tired as well, you stumble back to your house, where you sleep until the morning."
    jump bk3_next


label suki_dildo_fuck3:
    hide screen earth_money_date
    scene black
    scene kyoshi_bed_1
    with dissolve
    $ kyoshi_suki_face = 'neat'
    $ kyoshi_suki_penetrate = 'dick'
    menu:
        "kyoshi makeup":
            $ kyoshi_makeup = True
            $ kyoshi_suki_face = "neat"
        "no makeup":
            $ kyoshi_makeup = False
            $ kyoshi_suki_face = "none"
    $ renpy.pause(0.5)
    show tosv tosv17 with dissolve
    suki "so?"
    suki "you gonna fuck me with that dildo?"
    y "yeah."
    y "now lift your fucking thighs up."
    show tosv tosv15 with dissolve
    suki "how's this?"
    y "nice. you ready?"
    suki "i...."
    show tosv tosv16 with dissolve
    suki "......"
    suki "yes..."
    show tosv tosv01 with dissolve
    show ctc
    pause
    hide ctc
    y "say please."
    suki "...please..."
    show tosv tosv02 with dissolve
    suki "i feel it...."
    suki "aang, what are we-"
    show tosv tosv03
    if kyoshi_makeup:
        show suki_vag_blink:
            xpos 208 ypos 85
    else:
        show suki_blink_nomakeup:
            xpos 208 ypos 85
    with dissolve
    show ctc
    pause
    hide ctc
    suki "uunhhh..."
    show tosv tosv04 with dissolve
    show ctc
    pause
    hide ctc
    suki "ohh... aang... i..."
    suki "......."
    show tosv tosv05
    hide suki_vag_blink
    hide suki_blink_nomakeup
    with dissolve
    suki "wait!"
    suki "is this really what-"
    show tosv tosv06
    with vshake
    suki "{i}aahhh....{/i}"
    show ctc
    pause
    hide ctc
    suki "ff...fu...fuck..."
    suki "it's... fuck... it's up there... shh.... ah...."
    show tosv tosv05
    if kyoshi_makeup:
        show suki_vag_blink:
            xpos 208 ypos 85
    else:
        show suki_blink_nomakeup:
            xpos 208 ypos 85
    with dissolve
    suki "uhhnh...."
    show tosv tosv01
    hide suki_vag_blink
    hide suki_blink_nomakeup
    with dissolve
    y "ready?"
    suki "for... what?"
    y "well, i'm going to fuck you with it."
    y "now that you're... warmed up."
    suki "y....yes."
    suki "please."
    show tosv tosv100
    suki "ohhh.... fuck, aang...."
    show ctc
    pause
    hide ctc
    suki "i never thought.... unnhh.."
    hide suki_vag_blink with dissolve
    suki "i never thought you'd be... doing this with me.... {i}to{/i} me..."
    suki "with such a... meaty... dildo of all things..."
    suki "i... i love it... i fucking love it!"
    y "well then..."
    show tosv tosv101
    suki "ah!"
    show ctc
    pause
    hide ctc
    suki "yes! yes!"
    suki "fuck!"
    suki "it feels so good!"
    suki "i want to... i already want to..."
    y "want to what?"
    suki "i already want to cu..."
    show ctc
    pause
    hide ctc
    suki "wait... i..."
    show tosv tosv101_1
    suki "why... why can't i cum...?"
    suki "ngh... uhgh... mmmnh...."
    suki "what... what is..."

    suki "nnghh.... aang...."
    suki "it's... ahh... it's too much..."
    suki "so... goo... ff... good..."

    show ctc
    pause
    hide ctc
    suki "please... i don't und.... understand..."
    suki "it's so...."
    y "are you going to be a good girl, and do as you're told?"
    show tosv tosv101
    suki "i... wh... please..."
    y "I'm going to use your pussy as i see fit."
    suki "nngh... ah... fu..."
    suki "any... anything you... want.... please..."
    y "...i'll take it. for now."
    suki "ungh... pl... plea-"
    y "cum."
    show tosv tosv06 with vshake
    suki "{size=+5}aaaaaaahhhhhhhhhh!!!!!!!"
    with vshake
    show ctc
    pause
    hide ctc
    suki "fuuuuuuuuuuuuck......!"
    suki "..........."
    show tosv tosv04 with dissolve
    suki "i don't understand..."
    show ctc
    pause
    hide ctc
    suki "but thank-"
    y "cum."
    show tosv tosv06 with vshake
    suki "aahh!"
    suki "angh! fuck! ah!"
    suki "what..."
    y "cum."
    with vshake
    suki "nnno! ahhhh!"
    suki "nnngh!! fuuuuck!!"
    y "cum."
    with vshake
    suki "stop! st-"
    y "cum."
    with vshake
    with vshake
    suki "aaaaahhhhhhh!!!!"
    with vshake
    with vshake
    suki "nnnghhh!"





    ya "fuck, i'm gonna cum!"
    y "suki?"
    ya "you got so fucking tight...!"
    menu:
        "inside":
            y "take it, whore!"
            play sound "audio/splurt1.ogg"
            with flash
            y "ngh!"
            play sound "audio/splurt2.ogg"
            with flash
            y "nngh...."
            y "fuck..."
            show tosv tosv16
            show tosv_solodick
            show tosv_spermdrip
            with dissolve
            y "ahhhh...."
            show ctc
            pause
            hide ctc
            hide tosv_solodick
            hide tosv_spermdrip
            show tosv_spermout
            with dissolve
            y "...."
            y "sleep well, little whore."
            show ctc
            pause
            hide ctc
        "outside":

            show tosv tosv16
            show tosv_solodick
            with dissolve
            ya "take it, whore!"
            play sound "audio/splurt1.ogg"
            show tosv_spermshot
            pause 0.2
            hide tosv_spermshot

            show tosv_sperm1
            ya "ngh!"
            play sound "audio/splurt2.ogg"
            show tosv_spermshot
            pause 0.2
            hide tosv_spermshot

            show tosv_sperm2
            y "fuck!"
            play sound "audio/splurt3.ogg"
            show tosv_spermshot
            pause 0.2
            hide tosv_spermshot

            show tosv_sperm3
            y "aaahhh...."
            show ctc
            pause
            hide ctc
            y "...."
            hide tosv_solodick with dissolve
            y "sleep well, little whore."
            show ctc
            pause
            hide ctc

    scene black with dissolve
    "tired as well, you stumble back to your house, where you sleep until the morning."
    jump bk3_next

label toph_footjob1:
    $ toph_footjob = True
    $ toph_footjob_barechest = False
    $ toph_footjob = "dirt"




    scene black
    scene bg_bk3_tophome_night
    show toi toi04
    with dissolve
    t "so, hey!"

    show toi toi09 with dissolve
    t "um..."
    y "what's up?"
    show toi_blush with dissolve
    t "I... have something i want to ask you."
    y "okay...."
    show toi_blink with dissolve
    t "i....."
    t "........"
    show toi toi06
    hide toi_blink
    with dissolve
    t "I want to see..."
    y "what?"
    show toi toi04 with dissolve
    t "wait, first... let's sit."
    t "i've been on my feet all day."
    y "alright..."
    play sound "audio/thud.mp3"
    scene black
    scene bg_bk3_tophome_0
    show tofj tofj09
    show tofj_blink_ani
    with sshake
    "toph drops onto her butt with a thud."
    t "ugh... {i}finally.{/i}"
    y "now... what was your question?"
    show tofj_blush with dissolve
    t "I... um..."
    hide tofj_blink_ani
    show tofj_blink
    with dissolve
    t "i... {size=-15}wanna see your dick."
    y "what?"
    hide tofj_blink
    with dissolve
    t "....i wanna see your dick."
    show tofj_blink_ani
    y "that's.... not a question."
    t "well, i wanna see it."
    hide tofj_blink_ani
    show tofj tofj08
    hide tofj_blush
    with dissolve

    t "since we've been.... doing stuff with it..."
    t "for training...."
    t "it's only fair that i see it."
    y "uh, well, you make good points, but-"
    show tofj tofj09
    hide tofj_blink_ani
    show tofj_doubt
    with dissolve
    t "you whip it out all the time."
    t "so what's the problem?"
    y "....not {i}all{/i} the time...."
    y "also, are you sure?"
    hide tofj_doubt
    show tofj_smile
    with dissolve
    t "come on, you big baby!"
    t "whip it out!"
    y "i guess i can..."
    "you swiftly unleash your cock."
    show tofj tofj05
    hide tofj_smile
    with dissolve
    t "my innocent eyes!"
    y "i'm sorry! i thought-"
    t "how could you!"
    show tofj tofj06 with dissolve
    t "Ohhh... wow... but it's so big..."
    y "well, thank-"
    y "hey!"
    y "you're blind!"
    show tofj tofj09
    show tofj_smirk
    with dissolve
    t "took you long enough."
    y "that was... uncool."
    y "so, have you just been fucking with me?"
    hide tofj_smirk
    show tofj_doubt
    with dissolve
    t "what? no, i wanna see it."
    y "how?"
    t "well, i wasn't going to use my eyes, obviously."
    y "....what?"
    y "you can't.... see without your eyes..."
    hide tofj_doubt
    show tofj_smile
    with dissolve

    t "Sure i can!"
    t "i see with my feet."
    t "Why do you think I'm not wearing shoes?"
    show tofj tofj103
    show ctc
    pause
    hide ctc
    y "....."
    hide tofj_smile
    show tofj tofj08
    with dissolve
    t "they're like... a blindfold for me."
    y "wait... so you're gonna...."
    y "....feel me with your feet?"
    show tofj tofj09
    show tofj_doubt
    with dissolve
    t "well, duh."
    hide tofj_doubt
    show tofj_smirk
    with dissolve
    t "don't worry you pansy, i won't hurt you."
    t "I know how to use my feet."
    t "better than anyone you've ever met."
    y "huh."
    y "well... why do you wanna see my dick, again?"
    hide tofj_smirk
    show tofj_blink
    show tofj_blush
    with dissolve
    t "because I've never seen one."
    hide tofj_blink
    with dissolve
    t "It's not like dirty magazines come in braille!"
    t "...and since you've already been groping my breasts.... repeatedly...."
    show tofj_blink with dissolve
    t "it's only fair I get to do some groping of my own."
    y "It's not like I want to say no.... but it's delicate equipment...."
    y "are you really certain you won't break it accidentally?"
    hide tofj_blink
    show tofj_doubt
    hide tofj_blush
    show tofj_blush
    with dissolve
    t "You sure complain a lot... Are you a man, or a little girl?"
    y "I'm a man!"
    hide tofj_doubt
    show tofj_angry
    hide tofj_blush
    show tofj_blush
    with dissolve
    t "Are you a man or a little girl!?"
    ya "I'm a MAN!!!"
    t "Then prove it, twinkletoes!!"
    ya "fine!"
    show tofj_solodick with dissolve
    t "...."
    hide tofj_angry
    show tofj_doubt
    hide tofj_blush
    show tofj_blush
    with dissolve
    t "...."
    t "is it... out yet?"
    y "that would be hurtful, if i didn't know you were blind."
    t "okay, i'll just use my foot and-"
    y "maybe you should reach out with your hands first?"
    y "just to make sure you know how far away it is?"
    t "....."
    t "...fine..."
    show tofj_jack_1
    hide tofj_solodick
    y "hngh..."
    show ctc
    pause
    hide ctc
    t "is.... is this it?"
    t "am i touching it?"
    y "y...yes..."
    show tofj_jack_2
    hide tofj_jack_1
    hide tofj_doubt with dissolve
    t "ooooh..."
    show ctc
    pause
    hide ctc
    y "ahhh... goood....."
    t "you like that, huh?"
    t "how about...."
    show tofj_jack_slow
    hide tofj_jack_2
    $ renpy.pause(0.5)
    show tofj_smile
    hide tofj_blush
    show tofj_blush
    with dissolve
    t "hey! i can feel you tensing up!"
    y "you have... really tiny... fingers..."
    show ctc
    pause
    hide ctc
    show tofj_doubt
    hide tofj_smile
    hide tofj_blink_ani
    hide tofj_blush
    show tofj_blush
    with dissolve
    t "I do?"
    t "is that... good...?"
    y "very... good..."
    hide tofj_doubt
    show tofj_smirk
    hide tofj_blush
    show tofj_blush
    with dissolve
    t "oh?"
    show tofj_jack_fast
    hide tofj_jack_slow
    t "then how about this?"
    show ctc
    pause
    hide ctc
    y "ohhh... shit, toph!"
    hide tofj_smirk
    show tofj_smile
    hide tofj_blush
    show tofj_blush
    with dissolve
    t "yeah!?"
    t "i'm doing good?"
    t "awesome!"
    y "just... a little... more..."
    show expression "bk3/toph/footjob/jack03.png"
    hide tofj_jack_fast
    hide tofj_smile
    with dissolve
    $ renpy.pause(0.25)
    y "hey!"
    y "why'd you stop?"
    hide tofj_smile
    show tofj_doubt
    hide tofj_blush
    show tofj_blush
    with dissolve
    t "what?"
    t "because i want to see it?"
    t "which is why we're here?"
    y "oh... right."
    hide expression "bk3/toph/footjob/jack03.png"
    hide tofj_doubt
    with dissolve
    t "so...."
    show tofj tofj103 with dissolve
    t "give it here!"
    y "wait. um. are you just going to use your dirty feet?"
    show tofj_doubt
    hide tofj_blush
    show tofj_blush
    with dissolve
    t "well, yeah?"
    t "it's got dirt on it, which is {i}earth{/i} and earthbending helps me see..."
    t "unless you have a problem with that?"
    menu:
        "do what you gotta":
            y "if that helps you, then do what you need to."
            hide tofj_doubt with dissolve
            t "sweet."
        "clean feet, please":

            y "i'd really prefer you cleaned them off, first."
            show tofj tofj09 with dissolve
            t "oh, fine."
            hide tofj_doubt
            show tofj_blink
            with dissolve
            t "......"
            hide tofj_blink
            $ toph_footjob = "clean"
            show tofj tofj103 with dissolve
            t "there. how's that?"
            y "better."

    t "alright, pull it back out."
    show tofj tofj15 with dissolve
    show tofj_doubt
    hide tofj_blush
    show tofj_blush
    with dissolve
    t "huh."
    show ctc
    pause
    hide ctc
    y "what?"
    show tofj tofj101
    t "it's..."
    show ctc
    pause
    hide ctc
    t "hmm..."
    y "nngh..."
    t "...a little different than i expected..."
    y "y...yeah? how...ow...?"
    t "it's..."
    hide tofj_doubt
    show tofj_smile
    hide tofj_blush
    show tofj_blush
    with dissolve
    t "a lot bigger than i expected!"
    t "and..."
    hide tofj_smile
    show tofj_blink
    hide tofj_blush
    show tofj_blush
    with dissolve
    t "...somehow hard and soft at the same time."
    y "well, that's... ahh... that's a dick for you."
    hide tofj_blink
    show tofj_smile
    hide tofj_blush
    show tofj_blush
    with dissolve
    t "great!"
    show tofj tofj09 with dissolve
    t "thanks!"
    y "wait-"

    t "that was fun! and now i know what-"
    ya "oh, no you don't!"
    hide tofj_smile
    show tofj_doubt
    hide tofj_blush
    show tofj_blush
    with dissolve
    t "...what?"
    ya "here's something you should know about a dick..."
    ya "if you play with it, and then stop, you can really hurt it."
    t "really?"
    ya "yeah. it's called blue-balls, and it's a serious condition."
    t "i didn't know that..."
    y "but if you take care of it, it feels very {i}good{/i}."
    y "so you have the choice to either help me or hurt me."
    t "uhm..."
    t "well, you have been doing well in your training..."
    t "i guess we can do some more positive reinforcement."
    y "good. then continue."
    hide tofj_doubt
    show tofj_angry
    hide tofj_blush
    show tofj_blush
    with dissolve
    t "don't order me around, aang!"
    t "....."
    hide tofj_angry
    show tofj_doubt
    hide tofj_blush
    show tofj_blush
    with dissolve
    t "but i don't want to hurt you."
    t "come on, bring it back out."
    show tofj tofj101 with dissolve
    t "how's this?"
    y "nice..."
    t "is it... is it enough?"
    y "a little faster..."
    show tofj tofj101_1
    hide tofj_doubt
    show tofj_smirk
    hide tofj_blush
    show tofj_blush
    t "like... this?"
    show ctc
    pause
    hide ctc
    y "yes... ngh..."
    y "you know, it would help if i could look at your tits."
    hide tofj_smirk with dissolve
    t "come on aang, just finish already."
    menu:
        "rip open her shirt":
            show tofj tofj09
            show tofj_doubt
            hide tofj_blush
            show tofj_blush
            with dissolve
            t "what are you-"
            $ toph_footjob_barechest = True
            with sshake
            hide tofj_doubt
            show tofj_angry
            hide tofj_blush
            show tofj_blush
            with dissolve
            t "hey!"
            t "what the heck, aang!?"
            show ctc
            pause
            hide ctc
            hide tofj_angry
            show tofj tofj08
            with dissolve
            t "you...."
            t "you ripped my shirt..."

            show tofj tofj09
            show tofj_doubt
            hide tofj_blush
            show tofj_blush
            with dissolve
            t "why would-"
            ya "pick up your foot..."
            show tofj tofj10 with dissolve
            t "umm..."
            ya "and get back to work!"
            show tofj tofj101_1 with dissolve
        "have her speed up":

            ya "faster, toph!"
            show tofj_doubt
            hide tofj_blush
            show tofj_blush
            ya "come on!"
            pass

    t "what... what's gotten into you..."
    ya "faster!"
    show tofj tofj102
    t "umm..."
    show ctc
    pause
    hide ctc
    y "fuck yes..."
    y "that's it..."
    y "more..."
    t "aang... you're..."
    hide tofj_doubt
    show tofj_smirk
    hide tofj_blush
    show tofj_blush
    with dissolve
    t "mmmmmm...."
    ya "faster!"
    ya "use those tiny fucking feet, toph!"
    show tofj tofj102_1
    ya "yes!"
    ya "that's it...!"
    show ctc
    pause
    hide ctc
    t "that's... okay... aang..."
    ya "make me cum with your fucking toes!"
    t "this is kinda..."
    t "...hot!"
    hide tofj_blink_ani
    hide tofj_smirk
    show tofj_angry
    hide tofj_blush
    show tofj_blush
    with dissolve
    t "i'm doing it!"
    t "I'm jacking your... your cock!"
    ya "i'm gonna... i'm..."
    show tofj tofj101_2 with dissolve
    ya "don't you dare slow down!"
    t "come on, aang!"
    ya "ungh!"
    play sound "audio/splurt2.ogg"
    show tofj_sperm0
    $ renpy.pause(0.1)
    hide tofj_sperm0
    show tofj_sperm1
    hide tofj_angry
    show tofj_doubt
    hide tofj_blush
    show tofj_blush
    with dissolve
    t "oh!"
    t "is... is this..."
    y "fuck!"
    play sound "audio/splurt2.ogg"
    show tofj tofj18 with dissolve
    show tofj_sperm0
    $ renpy.pause(0.1)
    hide tofj_sperm0
    show tofj_sperm2
    $ renpy.pause(0.25)
    hide tofj_doubt
    show tofj_blink
    hide tofj_blush
    show tofj_blush
    hide tofj_sperm2
    show tofj_sperm2
    with dissolve
    t "this... you're... hm..."
    y "take it, you little slut!"
    play sound "audio/splurt2.ogg"
    hide tofj_sperm1
    show tofj_sperm0
    $ renpy.pause(0.1)
    hide tofj_sperm0
    show tofj_sperm3
    y "yes!"
    t "........"
    hide tofj_doubt
    show tofj_smirk
    hide tofj_blush
    show tofj_blush
    hide tofj_blink
    show tofj_blink
    hide tofj_sperm3
    show tofj_sperm3
    with dissolve
    t "ohhh... aang..."
    show ctc
    pause
    hide ctc
    show tofj tofj09 with dissolve
    y "ahh..."
    t "you..."
    hide tofj_blink with dissolve

    t "you... covered me..."
    y "damn... that was nice..."
    show tofj_blink with dissolve
    t "......"
    hide tofj_blink
    hide tofj_angry
    hide tofj_doubt
    hide tofj_blush
    show tofj_blush
    hide tofj_sperm3
    show tofj_sperm3
    with dissolve
    t "that was... really hot, aang."
    t "it's great that... this also helps your training."
    t "i mean, this... is positive reinforcement, right?"
    y "what?"
    y "oh, yeah."
    y "sure, whatever... damn..."
    show tofj_doubt
    hide tofj_blush
    show tofj_blush
    hide tofj_sperm3
    show tofj_sperm3
    with dissolve
    t "...."
    t "you're...."
    t "....you're not just taking advantage of me, right?"
    y "well... i mean, you're enjoying it, too."
    t "wait, you..."
    show tofj_angry
    hide tofj_blush
    hide tofj_doubt
    show tofj_blush
    hide tofj_sperm3
    show tofj_sperm3
    with dissolve
    t "you... you... sick jerk!"
    y "what? you want it!"
    t "n-no, i don't!"
    t "get... get out!"
    y "wait... um... i'm... not lying?"
    t "get out!"
    play sound "audio/thud.mp3"
    scene black with vshake
    "toph forcibly earthbends you outside through the wall, which she closes behind you."
    y "ugh... that was... painful..."
    "you pass out...."
    scene inside_shack with dissolve
    "....and wake up in your house."
    y "what the hell."
    y "i mean... she was clearly enjoying it."
    y "but, she's super pissed..."
    y "now what?"
    y "............"
    y "Katara has been surprisingly understanding lately."
    y "i should see what she has to say."
    jump bk3_next

label toph_footjob1_2:
    $ toph_footjob = True
    $ toph_footjob_barechest = False
    $ toph_footjob = "dirt"

    scene black
    scene bg_bk3_tophome_0
    show tofj tofj09
    show tofj_blink_ani
    with sshake
    "toph drops onto her butt with a thud."
    t "come on, then..."

    show tofj tofj08
    hide tofj_blush
    with dissolve

    t "if... that's what you want..."
    show tofj tofj09 with dissolve
    t "take it out then."
    show tofj_solodick with dissolve
    y "jack it, first."
    t "...fine..."
    show tofj_jack_1
    hide tofj_solodick
    y "hngh..."
    show ctc
    pause
    hide ctc
    t "is.... is this good?"
    y "y...yes..."
    show tofj_jack_2
    hide tofj_jack_1
    hide tofj_doubt with dissolve
    t "......."
    show ctc
    pause
    hide ctc
    y "ahhh... goood....."
    t "you like that, huh?"
    t "how about...."
    show tofj_jack_slow
    hide tofj_jack_2
    $ renpy.pause(0.5)
    show tofj_smile
    hide tofj_blush
    show tofj_blush
    with dissolve
    t "you really like that, huh?"
    y "you have... really tiny... fingers..."
    show ctc
    pause
    hide ctc
    show tofj_doubt
    hide tofj_smile
    hide tofj_blink_ani
    hide tofj_blush
    show tofj_blush
    with dissolve
    t "I guess...."
    hide tofj_doubt
    show tofj_smirk
    hide tofj_blush
    show tofj_blush
    with dissolve
    t "is that nice?"
    show tofj_jack_fast
    hide tofj_jack_slow
    t "then how about this?"
    show ctc
    pause
    hide ctc
    y "ohhh... shit, toph!"
    hide tofj_smirk
    hide tofj_blush
    show tofj_blush
    show expression "bk3/toph/footjob/jack03.png"
    hide tofj_jack_fast
    hide tofj_smile
    with dissolve
    $ renpy.pause(0.25)
    y "i want you to use your feet now."
    hide tofj_smile
    show tofj_doubt
    hide tofj_blush
    show tofj_blush
    with dissolve
    t "....okay."
    hide expression "bk3/toph/footjob/jack03.png"
    hide tofj_doubt
    with dissolve
    t "so...."
    show tofj tofj103 with dissolve
    t "give it here."
    menu:
        "do what you gotta":
            y "if that helps you, then do what you need to."
            hide tofj_doubt with dissolve
            t "sweet."
        "clean feet, please":

            y "i'd really prefer you cleaned them off, first."
            show tofj tofj09 with dissolve
            t "oh, fine."
            hide tofj_doubt
            show tofj_blink
            with dissolve
            t "......"
            hide tofj_blink
            $ toph_footjob = "clean"
            show tofj tofj103 with dissolve
            t "there. how's that?"
            y "better."

    t "alright, pull it back out."
    show tofj tofj15 with dissolve
    show tofj_doubt
    hide tofj_blush
    show tofj_blush
    with dissolve
    t "huh."
    show ctc
    pause
    hide ctc
    y "what?"
    show tofj tofj101
    t "......."
    show ctc
    pause
    hide ctc
    t "hmm..."
    y "nngh..."
    hide tofj_doubt
    show tofj_smile
    hide tofj_blush
    show tofj_blush
    with dissolve
    t "it's still... bigger than i expected..."
    hide tofj_smile
    show tofj_blink
    hide tofj_blush
    show tofj_blush
    with dissolve
    y "you know just what to say...."
    show tofj tofj101_1
    hide tofj_doubt
    show tofj_smirk
    hide tofj_blink
    hide tofj_blush
    show tofj_blush
    y "ungh... you sped up..."
    show ctc
    pause
    hide ctc
    t "just... finish..."
    y "you know, it would help if i could look at your tits."
    hide tofj_smirk with dissolve
    t "come on aang, just finish already."
    menu:
        "rip open her shirt":
            show tofj tofj09
            show tofj_doubt
            hide tofj_blush
            show tofj_blush
            with dissolve
            t "what are you-"
            $ toph_footjob_barechest = True
            with sshake
            hide tofj_doubt
            show tofj_angry
            hide tofj_blush
            show tofj_blush
            with dissolve
            t "hey!"
            t "what the heck, aang!?"
            show ctc
            pause
            hide ctc
            hide tofj_angry
            show tofj tofj08
            with dissolve
            t "you...."
            t "you ripped my shirt..."

            show tofj tofj09
            show tofj_doubt
            hide tofj_blush
            show tofj_blush
            with dissolve
            t "why would-"
            ya "pick up your foot..."
            show tofj tofj10 with dissolve
            ya "and get back to work!"
            show tofj tofj101_1 with dissolve
        "have her speed up":

            ya "faster, toph!"
            show tofj_doubt
            hide tofj_blush
            show tofj_blush
            ya "come on!"
            pass

    ya "faster!"
    show tofj tofj102
    t "umm..."
    show ctc
    pause
    hide ctc
    y "fuck yes..."
    y "that's it..."
    y "more..."
    t "aang......"
    ya "faster!"
    ya "use those tiny fucking feet, toph!"
    show tofj tofj102_1
    ya "yes!"
    ya "that's it...!"
    show ctc
    pause
    hide ctc
    t "i don't really like this, aang..."
    ya "make me cum with your fucking toes!"
    hide tofj_blink_ani
    show tofj_angry
    hide tofj_blush
    show tofj_blush
    with dissolve
    t "i'm doing it! stop being a jerk!"
    ya "i'm gonna... i'm..."
    show tofj tofj101_2 with dissolve
    ya "don't you dare slow down!"
    t "if you don't stop being mean, i'll just stop!"
    t "you-"
    ya "ungh!"
    play sound "audio/splurt2.ogg"
    show tofj_sperm0
    $ renpy.pause(0.1)
    hide tofj_sperm0
    show tofj_sperm1
    hide tofj_angry with dissolve
    t "w...what-"
    y "fuck!"
    play sound "audio/splurt2.ogg"
    show tofj tofj18 with dissolve
    show tofj_sperm0
    $ renpy.pause(0.1)
    hide tofj_sperm0
    show tofj_sperm2
    $ renpy.pause(0.25)
    show tofj_angry
    show tofj_blink
    hide tofj_blush
    show tofj_blush
    hide tofj_sperm2
    show tofj_sperm2
    with dissolve
    t "i... can't believe you'd..."
    y "take it, you little slut!"
    play sound "audio/splurt2.ogg"
    hide tofj_sperm1
    show tofj_sperm0
    $ renpy.pause(0.1)
    hide tofj_sperm0
    show tofj_sperm3
    y "yes!"
    t "........"
    t "ungh... you..."
    show ctc
    pause
    hide ctc
    show tofj tofj09 with dissolve
    y "ahh..."
    t "you're..."
    hide tofj_blink with dissolve
    t "you're such a jerk."
    y "damn... that was nice..."
    hide tofj_angry
    show tofj_blink
    with dissolve
    t "i'm covered in this gross..."
    t "......"
    y "that was fun, thanks."
    y "i'll be back later."
    t "............."
    scene black with dissolve
    "you head home for the night."
    jump bk3_next

label toph_footjob2:
    $ toph_footjob2_nude = False
    scene black
    scene bg_bk3_tophome_0
    show tofj tofj50
    with vshake
    "toph sits down with a thump."
    show ctc
    pause
    hide ctc
    t "...fine."
    t "what... what did you want?"
    show tofj2_solodick with dissolve
    y "what do you think?"
    show tofj2_uncertain with dissolve
    t "....."
    show ctc
    pause
    hide ctc
    show tofj2_blink
    hide tofj2_uncertain
    with dissolve
    t "......"
    t "fine."
    t "you win."
    show tofj tofj51
    hide tofj2_solodick
    with dissolve
    t "......"
    y "i'm waiting...."
    hide tofj2_blink with dissolve
    t "......."
    show tofj tofj105
    show ctc
    pause
    hide ctc
    y "yes... that's it..."
    y "you really {i}do{/i} know what you're doing with those..."
    t "......."
    y "still... this is a little underwhelming..."
    t "wait... i can speed up..."
    show tofj tofj106
    show tofj2_uncertain
    with dissolve
    t "is..."
    t "is this better...?"
    show ctc
    pause
    hide ctc
    y "ngh.... yeah..."
    y "keep... keep going..."
    t "please... please don't tell my parents where i am..."
    t "please don't tell on me."
    t "i'll... i'll rub you..."
    t "with my feet, when you ask."
    t "if you want."
    y "make me cum, and we'll see."
    show tofj tofj107
    hide tofj2_uncertain
    show tofj2_blink
    with dissolve
    t "i understand."
    show ctc
    pause
    hide ctc
    y "yes... yes..."
    t "ngh... hmph... agh...."
    t "this is... a lot of work..."
    y "open your eyes!"
    hide tofj2_blink with dissolve
    y "i'm... going to..."
    y "here it comes!"
    y "slow down, but don't you fucking stop!"
    show tofj tofj105 with dissolve
    y "ngh!"
    play sound "audio/splurt2.ogg"
    show tofj2_spermshot
    pause 0.2
    hide tofj2_spermshot
    show tofj2_sperm1
    y "little whore!"
    play sound "audio/splurt3.ogg"
    show tofj2_spermshot
    pause 0.2
    hide tofj2_spermshot
    show tofj2_sperm2
    hide tofj2_sperm1
    y "jack my cock with those cute little toes!"
    show tofj2_uncertain
    hide tofj2_sperm2
    show tofj2_sperm2
    with dissolve
    t "I... i'm trying!"
    show tofj tofj51 with dissolve
    play sound "audio/splurt1.ogg"

    show tofj2_spermshot
    pause 0.2
    hide tofj2_spermshot
    show tofj2_sperm3
    hide tofj2_sperm2
    y "NNNGHGHGH!"
    show ctc
    pause
    hide ctc
    t "......."
    t "is this... are you done?"
    t "can we just... move on now?"
    y "you really think this was it?"
    show tofj2_blink
    hide tofj2_uncertain
    hide tofj2_sperm3
    show tofj2_sperm3
    with dissolve
    y "maybe for tonight."
    y "besides, believe it or not, this is helping me become a better avatar."
    hide tofj2_blink with dissolve
    y "go find a towel."
    t "aang..."
    y "*sigh...*"
    y "you brought this on yourself."
    show ctc
    pause
    hide ctc
    scene black with dissolve
    "you head home for the night."
    jump bk3_next

label toph_footjob2_2:
    $ toph_footjob2_nude = False
    scene black
    scene bg_bk3_tophome_0
    show tofj tofj50
    with vshake
    "toph sits down with a thump."
    menu:
        "nude":
            $ toph_footjob2_nude = True
        "clothed":
            $ toph_footjob2_nude = False
    show ctc
    pause
    hide ctc
    t "...fine."
    t "take it out."
    show tofj2_solodick with dissolve
    y "that's what i like to hear."
    show tofj2_uncertain with dissolve
    t "....."
    show ctc
    pause
    hide ctc
    show tofj2_blink
    hide tofj2_uncertain
    with dissolve
    t "......"
    show tofj tofj51
    hide tofj2_solodick
    with dissolve
    t "......"
    y "you can start at any time...."
    hide tofj2_blink with dissolve
    t "......."
    show tofj tofj105
    show ctc
    pause
    hide ctc
    y "yes... that's it..."
    y "come on, slut..."
    t "......."
    y "you can do better..."
    t "i'll... i'll speed up..."
    show tofj tofj106
    show tofj2_uncertain
    with dissolve
    t "is..."
    t "is this better...?"
    show ctc
    pause
    hide ctc
    y "ngh.... yeah..."
    y "keep... keep going..."
    t "please... don't tell my parents where i am..."
    y "make me cum, and we'll see."
    show tofj tofj107
    hide tofj2_uncertain
    show tofj2_blink
    with dissolve
    t "i'll... i'll try..."
    show ctc
    pause
    hide ctc
    y "yes... yes..."
    t "ngh... hmph... agh...."
    t "this is... hard..."
    y "open your eyes!"
    hide tofj2_blink with dissolve
    y "i'm... going to..."
    y "here it comes!"
    y "slow down, but don't you fucking stop!"
    show tofj tofj105 with dissolve
    y "ngh!"
    play sound "audio/splurt2.ogg"
    show tofj2_spermshot
    pause 0.2
    hide tofj2_spermshot
    show tofj2_sperm1
    y "little whore!"
    play sound "audio/splurt3.ogg"
    show tofj2_spermshot
    pause 0.2
    hide tofj2_spermshot
    show tofj2_sperm2
    hide tofj2_sperm1
    y "jack my cock with those cute little toes!"
    show tofj2_uncertain
    hide tofj2_sperm2
    show tofj2_sperm2
    with dissolve
    t "I... i'm trying!"
    show tofj tofj51 with dissolve
    play sound "audio/splurt1.ogg"
    show tofj2_spermshot
    pause 0.2
    hide tofj2_spermshot
    show tofj2_sperm3
    hide tofj2_sperm2
    y "NNNGHGHGH!"
    show ctc
    pause
    hide ctc
    t "......."
    t "is this... are you done?"
    y "for tonight."
    show tofj2_blink
    hide tofj2_uncertain
    hide tofj2_sperm3
    show tofj2_sperm3
    with dissolve
    y "thanks for your help."
    y "your secret's safe with me."
    hide tofj2_blink with dissolve
    y "now, go find a towel."
    show ctc
    pause
    hide ctc
    scene black with dissolve
    "you head home for the night."
    jump bk3_next

label toph_sex1:
    hide screen earth_money_date
    scene black
    scene bg_bk3_tophome_night
    show toi toi04
    with dissolve
    $ toph_sex = True
    t "hey!"
    y "we're going to do something special tonight, toph."
    show toi toi09 with dissolve
    t "we are?"
    y "yes."
    y "we're going to have sex."
    show toi toi10 with dissolve
    t "s-sex!?"
    t "actual... sex?"
    y "that's right..."
    y "I'm tired of waiting."
    y "i think you want it, too."
    show toi toi09 with dissolve
    t "well..."
    t "i think that's a little sudden."
    t "i mean, we've only just-"
    y "i'm done waiting, toph."
    y "i know you want it."
    y "and you know what's at stake, here."
    show toi_blink with dissolve
    t "i... i understand..."
    y "lay down."
    scene black with dissolve
    scene bg_toph_missionary
    show totm totm11
    with dissolve
    t "like... this, aang?"
    y "you look... delicious."
    y "is that weird to say?"
    y "that felt weird."
    t "meh."
    y "don't \"meh\" me!"
    y "you're naked here!"
    t "yeah, but... come on, i can kick your butt even like this."
    y "i hold your future in my hands, so... maybe try not to emasculate me?"
    t "come on, already!"
    t "i've been dying to try this."
    y "really?"
    t "my life seems to be... spiraling out of control lately, and..."
    t "...this stuff seems to be the only thing centering me."
    t "it has order, but... it's liberating in a way."
    t "I know i don't have a lot of choice, but..."
    y "spread your legs."
    t "....."
    show totm totm00 with dissolve
    t "like this?"
    show ctc
    pause
    hide ctc
    y "damn, girl."
    y "it's time."
    y "are you ready?"
    t "i-"
    show totm totm01 with dissolve
    show ctc
    pause
    hide ctc
    t "uhh..."
    y "I'm right at your little entrance..."
    y "do you feel that?"
    t "y-yes, i'm a little nerv-"
    show totm totm02
    show totm_shock
    with dissolve
    t "aahhhh.... you're... you're slipping inside..."
    show ctc
    pause 
    hide ctc
    t "it's... i've never..."
    y "the head's almost in..."
    hide totm_shock with dissolve
    t "are... are you sure it's not in yet?"
    t "i can feel it ins-"
    show totm totm03
    show totm_shock
    with pflash
    t "hhhgh..."
    show ctc
    pause
    hide ctc
    t "ohh.... oh my god...."
    t "it's big... it's so b-"
    show totm totm04
    hide totm_shock
    with vshake
    t "ow!!"
    t "h-hey... ahhh...!"
    t "give... give me a second..."
    t "....."
    show totm totm03 with dissolve
    t "o...okay..."
    t "if you want, you can-"
    show totm totm102
    t "ow! nghh! ah!"
    t "eas... easy, aang!"
    show ctc
    pause
    hide ctc
    y "you want me to go easy on you?"
    t "y-yeah! ow! please!"
    y "okay, then."
    show totm totm101
    show expression "bk3/toph/missionary/blink.png"
    with dissolve
    t "ohh..."
    show ctc
    pause
    hide ctc
    y "how's that?"
    t "b-better..."
    y "a little easier?"
    y "not slamming your little cunt quite so forcefully?"
    t "thank... thank you, aang..."
    y "don't thank me yet."
    scene black
    show expression "bk3/toph/missionary/bg_toph_missionary1.jpg"

    show totm_cdick:
        ypos 20 xpos 477
        linear 1.0 ypos 120
        linear 1.0 ypos 20
        repeat

    show totm totm20
    with dissolve
    show ctc
    pause
    hide ctc
    y "i've been thinking..."
    t "...nnnhh... uhh...."
    y "you've had such a stressful time..."
    y "i think you need some sexual healing."
    t "sexual... ah... healing... nf...?"
    y "there's a very special technique..."
    t "ah... nh... wha...?"
    show ctc
    pause
    hide ctc
    menu:
        "choke a bitch":
            y "have you heard of asphyxiation?"
            t "as... ohhh... fix... wha...?"
            show expression "bk3/toph/missionary/chands.png":
                ypos -200
                linear 3.0 ypos -100
            $ renpy.pause(3, hard = True)

            show totm_cdick:
                ypos 20
                easein 2.0 ypos 120
                easeout 2.0 ypos 20
                repeat


            hide expression "bk3/toph/missionary/chands.png"
            show totm totm25 with vpunch

            t "hrk!"
            "You feel Toph tightening, making you go slower."
            show ctc
            pause
            hide ctc
            t "ghh...hgh...agh..."
            t "an...i...anh...eeth.."
            show expression "bk3/toph/missionary/cface_lewd.png"
            with dissolve

            y "Yeah, you like that, doncha?"
            show ctc
            pause
            hide ctc
            t "hhgh...hrk..."
            y "it's the lack of air."
            y "it can make the pleasure... more intense."
            t "hgh...gh..."
            show totm totm20
            show expression "bk3/toph/missionary/chands_open.png"
            hide expression "bk3/toph/missionary/cface_lewd.png"
            with dissolve
            "You release your grip to allow her to gasp for air."
            show ctc
            pause
            hide ctc
            t "*pant* *pant*"
            t "i... i couldn't breathe..."
            t "but it did feel-"
            hide expression "bk3/toph/missionary/chands_open.png"
            show totm totm25 with vpunch
            t "gagh!"
            "you tighten your grip once more."
            show expression "bk3/toph/missionary/cface_lewd.png"
            with dissolve
            t "hnnnghhahh..."
            y "i can't believe how tight you are..."
            y "i'm struggling to pull out of you each time..."
            show ctc
            pause
            hide ctc
            y "fuck..."
            y "fuck, toph..."
            y "your tight fucking cunt is gonna..."
            y "gonna make me...."
            menu:
                "don't release your grip until you cum":
                    "you speed up despite the clamplike feeling of Toph's pussy."
                    show totm_cdick:
                        ypos 20
                        easein 0.5 ypos 120
                        easeout 0.5 ypos 20
                        repeat
                    t "ngh! hrk! gh!"
                    y "that's it, bitch!"
                    y "you're mine! you're my little fucking whore!"
                    y "say it!"
                    t "...hghh!"
                    y "say you're my fucking whore!"
                    t "ahh...uuugh...ohhh..."
                    y "yes! you little slut!"
                    y "You cock loving slut!"
                    y "i'm almost there!"
                    menu:
                        "cum inside":

                            y "let's give you a creampie!"
                            t "nngh! aohh!"
                            play sound "audio/splurt2.ogg"
                            show totm_cdick:
                                ypos 120
                            with flash
                            "You empty your balls inside of Toph."
                            show totm totm20

                            show totm_cdick:
                                ypos -100
                            show expression "bk3/toph/missionary/csperm_in.png"
                            with Dissolve(2.0)

                            y "Aaaah.. that was the best."
                            hide expression "bk3/toph/missionary/csperm_in.png"
                        "cum outside":


                            ya "little slut!"
                            t "ah! oo 'ant-"
                            hide totm_cdick
                            show totm_cdick:
                                ypos 100 xpos 480
                            "In one big explosion, you release every drop of sperm from your balls on Toph's face."
                            show expression "bk3/toph/mastur_kat/white.png"
                            show expression "bk3/toph/missionary/csperm_out.png"
                            hide expression "bk3/toph/mastur_kat/white.png" with Dissolve(2.0)
                            show totm totm20 with Dissolve(1.5)

                            y "Aaaah... fuck. You're the best, Toph."


                    hide totm_cdick
                    y "Okay, I'll let myself out."
                    t "I... i don't think i'm..."
                    t "...going to be able to walk tomorrow..."
                    scene black with dissolve
                    "worn out, you head home for the night."
                    jump bk3_next
                "let her breathe":

                    show totm totm20 with Dissolve(1)
                    hide expression "bk3/toph/missionary/cface_lewd.png" with Dissolve(1)
                    t "ahh... hhha..."
                    show ctc
                    pause
                    hide ctc
                    t "it... it does feel..."
                    t "i'm so... dizzy..."
                    show totm_cdick:
                        ypos 20
                        easein 0.5 ypos 120
                        easeout 0.5 ypos 20
                        repeat
                    show expression "bk3/toph/missionary/cface_lewd.png" with dissolve
                    "you speed up as you feel yourself approaching climax..."
                    t "hah... ah... yes..."
                    t "yes... aang..."
                    hide expression "bk3/toph/missionary/cface_lewd.png" with dissolve
                    t "give... give it to... ahn... m-me..."
                    menu:
                        "cum inside":
                            ya "ngh! fuck!"
                            ya "let's give you a creampie!"
                            show totm totm26 with vshake
                            t "wait! don't!"
                            y "slut!"
                            show totm totm27
                            t "no!!!"
                            play sound "audio/splurt2.ogg"
                            show totm_cdick:
                                ypos 120
                            with flash
                            "You empty your balls inside of Toph."
                            show totm totm20

                            show totm_cdick:
                                ypos -100
                            show expression "bk3/toph/missionary/csperm_in.png"
                            with Dissolve(2.0)
                            t "uunngh...."
                            y "Aaaah.. that was the best."
                            hide expression "bk3/toph/missionary/csperm_in.png"

                            hide totm_cdick
                            y "Okay, I'll let myself out."
                            t "I... i don't think i'm..."
                            t "...going to be able to walk tomorrow..."
                            show ctc
                            pause
                            hide ctc
                            scene black with dissolve
                            "worn out, you head home for the night."
                            jump bk3_next
                        "cum outside":

                            ya "little slut!"
                            show expression "bk3/toph/missionary/cface_lewd.png" with dissolve
                            t "wait, what are you-"
                            hide totm_cdick
                            show totm_cdick:
                                ypos 100 xpos 480
                            "In one big explosion, you release every drop of sperm from your balls on Toph's face."
                            play sound "audio/splurt2.ogg"
                            show expression "bk3/toph/mastur_kat/white.png"
                            show expression "bk3/toph/missionary/csperm_out.png"
                            $ renpy.pause(0.05)
                            hide expression "bk3/toph/missionary/cface_lewd.png"
                            hide expression "bk3/toph/mastur_kat/white.png"
                            with Dissolve(1.5)
                            show ctc
                            pause
                            hide ctc
                            show totm totm20 with Dissolve(1.5)

                            y "Aaaah... fuck. You're the best, Toph."
                            hide totm_cdick
                            y "Okay, I'll let myself out."
                            t "I... i don't think i'm..."
                            t "...going to be able to walk tomorrow..."
                            show ctc
                            pause
                            hide ctc
                            scene black with dissolve
                            "worn out, you head home for the night."
                            jump bk3_next
                        "first position":

                            scene black
                            show expression "bk3/toph/missionary/bg_toph_missionary.jpg"
                            show totm totm105
                            with dissolve
                            pass
        "first position":
            scene black
            show expression "bk3/toph/missionary/bg_toph_missionary.jpg"
            show totm totm101
            show expression "bk3/toph/missionary/head_shock.png"
            show expression "bk3/toph/missionary/blink.png"
            with dissolve
            t "what is..."
            hide expression "bk3/toph/missionary/head_shock.png"
            hide expression "bk3/toph/missionary/blink.png"
            with dissolve
            t "what is it?"
            y "it's called...."
            show totm totm103
            t "ohhh... unnhh..."
            y "hard fucking!"
            t "unh!!"
            show ctc
            pause
            hide ctc
            "Toph squeezes you unintentionally with every thrust."
            y "fuck!"
            t "oh... hgh... aang..."
            y "Yeah, you like that, dont you?"
            show ctc
            pause
            hide ctc
            t "it's... ahh... ah... oh... fff... fu..."
            y "that's it! say it!"
            show totm totm104
            t "aahhh....!!"
            show ctc
            pause
            hide ctc
            y "say it!"
            t "fuu..."
            show totm totm105
            t "fuck!!!"
            show ctc
            pause
            hide ctc
            t "it's... *gasp...* so... ahh..."
            t "i'm... i feel so... i'm gonna..."
            show ctc
            pause
            hide ctc
            y "fuck...!"
            y "fuck, toph...!"
            y "your tight fucking cunt is gonna..."
            y "gonna make me...."

    show ctc
    pause
    hide ctc

    menu:
        "cum inside":
            ya "take my load, slut!"
            t "wait! no!"
            play sound "audio/splurt2.ogg"
            show totm totm06
            show expression "bk3/toph/missionary/head_shock.png"
            with flash
            ya "little whore!"
            play sound "audio/splurt3.ogg"
            with flash
            show ctc
            pause
            hide ctc
            t "hhgnh...."

            show totm totm07
            show expression "bk3/toph/missionary/blink.png"
            with flash
            show ctc
            pause
            hide ctc
            y "Aaaah... fuck. You're the best, Toph."
            y "Okay, I'll let myself out."
            t "I..."
            hide expression "bk3/toph/missionary/head_shock.png" with dissolve
            t "i don't think i'm..."
            t "...going to be able to walk tomorrow..."
            show ctc
            pause
            hide ctc
            scene black with dissolve
            "worn out, you head home for the night."
            jump bk3_next
        "cum outside":

            ya "take my load, slut!"
            t "wha-"
            play sound "audio/splurt2.ogg"
            show totm totm00
            show expression "bk3/toph/missionary/head_shock.png"
            show expression "bk3/toph/missionary/solodick.png"
            show expression "bk3/toph/missionary/spermshot.png"
            $ renpy.pause(0.3)
            hide expression "bk3/toph/missionary/spermshot.png"
            show expression "bk3/toph/missionary/spermout1.png"
            $ renpy.pause()
            ya "little whore!"
            show expression "bk3/toph/missionary/blink.png"
            play sound "audio/splurt3.ogg"
            show expression "bk3/toph/missionary/spermshot.png"
            $ renpy.pause(0.3)
            hide expression "bk3/toph/missionary/spermshot.png"
            show expression "bk3/toph/missionary/spermout2.png"
            $ renpy.pause()
            play sound "audio/splurt1.ogg"
            show expression "bk3/toph/missionary/spermshot.png"
            $ renpy.pause(0.3)
            hide expression "bk3/toph/missionary/spermshot.png"
            show expression "bk3/toph/missionary/spermout3.png"
            t "hhgnh...."
            show ctc
            pause
            hide ctc
            y "Aaaah... fuck. You're the best, Toph."
            y "Okay, I'll let myself out."
            t "I..."
            hide expression "bk3/toph/missionary/blink.png"
            with dissolve
            t "i don't think i'm..."
            hide expression "bk3/toph/missionary/head_shock.png" with dissolve
            t "...going to be able to walk tomorrow..."
            show ctc
            pause
            hide ctc
            scene black with dissolve
            "worn out, you head home for the night."
            jump bk3_next

label toph_sex2:
    $ toph_sex = True
    hide screen earth_money_date
    scene black
    scene bg_bk3_tophome_night
    show toi toi04
    with dissolve
    t "hey!"
    y "we're going to fuck tonight, toph."
    show toi toi09 with dissolve
    t "we... are?"
    y "that's right..."
    y "I'm tired of waiting."
    y "i think you want it, too."
    show toi_blink with dissolve
    t "i... i understand..."
    y "lay down."
    scene black with dissolve
    scene bg_toph_missionary
    show totm totm11
    with dissolve
    t "like... this, aang?"
    y "just like that."
    y "spread your legs."
    t "....."
    show totm totm00 with dissolve
    show ctc
    pause
    hide ctc
    y "damn, girl."
    y "it's time."
    y "ready?"
    t "i-"
    show totm totm01 with dissolve
    show ctc
    pause
    hide ctc
    t "uhh..."
    y "I'm right at your little entrance..."
    y "do you feel that?"
    t "y-yes, it's pushing into-"
    show totm totm02
    show totm_shock
    with dissolve
    t "aahhhh.... you're... you're slipping inside..."
    show ctc
    pause 
    hide ctc
    t "it's... it's going..."
    y "the head's almost in..."
    hide totm_shock with dissolve
    t "i can feel it ins-"
    show totm totm03
    show totm_shock
    with pflash
    t "hhhgh..."
    show ctc
    pause
    hide ctc
    t "ohh.... oh my god...."
    t "it's big... it's so b-"
    show totm totm04
    hide totm_shock
    with vshake
    t "ow!!"
    t "h-hey... ahhh...!"
    t "give... give me a second..."
    t "....."
    show totm totm03 with dissolve
    t "o...okay..."
    t "if you want, you can-"
    show totm totm102
    t "ow! nghh! ah!"
    t "eas... easy, aang!"
    show ctc
    pause
    hide ctc
    y "you want me to go easy on you?"
    t "y-yeah! ow! please!"
    y "okay, then."
    show totm totm101
    show expression "bk3/toph/missionary/blink.png"
    with dissolve
    t "ohh..."
    show ctc
    pause
    hide ctc
    y "how's that?"
    t "b-better..."
    y "a little easier?"
    y "not slamming your little cunt quite so forcefully?"
    t "thank... thank you, aang..."
    y "don't thank me yet."
    scene black
    show expression "bk3/toph/missionary/bg_toph_missionary1.jpg"

    show totm_cdick:
        ypos 20 xpos 477
        linear 1.0 ypos 120
        linear 1.0 ypos 20
        repeat

    show totm totm20
    with dissolve
    show ctc
    pause
    hide ctc
    y "i've been thinking..."
    t "...nnnhh... uhh...."
    y "you've had such a stressful time..."
    y "i think you need some sexual healing."
    t "sexual... ah... healing... nf...?"
    y "there's a very special technique..."
    t "ah... nh... wha...?"
    show ctc
    pause
    hide ctc
    menu:
        "choke a bitch":
            show expression "bk3/toph/missionary/chands.png":
                ypos -200
                linear 3.0 ypos -100
            $ renpy.pause(3, hard = True)

            show totm_cdick:
                ypos 20
                easein 2.0 ypos 120
                easeout 2.0 ypos 20
                repeat


            hide expression "bk3/toph/missionary/chands.png"
            show totm totm25 with vpunch

            t "hrk!"
            "You feel Toph tightening, making you go slower."
            show ctc
            pause
            hide ctc
            t "ghh...hgh...agh..."
            t "an...i...anh...eeth.."
            show expression "bk3/toph/missionary/cface_lewd.png"
            with dissolve

            y "Yeah, you like that, doncha?"
            show ctc
            pause
            hide ctc
            t "hhgh...hrk..."
            y "feeling lightheaded?"
            t "hgh...gh..."
            show totm totm20
            show expression "bk3/toph/missionary/chands_open.png"
            hide expression "bk3/toph/missionary/cface_lewd.png"
            with dissolve
            "You release your grip to allow her to gasp for air."
            show ctc
            pause
            hide ctc
            t "*pant* *pant*"
            t "i... i couldn't breathe..."
            t "but it did feel-"
            hide expression "bk3/toph/missionary/chands_open.png"
            show totm totm25 with vpunch
            t "gagh!"
            "you tighten your grip once more."
            show expression "bk3/toph/missionary/cface_lewd.png"
            with dissolve
            t "hnnnghhahh..."
            y "i can't believe how tight you are..."
            y "i'm struggle to pull out of you each time..."
            show ctc
            pause
            hide ctc
            y "fuck..."
            y "fuck, toph..."
            y "your tight fucking cunt is gonna..."
            y "gonna make me...."
            menu:
                "don't release your grip until you cum":
                    "you speed up despite the clamplike feeling of Toph's pussy."
                    show totm_cdick:
                        ypos 20
                        easein 0.5 ypos 120
                        easeout 0.5 ypos 20
                        repeat
                    t "ngh! hrk! gh!"
                    y "that's it, bitch!"
                    y "you're mine! you're my little fucking whore!"
                    y "say it!"
                    t "...hghh!"
                    y "say you're my fucking whore!"
                    t "ahh...uuugh...ohhh..."
                    y "yes! you little slut!"
                    y "You cock loving slut!"
                    y "i'm almost there!"
                    menu:
                        "cum inside":

                            y "let's give you a creampie!"
                            t "nngh! aohh!"
                            play sound "audio/splurt2.ogg"
                            show totm_cdick:
                                ypos 120
                            with flash
                            "You empty your balls inside of Toph."
                            show totm totm20

                            show totm_cdick:
                                ypos -100
                            show expression "bk3/toph/missionary/csperm_in.png"
                            with Dissolve(2.0)

                            y "Aaaah.. that was the best."
                            hide expression "bk3/toph/missionary/csperm_in.png"
                        "cum outside":


                            ya "little slut!"
                            t "ah! oo 'ant-"
                            hide totm_cdick
                            show totm_cdick:
                                ypos 100 xpos 480
                            "In one big explosion, you release every drop of sperm from your balls on Toph's face."
                            show expression "bk3/toph/mastur_kat/white.png"
                            show expression "bk3/toph/missionary/csperm_out.png"
                            hide expression "bk3/toph/mastur_kat/white.png" with Dissolve(2.0)
                            show totm totm20 with Dissolve(1.5)

                            y "Aaaah... fuck. You're the best, Toph."


                    hide totm_cdick
                    y "Okay, I'll let myself out."
                    t "I... i don't think i'm..."
                    t "...going to be able to walk tomorrow..."
                    scene black with dissolve
                    "worn out, you head home for the night."
                    jump bk3_next
                "let her breathe":

                    show totm totm20 with Dissolve(1)
                    hide expression "bk3/toph/missionary/cface_lewd.png" with Dissolve(1)
                    t "ahh... hhha..."
                    show ctc
                    pause
                    hide ctc
                    t "it... it does feel..."
                    t "i'm so... dizzy..."
                    show totm_cdick:
                        ypos 20
                        easein 0.5 ypos 120
                        easeout 0.5 ypos 20
                        repeat
                    show expression "bk3/toph/missionary/cface_lewd.png" with dissolve
                    "you speed up as you feel yourself approaching climax..."
                    t "hah... ah... yes..."
                    t "yes... aang..."
                    hide expression "bk3/toph/missionary/cface_lewd.png" with dissolve
                    t "give... give it to... ahn... m-me..."
                    menu:
                        "cum inside":
                            ya "ngh! fuck!"
                            ya "let's give you a creampie!"
                            show totm totm26 with vshake
                            t "wait! don't!"
                            y "slut!"
                            show totm totm27
                            t "no!!!"
                            play sound "audio/splurt2.ogg"
                            show totm_cdick:
                                ypos 120
                            with flash
                            "You empty your balls inside of Toph."
                            show totm totm20

                            show totm_cdick:
                                ypos -100
                            show expression "bk3/toph/missionary/csperm_in.png"
                            with Dissolve(2.0)
                            t "uunngh...."
                            y "Aaaah.. that was the best."
                            hide expression "bk3/toph/missionary/csperm_in.png"

                            hide totm_cdick
                            y "Okay, I'll let myself out."
                            t "I... i don't think i'm..."
                            t "...going to be able to walk tomorrow..."
                            show ctc
                            pause
                            hide ctc
                            scene black with dissolve
                            "worn out, you head home for the night."
                            jump bk3_next
                        "cum outside":

                            ya "little slut!"
                            show expression "bk3/toph/missionary/cface_lewd.png" with dissolve
                            t "wait, what are you-"
                            hide totm_cdick
                            show totm_cdick:
                                ypos 100 xpos 480
                            "In one big explosion, you release every drop of sperm from your balls on Toph's face."
                            play sound "audio/splurt2.ogg"
                            show expression "bk3/toph/mastur_kat/white.png"
                            show expression "bk3/toph/missionary/csperm_out.png"
                            $ renpy.pause(0.05)
                            hide expression "bk3/toph/missionary/cface_lewd.png"
                            hide expression "bk3/toph/mastur_kat/white.png"
                            with Dissolve(1.5)
                            show ctc
                            pause
                            hide ctc
                            show totm totm20 with Dissolve(1.5)

                            y "Aaaah... fuck. You're the best, Toph."
                            hide totm_cdick
                            y "Okay, I'll let myself out."
                            t "I... i don't think i'm..."
                            t "...going to be able to walk tomorrow..."
                            show ctc
                            pause
                            hide ctc
                            scene black with dissolve
                            "worn out, you head home for the night."
                            jump bk3_next
                        "first position":

                            scene black
                            show expression "bk3/toph/missionary/bg_toph_missionary.jpg"
                            show totm totm105
                            with dissolve
                            pass
        "first position":
            scene black
            show expression "bk3/toph/missionary/bg_toph_missionary.jpg"
            show totm totm101
            show expression "bk3/toph/missionary/head_shock.png"
            show expression "bk3/toph/missionary/blink.png"
            with dissolve
            t "what is..."
            hide expression "bk3/toph/missionary/head_shock.png"
            hide expression "bk3/toph/missionary/blink.png"
            with dissolve
            t "what is it?"
            y "it's called...."
            show totm totm103
            t "ohhh... unnhh..."
            y "hard fucking!"
            t "unh!!"
            show ctc
            pause
            hide ctc
            "Toph squeezes you unintentionally with every thrust."
            y "fuck!"
            t "oh... hgh... aang..."
            y "Yeah, you like that, dont you?"
            show ctc
            pause
            hide ctc
            t "it's... ahh... ah... oh... fff... fu..."
            y "that's it! say it!"
            show totm totm104
            t "aahhh....!!"
            show ctc
            pause
            hide ctc
            y "say it!"
            t "fuu..."
            show totm totm105
            t "fuck!!!"
            show ctc
            pause
            hide ctc
            t "it's... *gasp...* so... ahh..."
            t "i'm... i feel so... i'm gonna..."
            show ctc
            pause
            hide ctc
            y "fuck...!"
            y "fuck, toph...!"
            y "your tight fucking cunt is gonna..."
            y "gonna make me...."

    show ctc
    pause
    hide ctc

    menu:
        "cum inside":
            ya "take my load, slut!"
            t "wait! no!"
            play sound "audio/splurt2.ogg"
            show totm totm06
            show expression "bk3/toph/missionary/head_shock.png"
            with flash
            ya "little whore!"
            play sound "audio/splurt3.ogg"
            with flash
            show ctc
            pause
            hide ctc
            t "hhgnh...."

            show totm totm07
            show expression "bk3/toph/missionary/blink.png"
            with flash
            show ctc
            pause
            hide ctc
            y "Aaaah... fuck. You're the best, Toph."
            y "Okay, I'll let myself out."
            t "I..."
            hide expression "bk3/toph/missionary/head_shock.png" with dissolve
            t "i don't think i'm..."
            t "...going to be able to walk tomorrow..."
            show ctc
            pause
            hide ctc
            scene black with dissolve
            "worn out, you head home for the night."
            jump bk3_next
        "cum outside":

            ya "take my load, slut!"
            t "wha-"
            play sound "audio/splurt2.ogg"
            show totm totm00
            show expression "bk3/toph/missionary/head_shock.png"
            show expression "bk3/toph/missionary/solodick.png"
            show expression "bk3/toph/missionary/spermshot.png"
            $ renpy.pause(0.3)
            hide expression "bk3/toph/missionary/spermshot.png"
            show expression "bk3/toph/missionary/spermout1.png"
            $ renpy.pause()
            ya "little whore!"
            show expression "bk3/toph/missionary/blink.png"
            play sound "audio/splurt3.ogg"
            show expression "bk3/toph/missionary/spermshot.png"
            $ renpy.pause(0.3)
            hide expression "bk3/toph/missionary/spermshot.png"
            show expression "bk3/toph/missionary/spermout2.png"
            $ renpy.pause()
            play sound "audio/splurt1.ogg"
            show expression "bk3/toph/missionary/spermshot.png"
            $ renpy.pause(0.3)
            hide expression "bk3/toph/missionary/spermshot.png"
            show expression "bk3/toph/missionary/spermout3.png"
            t "hhgnh...."
            show ctc
            pause
            hide ctc
            y "Aaaah... fuck. You're the best, Toph."
            y "Okay, I'll let myself out."
            t "I..."
            hide expression "bk3/toph/missionary/blink.png"
            with dissolve
            t "i don't think i'm..."
            hide expression "bk3/toph/missionary/head_shock.png" with dissolve
            t "...going to be able to walk tomorrow..."
            show ctc
            pause
            hide ctc
            scene black with dissolve
            "worn out, you head home for the night."
            jump bk3_next

label toph_clean_fuck:
    "you knock on toph's door."
    t "who is it?"
    y "it's me."
    t "...that's true for everybody."
    y "oh. right. it's-"
    t "I'm just messing with you, twinkle toes."
    t "come on in."
    scene black with dissolve
    show bg_bk3_tophome_day
    show tub
    show tocl tocl09
    with dissolve
    t "hey, aang-"
    y "heh, nice. what's up girl. you looking to party?"
    show tocl_smile
    show tocl_blush
    with dissolve
    t "shut up, aang."
    t "you can hang out if you want, but i'm gonna keep bathing."
    y "i've got no problem with that."
    hide tocl_smile with dissolve
    t "um..."
    t "Okay."
    t "....."
    show tocl tocl107
    hide tocl_blush
    with dissolve
    t "so what did you need?"
    y "need?"
    y "uh..."
    menu:
        "some training":
            y "I was hoping we could do some training."
            y "I think my earthbending is really coming along."
            show tocl tocl100 with dissolve
            t "yeaahhh..."
            y "what?"
            y "is it... is it not?"
        "i'm looking for a cat... a pussycat.... ok, a vagina.":

            y "i was looking for a kitty."
            t "here?"
            y "well, i think i might see one."
            t "i can tell you there's no cat here."
            y "well, if you see a pussy around, you know, i'm here."
            t "...."
            show tocl tocl100 with dissolve
            t "you should focus on your training aang..."
            t "...because i think there is a pussy around here."
            y "hey!"

    y "i bet i could take you."
    show tocl tocl08
    show tocl_smile
    with dissolve
    t "don't make me laugh."
    t "i'd break you."
    y "come on. i'm the avatar!"
    y "you wouldn't stand a chance, really."
    hide tocl_smile with dissolve
    t "yeah? you wanna go right now?"
    y "....."
    y "(she's already kicked my ass more times than I'd like to count...)"
    y "not while you're naked..."
    y "let's reschedule."
    show tocl_smile with dissolve
    t "that's what i thought."
    y "still, i think i'm winning right now."
    hide tocl_smile with dissolve
    t "what do you mean?"
    y "well, you might be able to kick my ass..."
    y "but i'll have a hell of a view."
    show tocl_blush
    with dissolve
    t "oh... right..."
    show tocl tocl09 with dissolve
    t "umm-"
    y "seriously? you don't need to hide."
    y "it's cute you're embarassed though."
    show tocl tocl08
    show tocl_angry
    hide tocl_blush
    show tocl_blush
    with dissolve
    t "i'm not embarassed!"
    y "then why did you cover yourself?"
    t "....shut up!"
    hide tocl_angry
    hide tocl_blush
    show tocl tocl100
    with dissolve
    t "if you're just here to bug me..."
    t "you can just go."
    y "nah, i came to check you out."
    y "tell you i feel in need of some... afternoon encouragement."
    show tocl tocl101 with dissolve
    t "is that so?"
    y "yeah... you know you're my boo."
    t "i don't know what that means, but..."
    show tocl tocl102 with dissolve
    y "(damn!)"
    t "what did you have in mind?"
    y "well, i actually wanted to..."
    show tocl tocl107 with dissolve
    y "....."
    t "do what?"
    y "I wanted....."
    stop music
    play music "audio/Unwritten Return.mp3"
    show tocl tocl50 with dissolve
    y "....to get a closer look."
    t "at what?"
    t ".....oh."
    t "um... i not sure how comfortable i am-"
    y "don't worry, i just need a pretty view."
    y "(for starters...)"
    t "what... should i do?"
    y "well, why don't you rub yourself a little?"
    t "rub... myself?"
    y "sure. like you and katara did."
    t "oh, right..."
    show tocl tocl53 with dissolve
    t "like this?"
    y "well...."
    y "yeah...."
    y "but, actually move a little."
    show tocl tocl54 with dissolve
    t "there."
    t "i... i moved it."
    y "come on."
    show tocl tocl55 with dissolve
    t "{i}ahh...{/i}"
    y "(now we're talking!)"
    show tocl tocl53 with dissolve
    t "how... was that...?"
    y "great! now go up and down..."
    show tocl tocl104
    show ctc
    pause
    hide ctc
    t "{i}oohhh...{/i}"
    t "aang, it... ahh..."
    t "i don't know if i like... ahh... this..."
    y "but you're moaning..."
    t "not... mmm... on purpose..."
    y "open up."
    y "open your lips."
    show tocl tocl51 with dissolve
    t "........"
    t "............"
    show tocl tocl52 with dissolve
    show ctc
    pause
    hide ctc
    y "fucking gorgeous."
    t "th-thank you...."
    menu:
        "lick her pussy":
            y "(i need a fucking taste!)"
            y "put your hand down."
            show tocl tocl50 with dissolve
            t "why-"
            show tocl_tongue with dissolve
            t "oh!"
            show ctc
            pause
            hide ctc
            t "{i}oohhhhh...."
            hide tocl_tongue with dissolve
            t "w-why are you... stopping...?"
        "slap it with your cock":

            t "what are you... doing...?"

    "you swiftly take out your cock, an idea forming in your mind...."
    show tocl_pussyglow:
        alpha 0
        linear 4.0 alpha 0.8

    show tocl_dickslap
    t "oh!"
    show ctc
    pause
    hide ctc
    t "hnngh... ah..."
    t "my... ow... my kitty lips..."
    t "ah... ah... it's... good but... oww..."
    hide tocl_dickslap with dissolve
    show tocl tocl50
    y "your pussy's looking a little swollen..."
    t "you... just... beat it... ow..."
    t "i should kick your butt, twinkle-"
    show tocl_tongue
    show tocl_pussyglow:
        linear 4.0 alpha 0
    t "{i}oohhhhhh....."
    y "shhh.... relax..."
    hide tocl_pussyglow
    t "mmmh..."
    show ctc
    pause
    hide ctc
    t "{i}oohhh...."
    show tocl tocl52 with dissolve
    t "m...more...."
    show tocl_pussydrip with dissolve
    t "uuhh...."
    t "Keep... keep going... i'm... uhh...."
    hide tocl_tongue with dissolve
    t "wh... what are you doing?"
    hide tocl_pussydrip with dissolve
    t "don't... don't stop!"
    y "i've got something better for you."
    show tocl tocl59 with dissolve
    t "please... please i'm so close..."
    show tocl tocl60 with dissolve
    y "that's alright, i'm going to help you finish."
    t "yes, thank you, please, bring back your tongue-"
    y "not my tongue."
    t "huh?"
    show tocl tocl61 with dissolve
    t "hhgnhh...."
    t "aang... that's..."
    t "you're... slipping inside..."
    t "wai-"
    show tocl tocl62 with Dissolve(0.25)
    t "hngh...!"
    t "....fuck!"
    y "did you just swear?"
    t "it-it's.... fucking.... huge...."
    y "oh, we're not done yet."
    t "i can't take-"
    show tocl tocl63 with Dissolve(0.25)
    t "ah! fuck! aang!"
    t "hhhnnnh....."
    y "damn that's tight."
    y "and... it's really fucking hot inside you."
    t "*pant* *gasp* *pant*"
    y "how you feeling?"
    t "ahh... ah... ah...."
    y "oh, shoot... do you need me to take it out?"
    t "it's......"
    t "......."
    t "....yes...."
    t "i thought i could... it's stretching me inside...."
    y "okay, i'll just..."
    t "thank-"
    show tocl tocl64 with vshake
    t "aaahhh!!!!!"
    y "mmh..."
    t "fuck! fuck, aang!"
    y "what?"
    t "you... you {i}jerk{/i}!"
    t "it... ah... it... hnghh..."
    y "come on, you're enjoying it."
    t "take... ahh... take it... fuck!... out..."
    show tocl tocl61 with dissolve
    t "oh... fuck... thank fucking... ungh..."
    show tocl tocl105
    t "fuck!!"
    show ctc
    pause
    hide ctc
    y "it's cute how much you're swearing."
    y "I've barely heard you curse at all before."
    t "you! fucking! nnghhh....."
    t "...mmm...hhh...."
    y "aw, what's wrong, toph?"
    t "*mmmm....*"
    y "was that a moan?"
    t "n-no, you-"
    show tocl tocl106
    t "ahh!!"
    show ctc
    pause
    hide ctc
    y "damn you're squeezing my cock hard..."
    t "it's... ah... it's...."
    y "good?"
    t "n...no, you... ah... jerk..."
    y "come on..."
    t "n-no..."
    y "how does it feel?"
    t "it's... it's..."
    t "......"
    t "it's fucking amazing, aang! you asshole!"
    show tocl tocl106_2
    t "nngh...."
    t "f-fuck... fuck me...."
    y "what?"
    t "fuck me!"
    y "\"fuck me, master\"."
    t "n-no! you don't own me, aang!"
    y "well, you don't have to, but there might be punishments..."
    t "more *ungh* demeaning than *mmgh* this?"
    y "you love it."
    t "*ahh* yeah so *ugh* shut up and *ngh* fuck me!"
    y "\"master\"."
    t "no!"
    y "then i'll stop."
    t "i swear, aang, if i wasn't too *nghh* full to move, i'd-"
    y "say it."
    t "....."
    t "m... master! fuck me, master!"
    show tocl tocl106_1
    t "aangh!"
    show ctc
    pause
    hide ctc
    y "ngh! here it comes!"
    menu:
        "cum inside":
            play sound "audio/splurt2.ogg"
            show tocl tocl64
            with flash
            y "ngh!"
            t "huuuhhgh..."
            play sound "audio/splurt3.ogg"
            with flash
            t "ahhn...."
            play sound "audio/splurt2.ogg"
            with flash
            y "fuuuck..."
            show tocl tocl60
            show tocl_sperm4
            with dissolve
            show ctc
            pause
            hide ctc
            hide tocl_sperm4
        "cum outside":


            play sound "audio/splurt2.ogg"
            show tocl tocl60
            show tocl_spermshot
            $ renpy.pause (0.3)
            hide tocl_spermshot
            show tocl_sperm1
            y "ngh!"
            t "huuuhhgh..."
            play sound "audio/splurt3.ogg"
            show tocl_spermshot
            $ renpy.pause (0.3)
            hide tocl_spermshot
            show tocl_sperm2
            hide tocl_sperm1
            t "ahhn...."
            play sound "audio/splurt2.ogg"
            show tocl_spermshot
            $ renpy.pause (0.3)
            hide tocl_spermshot
            show tocl_sperm3
            hide tocl_sperm2
            y "fuuuck..."
            show ctc
            pause
            hide ctc
            hide tocl_sperm3

    show tocl tocl09
    show tocl_blush
    with dissolve
    t "well, i guess i need another bath..."
    y "good plan... slave."
    show tocl tocl08
    show tocl_angry
    hide tocl_blush
    with dissolve
    t "i am not your slave!"
    t "that was... that was just..."
    t "shut up!"
    y "you're cute when you're mad."
    show tocl_blush with dissolve
    t "i... you..."
    show tocl tocl102
    hide tocl_blush
    hide tocl_angry
    with dissolve
    t "whatever."
    y "i'll catch you later, toph."
    t "........."
    t "{size=-5}okay...."
    $ toph_clean_sex = True
    $ bk3_day = False
    jump bk3_village_background

label toph_katara_chair_sex:
    hide screen earth_money_date
    scene black
    scene bg_bk3_tophome_day

    show tokt tokt10 with dissolve
    t "oh, hey aang..."
    show ctc
    pause
    hide ctc
    y "Uhhh... what's going on here?"
    k3 "Me and Toph wanted to surprise you, but you're early."
    y "surprise me how..."
    k3 "Take the position Toph!"
    hide tokt tokt10 with Dissolve(1.3)


    show toch toch00 with Dissolve(1.3):
        ypos 110
    show ctc
    pause
    hide ctc
    y "i'm confused, but aroused."

    show toch toch01 with Dissolve(1.3):
        ypos 110
    t "*hnghh....*"
    y "whoa."
    show ctc
    pause
    hide ctc
    k3 "We decided to put a little show together for you."
    t "*{i}oohhh...{/i}*"
    t "i... i didn't get much say..."
    k3 "hush, toph."
    t "i can't see with my feet in the air..."
    k3 "look at my tits, aang!"
    k3 "look what i'm doing for you!"
    k3 "see!? i'm yours!"
    t "katara... i want you to... pay attention to me..."
    t "and this was partly my idea...."
    k3 "right... right... sorry..."
    y "katara, are you getting a little jealous?"
    k3 "no..."
    k3 "i just... i want you to trust me... and i... i don't want to be forgotten..."
    y "i promise that forgetting you is definitely not going to happen."
    t "guys... i'm still here..."
    t "let's do the thing, katara..."
    t "i... want it..."
    show toch toch01:
        linear 2.0 ypos 0

    show ctc
    pause
    hide ctc
    t "*{i}hhghh... oohhh...{/i}*"
    y "Did you really just shove a dildo in Toph's pussy and up your ass?"
    t "real...really deeeep, too...."
    y "how's your ass feeling, katara?"
    k3 "ti...tighter than i thought... but... this is for you, so..."
    k3 "do you... want to watch...?"

    show ctc
    pause
    hide ctc
    y "Hell yeah I wanna watch!"

    k3 "here... mmmh... we go!"

    show toch toch05 with Dissolve(1.2)

    hide toch toch01
    show toch toch100

    k3 "*nngh...* *ahh....*"
    t "{i}ohhhhhh...."
    t "ease....easy katara..."
    show ctc
    pause
    hide ctc
    y "That's fuckin hot."

    k3 "We call it \"the chair\"."
    t "{i}fuu... ahhh..."
    show ctc
    pause
    hide ctc
    k3 "It's difficult to do unless the other person is smaller."
    y "ah, so that's why toph's the \"chair\"."
    show toch toch01 with Dissolve(1.5)
    k3 "Are you enjoying it so far?"
    y "yeah, sure but..."
    menu:
        "don't overdo it":
            y "Slamming down on such a slender frame might be too much for her."
            k3 "Whatever you say, Aang."
            show toch toch100
        "slam her hard":
            y "Toph can take more than that."
            y "Put your weight into it, girl!"
            k3 "You heard him, Toph!"
            k3 "The gloves are coming off!"
            t "ohhh... unh... wait..."
            show toch toch101

    show ctc
    pause
    hide ctc

    k3 "hgh... fuck..."
    k3 "this is... really filling my fucking ass... ahh...."
    y "Fuck..."
    y "I'm about to cum just from watching you guys going at it!"
    y "Okay, which of you girls want to be my cum receptacle?"
    k3 "*ahh*... me!... *mmm*"
    t "small... *unngh*... girls need... *mmph*... love too...."
    menu:
        "katara":
            y "sorry Toph, Katara needs it more."
            show toch toch12 with Dissolve(1.5)
            menu:
                "cum inside her":
                    show toch toch13 with hpunch
                    hide toch toch13
                    show toch toch13
                    y "fuck!"
                    k3 "give it to me, aang!"
                    play sound "audio/splurt2.ogg"
                    show toch toch12
                    show expression "bk3/toph/chair_kat/sperm0.png"
                    with flash
                    $ renpy.pause()
                "cum on her pussy":

                    y "fuck!"
                    k3 "give it to me, aang!"
                    play sound "audio/splurt2.ogg"
                    show expression "bk3/toph/chair_kat/sperm1.png"
                    with flash
                    $ renpy.pause()
                    play sound "audio/splurt1.ogg"
                    show expression "bk3/toph/chair_kat/sperm2.png"
                    with flash
                    $ renpy.pause()
                    play sound "audio/splurt2.ogg"
                    show expression "bk3/toph/chair_kat/sperm3.png"
                    with flash
                    $ renpy.pause()
        "toph":


            y "sorry Katara, but Toph needs the nutrients."
            show toch toch10 with Dissolve(1.5)
            menu:
                "cum inside her":
                    show toch toch11 with hpunch
                    hide toch toch11
                    show toch toch11
                    y "fuck!"
                    t "give it to me, aang!"
                    play sound "audio/splurt2.ogg"
                    show toch toch10
                    show expression "bk3/toph/chair_kat/sperm0.png"
                    with flash
                    $ renpy.pause()
                "cum on her pussy":

                    y "fuck!"
                    t "give it to me, aang!"
                    play sound "audio/splurt2.ogg"
                    show expression "bk3/toph/chair_kat/sperm1.png"
                    with flash
                    $ renpy.pause()
                    play sound "audio/splurt1.ogg"
                    show expression "bk3/toph/chair_kat/sperm2.png"
                    with flash
                    $ renpy.pause()
                    play sound "audio/splurt2.ogg"
                    show expression "bk3/toph/chair_kat/sperm3.png"
                    with flash
                    $ renpy.pause()

    y "That was great girls."
    y "Thanks for the show."
    show ctc
    pause
    hide ctc
    scene black with dissolve
    "exhausted, you head home for the night."
    $ toph_katara_chair = 8
    $ bk3_day = False
    jump bk3_village_background

label toph_drinking:
    $ toph_drunk1 = True
    hide screen earth_money_date
    scene black
    scene bg_bk3_tophome_night
    show toi toi07
    with dissolve
    t "hey, aang!"
    y "you seem chipper!"
    t "because i am!"
    y "does that mean you're willing to go out and grab a couple drinks?"
    show toi toi09 with dissolve
    t "...."
    show toi toi07 with dissolve
    t "ah, what the hell!"
    t "let's do it!"
    t "where do you wanna go?"



    $ drunk_bar = 1
    y "how about the tavern?"
    t "awesome, i'll meet you there!"
    hide toi toi07 with dissolve
    y "i guess... she was eager to start."
    stop music
    play music "audio/Achaidh Cheide.mp3"   
    scene black
    scene inside_tavern_night
    with dissolve

















    $ toph_drunk = 'smile'

    y "now where is she...."
    t "heya!"
    show totd totd10 with dissolve
    t "s'bout time!"
    y "you got here fast."
    y "What are you drinking?"
    t "I have no idea, but it tastes like catpiss."
    if drunk_bar ==1:
        y "hmm... well, since I happen to own this spot..."
        y "try this, instead."
    if drunk_bar ==2:
        y "hmm... well, since I happen to know the owner of this spot..."
        y "try this, instead."
    show totd_pourwine
    "You pour Toph some of the more expensive stuff."
    hide totd_pourwine with dissolve
    show totd totd11 with dissolve
    y "How does it taste?"
    show totd totd10
    t "Not bad!"
    y " That's what I thought!"
    y " Here, let me fill you up again."
    show totd_pourwine
    t "I don't really..."
    t "...well I guess a little more won't hurt..."
    hide totd_pourwine with dissolve
    y "Bottoms up!"
    show totd totd11 with dissolve

    y "Wow you really don't hold back!"
    show totd totd10
    t "These glasses are too small!"
    t "Just give me the bottle."
    y "Just be sure to leave some for me."
    show expression "bk3/toph/drunk/bottle_xtra.png"
    t "Now that's more like it!"
    hide expression "bk3/toph/drunk/bottle_xtra.png" with dissolve

    show totd totd01

    y "Try to keep up with me if you can!"
    t "Hah! Don't think you can outdrink me!"

    show totd totd04
    y "Look at you go!"

    show totd totd01
    t "Pah! You've seen nothing yet!"
    show black with dissolve
    "10 minutes later...."

    show totd totd102
    hide black with dissolve

    $ renpy.pause(3, hard=True)
    show ctc
    pause
    hide ctc
    show totd totd01
    t "ah!"
    t "This is really good stuff!"
    show black with dissolve
    "Half an hour later...."
    hide black
    hide totd
    show totd totd03:
        parallel:
            linear 2.3 xpos 10
            linear 2 xpos 0
            repeat
        parallel:
            linear 2 ypos 5
            linear 2.3 ypos 0
            repeat
    show ctc
    pause
    hide ctc
    t "Isss... kinda hot in here isn't it?"
    t "le-lemme try somethin..."

    show totd totd05 with Dissolve(1.5)

    t "Aaaah, much... better!"
    t "*hick*"
    show ctc
    pause
    hide ctc
    t "Sss...soooo..."
    t "...I like your dick, man!!"
    $ toph_drunk = 'angry'
    t "When will my parents finally..."
    t "*hick*"
    t "...finally gonna..."
    t "gonna... treat me like an adult.."
    $ toph_drunk = 'sad'
    t "I wish I was taller..."


    show totd totd06
    show ctc
    pause
    hide ctc
    y "(she's bouncing all over the place...)"
    y "(hopefully this rolls back to happy-time drunk and away from throw-up drunk...)"

    show totd totd05
    t "*sniff...*"
    show ctc
    pause
    hide ctc
    "You hear cheering and turn your head to look at the commotion."
    hide totd with Dissolve(1.5)

    show totd_crowd
    show totd totd25:
        parallel:
            xpos 0
            linear 3.0 xpos 100
            linear 3.0 xpos -100
            linear 3.0 xpos 0
            repeat
        parallel:
            ypos 0
            linear 0.5 ypos 10
            linear 0.5 ypos 0
            repeat
    with dissolve
    "A highly intoxicated Suki is shaking her tits while walking up and down."
    show ctc
    pause
    hide ctc
    "A small crowd has formed around her."
    show totd totd26
    suki "Oh..."
    suki "*hick*"
    suki "...hey Aang!"
    suki "Do you you come here, too?"
    y "Girl, I come everywhere!"
    if drunk_bar ==1:
        y "(Damn, June is selling some potent stuff!)"
        y "(i hope i'm making a profit on this...)"
        y "(i swear if she's just giving it away...)"
    if drunk_bar ==2:
        y "(damn, iroh is selling some potent stuff!)"
        y "(i wonder if he's making a profit on this...)"
        y "(he's probably just giving it away to see tits...)"
    show totd totd25
    suki "Look at my titties!"
    if drunk_bar ==2:
        y "(yup.)"
    suki "Aren't they wonderful!?"
    y " \"wonderful\"? Have you been talking with Joo Dee?"
    suki "what?"
    y "it's just that she says it all the time and- nevermind."
    "You turn your attention back to Toph."

    hide totd_crowd
    hide totd
    with Dissolve(1.5)


    show totd totd100:
        parallel:
            linear 2.3 xpos 10
            linear 2 xpos 0
            repeat
        parallel:
            linear 2 ypos 5
            linear 2.3 ypos 0
            repeat
    with dissolve

    $ toph_drunk = 'angry'
    t "That stupid cow!"
    t "She thinks she's special just because of some stoopit tits?"
    t "I'll show what a..."
    t "*hick*"
    t "...what a real woman can doo..."
    t "Hold my bottle, Aang!!"
    hide totd
    show totd totd101:
        linear 3 xpos 5
        easeout 3.3 xpos -5
        repeat
    with Dissolve(1.5)
    t "Lalalalla..."
    t "*hick*"
    t "...lalaallaa...."
    t "Imma superstar!!"
    t "lalallaaa..."
    menu:
        "Watch Toph":
            y "You're the most sexy of 'em all Toph!"
            y "Now come down from there before you break something."
            hide totd totd101 with dissolve
            show totd totd100 with dissolve
            t "Se... seee!"
            t "I'm twice the woman she is!"
            hide totd
            show totd totd05:
                ypos 0
                linear 2 ypos 5
                linear 2.3 ypos 0
                repeat
            t "I... I know what ya want Aang!"
            y "You do?"
            t "Yeaah!!!"
            t "You..."
            t "*hick*"
            t "you want to stick your dick in my pooper!!"
            y "I don't think I'd phrase it like that..."
            y "but yeah, sure, when given the opportunity I'd absolutely do that."
            t "Well... you can't!!"
            t "That's foooor pooping!"
            t "Not for dicks!"
            t "You dick!!"
            y "...i feel like you're projecting."
            y "i literally have not even mentioned it."
            y "i think."
            t "But...butt maybe maybe if you ask me nicely..."
            y "oh?"
            t "I'm tired..."
            t "I'm just..."
            t "...just gonna close my eyes for a second..."
            y "nonono, wait-"
            hide totd
            show totd totd00 with hpunch
            y "......"
            y "...sure."
        "Watch Suki":


            hide totd with dissolve
            show totd_crowd
            show totd totd25:
                parallel:
                    xpos 0
                    linear 3.0 xpos 100
                    linear 3.0 xpos -100
                    linear 3.0 xpos 0
                    repeat
                parallel:
                    ypos 0
                    linear 0.5 ypos 10
                    linear 0.5 ypos 0
                    repeat
            y "Shake'em girl!"

            show totd
            show totd_crowd
            with hpunch

            "Suddenly you hear a crash behind you."
            hide totd
            hide totd_crowd
            show totd totd00
            with dissolve
            y "Oh shit..."
            y "Are you okay Toph?"
            t "unghh... you just.. butts..."
            y "....what?"
            t "you wan' ma bu... duncha...?"
            y "do i... want your butt? um, i mean, yeah."
            t "can... can't have it..."
            t "for... poops!"
            t "but... curi... curious... maybe..."
            t "ask... ask nice..."
            y "are you saying that you want anal, but i have to ask-"

    t "*SNOOOORRRE*"
    y "Oh man... she's out cold."

    menu:
        "do nothing":
            pass
        "lick Toph":
            y "hmmmm....."
            show totd totd35 with dissolve
            y "it seems a shame not to have a taste..."
            show totd totd36 with Dissolve(1.5)
            y "just relax...."
            t "hnghaba..."
            show totd totd37 with Dissolve(1.5)
            y "*slick*"
            y "mmmm...."
            t "ahn... ahh... gahn..."
            show ctc
            pause
            hide ctc
            "you pass your tongue up and down her parted lips..."
            "with suki distracting the rest of the drunk patrons, you take your time."
            "her sweet, unresisting pussy leaks onto your tongue as you take your fill."
            show ctc
            pause
            hide ctc
            show totd totd38 with Dissolve(1.5)
            y "i think that's enough."
            t "higah..."
            show totd totd35 with Dissolve(3.5)
            "you wait a moment for her drenched cunt to finish leaking onto the table."


    show totd totd00

    menu:
        "Go back to watching Suki":
            hide totd
            show totd_crowd
            show totd totd25:
                parallel:
                    xpos 0
                    linear 3.0 xpos 100
                    linear 3.0 xpos -100
                    linear 3.0 xpos 0
                    repeat
                parallel:
                    ypos 0
                    linear 0.5 ypos 10
                    linear 0.5 ypos 0
                    repeat

            "accompanied by the snoring of Toph, you watch Suki until you yourself black out."
            scene black with Dissolve(2.0)


            show expression "ebackgrounds/inside_tavern_day.jpg"
            show totd totd00
            with Dissolve(1.5)
            t "Oooh...my head. Where am I?"
            y "Mornin' Toph."
            show totd totd07 with dissolve
            t "What happened!!?"
            y "I think we got a little tipsy."
            y "I vaguely remember you dancing on the table."
            t "Oh shit, oh shit, oh shit!"
            hide totd with vshake
            "Quickly dressing herself she runs out of the door."

            y "you took... the bottle, though..."
        "Take Toph home":

            scene black with Dissolve(2.0)
            y "June, take care of Suki!"
            y "I'm taking this lightweight home."
            "You throw Toph over your shoulder and walk to her home."
            "dropping her inside, you stumble home yourself."

    jump bk3_next


label jin_sex1:
    hide screen earth_money_date
    scene black with Dissolve(1)
    show expression "bk3/skye/sex/brothel_skyeroom.jpg"
    with Dissolve(1)
    $ tojp_jinhead = 'none'
    if not jin_fucked:
        jin "finally!"
        jin "I'm so happy you want to do this, Lee..."
        jin "You're very good at this whole playing-hard-to-get thing!"
        y "trust me, this was anything but easy."
    jin "Just take your clothes off and lie down here."
    jin "Let me take care of everything."
    show tojp tojp11 with Dissolve(1.5)
    if not jin_fucked:
        y "Can do!"
    show tojp tojp15 with Dissolve(1.5)
    show ctc
    pause
    hide ctc
    "jin rests her big tits on your legs..."
    "the girl watches your dick so intently you doubt even an earthquake could break her concentration."

    jin "It looks so stiff... and red."
    jin "It's almost as if it's angry."
    y "Here... take a whiff of it."
    show tojp tojp16 with dissolve
    $ tojp_jinhead = 'blink'
    jin "*Sniff* *sniff*"
    jin "Hmmmm.... it has such an overwhelming smell."
    y "You might as well taste it too."
    $ tojp_jinhead = 'none'
    jin "i know what i want, lee."
    jin "don't worry, there's no need to rush."
    $ tojp_jinhead = 'blink'
    jin "mmmmmm....."
    jin "okay..."
    $ tojp_jinhead = 'none'
    show tojp tojp17 with dissolve
    y "Ah, yes... just like that."
    show tojp tojp18
    jin "*sluuurp*"
    $ tojp_jinhead = 'blink'
    show tojp tojp19
    y "damn, girl! That feels great!"
    show tojp tojp16
    jin "I'm so happy you say that."
    $ tojp_jinhead = 'none'
    jin "i really... really am."
    $ tojp_jinhead = 'blink'

    show tojp tojp103
    show ctc
    pause
    hide ctc
    jin "*slurp* *gnk* *slurp*"
    y "oh... daamn..."
    y "That's.... really good..."
    jin "*gulp* *smk* *sluurp*"
    show ctc
    pause
    hide ctc
    y "it's almost like you had a lot of practice..."

    show tojp tojp16 with Dissolve(1.5)
    $ tojp_jinhead = 'front'
    jin "I practiced using a dildo just for you."
    y "That's really considerate of you."
    jin "I've also done other sorts of studying, you know...."

    menu:
        "Oh, like what?":
            pass
            "She turns around and swings her leg over you..."
            "giving you a full view of her ass and pussy."
        "first, suck my dick some more":
            show tojp tojp103
            y "Hhhhnnn, that's great, keep focusing on the head."
            $ tojp_jinhead = 'none'
            "After sucking on your dick for another few minutes..."
            "she takes it out of her mouth with a 'plop' sound and turns around."
            show tojp tojp17

    $ tojp_jinhead = 'none'
    show tojp tojp12 with Dissolve(1.5)
    jin "I saw this position in a pornlove magazine."
    jin "I just read them to educate myself on the possibilities, though!"
    y "Hey, I don't mind."
    y "I know all about the alure of pornmags."
    jin "Anyway, I thought you might like this particular position."
    y "I'm certainly enjoying the view."
    jin "Press your penis against my pussy and I'll slowly back up."
    show tojp tojp13 with dissolve
    y "here you go, slut!"
    jin "mmmm..."
    show tojp tojp03
    jin "ah!"
    $ tojp_jinhead = 'lusty'

    show tojp tojp02
    jin "aaah!"
    jin "lee... your... your penis is so pushy..."
    y "...\"pushy\"?"
    jin "it's... pushing me apart... inside."
    jin "I don't know how else to... ah... say it..."
    show tojp tojp01 with vshake
    jin "ungh!"
    $ tojp_jinhead = 'blink'
    jin "That's as deep as I can go."
    $ tojp_jinhead = 'none'
    jin "Do you like this Lee?"
    jin "Do you like having a full view of your dick being eaten by my pussy?"
    show ctc
    pause
    hide ctc
    y "I. fucken. love. it."
    y "Only pure willpower is stopping me from filling you up right this instant."
    jin "I'm going to start moving again. Ready?"
    y "Ready like spaghetti, baby!"
    jin "...."
    y "......"
    y "do you still like me?"
    jin "......"
    jin "yes."
    jin "but it's close."
    y "i'll take it."
    y "now, move that luscious booty up and down for me!"
    show tojp tojp102
    show ctc
    pause
    hide ctc
    jin "Do you want me to make longer strokes?"

    y "absolutely, stroke from the top to the bottom baby!"
    jin "you suuuure....?"
    show ctc
    pause
    hide ctc
    y "do it!"
    show tojp tojp100
    y "unghh..."
    jin "It's like your dick is kissing my womb!"
    show ctc
    pause
    hide ctc
    jin "Look at me, Lee!"
    jin "Look at my big round ass... gobbling up your hard cock!"
    show ctc
    pause
    hide ctc
    $ tojp_jinhead = 'blink'
    jin "watch it disappear... deep... ah... inside me... and come out glistening!"
    y "Slam that pretty pussy down hard on me girl!"
    y "I can take it!"
    $ tojp_jinhead = 'none'

    jin "You certain!?"
    show ctc
    pause
    hide ctc
    y "Hell yeah!"
    y "Fuck my dick as hard as you can!"
    jin "Don't forget you asked for it!"
    $ tojp_jinhead = 'blink'

    show tojp tojp101
    $ tojp_jinhead = 'lusty'
    jin "oohhh!"
    jin "I... my..."
    jin "mind is feeling all fluffy!"
    show ctc
    pause
    hide ctc
    jin "yes... yes..."
    jin "wreck my pussy and break me!"
    ya "I'm gonna cum!"


    jin "Oo...okay..."

    menu:
        "cum inside":
            y "I'm gonna drown your uterus!"
            jin "Do it!"
            jin "Flood my innards with your sperm!"
            hide tojp
            show tojp tojp01
            y "hngh!"
            jin "ahh...!"
            play sound "audio/splurt2.ogg"
            with flash
            show tojp tojp02
            $ renpy.pause(0.3)
            show tojp tojp03
            $ renpy.pause(0.3)
            show tojp tojp12
            show expression "bk3/jin/fuck/cum_inside.png"
            $ tojp_jinhead = 'blink'
            jin "There's so much of it...I feel like a human faucet..."
            $ tojp_jinhead = 'none'
            jin "thank you."
        "cum on her ass":

            y "I'm gonna blow my load all over your ass!"
            jin "Do it! Paint my ass white with your sperm!"
            hide tojp
            show tojp tojp13
            y "Hnnnnngn!"
            play sound "audio/splurt2.ogg"
            show expression "bk3/jin/fuck/cumshot.png"
            $ renpy.pause(0.3)
            hide expression "bk3/jin/fuck/cumshot.png"
            show expression "bk3/jin/fuck/cum_outside1.png"
            jin "yes! yes! cum, lee!"
            play sound "audio/splurt3.ogg"
            show expression "bk3/jin/fuck/cumshot.png"
            $ renpy.pause(0.3)
            hide expression "bk3/jin/fuck/cumshot.png"
            show expression "bk3/jin/fuck/cum_outside2.png"
            jin "cum all over my tight little ass!"
            play sound "audio/splurt2.ogg"
            show expression "bk3/jin/fuck/cumshot.png"
            $ renpy.pause(0.3)
            hide expression "bk3/jin/fuck/cumshot.png"
            show expression "bk3/jin/fuck/cum_outside3.png"
            y "bitch!"
            jin "yes, baby! yes, lee!"
            jin "I'm your bitch!"
            play sound "audio/splurt1.ogg"
            hide expression "bk3/jin/fuck/cum_outside1.png"
            hide expression "bk3/jin/fuck/cum_outside2.png"
            $ tojp_jinhead = 'blink'
            jin "Oohhh...."
            jin "......."
            jin "fuck, that was great!"
            $ tojp_jinhead = 'none'
            jin "thank you."

    show ctc
    pause
    hide ctc
    scene black with dissolve
    "you fall asleep right there in your bed."
    $ jin_fucked = True
    jump bk3_next


label jin_sex2:
    hide screen earth_money_date
    scene black with Dissolve(1)
    show expression "bk3/skye/sex/brothel_skyeroom.jpg"
    with Dissolve(1)
    $ tojp_jinhead = 'none'
    jin "Just take your clothes off and lie down here."
    jin "Let me take care of everything."
    show tojp tojp11 with Dissolve(1.5)
    if not jin_fucked:
        y "Can do!"
    show tojp tojp15 with Dissolve(1.5)
    show ctc
    pause
    hide ctc
    "jin rests her big tits on your legs..."
    jin "mmmm...."
    show tojp tojp16 with dissolve
    $ tojp_jinhead = 'blink'
    jin "*Sniff* *sniff*"
    jin "smells soo... goood...."
    $ tojp_jinhead = 'none'
    jin "I need it... in my mouth..."
    show tojp tojp17 with dissolve
    y "Ah, yes... just like that."
    show tojp tojp18
    jin "*sluuurp*"
    $ tojp_jinhead = 'blink'
    show tojp tojp19
    y "damn, girl! That feels great!"
    show tojp tojp16
    jin "I'm so happy you say that."
    $ tojp_jinhead = 'none'
    jin "i really... really am."
    $ tojp_jinhead = 'blink'

    show tojp tojp103
    show ctc
    pause
    hide ctc
    jin "*slurp* *gnk* *slurp*"
    y "oh... daamn..."
    y "That's.... really good..."
    jin "*gulp* *smk* *sluurp*"
    show ctc
    pause
    hide ctc
    $ tojp_jinhead = 'none'
    jin "so... why are you really here?"
    y "what?"
    jin "are you here to wreck my pussy and leave me broken?"
    jin "full of semen?"
    jin "useless for everything except a place to dump your cum?"
    jin "like a good lover should be?"
    jin "do you need to empty your balls, love?"
    jin "that's what i'm for, you know."

    show tojp tojp16 with Dissolve(1.5)
    $ tojp_jinhead = 'front'
    jin "see this pussy?"
    jin "that's what {i}it{/i} is for."

    menu:
        "let's fuck":
            pass
            "She turns around and swings her leg over you..."
            "giving you a full view of her ass and pussy."
        "first, suck my dick some more":
            show tojp tojp103
            y "Hhhhnnn, that's great, keep focusing on the head."
            $ tojp_jinhead = 'none'
            "After sucking on your dick for another few minutes..."
            "she takes it out of her mouth with a 'plop' sound and turns around."
            show tojp tojp17

    $ tojp_jinhead = 'none'
    show tojp tojp12 with Dissolve(1.5)
    jin "I can't wait...."
    jin "i need it!"
    jin "push your cock against my pussy and I'll back onto it."
    show tojp tojp13 with dissolve
    y "here you go, slut!"
    jin "mmmm..."
    show tojp tojp03
    jin "ah!"
    $ tojp_jinhead = 'lusty'

    show tojp tojp02
    jin "aaah!"
    jin "lee... your... your penis is so goood...."
    jin "it's... pushing me apart... inside."
    show tojp tojp01 with vshake
    jin "ungh!"
    $ tojp_jinhead = 'blink'
    jin "That's as deep as I can go."
    $ tojp_jinhead = 'none'
    jin "Do you like this Lee?"
    jin "Do you like having a full view of your dick being swallowed by my pussy?"
    show ctc
    pause
    hide ctc
    y "I. fucken. love. it."
    y "Only pure willpower is stopping me from filling you up right this instant."
    jin "I'm going to start moving again. Ready?"
    y "Ready spaghetti, baby!"
    jin "...."
    y "......"
    y "do you still like me?"
    jin "......"
    jin "yes."
    jin "but it's close."
    y "i'll take it."
    y "now, move that luscious booty up and down for me!"
    show tojp tojp102
    show ctc
    pause
    hide ctc
    jin "Do you want me to make longer strokes?"

    y "absolutely, stroke from the top to the bottom baby!"
    jin "you suuuure....?"
    show ctc
    pause
    hide ctc
    y "do it!"
    show tojp tojp100
    y "unghh..."
    jin "It's like your dick is kissing my womb!"
    show ctc
    pause
    hide ctc
    jin "Look at me, Lee!"
    jin "Look at my big round ass... gobbling up your hard cock!"
    show ctc
    pause
    hide ctc
    $ tojp_jinhead = 'blink'
    jin "watch it disappear... deep... ah... inside me... and come out glistening!"
    y "Slam that pretty pussy down hard on me girl!"
    y "I can take it!"
    $ tojp_jinhead = 'none'

    jin "You certain!?"
    show ctc
    pause
    hide ctc
    y "Hell yeah!"
    y "Fuck my dick as hard as you can!"
    jin "Don't forget you asked for it!"
    $ tojp_jinhead = 'blink'

    show tojp tojp101
    $ tojp_jinhead = 'lusty'
    jin "oohhh!"
    jin "I... my..."
    jin "mind is feeling all fluffy!"
    show ctc
    pause
    hide ctc
    jin "yes... yes..."
    jin "wreck my pussy and break me!"
    ya "I'm gonna cum!"


    jin "i love you so much!"
    jin "so i have to fuck you!"
    jin "how can i show you love unless you're pumping me full?"
    jin "pump me full, lee!"
    jin "empty your fat fucking cock in me!"

    menu:
        "cum inside":
            y "I'm gonna drown your uterus!"
            jin "Do it!"
            jin "Flood my innards with your sperm!"
            hide tojp
            show tojp tojp01
            y "hngh!"
            jin "ahh...!"
            play sound "audio/splurt2.ogg"
            with flash
            show tojp tojp02
            $ renpy.pause(0.3)
            show tojp tojp03
            $ renpy.pause(0.3)
            show tojp tojp12
            show expression "bk3/jin/fuck/cum_inside.png"
            $ tojp_jinhead = 'blink'
            jin "There's so much of it...I feel like a human faucet..."
            $ tojp_jinhead = 'none'
            jin "thank you."
        "cum on her ass":

            y "I'm gonna blow my load all over your ass!"
            jin "Do it! Paint my ass white with your sperm!"
            hide tojp
            show tojp tojp13
            y "Hnnnnngn!"
            play sound "audio/splurt2.ogg"
            show expression "bk3/jin/fuck/cumshot.png"
            $ renpy.pause(0.3)
            hide expression "bk3/jin/fuck/cumshot.png"
            show expression "bk3/jin/fuck/cum_outside1.png"
            jin "yes! yes! cum, lee!"
            play sound "audio/splurt3.ogg"
            show expression "bk3/jin/fuck/cumshot.png"
            $ renpy.pause(0.3)
            hide expression "bk3/jin/fuck/cumshot.png"
            show expression "bk3/jin/fuck/cum_outside2.png"
            jin "cum all over my tight little ass!"
            play sound "audio/splurt2.ogg"
            show expression "bk3/jin/fuck/cumshot.png"
            $ renpy.pause(0.3)
            hide expression "bk3/jin/fuck/cumshot.png"
            show expression "bk3/jin/fuck/cum_outside3.png"
            y "bitch!"
            jin "yes, baby! yes, lee!"
            jin "I'm your bitch!"
            play sound "audio/splurt1.ogg"
            hide expression "bk3/jin/fuck/cum_outside1.png"
            hide expression "bk3/jin/fuck/cum_outside2.png"
            $ tojp_jinhead = 'blink'
            jin "Oohhh...."
            jin "......."
            jin "fuck, that was great!"
            $ tojp_jinhead = 'none'
            jin "thank you."

    show ctc
    pause
    hide ctc
    scene black with dissolve
    "you fall asleep right there in your bed."
    $ jin_fucked = True
    jump bk3_next

label jin_sex3:
    hide screen earth_money_date
    scene black with Dissolve(1)
    show expression "bk3/skye/sex/brothel_skyeroom.jpg"
    with Dissolve(1)
    $ tojp_jinhead = 'none'
    jin "you need to empty your balls, love."
    jin "that's what i'm for, you know."
    jin "Just take your clothes off and lie down here."
    jin "Let me take care of everything."
    show tojp tojp11 with Dissolve(1.5)
    if not jin_fucked:
        y "Can do!"
    show tojp tojp15 with Dissolve(1.5)
    show ctc
    pause
    hide ctc
    "jin rests her big tits on your legs..."
    jin "mmmm...."
    show tojp tojp16 with dissolve
    $ tojp_jinhead = 'blink'
    jin "*Sniff* *sniff*"
    jin "smells soo... goood...."
    $ tojp_jinhead = 'none'
    jin "I need it... in my mouth..."
    show tojp tojp17 with dissolve
    y "Ah, yes... just like that."
    show tojp tojp18
    jin "*sluuurp*"
    $ tojp_jinhead = 'blink'
    show tojp tojp19
    y "damn, girl! That feels great!"
    show tojp tojp16
    jin "I'm so happy you say that."
    $ tojp_jinhead = 'none'
    jin "i really... really am."
    $ tojp_jinhead = 'blink'

    show tojp tojp103
    show ctc
    pause
    hide ctc
    jin "*slurp* *gnk* *slurp*"
    y "oh... daamn..."
    y "That's.... really good..."
    jin "*gulp* *smk* *sluurp*"
    show ctc
    pause
    hide ctc

    show tojp tojp16 with Dissolve(1.5)
    $ tojp_jinhead = 'front'
    jin "see this pussy?"
    jin "it's here so you have a place to put your cum."
    jin "so i'm going to suck you off until you're close..."
    jin "and you can just finish in my little cunt!"
    jin "does that sound like fun?"

    menu:
        "let's fuck":
            y "just fuck me!"
            jin "nope!"
            jin "I want to keep sucking."
            show tojp tojp103
            show ctc
            pause
            hide ctc
            $ tojp_jinhead = 'none'
            y "fuck..."
        "first, suck my dick some more":
            show tojp tojp103
            y "Hhhhnnn, that's great, keep focusing on the head."
            show ctc
            pause
            hide ctc
            $ tojp_jinhead = 'none'

    jin "that's it... i fill your balls tightening..."
    jin "you're getting big in my mouth, love..."
    show ctc
    pause
    hide ctc
    jin "i.... fuck... i want your cock in me..."
    jin "i've changed my mind..."
    y "no... no, you're right."
    jin "what?"
    y "i want you to get none of the pleasure of sex."
    y "you're just a place to empy my seed."
    y "so blow me and take my load in your cunt when i tell you to."
    jin "i.... yes... you're right."
    jin "thank you!"
    jin "thank you so much!"
    show tojp tojp103_1
    jin "slurrp... gulp..."
    show ctc
    pause
    hide ctc
    y "oh, fuck!"
    y "i'm... i'm gonna... gonna cum..."
    $ tojp_jinhead = 'none'
    show tojp tojp12 with Dissolve(1.5)
    jin "fill my useless cunt with cum, baby!"
    jin "i need it!"
    $ tojp_jinhead = 'lusty'
    show tojp tojp01 with vshake
    jin "ungh!"
    y "here it comes!"

    show tojp tojp101_1

    jin "give it!"
    jin "give it, give it!"
    menu:
        "cum inside":
            y "I'm gonna drown your uterus!"
            jin "Flood me with your sperm!"
            y "hngh!"
            jin "ahh...!"
            play sound "audio/splurt2.ogg"
            with flash
            jin "don't stop!"
            y "shit!"
            play sound "audio/splurt2.ogg"
            hide tojp
            show tojp tojp01
            with flash
            jin "ahh... ah... fill... so... hot..."
            play sound "audio/splurt2.ogg"
            with flash

            show tojp tojp12
            show expression "bk3/jin/fuck/cum_inside.png"
            $ tojp_jinhead = 'blink'
            jin "There's so much of it...I feel like a human faucet..."
            $ tojp_jinhead = 'none'
            jin "thank you."
        "cum on her ass":

            y "I'm gonna blow my load all over your ass!"
            jin "no! put it in me!"
            hide tojp
            show tojp tojp13
            y "Hnnnnngn!"
            play sound "audio/splurt2.ogg"
            show expression "bk3/jin/fuck/cumshot.png"
            $ renpy.pause(0.3)
            hide expression "bk3/jin/fuck/cumshot.png"
            show expression "bk3/jin/fuck/cum_outside1.png"
            jin "yes! yes! cum, lee!"
            play sound "audio/splurt3.ogg"
            show expression "bk3/jin/fuck/cumshot.png"
            $ renpy.pause(0.3)
            hide expression "bk3/jin/fuck/cumshot.png"
            show expression "bk3/jin/fuck/cum_outside2.png"
            jin "cum all over my tight little ass!"
            play sound "audio/splurt2.ogg"
            show expression "bk3/jin/fuck/cumshot.png"
            $ renpy.pause(0.3)
            hide expression "bk3/jin/fuck/cumshot.png"
            show expression "bk3/jin/fuck/cum_outside3.png"
            y "bitch!"
            jin "yes! I'm your bitch!"
            play sound "audio/splurt1.ogg"
            hide expression "bk3/jin/fuck/cum_outside1.png"
            hide expression "bk3/jin/fuck/cum_outside2.png"
            $ tojp_jinhead = 'blink'
            jin "Oohhh...."
            jin "......."
            jin "fuck, that was great!"
            $ tojp_jinhead = 'none'
            jin "but i wish you'd cum inside me..."

    show ctc
    pause
    hide ctc
    scene black with dissolve
    "you fall asleep right there in your bed."
    $ jin_fucked = True
    jump bk3_next

label tophmomfuck:
    mv "Helloooo?"
    t "I recognize that voice! It's my mom!"
    y "I got an idea. Go hide until I call you."
    show expression "ebackgrounds/bg_bk3_tophome_0.jpg"
    show tomf tomf00
    with dissolve
    pop "Avatar, I've heard my daughter was travelling with you."
    pop "Is she here?"
    y "I'm not really sure she wants to talk to you as long as you still treat her like a kid."
    pop "But she's such a small tender girl! It's a dangerous world and..."
    y "I'm starting to see Toph's point..."
    y "Okay, let's make a deal."
    pop "The Bei Fong family is very wealthy."
    pop "we can give you whatever you desire if you help us."
    y "Mmmm... money is nice, but I want something else."
    y "Something only you personally can give me."
    pop "Anything to be able to see my little girl again!"
    y "Heh."
    y "Okay..."
    y "I want to fuck you."
    y "Right here, right now."
    pop "...e-excuse me..."
    pop "I must have misheard you?"
    y "Nah.. you've heard me right."
    y "If I get to pound your pussy, you and your daughter will be in each others arms within the hour."
    pop "....."
    y "You can be reunited with your daughter, and all it takes is spreading those legs of yours."
    y "I promise I'll keep it a secret."
    y "No one outside of these walls will ever know."
    pop "....how can I... be certain you speak the truth?"
    y "You'll have to trust me... or not. Your call. Yes or no? "
    pop "... you... I.... okay..."
    pop "But I warn you. If this is some sort of trick....."
    y "Yeah, yeah."
    y "Take off those clothes and lie down there."
    show tomf tomf01 with Dissolve(1.5)
    pop "please make this quick."
    show ctc
    pause
    hide ctc
    y "Lift your leg up."
    show tomf tomf02 with dissolve
    y "Oh yeah, gonna fuck me some high class rich lady pussy!"
    show ctc
    pause
    hide ctc
    y "I see Toph inherited the size of her boobs from you..."
    show expression "bk3/toph/momfuck/fuck1.png" with dissolve
    y "You're looking wet..."
    y "Are you actually looking forward to this?"
    y "I bet daddy bei fong doesn't give you what you need, am i right?"
    pop "Nonsense. Can we please get this over with?"
    y "Certainly."
    y "...if you call me daddy."
    pop "you... i... i am a grown married woman!"
    y "and?"
    pop "....please come here... daddy."
    y "fantastic."
    hide expression "bk3/toph/momfuck/fuck1.png"
    show tomf_fuckmom
    y "Oh wow, no problems getting in whatsoever."
    show ctc
    pause
    hide ctc
    y "You're wet as fuck!"
    y "Do you get this wet when your husband wants to fuck you too?"
    y "Or perhaps he hasn't been giving you enough attention?"
    pop "That's... ummpf... none of your business..."
    y "Aah don't worry about it. I'm sure he has other great qualities."
    y "I'm sure he'd be overjoyed to see you being fucked for the greater good of meeting up with your daughter."

    hide tomf_fuckmom with dissolve

    pop "...are you done already?"
    y "Would you be disappointmented if I was?"
    pop "NO!"
    y "Well, I've barely even started."
    y "But I think it's time I make good on my promise to you."
    y "Toph isn't the delicate flower you think she is."
    y "And I'm going to prove it to you."
    y "Toph! Come and join the fun we're having!"
    y "Show your mom you aren't a kid."
    show tomf tomf03 with hpunch

    t "Hey mom, watcha doing?"
    pop "Toph!!"
    pop "I... this... this isn't...!"
    t "Don't worry mom, I can understand the temptation of a hard cock going inside you."
    t "Show her, Aang."
    hide tomf_fuckmom
    show expression "bk3/toph/momfuck/toph_closedeyes.png"
    show tomf_fucktoph
    t "Ah!"
    show ctc
    pause
    hide ctc
    t "Unnnff.. see mom? I can take his dick...unf.. almost as easily as you can."
    y "This is the best mother daughter activity ever."
    y "I feel like making some \"That's what your mom said!\" jokes."
    y "but i'm too classy for that."
    y "unlike some sloppy floor-fucking bitches."
    pop "...."
    pop "toph, dear, you absolutely {i}must{/i} come home with me."
    t "I'm every bit the woman you are and don't need your protection."
    pop "But... but..."
    t "Do us both, Aang!"


    show tomf tomf04
    hide tomf_fucktoph
    show tomf_fuckall
    pop "AAaahh!"
    show ctc
    pause
    hide ctc
    y "mother... daughter... mother... daughter..."
    y "I can play this game all day long!"

    y "Hnnnngg... I was wrong..."
    y "Time to choose!"
    menu:
        "give toph a little sister":
            hide tomf_fuckall
            show expression "bk3/toph/momfuck/fuck3.png"
            y "bitch!"
            play sound "audio/splurt2.ogg"
            with flash
            hide expression "bk3/toph/momfuck/fuck3.png"
            show expression "bk3/toph/momfuck/dick_cummom.png"
            show expression "bk3/toph/momfuck/mom_closedeyes.png"
        "give mom a granddaughter":
            hide tomf_fuckall
            show expression "bk3/toph/momfuck/fuck16.png"
            y "bitch!"
            play sound "audio/splurt2.ogg"
            with flash
            hide expression "bk3/toph/momfuck/fuck16.png"
            show expression "bk3/toph/momfuck/dick_cumtoph.png"
            show expression "bk3/toph/momfuck/toph_closedeyes.png"

    y "Okay, I'll give you two some alone time now. You've got a lot to talk about."
    $ bk3_day = False
    jump bk3_village_background

label tophmomfuck2:
    show expression "ebackgrounds/bg_bk3_tophome_0.jpg"
    show tomf tomf00
    with dissolve
    pop "Avatar, Is my daughter here?"
    pop "we can give you whatever you desire if you help us."
    y "Mmmm... money is nice, but I want something else."
    y "I want to fuck you."
    y "Right here, right now."
    pop "very well.... i guess i don't have a choice."
    pop "I absolutely {i}must{/i} fuck you."
    pop "woe is me."
    y "....uh, right."
    y "Take off those clothes and lie down there."
    show tomf tomf01 with Dissolve(1.5)
    pop "please make this quick."
    y "Lift your leg up."
    show tomf tomf02 with dissolve
    y "Oh yeah, gonna fuck me some high class rich lady pussy!"
    y "I see Toph inherited the size of her boobs from you..."
    show expression "bk3/toph/momfuck/fuck1.png" with dissolve
    y "You're looking wet..."
    pop "Nonsense. Can we please get this over with?"
    y "Certainly."
    hide expression "bk3/toph/momfuck/fuck1.png"
    show tomf_fuckmom
    y "Oh wow, no problems getting in whatsoever."
    y "You're wet as fuck!"
    y "Do you get this wet when your husband wants to fuck you too?"
    y "Or perhaps he hasn't been giving you enough attention?"
    pop "That's... ummpf... none of your business..."
    y "Aah don't worry about it. I'm sure he has other great qualities."
    y "I'm sure he'd be overjoyed to see you being fucked for the greater good of meeting up with your daughter."

    hide tomf_fuckmom with dissolve

    pop "...are you done already?"
    y "Would you be disappointmented if I was?"
    pop "NO!"
    y "Well, I've barely even started."
    y "But I think it's time I make good on my promise to you."
    y "Toph isn't the delicate flower you think she is."
    y "And I'm going to prove it to you."
    y "Toph! Come and join the fun we're having!"
    y "Show your mom you aren't a kid."
    show tomf tomf03 with hpunch

    t "Hey mom, watcha doing?"
    pop "Toph!!"
    pop "I... this... this isn't...!"
    t "Don't worry mom, I can understand the temptation of a hard cock going inside you."
    t "Show her, Aang."
    hide tomf_fuckmom
    show expression "bk3/toph/momfuck/toph_closedeyes.png"
    show tomf_fucktoph
    t "Ah!"
    t "Unnnff.. see mom? I can take his dick...unf.. almost as easily as you can."
    y "This is the best mother daughter activity ever."
    y "I feel like making some \"That's what your mom said!\" jokes."
    y "but i'm too classy for that."
    y "unlike some sloppy floor-fucking bitches."
    pop "...."
    pop "toph, dear, you absolutely {i}must{/i} come home with me."
    t "I'm every bit the woman you are and don't need your protection."
    pop "But... but..."
    t "Do us both, Aang!"


    show tomf tomf04
    hide tomf_fucktoph
    show tomf_fuckall
    pop "AAaahh!"
    y "mother... daughter... mother... daughter..."
    y "I can play this game all day long!"

    y "Hnnnngg... I was wrong..."
    y "Time to choose!"
    menu:
        "give toph a little sister":
            hide tomf_fuckall
            show expression "bk3/toph/momfuck/fuck3.png"
            y "bitch!"
            play sound "audio/splurt2.ogg"
            with flash
            hide expression "bk3/toph/momfuck/fuck3.png"
            show expression "bk3/toph/momfuck/dick_cummom.png"
            show expression "bk3/toph/momfuck/mom_closedeyes.png"
        "give mom a granddaughter":
            hide tomf_fuckall
            show expression "bk3/toph/momfuck/fuck16.png"
            y "bitch!"
            play sound "audio/splurt2.ogg"
            with flash
            hide expression "bk3/toph/momfuck/fuck16.png"
            show expression "bk3/toph/momfuck/dick_cumtoph.png"
            show expression "bk3/toph/momfuck/toph_closedeyes.png"

    y "Okay, I'll give you two some alone time now. You've got a lot to talk about."
    $ bk3_day = False
    jump bk3_village_background


label toph_footjob1_3:
    $ toph_footjob_barechest = False
    $ toph_footjob = "dirt"

    scene black
    scene bg_bk3_tophome_0
    show tofj tofj09
    show tofj_blink_ani
    with sshake
    "toph drops onto her butt with a thud."
    t "now, give me that thick cock."

    show tofj tofj08
    hide tofj_blush
    with dissolve

    t "don't be shy."
    show tofj tofj09 with dissolve
    t "take it out."
    show tofj_solodick with dissolve
    y "jack it, first."
    t "mmmm..."
    t "you don't have to tell me twice."
    show tofj_jack_1
    hide tofj_solodick
    y "hngh..."
    show ctc
    pause
    hide ctc
    t "how's that, [bk3name]?"
    y "goo...good..."
    show tofj_jack_2
    hide tofj_jack_1
    hide tofj_doubt with dissolve
    t "\"goo good\", huh?"
    show ctc
    pause
    hide ctc
    y "ahhh..."
    t "i guess you wanna give me that goo, don't ya?"
    y "not yet..."
    t "then how about...."
    show tofj_jack_slow
    hide tofj_jack_2
    $ renpy.pause(0.5)
    show tofj_smile
    hide tofj_blush
    show tofj_blush
    with dissolve
    t "this?"
    y "mmgh..."
    t "oh, you're just too cute when you getting jacked off."
    y "you're... hmngh... cute... unh..."
    show ctc
    pause
    hide ctc
    show tofj_blink
    show tofj_blush
    with dissolve
    t "thanks, master!"
    hide tofj_blink
    show tofj_smirk
    hide tofj_blink_ani
    hide tofj_blush
    show tofj_blush
    with dissolve
    t "but i'm just enjoying gripping your warm... thick... cock."
    t "it really gives me purpose."
    show tofj_jack_fast
    hide tofj_jack_slow
    t "so let's speed up."
    show ctc
    pause
    hide ctc
    y "ohhh... shit, toph!"
    t "that's what i like to hear."
    hide tofj_smirk
    hide tofj_blush
    show tofj_blush
    show expression "bk3/toph/footjob/jack03.png"
    hide tofj_jack_fast
    hide tofj_smile
    with dissolve
    $ renpy.pause(0.25)
    t "but you want my feet, don't you?"
    y "so badly."
    show tofj_smirk
    hide tofj_smile
    hide tofj_blush
    show tofj_blush
    with dissolve
    t "mmm... my pleasure."
    hide expression "bk3/toph/footjob/jack03.png"
    hide tofj_doubt
    with dissolve
    t "so..."
    show tofj tofj103 with dissolve
    t "give it here."
    menu:
        "dirty":
            y "let's make a fucking mess."
            t "sweet."
        "clean":

            y "i'd really prefer you cleaned them off, first."
            show tofj tofj09 with dissolve
            t "if that's what you want, master."
            hide tofj_doubt
            show tofj_blink
            with dissolve
            t "......."
            hide tofj_blink
            $ toph_footjob = "clean"
            show tofj tofj103 with dissolve
            t "there. how's that?"
            y "better."

    t "alright, pull it back out."
    show tofj tofj15 with dissolve
    show tofj_doubt
    hide tofj_blush
    show tofj_blush
    with dissolve
    t "mmmm...."
    show ctc
    pause
    hide ctc
    y "what?"
    show tofj tofj101
    t "i..."
    show tofj_smirk
    hide tofj_doubt
    with dissolve
    t "...fucking love..."
    t "...how you feel between my toes."
    show ctc
    pause
    hide ctc
    y "nngh..."
    hide tofj_smirk
    show tofj_smile
    hide tofj_blush
    show tofj_blush
    with dissolve
    t "your big dick is so much fun!"
    y "you know just what to say...."
    hide tofj_smile
    show tofj_blink
    hide tofj_blush
    show tofj_blush
    with dissolve
    t "well... what if i said..."
    show tofj tofj101_1
    hide tofj_doubt
    show tofj_smirk
    hide tofj_blink
    hide tofj_blush
    show tofj_blush
    with dissolve
    t "...let's speed up?"
    y "ungh..."
    show ctc
    pause
    hide ctc
    t "yes, [bk3name]..."
    t "make a mess of me..."
    y "you know, it would help if i could look at your tits."
    hide tofj_smirk
    hide tofj_blush
    show tofj_smile
    with dissolve
    t "oh?"
    t "is that what you want?"
    hide tofj_smile
    show tofj_smirk
    hide tofj_blush
    show tofj_blush
    with dissolve
    t "and what would you do if i refused?"
    menu:
        "rip open her shirt":
            show tofj tofj09
            hide tofj_smirk
            show tofj_doubt
            hide tofj_blush
            show tofj_blush
            with dissolve
            t "hmm-?"
            $ toph_footjob_barechest = True
            with sshake
            hide tofj_doubt
            show tofj_angry
            hide tofj_blush
            show tofj_blush
            with dissolve
            t "yes!"
            t "that's it!"
            t "take what's yours, [bk3name]!"
            show ctc
            pause
            hide ctc
            hide tofj_angry
            show tofj tofj08
            with dissolve
            t "rip my shirt..."
            t "force me to rub your filthy, greedy cock..."
            show tofj tofj09
            show tofj_smirk
            hide tofj_blush
            show tofj_blush
            with dissolve
            t "make me..."
            show tofj tofj10
            show tofj_angry
            hide tofj_smirk
            hide tofj_blush
            with dissolve
            t "make you cum!"
            y "uh."
            hide tofj_angry

            hide tofj_blush
            show tofj_blush
            with dissolve
            t "don't be a chicken."
            show tofj tofj101_1
            with dissolve
            t "there you go."
        "have her speed up":

            ya "faster, toph!"
            show tofj_doubt
            hide tofj_blush
            show tofj_blush
            t "oh?"

    ya "faster!"
    show tofj tofj102
    show tofj_smirk
    hide tofj_doubt
    hide tofj_blush
    show tofj_blush
    with dissolve
    t "come on, then!"
    show ctc
    pause
    hide ctc
    t "fuck yes, baby..."
    t "forcing me to use my tiny little feet.."
    show tofj tofj102_1
    t "just to get you off..."
    t "you gonna release on me?"
    show ctc
    pause
    hide ctc
    t "are you gonna give me a warning?"
    t "...or just empty those big fucking balls all over me?"
    hide tofj_blink_ani
    show tofj_angry
    hide tofj_blush
    show tofj_blush
    with dissolve
    t "come on, asshole! give it to me!"
    show tofj tofj101_2 with dissolve
    ya "yes... fuck..."
    t "cum for me, you slut!"
    ya "ungh!"
    play sound "audio/splurt2.ogg"
    show tofj_sperm0
    $ renpy.pause(0.1)
    hide tofj_sperm0
    show tofj_sperm1
    hide tofj_angry
    show tofj_smile
    hide tofj_blush
    show tofj_blush
    hide tofj_sperm1
    show tofj_sperm1
    with dissolve
    t "*gasp*"
    t "yes, daddy!"
    y "fuck!"
    play sound "audio/splurt2.ogg"
    show tofj tofj18
    show tofj_angry
    hide tofj_smile
    show tofj_blink
    hide tofj_blush
    show tofj_blush
    hide tofj_sperm1
    show tofj_sperm1
    with dissolve
    t "cover me!"
    show tofj_sperm0
    $ renpy.pause(0.1)
    hide tofj_sperm0
    show tofj_sperm2
    $ renpy.pause(0.25)
    t "fuck, yes!"
    t "give me your cum, manwhore!"
    play sound "audio/splurt2.ogg"
    hide tofj_sperm1
    show tofj_sperm0
    $ renpy.pause(0.1)
    hide tofj_sperm0
    show tofj_sperm3
    hide tofj_angry
    show tofj_smirk
    hide tofj_blush
    show tofj_blush
    hide tofj_blink
    hide tofj_sperm3
    show tofj_sperm3
    with dissolve
    t "mmmm....."
    show ctc
    pause
    hide ctc
    show tofj tofj09 with dissolve
    y "unngh..."
    y "....."
    y "did you call me a slut?"
    hide tofj_smirk
    show tofj_smile
    hide tofj_blush
    show tofj_blush
    hide tofj_sperm3
    show tofj_sperm3
    with dissolve
    t "oh, yeah."
    y "and a manwhore?"
    hide tofj_smile
    show tofj_smirk
    hide tofj_blush
    show tofj_blush
    hide tofj_sperm3
    show tofj_sperm3
    with dissolve
    t "yeah!"
    t "did you like it?"
    y "....."
    y "kinda, yeah."
    t "i'll do that anytime."
    t "goodnight, [bk3name]!"
    scene black with dissolve
    "you head home for the night."
    jump bk3_next

label toph_footjob2_3:
    $ toph_footjob2_nude = False
    scene black
    scene bg_bk3_tophome_0
    show tofj tofj50
    with vshake
    "toph sits down with a thump."
    menu:
        "nude":
            $ toph_footjob2_nude = True
        "clothed":
            $ toph_footjob2_nude = False
    show ctc
    pause
    hide ctc
    t "i've been looking forward to seeing your cock again..."
    t "properly."
    show tofj2_solodick with dissolve
    y "that's what i like to hear."
    show tofj2_blink
    with dissolve
    t "where are you...."
    show tofj tofj51
    hide tofj2_solodick
    with dissolve
    t "ah... there you are."
    t "mmmm..."
    t "so handsome..."
    t "i forget..."
    y "you can start at any time...."
    show tofj tofj105
    show tofj2_uncertain
    hide tofj2_blink
    with dissolve

    t "sorry! sometimes i get... carried away..."
    show ctc
    pause
    hide ctc
    show tofj2_blink with dissolve
    t "i can feel every vein, every pulse..."
    t "so warm between my feet..."
    t "with a cock like this..."
    hide tofj2_blink with dissolve
    t "you really deserve to own all women..."
    t "including me."
    show tofj tofj106
    hide tofj2_uncertain
    with dissolve
    t "how about a little faster..."
    t "let's start forcing that cum up..."
    show ctc
    pause
    hide ctc
    y "ngh.... yeah..."
    y "keep... keep going..."
    show tofj2_uncertain with dissolve
    t "i want to feel you burst, [bk3name]."
    show tofj tofj107
    show tofj2_blink
    with dissolve
    t "don't be afraid... i'll pull it out."
    t "just relax... give in..."
    t "let me work."
    show ctc
    pause
    hide ctc
    y "yes... yes..."
    t "ngh... hmph... agh...."
    t "this is... so fucking sexy..."
    t "i'm so fucking wet..."
    y "open your eyes!"
    hide tofj2_blink with dissolve
    y "i'm... going to..."
    t "yes... yes, let it go!"
    t "let it all go!"
    y "slow down, but don't fucking stop!"
    show tofj tofj105 with dissolve
    y "ngh!"
    play sound "audio/splurt2.ogg"
    show tofj2_spermshot
    pause 0.2
    hide tofj2_spermshot
    show tofj2_sperm1
    y "little whore!"
    t "yes, daddy!"
    play sound "audio/splurt3.ogg"
    show tofj2_spermshot
    pause 0.2
    hide tofj2_spermshot
    show tofj2_sperm2
    hide tofj2_sperm1
    y "jack my cock with those cute little toes!"
    show tofj2_uncertain
    hide tofj2_sperm2
    show tofj2_sperm2
    with dissolve
    t "i love it! I fucking love it!"
    show tofj tofj51 with dissolve
    play sound "audio/splurt1.ogg"
    show tofj2_spermshot
    pause 0.2
    hide tofj2_spermshot
    show tofj2_sperm3
    hide tofj2_sperm2
    y "NNNGHGHGH!"
    show ctc
    pause
    hide ctc
    t "thank you... so much..."
    t "you're so... fucking powerful."
    t "i'm going to have to play with myself later."
    y "you do that."
    show tofj2_blink
    hide tofj2_uncertain
    hide tofj2_sperm3
    show tofj2_sperm3
    with dissolve
    y "thanks for your help."
    hide tofj2_blink with dissolve
    t "no, thank you."
    y "now, go find a towel."
    t "mmmm...."
    show ctc
    pause
    hide ctc
    scene black with dissolve
    "you head home for the night."
    jump bk3_next

label toph_blowjob3:
    hide screen earth_money_date
    scene black
    scene bg_bk3_tophome_2
    show tobb tobb01
    with dissolve
    t "you gonna give me that cock?"
    show tobb tobb02
    with dissolve
    t "*sniff* *sniff*"
    show tobb tobb03
    with dissolve
    t "mmm... i smell it..."

    show tobb tobb04
    with dissolve
    t "you haven't washed it!"
    t "you know just what i like."
    show tobb tobb01
    show tobb_unsure
    with dissolve
    t "i do get to clean it, right?"
    y "with your mouth, yeah."
    hide tobb_unsure with dissolve
    t "fuck yeah!"
    t "let me clean that thick, stinky cock..."
    t "...with my tiny little whore mouth."
    y "you sure?"
    show tobb_angry with dissolve
    t "don't tease me, aang!"
    t "i want to suck your fucking cock!"
    show tobb_blink

    with dissolve
    t "give it!"
    y "okay, okay... easy."
    hide tobb_blink
    hide tobb_angry
    with dissolve
    t "mmm... *pant* *pant*"
    show tobb_solodick with dissolve
    y "i'll let you give it a tongue bath."
    t "rub it on my face, first."

    show tobb tobb04
    with dissolve
    t "mmm..."
    t "you like how that feels?"
    t "your rough cock on my smooth, precious face?"
    t "seeing it push into my cheeks?"
    y "i really do."
    t "fuck this is making me wet."
    y "really?"
    t "yeah, i'm soaking this cheap rug."
    t "hold on-"
    show tobb tobb09
    hide tobb_solodick
    with dissolve
    t "mmmngh 'n ah."
    y "fuck yeah, i like that."
    t "mmgnh..."
    show tobb tobb100
    t "*sluurp*"
    show ctc
    pause
    hide ctc
    y "aahhhh..."
    y "good girl..."
    y "i had a long... sweaty day."
    y "so you need to slobber it clean, got it?"
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
    "toph sucks you to the balls, you can feel her throat wrapped around your shaft."
    show tobb tobb102
    y "oh fuck... toph..."
    "toph takes you in deeper and deeper... her slurps pulling you towards her each time."
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
    t "yes! more!"
    y "you cum dumpster!"
    show tobb_blink
    t "mmmmhhmm! yes!!"
    y "I'm gonna....."
    hide tobb_blink
    show tobb_unsure
    with dissolve
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
            y "fuuck..."
            t "delicious."
            t "all clean!"
            t "well, i guess i'm not clean any more..."
            y "fucking... great..."
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

            y "fuuck..."
            t "delicious."
            t "all clean!"
            show tobb_unsure
            hide tobb_spermout3
            show tobb_spermout3
            with dissolve
            t "well, i guess i'm not clean any more..."
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

label toph_sex3:
    $ toph_sex = True
    hide screen earth_money_date
    scene black
    scene bg_bk3_tophome_night
    show toi toi04
    with dissolve
    t "hey!"
    y "we're going to fuck tonight, toph."
    t "nice!"
    show toi_blink with dissolve
    t "give it me hard, okay?"
    scene black with dissolve
    scene bg_toph_missionary
    show totm totm11
    with dissolve
    t "come here..."
    show totm totm00 with dissolve
    show ctc
    pause
    hide ctc
    y "damn, girl."
    y "i guess you're ready."
    t "i've been waiting for you to fuck me all day."
    show totm totm01 with dissolve
    show ctc
    pause
    hide ctc
    t "ohhn... mmm..."
    t "push it... just a little more..."
    show totm totm02
    show totm_shock
    with dissolve
    t "aahhhh.... make me... make me yours..."
    show ctc
    pause 
    hide ctc
    t "it's... it's going..."
    y "the head's almost in..."
    hide totm_shock with dissolve
    t "i can feel it ins-"
    show totm totm03
    show expression "bk3/toph/missionary/head_shock_blink.png"

    with pflash
    t "hhhgh..."
    show ctc
    pause
    hide ctc
    t "ohh.... oh my god...."
    t "it's big... it's so b-"
    show totm totm04
    hide expression "bk3/toph/missionary/head_shock_blink.png"

    with vshake
    t "yes!!"
    t "ahhh...!"
    t "give... give me a second..."
    t "fuck, you're too big..."
    show totm totm03 with dissolve
    t "o...okay..."
    t "if you want, you can-"
    show totm totm102
    t "oh! nghh! ah!"
    t "fuck yes, aang!"
    show ctc
    pause
    hide ctc
    show totm totm101
    show expression "bk3/toph/missionary/blink.png"
    with dissolve
    show ctc
    pause
    hide ctc
    y "do you need me to go easy on you?"
    t "fuck no!"
    y "...oh."
    scene black
    show expression "bk3/toph/missionary/bg_toph_missionary1.jpg"

    show totm_cdick:
        ypos 20 xpos 477
        linear 1.0 ypos 120
        linear 1.0 ypos 20
        repeat

    show totm totm20
    with dissolve
    show ctc
    pause
    hide ctc
    y "let's liven things up?"
    t "ah... nh... wha..."
    show ctc
    pause
    hide ctc
    menu:
        "choke a bitch":
            show expression "bk3/toph/missionary/chands.png":
                ypos -200
                linear 3.0 ypos -100
            $ renpy.pause(3, hard = True)

            show totm_cdick:
                ypos 20
                easein 2.0 ypos 120
                easeout 2.0 ypos 20
                repeat


            hide expression "bk3/toph/missionary/chands.png"
            show totm totm25 with vpunch

            t "hrk!"
            "You feel Toph tightening, making you go slower."
            show ctc
            pause
            hide ctc
            t "ghh...hgh...agh..."
            t "an...i...anh...eeth.."
            show expression "bk3/toph/missionary/cface_lewd.png"
            with dissolve

            y "Yeah, you like that, doncha?"
            show ctc
            pause
            hide ctc
            t "hhgh...hrk..."
            y "feeling lightheaded?"
            t "hgh...gh..."
            show totm totm20
            show expression "bk3/toph/missionary/chands_open.png"
            hide expression "bk3/toph/missionary/cface_lewd.png"
            with dissolve
            "You release your grip to allow her to gasp for air."
            show ctc
            pause
            hide ctc
            t "*pant* *pant*"
            t "i... i couldn't breathe..."
            t "why did you sto-"
            hide expression "bk3/toph/missionary/chands_open.png"
            show totm totm25 with vpunch
            t "gagh!"
            "you tighten your grip once more."
            show expression "bk3/toph/missionary/cface_lewd.png"
            with dissolve
            t "hnnnghhahh..."
            y "i can't believe how tight you are..."
            y "i'm struggle to pull out of you each time..."
            show ctc
            pause
            hide ctc
            y "fuck..."
            y "fuck, toph..."
            y "your tight fucking cunt is gonna..."
            y "gonna make me...."
            menu:
                "don't release your grip until you cum":
                    "you speed up despite the clamplike feeling of Toph's pussy."
                    show totm_cdick:
                        ypos 20
                        easein 0.5 ypos 120
                        easeout 0.5 ypos 20
                        repeat
                    t "ngh! hrk! gh!"
                    y "that's it, bitch!"
                    y "you're mine! you're my little fucking whore!"
                    y "say it!"
                    t "...hghh!"
                    y "say you're my fucking whore!"
                    t "ahh...uuugh...ohhh..."
                    y "yes! you little slut!"
                    y "You cock loving slut!"
                    y "i'm almost there!"
                    menu:
                        "cum inside":

                            y "let's give you a creampie!"
                            t "nngh! aohh!"
                            play sound "audio/splurt2.ogg"
                            show totm_cdick:
                                ypos 120
                            with flash
                            "You empty your balls inside of Toph."
                            show totm totm20

                            show totm_cdick:
                                ypos -100
                            show expression "bk3/toph/missionary/csperm_in.png"
                            with Dissolve(2.0)

                            y "Aaaah.. that was the best."
                            hide expression "bk3/toph/missionary/csperm_in.png"
                        "cum outside":


                            ya "little slut!"
                            t "ah! oo 'ant-"
                            hide totm_cdick
                            show totm_cdick:
                                ypos 100 xpos 480
                            "In one big explosion, you release every drop of sperm from your balls on Toph's face."
                            show expression "bk3/toph/mastur_kat/white.png"
                            show expression "bk3/toph/missionary/csperm_out.png"
                            hide expression "bk3/toph/mastur_kat/white.png" with Dissolve(2.0)
                            show totm totm20 with Dissolve(1.5)

                            y "Aaaah... fuck. You're the best, Toph."


                    hide totm_cdick
                    y "Okay, I'll let myself out."
                    t "I... i don't think i'm..."
                    t "...going to be able to walk tomorrow..."
                    scene black with dissolve
                    "worn out, you head home for the night."
                    jump bk3_next
                "let her breathe":

                    show totm totm20 with Dissolve(1)
                    hide expression "bk3/toph/missionary/cface_lewd.png" with Dissolve(1)
                    t "ahh... hhha..."
                    show ctc
                    pause
                    hide ctc
                    t "it... it does feel..."
                    t "i'm so... dizzy..."
                    show totm_cdick:
                        ypos 20
                        easein 0.5 ypos 120
                        easeout 0.5 ypos 20
                        repeat
                    show expression "bk3/toph/missionary/cface_lewd.png" with dissolve
                    "you speed up as you feel yourself approaching climax..."
                    t "hah... ah... yes..."
                    t "yes... aang..."
                    hide expression "bk3/toph/missionary/cface_lewd.png" with dissolve
                    t "give... give it to... ahn... m-me..."
                    menu:
                        "cum inside":
                            ya "ngh! fuck!"
                            ya "let's give you a creampie!"
                            show totm totm26 with vshake
                            t "fill up your slut!"
                            t "release it all inside me!"
                            show totm totm27
                            t "i want to feel your seed!!!"
                            play sound "audio/splurt2.ogg"
                            show totm_cdick:
                                ypos 120
                            with flash
                            "You empty your balls inside of Toph."
                            show totm totm20

                            show totm_cdick:
                                ypos -100
                            show expression "bk3/toph/missionary/csperm_in.png"
                            with Dissolve(2.0)
                            t "uunngh...."
                            y "Aaaah.. that was the best."
                            hide expression "bk3/toph/missionary/csperm_in.png"

                            hide totm_cdick
                            y "Okay, I'll let myself out."
                            t "I... i don't think i'm..."
                            t "...going to be able to walk tomorrow..."
                            show ctc
                            pause
                            hide ctc
                            scene black with dissolve
                            "worn out, you head home for the night."
                            jump bk3_next
                        "cum outside":

                            ya "little slut!"
                            show expression "bk3/toph/missionary/cface_lewd.png" with dissolve
                            t "wait, what are you-"
                            hide totm_cdick
                            show totm_cdick:
                                ypos 100 xpos 480
                            "In one big explosion, you release every drop of sperm from your balls on Toph's face."
                            play sound "audio/splurt2.ogg"
                            show expression "bk3/toph/mastur_kat/white.png"
                            show expression "bk3/toph/missionary/csperm_out.png"
                            $ renpy.pause(0.05)
                            hide expression "bk3/toph/missionary/cface_lewd.png"
                            hide expression "bk3/toph/mastur_kat/white.png"
                            with Dissolve(1.5)
                            show ctc
                            pause
                            hide ctc
                            show totm totm20 with Dissolve(1.5)

                            y "Aaaah... fuck. You're the best, Toph."
                            hide totm_cdick
                            y "Okay, I'll let myself out."
                            t "I... i don't think i'm..."
                            t "...going to be able to walk tomorrow..."
                            show ctc
                            pause
                            hide ctc
                            scene black with dissolve
                            "worn out, you head home for the night."
                            jump bk3_next
                        "first position":

                            scene black
                            show expression "bk3/toph/missionary/bg_toph_missionary.jpg"
                            show totm totm105
                            with dissolve
                            pass
        "first position":
            scene black
            show expression "bk3/toph/missionary/bg_toph_missionary.jpg"
            show totm totm101
            show expression "bk3/toph/missionary/head_shock.png"
            show expression "bk3/toph/missionary/blink.png"
            with dissolve
            t "you gonna..."
            hide expression "bk3/toph/missionary/head_shock.png"
            hide expression "bk3/toph/missionary/blink.png"
            with dissolve
            t "...gonna give it..."
            t "to me...?"
            show totm totm103
            t "ohhh... unnhh..."
            y "how's that, bitch?!"
            t "unh!!"
            show ctc
            pause
            hide ctc
            "Toph squeezes you unintentionally with every thrust."
            y "fuck!"
            t "oh... hgh... aang..."
            y "Yeah, you like that, dont you?"
            show ctc
            pause
            hide ctc
            t "it's... ahh... ah... oh... fff... fu..."
            y "that's it! say it!"
            show totm totm104
            t "aahhh....!!"
            show ctc
            pause
            hide ctc
            y "say it!"
            t "fuu..."
            show totm totm105
            t "fuck!!!"
            show ctc
            pause
            hide ctc
            t "it's... *gasp...* so... ahh..."
            t "i'm... i feel so... i'm gonna..."
            show ctc
            pause
            hide ctc
            y "fuck...!"
            y "fuck, toph...!"
            y "your tight fucking cunt is gonna..."
            y "gonna make me...."

    show ctc
    pause
    hide ctc

    menu:
        "cum inside":
            ya "take my load, slut!"
            t "make me your cum dumpster!"
            play sound "audio/splurt2.ogg"
            show totm totm06
            show expression "bk3/toph/missionary/head_shock.png"
            with flash
            ya "little whore!"
            play sound "audio/splurt3.ogg"
            with flash
            show ctc
            pause
            hide ctc
            t "hhgnh...."

            show totm totm07
            show expression "bk3/toph/missionary/blink.png"
            with flash
            show ctc
            pause
            hide ctc
            y "Aaaah... fuck. You're the best, Toph."
            y "Okay, I'll let myself out."
            t "I..."
            hide expression "bk3/toph/missionary/head_shock.png" with dissolve
            t "i don't think i'm..."
            t "...going to be able to walk tomorrow..."
            show ctc
            pause
            hide ctc
            scene black with dissolve
            "worn out, you head home for the night."
            jump bk3_next
        "cum outside":

            ya "take my load, slut!"
            t "make me your cum dumpster!"
            play sound "audio/splurt2.ogg"
            show totm totm00
            show expression "bk3/toph/missionary/head_shock.png"
            show expression "bk3/toph/missionary/solodick.png"
            show expression "bk3/toph/missionary/spermshot.png"
            $ renpy.pause(0.3)
            hide expression "bk3/toph/missionary/spermshot.png"
            show expression "bk3/toph/missionary/spermout1.png"
            $ renpy.pause()
            ya "little whore!"
            show expression "bk3/toph/missionary/blink.png"
            play sound "audio/splurt3.ogg"
            show expression "bk3/toph/missionary/spermshot.png"
            $ renpy.pause(0.3)
            hide expression "bk3/toph/missionary/spermshot.png"
            show expression "bk3/toph/missionary/spermout2.png"
            $ renpy.pause()
            play sound "audio/splurt1.ogg"
            show expression "bk3/toph/missionary/spermshot.png"
            $ renpy.pause(0.3)
            hide expression "bk3/toph/missionary/spermshot.png"
            show expression "bk3/toph/missionary/spermout3.png"
            t "hhgnh...."
            show ctc
            pause
            hide ctc
            y "Aaaah... fuck. You're the best, Toph."
            y "Okay, I'll let myself out."
            t "I..."
            hide expression "bk3/toph/missionary/blink.png"
            with dissolve
            t "i don't think i'm..."
            hide expression "bk3/toph/missionary/head_shock.png" with dissolve
            t "...going to be able to walk tomorrow..."
            show ctc
            pause
            hide ctc
            scene black with dissolve
            "worn out, you head home for the night."
            jump bk3_next

label toph_anal3:
    hide screen earth_money_date
    scene black with Dissolve(1)
    scene expression "ebackgrounds/boobjob.jpg"
    show toaa toaa01
    with dissolve
    y "oh, hell yeah."
    show ctc
    pause
    hide ctc
    t "come... slide it in my ass."
    y "careful what you wish for."
    show toaa toaa03 with dissolve
    show ctc
    pause
    hide ctc
    t "here..."
    menu:
        "open her up with your finger":
            show toaa_fingering
            t "ohh...."
            show ctc
            pause
            hide ctc
            y "damn... i forget how tiny and tight you are sometimes..."
            t "it feels... good..."
            t "open me up, master..."
            hide toaa_fingering
            y "Time for some dick up your ass, Toph."
            t "yes... do it..."
        "Foreplay is for people who care":

            pass

    show toaa toaa20 with dissolve
    t "just... put it in gently at first, okay?"
    menu:
        "okay":
            show toaa_blink_toph
            show toaa toaa101
            t "hhngh..."
        "no":

            show toaa toaa24
            show toaa_blink_toph
            with vshake
            t "aahhh!!!!"

    show ctc
    pause
    hide ctc
    t "ahh... ahh... give it to my ass..."
    hide toaa_blink_toph with dissolve
    t "fill it... fuck..."

    menu:
        "wreck that ass!":
            y "well...."
            show toaa toaa106
            $ toaa_wrecked_ass = True
            t "aaahh!!! f-fuck! aang!"
            t "fucking hell!"
            y "I'm gonna ruin that tight little ass of yours!"
            t "fuck yes! ruin me!"
        "keep going slowly":
            $ toaa_wrecked_ass = False
            y "Fuck! You're like a goddamn clamp, Toph!"

    t "ahhh... aang... it... it's so good..."
    y "I'm getting... really close now, Toph!"
    t "let me have your spunk, [bk3name]!"
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
            t "it's... ah... so... much..."
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
            t "there's nothing like cum dripping out of your asshole..."
            y "i'm gonna have to take your word for it."
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
            t "there's nothing like that in the whole fucking world..."
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

    "test"

"test"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
