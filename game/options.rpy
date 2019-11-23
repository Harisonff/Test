








init -1 python hide:





    config.developer = False



    config.screen_width = 1000
    config.screen_height = 720



    style.say_who_window.background = Frame("orange_border.png", 40, 40)
    style.say_who_window.xalign = 0.0
    style.say_who_window.yalign = 1.0
    style.say_who_window.xpos = 2 
    style.say_who_window.ypos = 49 
    style.say_who_window.left_padding = 15
    style.say_who_window.top_padding = 15
    style.say_who_window.right_padding = 15 
    style.say_who_window.bottom_padding = 15
    style.say_who_window.xminimum = 300 
    style.say_who_window.yminimum = 50 




    config.window_title = u"Four Elements Trainer"



    config.name = "Four Elements Trainer"
    config.version = "0.8.3c"












    theme.threeD(
        
        

        
        widget = "#59667a",

        
        widget_hover = "#343e4d",

        
        widget_text = "#ffffff",

        
        
        widget_selected = "#bed4f6",

        
        disabled = "#929292",

        
        disabled_text = "#ababab",

        
        label = "#343e4d",

        
        frame = "#d2d2d2",

        
        
        
        
        
        mm_root = Animation("introscreen1.jpg", 3.2, "introscreen.jpg", .1),

        
        
        
        gm_root = "#59667a",

        
        
        rounded_window = False,

        
        
        
        )









    style.window.background = Frame("frame.png", 12, 12)




    style.window.left_margin = 1
    style.window.right_margin = 1
    style.window.top_margin = 1
    style.window.bottom_margin = 1




    style.window.left_padding = 60
    style.window.right_padding = 260
    style.window.top_padding = 35
    style.window.bottom_padding = 35




    style.window.yminimum = 175



























    style.default.font = "Fonts/hbold.ttf"



    style.default.size = 22

    style.default.color = "#000000" 











    config.has_sound = True



    config.has_music = True



    config.has_voice = False



    style.button.activate_sound = "audio/click3.mp3"
    style.imagemap.activate_sound = "audio/click3.mp3"



    config.enter_sound = "audio/click3.mp3"
    config.exit_sound = "audio/click3.mp3"



    config.sample_sound = "audio/click3.mp3"



    config.main_menu_music = "audio/Dreamer.mp3"











    config.help = "README.html"






    config.enter_transition = None


    config.exit_transition = None


    config.intra_transition = None


    config.main_game_transition = None


    config.game_main_transition = None


    config.end_splash_transition = None


    config.end_game_transition = None


    config.after_load_transition = None


    config.window_show_transition = None


    config.window_hide_transition = None


    config.adv_nvl_transition = dissolve


    config.nvl_adv_transition = dissolve


    config.enter_yesno_transition = None


    config.exit_yesno_transition = None


    config.enter_replay_transition = None


    config.exit_replay_transition = None


    config.say_attribute_transition = None





python early:
    config.save_directory = "Avatar Harem-1467471742"

init -1 python hide:









    config.default_fullscreen = False



    config.default_text_cps = 42



    config.default_afm_time = 10



    config.window_icon = "icon.png"



image water_hover = Animation("backgrounds/worldmap_imagemap/worldmap_hotspotglow_01.png", .2, "backgrounds/worldmap_imagemap/worldmap_hotspotglow_02.png", .2, "backgrounds/worldmap_imagemap/worldmap_hotspotglow_03.png", .2, "backgrounds/worldmap_imagemap/worldmap_hotspotglow_04.png", .2, "backgrounds/worldmap_imagemap/worldmap_hotspotglow_03.png", .2, "backgrounds/worldmap_imagemap/worldmap_hotspotglow_02.png", .2)
image earth_hover = Animation("backgrounds/worldmap_imagemap/worldmap_hotspotglow_01.png", .2, "backgrounds/worldmap_imagemap/worldmap_hotspotglow_02.png", .2, "backgrounds/worldmap_imagemap/worldmap_hotspotglow_03.png", .2, "backgrounds/worldmap_imagemap/worldmap_hotspotglow_04.png", .2, "backgrounds/worldmap_imagemap/worldmap_hotspotglow_03.png", .2, "backgrounds/worldmap_imagemap/worldmap_hotspotglow_02.png", .2)
image fire_hover = Animation("backgrounds/worldmap_imagemap/worldmap_hotspotglow_01.png", .2, "backgrounds/worldmap_imagemap/worldmap_hotspotglow_02.png", .2, "backgrounds/worldmap_imagemap/worldmap_hotspotglow_03.png", .2, "backgrounds/worldmap_imagemap/worldmap_hotspotglow_04.png", .2, "backgrounds/worldmap_imagemap/worldmap_hotspotglow_03.png", .2, "backgrounds/worldmap_imagemap/worldmap_hotspotglow_02.png", .2)
image air_hover = Animation("backgrounds/worldmap_imagemap/worldmap_hotspotglow_01.png", .2, "backgrounds/worldmap_imagemap/worldmap_hotspotglow_02.png", .2, "backgrounds/worldmap_imagemap/worldmap_hotspotglow_03.png", .2, "backgrounds/worldmap_imagemap/worldmap_hotspotglow_04.png", .2, "backgrounds/worldmap_imagemap/worldmap_hotspotglow_03.png", .2, "backgrounds/worldmap_imagemap/worldmap_hotspotglow_02.png", .2)

screen worldmap:
    add "backgrounds/worldmap_01.jpg"
    imagebutton idle "backgrounds/worldmap_imagemap/worldmap_hotspotglow_01.png" hover "water_hover" xpos 19 ypos 7 action Jump("water1") focus_mask True
    imagebutton idle "backgrounds/worldmap_imagemap/worldmap_hotspotglow_01.png" hover "earth_hover" xpos 816 ypos 7 action Jump("earth1") focus_mask True
    imagebutton idle "backgrounds/worldmap_imagemap/worldmap_hotspotglow_01.png" hover "fire_hover" xpos 42 ypos 503 action Jump("fire1") focus_mask True
    imagebutton idle "backgrounds/worldmap_imagemap/worldmap_hotspotglow_01.png" hover "air_hover" xpos 819 ypos 521 action Jump("air1") focus_mask True

screen worldmap_02:
    add "backgrounds/worldmap_01.jpg"
    imagebutton idle "backgrounds/worldmap_imagemap/worldmap_hotspotglow_01.png" hover "water_hover" xpos 19 ypos 7 action Jump("water2") focus_mask True
    imagebutton idle "backgrounds/worldmap_imagemap/worldmap_hotspotglow_01.png" hover "earth_hover" xpos 816 ypos 7 action Jump("earth2") focus_mask True
    imagebutton idle "backgrounds/worldmap_imagemap/worldmap_hotspotglow_01.png" hover "fire_hover" xpos 42 ypos 503 action Jump("fire2") focus_mask True
    imagebutton idle "backgrounds/worldmap_imagemap/worldmap_hotspotglow_01.png" hover "air_hover" xpos 819 ypos 521 action Jump("air2") focus_mask True

screen worldmap_03:
    add "backgrounds/worldmap_01.jpg"
    imagebutton idle "backgrounds/worldmap_imagemap/worldmap_hotspotglow_01.png" hover "water_hover" xpos 19 ypos 7 action Jump("water3") focus_mask True
    imagebutton idle "backgrounds/worldmap_imagemap/worldmap_hotspotglow_01.png" hover "earth_hover" xpos 816 ypos 7 action Jump("earth3") focus_mask True
    imagebutton idle "backgrounds/worldmap_imagemap/worldmap_hotspotglow_01.png" hover "fire_hover" xpos 42 ypos 503 action Jump("fire3") focus_mask True
    imagebutton idle "backgrounds/worldmap_imagemap/worldmap_hotspotglow_01.png" hover "air_hover" xpos 819 ypos 521 action Jump("air3") focus_mask True


image home_hover = Animation("backgrounds/bg_k_village_imagemap/bg_k_village_home_01.png", .2, "backgrounds/bg_k_village_imagemap/bg_k_village_home_02.png", .2, "backgrounds/bg_k_village_imagemap/bg_k_village_home_03.png", .2, "backgrounds/bg_k_village_imagemap/bg_k_village_home_04.png", .2, "backgrounds/bg_k_village_imagemap/bg_k_village_home_03.png", .2, "backgrounds/bg_k_village_imagemap/bg_k_village_home_02.png", .2)
image hunting_hover = Animation("backgrounds/bg_k_village_imagemap/bg_k_village_hunting_01.png", .2, "backgrounds/bg_k_village_imagemap/bg_k_village_hunting_02.png", .2, "backgrounds/bg_k_village_imagemap/bg_k_village_hunting_03.png", .2, "backgrounds/bg_k_village_imagemap/bg_k_village_hunting_04.png", .2, "backgrounds/bg_k_village_imagemap/bg_k_village_hunting_03.png", .2, "backgrounds/bg_k_village_imagemap/bg_k_village_hunting_02.png", .2)
image katara_hover = Animation("backgrounds/bg_k_village_imagemap/bg_k_village_katarahouse_01.png", .2, "backgrounds/bg_k_village_imagemap/bg_k_village_katarahouse_02.png", .2, "backgrounds/bg_k_village_imagemap/bg_k_village_katarahouse_03.png", .2, "backgrounds/bg_k_village_imagemap/bg_k_village_katarahouse_04.png", .2, "backgrounds/bg_k_village_imagemap/bg_k_village_katarahouse_03.png", .2, "backgrounds/bg_k_village_imagemap/bg_k_village_katarahouse_02.png", .2)
image market_hover = Animation("backgrounds/bg_k_village_imagemap/bg_k_village_marketplace_01.png", .2, "backgrounds/bg_k_village_imagemap/bg_k_village_marketplace_02.png", .2, "backgrounds/bg_k_village_imagemap/bg_k_village_marketplace_03.png", .2, "backgrounds/bg_k_village_imagemap/bg_k_village_marketplace_04.png", .2, "backgrounds/bg_k_village_imagemap/bg_k_village_marketplace_03.png", .2, "backgrounds/bg_k_village_imagemap/bg_k_village_marketplace_02.png", .2)
image mine_hover = Animation("backgrounds/bg_k_village_imagemap/bg_k_village_mine_01.png", .2, "backgrounds/bg_k_village_imagemap/bg_k_village_mine_02.png", .2, "backgrounds/bg_k_village_imagemap/bg_k_village_mine_03.png", .2, "backgrounds/bg_k_village_imagemap/bg_k_village_mine_04.png", .2, "backgrounds/bg_k_village_imagemap/bg_k_village_mine_03.png", .2, "backgrounds/bg_k_village_imagemap/bg_k_village_mine_02.png", .2)
image mountain_hover = Animation("backgrounds/bg_k_village_imagemap/bg_k_village_mountain_01.png", .2, "backgrounds/bg_k_village_imagemap/bg_k_village_mountain_02.png", .2, "backgrounds/bg_k_village_imagemap/bg_k_village_mountain_03.png", .2, "backgrounds/bg_k_village_imagemap/bg_k_village_mountain_04.png", .2, "backgrounds/bg_k_village_imagemap/bg_k_village_mountain_03.png", .2, "backgrounds/bg_k_village_imagemap/bg_k_village_mountain_02.png", .2)
image school_hover = Animation("backgrounds/bg_k_village_imagemap/bg_k_village_school_01.png", .2, "backgrounds/bg_k_village_imagemap/bg_k_village_school_02.png", .2, "backgrounds/bg_k_village_imagemap/bg_k_village_school_03.png", .2, "backgrounds/bg_k_village_imagemap/bg_k_village_school_04.png", .2, "backgrounds/bg_k_village_imagemap/bg_k_village_school_03.png", .2, "backgrounds/bg_k_village_imagemap/bg_k_village_school_02.png", .2)
image training_hover = Animation("backgrounds/bg_k_village_imagemap/bg_k_village_training_01.png", .2, "backgrounds/bg_k_village_imagemap/bg_k_village_training_02.png", .2, "backgrounds/bg_k_village_imagemap/bg_k_village_training_03.png", .2, "backgrounds/bg_k_village_imagemap/bg_k_village_training_04.png", .2, "backgrounds/bg_k_village_imagemap/bg_k_village_training_03.png", .2, "backgrounds/bg_k_village_imagemap/bg_k_village_training_02.png", .2)


screen snowday:
    add "backgrounds/bg_k_village_day.jpg"
    add SnowBlossom(Animation("images/snowflake3.png"), count=100, xspeed=(200, 500), yspeed=(400, 600), start=0)
    add SnowBlossom(Animation("images/snowflake3.png"), count=100, xspeed=(200, 500), yspeed=(400, 600), start=0)
    add SnowBlossom(Animation("images/snowflake3.png", 0.15, "images/snowflake1.png", 0.15), count=100, xspeed=(400, 600), yspeed=(500, 900), start=0)
    imagebutton idle "backgrounds/bg_k_village_imagemap/bg_k_village_home_01.png" hover "home_hover" xpos 0 ypos 376 action Jump("home_day") focus_mask True
    imagebutton idle "backgrounds/bg_k_village_imagemap/bg_k_village_hunting_01.png" hover "hunting_hover" xpos 377 ypos 531 action Jump("hunt_day") focus_mask True
    imagebutton idle "backgrounds/bg_k_village_imagemap/bg_k_village_katarahouse_01.png" hover "katara_hover" xpos 476 ypos 331 action Jump("katara_day") focus_mask True
    imagebutton idle "backgrounds/bg_k_village_imagemap/bg_k_village_marketplace_01.png" hover "market_hover" xpos 112 ypos 218 action Jump("market_day") focus_mask True
    imagebutton idle "backgrounds/bg_k_village_imagemap/bg_k_village_mine_01.png" hover "mine_hover" xpos 833 ypos 179 action Jump("mine_day") focus_mask True
    imagebutton idle "backgrounds/bg_k_village_imagemap/bg_k_village_mountain_01.png" hover "mountain_hover" xpos 497 ypos 0 action Jump("mountain_day") focus_mask True
    imagebutton idle "backgrounds/bg_k_village_imagemap/bg_k_village_school_01.png" hover "school_hover" xpos 663 ypos 389 action Jump("school_day") focus_mask True
    imagebutton idle "backgrounds/bg_k_village_imagemap/bg_k_village_training_01.png" hover "training_hover" xpos 114 ypos 463 action Jump("train_day") focus_mask True

screen day:
    add "backgrounds/bg_k_village_day.jpg"
    imagebutton idle "backgrounds/bg_k_village_imagemap/bg_k_village_home_01.png" hover "home_hover" xpos 0 ypos 376 action Jump("home_day") focus_mask True
    imagebutton idle "backgrounds/bg_k_village_imagemap/bg_k_village_hunting_01.png" hover "hunting_hover" xpos 377 ypos 531 action Jump("hunt_day") focus_mask True
    imagebutton idle "backgrounds/bg_k_village_imagemap/bg_k_village_katarahouse_01.png" hover "katara_hover" xpos 476 ypos 331 action Jump("katara_day") focus_mask True
    imagebutton idle "backgrounds/bg_k_village_imagemap/bg_k_village_marketplace_01.png" hover "market_hover" xpos 112 ypos 218 action Jump("market_day") focus_mask True
    imagebutton idle "backgrounds/bg_k_village_imagemap/bg_k_village_mine_01.png" hover "mine_hover" xpos 833 ypos 179 action Jump("mine_day") focus_mask True
    imagebutton idle "backgrounds/bg_k_village_imagemap/bg_k_village_mountain_01.png" hover "mountain_hover" xpos 497 ypos 0 action Jump("mountain_day") focus_mask True
    imagebutton idle "backgrounds/bg_k_village_imagemap/bg_k_village_school_01.png" hover "school_hover" xpos 663 ypos 389 action Jump("school_day") focus_mask True
    imagebutton idle "backgrounds/bg_k_village_imagemap/bg_k_village_training_01.png" hover "training_hover" xpos 114 ypos 463 action Jump("train_day") focus_mask True


screen night:
    add "backgrounds/bg_k_village_night.jpg"
    imagebutton idle "backgrounds/bg_k_village_imagemap/bg_k_village_home_01.png" hover "home_hover" xpos 0 ypos 376 action Jump("home_night") focus_mask True
    imagebutton idle "backgrounds/bg_k_village_imagemap/bg_k_village_katarahouse_01.png" hover "katara_hover" xpos 476 ypos 331 action Jump("katara_night") focus_mask True
    imagebutton idle "backgrounds/bg_k_village_imagemap/bg_k_village_marketplace_01.png" hover "market_hover" xpos 112 ypos 218 action Jump("market_night") focus_mask True

    imagebutton idle "backgrounds/bg_k_village_imagemap/bg_k_village_school_01.png" hover "school_hover" xpos 663 ypos 389 action Jump("school_night") focus_mask True

screen snownight:
    add "backgrounds/bg_k_village_night.jpg"
    add SnowBlossom(Animation("images/snowflake3.png"), count=100, xspeed=(200, 500), yspeed=(400, 600), start=0)
    add SnowBlossom(Animation("images/snowflake3.png"), count=100, xspeed=(200, 500), yspeed=(400, 600), start=0)
    add SnowBlossom(Animation("images/snowflake3.png", 0.15, "images/snowflake1.png", 0.15), count=100, xspeed=(400, 600), yspeed=(500, 900), start=0)
    imagebutton idle "backgrounds/bg_k_village_imagemap/bg_k_village_home_01.png" hover "home_hover" xpos 0 ypos 376 action Jump("home_night") focus_mask True
    imagebutton idle "backgrounds/bg_k_village_imagemap/bg_k_village_katarahouse_01.png" hover "katara_hover" xpos 476 ypos 331 action Jump("katara_night") focus_mask True
    imagebutton idle "backgrounds/bg_k_village_imagemap/bg_k_village_marketplace_01.png" hover "market_hover" xpos 112 ypos 218 action Jump("market_night") focus_mask True

    imagebutton idle "backgrounds/bg_k_village_imagemap/bg_k_village_school_01.png" hover "school_hover" xpos 663 ypos 389 action Jump("school_night") focus_mask True


screen kfinal_slave:
    add "backgrounds/bg_k_village_day1.jpg"
    imagebutton idle "backgrounds/bg_k_village_imagemap/bg_k_village_home_01.png" hover "home_hover" xpos 0 ypos 376 action Jump("home_final1") focus_mask True
    imagebutton idle "backgrounds/bg_k_village_imagemap/bg_k_village_hunting_01.png" hover "hunting_hover" xpos 377 ypos 531 action Jump("hunt_final1") focus_mask True
    imagebutton idle "backgrounds/bg_k_village_imagemap/bg_k_village_katarahouse_01.png" hover "katara_hover" xpos 476 ypos 331 action Jump("katara_final1") focus_mask True
    imagebutton idle "backgrounds/bg_k_village_imagemap/bg_k_village_marketplace_01.png" hover "market_hover" xpos 112 ypos 218 action Jump("market_final1") focus_mask True
    imagebutton idle "backgrounds/bg_k_village_imagemap/bg_k_village_mine_01.png" hover "mine_hover" xpos 833 ypos 179 action Jump("mine_final1") focus_mask True
    imagebutton idle "backgrounds/bg_k_village_imagemap/bg_k_village_mountain_01.png" hover "mountain_hover" xpos 497 ypos 0 action Jump("mountain_final1") focus_mask True
    imagebutton idle "backgrounds/bg_k_village_imagemap/bg_k_village_school_01.png" hover "school_hover" xpos 663 ypos 389 action Jump("school_final1") focus_mask True
    imagebutton idle "backgrounds/bg_k_village_imagemap/bg_k_village_training_01.png" hover "training_hover" xpos 114 ypos 463 action Jump("train_final1") focus_mask True

screen kfinal_harem:
    add "backgrounds/bg_k_village_day1.jpg"
    imagebutton idle "backgrounds/bg_k_village_imagemap/bg_k_village_home_01.png" hover "home_hover" xpos 0 ypos 376 action Jump("home_final2") focus_mask True
    imagebutton idle "backgrounds/bg_k_village_imagemap/bg_k_village_hunting_01.png" hover "hunting_hover" xpos 377 ypos 531 action Jump("hunt_final2") focus_mask True
    imagebutton idle "backgrounds/bg_k_village_imagemap/bg_k_village_katarahouse_01.png" hover "katara_hover" xpos 476 ypos 331 action Jump("katara_final2") focus_mask True
    imagebutton idle "backgrounds/bg_k_village_imagemap/bg_k_village_marketplace_01.png" hover "market_hover" xpos 112 ypos 218 action Jump("market_final2") focus_mask True
    imagebutton idle "backgrounds/bg_k_village_imagemap/bg_k_village_mine_01.png" hover "mine_hover" xpos 833 ypos 179 action Jump("mine_final2") focus_mask True
    imagebutton idle "backgrounds/bg_k_village_imagemap/bg_k_village_mountain_01.png" hover "mountain_hover" xpos 497 ypos 0 action Jump("mountain_final2") focus_mask True
    imagebutton idle "backgrounds/bg_k_village_imagemap/bg_k_village_school_01.png" hover "school_hover" xpos 663 ypos 389 action Jump("school_final2") focus_mask True
    imagebutton idle "backgrounds/bg_k_village_imagemap/bg_k_village_training_01.png" hover "training_hover" xpos 114 ypos 463 action Jump("train_final2") focus_mask True

image 2palace_hover = Animation("fbackgrounds/bg_a_city_imagemap/bg_a_palace_1.png", .2, "fbackgrounds/bg_a_city_imagemap/bg_a_palace_2.png", .2, "fbackgrounds/bg_a_city_imagemap/bg_a_palace_3.png", .2, "fbackgrounds/bg_a_city_imagemap/bg_a_palace_4.png", .2, "fbackgrounds/bg_a_city_imagemap/bg_a_palace_3.png", .2, "fbackgrounds/bg_a_city_imagemap/bg_a_palace_2.png", .2)
image 2fight_hover = Animation("fbackgrounds/bg_a_city_imagemap/bg_a_leavecity_1.png", .2, "fbackgrounds/bg_a_city_imagemap/bg_a_leavecity_2.png", .2, "fbackgrounds/bg_a_city_imagemap/bg_a_leavecity_3.png", .2, "fbackgrounds/bg_a_city_imagemap/bg_a_leavecity_4.png", .2, "fbackgrounds/bg_a_city_imagemap/bg_a_leavecity_3.png", .2, "fbackgrounds/bg_a_city_imagemap/bg_a_leavecity_2.png", .2)
image 2alley_hover = Animation("fbackgrounds/bg_a_city_imagemap/bg_a_alleys_1.png", .2, "fbackgrounds/bg_a_city_imagemap/bg_a_alleys_2.png", .2, "fbackgrounds/bg_a_city_imagemap/bg_a_alleys_3.png", .2, "fbackgrounds/bg_a_city_imagemap/bg_a_alleys_4.png", .2, "fbackgrounds/bg_a_city_imagemap/bg_a_alleys_3.png", .2, "fbackgrounds/bg_a_city_imagemap/bg_a_alleys_2.png", .2)
image 2armory_hover = Animation("fbackgrounds/bg_a_city_imagemap/bg_a_armory_1.png", .2, "fbackgrounds/bg_a_city_imagemap/bg_a_armory_2.png", .2, "fbackgrounds/bg_a_city_imagemap/bg_a_armory_3.png", .2, "fbackgrounds/bg_a_city_imagemap/bg_a_armory_4.png", .2, "fbackgrounds/bg_a_city_imagemap/bg_a_armory_3.png", .2, "fbackgrounds/bg_a_city_imagemap/bg_a_armory_2.png", .2)
image 2farm_hover = Animation("fbackgrounds/bg_a_city_imagemap/bg_a_farm_1.png", .2, "fbackgrounds/bg_a_city_imagemap/bg_a_farm_2.png", .2, "fbackgrounds/bg_a_city_imagemap/bg_a_farm_3.png", .2, "fbackgrounds/bg_a_city_imagemap/bg_a_farm_4.png", .2, "fbackgrounds/bg_a_city_imagemap/bg_a_farm_3.png", .2, "fbackgrounds/bg_a_city_imagemap/bg_a_farm_2.png", .2)
image 2prison_hover = Animation("fbackgrounds/bg_a_city_imagemap/bg_a_prison_1.png", .2, "fbackgrounds/bg_a_city_imagemap/bg_a_prison_2.png", .2, "fbackgrounds/bg_a_city_imagemap/bg_a_prison_3.png", .2, "fbackgrounds/bg_a_city_imagemap/bg_a_prison_4.png", .2, "fbackgrounds/bg_a_city_imagemap/bg_a_prison_3.png", .2, "fbackgrounds/bg_a_city_imagemap/bg_a_prison_2.png", .2)
image 2tavern_hover = Animation("fbackgrounds/bg_a_city_imagemap/bg_a_tavern_1.png", .2, "fbackgrounds/bg_a_city_imagemap/bg_a_tavern_2.png", .2, "fbackgrounds/bg_a_city_imagemap/bg_a_tavern_3.png", .2, "fbackgrounds/bg_a_city_imagemap/bg_a_tavern_4.png", .2, "fbackgrounds/bg_a_city_imagemap/bg_a_tavern_3.png", .2, "fbackgrounds/bg_a_city_imagemap/bg_a_tavern_2.png", .2)
image 2tower_hover = Animation("fbackgrounds/bg_a_city_imagemap/bg_a_tower_1.png", .2, "fbackgrounds/bg_a_city_imagemap/bg_a_tower_2.png", .2, "fbackgrounds/bg_a_city_imagemap/bg_a_tower_3.png", .2, "fbackgrounds/bg_a_city_imagemap/bg_a_tower_4.png", .2, "fbackgrounds/bg_a_city_imagemap/bg_a_tower_3.png", .2, "fbackgrounds/bg_a_city_imagemap/bg_a_tower_2.png", .2)
image 2training_hover = Animation("fbackgrounds/bg_a_city_imagemap/bg_a_training_1.png", .2, "fbackgrounds/bg_a_city_imagemap/bg_a_training_2.png", .2, "fbackgrounds/bg_a_city_imagemap/bg_a_training_3.png", .2, "fbackgrounds/bg_a_city_imagemap/bg_a_training_4.png", .2, "fbackgrounds/bg_a_city_imagemap/bg_a_training_3.png", .2, "fbackgrounds/bg_a_city_imagemap/bg_a_training_2.png", .2)


screen fday:
    add "fbackgrounds/bg_a_city_day.jpg"
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_palace_1.png" hover "2palace_hover" xpos 478 ypos 243 action Jump("2palace_day") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_leavecity_1.png" hover "2fight_hover" xpos 199 ypos 529 action Jump("2fight_day") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_alleys_1.png" hover "2alley_hover" xpos 292 ypos 127 action Jump("2alley_day") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_armory_1.png" hover "2armory_hover" xpos 574 ypos 559 action Jump("2armory_day") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_farm_1.png" hover "2farm_hover" xpos 692 ypos 93 action Jump("2farm_day") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_prison_1.png" hover "2prison_hover" xpos 760 ypos 391 action Jump("2prison_day") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_tavern_1.png" hover "2tavern_hover" xpos 77 ypos 198 action Jump("2tavern_day") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_tower_1.png" hover "2tower_hover" xpos 0 ypos 0 action Jump("2tower_day") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_training_1.png" hover "2training_hover" xpos 295 ypos 336 action Jump("2training_day") focus_mask True


screen fnight:
    add "fbackgrounds/bg_a_city_night.jpg"
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_palace_1.png" hover "2palace_hover" xpos 478 ypos 243 action Jump("2palace_night") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_leavecity_1.png" hover "2fight_hover" xpos 199 ypos 529 action Jump("2fight_night") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_alleys_1.png" hover "2alley_hover" xpos 292 ypos 127 action Jump("2alley_night") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_armory_1.png" hover "2armory_hover" xpos 574 ypos 559 action Jump("2armory_night") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_farm_1.png" hover "2farm_hover" xpos 692 ypos 93 action Jump("2farm_night") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_prison_1.png" hover "2prison_hover" xpos 760 ypos 391 action Jump("2prison_night") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_tavern_1.png" hover "2tavern_hover" xpos 77 ypos 198 action Jump("2tavern_night") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_tower_1.png" hover "2tower_hover" xpos 0 ypos 0 action Jump("2tower_night") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_training_1.png" hover "2training_hover" xpos 295 ypos 336 action Jump("2training_night") focus_mask True


screen fday1:
    add "fbackgrounds/bg_a_city_day.jpg"
    add "calender_and_money.png"
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_alleys_1.png" hover "2alley_hover" xpos 292 ypos 127 action Jump("falley_day1") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_armory_1.png" hover "2armory_hover" xpos 760 ypos 391 action Jump("farmory_day1") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_prison_1.png" hover "2prison_hover" xpos 574 ypos 559 action Jump("fprison_day1") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_tavern_1.png" hover "2tavern_hover" xpos 77 ypos 198 action Jump("ftavern_day1") focus_mask True
    hbox:
        xalign 0.6
        yalign 0.02
        text "[fmoney]"
    hbox:
        xalign 0.45
        yalign 0.02
        text "[fcalendar]"

screen fnight1:
    add "fbackgrounds/bg_a_city_night.jpg"
    add "calender_and_money.png"
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_alleys_1.png" hover "2alley_hover" xpos 292 ypos 127 action Jump("falley_night1") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_palace_1.png" hover "2palace_hover" xpos 478 ypos 243 action Jump("fpalace_night1") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_prison_1.png" hover "2prison_hover" xpos 574 ypos 559 action Jump("fprison_night1") focus_mask True
    hbox:
        xalign 0.6
        yalign 0.02
        text "[fmoney]"
    hbox:
        xalign 0.45
        yalign 0.02
        text "[fcalendar]"

screen fday2:
    add "fbackgrounds/bg_a_city_day.jpg"
    add "calender_and_money.png"
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_palace_1.png" hover "2palace_hover" xpos 478 ypos 243 action Jump("fpalace_day2") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_leavecity_1.png" hover "2fight_hover" xpos 199 ypos 529 action Jump("ffight_day2") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_alleys_1.png" hover "2alley_hover" xpos 292 ypos 127 action Jump("falley_day2") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_armory_1.png" hover "2armory_hover" xpos 760 ypos 391 action Jump("farmory_day2") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_farm_1.png" hover "2farm_hover" xpos 692 ypos 93 action Jump("ffarm_day2") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_prison_1.png" hover "2prison_hover" xpos 574 ypos 559 action Jump("fprison_day2") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_tavern_1.png" hover "2tavern_hover" xpos 77 ypos 198 action Jump("ftavern_day2") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_tower_1.png" hover "2tower_hover" xpos 0 ypos 0 action Jump("ftower_day2") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_training_1.png" hover "2training_hover" xpos 295 ypos 336 action Jump("ftraining_day2") focus_mask True
    hbox:
        xalign 0.6
        yalign 0.02
        text "[fmoney]"
    hbox:
        xalign 0.45
        yalign 0.02
        text "[fcalendar]"

screen fnight2:
    add "fbackgrounds/bg_a_city_night.jpg"
    add "calender_and_money.png"
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_palace_1.png" hover "2palace_hover" xpos 478 ypos 243 action Jump("fpalace_night2") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_leavecity_1.png" hover "2fight_hover" xpos 199 ypos 529 action Jump("ffight_night2") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_alleys_1.png" hover "2alley_hover" xpos 292 ypos 127 action Jump("falley_night2") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_armory_1.png" hover "2armory_hover" xpos 760 ypos 391 action Jump("farmory_night2") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_farm_1.png" hover "2farm_hover" xpos 692 ypos 93 action Jump("ffarm_night2") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_prison_1.png" hover "2prison_hover" xpos 574 ypos 559 action Jump("fprison_night2") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_tavern_1.png" hover "2tavern_hover" xpos 77 ypos 198 action Jump("ftavern_night2") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_tower_1.png" hover "2tower_hover" xpos 0 ypos 0 action Jump("ftower_night2") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_training_1.png" hover "2training_hover" xpos 295 ypos 336 action Jump("ftraining_night2") focus_mask True
    hbox:
        xalign 0.6
        yalign 0.02
        text "[fmoney]"
    hbox:
        xalign 0.45
        yalign 0.02
        text "[fcalendar]"

screen fday3:
    add "fbackgrounds/bg_a_city_day.jpg"
    add "calender_and_money.png"
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_palace_1.png" hover "2palace_hover" xpos 478 ypos 243 action Jump("fpalace_day3") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_leavecity_1.png" hover "2fight_hover" xpos 199 ypos 529 action Jump("ffight_day3") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_alleys_1.png" hover "2alley_hover" xpos 292 ypos 127 action Jump("falley_day2") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_armory_1.png" hover "2armory_hover" xpos 760 ypos 391 action Jump("farmory_day2") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_farm_1.png" hover "2farm_hover" xpos 692 ypos 93 action Jump("ffarm_day3") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_prison_1.png" hover "2prison_hover" xpos 574 ypos 559 action Jump("fprison_day3") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_tavern_1.png" hover "2tavern_hover" xpos 77 ypos 198 action Jump("ftavern_day2") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_tower_1.png" hover "2tower_hover" xpos 0 ypos 0 action Jump("ftower_day3") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_training_1.png" hover "2training_hover" xpos 295 ypos 336 action Jump("ftraining_day3") focus_mask True
    imagebutton idle "stats_button.png" hover "stats_button_dark.png" xpos 0.7 ypos 0 action [ Jump("stat_screen_fire_day")]
    hbox:
        xalign 0.6
        yalign 0.02
        text "[fmoney]"
    hbox:
        xalign 0.45
        yalign 0.02
        text "[fcalendar]"

screen fnight3:
    add "fbackgrounds/bg_a_city_night.jpg"
    add "calender_and_money.png"

    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_palace_1.png" hover "2palace_hover" xpos 478 ypos 243 action Jump("fpalace_night3") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_leavecity_1.png" hover "2fight_hover" xpos 199 ypos 529 action Jump("ffight_night3") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_alleys_1.png" hover "2alley_hover" xpos 292 ypos 127 action Jump("falley_night2") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_armory_1.png" hover "2armory_hover" xpos 760 ypos 391 action Jump("farmory_night2") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_farm_1.png" hover "2farm_hover" xpos 692 ypos 93 action Jump("ffarm_night3") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_prison_1.png" hover "2prison_hover" xpos 574 ypos 559 action Jump("fprison_night3") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_tavern_1.png" hover "2tavern_hover" xpos 77 ypos 198 action Jump("ftavern_night2") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_tower_1.png" hover "2tower_hover" xpos 0 ypos 0 action Jump("ftower_night3") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_training_1.png" hover "2training_hover" xpos 295 ypos 336 action Jump("ftraining_night3") focus_mask True
    imagebutton idle "stats_button.png" hover "stats_button_dark.png" xpos 0.7 ypos 0 action [ Jump("stat_screen_fire_night")]

    hbox:
        xalign 0.6
        yalign 0.02
        text "[fmoney]"
    hbox:
        xalign 0.45
        yalign 0.02
        text "[fcalendar]"

screen fnight4:
    add "fbackgrounds/bg_a_city_night.jpg"
    add "calender_and_money.png"

    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_tower_1.png" hover "2tower_hover" xpos 0 ypos 0 action Jump("ftower_night4") focus_mask True

    hbox:
        xalign 0.6
        yalign 0.02
        text "[fmoney]"
    hbox:
        xalign 0.45
        yalign 0.02
        text "[fcalendar]"

screen fnight5:
    add "fbackgrounds/bg_a_city_night.jpg"
    add "calender_and_money.png"

    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_palace_1.png" hover "2palace_hover" xpos 478 ypos 243 action Jump("fpalace_night5") focus_mask True

    hbox:
        xalign 0.6
        yalign 0.02
        text "[fmoney]"
    hbox:
        xalign 0.45
        yalign 0.02
        text "[fcalendar]"

screen fnight6:
    add "fbackgrounds/bg_a_city_night.jpg"
    add "calender_and_money.png"

    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_palace_1.png" hover "2palace_hover" xpos 478 ypos 243 action Jump("storm_palace") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_leavecity_1.png" hover "2fight_hover" xpos 199 ypos 529 action Jump("storm_palace") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_alleys_1.png" hover "2alley_hover" xpos 292 ypos 127 action Jump("storm_palace") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_armory_1.png" hover "2armory_hover" xpos 760 ypos 391 action Jump("storm_palace") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_farm_1.png" hover "2farm_hover" xpos 692 ypos 93 action Jump("storm_palace") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_prison_1.png" hover "2prison_hover" xpos 574 ypos 559 action Jump("storm_palace") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_tavern_1.png" hover "2tavern_hover" xpos 77 ypos 198 action Jump("storm_palace") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_tower_1.png" hover "2tower_hover" xpos 0 ypos 0 action Jump("storm_palace") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_training_1.png" hover "2training_hover" xpos 295 ypos 336 action Jump("storm_palace") focus_mask True

    hbox:
        xalign 0.6
        yalign 0.02
        text "[fmoney]"
    hbox:
        xalign 0.45
        yalign 0.02
        text "[fcalendar]"

screen fday10:
    add "fbackgrounds/bg_a_city_day.jpg"
    add "calender_and_money.png"

    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_palace_1.png" hover "2palace_hover" xpos 478 ypos 243 action Jump("fpalace_day10") focus_mask True

    hbox:
        xalign 0.6
        yalign 0.02
        text "[fmoney]"
    hbox:
        xalign 0.45
        yalign 0.02
        text "[fcalendar]"

screen fday11:
    add "fbackgrounds/bg_a_city_day.jpg"
    add "calender_and_money.png"

    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_tower_1.png" hover "2tower_hover" xpos 0 ypos 0 action Jump("tower_day10") focus_mask True

    hbox:
        xalign 0.6
        yalign 0.02
        text "[fmoney]"
    hbox:
        xalign 0.45
        yalign 0.02
        text "[fcalendar]"

screen zfday1:
    add "fbackgrounds/bg_a_city_day.jpg"


    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_armory_1.png" hover "2armory_hover" xpos 760 ypos 391 action Jump("zarmory1") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_palace_1.png" hover "2palace_hover" xpos 478 ypos 243 action Jump("zfpalace_day1") focus_mask True










screen fshop:
    add "calender_and_money.png"
    hbox:
        xalign 0.6
        yalign 0.02
        text "[fmoney]"
    hbox:
        xalign 0.45
        yalign 0.02
        text "[fcalendar]"

screen palace_select_day:
    add "fbackgrounds/bg_a_city_day.jpg"
    add "calender_and_money.png"
    imagebutton idle "buttons/hourglass_off.png" hover "buttons/hourglass_on.png" action Jump("city_night") focus_mask True
    imagebutton idle "buttons/throne_off.png" hover "buttons/throne_on.png" action Jump("throne_room_1") focus_mask True
    imagebutton idle "buttons/back_off.png" hover "buttons/back_on.png" action Jump("city") focus_mask True
    hbox:
        xalign 0.6
        yalign 0.02
        text "[fmoney]"
    hbox:
        xalign 0.45
        yalign 0.02
        text "[fcalendar]"


screen zfday2:
    add "fbackgrounds/bg_a_city_day.jpg"
    add "calender_and_money.png"
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_palace_1.png" hover "2palace_hover" xpos 478 ypos 243 action Jump("zfpalace_day1") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_leavecity_1.png" hover "2fight_hover" xpos 199 ypos 529 action Jump("zffight_day1") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_alleys_1.png" hover "2alley_hover" xpos 292 ypos 127 action Jump("zfalley_day1") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_armory_1.png" hover "2armory_hover" xpos 760 ypos 391 action Jump("zarmory1") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_farm_1.png" hover "2farm_hover" xpos 692 ypos 93 action Jump("zffarm_day1") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_prison_1.png" hover "2prison_hover" xpos 574 ypos 559 action Jump("zfprison_day1") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_tavern_1.png" hover "2tavern_hover" xpos 77 ypos 198 action Jump("zftavern_day1") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_tower_1.png" hover "2tower_hover" xpos 0 ypos 0 action Jump("zftower_day1") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_training_1.png" hover "2training_hover" xpos 295 ypos 336 action Jump("zftraining_day1") focus_mask True
    hbox:
        xalign 0.6
        yalign 0.02
        text "[fmoney]"
    hbox:
        xalign 0.45
        yalign 0.02
        text "[fcalendar]"

screen zfnight1:
    add "fbackgrounds/bg_a_city_night.jpg"
    add "calender_and_money.png"
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_palace_1.png" hover "2palace_hover" xpos 478 ypos 243 action Jump("zfpalace_night1") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_leavecity_1.png" hover "2fight_hover" xpos 199 ypos 529 action Jump("zffight_night1") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_alleys_1.png" hover "2alley_hover" xpos 292 ypos 127 action Jump("zfalley_night1") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_armory_1.png" hover "2armory_hover" xpos 760 ypos 391 action Jump("zfarmory_night1") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_farm_1.png" hover "2farm_hover" xpos 692 ypos 93 action Jump("zffarm_night1") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_prison_1.png" hover "2prison_hover" xpos 574 ypos 559 action Jump("zfprison_night1") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_tavern_1.png" hover "2tavern_hover" xpos 77 ypos 198 action Jump("zftavern_night1") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_tower_1.png" hover "2tower_hover" xpos 0 ypos 0 action Jump("zftower_night1") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_training_1.png" hover "2training_hover" xpos 295 ypos 336 action Jump("zftraining_night1") focus_mask True
    hbox:
        xalign 0.6
        yalign 0.02
        text "[fmoney]"
    hbox:
        xalign 0.45
        yalign 0.02
        text "[fcalendar]"

screen zfday20:
    add "fbackgrounds/bg_a_city_day.jpg"


    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_leavecity_1.png" hover "2fight_hover" xpos 199 ypos 529 action Jump("zffight_day20") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_palace_1.png" hover "2palace_hover" xpos 478 ypos 243 action Jump("zfpalace_day20") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_tower_1.png" hover "2tower_hover" xpos 0 ypos 0 action Jump("zftower_day20") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_tavern_1.png" hover "2tavern_hover" xpos 77 ypos 198 action Jump("zftavern_day20") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_alleys_1.png" hover "2alley_hover" xpos 292 ypos 127 action Jump("zfalley_day20") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_prison_1.png" hover "2prison_hover" xpos 574 ypos 559 action Jump("zfprison_day20") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_armory_1.png" hover "2armory_hover" xpos 760 ypos 391 action Jump("zfarmory_day20") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_training_1.png" hover "2training_hover" xpos 295 ypos 336 action Jump("zftraining_day20") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_farm_1.png" hover "2farm_hover" xpos 692 ypos 93 action Jump("zffarm_day20") focus_mask True




screen zfnight20:
    add "fbackgrounds/bg_a_city_night.jpg"


    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_palace_1.png" hover "2palace_hover" xpos 478 ypos 243 action Jump("zfpalace_night20") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_leavecity_1.png" hover "2fight_hover" xpos 199 ypos 529 action Jump("zffight_night20") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_alleys_1.png" hover "2alley_hover" xpos 292 ypos 127 action Jump("zfalley_night20") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_armory_1.png" hover "2armory_hover" xpos 760 ypos 391 action Jump("zfarmory_night20") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_farm_1.png" hover "2farm_hover" xpos 692 ypos 93 action Jump("zffarm_night20") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_prison_1.png" hover "2prison_hover" xpos 574 ypos 559 action Jump("zfprison_night20") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_tavern_1.png" hover "2tavern_hover" xpos 77 ypos 198 action Jump("zftavern_night20") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_tower_1.png" hover "2tower_hover" xpos 0 ypos 0 action Jump("zftower_night20") focus_mask True
    imagebutton idle "fbackgrounds/bg_a_city_imagemap/bg_a_training_1.png" hover "2training_hover" xpos 295 ypos 336 action Jump("zftraining_night20") focus_mask True



screen earth_money_date:
    add "calender_and_money.png"

    hbox:
        xalign 0.6
        yalign 0.02
        text "[emoney]"
    hbox:
        xalign 0.45
        yalign 0.02
        text "[ecalendar]"






init python:




    build.directory_name = "Four_Elements_Trainer_v.0.8.3c"




    build.executable_name = "Four Elements Trainer"



    build.include_update = False





























    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**.rpy', None)
    build.classify('**.txt', None)
    build.classify('**/thumbs.db', None)




    build.archive("scripts", "all")
    build.archive("images", "all")


    build.classify("game/**.rpy", "scripts")
    build.classify("game/**.rpyc", "scripts")


    build.classify("game/**.jpg", "images")
    build.classify("game/**.png", "images")
    build.classify("game/**.ogg", "images")
    build.classify("game/**.mp3", "images")
    build.classify("game/**.wav", "images")
    build.classify("game/**.txt", "images")




    build.documentation('*.html')
    build.documentation('*.txt')
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
