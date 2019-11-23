








init python:
    def eyewarp(x):
        return x**1.33
    eye_open = ImageDissolve("eye.png", 1.5, ramplen=128, reverse=False, time_warp=eyewarp)
    eye_shut = ImageDissolve("eye.png", 1, ramplen=128, reverse=True, time_warp=eyewarp)
    eye_open2 = ImageDissolve("eye.png", 1, ramplen=128, reverse=False, time_warp=eyewarp)






image firetank1:
    "battle/bk3_fire_tank.png"
    2.5
    "battle/bk3_fire_tank_attack.png"
    2.5
    repeat

image firetank2:
    "battle/bk3_fire_tank_attack.png"
    2.5
    "battle/bk3_fire_tank.png"
    2.5
    repeat

image hypno_light:
    "memory_dreams/circle1.png"
    0.3
    "memory_dreams/circle2.png"
    0.3
    repeat

image emberisland_cloud1:
    "emberisland/emberisland_cloud.png"
    xpos 1200
    linear 14 xpos -920

    5
    repeat





image crab1_crab1 = LiveComposite(
    (1000, 720),
    (0, 0), ConditionSwitch(
        "crab1_type == '1'", "emberisland/crab_1.png",
        "crab1_type == '2'", "emberisland/strongcrab_1.png",
        "crab1_type == '3'", "emberisland/legendcrab_1.png",
        "crab1_type == '4'", "emberisland/bessiecrab_1.png",
        "crab1_type == '5'", "emberisland/muskycrab_1.png",
        "crab1_type == '6'", "emberisland/stankcrab_1.png",
        "crab1_type == '7'", "emberisland/aqua1.png",
        "crab1_type == '8'", "emberisland/gray1.png",
        "crab1_type == '9'", "emberisland/green1.png",
        "crab1_type == '10'", "emberisland/orange1.png",
        "crab1_type == '11'", "emberisland/purple1.png",
        "True", "emberisland/aqua1.png",),
    (0, 0), ConditionSwitch(
        "crab1_rarity == 'n'", "transparent.png",
        "crab1_rarity == 'r'", "misc/rare_star.png",
        "crab1_rarity == 'e'", "misc/epic_star.png",
        "crab1_rarity == 'l'", "misc/legend_star.png",
        ),
    )


image crab1_crab2 = LiveComposite(
    (1000, 720),
    (0, 0), ConditionSwitch(
        "crab1_type == '1'", "emberisland/crab_2.png",
        "crab1_type == '2'", "emberisland/strongcrab_2.png",
        "crab1_type == '3'", "emberisland/legendcrab_2.png",
        "crab1_type == '4'", "emberisland/bessiecrab_2.png",
        "crab1_type == '5'", "emberisland/muskycrab_2.png",
        "crab1_type == '6'", "emberisland/stankcrab_2.png",
        "crab1_type == '7'", "emberisland/aqua2.png",
        "crab1_type == '8'", "emberisland/gray2.png",
        "crab1_type == '9'", "emberisland/green2.png",
        "crab1_type == '10'", "emberisland/orange2.png",
        "crab1_type == '11'", "emberisland/purple2.png",
        "True", "emberisland/aqua1.png",),
    (0, 0), ConditionSwitch(
        "crab1_rarity == 'n'", "transparent.png",
        "crab1_rarity == 'r'", "misc/rare_star.png",
        "crab1_rarity == 'e'", "misc/epic_star.png",
        "crab1_rarity == 'l'", "misc/legend_star.png",
        ),
    )

image crab1_shuffle:
    "crab1_crab1"
    0.4
    "crab1_crab2"
    0.4
    repeat

image iroh_slide = LiveComposite(
    (1000, 720),
    (0, 0), "bk3/iroh/idles/body.png",
    (0, 0), "bk3/iroh/idles/arm_lap2.png",
    (0, 0), "bk3/iroh/idles/surprise.png",
    )

image naga_chibi:
    "bk3/naga/chibi/nagachibi_1.png"
    1
    "bk3/naga/chibi/nagachibi_2.png"
    1
    repeat

image toph_ripples:
    "misc/toph_ripple1.png"
    0.1
    "misc/toph_ripple2.png"
    0.1
    "misc/toph_ripple3.png"
    0.1
    "misc/toph_ripple4.png"
    0.1
    "misc/toph_ripple5.png"
    0.1
    "misc/toph_ripple6.png"
    0.2
    "misc/toph_ripple7.png"
    0.3

image toph_ripples2:
    "misc/toph_ripple1.png"
    0.1
    "misc/toph_ripple2.png"
    0.1
    "misc/toph_ripple3.png"
    0.1
    "misc/toph_ripple4.png"
    0.1
    "misc/toph_ripple5.png"
    0.1
    "misc/toph_ripple6.png"
    0.2
    "misc/toph_ripple7.png"
    0.5

image bk_candle_flame:
    "misc/candle_flame1.png"
    0.75
    "misc/candle_flame2.png"
    0.75
    repeat

init:
    $ begin_scams = False
    $ earthbending = 0
    $ emoney = 0
    $ ecalendar = 1
    $ cheat_unlock = False
    $ solo_dicecups = False
    $ fountain_pee = False
    $ katara_found = False
    $ scams = 0
    $ hammer_game = False
    $ dice_game = False
    $ bk3_shady_met = False
    $ bk3_wood =0
    $ bk3_steel =0
    $ house_wood = False
    $ house_steel = False
    $ house_built = False
    $ quest1 = False
    $ quest2 = False
    $ quest3 = False
    $ quest4 = False
    $ quest5 = False
    $ quest6 = False
    $ quest7 = False
    $ quest8 = False
    $ we_poor = True
    $ bk3_journal = False
    $ bk3_stats = False
    $ bk3_village_access = False

    $ village_dev_explain = False
    $ village_dev_explain1 = False

    $ bk3_day = True
    $ tophs_home = 1

    $ position_1 = False
    $ position_2 = False
    $ position_3 = False
    $ position_4 = False
    $ position_5 = False
    $ position_6 = False
    $ position_7 = False
    $ position_8 = False

    $ avatar_shack_access = True
    $ hospital_building_access = True
    $ tophs_home_access = True
    $ shop_building_access = True
    $ tavern_shack_access = True
    $ brothel_building_access = True

    $ avatar_shack = 0
    $ hospital_building = 0
    $ shop_building = 0
    $ tavern_shack = 0


    $ dap1 = Character('daphne', show_side_image = "maze/sp_prisonbitch_sbox.png", window_right_padding=280, show_two_window=True, who_xpos=36)
    $ dap2 = Character('daphne', window_right_padding=280, show_two_window=True, who_xpos=36)
    $ strangegirl = Character("strange girl", color="#000000", window_right_padding=280, show_two_window=True, who_xpos=36)
    $ ct = Character("Ajala", color="#000000", window_right_padding=280, show_two_window=True, who_xpos=36)
    $ girl = Character("girl", color="#000000", window_right_padding=280, show_two_window=True, who_xpos=36)
    $ ju = Character("june", color="#000000", window_right_padding=280, show_two_window=True, who_xpos=36)
    $ suki = Character("suki", color="#000000", window_right_padding=280, show_two_window=True, who_xpos=36)
    $ ty = Character("ty lee", color="#000000", window_right_padding=280, show_two_window=True, who_xpos=36)
    $ anka = Character("anka", color="#000000", window_right_padding=280, show_two_window=True, who_xpos=36)
    $ jin = Character("jin", color="#000000", window_right_padding=280, show_two_window=True, who_xpos=36)
    $ skye = Character("skye", color="#000000", window_right_padding=280, show_two_window=True, who_xpos=36)
    $ cus = Character("customer", color="#000000", window_right_padding=280, show_two_window=True, who_xpos=36)
    $ sok = Character("sokka", color="#000000", window_right_padding=280, show_two_window=True, who_xpos=36)
    $ cn = Character("chibi naga", color="#000000", window_right_padding=280, show_two_window=True, who_xpos=36)
    $ nag = Character("nagina", color="#000000", window_right_padding=280, show_two_window=True, who_xpos=36)
    $ pop = Character("poppy", color="#000000", window_right_padding=280, show_two_window=True, who_xpos=36)
    $ to_n = Character('toph', color="#000000", show_side_image = "bk3/toph/sidebox/toph_sbox_neutral.png", window_right_padding=280, show_two_window=True, who_xpos=36)
    $ to_l = Character('toph', color="#000000", show_side_image = "bk3/toph/sidebox/toph_sbox_laugh.png", window_right_padding=280, show_two_window=True, who_xpos=36)
    $ to_d = Character('toph', color="#000000", show_side_image = "bk3/toph/sidebox/toph_sbox_doubt.png", window_right_padding=280, show_two_window=True, who_xpos=36)
    $ to_bs = Character('toph', color="#000000", show_side_image = "bk3/toph/sidebox/toph_sbox_blushsmile.png", window_right_padding=280, show_two_window=True, who_xpos=36)
    $ to_a = Character('toph', color="#000000", show_side_image = "bk3/toph/sidebox/toph_sbox_angry.png", window_right_padding=280, show_two_window=True, who_xpos=36)
    $ to_p = Character('toph', color="#000000", show_side_image = "bk3/toph/sidebox/toph_sbox_annoyed.png", window_right_padding=280, show_two_window=True, who_xpos=36)
    $ ek = Character("earth king", color="#000000", window_right_padding=280, show_two_window=True, who_xpos=36)
    $ dl1 = Character("dai lee 1", color="#000000", window_right_padding=280, show_two_window=True, who_xpos=36)
    $ dl2 = Character("dai lee 2", color="#000000", window_right_padding=280, show_two_window=True, who_xpos=36)
    $ fg = Character("fire soldier", color="#000000", window_right_padding=280, show_two_window=True, who_xpos=36)
    $ cbg = Character("cabbage guy", color="#000000", window_right_padding=280, show_two_window=True, who_xpos=36)
    $ k3_n = Character('katara', color="#000000", show_side_image = LiveComposite(
        (1000, 720),
        (750, 450), "katara/k_sidebox_fl_sgear.png"), window_right_padding=280, show_two_window=True, who_xpos=36)
    $ k3_p = Character('katara', color="#000000", show_side_image = LiveComposite(
        (1000, 720),
        (750, 450), "katara/k_sidebox_fl_sgear.png",
        (750, 450), "katara/k_sidebox_fl_pissed.png"), window_right_padding=280, show_two_window=True, who_xpos=36)
    $ k3_h = Character('katara', color="#000000", show_side_image = LiveComposite(
        (1000, 720),
        (750, 450), "katara/k_sidebox_fl_sgear.png",
        (750, 450), "katara/k_sidebox_fl_happy.png"), window_right_padding=280, show_two_window=True, who_xpos=36)
    $ k3_s = Character('katara', color="#000000", show_side_image = LiveComposite(
        (1000, 720),
        (750, 450), "katara/k_sidebox_fl_sgear.png",
        (750, 450), "katara/k_sidebox_fl_serious.png"), window_right_padding=280, show_two_window=True, who_xpos=36)
    $ k3_u = Character('katara', color="#000000", show_side_image = LiveComposite(
        (1000, 720),
        (750, 450), "katara/k_sidebox_fl_sgear.png",
        (750, 450), "katara/k_sidebox_fl_unhappy.png"), window_right_padding=280, show_two_window=True, who_xpos=36)
    $ bk3c = Character("customer", color="#070000",show_side_image = Image("bk3/suki/barblow/customer.png", xalign = 1.0, yalign = 1.0), window_right_padding=220, show_two_window=True, who_xpos=36)


    $ village_dev_explain2 = False
    $ caught_peeking = False
    $ caught_peeking1 = False
    $ fountain_pee2 = False
    $ build_the_shack = False
    $ hammer_game2 = False
    $ earth_training = False
    $ bk3_tavern_built = False
    $ bk3_tavern_built1 = False
    $ bk3_tavern_built2 = False
    $ earth_tavern_start = False
    $ toph_swim_talk = False
    $ katara_top_nude = False
    $ katara_bottom_nude = False
    $ toph_top_nude = False
    $ toph_bottom_nude = False
    $ dice_game2 = False
    $ first_lake_visit = False
    $ village_store_start = False
    $ village_store_build = False
    $ bk3_store_built = False
    $ after_store_training = False
    $ katara_blowjob_holdhead = False
    $ bk3_manapotions = 1
    $ maze_fight_tutorial = False
    $ maze_tutorial1 = False
    $ maze_tutorial2 = False
    $ maze_tutorial3 = False
    $ first_maze_fight = False
    $ obsidian =0
    $ occupied_room = 0
    $ first_maze_girl = False
    $ first_maze_girl_escape = False
    $ hospital_build = False
    $ hospital_built = False
    $ heal_maze_girl = False
    $ get_posters = False
    $ got_posters = False
    $ market_stroll = 0
    $ bk3_slave = False
    $ toph_massage_nude = False
    $ toph_massage =0
    $ crab1 = False
    $ crab1_name = "crab1"
    $ laogai_travel = False
    $ maze_music_on = False
    $ shady_explain = False

    $ crab1_type = "1"
    $ crab1_rarity = "1"

    $ first_arena_match = False

    $ first_maze_key = False
    $ june_money = False
    $ june_free = False
    $ toph_massaged = False
    $ toph_busty = False
    $ june_convo = False
    $ june_talk = 0

    $ maze_sections = 0

    $ eb6_self_convo = False

    $ suki_free = False
    $ suki_loose = False
    $ mushroom_cloud = False

    $ cartoon_school_convo = False
    $ cartoon_home_convo = False
    $ cartoon_adventure = False

    $ room23_fight = False
    $ room56_fight = False
    $ room59_fight = False

    $ suki_hospital = 0
    $ hypnoroom = "none"
    $ suki_hypno_talk = False
    $ joodee_tits = 0
    $ joodee_trigger = 0
    $ suki_hypno = 0
    $ first_suki_hypno_1 = False
    $ first_suki_hypno_2 = False
    $ first_suki_hypno_3 = False

    $ brothel_built = False
    $ brothel_building = 0
    $ wench_outfit = False
    $ suki_hypno_today = False
    $ suki_brothel = False
    $ suki_brothel_talk = False

    $ a_confused = False
    $ a_weakened = False
    $ iroh_fun_battle = False
    $ iroh_battle_count = 0

    $ june_convo_today = False
    $ june_hypno = 0
    $ june_hypno_1 = False
    $ june_hypno_2 = False
    $ june_wench_no = False

    $ arena_salts = 0
    $ arena_antidote = 0
    $ arena_steroid = 0
    $ bk3_tylee_met = False
    $ bk3_tylee_surprise = False

    $ toph_titjob = False
    $ toph_titjob2 = False
    $ toph_boobjob_tits = 'small'

    $ scam_distraction = 1
    $ kyoshi_outfit_talk = False
    $ skull_obsidian = False
    $ suki_sexual_favor = False
    $ crab1_hp = 24
    $ shop_building2_talk = False

    $ iroh_battle_convo = False
    $ suki_dildone = False

    $ kyoshi_dildo_key = False

    $ rarity_stones = 0
    $ rarity_happening = False
    $ crab_hunt2 = False

    $ bk3_anka = False
    $ anka_arena_battle = False

    $ toph_bikini = False
    $ toph_footjob = False
    $ toph_blackmail = 0

    $ ajala_jin_lesson = False
    $ ct_hypno2_1 = False
    $ ct_hypno2_2 = False
    $ ct_hypno2_3 = False

    $ jin_jasmine_met = False

    $ toph_blowjob = False

    $ jin_prison_room = False
    $ kyoshi_suki_penetrate = "dildo"
    $ find_joodee_help = False
    $ june_pubes = "bush"
    $ get_squanchy_talk = False
    $ june_thighs = False
    $ june_thigh_boss = True
    $ toph_public = 0
    $ ty_lee_brothel = False
    $ peasant_slut = False
    $ peasant_slut_hired = False
    $ tylee_brothel_watch = 0
    $ skye_today = False
    $ first_naga_bj = False
    $ earth_riddles = 0
    $ toph_sex = False
    $ gran_scare = False
    $ naga_eyes_begin = False
    $ naga_toph_old = 0
    $ katara_blowjob_water = True
    $ toph_clean_sex = False
    $ toph_katara_chair = 0
    $ toph_drunk1 = False
    $ drunk_bar = 1
    $ ty_balance_fucked = False
    $ kitten_gear = False
    $ jin_hypno = 0
    $ joodee_fuck = 0
    $ iroh_panty_hunt = 0
    $ jasmine_cus = 0
    $ jin_sucked = False
    $ toph_tunnel_training = 0
    $ snake_click = 0
    $ toph_drink_talk = False
    $ ajala_says_hypno_jin = False
    $ room97_obsidian = False
    $ june4talk1 = False
    $ june4talk2 = False
    $ jin_hypno6_talk = False
    $ ajala_jin_hypno = 0
    $ joodee_insem = False
    $ tavern_3 = False
    $ skull_obsidian2 = False
    $ nagas_eyes = 1
    $ tiny_naga_addressed = False
    $ suki_fucked = False
    $ ty_suki_skye_anal = False
    $ suki_final_hypno = False
    $ jin_fucked = False
    $ bk3name = "aang"
    $ hospital_upgrade_talk = False
    $ bk3_handjob = 0
    $ rescue_toph_redirect = False
    $ appa_free = False
    $ toph_free = False
    $ naga_battle = False
    $ nagina_free = False
    $ toph_mom_fucked = False
    $ toph_mom_fucked2 = False
    $ iroh_final_talk = False
    $ tophs_home_access = True
    $ june_fucked = False
    $ toph_slut = 0
    $ toph_footslut1 = False
    $ toph_footslut2 = False
    $ toph_blowslut = False
    $ toph_sexslut = False
    $ toph_analslut = False
    $ toph_slut_news = False
    $ toph_greeting = False
    $ sewercrab_win = False
    $ toph_footjob2_nude = False





    $ june_sympathy = 0
    $ laogai_travel = False
    $ sb = Character("smellerbee", color="#000000", window_right_padding=280, show_two_window=True, who_xpos=36)
    $ june_freed = False
    $ toph_face_touch = False
    $ toph_angry = 0
    $ toph_chat = 0
    $ toph_points = 0
    $ toph_face_touch = 0
    $ june_brothel = False
    $ june_brothel_talk = False
    $ toph_titplay = 0
    $ party_plan_explained = False
    $ party_complete = False
    $ katara_party_fuck = False
    $ suki_freed = False
    $ suki_headlocking = False
    $ hpunch2 = Move((5, 0), (-5, 0), .10, bounce=True, repeat=True, delay=.275)
    $ suki_love_met = False
    $ meangirls_maze_start = False
    $ brothel_quest = 0
    $ june_forced = False
    $ love_hypnosis_room = False
    $ toph_walk_talk = False
    $ lovehousefire = 0
    $ housefire_wins = 0
    $ shadygone = False
    $ love_suki_talk = False
    $ suki_joodee = False
    $ suki_visited_today = False
    $ juneshadytalk = False
    $ joodee_revenge = False
    $ irohshadytalk = False
    $ suki_bar_talk = False
    $ toph_comfort_talk = False
    $ mean_girls_quest = False
    $ shop_book_talk = False
    $ footjob_book = False
    $ market_book_talk = False
    $ iroh_book_talk = False
    $ june_book_talk = False
    $ toph_last_night = False
    $ toph_fixhouse = False
    $ suki_lantern_explain = False
    $ first_shady_delivery = False
    $ toph_footjob = 0
    $ suki_tavern_bartender = False
    $ love_suki_hypno = 0
    $ love_june_hypno = 0
    $ love_jd_hypno = 0
    $ suki_dl_tits = False
    $ suki_hypno_menu = 0
    $ suki_hypno_today = False
    $ suki_raid_talk = False
    $ suki_plan = False
    $ jasmine_raid = False
    $ fountain_raid = False
    $ palace_raid = False
    $ home_raid = False
    $ arena_raid = False
    $ market_raid = False
    $ suki_mast = False
    $ june_madam_outfit = False
    $ june_available = False
    $ love_toph_bikini = False
    $ madness_spirit = False
    $ love_jin_freed = False
    $ love_jin_brothel = False
    $ june_hypno_menu = 0
    $ june_hypno_today = False
    $ jin_brothel_talk = False
    $ laundry_obsidian = False
    $ suki_mast_admit = False
    $ suki_toph_ass = False
    $ jd_apologize = False
    $ helping_june_convo = False
    $ jd_hypno_today = False
    $ jd_hypno_menu = 0
    $ smellerbee_fountain = False
    $ smellerbee_gone = False
    $ june_dl_tits = False
    $ toph_licking = False
    $ love_toph_bj_facial = False
    $ suki_revenge_talk = False
    $ love_naga_eyes = False
    $ katara_upgrade_talk = False
    $ katara_upgrade_talk2 = False
    $ ty_hospital = False
    $ june_home_talk = False
    $ toph_obsidian_talk = False
    $ brothel_sign_thought = False
    $ tylee_board = False
    $ suki_tylee = 0
    $ dai_lee_hit = False
    $ suki_ty_palace = 0
    $ dl_timer_range = 0
    $ dl_timer_jump = 0
    $ find_suki_self = False
    $ dl_slow_blows = 0
    $ shady_obsidian = False
    $ shady_battle_talk = False
    $ jd_map = False
    $ love_bk3_map = False
    $ first_arena_fought = False
    $ suki_ty_hospital = 0
    $ love_suki_sex = False
    $ bk3_jd_dungeon = False
    $ jd_free = False
    $ jd_free_hospital = False
    $ jd_house = False
    $ jd_maid_outfit = False
    $ jd_obsidian = False
    $ jd_house_addressed = False
    $ jin_quick_talk =0
    $ jin_present = 0
    $ jin_love_bj = False
    $ mg_reward = False
    $ june_light = 0
    $ toph_back_disappear = 0
    $ ty_foot_offer = False
    $ love_toph_sex = False
    $ jin_loveblowjob = False
    $ love_june_fast = False
    $ bk3_rug_coins = False
    $ bk3_cushion2_coins = False
    $ bk3_cushion1_coins = False
    $ jin_love_bj = False
    $ jd_love_chat = False
    $ bk3_shop_watch = False
    $ jeff_present = False
    $ toph_love_nightmare = False
    $ toph_walk_quest = False
    $ totf_preg = False
    $ jd_break_hypno = 0
    $ ajala_jd_hypno_fight = False
    $ ajala_jd_hypno_fight2 = False
    $ cabbage_quest = False
    $ bk3_cabbages = 0
    $ cabbage_tylee = False
    $ cabbage_cart_blow = False
    $ cabbage_watch = False
    $ haiku_battle = False
    $ iroh_market = 0
    $ love_ajala_visited = False
    $ katara_lonely = 0
    $ katara_present_ask1 = False
    $ katara_present_ask2 = False
    $ go_fish_talk = False
    $ k_gf_start_check = False
    $ go_fish_convo = 0
    $ gf_my_turn = False
    $ gf_first_win = False
    $ totk_preg = False
    $ katara_cum_inside = False
    $ gf_count = 0
    $ gf_win_count = 0
    $ jin_anti_hypno_start = 0
    $ love_jin_sex = False
    $ toph_date_walk = "outside"
    $ toph_say_love = False
    $ ty_cabbages = 0
    $ love_ty_bj = False
    $ love_ty_sex_talk = False
    $ love_ty_sex_quest = 0
    $ love_naga_claw = False
    $ love_toph_anal1 = False
    $ love_toph_anal2 = False
    $ love_begin_snake_dream = False
    $ time_reset = False
    $ suki_bar_blow = 0
    $ bk3_love_bartending = 0
    $ bk3_bar_memory = 0
    $ bk3_bar_wins =0
    $ bk3_bar_level = 1
    $ bk3_bar_payout = 0
    $ bk3_su_bb_player = "True"
    $ love_toph_freed = False
    $ love_appa_freed = False
    $ love_jet_freed = False
    $ love_naga_battle = False
    $ love_nagina_free = False
    $ love_smellerbee_sex = False

    $ love_kat_preg_sex = False
    $ love_tylee_rub = False
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
