
















init python:
    class Room:
        def __init__(self, roomnr, rname, north, south, west, east, maze_enemy, maze_bg, sp_item, sp_content, sp_used,visit,special_touch,special_touch2):
            self.roomnr = roomnr
            self.rname = rname
            self.north = north
            self.south = south
            self.west = west
            self.east = east 
            self.maze_enemy = maze_enemy
            self.maze_bg = maze_bg
            self.sp_item = sp_item
            self.sp_content = sp_content
            self.sp_used = sp_used
            self.visit = visit
            self.special_touch = special_touch
            self.special_touch2 = special_touch2

init:




    $ bk3_lifepotions = 1
    $ bk3_allow_waterbending = False
    $ bk3_allow_firebending = False
    $ bk3_allow_earthbending = False

    $ bk3_maze_fightswon = 0
    $ bk3_maze_fightslost = 0
    $ bk3_inseminations = 0


    $ bk3_update_maze = 0

    $ earth_bending = 0
    $ emoney = 0

    $ while_counter = 0

    $ maze_follower="none"
    $ juneshackles_key = False
    $ prisonbitch_key = False
    $ prisonbitch_freed = False
    $ prisonbitch_reward = False
    $ prisonthighs_freed = False
    $ prisonthighs_reward = False

    $ naga_eyes = False

    $ sp_maze_key1 = False
    $ sp_kyoshi_dildo = False
    $ sp_kyoshi_dildo_key = False

    $ sp_item_xpos = 1
    $ sp_item_ypos = 1
    $ sp_item_width = 220
    $ sp_item_height = 220



    $ bk3_level = 1
    $ bk3_accuracy = 1
    $ bk3_evade = 1
    $ bk3_hp = 90
    $ bk3_exp = 0
    $ bk3_enemy_level = 1
    $ exp_total = 0
    $ level_up = False
    $ bk3_moves = 6
    $ bk3_fire_remaining = bk3_moves
    $ bk3_water_remaining = bk3_moves
    $ bk3_earth_remaining = bk3_moves
    $ bk3_level_points = 0
    $ accuracy_boost = False
    $ evasion_boost = False
    $ health_boost = False
    $ bk3enemylevel=2

    $ bk3_leveling_screen = True


    image sp_double_torches:
        xpos 500 ypos 550
        "maze/sp_twotorches_1.png"
        0.4
        "maze/sp_twotorches_2.png"
        0.4
        repeat

    image sp_pillar_torches:
        "maze/sp_pillartorch_1.png"
        0.4
        "maze/sp_pillartorch_2.png"
        0.4
        repeat

    image sp_steam:
        "maze/sp_we_steam1.png"
        0.5
        "maze/sp_we_steam2.png"
        0.5
        repeat

    image sp_spider_ani:
        "maze/sp_spider_1.png"
        0.4
        "maze/sp_spider_2.png"
        0.4
        repeat
    image sp_skullflame:
        "maze/sp_skullflame_1.png"
        0.3
        "maze/sp_skullflame_2.png"
        0.3
        repeat

    image open_treasurechest = "maze/open_treasurechest.png"
    image closed_treasurechest = "maze/closed_treasurechest.png"
    image npc_prisoner1 = "maze/sp_prisoner_1.png"
    image npc_prisoner2 = "maze/sp_prisoner_2.png"
    image npc_emptyshackles = "maze/sp_emptyshackles.png"

    image prisonbitch_nude = "maze/sp_prisonbitch.png"
    image prisonbitch_idle = LiveComposite(      
        (1000, 720),        
        (0, 0), "maze/sp_prisonbitch.png",
        (0, 0), "maze/sp_prisonbitch_clothes.png",
        )

    image prisonbitch_sbox = "maze/sp_prisonbitch_sbox.png"

    image prisonthighs_idle = "maze/sp_prisonthighs.png"
    image prisonthighs_sbox = "maze/sp_prisonthighs_sbox.png"

    define prithi0 = Character("Naked girl", color="#000000",  show_side_image = Image("transparent.png", xalign = 0, yalign = 0.96), window_right_padding=280, show_two_window=True, who_xpos=36)
    define prithi1 = Character("Naked girl", color="#000000",  show_side_image = Image("maze/sp_prisonthighs_sbox.png", xalign = 0, yalign = 0.96), window_right_padding=280, show_two_window=True, who_xpos=36)

    define pribit0 = Character("Naked girl", color="#000000",  show_side_image = Image("transparent.png", xalign = 0, yalign = 0.96), window_right_padding=280, show_two_window=True, who_xpos=36)
    define pribit1 = Character("Naked girl", color="#000000",  show_side_image = Image("maze/sp_prisonbitch_sbox.png", xalign = 0, yalign = 0.96), window_right_padding=280, show_two_window=True, who_xpos=36)


    image maze_directions = "maze/directions.png"
    image maze_nagaeyes = "maze/maze2_nagaeyes.png"

    image sp_n_escapehole = "maze/sp_n_crackinwall.png"
    image sp_we_straw = "maze/sp_we_straw1.png"
    image sp_we_grate = "maze/sp_we_grate.png"
    image sp_maze_grateroot = LiveComposite(      
        (1000, 720),        
        (0, 0), "maze/sp_we_grate.png",
        (0, 0), "maze/sp_northwall_pillars.png",
        (0, 0), "maze/sp_roots_1.png",
        )
    image sp_maze_pillarroot = LiveComposite(      
        (1000, 720),  
        (0, 0), "maze/sp_northwall_pillars.png",
        (0, 0), "maze/sp_roots_1.png",
        )
    image sp_wn_pillar = LiveComposite(      
        (1000, 720),
        (0, 0), "maze/sp_eastwall_1.png",
        )

    image sp_eastwall_2 = "maze/sp_eastwall_2.png"
    image sp_eastwall_3 = "maze/sp_eastwall_3.png"

    image sp_ceiluber = "maze/sp_ceiling_rubble.png"
    image sp_covegirl_0 = "maze/sp_covegirl_0.png"
    image sp_covegirl_1 = "maze/sp_covegirl_1.png"
    image sp_roots_1 = "maze/sp_roots_1.png"
    image sp_roots_2 = "maze/sp_roots_2.png"
    image sp_roots_3 = "maze/sp_roots_3.png"
    image sp_roots_4 = "maze/sp_roots_4.png"
    image sp_roots_5 = "maze/sp_roots_5.png"

    image sp_westwall_1 = "maze/sp_westwall_1.png"

    image sp_e_brokenwall = "maze/sp_e_brokenwall.png"

    image sp_e_mdoor_1 = LiveComposite(      
        (1000, 720),
        (0, 0), "maze/sp_e_door_1.png",
        (0, 0), "maze/sp_e_metaldoor_2_open.png",)

    image sp_e_mdoor_2 = LiveComposite(      
        (1000, 720),
        (0, 0), "maze/sp_e_door_1.png",
        (0, 0), "maze/sp_e_metaldoor_2_closed.png")

    image sp_e_walldoor = "maze/sp_e_door_2.png"

    image sp_northwall_pillars = "maze/sp_northwall_pillars.png"

    image sp_ns_md_open = "maze/sp_ns_metaldoor_open.png"
    image sp_ns_md_closed = "maze/sp_ns_metaldoor_closed.png"


    image sp_nwallpillar_combo1 = LiveComposite(      
        (1000, 720),
        (0, 0), "sp_westwall_1",
        (0, 0), "sp_northwall_pillars",)

    image sp_no_special = "maze/none.png"

    image sp_w_wallblocked = "maze/sp_westwall_breakthrough0.png"
    image sp_we_crack1 = "maze/sp_we_crack1.png"
    image sp_n_wallblocked = "maze/maze_blockedn.png"

    image sp_ne_floortiles_1 = "maze/sp_floortiles_1.png"
    image sp_ne_floortiles_2 = "maze/sp_floortiles_2.png"
    image sp_we_floortiles_3 = "maze/sp_floortiles_3.png"

    image sp_prisoner_1 = "maze/sp_prisoner_1.png"

    image sp_n_doorway1 = LiveComposite(      
        (1000, 720),
        (0, 0), "maze/sp_n_doorway_1.png",
        (0, 0), "maze/sp_northwall_pillars.png",
        )
    image sp_n_closeddoors_1 = LiveComposite(      
        (1000, 720),
        (0, 0), "maze/sp_n_doorway_1.png",
        (0, 0), "maze/sp_n_closeddoors.png",
        )
    image sp_n_opendoors_1 = LiveComposite(      
        (1000, 720),
        (0, 0), "maze/sp_n_doorway_1.png",
        (0, 0), "maze/sp_n_opendoors.png",
        )


    image sp2_buttwall = "maze/sp2_buttwall.png"
    image sp2_wallbuttgirl = "maze/sp2_wallbuttgirl.png"


label bk3_init_maze_1:


    $ room0  = Room(0,"room0",  1  , -1    , -1 , -1,    False,"maze/maze_nswe.jpg",         False ,    0 , False, 0,   "sp_no_special"         ,"sp_no_special")
    $ room1  = Room(1,"room1",  2  ,  0    , -1 , -1,    False,"maze/maze_ns_0.jpg",         False ,    0 , False, 0,   "sp_roots_1"            ,"sp_no_special")
    $ room2  = Room(2,"room2",  3  ,  1    , 11 , -1,    False,"maze/maze_nsw_1.jpg",        False ,    0 , False, 0,   "sp_ne_floortiles_2"    ,"sp_no_special")
    $ room3  = Room(3,"room3",  6  ,  2    ,  4,   5,    False,"maze/maze_nswe.jpg",         False ,    0 , False, 0,   "sp_ne_floortiles_1"    ,"sp_no_special")
    $ room4  = Room(4,"room4", -1 ,  -1    , 15,   3,    False,"maze/maze_we.jpg",           True  ,   40 , False, 0,   "sp_we_floortiles_3"    ,"sp_no_special")
    $ room5  = Room(5,"room5", -1 ,  -1    ,  3,   7,    False,"maze/maze_we.jpg",           False ,    0 , False, 0,   "sp_no_special"         ,"sp_maze_grateroot")

    $ room6  = Room(6,"room6", 10 ,   3    , -1,  -1,    False,"maze/maze_ns_1.jpg",         False ,    0 , False, 0,   "sp_double_torches"     ,"sp_no_special")
    $ room7  = Room(7,"room7", -1 ,  -1    ,  5,   8,    False,"maze/maze_we.jpg",           True ,     0 , False, 0,   "sp_roots_2"            ,"sp_no_special")
    $ room8  = Room(8,"room8",  9  , -1    ,  7,  -1,    True,"maze/maze_wn_1.jpg",         False ,    0 , False, 0,   "sp_roots_3"            ,"sp_no_special")
    $ room9  = Room(9,"room9", -1  , 8     , -1,  -1,    True, "maze/maze_ns_0.jpg",         True ,     0 , False, 0,   "sp_ne_floortiles_2"    ,"sp_n_closeddoors_1")
    $ room10 = Room(10,"room10", -1  ,  6    , -1,  -1,  True, "maze/maze_ns_0.jpg",         True ,     0 , False, 0,   "sp_n_wallblocked"      ,"sp_no_special")

    $ room11 = Room(11,"room11", -1  , -1    , 12,   2,   False, "maze/maze_we.jpg",         True  ,    0 , False, 0,   "sp_we_straw"           ,"sp_no_special")
    $ room12 = Room(12,"room12", -1  , 13    , -1,  11,   False, "maze/maze_se_1.jpg",       False ,    0 , False, 0,   "sp_no_special"         ,"sp_no_special")
    $ room13 = Room(13,"room13", 12  , -1    , 14,  -1,   False, "maze/maze_wn_1.jpg",       False ,    0 , False, 0,   "sp_wn_pillar"          ,"sp_no_special")
    $ room14 = Room(14,"room14", -1  , -1    , -1,  13,   False, "maze/maze_we.jpg",         True ,     0 , False, 0,   "sp_w_wallblocked"      ,"sp_no_special")
    $ room15 = Room(15,"room15", -1  , -1    , -1,   4,   False, "maze/maze_we.jpg",         True ,     0 , False, 0,   "sp_we_crack1"          ,"sp_steam")

    $ room16 = Room(16,"room16", -1  , -1    , 66,   -1,   False, "maze/maze_ws_1.jpg",        False ,     0 , False, 0,   "sp_no_special"         ,"sp_no_special")
    $ room17 = Room(17,"room17", -1  , 10    , -1,   20,   False, "maze/maze_se_1.jpg",      False ,     0 , False, 0,   "sp_no_special"         ,"sp_no_special")
    $ room18 = Room(18,"room18", 38  , -1    , 46,   15,   False, "maze/maze2_wne_0.jpg",    False ,     0 , False, 0,   "sp_no_special"         ,"sp_no_special")
    $ room19 = Room(19,"room19", 26  , -1    , 30,   14,   False, "maze/maze_we.jpg",        False ,    0 , False, 0,   "sp_n_doorway1"         ,"sp_e_brokenwall")
    $ room20 = Room(20,"room20", 21  , -1    , 17,   -1,   False, "maze/maze_wn_1.jpg",      True ,     0 , False, 0,   "sp_no_special"         ,"sp_no_special")

    $ room21 = Room(21,"room21", -1  , 20    , 22,   54,   False, "maze/maze_ws_1.jpg",      True ,     0 , False, 0,   "sp_roots_2"            ,"sp_e_walldoor")
    $ room22 = Room(22,"room22", -1  , -1    , 23,   21,   False, "maze/maze_we.jpg",        True ,     2 , False, 0,   "sp_roots_3"            ,"sp_no_special")
    $ room23 = Room(23,"room23", -1  , -1    , 24,   22,   True, "maze/maze_we.jpg",        False ,    0 , False, 0,   "sp_roots_2"            ,"sp_no_special")
    $ room24 = Room(24,"room24", -1  , -1    , -1,   23,   False, "maze/maze_we.jpg",        True  ,    0 , False, 0,   "sp_n_closeddoors_1"    ,"sp_nwallpillar_combo1")
    $ room25 = Room(25,"room25", -1  , 24    , -1,   -1,   False, "maze/maze_s_1.jpg",       True ,     0 , False, 0,   "sp_covegirl_1"         ,"sp_pillar_torches")


    $ room26 = Room(26,"room26", 27  , 19    , -1,   -1,   False, "maze/maze_ns_2.jpg",      True ,     0 , False, 0,   "sp_ns_md_closed"       ,"sp_no_special")
    $ room27 = Room(27,"room27", -1  , 26    , 28,   -1,   False, "maze/maze_ws_1.jpg",      False ,    0 , False, 0,   "sp_no_special"         ,"sp_no_special")
    $ room28 = Room(28,"room28", -1  , -1    , 33,   27,   False, "maze/maze_we.jpg",        False ,    0 , False, 0,   "sp_no_special"         ,"sp_no_special")
    $ room29 = Room(29,"room29", -1  , -1    , -1,   26,   False, "maze/maze_s_1.jpg",       True ,     0 , False, 0,   "sp_e_mdoor_1"          ,"sp_n_escapehole")
    $ room30 = Room(30,"room30", -1  , 31    , 37,   19,   False, "maze/maze_wes_1.jpg",     False ,    0 , False, 0,   "sp_no_special"         ,"sp_roots_2")

    $ room31 = Room(31,"room31", 30  , 32    , -1,   -1,   False, "maze/maze_ns_1.jpg",      False ,    0 , False, 0,   "sp_no_special"         ,"sp_roots_3")
    $ room32 = Room(32,"room32", 31  , -1    , -1,   -1,   True, "maze/maze_n_1.jpg",        False ,    0 , False, 0,   "sp_no_special"         ,"sp_no_special")
    $ room33 = Room(33,"room33", -1  , -1    , 34,   28,   False, "maze/maze_we.jpg",        False ,    0 , False, 0,   "sp_we_grate"           ,"sp_no_special")
    $ room34 = Room(34,"room34", -1  , 35    , -1,   33,   False, "maze/maze_se_1.jpg",      False ,    0 , False, 0,   "sp_no_special"         ,"sp_no_special")
    $ room35 = Room(35,"room35", 34  , 36    , -1,   -1,   False, "maze/maze_ns_0.jpg",      False ,    0 , False, 0,   "sp_no_special"         ,"sp_no_special")

    $ room36 = Room(36,"room36", 35  , -1    , 62,   37,   False, "maze/maze_nwe_1.jpg",     False ,    0 , False, 0,   "sp_maze_pillarroot"     ,"sp_no_special")
    $ room37 = Room(37,"room37", -1  , -1    , 36,   30,   False, "maze/maze_we.jpg",        False ,    0 , False, 0,   "sp_we_floortiles_3"     ,"sp_no_special")
    $ room38 = Room(38,"room38", 39  , 18    , -1,   -1,   False, "maze/maze2_ns_0.jpg",     False ,    0 , False, 0,   "sp_no_special"          ,"sp_no_special")
    $ room39 = Room(39,"room39", 40  , 38    , -1,   -1,   True, "maze/maze2_ns_1.jpg",      False ,    0 , False, 0,   "sp_no_special"          ,"sp_no_special")
    $ room40 = Room(40,"room40", -1  , 39    , 41,   -1,   False, "maze/maze2_ws.jpg",       True ,     0 , False, 0,   "maze/box_closed.png"   ,"sp_no_special")

    $ room41 = Room(41,"room41", -1  , -1    , 42,   40,   False, "maze/maze2_we.jpg",       False ,    0 , False, 0,   "sp_no_special"         ,"sp_no_special")
    $ room42 = Room(42,"room42", -1  , 43    , 47,   41,   False, "maze/maze2_wes.jpg",      False ,    0 , False, 0,   "sp_no_special"         ,"sp_no_special")
    $ room43 = Room(43,"room43", 42  , 44    , 52,   -1,   True, "maze/maze2_wns2.jpg",      False ,    0 , False, 0,   "sp_roots_1"            ,"sp_no_special")
    $ room44 = Room(44,"room44", 43  , 45    , 51,   -1,   False, "maze/maze2_wns.jpg",      False ,    0 , False, 0,   "sp_no_special"         ,"sp_no_special")
    $ room45 = Room(45,"room45", 44  , -1    , -1,   46,   False, "maze/maze2_ne.jpg",       False ,    0 , False, 0,   "sp_no_special"         ,"sp_no_special")

    $ room46 = Room(46,"room46", -1  , -1    , 45,   18,   False, "maze/maze2_we.jpg",       False ,    0 , False, 0,   "sp_no_special"         ,"sp_no_special")
    $ room47 = Room(47,"room47", -1  , -1    , 48,   42,   False, "maze/maze2_we.jpg",       False ,    0 , False, 0,   "sp_no_special"         ,"sp_no_special")
    $ room48 = Room(48,"room48", -1  , 49    , -1,   47,   False, "maze/maze2_se.jpg",       False ,    0 , False, 0,   "sp_no_special"         ,"sp_no_special")
    $ room49 = Room(49,"room49", 48  , 50    , -1,   -1,   False, "maze/maze2_ns_2.jpg",     True ,     0 , False, 0,   "sp2_buttwall"          ,"sp_no_special")
    $ room50 = Room(50,"room50", 49  , -1    , -1,   51,   False, "maze/maze2_ne.jpg",       False ,    0 , False, 0,   "sp_no_special"         ,"sp_no_special")
    $ room51 = Room(51,"room51", -1  , -1    , 50,   44,   False, "maze/maze2_we.jpg",       False ,    0 , False, 0,   "sp_no_special"         ,"sp_no_special")
    $ room52 = Room(52,"room52", -1  , -1    , -1,   43,   False, "maze/maze2_s_1.jpg",      True ,     0 , False, 0,   "sp2_wallbuttgirl"      ,"sp_no_special")
    $ room53 = Room(53,"room53", 52  , -1    , -1,   -1,   False, "maze/maze2_nagaroom.jpg", True ,     0 , False, 0,   "maze_nagaeyes"         ,"sp_no_special")

    $ room54 = Room(54,"room54", -1  , -1    , 21,   55,   False, "maze/maze_we.jpg",        False ,     0 , False, 0,   "sp_no_special"         ,"sp_no_special")
    $ room55 = Room(55,"room55", 57  , 56    , 54,   -1,   False, "maze/maze_nsw_1.jpg",     False ,     0 , False, 0,   "sp_no_special"         ,"sp_no_special")
    $ room56 = Room(56,"room56", 55  , -1    , -1,   -1,   True, "maze/maze_n_1.jpg",       False ,     0 , False, 0,   "sp_no_special"         ,"sp_no_special")
    $ room57 = Room(57,"room57", -1  , 55    , -1,   58,   False, "maze/maze_se_1.jpg",      False ,     0 , False, 0,   "sp_no_special"         ,"sp_no_special")
    $ room58 = Room(58,"room58", 59  , -1    , 57,   -1,   False, "maze/maze_wn_1.jpg",      True ,      0 , False, 0,   "sp_eastwall_2"         ,"sp_no_special")
    $ room59 = Room(59,"room59", -1  , 58    , -1,   60,   True, "maze/maze_se_1.jpg",      False ,     0 , False, 0,   "sp_no_special"         ,"sp_no_special")
    $ room60 = Room(60,"room60", 61  , -1    , 59,   -1,   False, "maze/maze_wn_1.jpg",      False ,     0 , False, 0,   "sp_eastwall_3"         ,"sp_no_special")
    $ room61 = Room(61,"room61", -1  , 60    , -1,   -1,   False, "maze/maze_s_1.jpg",       True ,      0 , False, 0,   "sp_ceiluber"           ,"sp_no_special")

    $ room62 = Room(62,"room62", 63  , -1    , -1,   36,   False, "maze/maze_ne_1.jpg",      False ,     0 , False, 0,   "sp_roots_1"            ,"sp_no_special")
    $ room63 = Room(63,"room63", 64  , 62    , 65,   -1,   False, "maze/maze_nsw_1.jpg",     False ,     0 , False, 0,   "sp_roots_2"            ,"sp_no_special")
    $ room64 = Room(64,"room64", -1  , 63    , -1,   -1,   True, "maze/maze_s_1.jpg",        False ,     0 , False, 0,   "sp_no_special"         ,"sp_no_special")
    $ room65 = Room(65,"room65", -1  , -1    , -1,   63,   True, "maze/maze_we.jpg",         False ,     0 , False, 0,   "sp_westwall_1"         ,"sp_no_special")

    $ room66 = Room(66,"room66", 69  , -1    , 67,   16,   False, "maze/maze_nwe_1.jpg",      False ,     0 , False, 0,   "sp_no_special"         ,"sp_no_special")
    $ room67 = Room(67,"room67", 68  , -1    , -1,   66,   False, "maze/maze_ne_1.jpg",       False ,     0 , False, 0,   "sp_no_special"         ,"sp_no_special")
    $ room68 = Room(68,"room68", -1  , 67    , -1,   69,   False, "maze/maze_se_1.jpg",       False ,     0 , False, 0,   "sp_no_special"         ,"sp_no_special")
    $ room69 = Room(69,"room69", 70  , 66    , 68,   78,   False, "maze/maze_nswe.jpg",       False ,     0 , False, 0,   "sp_no_special"         ,"sp_no_special")
    $ room70 = Room(70,"room70", 71  , 69    , -1,   -1,   False, "maze/maze_ns_0.jpg",       False ,     0 , False, 0,   "sp_no_special"         ,"sp_no_special")
    $ room71 = Room(71,"room71", -1  , 70    , -1,   -1,   False, "maze/maze_ns_1.jpg",       True ,      0 , False, 0,   "sp_no_special"         ,"sp_n_closeddoors_1")

    $ room72 = Room(72,"room72", 73  , -1    , 79,   -1,   False, "maze/maze_nsw_1.jpg",      False ,     0 , False, 0,   "sp_roots_5"            ,"sp_no_special")
    $ room73 = Room(73,"room73", -1  , 72    , -1,   74,   False, "maze/maze_s_1.jpg",        False ,     0 , False, 0,   "maze/sp_e_door_1.png"  ,"sp_roots_4")
    $ room74 = Room(74,"room74", -1  , 75    , 73,   -1,   False, "maze/maze_s_1.jpg",        False ,     0 , False, 0,   "maze/sp_e_door_0.png"  ,"sp_roots_3")
    $ room75 = Room(75,"room75", 74  , 76    , -1,   -1,   False, "maze/maze_ns_0.jpg",       False ,     0 , False, 0,   "sp_no_special"         ,"sp_ne_floortiles_1")
    $ room76 = Room(76,"room76", 75  , 77    , -1,   -1,   False, "maze/maze_ns_1.jpg",       False ,     0 , False, 0,   "sp_no_special"         ,"sp_ne_floortiles_2")
    $ room77 = Room(77,"room77", 76  , 78    , -1,   -1,   False, "maze/maze_ns_3.jpg",       True ,      0 , False, 0,   "sp_no_special"   ,"maze/sp_prisoner_june.png")
    $ room78 = Room(78,"room78", 77  , -1    , 69,   -1,   False, "maze/maze_wn_1.jpg",       False ,     0 , False, 0,   "sp_no_special"         ,"sp_no_special")
    $ room79 = Room(79,"room79", 80  , -1    , -1,   72,   False, "maze/maze_w_1.jpg",        False ,     0 , False, 0,   "maze/sp_stairup_1.png"         ,"sp_no_special")
    $ room80 = Room(80,"room80", -1  , 79    , -1,   81,   False, "maze/maze_w_1.jpg",        False ,     0 , False, 0,   "maze/sp_stairdown_1.png"         ,"sp_no_special")

    $ room81 = Room(81,"room81", -1  , -1    , 80,   82,   False, "maze/maze_we.jpg",         False ,     0 , False, 0,   "sp_we_floortiles_3"         ,"sp_no_special")

    $ room82 = Room(82,"room82", -1  , 83    , 81,   -1,   False, "maze/maze_we.jpg",         False ,     0 , False, 0,   "maze/sp_cavein_1.png"         ,"sp_no_special")
    $ room83 = Room(83,"room83", -1  , -1    , -1,   -1,   False, "maze/maze_s_1.jpg",        True  ,     0 , False, 0,   "sp_ceiluber"         ,"sp_no_special")




    $ roomlist = [room0,room1, room2,room3,room4,room5,room6,room7,room8,room9, room10, room11, 
                      room12, room13, room14, room15, room16, room17, room18, room19, room20, room21, room22, room23, room24, room25,
                      room26, room27, room28, room29, room30, room31, room32, room33, room34, room35, room36, room37, room38, room39,
                      room40, room41, room42, room43, room44, room45, room46, room47, room48, room49, room50, room51, room52, room53,
                      room54, room55, room56, room57, room58, room59, room60, room61, room62, room63, room64, room65, room66, room67,
                      room68, room69, room70, room71, room72, room73, room74, room75, room76, room77, room78, room79, room80, room81,
                      room82, room83]


    $ current_room = room1
    $ previous_room = current_room

    return















label bk3_maze_start:

    hide screen earth_money_date
    if not maze_music_on:
        $ maze_music_on = True
        stop music fadeout 1
        play music "audio/Unity.mp3"

    $ bk3_level3 = 10 - exp_total
    $ bk3_level4 = 20 - exp_total
    $ bk3_level5 = 35 - exp_total
    $ bk3_level6 = 55 - exp_total
    $ bk3_level7 = 80 - exp_total
    $ bk3_level8 = 110 - exp_total
    $ bk3_level9 = 145 - exp_total
    $ bk3_level10 = 185 - exp_total
    $ bk3_level11 = 230 - exp_total
    $ bk3_level12 = 280 - exp_total
    $ bk3_level13 = 335 - exp_total
    $ bk3_level14 = 390 - exp_total
    $ bk3_level15 = 450 - exp_total
    $ bk3_level16 = 520 - exp_total
    $ bk3_level17 = 600 - exp_total
    $ bk3_level18 = 690 - exp_total
    $ bk3_level19 = 790 - exp_total
    $ bk3_level20 = 900 - exp_total
    $ bk3_level21 = 1020 - exp_total
    $ bk3_level22 = 1150 - exp_total
    $ bk3_level23 = 1290 - exp_total
    $ bk3_level24 = 1440 - exp_total
    $ bk3_level25 = 1600 - exp_total
    $ bk3_level26 = 1790 - exp_total
    $ bk3_level27 = 1990 - exp_total
    $ bk3_level28 = 2200 - exp_total
    $ bk3_level29 = 2420 - exp_total
    $ bk3_level30 = 2700 - exp_total






    if bk3_update_maze == 0:
        $ bk3_update_maze = 1
        call bk3_init_maze_1 from _call_bk3_init_maze_1














    $ current_room.visit = current_room.visit + 1



    if current_room.rname == "room1":
        if toph_tunnel_training ==1:
            jump maze_update_two

        if ty_lee_brothel and not peasant_slut:
            scene dark_tunnel
            show sp_prisonthighs
            with dissolve
            skye "hi! my name's skye!"
            skye "can you please, please get me the fuck out of here?"
            skye "pretty please with a blowjob on top?"
            y "does nobody down here wear clothes?"
            skye "not since ajala got... weird."
            skye "she keeps most female prisoners naked now for some reason."
            y "....."
            skye "anyway... get me out of here, please?"
            skye "and, i'm sure it's asking too much, but... do you have somewhere i could stay?"
            skye "i was a courtesan in omashu before i came here, so i could..."
            y "a courtesan?"
            skye "oh, sorry -- i was a {i}really{/i} slutty prostitute."
            skye "like... pro-bono boning out the ass. actually, often {i}in{/i} the ass."
            skye "i'm just a super nymphomaniac, degenerate, cock gobbling whore!"
            y "I... have a business opportunity for you."
            skye "really!?"
            skye "can i suck a lot of cock?"
            skye "i have sort of... an oral fixation."
            y "that won't be a problem."
            y "i'll take you to my village outside ba sing se."
            y "there's a brothel, and we'll put you to work."
            skye "that's amazing!"
            skye "oh, and there's no way i can thank you, but i found this pretty rock."
            $ obsidian +=1
            play sound "audio/win2.mp3"
            "you got 1 obsidian!"
            y "oh, dang. nice."
            y "come on, i'll take you to the village and meet you at the brothel."
            $ bk3_day = False
            $ peasant_slut = True
            jump bk3_village_background

        if prisonbitch_freed and not ajala_jin_lesson:
            scene dark_tunnel
            show tomc tomc01
            with dissolve
            ct "welcome back, avatar."
            y "oh, hey."
            show tomc tomc02 with dissolve
            $ renpy.pause(0.2,hard=True)
            show tomc tomc03 with dissolve
            $ renpy.pause(0.2,hard=True)
            show tomc tomc04 with dissolve
            ct "congratulations on rescuing..."
            ct "jin? was that her name?"
            y "yeah."
            y "so, what's up?"
            ct "it's my responsibility to make sure you're well trained."
            ct "which requires continued practice."
            y "oh. neat."
            ct "we'll use the equipment here, and you can hypnotize me."
            ct "once again, you are to make me say \"long feng is the true ruler of ba sing se.\""
            show tomc_angry with dissolve
            ct "and {i}only{/i} that."
            ct "understood?"
            y "yeah, yeah, i got it."
            hide tomc_angry with dissolve
            ct "good."
            y "let's do this."
            show hypno_light:
                xalign 0.0 yalign 0.5
                linear 2.0 xalign 1.0
                linear 2.0 xalign 0.0
                repeat
            show ctc
            $ renpy.pause(4.0, hard=True)
            hide ctc
            show tomc tomc06

            hide hypno_light
            with dissolve
            y "(gotta check....)"
            y "tell me... \"long feng sucks hefty choads.\""
            ct "long... feng... sucks..."
            y "...."
            y "well, that wasn't the whole thing... but good enough."
            y "so..."
            y "how many times has long feng hypnotized you?"
            ct "...never..."
            y "what? seriously?"
            y "have you ever been hypnotized?"
            ct "only... by... you..."
            y "oh. snap."
            y "why hasn't feng hypnotized you?"
            ct "he wants... to keep me... mentally untainted..."
            ct "...pure..."
            y "well that... is going to change."
            jump ct_hypno_menu2

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


        if joodee_tits ==6:
            scene dark_tunnel
            show tomc tomc01
            with dissolve
            ct "welcome back, avatar."
            y "oh, hey."
            y "did you do something to joo dee?"
            ct "....."
            ct "long feng has granted you a favor."
            y "oh?"
            ct "yes..."
            ct "he has given joo dee additional hypnosis, so that she would be more subservient to your wishes."
            ct "that is a gift to you as encouragement to excel with the girls you are \"rescuing\"."
            y "uh... well, it didn't work."
            y "and her trigger phrase stopped working."
            ct "that is purposeful."
            ct "long feng does not grant boons without an equal gesture to balance the scales."
            y "ugh. okay, what do you want?"
            ct "bring me one of these slaves."
            ct "I wish to see.... how far along they are."
            y "any one in particular?"
            ct "hm...."
            ct "that kyoshi one was quite difficult to subdue."
            ct "bring her to me."
            y "fine, i'll bring you suki."
            ct "very well...."
            $ joodee_tits +=1
            hide tomc tomc01 with dissolve
            scene black with dissolve
            jump bk3_village_background

        if joodee_tits >= 1 and joodee_trigger ==0:
            scene dark_tunnel
            show tomc tomc01
            with dissolve
            ct "avatar-"
            y "whoa! where did you come from?"
            show tomc tomc02 with dissolve
            ct "these are {i}my{/i} tunnels."
            show tomc tomc04 with dissolve
            ct "given to me by long feng himself."
            y "okay... so what do you want?"
            show tomc_angry with dissolve
            ct "i'm here to deliver a... gesture... from the grand secretariat."
            hide tomc_angry
            show tomc_blink
            with dissolve
            ct "joodee's trigger sentence is...."
            ct "\"The Earth King has invited you to Lake Laogai.\""
            hide tomc_blink with dissolve
            ct "got it?"
            y "i think so..."
            show tomc tomc01 with dissolve
            ct "good."
            $ joodee_trigger = 1
            hide tomc tomc01 with dissolve
            y "nice."

        if current_room.visit == 1:
            scene black
            scene dark_tunnel
            show toi toi200
            with dissolve
            t "Okay, Twinkletoes, you're gonna take lead here."
            t "i'll back you up."
            y "what? why me first?"
            t "because i haven't come around to katara's teaching style yet, and i believe in not being a sissy."
            t "so get a move on!"
            hide toi toi200 with dissolve
            "you can maneuver the tunnels by clicking the directional buttons or using your arrow keys."

            $ while_counter = 0
            while while_counter == 0:

                $ bk3_allow_earthbending = True
                $ bk3_allow_waterbending = True
                $ bk3_allow_firebending  = True





                $ while_counter = 1



    if current_room == room0:
        jump backtotherealworld





    scene black





    show expression current_room.maze_bg


    if current_room.special_touch != "sp_no_special":
        show expression current_room.special_touch
    if current_room.special_touch2 != "sp_no_special":
        show expression current_room.special_touch2










    $ bk3_special_rooms = [room1, room2, room3, room4, room5, room7, room9 ,room10 , room11 , room14 , room15 , room16, room18 , room20 , room21 , 
        room22 , room23, room24 ,room25 ,room26 , room27 , room29 , room32 , room33, room40,room49 , room52 , room53, room56, room58, room59, room60, room66,
        room61, room71, room72, room77, room82, room83]

    if current_room in bk3_special_rooms:
        $ renpy.jump ("unique_"+current_room.rname)



    if current_room.roomnr in [5,84,87,90,92,93,94,95,96,97,101,102,104,105,106,107,108,109,110]:
        $ renpy.jump ("unique_"+current_room.rname)






    $ bk3_enemyreturn_rooms = [room2, room3, room15, room20, room23, room36, room39, room48, room56, room59, room68, room74]

    if current_room in bk3_enemyreturn_rooms:
        if current_room.visit >= 6:
            if (current_room.visit%6) == 0:
                jump maze_enemies




    if current_room.maze_enemy:
        jump maze_enemies





    call screen maze_directions



screen maze_directions:




    imagemap:

        ground "maze/directions.png"
        hover "maze/directions_on.png"
        idle "maze/directions_transparent.png"














        if current_room.north >= 0:
            hotspot (465, 524, 101, 112) action [SetVariable("previous_room",current_room), SetVariable("current_room",roomlist[current_room.north]), Jump("bk3_maze_start")]
            key "focus_up" action [SetVariable("previous_room",current_room),SetVariable("current_room",roomlist[current_room.north]), Jump("bk3_maze_start")]

        if current_room.south >= 0:
            hotspot (363, 635, 300, 84) action [SetVariable("previous_room",current_room), SetVariable("current_room",roomlist[current_room.south]), Jump("bk3_maze_start")]
            key "focus_down" action [SetVariable("previous_room",current_room),SetVariable("current_room",roomlist[current_room.south]), Jump("bk3_maze_start")]

        if current_room.west >= 0:
            hotspot (363, 524, 104, 110) action [SetVariable("previous_room",current_room), SetVariable("current_room",roomlist[current_room.west]), Jump("bk3_maze_start")]
            key "focus_left" action [SetVariable("previous_room",current_room),SetVariable("current_room",roomlist[current_room.west]), Jump("bk3_maze_start")]

        if current_room.east >= 0:
            hotspot (566, 526, 98, 110) action [SetVariable("previous_room",current_room), SetVariable("current_room",roomlist[current_room.east]), Jump("bk3_maze_start")]
            key "focus_right" action [SetVariable("previous_room",current_room),SetVariable("current_room",roomlist[current_room.east]), Jump("bk3_maze_start")]

        if current_room.sp_item == True and current_room.sp_used == False:
            hotspot (sp_item_xpos, sp_item_ypos, sp_item_width, sp_item_height) action Jump("unique_"+current_room.rname+"_activate")

        if maze_fight_tutorial:
            textbutton "{color=#000000}Character stats" action Jump("maze_character_screen") xpos 0.375 ypos 10
        if maze_fight_tutorial and not jin_prison_room and not naga_eyes_begin:
            if toph_tunnel_training !=1:
                textbutton "{color=#000000}entrance" action Jump("backtotherealworld") xpos 0.62 ypos 10
        if ajala_jin_lesson and toph_tunnel_training !=1:
            textbutton "{color=#000000}visit ajala" action Jump("visit_ajala") xpos 0.2 ypos 10

label maze_character_screen:
    $ bk3_level3 = 10 - exp_total
    $ bk3_level4 = 20 - exp_total
    $ bk3_level5 = 35 - exp_total
    $ bk3_level6 = 55 - exp_total
    $ bk3_level7 = 80 - exp_total
    $ bk3_level8 = 110 - exp_total
    $ bk3_level9 = 145 - exp_total
    $ bk3_level10 = 185 - exp_total
    $ bk3_level11 = 230 - exp_total
    $ bk3_level12 = 280 - exp_total
    $ bk3_level13 = 335 - exp_total
    $ bk3_level14 = 390 - exp_total
    $ bk3_level15 = 450 - exp_total
    $ bk3_level16 = 520 - exp_total
    $ bk3_level17 = 600 - exp_total
    $ bk3_level18 = 690 - exp_total
    $ bk3_level19 = 790 - exp_total
    $ bk3_level20 = 900 - exp_total
    $ bk3_level21 = 1020 - exp_total
    $ bk3_level22 = 1150 - exp_total
    $ bk3_level23 = 1290 - exp_total
    $ bk3_level24 = 1440 - exp_total
    $ bk3_level25 = 1600 - exp_total
    $ bk3_level26 = 1790 - exp_total
    $ bk3_level27 = 1990 - exp_total
    $ bk3_level28 = 2200 - exp_total
    $ bk3_level29 = 2420 - exp_total
    $ bk3_level30 = 2700 - exp_total

    $ bk3_leveling_screen = True
    show screen bk3_level_up_stats1
    show ctc
    pause
    hide ctc
    hide screen bk3_level_up_stats1
    jump bk3_maze_start



label treasure_chest:



    play audio "audio/open_chest.mp3"
    $ renpy.pause (0.5)

    $ current_room.sp_used = True
    hide closed_treasurechest
    show open_treasurechest at Position(xpos=sp_item_xpos, ypos=sp_item_ypos, xanchor=0, yanchor=0)


    "you found [current_room.sp_content] coins!"
    if current_room.sp_content >= 1:
        play sound "audio/money.mp3"
    $ emoney += current_room.sp_content
    $ current_room.sp_content = 0

    return







label maze_enemies:
    if not first_maze_fight:
        jump bk3_start_the_fight


    if current_room.roomnr >= 38 and current_room.roomnr <= 51:
        show expression "maze/maze_enemies_badgermole.png" with hpunch
    else:
        show expression "maze/maze_enemies.png" with hpunch

    if current_room == room11:
        show ctc
        pause
        hide ctc
        hide expression "maze/maze_enemies.png"
        jump bk3_start_the_fight

    menu:
        "Run for your life!":

            $ current_room = previous_room
            scene black with Dissolve(1.0)

            "You quickly retreat. The enemy doesn't follow you."
            if maze_follower == "prisonbitch":
                jin "That was scary!"

            jump bk3_maze_start
        "Attack!":


            if current_room.roomnr >= 38 and current_room.roomnr <= 51:
                hide expression "maze/maze_enemies_badgermole.png"
            else:
                hide expression "maze/maze_enemies.png"
            jump bk3_start_the_fight










label unique_room1:
    if bk3_handjob ==3:
        y "okay, toph's tracks lead straight ahead."

    if maze_follower == "prisonbitch":

        jin "Thanks for saving me. I can find my way out from here now!"
        jin "come find me at the jasmine dragon!"

        jin "Thanks again for everything. Byebye!"


        "She waves at you and disappears."
        $ prisonbitch_freed = True
        $ maze_follower = "none"
        $ jin_prison_room = False

    if maze_follower == "prisonthighs":
        if room53.sp_content == 0 and naga_eyes != True:


            ty "i'm sticking with you until we get that treasure."


        elif naga_eyes == True:



            ty "Bye avatar!"
            ty "see you soon!"
            $ maze_follower = "none"
        else:



            ty "Thanks for everything. I can find my way out from here now!"

            menu:
                "Don't I get some kind of reward?":

                    ty "You got to cum on my ass. Isn't that reward enough?"
                    ty "But okay, here's some gold for your trouble"
                    $ emoney += 20
                    play sound "audio/money.mp3"
                    ty "Seeya"
                    "...where the hell did she keep these?!"
                "Be a bit more careful next time, okay?":





                    ty "Will do!"
                    ty "I'll repay you somehow in the future. Just you wait and see!"
                    $ prisonthighs_reward = True



            ty "Thanks again for everything. Byebye!"


            "She waves at you and disappears."
            $ maze_follower = "none"

    call screen maze_directions


label unique_room2:
    $ current_room = room2
    $ bk3enemylevel=2
    if bk3_handjob ==3:
        y "toph's tracks lead straight ahead."

    if not maze_fight_tutorial:
        $ current_room.maze_enemy = True
        play sound "audio/win2.mp3"
        "you found a life potion and a mana potion!"
        y "i did?"
        y "neat."
        y "oh."
        y "oh, no."
        y "that means..."
        y "nonononono-"
        $ bk3_fire_remaining = bk3_moves
        $ bk3_water_remaining = bk3_moves


        $ bk3_enemy_life_start = 90
        $ bk3_enemy_life = bk3_enemy_life_start
        $ bk3_enemy_attack = 10
        $ bk3_fuckable = True


        $ bk3_player_life_start = bk3_hp
        $ bk3_player_life = bk3_player_life_start
        $ bk3_player_attack= 15
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


        show expression "maze/black50.png"

        $ bk3_ypos_lifebar_player = 0
        $ bk3_ypos_lifebar_enemy  = 0

        show expression bk3_current_enemy
        show screen bk3_lifebars  
        show screen bk3_fighting_interface
        show ctc
        pause
        hide ctc
        show blackveil with dissolve

        "an enemy appeared!"
        "but the good news is that you have what it takes to kick their ass!"
        $ maze_tutorial1 = True
        "these are your life potions - using them will restore your health."
        $ maze_tutorial1 = False
        $ maze_tutorial2 = True
        "these are your mana potions - using them will restore your mana."
        "right now, you're pretty weak, and can only do so many water and fire bending attacks."
        "mana potions will restore all of your available attacks."
        "you have infinite earth bending attacks."
        $ maze_tutorial2 = False
        $ maze_tutorial3 = True
        "your opponents can be water, earth, or fire."
        "certain attacks hurt certain benders more than others."
        "a spread attack will always hit, but isn't that strong."
        "a focused attack is strong, but can miss."
        "the girls lose armor the more you damage them."
        $ maze_tutorial3 = False
        "the enemy's level is above their head, watch out for higher levels!"
        "defeat this enemy to level up and earn some coins!"
        hide blackveil
        hide expression "maze/black50.png"
        hide expression bk3_current_enemy
        hide screen bk3_lifebars  
        hide screen bk3_fighting_interface
        $ maze_fight_tutorial = True
        jump maze_enemies
    else:

        if current_room.visit ==6:
            $ current_room.visit = 1
            jump maze_enemies
        else:
            call screen maze_directions






























label unique_room3:
    $ current_room = room3
    if bk3_handjob ==3:
        y "toph's tracks lead to the right."

    call screen maze_directions





label unique_room4:


    $ sp_item_xpos = 100
    $ sp_item_ypos = 140
    $ sp_item_width = 220
    $ sp_item_height = 200

    if current_room.sp_used:
        show open_treasurechest at Position(xpos=sp_item_xpos, ypos=sp_item_ypos, xanchor=0, yanchor=0)
    else:
        show closed_treasurechest at Position(xpos=sp_item_xpos, ypos=sp_item_ypos, xanchor=0, yanchor=0)



    call screen maze_directions

label unique_room4_activate:
    call treasure_chest from _call_treasure_chest
    $ bk3_lifepotions +=1
    play sound "audio/win2.mp3"
    "you found a life potion!"
    call screen maze_directions








label unique_room5:


    $ sp_item_xpos = 335
    $ sp_item_ypos = 1
    $ sp_item_width = 330
    $ sp_item_height = 230

    if room5.sp_item == True:
        "With your earthbending at it's peak, you can sense there's a hidden corridor in this room."
        "A small push between the pillars should reveal the entry."


    call screen maze_directions

label unique_room5_activate:
    $ current_room.north = 98
    $ current_room.special_touch = "maze/sp_we_grate_1.png"
    $ current_room.special_touch2 = "maze/sp_roots_1.png"
    $ current_room.sp_item = False

    y "damn!"
    y "i've been walking past this point and never noticed anything before."
    y "do i need glasses?"
    y "....i'll worry about that later."

    jump bk3_maze_start






label unique_room7:


    $ sp_item_xpos = 500
    $ sp_item_ypos = 140
    $ sp_item_width = 220
    $ sp_item_height = 200



    if current_room.sp_used:
        show open_treasurechest at Position(xpos=sp_item_xpos, ypos=sp_item_ypos, xanchor=0, yanchor=0)
    elif current_room.sp_used == False:
        $ occupied_room =7
        show closed_treasurechest at Position(xpos=sp_item_xpos, ypos=sp_item_ypos, xanchor=0, yanchor=0)


    if current_room.visit==1:
        "Mmm a chest. maybe I can open it..."


    call screen maze_directions

label unique_room7_activate:
    play audio "audio/open_chest.mp3"
    $ renpy.pause (0.5)


    hide closed_treasurechest
    show open_treasurechest at Position(xpos=sp_item_xpos, ypos=sp_item_ypos, xanchor=0, yanchor=0)

    jump maze_enemies






label unique_room9:


    $ sp_item_xpos = 400
    $ sp_item_ypos = 10
    $ sp_item_width = 200
    $ sp_item_height = 250

    if current_room.visit==1:
        if sp_maze_key1:
            "Mmm a closed door. Maybe my key will fit"
        else:
            "a closed door but I don't have a key for it."

    if current_room.maze_enemy == True and current_room.sp_content == 1:
        "Shit! That bitch is still here!"
        jump maze_enemies

    call screen maze_directions



label unique_room9_activate:

    if maze_follower == "prisonbitch" and sp_maze_key1 == True:
        pribit1 "Maybe you shouldn't open that. If you do, don't count on me sticking around."
    if maze_follower == "prisonthighs" and sp_maze_key1 == True:
        ty "That door is looking ominous. Open it and I'm outta here."



    if sp_maze_key1 == True and current_room.sp_content == 0:

        menu:
            "Open door":
                play sound "audio/door.mp3"
                $ maze_follower = "none"


                $ current_room.north = 16
                $ room16.south = 9
                $ current_room.special_touch2 = "sp_n_opendoors_1"
                $ current_room.sp_content = 1


                show expression current_room.special_touch2 with Dissolve(2.0)
                "When you turn the key the door swings open and someone jumps through it!"
                jump maze_enemies
            "leave the door locked":

                "You leave it alone."

    if sp_maze_key1 == False:
        "I have no key which will unlock this door...yet."

    if sp_maze_key1 == True and current_room.maze_enemy == False and current_room.sp_content == 1:

        if current_room.special_touch2 == "sp_n_opendoors_1":
            $ current_room.special_touch2 = "sp_n_closeddoors_1"
            show expression current_room.special_touch2
            play sound "audio/thud.mp3"
            $ room16.south = -1
            $ current_room.north = -1
        else:
            $ current_room.special_touch2 = "sp_n_opendoors_1"
            show expression current_room.special_touch2
            play sound "audio/door.mp3"
            $ room16.south = 9
            $ current_room.north = 16




    call screen maze_directions







label unique_room10:


    $ sp_item_xpos = 400
    $ sp_item_ypos = 10
    $ sp_item_width = 200
    $ sp_item_height = 250

    if current_room.north == -1 and current_room.visit == 1:
        if maze_sections == 0:
            "You knock on the wall to the north, it seems there's a room behind it."
            "Too bad your earthbending is still too weak to break through it"
        else:
            "You knock on the north wall, it seems there's a room behind it."
            "You might be able to earthbend your way through it."

    call screen maze_directions

label unique_room10_activate:
    if current_room.north == -1  and maze_sections >= 1:

        menu:
            "break through":
                play audio "audio/rock_crumble.mp3"

                $ current_room.special_touch = "maze/maze_unblockedn.png"
                show expression current_room.special_touch with Dissolve(2.0)
                $ current_room.sp_used = True
                $ current_room.north = 17
                y "nice!"
            "let's not mess with this right now":

                "You leave it alone."
    else:
        "My earthbending is still too weak."

    call screen maze_directions






label unique_room11:


    $ sp_item_xpos = 200
    $ sp_item_ypos = 0
    $ sp_item_width = 170
    $ sp_item_height = 300

    if current_room.sp_used == False:

        show npc_prisoner1 at Position(xpos=sp_item_xpos, ypos=sp_item_ypos, xanchor=0, yanchor=0)

        if current_room.visit == 1:
            "*Sob...* Mister can you free me from this place?"
        elif current_room.visit == 2:
            "It's cold, I'm hungry. I miss my family."
        elif current_room.visit == 3:
            "dude, are you even human?"
        elif current_room.visit == 4:
            "Fuck this shit. You're going down!"
            play sound "audio/shackles_gone.mp3"

            hide npc_prisoner1
            show npc_emptyshackles at Position(xpos=sp_item_xpos, ypos=sp_item_ypos, xanchor=0, yanchor=0)

            $ current_room.sp_used = True

            "The girl easily frees herself and comes at you!"

            jump maze_enemies
    else:

        show npc_emptyshackles at Position(xpos=sp_item_xpos, ypos=sp_item_ypos, xanchor=0, yanchor=0)




    if maze_follower == "prisonbitch" and current_room.sp_content < 10:


        if current_room.sp_used and current_room.sp_content < 10:
            show expression "prisonbitch_sbox"

            if current_room.sp_content == 1:
                "There used to be a girl here chained to the wall."
                $ current_room.content == 2

            elif current_room.sp_content == 2:
                "Being chained up is kind of kinky. I like that. In theory."
                $ current_room.sp_content = 3

            elif current_room.sp_content == 3:
                "It'd be nice if you could take me to the exit."
                $ current_room.sp_content = 10
            hide expression "prisonbitch_sbox"
        else:

            show expression "prisonbitch_sbox"
            "Poor girl.. can you try and free her?"
            $ current_room.sp_content = 2
            hide expression "prisonbitch_sbox"

    call screen maze_directions

label unique_room11_activate:


    menu:
        "nah, I'm busy. Maybe later.":
            call screen maze_directions
        "Let's see if I can free her.":

            play sound "audio/shackles_gone.mp3"
            hide npc_prisoner1
            show npc_emptyshackles at Position(xpos=sp_item_xpos, ypos=sp_item_ypos, xanchor=0, yanchor=0)

            $ current_room.sp_used = True

            show thankful_girl with Dissolve(1.5)
            "girl" "Thank you!"
            "girl" "here, take this. I found it behind a loose stone in the wall."
            $ emoney += 20
            play sound "audio/money.mp3"
            "She hands you 20 coins."
            play sound "audio/kiss.mp3"
            with pflash
            "she gives you a sloppy wet kiss with lots of tongue."
            y "um... that was nice, but what the-"
            "girl" "where... where am i...?"
            hide thankful_girl with vshake
            "the girl falls to the floor suddenly."
            y "...i guess i'm just that good."
            show toi toi210
            show toi_swim_surprise
            with dissolve
            t "we need to get her out of here."
            t "we'll take her back to my house."
            t "let's get out of here."
            y "Hmmm.. she looks familiar."
            t "come on!"
            $ first_maze_girl = True
            hide toi toi210
            hide toi_swim_surprise
            with dissolve
            call screen maze_directions









label unique_room14:


    $ sp_item_xpos = 1
    $ sp_item_ypos = 1
    $ sp_item_width = 140
    $ sp_item_height = 430


    if current_room.west == -1 and current_room.visit == 1:
        if maze_sections == 0:
            "You knock on the westwall, it seems there's a room behind it."
            "Too bad your earthbending is still too weak to break through it"
        else:
            "You knock on the wall to the west, it seems there's a room behind it."
            "You might be able to earthbend your way throught it."

    call screen maze_directions

label unique_room14_activate:
    if current_room.west == -1  and maze_sections >= 2:

        menu:
            "break through":
                play audio "audio/rock_crumble.mp3"



                $ current_room.sp_used = True
                $ current_room.west = 19
                $ current_room.special_touch = "maze/sp_westwall_breakthrough.png"
                show expression current_room.special_touch with Dissolve(2.0)
            "let's not mess with this right now":

                "You leave it alone."
    else:
        "I'm still too weak to break through this wall."

    call screen maze_directions   





label unique_room15:


    $ sp_item_xpos = 10
    $ sp_item_ypos = 20
    $ sp_item_width = 200
    $ sp_item_height = 600



    if current_room.west == -1:
        if maze_sections >=3 and current_room.visit == 1:
            "Hot steam escaping from a crack in the ground."
            "I think I can close it without opening up a new crack under my feet."

        elif current_room.visit == 1:
            "Hot steam escaping from a crack in the ground."
            "There's a chance a new crack will open up right under me if I try and close it with earthbending."
            "Let's not mess with this until I'm a more experienced earthbender."
    if maze_sections >= 3 and current_room.sp_used == False:
        "I think I can close this."


    call screen maze_directions

label unique_room15_activate:

    if current_room.west == -1  and maze_sections >= 3:

        menu:
            "Close the crack":
                play audio "audio/rock_crumble.mp3"
                show expression current_room.maze_bg with hpunch


                $ current_room.sp_used = True
                $ current_room.west = 18
                $ current_room.special_touch2 = "sp_no_special"
                $ current_room.special_touch = "sp_no_special"
                hide expression current_room.special_touch with Dissolve(2.0)
                hide expression current_room.special_touch2 with Dissolve(2.0)
            "let's not mess with this right now":


                "You leave it alone."
    else:
        "There's nothing I can do about this right now. I'll need to be a stronger earthbender."

    call screen maze_directions   






label unique_room16:



    if maze_follower == "prisonthighs":
        ty "I really don't feel like hanging around here any longer so if you want to go on it'll be without me."


    call screen maze_directions   

label unique_room16_activate:



    call screen maze_directions





label unique_room17:
    call screen maze_directions   

label unique_room17_activate:



    call screen maze_directions






label unique_room18:

    if current_room.visit == 1:
        "This... looks like trouble."
    call screen maze_directions   

label unique_room18_activate:



    call screen maze_directions





label unique_room20:


    $ sp_item_xpos = 167
    $ sp_item_ypos = 98
    $ sp_item_width = 104
    $ sp_item_height = 27

    call screen maze_directions

label unique_room20_activate:

    "You see a loose stone."
    "You carefully take it out, turn it around and put it back in."
    "You gained......nothing."

    call screen maze_directions






label unique_room21:

    $ sp_item_xpos = 400
    $ sp_item_ypos = 20
    $ sp_item_width = 240
    $ sp_item_height = 500
    show mushroom_3:
        xpos 200 ypos 550
    show mushroom_2:
        xpos 600 ypos 250
    show mushroom_1:
        xpos 250 ypos 200

    if not current_room.sp_used:









        if not suki_loose:
            show suki_prisoner at Position(xpos=sp_item_xpos, ypos=sp_item_ypos, xanchor=0, yanchor=0)

            if current_room.visit == 1:
                "???" "Are... are you going to hurt me?"
            elif current_room.visit == 8:
                suki "You aren't really a people person are you?"
        else:
            show expression "maze/sp_emptyshackles1.png" at Position(xpos=sp_item_xpos, ypos=sp_item_ypos, xanchor=0, yanchor=0)
    else:


        show expression "maze/sp_emptyshackles1.png" at Position(xpos=sp_item_xpos, ypos=sp_item_ypos, xanchor=0, yanchor=0)

    call screen maze_directions

label unique_room21_activate:
    if current_room.sp_content ==2 and not suki_free:
        y "i need to chase suki down."
        show expression "maze/sp_emptyshackles1.png" at Position(xpos=sp_item_xpos, ypos=sp_item_ypos, xanchor=0, yanchor=0)
        call screen maze_directions




























    if current_room.sp_content == 0:
        show expression "maze/suki_body.png"
        show expression "maze/suki_headdown.png"
        with Dissolve(1.5)

        y "Ahem."

        suki "....Aang, is that you? It's you!!!"
        y "It is!"
        y "....."
        y "and you are...?"
        suki "It's me! Suki!"
        suki "Oh, wait, you don't recognize me because of the hair...."

        hide expression "maze/suki_headdown.png"
        show expression "maze/suki_headup.png"
        with vshake

        "The girl whips her head up, flinging away the hair in front of her face."
        y "Hi... Sucki?"
        suki "Suki!"
        y "Yeah, that {i}is{/i} what I want."
        suki "......."
        suki "Can you free me?"
        suki "i'm so hungry....."
        $ current_room.sp_content = 1

    if current_room.sp_content ==1:

        show expression "maze/suki_body.png"
        show expression "maze/suki_headup.png"
        with dissolve

    menu:
        "leave her chained to the wall":
            y "Sorry, I'll come back for you but I need to do something else first."
            suki "Don't leave me here!"

            hide expression "maze/suki_headup.png"
            hide expression "maze/suki_body.png"

            call screen maze_directions
        "Strike up a conversation":

            y "So what happened?"
            suki "I got ambushed and woke up here."
            y "Man that sucks, sushi."
            suki "it's suki!"
            y "that is sucky."
            suki "suki!"
            y "i feel like we're saying the same thing."
            suki "....."

            hide expression "maze/suki_headup.png"
            hide expression "maze/suki_body.png"
            jump unique_room21_activate
        "Free her":


            y "hmm.... looks like i can open these...."
            suki "really!?"

            menu:
                "sexual favor":
                    $ suki_sexual_favor = True
                    y "yeah, but... i need a favor first."
                    suki "well... what is it? there's not much i can do here."
                    y "no big. i just need to get my rocks off."
                    suki "what?"
                    suki "wait, you don't mean your-"
                    y "oh, but i do."
                    y "i need to cum and you have a pretty face."
                    suki "i'm not going to help you with that!"
                    y "okay, bye!"
                    suki "wait! wait!"
                    suki "um..."
                    scene black with dissolve
                    $ renpy.pause(0.05, hard=True)
                    scene dickrub_maze
                    show tosd_piss:
                        xpos 460 ypos 350
                    show tosd tosd01
                    with Dissolve(1.0)
                    $ renpy.pause(0.5, hard=True)
                    suki "what do you... need me to do?"
                    menu:
                        "\"piss yourself\"":
                            y "I want you to piss yourself."
                            suki "I.... what? why?"
                            y "because i said so."
                            suki "how does that help you-"
                            y "either you want my help or you don't."
                            suki "........"
                            show tosd tosd02 with dissolve
                            suki "*ungh...*"
                            suki "this is so embarrassing...."
                            suki "............."
                            show tosd_piss:
                                alpha 1.0
                                xpos 460 ypos 380
                                linear 2.0 ypos 450

                            $ renpy.pause(1, hard=True)
                            suki "mmn..."
                            show ctc
                            pause
                            hide ctc
                            show tosd tosd01 with dissolve
                            suki "this is disgusting..."
                            suki "it's all hot and wet..."
                            suki "is... is that enough?"
                            suki "please let me out... i'm sitting right in it..."
                            jump suki_prison_tongue
                        "\"stick out tongue\"":

                            jump suki_prison_tongue
                "just let her go":

                    jump suki_gets_freed

            label suki_prison_tongue:
                y "stick out your tongue."
                suki "but-"
                y "do it or i walk away."
                suki "....."
                show tosd tosd02 with dissolve
                suki "....."
                show tosd tosd06 with dissolve
                show ctc
                pause
                hide ctc
                show tosd tosd05 with dissolve
                suki "anhhh...."
                show ctc
                pause
                hide ctc
                y "nice... very nice."
                y "now close your legs."
                y "what are you, a whore?"
                suki "....."
                show tosd tosd03 with dissolve
                suki "....why are you doing this?"
                y "because we can help each other."
                y "this is just a business transaction."
                y "your freedom for my cum."
                suki "that's not fair..."
                y "close your eyes."
                suki "...why?"
                y "i'm going to rub my cock on your face."
                suki "please don't..."
                y "{i}*zziiiiip*"
                show tosd tosd04 with dissolve
                suki "no, i.... i don't want that..."
                show tosd_hands with dissolve
                y "that's okay."
                y "I really don't mind."
                show ctc
                pause
                hide ctc
                show tosd tosd03 with dissolve
                suki "wait..."
                suki "please..."
                y "yes?"
                suki "i'll... i'll let you do it-"
                y "do what?"
                suki "rub... rub your..."
                y "say it."
                suki "...your..."
                suki "your... cock..."
                suki "...on my..."
                suki "......"
                suki "...face."
                suki "but you have to promise not to tell anyone."
                y "oh, of course, honey."
                y "It stays between us."
                suki "...."
                show tosd tosd04 with dissolve
                suki "go... go ahead..."
                y "say please."
                suki "plea-"

                show tosd_dickslap_begin:
                    xpos 490 ypos 230

                with Pause(0.5)
                play sound "audio/slap.mp3"
                suki "ungh!"
                "with an audible *smack*, you drop your cock onto suki's face."
                y "oh, fuck yeah."
                suki "uuughh! gross!"
                y "go ahead and take a big whiff, suki."
                suki "uughh... stop..."
                y "smell my fucking cock."
                suki "i am a warrior... i am a kyoshi warrior!"
                hide tosd_dickslap_begin
                show tosd_dickslap_repeated:
                    xpos 490 ypos 230
                show ctc
                pause
                hide ctc
                y "you're a what?"
                suki "i'm-"
                suki "uhghh!"
                y "say it again."
                suki "I'm a kyoshi-"
                suki "unghh... hngh..."
                suki "i'm a kysohi warrior!"
                y "so what are you doing here?"
                suki "i was-"
                suki "stop slapping my face! it hurts!"
                show tosd_solodick:
                    xpos 490 ypos 230
                hide tosd_dickslap_repeated
                y "oh, fine."
                hide tosd_solodick
                show tosd_dickrub:
                    xpos 490 ypos 230
                suki "ungh!"
                show ctc
                pause
                hide ctc
                y "Is that better?"
                y "your face is really going to smell like cock."
                y "I don't think i bathed today."
                y "or this whole week, really."
                y "damn... when was the last time i bathed?"
                suki "*whimper*"
                suki "{size=-4}ew...ew...ew..."
                "gripping her head steady against your cock, you sway your hips back and forth, making sure to press into suki's cheeks and nose..."
                "you even manage to wipe precum on her eyelids, as her face begins to glisten with the smeared liquid."
                y "open your eyes."
                suki "i don't... i don't want to..."
                show tosd_dickslap_once:
                    xpos 490 ypos 230
                hide tosd_dickrub
                ya "open them!"
                show tosd tosd03 with dissolve
                show ctc
                pause
                hide ctc
                y "that's it... just like that..."
                hide tosd_dickslap_once
                show tosd_dickslap_repeated:
                    xpos 490 ypos 230
                y "keep your head right there..."
                y "slapping my cock on your pretty fucking face..."
                suki "aang... ungh... please... just let me go..."
                y "not until i nut, bitch!"
                show tosd tosd04
                hide tosd_dickslap_repeated

                show tosd_dickrub:
                    xpos 490 ypos 230
                with dissolve
                suki "i'm... i'm a proud..."
                suki "...a proud kyoshi warrior..."
                y "I'm gonna cum!"
                suki "my face belongs to ky-"
                y "your face belongs to kyoshi, the avatar, which is now me!"
                y "kyoshi is rubbing her cock on your face, bitch!"
                y "you're welcome!"
                suki "w-what...?"
                y "thank me!"
                suki "tha... thank you... kyoshi..."
                ya "open your eyes!"
                hide tosd_dickrub
                show tosd tosd03
                with dissolve
                ya "yes!"
                suki "please! don't!"
                ya "that's perfect! fuck!"
                play sound "audio/splurt2.ogg"
                show tosd tosd04
                show expression "bk3/katara/blowjob/sperm1.png":
                    xpos -270 ypos -250
                with flash
                suki "ungh! no!"
                play sound "audio/splurt3.ogg"
                hide expression "bk3/katara/blowjob/sperm1.png"
                show expression "bk3/katara/blowjob/sperm2.png":
                    xpos -270 ypos -250
                with flash
                ya "ngh!"
                suki "aang! why!?"
                ya "eyes open! tongue out! bitch!"
                show tosd tosd07 with dissolve
                ya "yes!"
                play sound "audio/splurt1.ogg"
                show tosd tosd06
                hide expression "bk3/katara/blowjob/sperm2.png"
                show expression "bk3/katara/blowjob/sperm3.png":
                    xpos -270 ypos -250
                with flash
                suki "eww..."
                y "ahhhh...."
                show ctc
                pause
                hide ctc

                y "well, i feel better."
                show tosd tosd08 with dissolve
                suki "please let me go now.... these chains hurt..."
                y "sure."
                suki "i don't... understand, aang."
                suki "you're the avatar... why-"
                hide tosd_hands with dissolve
                y "sshhh..."
                show ctc
                pause
                hide ctc
                y "relax, you did great."
                y "now let's get you out of here."
                scene black with dissolve
                scene maze_ws_1
                show sp_e_door_2
                show sp_roots_2
                show suki_prisoner:
                    xpos 400 ypos 20
                show mushroom_3:
                    xpos 200 ypos 550
                show mushroom_2:
                    xpos 600 ypos 250
                show mushroom_1:
                    xpos 250 ypos 200
                with Dissolve(1.5)

            label suki_gets_freed:
                hide expression "maze/suki_headup.png"
                hide expression "maze/suki_body.png"
                play sound "audio/shackles_gone.mp3"
                hide suki_prisoner
                show suki_prisoner2:
                    xpos 400 ypos 20
                show expression "maze/sp_emptyshackles1.png" at Position(xpos=sp_item_xpos, ypos=sp_item_ypos, xanchor=0, yanchor=0)

                $ current_room.sp_content = 2


                suki "finally!"
                suki "ungh... i'm so hungry!"
                y "well, there's a tavern back in the vil-"
                hide mushroom_2 with vshake
                "suki quickly scarfs down the mushrooms closest to her."
                y "oh. uh... i mean, the village has a tavern."
                y "but, you know, do you."
                suki "........"
                suki "..........................."
                y "are you okay?"
                suki "{size=+10}demon!!"
                suki "{size=+10}aaahhh!!!!!!!"
                hide suki_prisoner2 with moveoutleft
                y "....."
                y "that's not good."
                y "sounds like a pretty bad trip."
                y "*sigh* i'll go get her."
                $ suki_free = False
                $ suki_loose = True
                call screen maze_directions






label unique_room22:


    $ sp_item_xpos = 400
    $ sp_item_ypos = 100
    $ sp_item_width = 220
    $ sp_item_height = 200

    if current_room.sp_used:
        show open_treasurechest at Position(xpos=sp_item_xpos, ypos=sp_item_ypos, xanchor=0, yanchor=0)
    else:
        show closed_treasurechest at Position(xpos=sp_item_xpos, ypos=sp_item_ypos, xanchor=0, yanchor=0)


    call screen maze_directions

label unique_room22_activate:

    call treasure_chest from _call_treasure_chest_1

    "There's also a health potion!"
    y "Shit, the potion's empty. Hmmm there's a note."
    "\"To whomever is the owner of this health potion....\""
    "\"Sorry I was thirsty, but I left two coins, so we're cool right? Signed, Sokka.\""
    y "...How the hell did he even get here?!! I had to earthbend my way in!!"
    call screen maze_directions





label unique_room23:
    if not room23_fight:
        $ current_room.maze_enemy = True
    if current_room.maze_enemy == True:
        jump maze_enemies

    if current_room.visit ==6:
        $ current_room.visit = 0
        jump maze_enemies
    else:
        call screen maze_directions





label unique_room24:


    $ sp_item_xpos = 400
    $ sp_item_ypos = 10
    $ sp_item_width = 200
    $ sp_item_height = 250

    if not mushroom_cloud:
        show mushroom_1:
            xpos 400 ypos 150
        show mushroom_2:
            xpos 600 ypos 250
        show mushroom_3:
            xpos 250 ypos 200

    if current_room.visit == 1:
        y "A closed door. But is it locked?"

    if suki_loose and not cartoon_adventure:
        y "suki went this way, she must have gone through here."
    call screen maze_directions



label unique_room24_activate:

    if not suki_loose:
        y "yup. locked."
        call screen maze_directions

    if current_room.special_touch == "sp_n_closeddoors_1":
        play sound "audio/door.mp3"



        $ current_room.north = 25
        $ current_room.special_touch = "sp_n_opendoors_1"
        hide mushroom_1
        hide mushroom_2
        hide mushroom_3
        $ renpy.pause(0.05)
        show purple_layer
        show expression current_room.special_touch
        with Dissolve(1.0)
        if current_room.sp_content == 0:
            $ mushroom_cloud = True
            $ renpy.pause(1.0)
            "as you open the door, the mushrooms explode, unleashing a purple cloud."
            ya "*cough* *cough*"
            ya "fuck."
            ya "*cough*"
            ya "when if find you, i'm kicking your ass, sushi!"
            $ current_room.sp_content = 1
            jump unique_room25


    elif current_room.special_touch == "sp_n_opendoors_1":
        $ current_room.north = -1
        $ current_room.special_touch = "sp_n_closeddoors_1"
        show expression current_room.special_touch with Dissolve(1.0)
        play sound "audio/thud.mp3"
        $ current_room.sp_content += 1
        if current_room.sp_content == 2:
            "I can close it again?! I wonder if this has absolutely no useful function."
            $ current_room.sp_content += 1

    if current_room.sp_content == 6:
        "open close open close open close."



    call screen maze_directions





label unique_room25:

    if suki_loose and not cartoon_adventure:
        scene black with dissolve
        scene maze_ns_3:
            yzoom -1.0

        with dissolve
        y "what...."
        y "what the fuck?"
        show ctc
        pause
        hide ctc
        y "and behind me is..."
        scene maze_s_1


        with pushright
        y "....a wall."
        y "okay."
        scene maze_ns_3:
            yzoom -1.0


        with dissolve
        y "only way out is forward."
        menu:
            "forward":
                scene black
                scene maze_nwe_1:
                    yzoom -1.0
                show sp_roots_1
                with dissolve
                y "this is super disconcerting."

        menu:
            "left":
                scene black
                scene maze_se_1:
                    yzoom -1.0
                with dissolve
            "right":

                scene black
                scene maze_ws_1:
                    yzoom -1.0
                with dissolve

        show pgfull:
            ypos -200 xpos 100
            yzoom -1.0
        with dissolve
        s "{i}you... ssss...."
        y "ah fuck, you're making me nauseous."
        s "{i}i will fuck the skin from your bones...."
        y "I... what?"
        y "look can you at least stand on the groun- ceiling? with me?"
        hide pgfull with dissolve
        show pgfull with dissolve
        y "nope, didn't help. made things worse."
        s "{i}i will rape your chi...."
        y "that seems more complicated than anything."
        s "{i}ssssssssssss..........."
        hide pgfull with dissolve
        y "......."
        y "that probably didn't mean anything."

        menu:
            "forward":
                scene black
                scene maze_s_2:
                    yzoom -1.0
                show mushroom_2:
                    ypos 50 xpos 50
                    yzoom -1.0
                show purple_layer
                with dissolve
                y "*cough*"
                y "what is this purple-"
                y "oh."
                y "i'm high."
                y "that makes sense."
                y "....."
                y "fuck."

        menu:
            "right":
                scene black
                scene maze_w_1:
                    yzoom -1.0
                with dissolve
                show as_sidebox_hiss
                "{i}avatar...."
                y "what now?"
                "{i}i will protect you from evil, avatar....."
                "{i}trust...."
                hide as_sidebox_hiss with dissolve
                y "uh...."
        menu:
            "right":
                scene black with dissolve
                scene maze2_ns_0:
                    yzoom -1.0
                show purple_layer
                with dissolve
                y "oh, what the damn hell."
                show tf:
                    ypos -150 xpos -300
                    yzoom -1.0
                hide purple_layer
                show purple_layer
                with dissolve
                if thief >= zuko:
                    t "you're slipping, thief."
                    y "I'm not a thief! not any more!"
                if zuko > thief:
                    t "you're slipping, zuko."
                    y "i'm not zuko! not any more!"
                y "and it's this damn shroom cloud."
                ty "what shroom cloud?"
                hide tf with dissolve
                y "...that was ominous."
                y "okay, i must just be high, it's not a big deal-"
                hide maze2_ns_0
                scene maze2_ns_0
                hide purple_layer
                show purple_layer
                with sshake
                y "ah! fuck!"
                y "why?"
                y "my head.... my head is..."
                show nbody
                show expression "bk3/suki/idles/underwear.png"
                show tosi_angry
                hide purple_layer
                show purple_layer
                with dissolve
                suki "no! you won't lock me up again!"
                suki "i am a kyoshi warrior! i will {i}not{/i} be taken again!"
                y "wait! suki! i'm not-"
                hide nbody
                hide expression "bk3/suki/idles/underwear.png"
                hide tosi_angry
                with dissolve
                ya "damn it!"
                show closed_treasurechest at truecenter
                with dissolve
                y "....."
                y "how...."
                y "....."
                menu:
                    "open chest":
                        hide closed_treasurechest
                        show open_treasurechest at truecenter
                        with dissolve
                        y "oh, neat."
                        y "i wonder what's-"
                        scene black
                        scene maze_door_n
                        with irisout
                    "move forward":
                        hide closed_treasurechest
                        show open_treasurechest at truecenter
                        with dissolve
                        y "but i didn't-"
                        scene black
                        scene maze_door_n
                        with irisout


        y "....what...."
        y "where... am i?"
        y "it's like the tunnels, but..."
        y "...more cartoony..."
        menu:
            "open door":
                scene black with dissolve
                show sp_n_opendoors_1
                show purple_layer
                with dissolve
                show ctc
                pause
                hide ctc
                y "whoa...."
                $ cartoon_adventure = True
                y "i hope this is the last of it."
                menu:
                    "forward":
                        "a voice comes to you as you walk through the doors..."
                        scene black with dissolve
                        "wealth.... or power?"
                        menu:
                            "power":
                                $ exp_total +=40
                                "you gained a bunch of experience!"
                            "wealth":

                                $ emoney +=100
                                "you gained 100 coins!"
                        call screen maze_directions



    $ sp_item_xpos = 400
    $ sp_item_ypos = 10
    $ sp_item_width = 200
    $ sp_item_height = 250

    if suki_loose and not suki_free:
        jump maze_enemies
    if current_room.visit == 2:
        "You see what looks like a life sized statue of a naked woman."
    if current_room.maze_enemy == True:
        jump maze_enemies
    if current_room.sp_item == True and current_room.maze_enemy == False and current_room.special_touch == "sp_covegirl_0":
        "You search the room and find a small statue of avatar Kyoshi in the alcove."
        play sound "audio/money.mp3"
        show expression "maze/kyoshi_dildo.png" with Dissolve(1.0)
        y "...this is a very poorly disguised dildo."
        y "maybe it's suki's?"
        hide expression "maze/kyoshi_dildo.png" with Dissolve(1.0)
        show expression "maze/kyoshi_dildo_bottom.png" with Dissolve(1.0)
        "The bottom has a strange triangle shaped opening."
        hide expression "maze/kyoshi_dildo_bottom.png"
        $ current_room.sp_item = False
        $ sp_kyoshi_dildo = True

    call screen maze_directions




label unique_room25_activate:


    "You step closer to take a better look.... did it just blink its eyes?"


    menu:
        "Leave it be":
            call screen maze_directions
        "pinch it's nipple":
            $ current_room.sp_used = True
            $ current_room.special_touch = "sp_covegirl_0"
            show expression current_room.special_touch with Dissolve(2.0)
            play sound "audio/slap.mp3"

            "the statue shrieks and slaps you hard in the face."
            "???" "Asshole! You're gonna pay for that!"
            "She wipes off the rockdust on her and steps out of the alcove."
            $ current_room.maze_enemy = True
        "Tickle it":

            $ current_room.sp_used = True

            play sound "audio/giggling.mp3"
            "???" "Ahahahaa!! Stop that!"
            "She wipes off the rockdust on her and steps out of the alcove."

            $ current_room.special_touch = "sp_covegirl_0"
            show expression current_room.special_touch with Dissolve(2.0)
            $ current_room.maze_enemy = True

    jump maze_enemies

    call screen maze_directions





label unique_room26:


    $ sp_item_xpos = 290
    $ sp_item_ypos = 60
    $ sp_item_width = 170
    $ sp_item_height = 460

    if current_room.maze_enemy == True:
        jump maze_enemies
    if current_room.maze_enemy == False and room29.visit >= 1 and current_room.sp_content == 0:
        play sound "audio/money.mp3"
        "You found 50 gold!"
        $ emoney += 50

        $ current_room.sp_content = 1

    if current_room.visit==1:
        "a timid voice calls out to you."
        pribit0 "H...hello? Is there anyone there?"
        pribit0 "I'm a really cute girl and if you can get me out of here, I'll suck your cock! or eat you out or whatever..."
        y "Hey so, I wouldn't mind taking you up on that offer, but the walls are pretty thick and that door is solid iron."

        y "Do you know where the key to this door is?"
        pribit0 "Some bitch patrolling this place has it. She should be close by."

        if prisonbitch_key == True:
            y "Ah, I think I already met her I've got a key right here."
        if prisonbitch_key == True and maze_follower != "none":
            pribit0 "That's great, but please get rid of that other person with you first."
            y ".....why?"
            pribit0 "Three is my unlucky number."
            y "Are you certain you want to get out of there?"
            pribit0 "Absolutely! I'm just very superstitious."
            call screen maze_directions

            menu:
                "Open door":
                    $ current_room.sp_used = True
                    $ current_room.special_touch = "sp_ns_md_open"
                    $ current_room.west = 29
                    $ room29.special_touch = "sp_e_mdoor_1"
                    $ room29.east = 26
                    show expression "sp_ns_md_open" with Dissolve(1.2)
                "leave it closed":

                    "I just remembered something. I'll be right back."



    call screen maze_directions


label unique_room26_activate:


    if maze_follower != "none" and room29.visit == 0:
        pribit0 "You have the key?! That's great, but please get rid of that other person with you first."
        y ".....why?"
        pribit0 "Three is my unlucky number."
        y "Are you certain you want to get out of there?"
        pribit0 "Absolutely! I'm just very superstitious."
        call screen maze_directions

    if prisonbitch_key == True:
        menu:
            "open door":
                play sound "audio/door.mp3"
                $ current_room.sp_used = True
                $ current_room.special_touch = "sp_ns_md_open"
                $ current_room.west = 29
                $ room29.special_touch = "sp_e_mdoor_1"
                $ room29.east = 26
                show expression "sp_ns_md_open" with Dissolve(1.2)
            "leave door closed":

                pass
    if prisonbitch_key == False:
        "It's a sturdy metal door with thick walls surrounding it."









label unique_room27:

    if maze_follower == "prisonbitch" and room26.maze_enemy == True and current_room.sp_content <=0:

        jin "Hey, I can see that woman who was taunting us in the cell!"
        jin "She's ridiculously strong. Maybe we should escape the other way?"

        hide prisonbitch_sbox with Dissolve(1.0)
        $ current_room.sp_content = 1
    call screen maze_directions






label unique_room29:


    $ sp_item_xpos = 200
    $ sp_item_ypos = 120
    $ sp_item_width = 220
    $ sp_item_height = 200




    if current_room.sp_used == False:
        show open_treasurechest at Position(xpos=sp_item_xpos, ypos=sp_item_ypos, xanchor=0, yanchor=0)
    if current_room.sp_used == True:
        show open_treasurechest at Position(xpos=(sp_item_xpos+200), ypos=sp_item_ypos, xanchor=0, yanchor=0)

    if current_room.visit==1:
        $ jin_prison_room = True
        show tojn tojn01:
            xpos -150
        with dissolve
        jin "Thanks! I have no idea what these crazy people would've done to me If you hadn't come along!"
        y "No problem."
        show tojn tojn02 with dissolve
        jin "And to top it off, I only have this tiny piece of cloth to cover myself with!"
        y "I noticed."
        show tojn tojn03 with dissolve
        jin "Please... notice a little less."
        y "Ah, uh, sorry."
        show tojn tojn01 with dissolve
        jin "nah, it's cool."
        jin "Let's get out of here while we can."
        y "aren't you forgetting something?"
        jin "what do you-"
        jin "oh. um."
        y "yeah. the price of freedom."
        jin "i was just... saying anything..."
        jin "i'm... not going to actually blow you."
        y "i guess i can just leave you...."
        show tojn tojn02 with dissolve
        jin "wait!"
        jin "umm..."
        show tojn tojn01 with dissolve
        jin "how about this...."
        show dickrub_maze_jin
        show tojb tojb01
        with Dissolve(1.0)
        show ctc
        pause
        hide ctc
        jin "can you... rub on my buttcheeks?"
        jin "maybe use my cheeks to get off?"
        jin "would that work?"
        menu:
            "\"i will happily fuck those ass cheeks\"":
                y "your cheeks do look... plush."
                jin "then get to it!"
                jin "come on, i want to get out of here."
                show tojb_solodick with dissolve
                y "i'm happy to oblige."
                y "say please."
                jin "....please."
                y "flatter me."
                jin "please... savior."
                jin "my hero. rescuer."
                jin "please hump my plump, firm bottom..."
                jin "and set me free."
                y "that... wasn't bad."
                hide tojb_solodick
                show tojb tojb11
                with dissolve
                jin "ohh..."
                jin "um..."
                jin "i just realized... that this is really happening."
                y "yes... now squeeze."
                show tojb tojb12 with dissolve
                y "nghh... damn..."
                jin "I can go tighter."
                y "well do it!"
                show tojb tojb13 with dissolve
                jin "how's that?"
                y "fuck..."
                jin "i'm gonna squeeze really hard, okay?"
                y "go for it."
                show tojb tojb14 with dissolve
                y "fucking. damn. it. that's comfy."
                jin "oh? okay."
                show tojb tojb11 with dissolve
                jin "here goes nothing..."
                show tojb tojb100
                y "unghh..."
                show ctc
                pause
                hide ctc
                jin "is... is this working?"
                y "hunhh...."
                jin "it's really... warm..."
                $ jin_buttrub_face = 'blink'
                jin "just... enjoy."
                jin "thank you for saving me..."
                jin "i'm genuinely grateful."
                show ctc
                pause
                hide ctc

                jin "I'm sorry it's not... my mouth, but..."
                $ jin_buttrub_face = 'back'
                jin "I hope my ass makes you shoot big, heavy loads...."
                jin "right... right on my back if you want..."
                y "oh, fuck! where did you learn to talk like that?"
                $ jin_buttrub_face = 'side'
                jin "don't stop..."
                jin "come on... come on..."
                jin "get it out..."
                $ jin_buttrub_face = 'blink'
                jin "i feel you caught in there... rubbing my asshole, trapped between my cheeks..."
                "jin's warm, supple bottom keeps you perfectly engulfed as she squeezes and gyrates..."
                $ jin_buttrub_face = 'back'
                "eagerly milking you using only her juicy, giving mounds, friction, and pressure."
                "you feel your balls begin to churn as the load rises up."
                "you don't even warn her as you begin firing onto her warm, tan back."
                show tojb tojb01
                show tojb_solodick
                with dissolve
                y "ahh..."
                play sound "audio/splurt1.ogg"
                show tojb_spermshot
                $ renpy.pause(0.3, hard=True)
                hide tojb_spermshot

                show tojb_sperm1
                jin "ohh..."
                play sound "audio/splurt2.ogg"
                show tojb_spermshot
                $ renpy.pause(0.3, hard=True)
                hide tojb_spermshot

                hide tojb_sperm1
                show tojb_sperm2
                y "fuck i needed this..."
                jin "yes... ahh..."
                jin "empty... all of it... on my back..."

                play sound "audio/splurt3.ogg"
                show tojb_spermshot
                $ renpy.pause(0.3, hard=True)
                hide tojb_spermshot

                hide tojb_sperm2
                show tojb_sperm3
                jin "mmmm..."
                show ctc
                pause
                hide ctc
                $ jin_buttrub_face = 'side'
                jin "that was... a lot."

                hide tojb_solodick
                y "AAaahh... and it felt good."
                jin "I'm... glad."
                show ctc
                pause
                hide ctc
                jin "i don't mean to be rude, but..."
                hide dickrub_maze_jin
                hide tojb tojb01
                show tojn tojn01
                hide tojb_sperm3
                with Dissolve(1.0)
                jin "i think we should go before-"
            "\"mouth or nothing!\"":


                hide dickrub_maze_jin
                hide tojb tojb01
                show tojn tojn03
                with dissolve
                jin "then, nothing!"






        play sound "audio/thud.mp3"
        $ current_room.special_touch = "sp_e_mdoor_2"
        show expression current_room.special_touch
        show tojn tojn02 with dissolve
        "The door suddenly slams shut."
        y "The Fuck just happened!?"
        jin "I don't know!"

        "A woman's face appears behind the bars of the now securely closed door."
        "guard" "Hahaha! You idiot! I captured you by simply closing the door!"
        "guard" "And there's no keylock on the inside!"
        "guard" "I was ready to beat you into a pulp, but this is fine too!"
        "guard" "Hahaha!"
        show tojn tojn03 with dissolve
        jin "You bitch! Step inside and repeat that!"
        y "Shitshitshit...."
        jin "I'm sorry I got you into this mess."
        y "No, I should've paid more attention to my surroundings."
        jin "So now what do we do?"
        y "If push comes to shove I think I can get us out of here, but I might bring the ceiling down on our heads in the process."
        y "So... let's try some other things first."


        $ current_room.east= -1
        $ room26.west=-1
        $ room26.special_touch = "sp_ns_md_closed"
        $ room26.sp_used = False


        $ room26.maze_enemy = True




    call screen maze_directions


label unique_room29_activate:

    if current_room.sp_used == False:
        hide open_treasurechest
        show open_treasurechest at Position(xpos=(sp_item_xpos+200), ypos=sp_item_ypos, xanchor=0, yanchor=0) with Dissolve(1.3)
        $ current_room.sp_used = True
        $ current_room.north = 28
        $ room28.south = 29

    hide tojn tojn01
    show tojn tojn01
    with dissolve
    jin "Ooohh you found an opening!"
    $ renpy.pause(0.8)
    jin "So that's where all the draft came from!"
    "{i}SSSst! "

    y "How were you in here for more than five minutes without seeing this?"
    jin "It's a very heavy looking chest! And it was empty, so why bother?"
    y "Well, whatever, let's get out of here."
    jin "sounds good to me!"
    $ maze_follower = "prisonbitch"
    jin "Let's get to the exit and I can find my own way after that."

    call screen maze_directions





label unique_room32:
    if current_room.maze_enemy == True:
        jump maze_enemies

    if current_room.maze_enemy == False and prisonbitch_key == False:
        play sound "audio/money.mp3"
        show expression "maze/prisonkey.png" with Dissolve(1.0)
        "You found a key lying on the ground!"
        hide expression "maze/prisonkey.png" with Dissolve(1.0)

        $ prisonbitch_key = True

    call screen maze_directions






label unique_room33:


    $ sp_item_xpos = 724
    $ sp_item_ypos = 177
    $ sp_item_width = 95
    $ sp_item_height = 56

    image grate_eyes:
        "maze/grate_eyes1.png"
        4.0
        "transparent.png"
        0.3
        "maze/grate_eyes1.png"
        7.0
        "transparent.png"
        0.3
        repeat


    if current_room.sp_content == 0:
        $ current_room.sp_item = True
        $ current_room.sp_used = False


        mv "Pssst!"
        mv "Hey, you! down here!"
        $ current_room.sp_content = 1


    if current_room.sp_content >= 10 and current_room.sp_content < 15:
        mv "Pssst!"
        mv "Hey you! I'm down here!"



    call screen maze_directions

label unique_room33_activate:


    if current_room.sp_content >= 10:



        if current_room.sp_content >= 15:
            $ current_room = room108
            jump bk3_maze_start

        show expression "maze/grate_eyes.jpg"
        show grate_eyes

        if current_room.sp_content < 15:
            "mysterious voice" "Hey man, I... "
            y "Yo socks, I know it's you."

        if current_room.sp_content == 11:
            sok "Oh, damn, I wanted to play a prank on you. Making you run around the maze searching for a rat."
            sok "Pretending I'd eat it."
            y "Oh, well I'll load up an earlier savegame later and fall for it."
            sok "what?"
            y "nothin"
        elif current_room.sp_content == 12:
            y "I didn't find you a rat yet."
            sok "Seriously, just go where you found June, It's somewhere around there."
            sok "But forget it, that was only supposed to be a prank anyway."
        elif current_room.sp_content == 13:
            y "I found you a rat btw."
            sok "Forget it, that was only supposed to be a prank anyway."
        elif current_room.sp_content == 14:
            y "Sorry, but I don't have a rat on me right now."
            sok "Forget it, that was only supposed to be a prank anyway."
            sok "Which btw you fell for hook line and stinker!"
            sok "I was worried you'd recognize my voice but I totally fooled you!"
            y "Eh yeah, cool."

        $ current_room.sp_content = 15


        y "We got some serious business to deal with."
        sok "Okay, come on in first. it'll be easier to talk."
        show expression "maze/grate_removed_big.png"
        "Sokka opens the grate and beckens you to crawl through."
        $ current_room.north = 108

        hide expression "maze/grate_eyes.png"


        call screen maze_directions


    if current_room.sp_content == 4:
        show expression "maze/grate_eyes.jpg"
        show grate_eyes

        menu:
            "Nevermind":
                pass
            "Show me the pornlove pages":

                mv "Okay, but give it back when you're done with it."

                $ generic_counter = 0
                while generic_counter == 0:

                    show expression "maze/grate_pornlove1.jpg" with Dissolve(1.5)

                    $ renpy.pause()

                    hide expression "maze/grate_pornlove1.jpg"
                    show expression "maze/grate_pornlove2.jpg"

                    $ renpy.pause()

                    hide expression "maze/grate_pornlove2.jpg"
                    show expression "maze/grate_pornlove3.jpg"

                    $ renpy.pause()

                    hide expression "maze/grate_pornlove3.jpg"


                    menu:
                        "read again.":
                            pass
                        "I'm done(give it back)":
                            $ generic_counter = 1
            "Can you tell me something about this pornlove edition?":



                mv "Well, with all the refugee's coming into Ba Sing Se there's a lot of new girls."
                mv "Some willing to get themselves pumped full of sperm for some coin."
                mv "So a lot of new material is being printed."
                mv "This one has a boyish looking girl with some warpaint on her face or something."
                jump unique_room33_activate


        hide expression "maze/grate_eyes.jpg"
        hide grate_eyes


    elif current_room.sp_content == 2 or current_room.sp_content == 3:
        show expression "maze/grate_eyes.jpg"
        show grate_eyes


        mv "Do you have it?"
        menu:
            "how about a small preview?":
                mv "Hmmm... Alright..."
                mv "But you'll have to look at it through the grate."
                show expression "maze/grate_pornlove1.jpg"
                show expression "maze/grate_shadows.png"

                $ renpy.pause()

                hide expression "maze/grate_shadows.png"
                hide expression "maze/grate_pornlove1.jpg"
            "Sorry, haven't seen any yet":


                mv "well, Hurry up!"
            "Where did you say I can find rats?":

                mv "Somewhere in the maze with something for them to eat."

            "I have it!" if current_room.sp_content == 3:

                "You carefully push it through the grate."
                mv "Finally!"
                mv "I'll go get the magazine and fix myself a snack!"
                $ current_room.sp_content = 4

                jump unique_room33_activate



        hide expression "maze/grate_eyes.jpg"
        hide grate_eyes

    elif current_room.sp_content == 1:
        show expression "maze/grate_eyes.jpg"
        show grate_eyes

        y "what the damn hell? There's someone in there!"
        y "Are you a prisoner? I'll get you out of there!"
        mv "NO! No, I'm fine. I used to be a prisoner but I escaped."
        mv "I'm living in this place's sewer system."
        y "Eeeh yeah... Why don't you get out of there and come with me?"
        y "There's a new village where you can take refuge."
        mv "Nah, I like it here."
        y "you... do?"
        mv "Yeah. It's nice and quiet most of the time, so nobody bothers me here."
        y "What about food?"
        mv "Rats."
        y "I haven't seen many of those around here...... oooh."
        y "Okay, I guess I'll be going now. Good luck and all that."
        mv "WAIT!"
        "I want to make you an offer!"
        y "...I'm telling you right now..."
        y "I'm NOT sticking my dick in there."
        mv "What would I want with your dick?"
        y "Sorry. It's just that this sort of thing usually ends up with me dropping my pants."
        y "So, what is it you want?"
        mv "Rats."
        y "Really? I can't get you something from a tavern?"
        mv "Rats."
        y "I'm afraid to ask, but what's in it for me?"
        mv "I'll show you the last remaining pages of my Pornlove magazine."
        y "What happened to the other pages?"
        mv "I used them for hygienic purposes."
        y ".....right."
        y "Are you suuuuure I can't get you a pizza instead?"
        y "or a tetanus shot?"
        mv "Is it a ratpizza?"
        y "Sigh. Never mind."
        y "okay, where can I find rats?"
        mv "Where there's food for rats. Breadcrumbs, dead people, etc, etc."
        y "I'll see what I can do. No promises."


        $ current_room.sp_content = 2
        hide expression "maze/grate_eyes.jpg"
        hide grate_eyes




    call screen maze_directions










label unique_room40:


    $ sp_item_xpos = 350
    $ sp_item_ypos = 170
    $ sp_item_width = 220
    $ sp_item_height = 200

    show expression current_room.special_touch at Position(xpos=sp_item_xpos, ypos=sp_item_ypos, xanchor=0, yanchor=0)

    if current_room.sp_content >= 2:
        $ current_room.sp_content = 1

    if current_room.sp_content >= 1:
        if renpy.random.choice(['0', '1']) == '1':
            if current_room.special_touch == "maze/box_open.png":
                hide expression current_room.special_touch
                $ current_room.special_touch = "maze/box_closed.png"
                show expression current_room.special_touch at Position(xpos=sp_item_xpos, ypos=sp_item_ypos, xanchor=0, yanchor=0)


            "Knock! Knock! Knock!"

            $ current_room.sp_content = 2



    call screen maze_directions

label unique_room40_activate:

    if current_room.sp_content == 3:
        "The girl inside is out cold."
        call screen maze_directions
    if current_room.sp_content == 2:
        "someone's in the box!"
        menu:
            "fist some guard bitches!":
                pass
            "nah":
                call screen maze_directions

        show expression "images/maze/fistbox/fistbox.jpg" with Dissolve (1.5)
        "a plump behind presses against the hole in the box."
        "...Eagerly awaiting what will come."
        y "Well fuck... don't mind if I do!"
        show expression "images/maze/black.png" with dissolve
        "You spit on your hand and slowly start rubbing her slit."
        "You start by inserting one finger... gently prodding until you hear soft moaning coming from outside."
        "Two fingers in, you move a bit faster."
        "After a few minutes of slowly opening her up..."

        image fistherbox:
            "images/maze/fistbox/fistbox_0.png"
            0.3
            "images/maze/fistbox/fistbox_1.png"
            0.3
            "images/maze/fistbox/fistbox_2.png"
            0.3
            "images/maze/fistbox/fistbox_3.png"
            0.3
            "images/maze/fistbox/fistbox_4.png"
            0.3
            "images/maze/fistbox/fistbox_3.png"
            0.3
            "images/maze/fistbox/fistbox_2.png"
            0.3
            "images/maze/fistbox/fistbox_1.png"
            0.3
            repeat
        hide fistbox_0
        show fistherbox
        hide expression "images/maze/black.png"
        show expression "images/maze/black.png"
        hide expression "images/maze/black.png" with Dissolve(1.5)

        "... you have your entire hand sliding in and out at a feverish pace."
        "The girl's moaning gets louder and louder."
        mv "AAhh, yes! Faaaster! Faster!"
        mv "{size=+10}Fuuuck me up!!{/size}"
        mv "{size=+15}{b}Fuuuuuuck meee uuuup!!!{/b}{/size}"

        hide fistherbox

        show expression "images/maze/fistbox/fistbox_3.png" with hpunch
        show expression "images/maze/fistbox/fistbox_3.png" with hpunch
        "With a scream of satisfaction the girl faints as she climaxes."

        hide expression "images/maze/fistbox/fistbox_3.png"
        hide expression "images/maze/fistbox/fistbox.jpg"
        hide expression "maze/box_inside.jpg"
        with Dissolve(2.0)

        y "That... was nice!"
        y "She's lucky I wasn't wearing my wristwatch."

        $ current_room.sp_content = 3

        call screen maze_directions

    if current_room.special_touch == "maze/box_closed.png":
        hide expression current_room.special_touch
        $ current_room.special_touch = "maze/box_open.png"
        show expression current_room.special_touch at Position(xpos=sp_item_xpos, ypos=sp_item_ypos, xanchor=0, yanchor=0)
    elif current_room.special_touch == "maze/box_open.png":
        hide expression current_room.special_touch
        $ current_room.special_touch = "maze/box_closed.png"
        show expression current_room.special_touch at Position(xpos=sp_item_xpos, ypos=sp_item_ypos, xanchor=0, yanchor=0)

    if current_room.special_touch == "maze/box_open.png" and current_room.sp_content == 0:
        "It looks empty. It's pretty big."
        "You step into the wooden crate and close the lid above you."
        show expression "maze/box_inside.jpg"
        y "This'd be a good hiding place!"
        y "It smells funny in here."
        y "oh, hey, there's a rock!"
        play sound "audio/win2.mp3"
        "you found 1 obsidian!"
        $ obsidian +=1
        y "neat!"
        "Just when you decide to climb out you hear voices getting close."

        "female voice 1" "So, how's work progressing?"
        "female voice 2" "As well as can be expected, captain."
        "female voice 2" "The badgermoles are a nuisance, but we can handle them."
        "female voice 1" "Good, good."
        "female voice 1" "What's with that crate? And why does it have a perfect round hole in it?"
        "female voice 2" "...uhh...well, we like to relax by playing games during our breaks."
        "female voice 1" "What sort of games?"
        "female voice 2" "...the sort where you can have anonymous fisting fun."
        "female voice 1" "So... how does that work?"
        "female voice 2" "If you hear three knocks coming from the crate it means someone's in there."
        "female voice 2" "and you can use the hole."
        "female voice 2" "Not knowing who's inside helps prevent awkward moments later on."
        "female voice 1" "Yeah, I can see how that would be a distraction."
        "female voice 1" "I'll try it myself sometime in the future."

        "The voices slowly trail off continuing their conversation as you step out of the crate."

        $ current_room.sp_content = 1
        hide expression "maze/box_inside.jpg" with Dissolve(1.0)
        y "I'm definitely going to need to visit this crate often from now on."

    call screen maze_directions







label unique_room49:


    $ sp_item_xpos = 730
    $ sp_item_ypos = 250
    $ sp_item_width = 260
    $ sp_item_height = 460


    if current_room.visit == 1:
        "You see a white butt sticking out of the wall, squirming."
        "It looks like it's stuck in the wall."


    call screen maze_directions

label unique_room49_activate:



    menu:
        "cum on her ass" if room52.sp_content == 1:
            "You start jacking off."
            y "So, how exactly did you get stuck here again?"
            ty "I was trying to get into this room by dislodging a stone and crawling through."
            ty "There was molebadger blocking the entry."
            y "But why did you want to get in here anyway?"
            ty "i'll tell you after, i promise!"
            ty "this is just... uncomfortable..."
            y "Almost there... can't you say something sexy?"
            ty "umm, bouncy boobies?"
            play sound "audio/gltch2b.mp3"
            $ current_room.special_touch2 = "maze/sp_buttwall_sperm.png"
            show expression current_room.special_touch2 with Dissolve(1.3)
            y "....."
            y "well, that worked anyway...."

            y "Okay that should be enough to do the trick."
            $ room52.sp_content = 3

        "stroke it" if room52.sp_content == 0:

            "You gently slide two fingers across her innerthigh."
            show expression current_room.maze_bg with vpunch
            mv "AAAhAAAAH!! Who's that?! Who's there!! Pleasedontbearat pleasedontbearat pleasedontbear..."

            menu:
                "Don't say anything":
                    call screen maze_directions
                "Smack that ass!":

                    $ while_counter = 0
                    play sound "audio/slap.mp3"

                    show expression current_room.maze_bg with hpunch
                    mv "Ouch!"
                    show expression "maze/sp_maze_hand.png" with Dissolve(2.0)


                    $ while_counter = 0
                    while while_counter < 10:
                        $ while_counter += 1

                        menu:
                            "stop this madness":
                                $ while_counter = 10
                            "give her another one":
                                play sound "audio/slap.mp3" 

                                show expression current_room.maze_bg with hpunch




                    if while_counter == 10:
                        y "Okay, that was fun but I've got to give my hand some rest now."

                    hide expression "maze/sp_maze_hand.png" with Dissolve(2.0)
        "don't do anything":




            call screen maze_directions


        "speak" if room49.sp_content < 1 and room52.sp_content == 0:



            $ room49.sp_content = 0
            y "Eh... hello?"
            y "Anyone there?"
            mv "no, I'm just a butt growing out of a wall!"
            mv "Wtf! Of course there's someone here!"
            mv "Can you please pull me out?"
            y "Isn't it easier to push you?"
            mv "...I think it'd prefer being pulled."
            mv "Just walk around and pull me out by holding my hands..."


    call screen maze_directions





label unique_room52:

    $ sp_item_xpos = 176
    $ sp_item_ypos = 76
    $ sp_item_width = 182
    $ sp_item_height = 388

    $ current_room.east = 43

    if room53.sp_content == 1:
        $ current_room.north = -1
        hide expression current_room.special_touch2 with Dissolve(1.0)
        $ current_room.special_touch2 = "sp_no_special"

        ty "I'll just close this so you won't be tempted to return to it later by yourself."
        ty "Okay, let's get out of here! I'll follow you."

        $ room53.sp_content = 3

    if room53.sp_content == 2:
        show expression current_room.maze_bg with vpunch
        "The secret passage automatically closes itself."
        $ room53.sp_content = 3



    if room52.sp_content != 3:
        if room49.sp_content == 1:
            y "ty lee!?"
            y "you're the other end of the talking butt?"
            ty "yup! now {i}please{/i} get me out of here."
            y "Sure, just a moment."


    if current_room.visit == 1 and room49.sp_content != 1:
        ty "hello?"
        ty "please help!"
        y "....."
        show expression "bk3/tylee/stuckwall/base.jpg"
        show tosw tosw01
        with Dissolve(1.5)
        ty "hi there! i was-"
        y "ty lee?"
        show tosw_surprise with dissolve
        ty "oh, hey! it's you!"
        y "that's... always true."
        y "you don't remember my name, do you?"
        ty "of course i do!"
        hide tosw_surprise with dissolve
        ty "you're... the avatar!"
        y "close... but not my name."
        show tosw_ashamed with dissolve
        ty "it's... um...."
        ty "wait..."
        y "...."
        hide tosw_ashamed with dissolve
        ty "aang!"
        ty "it's aang!"
        y "took you long enough."
        y "so... what are you doing here?"
        show tosw_ashamed with dissolve
        ty "I'm stuck."
        y "Yeah, I can see that."
        y "{i}why{/i} are you stuck?"
        hide tosw_ashamed with dissolve
        ty "i was treasure hunting."
        y "seriously? here, of all places?"
        show tosw_ashamed with dissolve
        ty "Could you just pull me out? please?"
        y "sure... if you can tell me why you're naked."
        hide tosw_ashamed with dissolve
        ty "have you seen the shoulderpads on those kyoshi warrior outfits?"
        ty "i had to take it off to get in here."
        y "and you still got stuck?"
        show tosw_ashamed with dissolve
        ty "stuck like a broken zipper!"
        y "oh man... that's the worst kind."
        ty "I know!"
        ty "do you think you can get me out?"
        y "I'm not sure..."
        y "I've been feeling really out of it today."
        y "and this looks pretty complicated..."
        y "i'd need to clear my head first."
        y "a blowjob really helps me think..."
        hide tosw_ashamed with dissolve
        ty "i can do that!"
        y "that's great!"
        y "(that was easy...)"
        y "let me just unzip..."
        show tosw_ashamed with dissolve
        ty "unzip?"
        y "aaand...."
        hide tosw_ashamed
        show tosw tosw02_1
        with dissolve
        y "this is my dick."
        y "have you two met?"
        show tosw tosw02
        show tosw_lookdown
        with dissolve
        ty "i don't... think so."
        ty "i think i would remember if i had."
        show ctc
        pause
        hide ctc
        ty "*sniff* *sniff*"
        ty "it has a really... strong smell."
        y "have you given a blowjob before?"
        ty "um... i'm not sure."
        y "you're not sure?"
        ty "It depends..."
        y "on what?"
        ty "...on what a blowjob is?"
        y "....."
        y "okay...."
        y "well, smelling is nice, but sucking is better."
        hide tosw_lookdown
        show tosw tosw05
        with dissolve
        ty "hmm?"
        show ctc
        pause
        hide ctc
        y "that's right!"
        y "now, you just have to go up and down on it, sucking."
        ty "......hhmmm......"
        y "(please work, please work, please work...)"
        show tosw tosw100
        ty "*sluurp* *suck* *glp*"
        show ctc
        pause
        hide ctc
        ty "hmah? *suck*"
        y "unhh... damn, girl..."
        ty "*slurp* *ssluuurp*"
        "ty lee's unrestrained enthusiasm is fully on display as she slurps and swallows your cock."
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
                y "holy shit... holy fucking shit..."
                y "take my cock, whore!"
                y "didn't your mother tell you not to suck cocks in tunnels?"
                ty "hgh?"
                y "don't... ah... fuck... don't worry about it..."
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
                y "holy shit... holy fucking shit..."
                y "take my cock, whore!"
                y "didn't your mother tell you not to suck cocks in tunnels?"
                ty "hgh?"
                y "don't... ah... fuck... don't worry about it..."
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
        y "Hey, i just had an idea."
        y "Maybe I can lube you up with sperm to get you out!"
        ty "That's a... *gulp*... great idea!"
        show tosw tosw01
        show tosw_ashamed with dissolve
        ty "Ooops!"
        ty "I... i swallowed it..."
        y "Don't worry Ty, that's totally normal."
        y "and there's more where that came from."
        hide tosw_ashamed
        ty "oh, yay!"
        ty "i guess i'll wait here, then..."
        hide tosw
        hide expression "bk3/tylee/stuckwall/base.jpg"
        with dissolve
        $ room49.sp_content = 2
        $ room52.sp_content = 1

    if room52.sp_content == 4:
        if room52.sp_used == True:

            show tfn:
                xpos -300
            with dissolve
            ty "hey, thanks for getting me out!"
            $ prisonthighs_freed = True
            ty "Anyway... Can you please get me out of here?"
            ty "I'll make it worth your effort!"

            y "I mean, I'm not just gonna leave you here."

            if maze_follower != "none":
                ty "Oh, it looks like there's already someone travelling with you."
                ty "Sorry but three is a crowd. I'll wait here until you're alone again."
                hide prisonthighs_idle with Dissolve(1.2)
                if maze_follower == "prisonbitch":

                    jin "Honestly, I would really like to get to the exit sometime soon."
            else:



                ty "Great! Let's go!"
                ty "I'll tag along and won't bother you."
                ty "Oh! one last thing."
                ty "I'm here tomb-raiding."
                ty "wanna help me?"
                ty "The split will be 80/20."
                ty "80 for me, and 20 for me. Non-negotiable."
                y "...that's not how a split works."
                ty "heehee, just a joke. Almost had you!"
                ty "80 for me, 20 for you."
                y "....ah, what the hell."
                y "alright, naked lady - let's hunt for treasure!"
                ty "It's a deal!"
                "ty lee pushes a rock and a descending stairway is revealed..."
                $ current_room.north = 53
                $ current_room.special_touch2 = "maze/stairway_down.png"
                show expression current_room.special_touch2
                show expression current_room.maze_bg with hpunch
                ty "We need to go down here."
                $ room52.sp_content = 5

                hide prisonthighs_idle with Dissolve(1.2)

                $ maze_follower = "prisonthighs"
                $ room52.sp_content = 5
                $ current_room.east = -1

                $ naga_eyes_begin = True



    call screen maze_directions

label unique_room52_activate:



    if room52.sp_content == 3:
        y "Okay, you're all spermed up."
        "you pull ty lee from the hole in the wall."
        show expression current_room.maze_bg with vpunch
        $ current_room.special_touch = "sp_no_special"
        show expression current_room.special_touch
        $ room49.special_touch = "sp_no_special"
        $ room49.special_touch2 = "sp_no_special"
        $ room49.sp_item = False
        $ room49.sp_content = 3
        $ room52.sp_content = 4
        $ room52.sp_used = True
        jump unique_room52


    if room52.sp_content != 3:

        if room49.sp_content == 2:
            ty "Please hurry and put some sperm on my thighs!"
            y "can do!"

        if room49.sp_content == 0:


            menu:
                "Try and pull her out":
                    $ room49.sp_content = 2
                    $ room52.sp_content = 1
                "Leave her be for now":
                    call screen maze_directions

            "you grab her hands and start pulling."
            ty "ouch-ouch-ouch! stop it!!"
            y "What's the matter?"
            ty "Doing it like that will rip all of the skin off my thighs!"
            ty "We'll need to lube me up somehow."
            y "Well, don't look at me, I got nothing like that on me."
            ty "...maybe you do."
            y "What are you talking about?"
            ty "this is awkward..."
            ty "um...."
            ty "you have... um..."
            ty "...sperm."
            y "What?"
            y "you can't be serious."
            ty "You heard me!"
            if maze_follower == "prisonbitch":
                jin "She's talking about your man juice!"
            y "Just to make sure... you want me to smear your ass..."
            ty "thighs!"
            y "right... thighs... with..."
            y "...sperm."
            ty "I don't see another way."
            y "Okay, just wait here and.... uh, right. nevermind."
            y "I'll find your ass and lube it up."

            $ room49.sp_content = 2
            $ room52.sp_content = 1

        if room49.sp_content == 1:
            menu:
                "Try and pull her out":
                    pass
                "Leave her be for now":
                    call screen maze_directions
            "you grab her hands and start pulling."
            ty "ouchouchouch! stop it!!"
            y "What's the matter?"
            ty "Doing it like this will rip the skin off my thighs!"
            ty "We'll need to lube it up somehow."
            y "With spit?"
            ty "M...maybe something with a higher viscosity."
            y "What are you talking about?"
            ty "um..."
            ty "awkward, but..."
            ty "...sperm."
            y "whoa. okay."
            y "Just to make sure i understand... you want me to cum on your ass?"
            ty "thighs!"
            y "Well... to be honest, I was going to do that anyway, so no problem with me."
            y "Okay, just wait here. I'll... go find your butt."

            $ room49.sp_content = 2
            $ room52.sp_content = 1





    call screen maze_directions





label unique_room53:

    $ sp_item_xpos = 717
    $ sp_item_ypos = 65
    $ sp_item_width = 270
    $ sp_item_height = 610


    if current_room.visit == 1 and maze_follower == "prisonthighs":
        show expression "maze/black.png"
        "You walk down the stairs following ty lee."
        "Your eyes slowly get used to the dark room."
        hide expression "maze/black.png" with Dissolve(3.3)
        $ maze_follower = "prisonthighs"

        y "WAAAAAA!!!?"
        show tfn:
            xpos -630
        with dissolve
        ty "Calm down, it's just a statue."
        ty "It's supposed to be a powerful spirit or something."
        ty "used to be revered for some reason or other."
        ty "There's a bit of a story behind it. I read up on it while researching where I could find it."
        ty "Wanna hear it?"
        menu:
            "Sure":
                ty "Once there were two sisters: One insane and loving, the other calculating and jealous."
                ty "They desired the same thing."
                y "What kind of thing?"
                ty "I don't know."
                y "It's a guy right? They wanted the same guy."
                ty "I don't know. Anyway-"
                y "what kind of historian are you?"
                ty "the treasure hunting kind! now hush!"
                ty "anyway... both wanted something, but only both could have it."
                y "That... doesn't make any sense."
                ty "I'm just telling you what's written in the books."
                ty "Neither wanted the other to have what they themselves desired."
                ty "And thus, they are fated to never get what they want."
                y "So what does that have to do with this snake chick?"
                ty "She's one of the sisters."
                y "which one? And why would anyone worship either?"
                ty "i'm not really sure, but it's said this one had power over the world of dreams and illusions."
                ty "it's said she could give or take away nightmares, and her illusions were flawless."
                y "She's a nightmare to look at!"
                y "i mean, you know... Except for the boobies."
                y "Hey, maybe they wanted legs!"
                y "I haven't seen either of them with those!"
                ty "....\"either of them\"?"
                y "uh... just kidding?"
                ty "....."
                ty "okay!"
            "Nope":



                y "i Don't feel like listening to boring stories."
                ty "fine."

        ty "Anyway, we're here for the eyes. They're made of precious gems."
        ty "I've got nothing on me, so you'll have to pry them out."
        y "What about the 80/20 split?"
        ty "What about it?"
        y "You can't divide two eyes up like that."
        ty "hmmm... you're right..."
        ty "well, you did rescue me."
        ty "i guess we can go 50/50."
        ty "you take one, and i'll take one."
        y "i'm... not super sure i want one, honestly."
        ty "come on, live dangerously!"
        y "yolo, okay. i need to be careful."
        ty "what?"
        y "you only live- you know what, nevermind."
        y "i'll get the damn eyes."
        y "creepy boob-snake woman."





        $ current_room.north = -1


    call screen maze_directions

label unique_room53_activate:

    "You look at the statue, half convinced it's going to lunge at you."
    "as you approach...."
    show expression "maze/maze2_nagaeyes1.png":
        alpha 1.0
        linear 1.6 alpha 0.2
        linear 1.6 alpha 1.0
        repeat
    "...it's eyes suddenly glow."
    y "um... are you seeing this?"
    ty "no. no, i'm definitely not. i'm definitely not seeing glowing eyes."
    y "i feel like... you totally are."
    ty "nope!"
    ty "now quit messing around! grab them and let's go!"
    "hesistantly, you reach forward and..."
    hide expression "maze/maze2_nagaeyes1.png"
    hide expression "maze/maze2_nagaeyes.png"
    $ current_room.special_touch = "sp_no_special"
    hide expression current_room.special_touch
    with Dissolve (1.0)
    "...surprisingly, they pop right out."
    y "huh. that was easier than-"
    "{i}ssssssssssss..........."
    y "do you... hear that?"
    ty "nope! definitely don't hear a menacing hiss!"
    y "okay, come on!"
    y "anyway, here's your half."
    ty "um... why don't you... keep those."
    y "what?"
    ty "as a... thank you?"
    y "you're afraid of a curse, aren't you?"
    ty "no."
    y "...."
    ty "yes."
    ty "but i'm sure you're gonna be fine."
    ty "now let's get out of here."
    y "alright."
    y "hey, when we get out, where are you going to go?"
    ty "i don't... actually know."
    y "tell you what, i've got a place for you."
    y "i may have mentioned it before, and it's a brothel, but-"
    ty "oh! fun!"
    ty "i'll think i'll leave you now to find my way there."
    y "....it's because of the eyes, isn't it?"
    ty "maybe!"
    y "you made me take them!"
    ty "okay, bye!"
    hide tfn with dissolve
    y "....."
    $ naga_eyes = True
    $ current_room.sp_used = True
    $ room52.north = -1
    $ room52.special_touch2 = "sp_no_special"
    $ current_room.sp_content = 2
    $ current_room.north = 52
    $ naga_eyes_begin = False
    $ maze_follower = "none"

    call screen maze_directions






label unique_room56:
    if not room56_fight:
        $ current_room.maze_enemy = True

    if current_room.maze_enemy == True:
        jump maze_enemies

    if current_room.visit ==6:
        jump maze_enemies
    else:
        call screen maze_directions






label unique_room58:

    $ sp_item_xpos = 838
    $ sp_item_ypos = 116
    $ sp_item_width = 80
    $ sp_item_height = 125
    call screen maze_directions

label unique_room58_activate:
    if bk3_allow_firebending == True:
        if current_room.special_touch2 == "sp_no_special":
            $ current_room.special_touch2 = "sp_skullflame"
            if not skull_obsidian:
                $ obsidian +=2
                play sound "audio/win2.mp3"
                "you got {b}2 obsidian{/b}!"
                $ skull_obsidian = True
                $ skull_obsidian2 = True
            if skull_obsidian and not skull_obsidian2:
                $ obsidian +=1
                play sound "audio/win2.mp3"
                "you got {b}1 obsidian{/b}!"
                $ skull_obsidian2 = True
                y "neat!"
            show expression current_room.special_touch2
        elif current_room.special_touch2 == "sp_skullflame":
            hide expression current_room.special_touch2
            $ current_room.special_touch2 = "sp_no_special"
    else:
        "Oh shit, I can't firebend right now. Well maybe later."




    call screen maze_directions






label unique_room59:
    if not room59_fight:
        $ current_room.maze_enemy = True

    if current_room.maze_enemy == True:
        jump maze_enemies

    if current_room.visit ==6:
        $ current_room.visit = 0
        jump maze_enemies
    else:
        call screen maze_directions







label unique_room60:
    show sp_spider_ani:
        ypos 0
        linear 6.0 ypos -340
        linear 6.0 ypos 0
        repeat
    call screen maze_directions






label unique_room61:

    $ sp_item_xpos = 300
    $ sp_item_ypos = 240
    $ sp_item_width = 380
    $ sp_item_height = 240

    if current_room.visit == 1:
        "part of the ceiling has caved in creating a small pile of rubble."



    call screen maze_directions

label unique_room61_activate:
    if current_room.sp_content == 0:
        "You search through the pile of stones."
        show expression "maze/kyoshi_dildo_key.png" with Dissolve(1.0)
        play sound "audio/money.mp3"
        "You find a couple of coins and an oddly shaped key."
        "It doesn't look like it'd fit in a doorlock. It's too small and oddly shaped."
        hide expression "maze/kyoshi_dildo_key.png" with Dissolve(1.0)
        $ current_room.sp_content = 1
        $ kyoshi_dildo_key = True
        $ emoney += 6
    elif current_room.sp_content < 4:
        "Except a few coins you missed earlier, there's nothing."
        $ emoney += 1
        $ current_room.sp_content += 1
    elif current_room.sp_content < 7:
        "Nothing."
        $ current_room.sp_content += 1
    else:
        "Dude, please stop. This isn't healthy."




    call screen maze_directions





label unique_room66:
    if maze_follower == "prisonthighs":
        $ maze_follower = "none"

    call screen maze_directions






label unique_room71:


    $ sp_item_xpos = 400
    $ sp_item_ypos = 10
    $ sp_item_width = 200
    $ sp_item_height = 250


    call screen maze_directions



label unique_room71_activate:
    if room72.visit == 0:
        "Something is blocking the door from opening on the other side."

    if current_room.special_touch2 == "sp_n_closeddoors_1" and room72.visit != 0:
        play sound "audio/door.mp3" 
        $ current_room.north = 72
        $ current_room.special_touch2 = "sp_n_opendoors_1"
        show expression current_room.special_touch2 with Dissolve(1.0)


    elif current_room.special_touch2 == "sp_n_opendoors_1":
        $ current_room.north = -1
        $ current_room.special_touch2 = "sp_n_closeddoors_1"
        show expression current_room.special_touch2 with Dissolve(1.0)
        play sound "audio/thud.mp3"


    call screen maze_directions






label unique_room72:
    if current_room.visit == 1:
        "Roots have grown all around the door on this side and are blocking it."
        "A few kicks forces the doors open."
        play sound "audio/thud.mp3"
        show expression current_room.maze_bg with vpunch
        $ room71.special_touch2 = "sp_n_opendoors_1"
        $ current_room.south = 71
        $ room71.north = 72

    call screen maze_directions





label unique_room77:


    $ sp_item_xpos = 730
    $ sp_item_ypos = 10
    $ sp_item_width = 240
    $ sp_item_height = 705


    call screen maze_directions



label unique_room77_activate:
    if current_room.sp_content == 0:
        y "She's so pale... maybe she's dead?"
        "You try to feel her pulse."
        hide expression current_room.special_touch2
        show expression "maze/sp_prisoner_june_1.png" with vpunch

        ju "NO! please no more!!"
        y "whoa!"
        y "fuck."
        y "Calm down, I'm not with whoever's been doing... whatever's been going on here."
        ju "Please help me get out of here!!"
        ju "I was trying to track down the...."
        y "who?"
        ju "wait... are you... the avatar?"
        y "yeah."
        ju ".......ehm forget i said anything about that."
        ju "i wasn't hunting anyone. and {i}definitely{/i} not you."
        y "......"
        ju "Anyway, please free me!"
        menu:
            "absolutely! but first let me ask you some questions":
                y "First who did this?"
                ju "some bitch in a triangle hat."
                y "What did she do besides stripping you naked and hanging you here?"
                ju "That's the strange thing, nothing."
                ju "Nothing besides giving me some food and water every day."
                ju "But I've been having really weird nightmares."
                ju "Voices who keep telling me something, but I can never remember what."
                ju "i don't... i remember lights, but..."
                ju "i just don't remember...."
                $ current_room.sp_content = 4
            "what do i get?":


                ju "I have money!"
                menu:
                    "Money's nice":
                        ju "Okay, free me and I'll give you lots of it!"
                        $ current_room.sp_content = 2
                        $ june_money = True
                    "I want to cum on your hairy cunt":

                        ju "What!?"
                        y "I want to cum on your hairy cunt while you say demeaning things about yourself."
                        ju "...you can't be serious"
                        y "Not interested? Okay, see you around."
                        ju "Wait! Just.. all right. it's a deal."
                        y "Lift your right leg up."
                        show expression "maze/june_hairy.png"
                        "you start jacking off."
                        y "Now start talking."
                        ju "Uuuh...I am a bitch."
                        y "go on."
                        ju "I'm a smelly, hairy bitch..."
                        y "Excellent, keep going."
                        ju "I'm a filthy whore, who's too lazy to use a razor on anything besides my armpits."
                        y "NNNGgh!"
                        play sound "audio/gltch2b.mp3"
                        show expression "maze/june_sperm1.png"
                        y "Ngh!"
                        play sound "audio/gltch2b.mp3"
                        show expression "maze/june_sperm2.png"
                        y "One...more.."
                        play sound "audio/gltch2b.mp3"
                        show expression "maze/june_sperm3.png"
                        y "AAaah..."
                        y "That was nice. You can put your leg down."

                        hide expression "maze/june_sperm1.png"
                        hide expression "maze/june_sperm2.png"
                        hide expression "maze/june_sperm3.png"
                        hide expression "maze/june_hairy.png"
                        with Dissolve(2.0)




                        $ current_room.sp_content = 3



    elif current_room.sp_content < 5:
        hide expression current_room.special_touch2
        show expression "maze/sp_prisoner_june_1.png"
        ju "Can you please, free me now?"
        menu:
            "Sorry, I'm busy. I'll be back later.":
                pass
            "Of course" if juneshackles_key == True:
                "You use the key you found earlier."
                play sound "audio/shackles_gone.mp3"                
                $ current_room.special_touch2 = "maze/sp_prisoner_june_2.png"
                show expression current_room.special_touch2
                hide expression "maze/sp_prisoner_june_1.png" with dissolve
                $ current_room.sp_item = False
                $ june_free = True

            "Of course" if juneshackles_key == False:
                "You try to open the shackles, but there's a lock preventing you."
                y "Sorry, but it looks like you'll be here for awhile longer."
                ju "What?! Why?!"
                y "There's a lock and I can't open it."
                y "Do you know where they're keeping the keys?"
                ju "I have no idea."
                y "Ah, crap."
                menu:
                    "Guess you'll be stuck here afteral.":
                        ju "But you said you'd free me!"
                        y "Look, I have no idea where the key to these shackles is."
                        y "My hands are tied.... eeeh no pun intended."
                        y "If I find them I'll come and free you."
                        $ current_room.sp_content = 5
                    "Don't worry, I'll find the key" if current_room.sp_content == 4:
                        ju "Please, hurry. I don't know how much longer I can take this."

                        $ current_room.sp_content = 6






            "what do i get?" if current_room.sp_content == 4:
                ju "I have money!"
                menu:
                    "Money's nice":
                        ju "Okay, free me and I'll give you lots of it!"
                        $ current_room.sp_content = 2
                        $ june_money = True
                    "I want to cum on your hairy cunt":

                        ju "What!?"
                        y "I want to cum on your hairy cunt while you say demeaning things about yourself."
                        ju "...you can't be serious"
                        y "Not interested? Okay, see you around."
                        ju "Wait! Just.. all right. it's a deal."
                        y "Lift your right leg up."
                        show expression "maze/june_hairy.png"
                        "you start jacking off."
                        y "Now start talking."
                        ju "Uuuh...I am a bitch."
                        y "go on."
                        ju "I'm a smelly, hairy bitch..."
                        y "Excellent, keep going."
                        ju "I'm a filthy whore, who's too lazy to use a razor on anything besides my armpits."
                        y "NNNGgh!"
                        play sound "audio/gltch2b.mp3"
                        show expression "maze/june_sperm1.png"
                        y "Ngh!"
                        play sound "audio/gltch2b.mp3"
                        show expression "maze/june_sperm2.png"
                        y "One...more.."
                        play sound "audio/gltch2b.mp3"
                        show expression "maze/june_sperm3.png"
                        y "AAaah..."
                        y "That was nice. You can put your leg down."

                        hide expression "maze/june_sperm1.png"
                        hide expression "maze/june_sperm2.png"
                        hide expression "maze/june_sperm3.png"
                        hide expression "maze/june_hairy.png"
                        with Dissolve(2.0)




                        $ current_room.sp_content = 3


            "let's have some more masturbation fun first" if current_room.sp_content == 3:
                y "Lift your right leg up."
                show expression "maze/june_hairy.png"
                "you start jacking off."
                y "Just like earlier."
                ju "I'm a smelly bitch."
                ju "I'm a smelly, hairy bitch.."
                y "Yeah...."
                ju "I'm not good enough to spit on."
                y "NNNGgh!"
                play sound "audio/gltch2b.mp3"
                show expression "maze/june_sperm1.png"
                y "Ngh!"
                play sound "audio/gltch2b.mp3"
                show expression "maze/june_sperm2.png"
                y "One...more.."
                play sound "audio/gltch2b.mp3"
                show expression "maze/june_sperm3.png"
                y "AAaah...."
                y "That was nice. You can put your leg down."

                hide expression "maze/june_sperm1.png"
                hide expression "maze/june_sperm2.png"
                hide expression "maze/june_sperm3.png"
                hide expression "maze/june_hairy.png"
                with Dissolve(2.0)
    else:

        hide expression current_room.special_touch2
        show expression "maze/sp_prisoner_june_1.png"
        "Have you found the key?"
        menu:
            "Sorry, haven't seen it yet" if juneshackles_key == False:
                ju "please hurry."
            "I think I have." if juneshackles_key == True:
                ju "Please hurry and free me!"
                menu:
                    "Okay, hold still":
                        play sound "audio/shackles_gone.mp3"                
                        $ current_room.special_touch2 = "maze/sp_prisoner_june_2.png"
                        show expression current_room.special_touch2
                        hide expression "maze/sp_prisoner_june_1.png" with dissolve
                        $ current_room.sp_item = False
                        $ june_free = True
                    "I'll be right back":

                        pass






    call screen maze_directions






label unique_room82:
    if current_room.visit == 1:
        "You see a caved in wall and a big hole in the floor."
        "Peering into the hole you can't see much more than shadows."
        "I could jump in, but there's no telling what's down there."



    call screen maze_directions





label unique_room83:


    $ sp_item_xpos = 800
    $ sp_item_ypos = 10
    $ sp_item_width = 200
    $ sp_item_height = 710

    if room33.sp_content == 2:
        "You see a rat nibbling on the lifeless hand sticking out from the rubble."
        "...and knock it unconscious."
        play sound "audio/win2.mp3"
        "You have an unconscious rat!"
        "woo!"
        show expression "maze/grate_tp.png" with Dissolve(1.0)
        hide expression "maze/grate_tp.png" with Dissolve(2.5)
        $ room33.sp_content = 3


    if current_room.visit == 1:
        show expression "maze/black.png"
        play sound "audio/thud.mp3"
        "You fall on a small pile of rubble, almost twisting your ankle."


        show expression "maze/black.png" with Dissolve(3.3):
            alpha 0.4
        "As your eyes slowly get used to the dim light you see a hand sticking out of under the rubble."
        "It's as cold as the stones surrounding it and holding a small key."
        play sound "audio/money.mp3"
        show expression "maze/prisonkey.png" with Dissolve(1.0)
        "You found a key! Maybe to unlock shackles?"
        hide expression "maze/prisonkey.png" with Dissolve(1.0)
        $ juneshackles_key = True
        "Now you'll have to get out of here somehow."

    call screen maze_directions

label unique_room83_activate:
    "You tap the wall, looking for weakpoints."
    menu:
        "Let's look further":
            pass
        "Earthbend your way out of this place!":

            $ current_room.east = 76
            $ room76.west = 83
            $ room76.special_touch = "maze/sp_w_breakthrough.png"
            show expression current_room.maze_bg with vpunch
            play audio "audio/rock_crumble.mp3"
            show expression "maze/maze_s_2.jpg" with Dissolve(2.0)
            $ current_room.maze_bg = "maze/maze_s_2.jpg"
            $ current_room.special_touch = "sp_no_special"
            $ current_room.special_touch2 = "sp_no_special"
            $ current_room.sp_item = False

    call screen maze_directions





label unique_room84:
    if current_room.visit == 1:
        play sound "audio/thud.mp3"
        with sshake
        y "ooohhh... my head...."
        y "that tiny bitch..."
        y "....I'm not gonna go easy on her asshole later."
        y "Where the hell am I?"



    call screen maze_directions





label unique_room87:


    $ sp_item_xpos = 400
    $ sp_item_ypos = 40
    $ sp_item_width = 200
    $ sp_item_height = 200

    if current_room.visit == 1:
        y "Crap, a dead end..."
        y "...and I don't want to risk the ceiling caving in on me by earthbending."
        y "I should examine this tunnel carefully. Maybe I can find some sort of clue."


    call screen maze_directions

label unique_room87_activate:

    if current_room.sp_content == 0:

        $ snakedoor_eyes = 0
        image snakedoor_ring = LiveComposite(
            (400, 400),
            (0, 0), "maze/snakedoor_ring.png",
            (0, 0), ConditionSwitch( 
                "snakedoor_eyes == 0", "transparent.png", 
                "snakedoor_eyes == 1", "maze/snakedoor_eyes_1.png", 
                "snakedoor_eyes == 2", "maze/snakedoor_eyes_2.png", 
                "snakedoor_eyes == 4", "transparent.png",)
            )


        $ current_room.sp_content = 1
        $ current_room.special_touch2 = "maze/snakedoor_smallring.png"
        show expression current_room.maze_bg with vpunch
        "you discover a strange object after brushing away some earth."
        "It seems to be embedded in the wall."


    show expression "maze/snakepuzzle_bg.jpg"
    show snakedoor_ring:
        xpos 240 ypos 20
        rotate 0
    with Dissolve(1.5)


    if current_room.sp_content >= 1 and  current_room.sp_content < 4:
        $ snakedoor_rotation = 0
        $ snakedoor_sequence_1 = [0,90,180,270,360]
        $ snakedoor_sequence_2 = [0,-90,-0,90,180]
        $ snakedoor_sequence_3 = [0,180,90,180,90]
        $ snakedoor_turns = 1

        y "I wonder what happens when I turn this."

        if snakedoor_eyes ==1:
            y "i think i need to figure out how to open both eyes."

        while snakedoor_turns < 5:


            call screen snakedoor_puzzle           

            show snakedoor_ring:
                xpos 240 ypos 20
                linear 0.5 rotate snakedoor_rotation

            if snakedoor_turns == 0:
                hide snakedoor_ring
                hide expression "maze/snakepuzzle_bg.jpg"
                show expression "maze/snakedoor_smallring.png"
                call screen maze_directions                       

            if current_room.sp_content == 1:
                if snakedoor_sequence_1[snakedoor_turns] == snakedoor_rotation:
                    $ snakedoor_turns = snakedoor_turns + 1
                    show text "{color=#ffffff}click{/color}":
                        xpos 400 ypos 100
                    $ snake_click +=1
                    if snake_click ==1:
                        y "hey, I heard a click!"
                        y "i bet when i hear a click, it means i did something right."
                        $ snake_click +=1

                    pause 1
                    hide text
                    with dissolve
                    $ renpy.pause(0.4)
                else:

                    $ snakedoor_turns = 1

            if current_room.sp_content == 2:
                if snakedoor_sequence_2[snakedoor_turns] == snakedoor_rotation:
                    $ snakedoor_turns = snakedoor_turns + 1
                    show text "{color=#ffffff}click{/color}":
                        xpos 400 ypos 100
                    pause 1
                    hide text
                    with dissolve
                else:
                    $ snakedoor_turns = 1

            if current_room.sp_content == 3:
                if snakedoor_sequence_3[snakedoor_turns] == snakedoor_rotation:
                    $ snakedoor_turns = snakedoor_turns + 1
                    show text "{color=#ffffff}click{/color}":
                        xpos 400 ypos 100
                    pause 1
                    hide text
                    with dissolve
                else:
                    $ snakedoor_turns = 1


            if snakedoor_rotation == 360 or snakedoor_rotation == -360:
                $ snakedoor_rotation = 0
                hide snakedoor_ring
                show snakedoor_ring:
                    xpos 240 ypos 20
                    rotate 0

            if snakedoor_turns > 4:
                show snakedoor_ring with hpunch
                if current_room.sp_content == 1:
                    $ snakedoor_eyes = 1
                    "One of the snake's eyes has opened!"

                    $ room87.east = 88
                    $ room87.special_touch = "maze/sp_e_sunkenwall.png"

                if current_room.sp_content == 2:
                    $ snakedoor_eyes = 2
                    $ room91.east = 90
                    $ room91.special_touch = "maze/sp_e_sunkenwall.png"

                if current_room.sp_content == 3:
                    $ snakedoor_eyes = 4
                    y "Did i break it? It's stuck as fuck."
                    y "hey, that rhymed!"

                $ current_room.sp_content += 1

    if current_room.sp_content == 4:
        y "I broke this already."



    hide snakedoor_ring
    hide expression "maze/snakepuzzle_bg.jpg"
    show expression "maze/snakedoor_smallring.png"

    if snakedoor_eyes > 0:

        show expression "maze/sp_e_sunkenwall.png"



    screen snakedoor_puzzle:
        vbox xalign 0.9 yalign 0.4:
            textbutton _("turn right") action [SetVariable("snakedoor_rotation", snakedoor_rotation + 90), Return]
            textbutton _("turn left") action [SetVariable("snakedoor_rotation", snakedoor_rotation - 90), Return]
            textbutton _("reset") action [SetVariable("snakedoor_rotation", 0), SetVariable("snakedoor_turns", 1), Return]
            textbutton _("exit") action [SetVariable("snakedoor_turns", 0), Return]

    call screen maze_directions





label unique_room90:

    if current_room.visit == 1:
        y "nice! a new room that..."
        y "...goes nowhere."
        y "just my fucking luck."
        y "why would they bother with the wall-"
        "suddenly you feel a rumbling beneath you. The earth starts shaking!"
        while current_room.sp_content < 3:
            show expression current_room.maze_bg with hpunch
            $ renpy.pause(2.0)
            $ current_room.sp_content += 1
        y "Fuck! Is this an earthquake?"
        y "i always knew this was how i'd die."
        y "alone in an abandoned tunnel."
        ya "come at me, god!"
        show expression "maze/badgermolehill.png" with Dissolve(1.5)
        $ current_room.special_touch = "maze/badgermolehill.png"
        y "whoa. what am i looking at?"
        y "i think it's time for me to put on my whoopsie-daisy-roller-bladies and scoot the fuck out of here."
        $ current_room.maze_bg = "maze/maze2_wns.jpg"

        $ previous_room = current_room
        $ current_room = roomlist[current_room.west]
        jump bk3_maze_start


    if current_room.visit == 2:

        show expression "bk3_fight/badgermole_1.png":
            ypos -50 xpos 100
            zoom 0.8
        y "aaaah!"
        y "What? You wanna fight?"
        ya "I can take you, asshole!"
        hide expression "bk3_fight/badgermole_1.png"

        show ani_badgermole_dig:
            ypos -50 xpos 100
            zoom 0.8 xalign 0.5
            easein 8.0 zoom 0.3 ypos 50
        with hpunch

        "it turns around ands starts digging."
        hide ani_badgermole_dig with Dissolve(1.5)
        y "Did I scare it off?"

        menu:
            "Call it names":
                y "that's right, who's your daddy!? I was gonna wop you right in the dick!"
                y "with my even bigger dick!"
                y "man, i'm unstop-"
                show expression "bk3_fight/badgermole_1.png":
                    xalign 0.5
                    ypos 0 xpos 500
                    zoom 0.3
                    linear 1.0 zoom 1.0 ypos 50
                y "waitwaitwait, nonono, you're the daddy! you're the da-"
                hide expression "bk3_fight/badgermole_1.png"
                $ current_room.north = 92
                $ temp_badgermole_fight = bk3_maze_fightslost
                $ current_room.sp_content = 5

                jump bk3_start_the_fight
            "Count your blessings":
                $ temp_badgermole_fight = bk3_maze_fightslost
                pass

        $ current_room.north = 92



        y "well, slap my ass and call me kitty! That little bugger dug a new tunnel!"
    call screen maze_directions




label unique_room92:
    if current_room.visit == 1:
        show ani_badgermole_dig

        if room90.sp_content == 5:
            if temp_badgermole_fight == bk3_maze_fightslost:
                y "That's right you fluffy bastard!"
                y "Dig me a way out of here or I'll take your hide!"
            else:
                y "Oh, good, it's ignoring me."

        y "wait a minute... besides digging, it's also using earthbending to find it's way?"
        y "oh... so that's how they're so good at this."
        "As you watch the badgermole, your understanding of earthbending deepens."
        play sound "audio/win2.mp3"
        "your earthbending skill increases!"
        $ earthbending +=1

        show ani_badgermole_dig:
            ypos 750 xpos 100
            zoom 1.0 xalign 0.5
            linear 5.0 zoom 0.3 ypos 250

        hide ani_badgermole_dig with Dissolve(4)

        $ current_room.north = 93



    call screen maze_directions




label unique_room93:
    if current_room.visit == 1:
        show ani_badgermole_dig:
            ypos -50
            zoom 1.3 xalign 0.5
            linear 8.0 zoom 0.3 ypos 50



        if temp_badgermole_fight != bk3_maze_fightslost:
            y "Oh, and sorry for beating on some of your kind."
            y "Don't tell Toph, okay?"
            y "I have this feeling she'd dislike that."
        else:
            y "Show that rock who's boss and dig me a way out of here!"

        hide ani_badgermole_dig with Dissolve(1.5)

        $ current_room.north = 94
        y "Woohoo!"

    call screen maze_directions





label unique_room94:
    if current_room.visit == 1:
        show ani_badgermole_dig:
            ypos -50
            zoom 1.3 xalign 0.5
            linear 8.0 zoom 0.3 ypos 50


        y "Wasn't that weird dog on the posters i was handing out at first supposed to be able to fly?"
        y "Maybe it uses airbending?"
        y "Man, if we had that flying thing we could just land right in the lap of the earthking and tell him Long Feng is an asshole."
        y "I'm not sure whether the king would take my word for it, but I'm the avatar so that should at least have some pull."
        y "i should try to find that fluffy bowling ball."
        hide ani_badgermole_dig with Dissolve(1.5)
        $ current_room.north = 95


    call screen maze_directions




label unique_room95:
    if current_room.visit == 1:
        show ani_badgermole_dig
        y "Hmmm... looks like he hit a specifically hard to get through part..."
        y "I'll come back later to see if he made some progress."
        $ current_room.maze_bg = "maze/maze2_se.jpg"
    if current_room.visit == 2:
        $ current_room.east = 96
        y "Hey, that badgermole is gone."
        y "I sure as hell hope this will lead me somewhere outside."
        $ room48.maze_bg = "maze/maze2_wes.jpg"
        $ room48.west = 96


    call screen maze_directions





label unique_room96:
    if current_room.visit == 1:
        $ toph_tunnel_training = 2
        if peasant_slut:
            show sp_prisonthighs with dissolve
            "You see Skye walk in the room licking her lips."
            skye "Oh, hi!"
            y "how the... what the hell are you doing here!?"
            skye "just making a house visit."
            skye "Ajala got lonely and had need for my \"cleaning services\"."
            skye "I felt bad for her, and threw her one."
            y "Aren't you afraid she'll take you prisoner again?"
            skye "When I finished cleaning her, she was fast asleep."
            skye "so no, not really."
            skye "I was just on my way home, but must have taken a wrong turn."
            skye "Well, I'll be going now."
            skye "bye!"
            hide sp_prisonthighs with dissolve
            y "Damn... wish I'd seen that!"
            "Mere seconds after Skye has left you see Ajala, wobbling towards you."
            show expression "maze/ajala_nude_idle.png" with dissolve
            ct "aah... aavatar... have you seen a blonde girl pass through here?"
            menu:
                "yeah (misdirect ajala)":
                    y "she went that way... *you point to the opposite direction of where Skye went*"
                    ct "Thanks!"
                    ct "That girl is the best at reaching every nook and cranny with her tongue and... erhh..."
                "No":


                    y "No, is she one of your prisoners?"
                    ct "I wish!"
                    ct "She was, but managed to get away."
                    ct "I managed to lure her back to clean my ass for money."
                    y "note to self... never kiss skye. ever."
                    ct "but I was distracted when she finished and she got away again."
                    y "Why do you want to catch her when she's giving you what you want?"
                    ct "well, skye's the best at what she does, and she knows it..."
                    ct "and her prices reflect that."

            ct "Anyway, I'll go see if I can catch up with her!"
            ct "Oh, and we've got a badgermole infestation."
            ct "we don't have enough personnel to deal with them, so be careful in these tunnels."
            ct "There are some strong ones among them."
            hide expression "maze/ajala_nude_idle.png" with Dissolve(1.5)
            "ajala stumbles off, still clearly wobbly in the legs."

    call screen maze_directions





label unique_room97:
    $ sp_item_xpos = 400
    $ sp_item_ypos = 85
    $ sp_item_width = 115
    $ sp_item_height = 70

    if current_room.visit == 1:
        show expression "maze/black.png"
        hide expression "maze/black.png" with Dissolve(2.0)
        y "oh, fuck no... not another statue..."
        y "Why the hell would they make two of 'em? One wasn't enough?"
        y "well, i'm definitely not gonna touch this one."
        y "....."
        y "i wonder why there's no head?"
        y "...."
        menu:
            "ask naga":
                y "hey, naga? are you still in my head?"
                "{i}yessss...."
                y "what's with this statue of you?"
                "{i}not me...."
                y "what are you talking about?"
                y "this is exactly like the other statue, with the eyes."
                "{i}no head...."
                y "so?"
                "{i}different head..."
                y "wait... are you saying there's another snake lady? have i met her?"
                "{i}yesss...."
                y "why is the head smashed?"
                "{i}sssecretsss..."
                y "does this have something to do with the snake puzzle?"
                y "the two snakes eating each other?"
                "{i}yesss... locked in a ssstruggle... to consssume..."
                y "and one of them is you?"
                "{i}....."
                y "what happens if i touch this statue?"
                "{i}nothing..."
                y "nothing? but when i touched your statue, you appeared in my head!"
                "{i}the eyesss..."
                y "what?"
                "{i}...."
                y "wait... is it because i still have the statue eyes that you're in my head!?"
                "{i}...."
                y "you bitch! that's what it is, isn't it!?"
                y "we're going to talk about this later!"
                y "....but i still don't wanna touch this thing."
            "not important":

                y "questions for later."
                y "right now i need to find my way out... and i don't think it's in here."
                y "but i am curious..."
                y "naga are you still in my head?"
                "{i}yesss..."
                y "huh. okay."
                y "well, i'll figure out how to leave and then we'll deal with that."
                y "i'm just not going to touch this statue."
                "{i}no risssk..."
                y "I don't care, i don't want to talk about it."
                "{i}no eyesss...."
                "you put your fingers in your ears."
                y "lalalala! i told you i don't-"
                "{i}no eyesss to risssk..."
                y "oh shit, you're in my head... plugging my ears doesn't work..."
                y "fine, i guess that-"
                y "....."
                y "wait... is it because i still have the statue eyes that you're in my head!?"
                "{i}...."
                y "you bitch! that's what it is, isn't it!?"
                y "we're going to talk about this later!"
                y "....but i still don't wanna touch this thing."

        $ current_room.sp_item = True

    if not room97_obsidian:
        y "I'm not afraid of you, you scary headless statue."
        y "I can cum all over your stupid stone tits without even touching you whenever I'd like!"
        y "I could do it right now, but maybe i don't want to!"
        y "...but maybe i do?"
        y "maybe later."

        $ current_room.sp_used = False
        $ current_room.special_touch = "transparent.png"
        y "I really want to jizz on her tits for some reason..."

    call screen maze_directions

label unique_room97_activate:
    menu:
        "cum on tits":
            play sound "audio/splurt2.ogg"
            show expression "maze/maze2_nagaroom2_sperm.png"
            with flash
            $ current_room.special_touch = "maze/maze2_nagaroom2_sperm.png"
            $ current_room.sp_used = True
            y "Hnnng... take that, bitch..."
            y "your bust covered in my load..."
            y "i covered your legacy in mine!"
            y "this is ...totally not sacrilegious... I think."
            y "eh."
            if not room97_obsidian:
                $ obsidian +=2
                $ room97_obsidian = True
                play sound "audio/win2.mp3"
                "you got 2 obsidian!"
                y "I... what? how?"
                y "....."
                y "i have magic jizz."
        "forget it":

            y "Maybe I should play it safe and leave this be."
            y "I mean, I'm sure I can unload on Toph's tits later so I don't actually need to."
            pass

    call screen maze_directions







label unique_room101:

    if current_room.visit == 1:
        show tolf tolf01:
            xpos -280
        with dissolve
        lf "hello, avatar."
        lf "how is the brainwashing coming?"
        lf "making progress?"
        y "well-"
        show tolf tolf02 with dissolve
        lf "because i know that you are {i}not{/i}."
        lf "you have betrayed my trust, avatar."
        lf "i gave you a spectacular opportunity, and you repay me with selfish decisions and ruining Ajala."
        lf "Avatar, you have become a bother that I am no longer willing to put up with."
        lf "The tunnel to the right leads to Toph, the tunnel to the left to your skybison."
        lf "You can save one by proceeding, but that would mean it's too late for the other."
        lf "Or you can save them both by going back and leaving the Earth kingdom willingly."
        y "....."
        y "Look at my eyes, fucker."
        y "You better start running long and hard."
        ya "Right now I'm going to get back my bitch and my ride..."
        ya "and afterwards... I'M GOING TO FUCK YOU UP!"
        show tolf tolf01
        show tolf_blink:
            xpos -280
        with dissolve
        lf "I have countless of soldiers to command."
        lf "at a word, i can-"
        y "Good."
        show tolf tolf02
        hide tolf_blink
        with dissolve
        y "You'll fucking need them to keep me entertained while I think up ways to slowly take you apart."
        lf "Kill him!!"
        hide tolf
        $ current_room.maze_enemy = True
        jump maze_enemies

    if current_room.visit > 1 and current_room.maze_enemy == True:
        jump maze_enemies
    call screen maze_directions




label unique_room102:

    if current_room.visit == 1 and room106.visit ==0:
        y "following this tunnel will lead me to Appa, but what about Toph?"
    call screen maze_directions





label unique_room104:
    $ bk3_handjob = 4
    if current_room.visit == 1 and room106.visit == 0:
        show expression "maze/appa_body.png"
        show expression "maze/appa_head1.png"
        show expression "maze/appa_chains_on.png"

        y "goddamnit! You're a big one!"
        hide expression "maze/appa_head1.png"
        show expression "maze/appa_head2.png":
            ypos 0
            easein 1 ypos 30
            easein 1 ypos 0
            repeat
        "appa" "NRRRHhG!!"
        y "Do you recognize me?"
        y "'cause I sure as hell don't recognize you."
        y "well, let's get rid of these chains."
        hide expression "maze/appa_chains_on.png"
        show expression "maze/appa_chains_off.png"
        y "How's that?"
        hide expression "maze/appa_head2.png"
        show expression "maze/appa_head3.png":
            ypos 0
            easein 1 ypos 30
            easein 1 ypos 0
            repeat
        y "Don't get your spit all over me you big furball."
        y "Aaawww, you're an okay dude."
        y "So, you can fly right? 'cause I'm telling you right here and now..."
        y "if you can't fly us over to the king, we're sorta fucked."
        y "Actually, how are you supposed to get out of here anyway..."
        y "You're too friggin' big to use the way I came in."

        y "Hmm... what's that up there?"
        show expression "maze/appa_head3.png":
            ypos 0


        show expression "maze/appa_bg_hatch.jpg":
            ypos -280
        with Dissolve(1.5)

        show expression "maze/appa_bg_hatch.jpg":
            ypos -280
            linear 5 ypos 0
        $ renpy.pause(1.5)
        y "looks like a hatch big enough for you."
        y "Don't know whether there's a mechanism around here to open it, but I'm just gonna force it open with earthbending."
        show expression "maze/appa_bg_hatch.jpg":
            ypos 0
        show expression "maze/appa_bg_air.png" with hpunch
        y "There, that should be enough."
        y "You go off by yourself before any Long feng assholes show up to imprison you again."
        y "I have some other stuff to do."

        hide expression "maze/appa_bg_air.png"
        hide expression "maze/appa_bg_hatch.jpg"
        with Dissolve(1.5)


        y "Well, go on. we'll meet again outside."
        "With ease, the enormous animal jumps up in the air and flies up, escaping through the hatch."


        hide expression "maze/appa_head3.png"
        hide expression "maze/appa_body.png"
        with moveouttop

        y "Good boy!"
        y "I think team Avatar has just gained air superiority!"
        y "Blitzkrieg is go!"
        y "Now let's see if Toph needs help."
        y "but I doubt it."

    elif current_room.visit == 1 and room106.visit >= 1:

        show expression "maze/appa_chains_off.png"
        y "What the hell happened here? Where's that flying furbal?"
        y "Looks like he was here."
        y "Huh, I stepped on something."
        show expression "maze/appa_mask.png" with dissolve
        y "...the fuck..."
        y "What's this doing here?"
        y "Okay, whatever. let's get out of here."
        hide expression "maze/appa_mask.png" with dissolve
        show toi toi02 with dissolve
        t "Well, you go and pick up Sokka. I'll meet up with you guys later."
        y "Sokka's in the tunnels?"
        t "Yeah, remember where you Freed Jin?"
        y "no."
        t "somewhere there you can find a grate. That's where you'll find him."
        hide toi with dissolve
        $ room33.sp_content += 10
    else:



        show expression "maze/appa_chains_off.png"




    $ appa_free = True

    call screen maze_directions



label unique_room105:

    if current_room.visit == 1 and room104.visit == 0:
        y "following this tunnel will lead me to Toph, but without Appa I'll never get enough airmiles..."
    call screen maze_directions    




label unique_room106:

    $ bk3_handjob = 4
    if current_room.visit == 1 and room104.visit == 0:


        show expression "maze/cage_toph_closed.png"
        y "What the hell?"

        show expression "maze/cage_toph_batter1.png" with hpunch
        show expression "maze/cage_toph_closed.png"

        y "Oh my god, what kind of wild animal have they put in there?"

        show expression "maze/cage_toph_batter2.png" with hpunch
        show expression "maze/cage_toph_closed.png"

        t "Aang is that you?!"
        t "get me out of here!!"
        show expression "maze/cage_toph_batter3.png" with hpunch
        show expression "maze/cage_toph_closed.png"


        y "Are you metalbending? Cool stuff!"
        t "Of course! I rule!"
        t "But it's taking me forever so help me speed this up."
        show expression "maze/cage_toph_batter4.png"
        show expression "maze/cage_toph_inside.png"
        with hpunch

        "With combined powers you break open Toph's cell."
        "You learned metalbending!!!"
        hide expression "maze/cage_toph_inside.png" with Dissolve(1.5)
        t "Toph steps out and hugs and kisses you."
        t "Great job Aang!"
        show toi toi02 with dissolve
        t "I could've gotten out myself with enough time, but it's nice of you to drop by."
        y "I don't doubt it."
        y "how did you get in there?"
        t "i was kidnapped by a couple weak-ass bounty hunters."
        t "my parents sent them to hold onto me until my mother could arrive."
        t "she's on her way now, but... we can worry about that later."
        y "fair enough."
        y "Now let's go find Appa!"
        t "Appa is somewhere here? "
        t "Yeah, let's go get him!"
        y "Right behind you!"
        hide toi with dissolve

    elif current_room.visit == 1 and room106.visit >= 1:
        show expression "maze/cage_toph_closed.png"
        show expression "maze/cage_toph_batter4.png"
        y "Toph! what happened?!"
        show toi toi02 with dissolve
        t "Some dickfaces thought they could imprison me in a metal box."
        t "turns out my parents are {i}really{/i} determined to get me back."
        t "my mother's even on her way... but we'll worry about that later."
        t "Heh, I guess I taught myself to metalbend!"
        y "That's awesome!"
        t "Sure is!"
        t "But what about you?"
        t "What the flying fuck took you so long?"
        y "exactly."
        t "what?"
        y "the flying fuck took me forever."
        t "i... don't..."
        y "I found appa and freed him."
        t "Oooh! Great job, twinkletoes!"
        y "excuse you?"
        t "i mean..."
        t "great job [bk3name]."
        y "better."
        t "Where is he?"
        y "I told him to find his way outside because I still had to get you."
        t "All right, we'll use him to fly straight to the king!"
        t "Now let's get out of here!"


        t "Well, you go and pick up Sokka. I'll meet up with you guys later"
        y "Sokka's in the tunnels?"
        t "Yeah, remember where you Freed Jin?"
        y "no."
        t "somewhere there you can find a grate. That's where you'll find him."
        $ room33.sp_content += 10
    else:

        show expression "maze/cage_toph_closed.png"
        show expression "maze/cage_toph_batter4.png"

    $ toph_free = True
    call screen maze_directions





label unique_room107:
    if current_room.maze_enemy == True:
        jump bk3_start_the_fight


    if current_room.visit == 5:
        y "this.... is one long ass tunnel."
        y "heh."
        y "....a long ass-tunnel."
        y "heh."
    elif current_room.visit == 6:
        y "shouldn't I be getting somewhere by now?"
    elif current_room.visit == 7:
        y "Is this one of those gamebreaking bugs?"
    elif current_room.visit == 8:
        ya "aaarrgh!!"
        y "Whatever is going on here, it's keeping me from getting to the end of this tunnel."
        y "This is worse than being locked up!"
        y "Okay, think...."
        y "right!"
        y "hey, Fake-naga-snake-person living in my brain... any suggestions?"
        "{i}Fake! Illusssion! You're not moving!"
        y "Illusions?"
        y "Aren't you supposed to ward me from those?"
        y "Get going and deal with it!"
        y "No free boarding in my mind, you scallywag."
        "{i}What?"
        y "You don't like pirate talk?"
        y "whatever, look, as long as you're in my mind it's your job to deal with crazy hallucination shit."
        y "Now get to it!"
        "{i}These are manmade! You're on your own."
        y "Goddamnit...."
        y "women are all the same..."
        y "one moment they're all sweet and licking you with a split tongue, then...."
        y "....."
        y "you know that I can still drop these eyestones of yours right here!"
        y "I'm going to do it!"
        y "......."
        y "Fuck."
        "{i}Rocksss move, jussst rocksss."
        y "...rocks?"
        y "OOOOhh...."
        y "There's some earthbender motherfucker messing with the tunnels!"
        y "Moving the ground under my feet and the walls as I move forward?"
        y "That means he's close by."
        ya "Okay, rockfucker. I've caught on to you!"
        ya "Show yourself or I'm going to bring these walls down on both of us!"
        show tomc tomc01:
            xpos -300
        with dissolve
        y "ajala?"
        y "what are you doing here?"
        ct "stopping you."
        y "uh... why?"
        ct "because long feng, the true ruler of basingse, has asked it of me."
        ct "this is as far as you go!"
        y "wait, let's talk this out-"
        hide tomc tomc01
        $ current_room.maze_enemy = True
        $ current_room.north = 99
        jump bk3_start_the_fight
    if current_room.sp_content == 1:






        $ current_room.sp_content = 2






        show expression "bk3/mazect/sex/hat_ground.png"
        show toms toms00
        with Dissolve(1)
        y "Oh wow, that's an odd but inviting postion to pass out in."
        y "Maybe I should hurry up finding Toph... and not fuck ajala?"
        menu:
            "Yeah... this is not the time for fucking":
                hide toms
                hide expression "bk3/mazect/sex/hat_ground.png"
                call screen maze_directions
            "Actually, this is the perfect moment for unconscious consensual sex":
                pass
        show toms toms01
        y "this... is a nice ass."
        y "juicy, warm, welcoming."
        show toms toms02
        y "oooh, and firm, too."
        y "firm, inviting... this is a fantastic ass."
        y "how have i not fucked her yet?"
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
        y "Hold still ajala, this is needed to undo Long Feng's control over you!"
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
        y "okay, What was I doing again? before Ajala attacked me?"
        y "Oh, yeah, looking for Toph."
        y "Get yourself to safety Ajala, things are going to get messy..."
        y "uh, messier."
        ct "o...okay..."
        show toms_blink with dissolve
        ct "(why am i so wet...?)"
        y "gotta go!"
        hide toms
        hide toms_blink
        hide expression "bk3/mazect/sex/sperm_pussy.png"
        hide expression "bk3/mazect/sex/sperm_ass.png"
        hide expression "bk3/mazect/sex/hat_ground.png"
        with fade

    call screen maze_directions






label unique_room108:


    $ sp_item_xpos = 460
    $ sp_item_ypos = 90
    $ sp_item_width = 125
    $ sp_item_height = 222

    if current_room.sp_content <= 1:
        show expression "maze/paperboat.png":
            xzoom 0.5 yzoom 0.5
            ypos 270 xpos 890
            linear 24 ypos 700 xpos -200 xzoom 1.7 yzoom 1.7
            linear 28
            repeat


    if current_room.sp_content == 0:
        $ renpy.pause()
        "The paperboat floating lazily down the small canal has brown gunk stuck to it..."
        show expression "maze/sokka_idle.png" with Dissolve(1.5)
        sok "Welcome to my room! Cozy, right?"
        sok "You can drop by whenever you want, but make sure to put the grate back so others won't notice."
        y "We've found appa and are going to visit the king. Wanna come along?"
        sok "Hell yeah I wanna come along! We'll meet outside."
        sok "Oh and Aang... don't take a right here."
        y "Why not?"
        sok "There's things you don't want to meet. Trust me on this."
        sok "Oh, and if you want to read my pornlove it's right there in between the other books."
        hide expression "maze/sokka_idle.png" with Dissolve(1.5)
        $ current_room.sp_content = 1

        $ renpy.pause()


    call screen maze_directions



label unique_room108_activate:

    "flipping through the books you find Sokka's pornlove."

    show expression "maze/grate_pornlove1.jpg" with Dissolve(1.5)

    show ctc
    pause
    hide ctc

    hide expression "maze/grate_pornlove1.jpg"
    show expression "maze/grate_pornlove2.jpg"

    show ctc
    pause
    hide ctc

    hide expression "maze/grate_pornlove2.jpg"
    show expression "maze/grate_pornlove3.jpg"

    show ctc
    pause
    hide ctc

    hide expression "maze/grate_pornlove3.jpg"
    if sewercrab_win:

        show pornlove_yue
        show ctc
        pause
        hide ctc

        hide pornlove_yue

    call screen maze_directions




label unique_room109:


    if current_room.visit == 1:
        $ renpy.pause()
        y "What's so horrible about this place?"
        "You see a rugged crab shuffling forward."
        show expression "bk3_fight/sewercrab.png" with Dissolve(1.5)
        y "Eeeeh... hey boy, how did you get down here?"
        y "Well... i guess it stands to reason some people would flush their crabs and them ending up here?"
        y "The world is a cruel place and..."
        "You see it slowly tearing up pornlove issues and folding them into paperboats."
        y "{size=+5}you monster!!!!"
        $ current_room.maze_enemy = True

    if current_room.maze_enemy == True:
        show expression "bk3_fight/sewercrab.png" with vpunch
        menu:
            "Leave it be, you don't need silly pornmags anyway.":
                $ current_room = previous_room
                scene black with Dissolve(1.0)
                "You slowly back up out of the tunnel."
                jump bk3_maze_start
            "Attack and destroy":

                hide expression "bk3_fight/sewercrab.png"
                jump bk3_start_the_fight

    if current_room.sp_content == 1:
        $ current_room.east = 110
        "with the crab defeated you find the tattered remains of what once must have been a beatiful collection."
        $ room108.sp_content = 2
        $ current_room.sp_content = 2


    call screen maze_directions

label unique_room109_activate:
    call screen maze_directions
label unique_room110_activate:
    call screen maze_directions





label unique_room110:

    if current_room.visit == 1:
        y "hmmm... what's up with this place? There's light coming from the ceiling."






    show expression "maze/poop_0.png":
        xpos 530 ypos -120
        linear 0.7 ypos 500
        ypos -120

    play sound "audio/thud.mp3"

    $ renpy.pause(4)

    show expression "maze/poop_0.png":
        xpos 650 ypos -120
        linear 0.7 ypos 370
        ypos -120

    play sound "audio/thud.mp3"

    $ renpy.pause(4)



    if current_room.visit == 1:
        y "Oh crap....literally."
        y "There's no way I'm going further than this."




    call screen maze_directions







label maze_update_two:




    image ani_badgermole_dig:
        ypos 800
        "maze/badgermole_dig.png"
        0.3
        im.Flip("maze/badgermole_dig.png", horizontal=True)
        0.3
        repeat

    if bk3_update_maze == 1:
        $ bk3_update_maze = 2

        $ room84 = Room(84,"room84", -1, 85    , -1,   91,   False, "maze/maze2_se.jpg",          False  ,     0 , False, 0,   "sp_no_special"         ,"sp_no_special")
        $ room85 = Room(85,"room85", 84, 86    , -1,   -1,   False, "maze/maze2_ns_0.jpg",        False  ,     0 , False, 0,   "sp_no_special"         ,"sp_no_special")
        $ room86 = Room(86,"room86", 85, -1    , -1,   87,   False, "maze/maze2_ne.jpg" ,         False  ,     0 , False, 0,   "maze/sp_n_brokenwall.png"         ,"sp_no_special")
        $ room87 = Room(87,"room87", -1, -1    , 86,   -1,   False, "maze/maze2_we.jpg",          True  ,      0 , False, 0,   "maze/sp_e_wall.png"    ,"sp_no_special")
        $ room88 = Room(88,"room88", 89, -1    , 87,   -1,   False, "maze/maze2_wns2.jpg",        False  ,     0 , False, 0,   "sp_no_special"         ,"sp_no_special")
        $ room89 = Room(89,"room89", -1, 88    , 97,   -1,   False, "maze/maze2_ws.jpg",          False  ,     0 , False, 0,   "sp_no_special"         ,"maze/sp_roots_1.png")
        $ room90 = Room(90,"room90", -1, -1    , 91,   -1,   False, "maze/maze2_ws.jpg",          False  ,     0 , False, 0,   "sp_no_special"         ,"sp_no_special")
        $ room91 = Room(91,"room91", -1, -1    , 84,   -1,   False, "maze/maze2_we.jpg",          False  ,     0 , False, 0,   "maze/sp_e_wall.png"    ,"sp_no_special")
        $ room92 = Room(92,"room92", -1, 90    , -1,   -1,   False, "maze/maze2_ns_0.jpg",        False  ,     0 , False, 0,   "sp_no_special"         ,"sp_no_special")
        $ room93 = Room(93,"room93", -1, 92    , -1,   -1,   False, "maze/maze2_ns_1.jpg",        False  ,     0 , False, 0,   "sp_no_special"         ,"sp_no_special")
        $ room94 = Room(94,"room94", -1, 93    , -1,   -1,   False, "maze/maze2_ns_0.jpg",        False  ,     0 , False, 0,   "sp_no_special"         ,"sp_no_special")
        $ room95 = Room(95,"room95", -1, 94    , -1,   -1,   False, "maze/maze2_ns_1.jpg",        False  ,     0 , False, 0,   "sp_no_special"         ,"sp_no_special")
        $ room96 = Room(96,"room96", -1, -1    , 95,   48,   False, "maze/maze2_we.jpg",          False  ,     0 , False, 0,   "sp_no_special"         ,"sp_no_special")
        $ room97 = Room(97,"room97", -1, -1    , -1,   89,   False, "maze/maze2_nagaroom2.jpg",   False  ,     0 , False, 0,   "sp_no_special"         ,"sp_no_special")


        $ roomlist = [room0,room1, room2,room3,room4,room5,room6,room7,room8,room9, room10, room11, 
                          room12, room13, room14, room15, room16, room17, room18, room19, room20, room21, room22, room23, room24, room25,
                          room26, room27, room28, room29, room30, room31, room32, room33, room34, room35, room36, room37, room38, room39,
                          room40, room41, room42, room43, room44, room45, room46, room47, room48, room49, room50, room51, room52, room53,
                          room54, room55, room56, room57, room58, room59, room60, room61, room62, room63, room64, room65, room66, room67,
                          room68, room69, room70, room71, room72, room73, room74, room75, room76, room77, room78, room79, room80, room81,
                          room82, room83, room84, room85, room86, room87, room88, room89, room90, room91, room92, room93, room94, room95,
                          room96, room97]

        $ current_room = room84
        $ previous_room = room84







label maze_update_three:


    if bk3_update_maze == 2:
        $ bk3_update_maze = 3




        $ room33.sp_item = True
        $ room33.sp_used = False

        $ room98  = Room( 98,"room98",  107, 5    , -1,   -1,   False, "maze/maze_ns_0.jpg",   False  ,    0 , False, 0,   "sp_no_special"         ,"sp_no_special")
        $ room99  = Room( 99,"room99",  -1, 98    , -1,  100,   False, "maze/maze_se_1.jpg",   False  ,    0 , False, 0,   "sp_no_special"         ,"sp_no_special")
        $ room100 = Room(100,"room100", 101,-1    , 99,   -1,   False, "maze/maze_wn_1.jpg",   False  ,    0 , False, 0,   "sp_no_special"         ,"sp_no_special")
        $ room101 = Room(101,"room101",  -1,100    , 102, 105,   False, "maze/maze_wes_1.jpg", False  ,    0 , False, 0,   "sp_no_special"         ,"sp_no_special")
        $ room102 = Room(102,"room102", 103,-1    , -1,  101,   False, "maze/maze_ne_1.jpg",   False  ,    0 , False, 0,   "sp_no_special"         ,"sp_no_special")
        $ room103 = Room(103,"room103", 104,102    , -1,   -1,   False, "maze/maze_ns_1.jpg",  False  ,    0 , False, 0,   "sp_no_special"         ,"sp_no_special")
        $ room104 = Room(104,"room104", -1,103    , -1,   -1,   False, "maze/appa_bg.jpg",     False  ,    0 , False, 0,   "sp_no_special"         ,"sp_no_special")

        $ room105 = Room(105,"room105", 106,-1    , 101,  -1,   False, "maze/maze_wn_1.jpg",   False  ,    0 , False, 0,   "sp_no_special"         ,"sp_no_special")
        $ room106 = Room(106,"room106", -1 ,105   ,  -1,  -1,   False, "maze/maze_s_1.jpg",    False  ,    0 , False, 0,   "sp_no_special"         ,"sp_no_special")


        $ room107 = Room(107,"room107", 98 ,98   ,  -1,  -1,   False, "maze/maze_ns_1.jpg",    False  ,    0 , False, 0,   "sp_no_special"         ,"sp_no_special")

        $ room108 = Room(108,"room108", 33 ,-1   ,  -1,  109,   False, "maze/sokka_room.jpg",   True  ,    0 , False, 0,   "sp_no_special"         ,"sp_no_special")
        $ room109 = Room(109,"room109", -1 ,-1   ,  108,  -1,   False, "maze/sokka_room2.jpg",  True  ,    0 , False, 0,   "sp_no_special"         ,"sp_no_special")
        $ room110 = Room(110,"room110", -1 ,-1   ,  109,  -1,   False, "maze/sokka_room2.jpg",  True  ,    0 , False, 0,   "sp_no_special"         ,"maze/sokka_room2_lights.png")


        $ roomlist = [room0,room1, room2,room3,room4,room5,room6,room7,room8,room9, room10, room11, 
                          room12, room13, room14, room15, room16, room17, room18, room19, room20, room21, room22, room23, room24, room25,
                          room26, room27, room28, room29, room30, room31, room32, room33, room34, room35, room36, room37, room38, room39,
                          room40, room41, room42, room43, room44, room45, room46, room47, room48, room49, room50, room51, room52, room53,
                          room54, room55, room56, room57, room58, room59, room60, room61, room62, room63, room64, room65, room66, room67,
                          room68, room69, room70, room71, room72, room73, room74, room75, room76, room77, room78, room79, room80, room81,
                          room82, room83, room84, room85, room86, room87, room88, room89, room90, room91, room92, room93, room94, room95,
                          room96, room97, room98, room99, room100, room101, room102, room103, room104, room105, room106, room107, room108,
                          room109,room110]





    jump bk3_maze_start







label backtotherealworld:
    if maze_follower == "prisonthighs":
        if room53.sp_content == 0 and naga_eyes != True:

            ty "i'm sticking with you until we get that treasure."

        elif naga_eyes == True:
            ty "Bye avatar!"
            ty "see you soon!"
            $ maze_follower = "none"

    if maze_follower == "prisonbitch":
        show tojn tojn01 with dissolve
        jin "Thanks for saving me. I can find my way out from here now!"
        jin "come find me at the jasmine dragon!"

        jin "Thanks again for everything. Byebye!"
        hide tojn tojn01 with dissolve

        "She waves at you and disappears."
        $ prisonbitch_freed = True
        $ maze_follower = "none"
        $ jin_prison_room = False

    if suki_free and suki_hospital == 0:
        $ current_room = roomlist[1]
        $ previous_room = roomlist[1]
        scene black with dissolve
        $ maze_music_on = False
        jump inside_hospital_building

    if suki_loose and not suki_free:
        $ current_room = roomlist[1]
        $ previous_room = roomlist[1]
        y "i need to find suki before I can leave."
        jump bk3_maze_start

    if first_maze_girl and first_maze_girl_escape:
        "Congratulations, you escaped the maze!!"
        $ bk3_day = False
        $ maze_music_on = False
        $ current_room = roomlist[1]
        $ previous_room = roomlist[1]
        jump bk3_village_background

    if first_maze_girl and not first_maze_girl_escape:
        stop music fadeout 1
        scene black
        scene lake_laogai_3
        with dissolve
        y "this... girl... is... fucking... heavy..."
        show toi toi200
        show toi_swim_angry:
            xzoom -1.0
        with dissolve
        t "stop complaining!"
        t "let's just get back to the village!"
        $ bk3_day = False
        $ maze_music_on = False
        $ current_room = roomlist[1]
        $ previous_room = roomlist[1]
        jump bk3_village_background
    else:

        show toi toi200 with dissolve
        t "come on you big baby, let's look around some more."
        hide toi toi200 with dissolve


    $ current_room = roomlist[1]
    $ previous_room = roomlist[1]
    jump bk3_maze_start
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
