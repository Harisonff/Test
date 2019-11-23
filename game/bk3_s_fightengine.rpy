init:



    image bk3_girlhead_1ani:
        "bk3_fight/girl_head_1a.png"
        0.3
        "bk3_fight/girl_head_1.png"
        0.5
        "bk3_fight/girl_head_1a.png"
        0.3
        "bk3_fight/girl_head_1.png"
        4.5
        repeat

    image bk3_girlhead_2ani:
        "bk3_fight/girl_head_2a.png"
        0.3
        "bk3_fight/girl_head_2.png"
        0.5
        "bk3_fight/girl_head_2a.png"
        0.3
        "bk3_fight/girl_head_2.png"
        4.5
        repeat

    image bk3_girlhead_3ani:
        "bk3_fight/girl_head_3a.png"
        0.3
        "bk3_fight/girl_head_3.png"
        0.5
        "bk3_fight/girl_head_3a.png"
        0.3
        "bk3_fight/girl_head_3.png"
        4.5
        repeat

    image bk3_girlhead_4ani:
        "bk3_fight/girl_head_4a.png"
        0.3
        "bk3_fight/girl_head_4.png"
        0.5
        "bk3_fight/girl_head_4a.png"
        0.3
        "bk3_fight/girl_head_4.png"
        4.5
        repeat

    image bk3_girlhead_5ani:
        "bk3_fight/girl_head_5a.png"
        0.3
        "bk3_fight/girl_head_5.png"
        0.5
        "bk3_fight/girl_head_5a.png"
        0.3
        "bk3_fight/girl_head_5.png"
        4.5
        repeat

    image frape frape0 = "bk3_fight/frape0.png"
    image frape frape1 = "bk3_fight/frape1.png"
    image frape frape2 = "bk3_fight/frape2.png"
    image frape_analgape = "bk3_fight/frape2_gape.png"
    image frape_analoverlay = "bk3_fight/frape2_analoverlay.png"

    image frape_openpuss = "bk3_fight/frape1_pussopen.png"
    image frape_heldopenpuss = "bk3_fight/frape1_pussheldopen.png"
    image frape_pussoverlay = "bk3_fight/frape1_pussoverlay.png"
    image frape_dick = "bk3_fight/frape1_dick.png"
    image frape_dick2 = "bk3_fight/frape1_dick2.png"
    image frape2_dick2 = "bk3_fight/frape2_dick2.png"



    image bk3_nchainedgirl = LiveComposite(
    (1000, 720),
    (0, 0), "bk3_fight/nude_girl_1.png",
    (0, 0), "bk3_fight/girl_head_0.png",)

    image bk3_nchained_flipped = LiveComposite(
    (1000, 720),
    (0, 0), im.Flip("bk3_fight/nude_girl_1.png",horizontal=True),
    (-10, 0), "bk3_fight/girl_head_0.png",)



    image bk3_nudegirl = LiveComposite(
    (1000, 720),
    (0, 0), "bk3_fight/nude_girl_1.png",
    (0, 0), ConditionSwitch(        
        "bk3_girlhead == 'bk3_girlhead_1'", "bk3_fight/girl_head_1.png",
        "bk3_girlhead == 'bk3_girlhead_2'", "bk3_fight/girl_head_2.png",
        "bk3_girlhead == 'bk3_girlhead_3'", "bk3_fight/girl_head_3.png",
        "bk3_girlhead == 'bk3_girlhead_4'", "bk3_fight/girl_head_4.png",
        "bk3_girlhead == 'bk3_girlhead_5'", "bk3_fight/girl_head_5.png",),
    (0, 0), "bk3_fight/eyebrow_angry.png",   
    (0, 0), ConditionSwitch(
        "bk3_armor == 'level_00'", "bk3_fight/transparent.png",  
        "bk3_armor == 'level_05'", "bk3_fight/transparent.png",
        "bk3_armor == 'level_10'", "bk3_fight/transparent.png",
        "bk3_armor == 'level_15'", "bk3_fight/transparent.png",))

    image bk3_nude_flipped = LiveComposite(
    (1000, 720),
    (0, 0), im.Flip("bk3_fight/nude_girl_1.png",horizontal=True),
    (-10, 0), ConditionSwitch(        
        "bk3_girlhead == 'bk3_girlhead_1'", "bk3_fight/girl_head_1.png",
        "bk3_girlhead == 'bk3_girlhead_2'", "bk3_fight/girl_head_2.png",
        "bk3_girlhead == 'bk3_girlhead_3'", "bk3_fight/girl_head_3.png",
        "bk3_girlhead == 'bk3_girlhead_4'", "bk3_fight/girl_head_4.png",
        "bk3_girlhead == 'bk3_girlhead_5'", "bk3_fight/girl_head_5.png",),
    (-10, 0), "bk3_fight/eyebrow_angry.png",       
    (0, 0), ConditionSwitch(
        "bk3_armor == 'level_00'", "bk3_fight/transparent.png", 
        "bk3_armor == 'level_05'", "bk3_fight/transparent.png",
        "bk3_armor == 'level_10'", "bk3_fight/transparent.png",
        "bk3_armor == 'level_15'", "bk3_fight/transparent.png",))




    image bk3_earthgirl = LiveComposite(
    (1000, 720),
    (0, 0), "bk3_fight/nude_girl_1.png",
    (0, 0), ConditionSwitch(
        "bk3_girlhead == 'bk3_girlhead_1'", "bk3_fight/girl_head_1.png",
        "bk3_girlhead == 'bk3_girlhead_2'", "bk3_fight/girl_head_2.png",
        "bk3_girlhead == 'bk3_girlhead_3'", "bk3_fight/girl_head_3.png",
        "bk3_girlhead == 'bk3_girlhead_4'", "bk3_fight/girl_head_4.png",
        "bk3_girlhead == 'bk3_girlhead_5'", "bk3_fight/girl_head_5.png",),
    (0, 0), "bk3_fight/eyebrow_angry.png",       
    (0, 0), ConditionSwitch(
        "bk3_armor == 'level_00'", "bk3_fight/transparent.png",    
        "bk3_armor == 'level_05'", "bk3_fight/egirl1_armor_05.png",
        "bk3_armor == 'level_10'", "bk3_fight/egirl1_armor_10.png",
        "bk3_armor == 'level_15'", "bk3_fight/egirl1_armor_15.png",),
    (0, 0), ConditionSwitch(
        "bk3_mask == 'mask_01'", "bk3_fight/mask_1.png",    
        "bk3_mask == 'mask_02'", "bk3_fight/mask_2.png",
        "bk3_mask == 'mask_03'", "bk3_fight/mask_3.png",))

    image bk3_earthgirl_flipped = LiveComposite(
    (1000, 720),
    (0, 0), im.Flip("bk3_fight/nude_girl_1.png",horizontal=True),
    (-10, 0), ConditionSwitch(
        "bk3_girlhead == 'bk3_girlhead_1'", "bk3_fight/girl_head_1.png",
        "bk3_girlhead == 'bk3_girlhead_2'", "bk3_fight/girl_head_2.png",
        "bk3_girlhead == 'bk3_girlhead_3'", "bk3_fight/girl_head_3.png",
        "bk3_girlhead == 'bk3_girlhead_4'", "bk3_fight/girl_head_4.png",
        "bk3_girlhead == 'bk3_girlhead_5'", "bk3_fight/girl_head_5.png",),
    (-10, 0), "bk3_fight/eyebrow_angry.png",      
    (0, 0), ConditionSwitch(
        "bk3_armor == 'level_00'", "bk3_fight/transparent.png",    
        "bk3_armor == 'level_05'", im.Flip("bk3_fight/egirl1_armor_05.png",horizontal=True),
        "bk3_armor == 'level_10'", im.Flip("bk3_fight/egirl1_armor_10.png",horizontal=True),
        "bk3_armor == 'level_15'", im.Flip("bk3_fight/egirl1_armor_15.png",horizontal=True),),
    (-10, 0), ConditionSwitch(
        "bk3_mask == 'mask_01'", "bk3_fight/mask_1.png",    
        "bk3_mask == 'mask_02'", "bk3_fight/mask_2.png",
        "bk3_mask == 'mask_03'", "bk3_fight/mask_3.png",))



    image bk3_firegirl = LiveComposite(
    (1000, 720),
    (0, 0), "bk3_fight/nude_girl_1.png",
    (0, 0), ConditionSwitch(
        "bk3_girlhead == 'bk3_girlhead_1'", "bk3_fight/girl_head_1.png",
        "bk3_girlhead == 'bk3_girlhead_2'", "bk3_fight/girl_head_2.png",
        "bk3_girlhead == 'bk3_girlhead_3'", "bk3_fight/girl_head_3.png",
        "bk3_girlhead == 'bk3_girlhead_4'", "bk3_fight/girl_head_4.png",
        "bk3_girlhead == 'bk3_girlhead_5'", "bk3_fight/girl_head_5.png",),
    (0, 0), "bk3_fight/eyebrow_angry.png",       
    (0, 0), ConditionSwitch(
        "bk3_armor == 'level_00'", "bk3_fight/transparent.png",    
        "bk3_armor == 'level_05'", "bk3_fight/fgirl1_armor_05.png",
        "bk3_armor == 'level_10'", "bk3_fight/fgirl1_armor_10.png",
        "bk3_armor == 'level_15'", "bk3_fight/fgirl1_armor_15.png",),
    (0, 0), ConditionSwitch(
        "bk3_mask == 'mask_01'", "bk3_fight/mask_1.png",    
        "bk3_mask == 'mask_02'", "bk3_fight/mask_2.png",
        "bk3_mask == 'mask_03'", "bk3_fight/mask_3.png",))


    image bk3_firegirl_flipped = LiveComposite(
    (1000, 720),
    (0, 0), im.Flip("bk3_fight/nude_girl_1.png", horizontal=True),
    (-10, 0), ConditionSwitch(
        "bk3_girlhead == 'bk3_girlhead_1'", "bk3_fight/girl_head_1.png",
        "bk3_girlhead == 'bk3_girlhead_2'", "bk3_fight/girl_head_2.png",
        "bk3_girlhead == 'bk3_girlhead_3'", "bk3_fight/girl_head_3.png",
        "bk3_girlhead == 'bk3_girlhead_4'", "bk3_fight/girl_head_4.png",
        "bk3_girlhead == 'bk3_girlhead_5'", "bk3_fight/girl_head_5.png",),
    (-10, 0), "bk3_fight/eyebrow_angry.png",      
    (0, 0), ConditionSwitch(
        "bk3_armor == 'level_00'", "bk3_fight/transparent.png",    
        "bk3_armor == 'level_05'", im.Flip("bk3_fight/fgirl1_armor_05.png",horizontal=True),
        "bk3_armor == 'level_10'", im.Flip("bk3_fight/fgirl1_armor_10.png",horizontal=True),
        "bk3_armor == 'level_15'", im.Flip("bk3_fight/fgirl1_armor_15.png",horizontal=True),),
    (-10, 0), ConditionSwitch(
        "bk3_mask == 'mask_01'", "bk3_fight/mask_1.png",    
        "bk3_mask == 'mask_02'", "bk3_fight/mask_2.png",
        "bk3_mask == 'mask_03'", "bk3_fight/mask_3.png",))



    image bk3_watergirl = LiveComposite(
    (1000, 720),
    (0, 0), "bk3_fight/nude_girl_1.png",
    (0, 0), ConditionSwitch(
        "bk3_girlhead == 'bk3_girlhead_1'", "bk3_fight/girl_head_1.png",
        "bk3_girlhead == 'bk3_girlhead_2'", "bk3_fight/girl_head_2.png",
        "bk3_girlhead == 'bk3_girlhead_3'", "bk3_fight/girl_head_3.png",
        "bk3_girlhead == 'bk3_girlhead_4'", "bk3_fight/girl_head_4.png",
        "bk3_girlhead == 'bk3_girlhead_5'", "bk3_fight/girl_head_5.png",),
    (0, 0), "bk3_fight/eyebrow_angry.png",       
    (0, 0), ConditionSwitch(
        "bk3_armor == 'level_00'", "bk3_fight/transparent.png",  
        "bk3_armor == 'level_05'", "bk3_fight/wgirl1_armor_05.png",
        "bk3_armor == 'level_10'", "bk3_fight/wgirl1_armor_10.png",
        "bk3_armor == 'level_15'", "bk3_fight/wgirl1_armor_15.png",),
    (0, 0), ConditionSwitch(
        "bk3_mask == 'mask_01'", "bk3_fight/mask_1.png",
        "bk3_mask == 'mask_02'", "bk3_fight/mask_2.png",
        "bk3_mask == 'mask_03'", "bk3_fight/mask_3.png",))

    image bk3_watergirl_flipped = LiveComposite(
    (1000, 720),
    (0, 0), im.Flip("bk3_fight/nude_girl_1.png", horizontal=True),
    (-10, 0), ConditionSwitch(
        "bk3_girlhead == 'bk3_girlhead_1'", "bk3_fight/girl_head_1.png",
        "bk3_girlhead == 'bk3_girlhead_2'", "bk3_fight/girl_head_2.png",
        "bk3_girlhead == 'bk3_girlhead_3'", "bk3_fight/girl_head_3.png",
        "bk3_girlhead == 'bk3_girlhead_4'", "bk3_fight/girl_head_4.png",
        "bk3_girlhead == 'bk3_girlhead_5'", "bk3_fight/girl_head_5.png",),
    (-10, 0), "bk3_fight/eyebrow_angry.png",       
    (0, 0), ConditionSwitch(
        "bk3_armor == 'level_00'", "bk3_fight/transparent.png",   
        "bk3_armor == 'level_05'", im.Flip("bk3_fight/wgirl1_armor_05.png",horizontal=True),
        "bk3_armor == 'level_10'", im.Flip("bk3_fight/wgirl1_armor_10.png",horizontal=True),
        "bk3_armor == 'level_15'", im.Flip("bk3_fight/wgirl1_armor_15.png",horizontal=True),),
    (-10, 0), ConditionSwitch(
        "bk3_mask == 'mask_01'", "bk3_fight/mask_1.png",    
        "bk3_mask == 'mask_02'", "bk3_fight/mask_2.png",
        "bk3_mask == 'mask_03'", "bk3_fight/mask_3.png",))


    image bk3_badgermole = "bk3_fight/badgermole_1.png"
    image bk3_badgermole_flipped = im.Flip("bk3_fight/badgermole_1.png",horizontal=True)



    image bk3_ajalagirl = LiveComposite(
    (1000, 720),
    (-3, 0), ConditionSwitch(
        "bk3_armor == 'level_00'", "bk3_fight/transparent.png",  
        "bk3_armor == 'level_05'", "bk3_fight/bk3_ajalahead_hatdrop.png",
        "bk3_armor == 'level_10'", "bk3_fight/bk3_ajalahead_hatdrop.png",
        "bk3_armor == 'level_15'", "bk3_fight/bk3_ajalahead_hatdrop.png"),    
    (0, 0), "bk3_fight/ajala_girl_1.png",
    (0, 0), "bk3_fight/bk3_ajalahead_1.png",  
    (0, 0), ConditionSwitch(
        "bk3_armor == 'level_00'", "bk3_fight/transparent.png",  
        "bk3_armor == 'level_05'", "bk3_fight/ajala1_armor_05.png",
        "bk3_armor == 'level_10'", "bk3_fight/ajala1_armor_10.png",
        "bk3_armor == 'level_15'", "bk3_fight/ajala1_armor_15.png"),
    (0, 0), "bk3_fight/ajala_braid.png",
    
    )

    image bk3_ajalagirl_flipped = LiveComposite(
    (1000, 720),
    (0, 0), ConditionSwitch(
        "bk3_armor == 'level_00'", "bk3_fight/transparent.png",  
        "bk3_armor == 'level_05'", "bk3_fight/bk3_ajalahead_hatdrop.png",
        "bk3_armor == 'level_10'", "bk3_fight/bk3_ajalahead_hatdrop.png",
        "bk3_armor == 'level_15'", "bk3_fight/bk3_ajalahead_hatdrop.png"),    
    (0, 0), im.Flip("bk3_fight/ajala_girl_1.png",horizontal = True),
    (-2, 0), "bk3_fight/bk3_ajalahead_1.png",  
    (0, 0), ConditionSwitch(
        "bk3_armor == 'level_00'", "bk3_fight/transparent.png",  
        "bk3_armor == 'level_05'", im.Flip("bk3_fight/ajala1_armor_05.png", horizontal=True),
        "bk3_armor == 'level_10'", im.Flip("bk3_fight/ajala1_armor_10.png", horizontal=True),
        "bk3_armor == 'level_15'", im.Flip("bk3_fight/ajala1_armor_15.png", horizontal=True)), 
    (-2, 0), "bk3_fight/ajala_braid.png",
    )



    image bk3_sewercrab = "bk3_fight/sewercrab.png"
    image bk3_sewercrab_flipped = im.Flip("bk3_fight/sewercrab.png",horizontal=True)

    image sewercrab:
        "bk3_sewercrab"
        1.5
        "bk3_sewercrab_flipped"
        1.5
        repeat

    image ajalagirl:
        "bk3_ajalagirl"
        1.5
        "bk3_ajalagirl_flipped"
        1.5
        repeat






    image ncgirl:
        "bk3_nchainedgirl"
        1.5
        "bk3_nchained_flipped"
        1.5
        repeat

    image ngirl:
        "bk3_nudegirl"
        1.5
        "bk3_nude_flipped"
        1.5
        repeat

    image egirl:
        "bk3_earthgirl"
        1.5
        "bk3_earthgirl_flipped"
        1.5
        repeat

    image fgirl:
        "bk3_firegirl"
        1.5
        "bk3_firegirl_flipped"
        1.5
        repeat

    image wgirl:
        "bk3_watergirl"
        1.5
        "bk3_watergirl_flipped"
        1.5
        repeat

    image bmole:
        "bk3_badgermole"
        1.5
        "bk3_badgermole_flipped"
        1.5
        repeat

    image bk3_aa = "bk3_fight/bk3_aa.png"
    image bk3_aa_flipped = im.Flip("bk3_fight/bk3_aa.png",horizontal=True)

    image bk3_green_monster:
        "bk3_aa"
        1.5
        "bk3_aa_flipped"
        1.5
        repeat





    image fire_attack = "bk3_fight/fire_attack.png"
    image fire_attack_spread = "bk3_fight/fire_attack_spread.png"

    image earth_attack = "bk3_fight/earth_attack.png"
    image earth_attack_spread = "bk3_fight/earth_attack_spread.png"

    image water_attack = "bk3_fight/water_attack.png"
    image water_attack_spread = "bk3_fight/water_attack_spread.png"





label bk3_start_the_fight:





    $ bk3_enemy_life_start = 90
    $ bk3_enemy_life = bk3_enemy_life_start
    $ bk3_enemy_attack = 10
    $ bk3_fuckable = True





    $ bk3_takes_damage = False
    $ bk3_armor = "level_15"
    $ bk3_enemy_type = renpy.random.choice(['water', 'fire', 'earth'])
    $ bk3_attack_bonus = 0
    $ bk3_enemy_firststrike = False
    $ bk3_attacktype = "human_slash"

    $ bk3_enemy_attack_chance = "mediocre"
    $ bk3_player_attack_chance = "mediocre"

    $ bk3_girlhead = renpy.random.choice(['bk3_girlhead_1', 'bk3_girlhead_2', 'bk3_girlhead_3', 'bk3_girlhead_4','bk3_girlhead_5'])
    $ bk3_mask = renpy.random.choice(['mask_01', 'mask_02', 'mask_03'])

    $ bk3_attack_type = "fire"






    if bk3_enemy_type == "water":
        $ bk3_current_enemy = "wgirl"

    if bk3_enemy_type == "fire":
        $ bk3_current_enemy = "fgirl"

    if bk3_enemy_type == "earth":
        $ bk3_current_enemy = "egirl"




    image bk3_current_enemy_attack = LiveComposite(
    (1000, 720),
    (0, 0), ConditionSwitch(
        "bk3_attacktype == 'human_slash'",      "bk3_fight/generic_enemy_attack.png",
        "bk3_attacktype == 'badgermole_slash'", "bk3_fight/badgermole_attack.png",))


    jump bk3_final_fighttweaks





label bk3_final_fighttweaks:

    if maze_follower == "prisonbitch":
        jin "I think I'll just stand over there where it's safe. Good luck though!"

    if maze_follower == "prisonthighs":
        ty "Ah... I'll just get out of your way and stand waaay over there. Happy hunting!"








    if current_room == room2:
        $ bk3_enemy_level = 2
        $ bk3_enemy_life_start = 90
        $ bk3_enemy_life = bk3_enemy_life_start
        $ bk3_enemy_attack = 10
        if bk3_enemy_level > bk3_level:
            $ bk3_enemy_firststrike = True

    if current_room == room3:
        $ bk3_enemy_level = 2
        $ bk3_enemy_life_start = 90
        $ bk3_enemy_life = bk3_enemy_life_start
        $ bk3_enemy_attack = 10
        if bk3_enemy_level > bk3_level:
            $ bk3_enemy_firststrike = True


    if current_room ==room8:
        $ bk3_enemy_level = 5
        $ bk3_enemy_life_start = 120
        $ bk3_enemy_life = bk3_enemy_life_start
        $ bk3_enemy_attack = 15
        if bk3_enemy_level > bk3_level:
            $ bk3_enemy_firststrike = True

        if bk3_enemy_level == 10:
            $ bk3_enemy_level = 10
            $ bk3_enemy_life_start = 10
            $ bk3_enemy_life = bk3_enemy_life_start
            $ bk3_enemy_attack = 30
            if bk3_enemy_level > bk3_level:
                $ bk3_enemy_firststrike = True


    if current_room == room9:
        "Hahaha! I'll have you know I'm a goddess at evading attacks!"
        $ bk3_player_attack_chance = "none"

    elif current_room == room11:

        $ bk3_current_enemy = "ncgirl"
        $ bk3_fuckable = False

    elif current_room == room23:
        $ bk3_enemy_level = 5
        $ bk3_enemy_life_start = 120
        $ bk3_enemy_life = bk3_enemy_life_start
        $ bk3_enemy_attack = 15
        if bk3_enemy_level > bk3_level:
            $ bk3_enemy_firststrike = True

    elif current_room == room25:
        $ bk3_girlhead = 'bk3_girlhead_1'
        $ bk3_current_enemy = "ngirl"
        $ bk3_enemy_level = 10
        $ bk3_enemy_life_start = 150
        $ bk3_enemy_life = bk3_enemy_life_start
        $ bk3_enemy_attack = 20
        if bk3_enemy_level > bk3_level:
            $ bk3_enemy_firststrike = True

    elif current_room == room26:
        $ bk3_girlhead = 'bk3_girlhead_2'
        $ bk3_enemy_type == "water"
        $ bk3_current_enemy = "wgirl"
        $ bk3_enemy_life_start += bk3_enemy_life_start
        $ bk3_enemy_life = bk3_enemy_life_start

    if current_room.roomnr >= 38 and current_room.roomnr <= 51:

        $ bk3_current_enemy = "bmole"
        $ bk3_enemy_type = "earth"
        $ bk3_enemy_life_start = 100
        $ bk3_enemy_life = 100
        $ bk3_attacktype = 'badgermole_slash'

    elif current_room.roomnr == 56:
        $ bk3_enemy_level = 10
        $ bk3_enemy_life_start = 150
        $ bk3_enemy_life = bk3_enemy_life_start
        $ bk3_enemy_attack = 20
        if bk3_enemy_level > bk3_level:
            $ bk3_enemy_firststrike = True

    elif current_room == room59:
        $ bk3_enemy_level = 5
        $ bk3_enemy_life_start = 120
        $ bk3_enemy_life = bk3_enemy_life_start
        $ bk3_enemy_attack = 15
        if bk3_enemy_level > bk3_level:
            $ bk3_enemy_firststrike = True

    if current_room.roomnr == 90:
        $ bk3_current_enemy = "bmole"
        $ bk3_enemy_type = "earth"
        $ bk3_enemy_life_start = 200
        $ bk3_enemy_life = bk3_enemy_life_start
        $ bk3_enemy_attack = 20
        if bk3_enemy_level > bk3_level:
            $ bk3_enemy_firststrike = True
        $ bk3_attacktype = 'badgermole_slash'

    elif current_room.roomnr == 107:
        $ bk3_enemy_level = 15
        $ bk3_enemy_life_start = 180
        $ bk3_enemy_life = bk3_enemy_life_start
        $ bk3_enemy_attack = 20
        if bk3_enemy_level > bk3_level:
            $ bk3_enemy_firststrike = True



    if current_room.roomnr == 107:

        $ bk3_current_enemy = "ajalagirl"
        $ bk3_enemy_level = 20
        $ bk3_enemy_type = "earth"
        $ bk3_enemy_life_start = 210
        $ bk3_enemy_life = bk3_enemy_life_start
        $ bk3_enemy_attack = 25
        $ bk3_attacktype = 'human_slash'
        $ bk3_fuckable = False

    if current_room.roomnr == 109:

        $ bk3_current_enemy = "sewercrab"
        $ bk3_enemy_type = "water"
        $ bk3_enemy_life_start = 444
        $ bk3_enemy_life = 444
        $ bk3_attacktype = 'human_slash'
        $ bk3_fuckable = False









    show expression "maze/black50.png"


    $ bk3_ypos_lifebar_enemy  = 0

    if current_room.roomnr == 25 and suki_loose and not suki_free:
        show tosi tosi100_1:
            xpos -270
        y "suki! it's about fucking time!"
        y "where did you get this outfit?"
        suki "i found where you hid my kyoshi clothing!"
        y "yoshi? like the retarded dragon?"
        suki "the kyoshi are a proud line of female warriors!"
        suki "so you stay away from me, long!"
        y "....long?"
        suki "you won't fool me, long feng!"
        y "wait... i just realized... his first name is \"long\"?"
        y "yeah, i'm not calling him that."
        y "dude is clearly over-compensating."
        suki "i will beat you off, long!"
        y "...i mean, you know how that sounds, right?"
        suki "die!"
        ya "fine, if I have to fight you to sober you up, i will."
        y "you're gonna come down hard girl."
        $ bk3_enemy_type = 'earth'
    else:
        show expression bk3_current_enemy
    show screen bk3_lifebars  

    $ maze_music_on = False
    stop music fadeout 1
    play music "audio/Prelude and Action.mp3"


    if bk3_enemy_firststrike:
        jump bk3_enemy_turn
    else:

        call screen bk3_fighting_interface







































label zomzom:
    "text"
    call screen bk3_fighting_interface

screen bk3_fighting_interface:

    imagemap:



        ground "bk3_fight/generic_background.png"
        hover "bk3_fight/attack_on.png"
        idle "bk3_fight/attack_off.png"

        if not maze_fight_tutorial:
            add "bk3_fight/attack_off.png"

        if maze_fight_tutorial:
            if bk3_lifepotions >= 1:
                hotspot (75, 279, 120, 120) action [SetVariable("bk3_attack_type","bk3_lifepotion"),   Jump("bk3_players_turn")]
                text "{b}[bk3_lifepotions]" xpos 172 ypos 283

            if bk3_manapotions >= 1:
                hotspot (75, 151, 120, 120) action [SetVariable("bk3_attack_type","bk3_manapotion"),   Jump("bk3_players_turn")]
                text "{b}[bk3_manapotions]" xpos 172 ypos 157

            if bk3_allow_firebending == True and bk3_fire_remaining >0:
                hotspot (77, 612, 90, 104) action [SetVariable("bk3_attack_type","fire"),             Jump("bk3_players_turn")]
                hotspot (170, 614, 111, 103) action [SetVariable("bk3_attack_type","fire_spread"),      Jump("bk3_players_turn")]
                text "{color=#ffffff}[bk3_fire_remaining]/[bk3_moves]" xpos 60 ypos 620

            if bk3_allow_waterbending == True and bk3_water_remaining >0:
                hotspot (76, 507, 93, 99) action [SetVariable("bk3_attack_type","water")       ,     Jump("bk3_players_turn")]
                hotspot (169, 507, 109, 102) action [SetVariable("bk3_attack_type","water_spread"),     Jump("bk3_players_turn")]
                text "{color=#ffffff}[bk3_water_remaining]/[bk3_moves]" xpos 60 ypos 510

            if bk3_allow_earthbending == True:
                hotspot (76, 398, 93, 107) action [SetVariable("bk3_attack_type","earth"),            Jump("bk3_players_turn")]
                hotspot (168, 395, 116, 111) action [SetVariable("bk3_attack_type","earth_spread"),     Jump("bk3_players_turn")]
                text "{color=#ffffff}{image=infinity1.png}" xpos 60 ypos 400



        if maze_tutorial1:
            add "bk3_fight/maze_tutorial1.png"

        if maze_tutorial2:
            add "bk3_fight/maze_tutorial2.png"

        if maze_tutorial3:
            add "bk3_fight/maze_tutorial3.png"


screen bk3_lifebars:

    add "bk3_fight/lifebar.png"

    add "bk3_fight/lifebar_player.png":
        ypos bk3_ypos_lifebar_player

    add "bk3_fight/lifebar_enemy.png":
        ypos bk3_ypos_lifebar_enemy

    text "{color=#ffffff}[bk3_enemy_life]" xpos 920 ypos 370
    text "{color=#ffffff}[bk3_player_life]" xpos 10 ypos 350
    text "{color=#ffffff}Level [bk3_enemy_level]" xpos 450 ypos 10












label bk3_players_turn:

    if bk3_accuracy == 1:
        $ rand_accuracy = WeightedChoice([("low", 0.90), ("mediocre", 0.10)])
        if rand_accuracy == "low":
            $ bk3_player_attack_chance == "low"
        if rand_accuracy == "mediocre":
            $ bk3_player_attack_chance == "mediocre"

    if bk3_accuracy ==2:
        $ rand_accuracy = WeightedChoice([("low", 0.80), ("mediocre", 0.20)])
        if rand_accuracy == "low":
            $ bk3_player_attack_chance == "low"
        if rand_accuracy == "mediocre":
            $ bk3_player_attack_chance == "mediocre"

    if bk3_accuracy == 3:
        $ rand_accuracy = WeightedChoice([("low", 0.70), ("mediocre", 0.30)])
        if rand_accuracy == "low":
            $ bk3_player_attack_chance == "low"
        if rand_accuracy == "mediocre":
            $ bk3_player_attack_chance == "mediocre"

    if bk3_accuracy ==4:
        $ rand_accuracy = WeightedChoice([("low", 0.60), ("mediocre", 0.40)])
        if rand_accuracy == "low":
            $ bk3_player_attack_chance == "low"
        if rand_accuracy == "mediocre":
            $ bk3_player_attack_chance == "mediocre"

    if bk3_accuracy ==5:
        $ rand_accuracy = WeightedChoice([("low", 0.50), ("mediocre", 0.50)])
        if rand_accuracy == "low":
            $ bk3_player_attack_chance == "low"
        if rand_accuracy == "mediocre":
            $ bk3_player_attack_chance == "mediocre"

    if bk3_accuracy ==6:
        $ rand_accuracy = WeightedChoice([("low", 0.40), ("mediocre", 0.60)])
        if rand_accuracy == "low":
            $ bk3_player_attack_chance == "low"
        if rand_accuracy == "mediocre":
            $ bk3_player_attack_chance == "mediocre"

    if bk3_accuracy ==7:
        $ rand_accuracy = WeightedChoice([("low", 0.30), ("mediocre", 0.70)])
        if rand_accuracy == "low":
            $ bk3_player_attack_chance == "low"
        if rand_accuracy == "mediocre":
            $ bk3_player_attack_chance == "mediocre"

    if bk3_accuracy ==8:
        $ rand_accuracy = WeightedChoice([("low", 0.20), ("mediocre", 0.80)])
        if rand_accuracy == "low":
            $ bk3_player_attack_chance == "low"
        if rand_accuracy == "mediocre":
            $ bk3_player_attack_chance == "mediocre"

    if bk3_accuracy ==9:
        $ rand_accuracy = WeightedChoice([("low", 0.10), ("mediocre", 0.90)])
        if rand_accuracy == "low":
            $ bk3_player_attack_chance == "low"
        if rand_accuracy == "mediocre":
            $ bk3_player_attack_chance == "mediocre"

    if bk3_accuracy ==10:
        $ rand_accuracy = WeightedChoice([("mediocre", 0.90), ("high", 0.10)])
        if rand_accuracy == "mediocre":
            $ bk3_player_attack_chance == "mediocre"
        if rand_accuracy == "high":
            $ bk3_player_attack_chance == "high"

    if bk3_accuracy >=11:
        $ rand_accuracy = WeightedChoice([("mediocre", 0.80), ("high", 0.20)])
        if rand_accuracy == "mediocre":
            $ bk3_player_attack_chance == "mediocre"
        if rand_accuracy == "high":
            $ bk3_player_attack_chance == "high"

    if bk3_accuracy ==12:
        $ rand_accuracy = WeightedChoice([("mediocre", 0.70), ("high", 0.30)])
        if rand_accuracy == "mediocre":
            $ bk3_player_attack_chance == "mediocre"
        if rand_accuracy == "high":
            $ bk3_player_attack_chance == "high"

    if bk3_accuracy == 13:
        $ rand_accuracy = WeightedChoice([("mediocre", 0.60), ("high", 0.40)])
        if rand_accuracy == "mediocre":
            $ bk3_player_attack_chance == "mediocre"
        if rand_accuracy == "high":
            $ bk3_player_attack_chance == "high"

    if bk3_accuracy ==14:
        $ rand_accuracy = WeightedChoice([("mediocre", 0.50), ("high", 0.50)])
        if rand_accuracy == "mediocre":
            $ bk3_player_attack_chance == "mediocre"
        if rand_accuracy == "high":
            $ bk3_player_attack_chance == "high"

    if bk3_accuracy ==15:
        $ rand_accuracy = WeightedChoice([("mediocre", 0.40), ("high", 0.60)])
        if rand_accuracy == "mediocre":
            $ bk3_player_attack_chance == "mediocre"
        if rand_accuracy == "high":
            $ bk3_player_attack_chance == "high"

    if bk3_accuracy ==16:
        $ rand_accuracy = WeightedChoice([("mediocre", 0.30), ("high", 0.70)])
        if rand_accuracy == "mediocre":
            $ bk3_player_attack_chance == "mediocre"
        if rand_accuracy == "high":
            $ bk3_player_attack_chance == "high"

    if bk3_accuracy ==17:
        $ rand_accuracy = WeightedChoice([("mediocre", 0.25), ("high", 0.75)])
        if rand_accuracy == "mediocre":
            $ bk3_player_attack_chance == "mediocre"
        if rand_accuracy == "high":
            $ bk3_player_attack_chance == "high"

    if bk3_accuracy ==18:
        $ rand_accuracy = WeightedChoice([("mediocre", 0.20), ("high", 0.80)])
        if rand_accuracy == "mediocre":
            $ bk3_player_attack_chance == "mediocre"
        if rand_accuracy == "high":
            $ bk3_player_attack_chance == "high"

    if bk3_accuracy ==19:
        $ rand_accuracy = WeightedChoice([("mediocre", 0.15), ("high", 0.85)])
        if rand_accuracy == "mediocre":
            $ bk3_player_attack_chance == "mediocre"
        if rand_accuracy == "high":
            $ bk3_player_attack_chance == "high"

    if bk3_accuracy ==20:
        $ rand_accuracy = WeightedChoice([("mediocre", 0.10), ("high", 0.90)])
        if rand_accuracy == "mediocre":
            $ bk3_player_attack_chance == "mediocre"
        if rand_accuracy == "high":
            $ bk3_player_attack_chance == "high"

    if bk3_accuracy >=21:
        $ rand_accuracy = WeightedChoice([("high", 0.90), ("ultimate", 0.10)])
        if rand_accuracy == "high":
            $ bk3_player_attack_chance == "high"
        if rand_accuracy == "ultimate":
            $ bk3_player_attack_chance == "ultimate"

    if bk3_accuracy ==22:
        $ rand_accuracy = WeightedChoice([("high", 0.80), ("ultimate", 0.20)])
        if rand_accuracy == "high":
            $ bk3_player_attack_chance == "high"
        if rand_accuracy == "ultimate":
            $ bk3_player_attack_chance == "ultimate"

    if bk3_accuracy == 23:
        $ rand_accuracy = WeightedChoice([("high", 0.70), ("ultimate", 0.30)])
        if rand_accuracy == "high":
            $ bk3_player_attack_chance == "high"
        if rand_accuracy == "ultimate":
            $ bk3_player_attack_chance == "ultimate"

    if bk3_accuracy ==24:
        $ rand_accuracy = WeightedChoice([("high", 0.60), ("ultimate", 0.40)])
        if rand_accuracy == "high":
            $ bk3_player_attack_chance == "high"
        if rand_accuracy == "ultimate":
            $ bk3_player_attack_chance == "ultimate"

    if bk3_accuracy ==25:
        $ rand_accuracy = WeightedChoice([("high", 0.50), ("ultimate", 0.50)])
        if rand_accuracy == "high":
            $ bk3_player_attack_chance == "high"
        if rand_accuracy == "ultimate":
            $ bk3_player_attack_chance == "ultimate"

    if bk3_accuracy ==26:
        $ rand_accuracy = WeightedChoice([("high", 0.40), ("ultimate", 0.60)])
        if rand_accuracy == "high":
            $ bk3_player_attack_chance == "high"
        if rand_accuracy == "ultimate":
            $ bk3_player_attack_chance == "ultimate"

    if bk3_accuracy ==27:
        $ rand_accuracy = WeightedChoice([("high", 0.30), ("ultimate", 0.7)])
        if rand_accuracy == "high":
            $ bk3_player_attack_chance == "high"
        if rand_accuracy == "ultimate":
            $ bk3_player_attack_chance == "ultimate"

    if bk3_accuracy ==28:
        $ rand_accuracy = WeightedChoice([("high", 0.20), ("ultimate", 0.80)])
        if rand_accuracy == "high":
            $ bk3_player_attack_chance == "high"
        if rand_accuracy == "ultimate":
            $ bk3_player_attack_chance == "ultimate"

    if bk3_accuracy ==29:
        $ rand_accuracy = WeightedChoice([("high", 0.10), ("ultimate", 0.9)])
        if rand_accuracy == "high":
            $ bk3_player_attack_chance == "high"
        if rand_accuracy == "ultimate":
            $ bk3_player_attack_chance == "ultimate"

    if bk3_accuracy ==30:
        $ rand_accuracy = "ultimate"
        $ bk3_player_attack_chance == "ultimate"



    if bk3_player_attack_chance == "none":
        $ rand_attack = renpy.random.choice(['miss'])

    elif bk3_player_attack_chance == "low":
        $ rand_attack = renpy.random.choice(['hit', 'miss', 'miss', 'miss'])

    elif bk3_player_attack_chance == "mediocre":
        $ rand_attack = renpy.random.choice(['hit','hit', 'miss'])

    elif bk3_player_attack_chance == "high":
        $ rand_attack = renpy.random.choice(['hit','hit','hit', 'miss'])

    elif bk3_player_attack_chance == "ultimate":
        $ rand_attack = renpy.random.choice(['hit'])




    if rand_attack == 'miss':
        $ bk3_takes_damage = False
        if current_room.roomnr == 25 and suki_loose and not suki_free:
            hide tosi tosi100_1
            show tosi tosi100_1
            play sound "audio/knife.wav"
        else:
            hide bk3_current_enemy
            show expression bk3_current_enemy:
                xpos 300
        $ renpy.pause(0.2)
    else:

        $ bk3_takes_damage = True


    if bk3_attack_type == "fire_spread" or bk3_attack_type == "water_spread" or bk3_attack_type == "earth_spread":
        $ rand_attack = 'hit'
        $ bk3_takes_damage = True









    if bk3_attack_type == "fire":
        play sound "audio/firewall.mp3"
        show fire_attack
        $ renpy.pause(0.7)
        hide fire_attack
        $ bk3_fire_remaining -=1

    elif bk3_attack_type == "fire_spread":
        play sound "audio/firewall.mp3"
        show fire_attack_spread
        $ renpy.pause(0.7)
        hide fire_attack_spread
        $ bk3_fire_remaining -=1


    elif bk3_attack_type == "water":
        play sound "audio/water_splash.mp3"
        show water_attack
        $ renpy.pause(0.7)
        hide water_attack
        $ bk3_water_remaining -=1


    elif bk3_attack_type == "water_spread":
        play sound "audio/water_splash.mp3"
        show water_attack_spread
        $ renpy.pause(0.7)
        hide water_attack_spread
        $ bk3_water_remaining -=1


    elif bk3_attack_type == "earth":
        show earth_attack
        play sound "audio/rock_crumble.mp3"

        $ renpy.pause(0.7)
        hide earth_attack


    elif bk3_attack_type == "earth_spread":
        show earth_attack_spread
        play sound "audio/rock_crumble.mp3"

        $ renpy.pause(0.7)
        hide earth_attack_spread

    elif bk3_attack_type == "bk3_lifepotion":
        if bk3_lifepotions >= 1:
            if bk3_hp <= 100:
                $ bk3_player_life += 60

            if bk3_hp >= 101 and bk3_hp <150:
                $ bk3_player_life += 80

            if bk3_hp >= 150 and bk3_hp <200:
                $ bk3_player_life += 100

            if bk3_hp >= 200:
                $ bk3_player_life += 120

            if bk3_player_life > bk3_player_life_start:
                $ bk3_player_life = bk3_player_life_start

            $ bk3_lifepotions = bk3_lifepotions - 1
            "you used a life potion!"
            "You have [bk3_lifepotions] life potions left!"

            call bk3_calculate_lifebar_positions from _call_bk3_calculate_lifebar_positions

            if current_room.roomnr == 25 and suki_loose and not suki_free:
                hide tosi tosi100_1
                show tosi tosi100_1:
                    xpos -270
            else:
                hide bk3_current_enemy
                show expression bk3_current_enemy

            jump bk3_enemy_turn
        else:
            "You don't have any lifepotions left!"

            if current_room.roomnr == 25 and suki_loose and not suki_free:
                hide tosi tosi100_1
                show tosi tosi100_1:
                    xpos -270
            else:
                hide bk3_current_enemy
                show expression bk3_current_enemy


            if bk3_allow_waterbending == False and bk3_allow_firebending == False and  bk3_allow_earthbending == False:
                jump bk3_enemy_turn

            call screen bk3_fighting_interface

    elif bk3_attack_type == "bk3_manapotion":
        if bk3_manapotions >= 1:
            $ bk3_fire_remaining = bk3_moves
            $ bk3_water_remaining = bk3_moves

            $ bk3_manapotions -= 1
            "you used a mana potion!"
            "You have [bk3_manapotions] mana potions left!"
            if current_room.roomnr == 25 and suki_loose and not suki_free:
                hide tosi tosi100_1
                show tosi tosi100_1:
                    xpos -270
            else:
                hide bk3_current_enemy
                show expression bk3_current_enemy

            jump bk3_enemy_turn
        else:
            "You don't have any mana potions left!"

            if current_room.roomnr == 25 and suki_loose and not suki_free:
                hide tosi tosi100_1
                show tosi tosi100_1:
                    xpos -270
            else:
                hide bk3_current_enemy
                show expression bk3_current_enemy


            if bk3_allow_waterbending == False and bk3_allow_firebending == False and  bk3_allow_earthbending == False:
                jump bk3_enemy_turn

            call screen bk3_fighting_interface
    else:

        jump bk3_enemy_turn











    if current_room.roomnr == 25 and suki_loose and not suki_free:
        hide tosi tosi100_1
        show tosi tosi100_1:
            xpos -270
    else:
        hide bk3_current_enemy
        show expression bk3_current_enemy




    jump dealing_with_damage_etc












label dealing_with_damage_etc:

    call bk3_calculate_your_attack_bonus from _call_bk3_calculate_your_attack_bonus

    if bk3_takes_damage == False:
        jump bk3_enemy_turn

    elif bk3_attack_type == "fire_spread" or bk3_attack_type == "water_spread" or bk3_attack_type == "earth_spread":
        $ bk3_enemy_life = bk3_enemy_life - ((bk3_player_attack/3)+ bk3_attack_bonus)
    else:

        $ bk3_enemy_life = bk3_enemy_life - (bk3_player_attack + bk3_attack_bonus)










    if bk3_enemy_life >=(bk3_enemy_life_start - 20):
        $ bk3_armor = 'level_15'

    elif bk3_enemy_life >=(bk3_enemy_life_start/3):
        $ bk3_armor = 'level_10'

    elif bk3_enemy_life >=(bk3_enemy_life_start/4):
        $ bk3_armor = 'level_05'

    elif bk3_enemy_life <=(bk3_enemy_life_start/5):
        $ bk3_armor = 'level_00'


    if current_room.roomnr == 25 and suki_loose and not suki_free:
        show tosi tosi100_1:
            xpos -270
        with hpunch
    else:

        show expression bk3_current_enemy with hpunch



    if bk3_enemy_life <=0:
        $ bk3_ypos_lifebar_enemy = -370
        hide tosi tosi100_1
        hide bk3_current_enemy
        with Dissolve(1.5)
        "You knocked her unconscious!"
        jump bk3_fight_endstate

    call bk3_calculate_lifebar_positions from _call_bk3_calculate_lifebar_positions_1


    jump bk3_enemy_turn

















label bk3_enemy_turn:

    if bk3_evade == 1:
        $ rand_evade = WeightedChoice([("high", 0.90), ("mediocre", 0.10)])
        if rand_evade == "high":
            $ bk3_enemy_attack_chance == "high"
        if rand_evade == "mediocre":
            $ bk3_enemy_attack_chance == "mediocre"

    if bk3_evade ==2:
        $ rand_evade = WeightedChoice([("high", 0.80), ("mediocre", 0.20)])
        if rand_evade == "high":
            $ bk3_enemy_attack_chance == "high"
        if rand_evade == "mediocre":
            $ bk3_enemy_attack_chance == "mediocre"

    if bk3_evade == 3:
        $ rand_evade = WeightedChoice([("high", 0.70), ("mediocre", 0.30)])
        if rand_evade == "high":
            $ bk3_enemy_attack_chance == "high"
        if rand_evade == "mediocre":
            $ bk3_enemy_attack_chance == "mediocre"

    if bk3_evade ==4:
        $ rand_evade = WeightedChoice([("high", 0.60), ("mediocre", 0.40)])
        if rand_evade == "high":
            $ bk3_enemy_attack_chance == "high"
        if rand_evade == "mediocre":
            $ bk3_enemy_attack_chance == "mediocre"

    if bk3_evade ==5:
        $ rand_evade = WeightedChoice([("high", 0.50), ("mediocre", 0.50)])
        if rand_evade == "high":
            $ bk3_enemy_attack_chance == "high"
        if rand_evade == "mediocre":
            $ bk3_enemy_attack_chance == "mediocre"

    if bk3_evade ==6:
        $ rand_evade = WeightedChoice([("high", 0.40), ("mediocre", 0.60)])
        if rand_evade == "high":
            $ bk3_enemy_attack_chance == "high"
        if rand_evade == "mediocre":
            $ bk3_enemy_attack_chance == "mediocre"

    if bk3_evade ==7:
        $ rand_evade = WeightedChoice([("high", 0.30), ("mediocre", 0.70)])
        if rand_evade == "high":
            $ bk3_enemy_attack_chance == "high"
        if rand_evade == "mediocre":
            $ bk3_enemy_attack_chance == "mediocre"

    if bk3_evade ==8:
        $ rand_evade = WeightedChoice([("high", 0.20), ("mediocre", 0.80)])
        if rand_evade == "high":
            $ bk3_enemy_attack_chance == "high"
        if rand_evade == "mediocre":
            $ bk3_enemy_attack_chance == "mediocre"

    if bk3_evade ==9:
        $ rand_evade = WeightedChoice([("high", 0.10), ("mediocre", 0.90)])
        if rand_evade == "high":
            $ bk3_enemy_attack_chance == "high"
        if rand_evade == "mediocre":
            $ bk3_enemy_attack_chance == "mediocre"

    if bk3_evade ==10:
        $ rand_evade = WeightedChoice([("mediocre", 0.90), ("low", 0.10)])
        if rand_evade == "mediocre":
            $ bk3_enemy_attack_chance == "mediocre"
        if rand_evade == "low":
            $ bk3_enemy_attack_chance == "low"

    if bk3_evade >=11:
        $ rand_evade = WeightedChoice([("mediocre", 0.80), ("low", 0.20)])
        if rand_evade == "mediocre":
            $ bk3_enemy_attack_chance == "mediocre"
        if rand_evade == "low":
            $ bk3_enemy_attack_chance == "low"


    if bk3_enemy_attack_chance == "none":
        $ rand_attack = renpy.random.choice(['miss'])

    elif bk3_enemy_attack_chance == "low":
        $ rand_attack = renpy.random.choice(['hit', 'miss', 'miss', 'miss'])

    elif bk3_enemy_attack_chance == "mediocre":
        $ rand_attack = renpy.random.choice(['hit','hit', 'miss'])

    elif bk3_enemy_attack_chance == "high":
        $ rand_attack = renpy.random.choice(['hit','hit','hit', 'miss'])

    elif bk3_enemy_attack_chance == "ultimate":
        $ rand_attack = renpy.random.choice(['hit'])



    $ enemy_hits_hard = renpy.random.choice([10, 0, 0])



    if current_room.roomnr == 25 and suki_loose and not suki_free:
        show generic_enemy_attack
        play sound "audio/knife.wav"
        hide generic_enemy_attack with Dissolve(1.0)
    else:
        show bk3_current_enemy_attack
        play sound "audio/knife.wav"
        hide bk3_current_enemy_attack with Dissolve(1.0)



    if rand_attack == 'miss':
        "You evaded the attack!"
        call screen bk3_fighting_interface
    else:
        $ bk3_player_life = (bk3_player_life - bk3_enemy_attack) - enemy_hits_hard

        if bk3_player_life <= 0:
            jump bk3_fight_endstate

        $ bk3_ypos_lifebar_player = 370-((bk3_player_life*370)/bk3_player_life_start)
        show expression "bk3_fight/red_screen.png"
        hide expression "bk3_fight/red_screen.png" with dissolve


        call screen bk3_fighting_interface












label bk3_calculate_your_attack_bonus:

    $ bk3_attack_bonus = 0



    if bk3_enemy_type == 'fire':

        if bk3_attack_type == "earth_spread":
            $ bk3_attack_bonus = (bk3_player_attack/3)

        if bk3_attack_type == "earth":
            $ bk3_attack_bonus = bk3_player_attack


    if bk3_enemy_type == 'water':

        if bk3_attack_type == "fire_spread":
            $ bk3_attack_bonus = (bk3_player_attack/3)

        if bk3_attack_type == "fire":
            $ bk3_attack_bonus = bk3_player_attack


    if bk3_enemy_type == 'earth':

        if bk3_attack_type == "water_spread":
            $ bk3_attack_bonus = (bk3_player_attack/3)

        if bk3_attack_type == "water":
            $ bk3_attack_bonus = bk3_player_attack


    return





label bk3_calculate_lifebar_positions:

    if bk3_enemy_life <= 0:
        jump bk3_fight_endstate
    if bk3_player_life <= 0:
        jump bk3_fight_endstate

    if bk3_player_life_start <= 0:
        $ bk3_player_life_start = 1
    if bk3_enemy_life_start <= 0:
        $ bk3_enemy_life_start = 1



    $ bk3_ypos_lifebar_player = 370-((bk3_player_life*370)/bk3_player_life_start)
    $ bk3_ypos_lifebar_enemy = -(370-((bk3_enemy_life*370)/bk3_enemy_life_start))



    return















label bk3_fight_endstate:
    hide bk3_current_enemy
    stop music fadeout 1
    play music "audio/Unity.mp3"



    if bk3_current_enemy == "ajalagirl":
        if bk3_player_life <= 0:
            "Ajala has thoroughly beaten you, she looks...saddened."
            $ bk3_maze_fightslost += 1
            hide screen bk3_lifebars

            $ bk3_player_life_start = bk3_hp
            $ bk3_player_life = bk3_player_life_start
            scene black with dissolve
            "you wake up in the hospital."
            $ maze_music_on = False
            $ current_room = room1
            jump inside_hospital_building
        else:

            hide screen bk3_lifebars
            "You won....with a sigh of relief Ajala slumps to the ground."
            $ current_room.maze_enemy = False
            $ room107.sp_content = 1
            jump bk3_maze_start



    if bk3_current_enemy == "sewercrab":
        if bk3_player_life <= 0:
            "You got your ass handed to you and crawl away while your enemy is starting to fold his boats again."
            $ bk3_maze_fightslost += 1

            hide screen bk3_lifebars
            $ current_room = previous_room
            jump bk3_maze_start
        else:

            hide screen bk3_lifebars
            "You won.... "
            $ current_room.maze_enemy = False
            $ current_room.sp_content = 1
            y "what's this?"
            play sound "audio/win2.mp3"
            show blackveil
            show pornlove_yue
            with dissolve
            $ sewercrab_win = True
            "you found some pornlove pages!"
            show ctc
            pause
            hide ctc
            jump yue_pornlove_menu

            label yue_pornlove_menu:
                menu:
                    "keep reading":
                        show ctc
                        pause
                        hide ctc
                        jump yue_pornlove_menu
                    "leave":
                        y "i'll put this on sokka's shelf."
                        y "with the other pornlove."
                        hide blackveil
                        hide pornlove_yue
                        with dissolve
                        jump bk3_maze_start






    if bk3_current_enemy == "bmole":
        if bk3_player_life <= 0:
            "You got your ass handed to you."
            "you can't be sure, but it sounds like the creature is laughing as you crawl away."
            $ bk3_maze_fightslost += 1

            hide screen bk3_lifebars
            $ current_room = previous_room


            if maze_follower =="prisonbitch":
                jin "Better luck next time!"

            if maze_follower =="prisonthighs":
                ty "Oh well, we're still alive. That's nice."


            jump bk3_maze_start
        else:

            hide screen bk3_lifebars
            "You won. Well done you ravisher of badgermoles!"


            if maze_follower =="prisonbitch":
                jin "Eeewh! Is it dead?"


            if maze_follower =="prisonthighs":
                ty "Yuck, I hate those animals! Good riddance."


            $ current_room.maze_enemy = False

            if bk3_enemy_level == 2:
                $ exp_total +=6
                show text "+6 exp" at truecenter
                with dissolve
                $ renpy.pause(0.5)
                hide text with dissolve

            if bk3_enemy_level == 5:
                $ exp_total +=15
                show text "{color=#ffffff}{size=+10}+12 exp" at truecenter
                with dissolve
                $ renpy.pause(0.5)
                hide text with dissolve

            if bk3_enemy_level == 10:
                $ exp_total +=25
                show text "{color=#ffffff}{size=+10}+20 exp" at truecenter
                with dissolve
                $ renpy.pause(0.5)
                hide text with dissolve

            if exp_total >= 5 and bk3_level < 2:
                $ bk3_level +=1
                $ bk3_accuracy += 1
                $ bk3_evade +=1
                $ bk3_hp += 5
                $ bk3_level_points +=1
                $ bk3_player_attack +=0
                $ level_up = True

            if exp_total >= 10 and bk3_level < 3:
                $ bk3_level +=1
                $ bk3_accuracy += 1
                $ bk3_evade +=1
                $ bk3_hp += 5
                $ bk3_level_points +=1
                $ bk3_player_attack +=0
                $ level_up = True

            if exp_total >= 20 and bk3_level < 4:
                $ bk3_level +=1
                $ bk3_accuracy += 1
                $ bk3_evade +=1
                $ bk3_hp += 5
                $ bk3_level_points +=1
                $ bk3_player_attack +=0
                $ level_up = True

            if exp_total >= 35 and bk3_level < 5:
                $ bk3_level +=1
                $ bk3_accuracy += 1
                $ bk3_evade +=1
                $ bk3_hp += 5
                $ bk3_level_points +=1
                $ bk3_player_attack +=0
                $ level_up = True

            if exp_total >= 55 and bk3_level < 6:
                $ bk3_level +=1
                $ bk3_accuracy += 1
                $ bk3_evade +=1
                $ bk3_hp += 5
                $ bk3_level_points +=1
                $ bk3_player_attack +=0
                $ level_up = True

            if exp_total >= 80 and bk3_level < 7:
                $ bk3_level +=1
                $ bk3_accuracy += 1
                $ bk3_evade +=1
                $ bk3_hp += 5
                $ bk3_level_points +=1
                $ bk3_player_attack +=0
                $ level_up = True

            if exp_total >= 110 and bk3_level < 8:
                $ bk3_level +=1
                $ bk3_accuracy += 1
                $ bk3_evade +=1
                $ bk3_hp += 5
                $ bk3_level_points +=1
                $ bk3_player_attack +=0
                $ level_up = True

            if exp_total >= 145 and bk3_level < 9:
                $ bk3_level +=1
                $ bk3_accuracy += 1
                $ bk3_evade +=1
                $ bk3_hp += 5
                $ bk3_level_points +=1
                $ bk3_player_attack +=0
                $ level_up = True

            if exp_total >= 185 and bk3_level < 10:
                $ bk3_level +=1
                $ bk3_accuracy += 1
                $ bk3_evade +=1
                $ bk3_hp += 5
                $ bk3_level_points +=1
                $ bk3_player_attack +=0
                $ level_up = True

            if exp_total >= 230 and bk3_level < 11:
                $ bk3_level +=1
                $ bk3_accuracy += 1
                $ bk3_evade +=1
                $ bk3_hp += 5
                $ bk3_level_points +=1
                $ bk3_player_attack +=0
                $ level_up = True

            if exp_total >= 280 and bk3_level < 12:
                $ bk3_level +=1
                $ bk3_accuracy += 1
                $ bk3_evade +=1
                $ bk3_hp += 5
                $ bk3_level_points +=1
                $ bk3_player_attack +=0
                $ level_up = True

            if exp_total >= 335 and bk3_level < 13:
                $ bk3_level +=1
                $ bk3_accuracy += 1
                $ bk3_evade +=1
                $ bk3_hp += 5
                $ bk3_level_points +=1
                $ bk3_player_attack +=0
                $ level_up = True

            if exp_total >= 390 and bk3_level < 14:
                $ bk3_level +=1
                $ bk3_accuracy += 1
                $ bk3_evade +=1
                $ bk3_hp += 5
                $ bk3_level_points +=1
                $ bk3_player_attack +=0
                $ level_up = True

            if exp_total >= 450 and bk3_level < 15:
                $ bk3_level +=1
                $ bk3_accuracy += 1
                $ bk3_evade +=1
                $ bk3_hp += 5
                $ bk3_level_points +=1
                $ level_up = True

            if exp_total >= 520 and bk3_level < 16:
                $ bk3_level +=1
                $ bk3_accuracy += 1
                $ bk3_evade +=1
                $ bk3_hp += 5
                $ bk3_level_points +=1
                $ bk3_player_attack +=0
                $ level_up = True

            if exp_total >= 600 and bk3_level < 17:
                $ bk3_level +=1
                $ bk3_accuracy += 1
                $ bk3_evade +=1
                $ bk3_hp += 5
                $ bk3_level_points +=1
                $ bk3_player_attack +=0
                $ level_up = True

            if exp_total >= 690 and bk3_level < 18:
                $ bk3_level +=1
                $ bk3_accuracy += 1
                $ bk3_evade +=1
                $ bk3_hp += 5
                $ bk3_level_points +=1
                $ bk3_player_attack +=0
                $ level_up = True

            if exp_total >= 790 and bk3_level < 19:
                $ bk3_level +=1
                $ bk3_accuracy += 1
                $ bk3_evade +=1
                $ bk3_hp += 5
                $ bk3_level_points +=1
                $ bk3_player_attack +=0
                $ level_up = True

            if exp_total >= 900 and bk3_level < 20:
                $ bk3_level +=1
                $ bk3_accuracy += 1
                $ bk3_evade +=1
                $ bk3_hp += 5
                $ bk3_level_points +=1
                $ bk3_player_attack +=0
                $ level_up = True

            if exp_total >= 1020 and bk3_level < 21:
                $ bk3_level +=1
                $ bk3_accuracy += 1
                $ bk3_evade +=1
                $ bk3_hp += 5
                $ bk3_level_points +=1
                $ level_up = True

            if exp_total >= 1150 and bk3_level < 22:
                $ bk3_level +=1
                $ bk3_accuracy += 1
                $ bk3_evade +=1
                $ bk3_hp += 5
                $ bk3_level_points +=1
                $ bk3_player_attack +=0
                $ level_up = True

            if exp_total >= 1290 and bk3_level < 23:
                $ bk3_level +=1
                $ bk3_accuracy += 1
                $ bk3_evade +=1
                $ bk3_hp += 5
                $ bk3_level_points +=1
                $ bk3_player_attack +=0
                $ level_up = True

            if exp_total >= 1440 and bk3_level < 24:
                $ bk3_level +=1
                $ bk3_accuracy += 1
                $ bk3_evade +=1
                $ bk3_hp += 5
                $ bk3_level_points +=1
                $ bk3_player_attack +=0
                $ level_up = True

            if exp_total >= 1600 and bk3_level < 25:
                $ bk3_level +=1
                $ bk3_accuracy += 1
                $ bk3_evade +=1
                $ bk3_hp += 5
                $ bk3_level_points +=1
                $ bk3_player_attack +=0
                $ level_up = True

            if exp_total >= 1790 and bk3_level < 26:
                $ bk3_level +=1
                $ bk3_accuracy += 1
                $ bk3_evade +=1
                $ bk3_hp += 5
                $ bk3_level_points +=1
                $ bk3_player_attack +=0
                $ level_up = True

            if exp_total >= 1990 and bk3_level < 27:
                $ bk3_level +=1
                $ bk3_accuracy += 1
                $ bk3_evade +=1
                $ bk3_hp += 5
                $ bk3_level_points +=1
                $ bk3_player_attack +=0
                $ level_up = True

            if exp_total >= 2200 and bk3_level < 28:
                $ bk3_level +=1
                $ bk3_accuracy += 1
                $ bk3_evade +=1
                $ bk3_hp += 5
                $ bk3_level_points +=1
                $ bk3_player_attack +=0
                $ level_up = True

            if exp_total >= 2420 and bk3_level < 29:
                $ bk3_level +=1
                $ bk3_accuracy += 1
                $ bk3_evade +=1
                $ bk3_hp += 5
                $ bk3_level_points +=1
                $ bk3_player_attack +=0
                $ level_up = True

            if exp_total >= 2700 and bk3_level < 30:
                $ bk3_level +=1
                $ bk3_accuracy += 1
                $ bk3_evade +=1
                $ bk3_hp += 5
                $ bk3_level_points +=1
                $ bk3_player_attack +=0
                $ level_up = True

            if level_up:
                show text "you've reached level [bk3_level]!" at truecenter
                with dissolve
                $ renpy.pause()
                hide text with dissolve


                $ bk3_ypos_lifebar_player = 0




                if bk3_level == 3:
                    $ bk3_moves +=1
                    "you can now do 1 more attack with each move!"
                if bk3_level == 5:
                    $ bk3_moves +=1
                    "you can now do 1 more attack with each move!"
                if bk3_level == 7:
                    $ bk3_moves +=1
                    "you can now do 1 more attack with each move!"
                if bk3_level == 9:
                    $ bk3_moves +=1
                    "you can now do 1 more attack with each move!"
                if bk3_level == 11:
                    $ bk3_moves +=1
                    "you can now do 1 more attack with each move!"
                if bk3_level == 13:
                    $ bk3_moves +=1
                    "you can now do 1 more attack with each move!"
                if bk3_level == 15:
                    $ bk3_moves +=1
                    "you can now do 1 more attack with each move!"
                if bk3_level == 17:
                    $ bk3_moves +=1
                    "you can now do 1 more attack with each move!"
                if bk3_level == 19:
                    $ bk3_moves +=1
                    "you can now do 1 more attack with each move!"
                if bk3_level == 21:
                    $ bk3_moves +=1
                    "you can now do 1 more attack with each move!"
                if bk3_level == 23:
                    $ bk3_moves +=1
                    "you can now do 1 more attack with each move!"
                if bk3_level == 25:
                    $ bk3_moves +=1
                    "you can now do 1 more attack with each move!"
                if bk3_level == 27:
                    $ bk3_moves +=1
                    "you can now do 1 more attack with each move!"
                if bk3_level == 29:
                    $ bk3_moves +=1
                    "you can now do 1 more attack with each move!"
                if bk3_level == 30:
                    $ bk3_moves +=1
                    "you can now do 1 more attack with each move!"


                $ bk3_fire_remaining = bk3_moves
                $ bk3_water_remaining = bk3_moves


                $ bk3_player_life_start = bk3_hp
                $ bk3_player_life = bk3_player_life_start

                $ level_up = False
                $ bk3_leveling_screen = True
                call screen bk3_level_up_stats2

            jump bk3_maze_start



    if bk3_player_life <= 0:

        if bk3_current_enemy == "ncgirl":
            $ bk3_maze_fightslost += 1
            hide screen bk3_lifebars
            $ current_room = previous_room
            show thankful_girl with dissolve
            "girl" "....."
            "girl" "where... where am i...?"
            hide thankful_girl with vshake
            "the girl falls to the floor suddenly."
            show toi toi210
            show toi_swim_surprise
            with dissolve
            t "we need to get her out of here."
            t "we'll take her back to my house."
            t "let's get out of here."
            hide toi toi210
            hide toi_swim_surprise
            with dissolve
            $ first_maze_girl = True
            jump bk3_maze_start

        "You got your ass handed to you and crawl away."
        "That's right! Run like a bitch! I'll get you later!"

        $ bk3_maze_fightslost += 1

        hide screen bk3_lifebars

        $ bk3_player_life_start = bk3_hp
        $ bk3_player_life = bk3_player_life_start

        if first_maze_girl and first_maze_girl_escape:
            scene black with dissolve
            "you wake up in the hospital."
            $ maze_music_on = False
            $ current_room = room1
            jump inside_hospital_building



        $ current_room = previous_room


        if maze_follower =="prisonbitch":
            jin "Better luck next time!"

        if maze_follower =="prisonthighs":
            ty "Oh well, we're still alive. That's nice."

        jump bk3_maze_start
    else:

        hide screen bk3_lifebars
        "You won!"
        $ first_maze_fight = True
        $ current_room.maze_enemy = False

        if current_room == room23:
            $ room23_fight = True

        if current_room == room25:
            if suki_free:
                pass
            else:

                $ exp_total +=15
                "suki passes out on the floor in front of you."
                y "it's about time."
                $ suki_free = True
                $ room21.sp_item = False
                y "alright, sucky, let's get you back to the village."
                jump backtotherealworld

        if current_room == room56:
            $ room56_fight = True

        if current_room == room59:
            $ room59_fight = True

        $ random_emoney = renpy.random.choice([5, 10, 15, 20])
        $ emoney += random_emoney
        if random_emoney >0:
            play sound "audio/money.mp3"
            "You found [random_emoney] coins!"

        if bk3_enemy_level == 2:
            $ exp_total +=6
            show text "{color=#ffffff}{size=+20}+6 exp" at truecenter
            with dissolve
            $ renpy.pause(0.5)
            hide text with dissolve

        if bk3_enemy_level == 5:
            $ exp_total +=12
            show text "{color=#ffffff}{size=+10}+12 exp" at truecenter
            with dissolve
            $ renpy.pause(0.5)
            hide text with dissolve

        if bk3_enemy_level == 10:
            $ exp_total +=20
            show text "{color=#ffffff}{size=+10}+20 exp" at truecenter
            with dissolve
            $ renpy.pause(0.5)
            hide text with dissolve

        if bk3_enemy_level == 20:
            $ exp_total +=30
            show text "{color=#ffffff}{size=+10}+30 exp" at truecenter
            with dissolve
            $ renpy.pause(0.5)
            hide text with dissolve

        if exp_total >= 5 and bk3_level < 2:
            $ bk3_level +=1
            $ bk3_accuracy += 1
            $ bk3_evade +=1
            $ bk3_hp += 5
            $ bk3_level_points +=1
            $ bk3_player_attack +=0
            $ level_up = True

        if exp_total >= 10 and bk3_level < 3:
            $ bk3_level +=1
            $ bk3_accuracy += 1
            $ bk3_evade +=1
            $ bk3_hp += 5
            $ bk3_level_points +=1
            $ bk3_player_attack +=0
            $ level_up = True

        if exp_total >= 20 and bk3_level < 4:
            $ bk3_level +=1
            $ bk3_accuracy += 1
            $ bk3_evade +=1
            $ bk3_hp += 5
            $ bk3_level_points +=1
            $ bk3_player_attack +=0
            $ level_up = True

        if exp_total >= 35 and bk3_level < 5:
            $ bk3_level +=1
            $ bk3_accuracy += 1
            $ bk3_evade +=1
            $ bk3_hp += 5
            $ bk3_level_points +=1
            $ bk3_player_attack +=0
            $ level_up = True

        if exp_total >= 55 and bk3_level < 6:
            $ bk3_level +=1
            $ bk3_accuracy += 1
            $ bk3_evade +=1
            $ bk3_hp += 5
            $ bk3_level_points +=1
            $ bk3_player_attack +=0
            $ level_up = True

        if exp_total >= 80 and bk3_level < 7:
            $ bk3_level +=1
            $ bk3_accuracy += 1
            $ bk3_evade +=1
            $ bk3_hp += 5
            $ bk3_level_points +=1
            $ bk3_player_attack +=0
            $ level_up = True

        if exp_total >= 110 and bk3_level < 8:
            $ bk3_level +=1
            $ bk3_accuracy += 1
            $ bk3_evade +=1
            $ bk3_hp += 5
            $ bk3_level_points +=1
            $ bk3_player_attack +=0
            $ level_up = True

        if exp_total >= 145 and bk3_level < 9:
            $ bk3_level +=1
            $ bk3_accuracy += 1
            $ bk3_evade +=1
            $ bk3_hp += 5
            $ bk3_level_points +=1
            $ bk3_player_attack +=0
            $ level_up = True

        if exp_total >= 185 and bk3_level < 10:
            $ bk3_level +=1
            $ bk3_accuracy += 1
            $ bk3_evade +=1
            $ bk3_hp += 5
            $ bk3_level_points +=1
            $ bk3_player_attack +=0
            $ level_up = True

        if exp_total >= 230 and bk3_level < 11:
            $ bk3_level +=1
            $ bk3_accuracy += 1
            $ bk3_evade +=1
            $ bk3_hp += 5
            $ bk3_level_points +=1
            $ bk3_player_attack +=0
            $ level_up = True

        if exp_total >= 280 and bk3_level < 12:
            $ bk3_level +=1
            $ bk3_accuracy += 1
            $ bk3_evade +=1
            $ bk3_hp += 5
            $ bk3_level_points +=1
            $ bk3_player_attack +=0
            $ level_up = True

        if exp_total >= 335 and bk3_level < 13:
            $ bk3_level +=1
            $ bk3_accuracy += 1
            $ bk3_evade +=1
            $ bk3_hp += 5
            $ bk3_level_points +=1
            $ bk3_player_attack +=0
            $ level_up = True

        if exp_total >= 390 and bk3_level < 14:
            $ bk3_level +=1
            $ bk3_accuracy += 1
            $ bk3_evade +=1
            $ bk3_hp += 5
            $ bk3_level_points +=1
            $ bk3_player_attack +=0
            $ level_up = True

        if exp_total >= 450 and bk3_level < 15:
            $ bk3_level +=1
            $ bk3_accuracy += 1
            $ bk3_evade +=1
            $ bk3_hp += 5
            $ bk3_level_points +=1
            $ bk3_player_attack +=0
            $ level_up = True

        if exp_total >= 520 and bk3_level < 16:
            $ bk3_level +=1
            $ bk3_accuracy += 1
            $ bk3_evade +=1
            $ bk3_hp += 5
            $ bk3_level_points +=1
            $ bk3_player_attack +=0
            $ level_up = True

        if exp_total >= 600 and bk3_level < 17:
            $ bk3_level +=1
            $ bk3_accuracy += 1
            $ bk3_evade +=1
            $ bk3_hp += 5
            $ bk3_level_points +=1
            $ bk3_player_attack +=0
            $ level_up = True

        if exp_total >= 690 and bk3_level < 18:
            $ bk3_level +=1
            $ bk3_accuracy += 1
            $ bk3_evade +=1
            $ bk3_hp += 5
            $ bk3_level_points +=1
            $ bk3_player_attack +=0
            $ level_up = True

        if exp_total >= 790 and bk3_level < 19:
            $ bk3_level +=1
            $ bk3_accuracy += 1
            $ bk3_evade +=1
            $ bk3_hp += 5
            $ bk3_level_points +=1
            $ bk3_player_attack +=0
            $ level_up = True

        if exp_total >= 900 and bk3_level < 20:
            $ bk3_level +=1
            $ bk3_accuracy += 1
            $ bk3_evade +=1
            $ bk3_hp += 5
            $ bk3_level_points +=1
            $ bk3_player_attack +=0
            $ level_up = True

        if exp_total >= 1020 and bk3_level < 21:
            $ bk3_level +=1
            $ bk3_accuracy += 1
            $ bk3_evade +=1
            $ bk3_hp += 5
            $ bk3_level_points +=1
            $ bk3_player_attack +=0
            $ level_up = True

        if exp_total >= 1150 and bk3_level < 22:
            $ bk3_level +=1
            $ bk3_accuracy += 1
            $ bk3_evade +=1
            $ bk3_hp += 5
            $ bk3_level_points +=1
            $ bk3_player_attack +=0
            $ level_up = True

        if exp_total >= 1290 and bk3_level < 23:
            $ bk3_level +=1
            $ bk3_accuracy += 1
            $ bk3_evade +=1
            $ bk3_hp += 5
            $ bk3_level_points +=1
            $ bk3_player_attack +=0
            $ level_up = True

        if exp_total >= 1440 and bk3_level < 24:
            $ bk3_level +=1
            $ bk3_accuracy += 1
            $ bk3_evade +=1
            $ bk3_hp += 5
            $ bk3_level_points +=1
            $ bk3_player_attack +=0
            $ level_up = True

        if exp_total >= 1600 and bk3_level < 25:
            $ bk3_level +=1
            $ bk3_accuracy += 1
            $ bk3_evade +=1
            $ bk3_hp += 5
            $ bk3_level_points +=1
            $ bk3_player_attack +=0
            $ level_up = True

        if exp_total >= 1790 and bk3_level < 26:
            $ bk3_level +=1
            $ bk3_accuracy += 1
            $ bk3_evade +=1
            $ bk3_hp += 5
            $ bk3_level_points +=1
            $ bk3_player_attack +=0
            $ level_up = True

        if exp_total >= 1990 and bk3_level < 27:
            $ bk3_level +=1
            $ bk3_accuracy += 1
            $ bk3_evade +=1
            $ bk3_hp += 5
            $ bk3_level_points +=1
            $ bk3_player_attack +=0
            $ level_up = True

        if exp_total >= 2200 and bk3_level < 28:
            $ bk3_level +=1
            $ bk3_accuracy += 1
            $ bk3_evade +=1
            $ bk3_hp += 5
            $ bk3_level_points +=1
            $ bk3_player_attack +=0
            $ level_up = True

        if exp_total >= 2420 and bk3_level < 29:
            $ bk3_level +=1
            $ bk3_accuracy += 1
            $ bk3_evade +=1
            $ bk3_hp += 5
            $ bk3_level_points +=1
            $ bk3_player_attack +=0
            $ level_up = True

        if exp_total >= 2700 and bk3_level < 30:
            $ bk3_level +=1
            $ bk3_accuracy += 1
            $ bk3_evade +=1
            $ bk3_hp += 5
            $ bk3_level_points +=1
            $ bk3_player_attack +=0
            $ level_up = True

        if level_up:























            show text "{color=#ffffff}{size=+10}you've reached level [bk3_level]!" at truecenter
            with dissolve
            $ renpy.pause()
            hide text with dissolve

            if bk3_level == 3:
                $ bk3_moves +=1
                "you can now do 1 more attack with each move!"
            if bk3_level == 5:
                $ bk3_moves +=1
                "you can now do 1 more attack with each move!"
            if bk3_level == 7:
                $ bk3_moves +=1
                "you can now do 1 more attack with each move!"
            if bk3_level == 9:
                $ bk3_moves +=1
                "you can now do 1 more attack with each move!"
            if bk3_level == 11:
                $ bk3_moves +=1
                "you can now do 1 more attack with each move!"
            if bk3_level == 13:
                $ bk3_moves +=1
                "you can now do 1 more attack with each move!"
            if bk3_level == 15:
                $ bk3_moves +=1
                "you can now do 1 more attack with each move!"
            if bk3_level == 17:
                $ bk3_moves +=1
                "you can now do 1 more attack with each move!"
            if bk3_level == 19:
                $ bk3_moves +=1
                "you can now do 1 more attack with each move!"
            if bk3_level == 21:
                $ bk3_moves +=1
                "you can now do 1 more attack with each move!"
            if bk3_level == 23:
                $ bk3_moves +=1
                "you can now do 1 more attack with each move!"
            if bk3_level == 25:
                $ bk3_moves +=1
                "you can now do 1 more attack with each move!"
            if bk3_level == 27:
                $ bk3_moves +=1
                "you can now do 1 more attack with each move!"
            if bk3_level == 29:
                $ bk3_moves +=1
                "you can now do 1 more attack with each move!"
            if bk3_level == 30:
                $ bk3_moves +=1
                "you can now do 1 more attack with each move!"


            $ bk3_fire_remaining = bk3_moves
            $ bk3_water_remaining = bk3_moves


            $ bk3_player_life_start = bk3_hp
            $ bk3_player_life = bk3_player_life_start

            $ bk3_ypos_lifebar_player = 0

        if current_room.roomnr == 101:
            show tolf tolf02:
                xpos -280
            with dissolve
            lf "damn it!"
            lf "ugh, no matter!"
            lf "dai lee!"
            show toeg toeg01
            show toeg toeg03:
                xzoom -1
            with dissolve
            lf "arrest the avatar!"
            dl "........"
            lf "i said... arrest him!"
            dl "........"
            lf "what is wrong with you?"
            y "it's because they haven't made up their minds."
            lf "what?"
            y "you've probably struggled your whole life, conniving, scheming, gathering power where you can..."
            y "but power, true power, is something you're born with."
            y "and i, the avatar, am more powerful than anyone."
            y "one of us is going to go free, and the other is going to be imprisoned for the rest of their life."
            y "they're not sure which one is which..."
            y "but you know. and i know."
            show tolf_blink:
                xpos -280
            with dissolve
            lf "this... this can't be."
            y "go ahead... try me."
            lf "....."
            hide tolf_blink with dissolve
            lf "...congratulations, avatar."
            lf "you've beat me at my own game."
            y "don't flatter yourself..."
            y "you were never even a player."
            hide toeg
            hide tolf
            hide tolf_blink
            with dissolve
            "the dai lee take long feng away, imprisoning him."
            "they bow and move swiftly out of sight, moving long feng deeper into the tunnels."
            y "excellent."
            y "once i free these nerds i'll go visit the earth king."
            y "without feng's interference."


    jump bk3_after_fight_win


label bk3_after_fight_win:
    if level_up:
        $ level_up = False
        $ bk3_leveling_screen = True
        call screen bk3_level_up_stats

    if current_room.roomnr == 25 and suki_loose and not suki_free:
        "suki passes out on the floor in front of you."


    if bk3_current_enemy == "ncgirl":
        show thankful_girl with dissolve
        "girl" "....."
        "girl" "where... where am i...?"
        hide thankful_girl with vshake
        "the girl falls to the floor suddenly."
        show toi toi210
        show toi_swim_surprise
        with dissolve
        t "we need to get her out of here."
        t "we'll take her back to my house."
        t "let's get out of here."
        hide toi toi210
        hide toi_swim_surprise
        with dissolve
        $ first_maze_girl = True

    if bk3_fuckable == True:
        pass
    else:
        jump bk3_maze_start

    if occupied_room ==7:
        "you open the treasure chest...."
        play sound "audio/win2.mp3"
        $ bk3_lifepotions +=2
        "you found 2 life potions!"
        $ bk3_manapotions += 2
        play sound "audio/win2.mp3"
        "you found 2 mana potions!"
        play sound "audio/win2.mp3"
        $ obsidian +=1
        "you found 1 batch of obsidian!"
        $ current_room.sp_used = True
        $ occupied_room = 0



    if bk3_current_enemy == "bmole":
        jump bk3_maze_start
    else:
        "Wanna fuck your opponent?"
        menu:
            "Nah, not this time.":
                jump bk3_maze_start
            "My dick is hard and ready to go!":
                jump bk3_winnerfucksall



label bk3_winnerfucksall:

    show frape frape0

    if bk3_girlhead == 'bk3_girlhead_1':
        show expression 'bk3_girlhead_1ani'

    elif bk3_girlhead == 'bk3_girlhead_2':
        show expression 'bk3_girlhead_2ani'

    elif bk3_girlhead == 'bk3_girlhead_3':
        show expression 'bk3_girlhead_3ani'

    elif bk3_girlhead == 'bk3_girlhead_4':
        show expression 'bk3_girlhead_4ani'

    elif bk3_girlhead == 'bk3_girlhead_5':
        show expression 'bk3_girlhead_5ani'
    show expression "bk3_fight/eyebrow_angry.png"
    "What? You want to put your filthy dick inside me ?!" with Dissolve(1.0)
    y "Ah, I was hoping you'd stay unconscious a bit longer."
    show frape frape1 with Dissolve(1.0)
    "So what'll be, ass or pussy? Wait, let me see your stampcard first."

    if bk3_maze_fightswon == 0:
        "You don't even have a stampcard?"
        show expression "bk3_fight/stamp_paper.png"
        "Here's a blank one."
        show expression "bk3_fight/stamp_stamp_1.png"
        "and here's your first stamp. Fill it up and you can fill me up!"
        hide expression "bk3_fight/stamp_paper_1.png"
    elif bk3_maze_fightswon == 1:
        show expression "bk3_fight/stamp_paper.png"
        show expression "bk3_fight/stamp_stamp_1.png"
        "You already have one. Here's number two!"
        hide expression "bk3_fight/stamp_stamp_1.png"
        show expression "bk3_fight/stamp_stamp_2.png"
        "Just two more!"
        hide expression "bk3_fight/stamp_paper.png"

        hide expression "bk3_fight/stamp_stamp_2.png"
    elif bk3_maze_fightswon == 2:
        show expression "bk3_fight/stamp_paper.png"
        show expression "bk3_fight/stamp_stamp_2.png"
        "Two done and here's your third."
        hide expression "bk3_fight/stamp_stamp_2.png"
        show expression "bk3_fight/stamp_stamp_3.png"
        "Just one more!"
        hide expression "bk3_fight/stamp_paper.png"
        hide expression "bk3_fight/stamp_stamp_3.png"
    elif bk3_maze_fightswon == 3:
        show expression "bk3_fight/stamp_paper.png"
        show expression "bk3_fight/stamp_stamp_3.png"
        "You already have three?"
        hide expression "bk3_fight/stamp_stamp_3.png"
        show expression "bk3_fight/stamp_stamp_4.png"
        "With mine added your card is full! What'll it be pussy or ass?"
        hide expression "bk3_fight/stamp_paper.png"
        hide expression "bk3_fight/stamp_stamp_4.png"


    $ bk3_maze_fightswon += 1

    if bk3_maze_fightswon >= 4:
        $ bk3_maze_fightswon = 0
        pass
    else:
        show frape frape0 with vpunch
        scene black
        "She jumps up and runs away before you can say anything."
        jump bk3_maze_start

    menu:
        "ass":

            girl "Fine you faggot, put it in my ass."

            show frape frape2
            show frape_analgape
            with Dissolve(1.3)
            girl "come on, this isn't a peepshow."
            show frape_dick
            girl "put it in."
            show frape_analoverlay

            hide frape_dick
            show frape_dick:
                ypos 60
                linear 1.0 ypos 0
                linear 1.5 ypos 60
                repeat
            hide frape_analoverlay
            show frape_analoverlay


            girl "What? you think that does anything for me?"
            girl "Hah! A nice cock but you've got no idea what to do with it!"
            girl "harder!"

            girl "Tickle my throat with that long shlong of yours!"

            show frape_dick:
                ypos 60
                linear 1.0 ypos -80
                linear 1.5 ypos 60
                repeat
            with vpunch


            girl "Faster!!"
            show frape_dick:
                ypos 60
                linear 0.5 ypos -80
                linear 1.0 ypos 60
                repeat
            with vpunch

            girl "that's more like it!"

            show frape_dick:
                ypos -100
            with vpunch
            play sound "audio/gltch2b.mp3"
            hide expression "bk3_fight/eyebrow_angry.png"
            show expression "bk3_fight/eyebrow_happy.png"
            girl "oh."
            hide frape_dick
            show frape2_dick2 with Dissolve(1.3)
            girl "That's quite a bit."
            y "I'm ready for that pussy now."

            hide expression "bk3_fight/eyebrow_happy.png"
            show expression "bk3_fight/eyebrow_angry.png"

            girl "After you've just been in my ass?! No way!"
            y "Aaawh."



            scene black with Dissolve(1.4)

            "Before you can press the matter the girl jumps up and runs away, leaving a trail of dripping cum on the floor."
            y "....."


            jump bk3_maze_start
        "pussy":

            girl "Ah, excellent choice. Let's see if you have what it takes to satisfy me."


            hide frape_openpuss
            show frape_openpuss:
                ypos 4
                linear 1.0 ypos -3
                linear 1.5 ypos 4
                repeat

            hide frape_dick
            show frape_dick:
                ypos -10
                linear 1.0 ypos -50
                linear 1.5 ypos -10
                repeat

            show frape_pussoverlay

            girl "What? you think that does anything for me?"
            girl "Hah! A nice cock but you've got no idea what to do with it!"
            girl "Go harder, you piece of shit!"

            girl "Kiss my womb with your fat dick!"

            show frape_dick:
                ypos -10
                linear 1.0 ypos -180
                linear 1.5 ypos -10
                repeat


            girl "Faster!!"
            show frape_dick:
                ypos -10
                linear 0.5 ypos -180
                linear 1.0 ypos -10
                repeat


            girl "that's more like it!"

            show frape_dick:
                ypos -140
            play sound "audio/gltch2b.mp3"
            hide expression "bk3_fight/eyebrow_angry.png"
            show expression "bk3_fight/eyebrow_happy.png"
            girl "oh."




            play sound "audio/gltch2b.mp3"
            girl "Aaaah. That's a nice amount. I can feel it flowing inside me."
            $ bk3_inseminations += 1
            hide frape_dick
            hide frape_openpuss
            hide frape_pussoverlay
            with Dissolve(0.8)

            show frape_dick2

            y "Ready for round two?"
            girl "Nah not now, spreading loads has a better chance of getting me pregnant."
            y "....Say wut?!?"
            hide frape_dick2
            show frape_heldopenpuss with Dissolve(1.3)
            hide expression "bk3_fight/eyebrow_happy.png"
            show expression "bk3_fight/eyebrow_angry.png"

            girl "With this much cum inside me you can't really be surprised about that possibility, right?"

            hide frape frape0
            hide frape_heldopenpuss

            if bk3_girlhead == 'bk3_girlhead_1':
                hide expression 'bk3_girlhead_1ani'

            elif bk3_girlhead == 'bk3_girlhead_2':
                hide expression 'bk3_girlhead_2ani'

            elif bk3_girlhead == 'bk3_girlhead_3':
                hide expression 'bk3_girlhead_3ani'

            elif bk3_girlhead == 'bk3_girlhead_4':
                hide expression 'bk3_girlhead_4ani'

            elif bk3_girlhead == 'bk3_girlhead_5':
                hide expression 'bk3_girlhead_5ani'
            hide expression "bk3_fight/eyebrow_happy.png"
            with Dissolve(2.0)

            "Before you can answer the girl jumps up and runs away."
            y "....weird..."
            scene black


            if maze_follower == "prisonbitch":
                jin "Wow... I got a superwet from watching that."

            if maze_follower == "prisonthighs":
                ty "Wow... so you didn't use all of your sperm on me..."


            jump bk3_maze_start

screen bk3_level_up_stats1:
    add "misc/bk3_scroll.jpg"
    text "{color=#000000}Level:" xpos 340 ypos 180
    text "{color=#000000}[bk3_level]" xpos 640 ypos 180
    text "{color=#000000}Max Health:" xpos 340 ypos 230
    text "{color=#000000}[bk3_hp]" xpos 640 ypos 230

    text "{color=#000000}Accuracy:" xpos 340 ypos 280
    text "{color=#000000}[bk3_accuracy]" xpos 640 ypos 280
    text "{color=#000000}Evasion:" xpos 340 ypos 330
    text "{color=#000000}[bk3_evade]" xpos 640 ypos 330
    text "{color=#000000}Total Experience:" xpos 340 ypos 380
    text "{color=#000000}[exp_total]" xpos 640 ypos 380
    text "{color=#000000}Until Next Level:" xpos 340 ypos 430
    if bk3_level ==1:
        text "{color=#000000}5" xpos 640 ypos 430
    if bk3_level ==2:
        text "{color=#000000}[bk3_level3]" xpos 640 ypos 430
    if bk3_level ==3:
        text "{color=#000000}[bk3_level4]" xpos 640 ypos 430
    if bk3_level ==4:
        text "{color=#000000}[bk3_level5]" xpos 640 ypos 430
    if bk3_level ==5:
        text "{color=#000000}[bk3_level6]" xpos 640 ypos 430
    if bk3_level ==6:
        text "{color=#000000}[bk3_level7]" xpos 640 ypos 430
    if bk3_level ==7:
        text "{color=#000000}[bk3_level8]" xpos 640 ypos 430
    if bk3_level ==8:
        text "{color=#000000}[bk3_level9]" xpos 640 ypos 430
    if bk3_level ==9:
        text "{color=#000000}[bk3_level10]" xpos 640 ypos 430
    if bk3_level ==10:
        text "{color=#000000}[bk3_level11]" xpos 640 ypos 430
    if bk3_level ==11:
        text "{color=#000000}[bk3_level12]" xpos 640 ypos 430
    if bk3_level ==12:
        text "{color=#000000}[bk3_level13]" xpos 640 ypos 430
    if bk3_level ==13:
        text "{color=#000000}[bk3_level14]" xpos 640 ypos 430
    if bk3_level ==14:
        text "{color=#000000}[bk3_level15]" xpos 640 ypos 430
    if bk3_level ==15:
        text "{color=#000000}[bk3_level16]" xpos 640 ypos 430
    if bk3_level ==16:
        text "{color=#000000}[bk3_level17]" xpos 640 ypos 430
    if bk3_level ==17:
        text "{color=#000000}[bk3_level18]" xpos 640 ypos 430
    if bk3_level ==18:
        text "{color=#000000}[bk3_level19]" xpos 640 ypos 430
    if bk3_level ==19:
        text "{color=#000000}[bk3_level20]" xpos 640 ypos 430
    if bk3_level ==20:
        text "{color=#000000}[bk3_level21]" xpos 640 ypos 430
    if bk3_level ==21:
        text "{color=#000000}bk3_level22" xpos 640 ypos 430
    if bk3_level ==22:
        text "{color=#000000}[bk3_level23]" xpos 640 ypos 430
    if bk3_level ==23:
        text "{color=#000000}[bk3_level24]" xpos 640 ypos 430
    if bk3_level ==24:
        text "{color=#000000}[bk3_level25]" xpos 640 ypos 430
    if bk3_level ==25:
        text "{color=#000000}[bk3_level26]" xpos 640 ypos 430
    if bk3_level ==26:
        text "{color=#000000}[bk3_level27]" xpos 640 ypos 430
    if bk3_level ==27:
        text "{color=#000000}[bk3_level28]" xpos 640 ypos 430
    if bk3_level ==28:
        text "{color=#000000}[bk3_level29]" xpos 640 ypos 430
    if bk3_level ==29:
        text "{color=#000000}[bk3_level30]" xpos 640 ypos 430
    if bk3_level ==30:
        text "{color=#000000}N/A" xpos 640 ypos 430

    text "{color=#000000}You have{/color=#000000} {color=#ff0000}[bk3_level_points]{/color=#ff0000} {color=#000000}remaining bonus point(s)." xpos 320 ypos 550

screen bk3_level_up_stats:
    add "misc/bk3_scroll.jpg"
    text "{color=#000000}Level:" xpos 340 ypos 130
    text "{color=#000000}[bk3_level]" xpos 640 ypos 130
    text "{color=#000000}Health:" xpos 340 ypos 180
    text "{color=#000000}[bk3_hp]" xpos 640 ypos 180

    text "{color=#000000}Accuracy:" xpos 340 ypos 230
    text "{color=#000000}[bk3_accuracy]" xpos 640 ypos 230
    text "{color=#000000}Evasion:" xpos 340 ypos 280
    text "{color=#000000}[bk3_evade]" xpos 640 ypos 280
    text "{color=#000000}Total Experience:" xpos 340 ypos 330
    text "{color=#000000}[exp_total]" xpos 640 ypos 330
    text "{color=#000000}Until Next Level:" xpos 340 ypos 380
    if bk3_level ==1:
        text "{color=#000000}5" xpos 640 ypos 380
    if bk3_level ==2:
        text "{color=#000000}[bk3_level3]" xpos 640 ypos 380
    if bk3_level ==3:
        text "{color=#000000}[bk3_level4]" xpos 640 ypos 380
    if bk3_level ==4:
        text "{color=#000000}[bk3_level5]" xpos 640 ypos 380
    if bk3_level ==5:
        text "{color=#000000}[bk3_level6]" xpos 640 ypos 380
    if bk3_level ==6:
        text "{color=#000000}[bk3_level7]" xpos 640 ypos 380
    if bk3_level ==7:
        text "{color=#000000}[bk3_level8]" xpos 640 ypos 380
    if bk3_level ==8:
        text "{color=#000000}[bk3_level9]" xpos 640 ypos 380
    if bk3_level ==9:
        text "{color=#000000}[bk3_level10]" xpos 640 ypos 380
    if bk3_level ==10:
        text "{color=#000000}[bk3_level11]" xpos 640 ypos 380
    if bk3_level ==11:
        text "{color=#000000}[bk3_level12]" xpos 640 ypos 380
    if bk3_level ==12:
        text "{color=#000000}[bk3_level13]" xpos 640 ypos 380
    if bk3_level ==13:
        text "{color=#000000}[bk3_level14]" xpos 640 ypos 380
    if bk3_level ==14:
        text "{color=#000000}[bk3_level15]" xpos 640 ypos 380
    if bk3_level ==15:
        text "{color=#000000}[bk3_level16]" xpos 640 ypos 380
    if bk3_level ==16:
        text "{color=#000000}[bk3_level17]" xpos 640 ypos 380
    if bk3_level ==17:
        text "{color=#000000}[bk3_level18]" xpos 640 ypos 380
    if bk3_level ==18:
        text "{color=#000000}[bk3_level19]" xpos 640 ypos 380
    if bk3_level ==19:
        text "{color=#000000}[bk3_level20]" xpos 640 ypos 380
    if bk3_level ==20:
        text "{color=#000000}[bk3_level21]" xpos 640 ypos 380
    if bk3_level ==21:
        text "{color=#000000}bk3_level22" xpos 640 ypos 380
    if bk3_level ==22:
        text "{color=#000000}[bk3_level23]" xpos 640 ypos 380
    if bk3_level ==23:
        text "{color=#000000}[bk3_level24]" xpos 640 ypos 380
    if bk3_level ==24:
        text "{color=#000000}[bk3_level25]" xpos 640 ypos 380
    if bk3_level ==25:
        text "{color=#000000}[bk3_level26]" xpos 640 ypos 380
    if bk3_level ==26:
        text "{color=#000000}[bk3_level27]" xpos 640 ypos 380
    if bk3_level ==27:
        text "{color=#000000}[bk3_level28]" xpos 640 ypos 380
    if bk3_level ==28:
        text "{color=#000000}[bk3_level29]" xpos 640 ypos 380
    if bk3_level ==29:
        text "{color=#000000}[bk3_level30]" xpos 640 ypos 380
    if bk3_level ==30:
        text "{color=#000000}N/A" xpos 640 ypos 380

    if bk3_leveling_screen:
        if bk3_level_points >=1:
            text "{color=#000000}Allocate{/color=#000000} {color=#ff0000}[bk3_level_points]{/color=#ff0000} {color=#000000}remaining bonus point(s)." xpos 320 ypos 470
            textbutton "{color=#000000}Accuracy" action [SetVariable("accuracy_boost", True), Jump("bk3_points")] xpos 270 ypos 520
            textbutton "{color=#000000}Evasion" action [SetVariable("evasion_boost", True), Jump("bk3_points")] xpos 470 ypos 520
            textbutton "{color=#000000}Health" action [SetVariable("health_boost", True), Jump("bk3_points")] xpos 670 ypos 520


    textbutton "{color=#000000}Return" action [SetVariable("bk3_leveling_screen", True), Jump("bk3_after_fight_win")] xpos 470 ypos 620

screen bk3_level_up_stats2:
    add "misc/bk3_scroll.jpg"
    text "{color=#000000}Level:" xpos 340 ypos 130
    text "{color=#000000}[bk3_level]" xpos 640 ypos 130
    text "{color=#000000}Health:" xpos 340 ypos 180
    text "{color=#000000}[bk3_hp]" xpos 640 ypos 180

    text "{color=#000000}Accuracy:" xpos 340 ypos 230
    text "{color=#000000}[bk3_accuracy]" xpos 640 ypos 230
    text "{color=#000000}Evasion:" xpos 340 ypos 280
    text "{color=#000000}[bk3_evade]" xpos 640 ypos 280
    text "{color=#000000}Total Experience:" xpos 340 ypos 330
    text "{color=#000000}[exp_total]" xpos 640 ypos 330
    text "{color=#000000}Until Next Level:" xpos 340 ypos 380
    if bk3_level ==1:
        text "{color=#000000}5" xpos 640 ypos 380
    if bk3_level ==2:
        text "{color=#000000}[bk3_level3]" xpos 640 ypos 380
    if bk3_level ==3:
        text "{color=#000000}[bk3_level4]" xpos 640 ypos 380
    if bk3_level ==4:
        text "{color=#000000}[bk3_level5]" xpos 640 ypos 380
    if bk3_level ==5:
        text "{color=#000000}[bk3_level6]" xpos 640 ypos 380
    if bk3_level ==6:
        text "{color=#000000}[bk3_level7]" xpos 640 ypos 380
    if bk3_level ==7:
        text "{color=#000000}[bk3_level8]" xpos 640 ypos 380
    if bk3_level ==8:
        text "{color=#000000}[bk3_level9]" xpos 640 ypos 380
    if bk3_level ==9:
        text "{color=#000000}[bk3_level10]" xpos 640 ypos 380
    if bk3_level ==10:
        text "{color=#000000}[bk3_level11]" xpos 640 ypos 380
    if bk3_level ==11:
        text "{color=#000000}[bk3_level12]" xpos 640 ypos 380
    if bk3_level ==12:
        text "{color=#000000}[bk3_level13]" xpos 640 ypos 380
    if bk3_level ==13:
        text "{color=#000000}[bk3_level14]" xpos 640 ypos 380
    if bk3_level ==14:
        text "{color=#000000}[bk3_level15]" xpos 640 ypos 380
    if bk3_level ==15:
        text "{color=#000000}[bk3_level16]" xpos 640 ypos 380
    if bk3_level ==16:
        text "{color=#000000}[bk3_level17]" xpos 640 ypos 380
    if bk3_level ==17:
        text "{color=#000000}[bk3_level18]" xpos 640 ypos 380
    if bk3_level ==18:
        text "{color=#000000}[bk3_level19]" xpos 640 ypos 380
    if bk3_level ==19:
        text "{color=#000000}[bk3_level20]" xpos 640 ypos 380
    if bk3_level ==20:
        text "{color=#000000}[bk3_level21]" xpos 640 ypos 380
    if bk3_level ==21:
        text "{color=#000000}bk3_level22" xpos 640 ypos 380
    if bk3_level ==22:
        text "{color=#000000}[bk3_level23]" xpos 640 ypos 380
    if bk3_level ==23:
        text "{color=#000000}[bk3_level24]" xpos 640 ypos 380
    if bk3_level ==24:
        text "{color=#000000}[bk3_level25]" xpos 640 ypos 380
    if bk3_level ==25:
        text "{color=#000000}[bk3_level26]" xpos 640 ypos 380
    if bk3_level ==26:
        text "{color=#000000}[bk3_level27]" xpos 640 ypos 380
    if bk3_level ==27:
        text "{color=#000000}[bk3_level28]" xpos 640 ypos 380
    if bk3_level ==28:
        text "{color=#000000}[bk3_level29]" xpos 640 ypos 380
    if bk3_level ==29:
        text "{color=#000000}[bk3_level30]" xpos 640 ypos 380
    if bk3_level ==30:
        text "{color=#000000}N/A" xpos 640 ypos 380

    if bk3_leveling_screen:
        if bk3_level_points >=1:
            text "{color=#000000}Allocate{/color=#000000} {color=#ff0000}[bk3_level_points]{/color=#ff0000} {color=#000000}remaining bonus point(s)." xpos 320 ypos 470
            textbutton "{color=#000000}Accuracy" action [SetVariable("accuracy_boost", True), Jump("bk3_points")] xpos 270 ypos 520
            textbutton "{color=#000000}Evasion" action [SetVariable("evasion_boost", True), Jump("bk3_points")] xpos 470 ypos 520
            textbutton "{color=#000000}Health" action [SetVariable("health_boost", True), Jump("bk3_points")] xpos 670 ypos 520


    textbutton "{color=#000000}Return" action [SetVariable("bk3_leveling_screen", True), Jump("bk3_maze_start")] xpos 470 ypos 620


label bk3_points:
    $ accuracy_predict = bk3_accuracy+1
    $ evasion_predict = bk3_evade + 1
    $ health_predict = bk3_hp + 5
    show screen bk3_level_up_stats
    if accuracy_boost:
        $ bk3_accuracy +=1
        $ bk3_level_points -=1
        $ accuracy_boost = False
        call screen bk3_level_up_stats











    if evasion_boost:
        $ bk3_evade +=1
        $ bk3_level_points -=1
        $ evasion_boost = False
        call screen bk3_level_up_stats











    if health_boost:
        $ bk3_hp +=5
        $ bk3_level_points -=1
        $ health_boost = False
        call screen bk3_level_up_stats
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
