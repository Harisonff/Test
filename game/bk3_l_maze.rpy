
init:

    define bk3_g1 = Character("Guard 1", color="#000000",show_side_image = Image("maze/love_guard1.png", xalign = 1.0, yalign = 1.0), window_right_padding=220, show_two_window=True, who_xpos=36)
    define bk3_g2 = Character("Guard 2", color="#000000",show_side_image = Image("maze/love_guard2.png", xalign = 1.0, yalign = 1.0), window_right_padding=220, show_two_window=True, who_xpos=36)

    $ june_sympathy = 0
    $ smellerbee_sympathy = 0

    define bk3_g1_bars = Character("Guard 1", color="#000000",show_side_image = Image("maze/love_guard1_bars.png", xalign = 1.0, yalign = 1.0), window_right_padding=220, show_two_window=True, who_xpos=36)
    define bk3_g2_bars = Character("Guard 2", color="#000000",show_side_image = Image("maze/love_guard2_bars.png", xalign = 1.0, yalign = 1.0), window_right_padding=220, show_two_window=True, who_xpos=36)

    $ meangirls_escapedmaze = 0
    $ ajala_headlock_fuckedinass = False

    define bk3_g3_jess = Character("Jessica", color="#000000",show_side_image = Image("maze/love_guard_jess.png", xalign = 1.0, yalign = 1.0), window_right_padding=220, show_two_window=True, who_xpos=36)

    define bk3_ajavag = Character("ajala", color="#000000",show_side_image = Image("bk3/ajala/vag/sideimage.png", xalign = 1.0, yalign = 1.0), window_right_padding=220, show_two_window=True, who_xpos=36)
    define bk3_ajavag1 = Character("ajala", color="#000000",show_side_image = Image("bk3/ajala/vag/sideimage_shock.png", xalign = 1.0, yalign = 1.0), window_right_padding=220, show_two_window=True, who_xpos=36)
    define bk3_ajavag2 = Character("ajala", color="#000000",show_side_image = Image("bk3/ajala/vag/sideimage_lewd.png", xalign = 1.0, yalign = 1.0), window_right_padding=220, show_two_window=True, who_xpos=36)

    define bk3_g1_b = Character("Guard 1", color="#000000",show_side_image = Image("maze/love_guardb_right.png", xalign = 1.0, yalign = 1.0), window_right_padding=220, show_two_window=True, who_xpos=36)
    define bk3_g2_b = Character("Guard 2", color="#000000",show_side_image = Image("maze/love_guardb_left.png", xalign = 1.0, yalign = 1.0), window_right_padding=220, show_two_window=True, who_xpos=36)

    $ b3love_jin_key = False
    $ b3love_jin_mazesex = 0
    $ b3love_dildo_gotit = False
    $ b3love_sokkapanties = 0
    $ b3love_pornlove1_own = False
    $ b3love_ajala_mazevag = 0
    $ meangirls_number_oflicks = 0

    $ bk3_jd_dungeon = False

    $ bk3_room38_guardsex = False



    $ bk3_rescue_idiots = 0




    $ ajala_choice = 'helpyou'
    $ bk3love_freetoph = 0



label love_bk3_init_maze_2:


    $ room0  = Room(0,"room0",  1  , -1    , -1 , -1,    False,"maze/maze_nswe.jpg",         False ,    0 , False, 0,   "sp_no_special"         ,"sp_no_special")
    $ room1  = Room(1,"room1",  2  ,  0    , -1 , -1,    False,"maze/maze_ns_0.jpg",         False ,    0 , False, 0,   "sp_roots_1"            ,"sp_no_special")
    $ room2  = Room(2,"room2",  3  ,  1    , 11 , -1,    False,"maze/maze_nsw_1.jpg",        False ,    0 , False, 0,   "sp_ne_floortiles_2"    ,"sp_no_special")
    $ room3  = Room(3,"room3",  6  ,  2    ,  4,   5,    False,"maze/maze_nswe.jpg",         False ,    0 , False, 0,   "sp_ne_floortiles_1"    ,"sp_no_special")
    $ room4  = Room(4,"room4", -1 ,  -1    , 15,   3,    False,"maze/maze_we.jpg",           True  ,   50 , False, 0,   "sp_we_floortiles_3"    ,"sp_no_special")
    $ room5  = Room(5,"room5", -1 ,  -1    ,  3,   7,    False,"maze/maze_we.jpg",           False ,    0 , False, 0,   "sp_no_special"         ,"sp_maze_grateroot")

    $ room6  = Room(6,"room6", 10 ,   3    , -1,  -1,    False,"maze/maze_ns_1.jpg",         False ,    0 , False, 0,   "sp_double_torches"     ,"sp_no_special")
    $ room7  = Room(7,"room7", -1 ,  -1    ,  5,   8,    False,"maze/maze_we.jpg",           True ,     0 , False, 0,   "sp_roots_2"            ,"sp_no_special")
    $ room8  = Room(8,"room8",  9  , -1    ,  7,  -1,    False,"maze/maze_wn_1.jpg",         False ,    0 , False, 0,   "sp_roots_3"            ,"sp_no_special")
    $ room9  = Room(9,"room9", -1  , 8     , -1,  -1,    True, "maze/maze_ns_0.jpg",         True ,     0 , False, 0,   "sp_ne_floortiles_2"    ,"sp_n_closeddoors_1")
    $ room10 = Room(10,"room10", -1  ,  6    , -1,  -1,  True, "maze/maze_ns_0.jpg",         True ,     0 , False, 0,   "sp_n_wallblocked"      ,"sp_no_special")

    $ room11 = Room(11,"room11", -1  , -1    , 12,   2,   False, "maze/maze_we.jpg",         True  ,    0 , False, 0,   "sp_we_straw"           ,"sp_no_special")
    $ room12 = Room(12,"room12", -1  , 13    , -1,  11,   False, "maze/maze_se_1.jpg",       False ,    0 , False, 0,   "sp_no_special"         ,"sp_no_special")
    $ room13 = Room(13,"room13", 12  , -1    , 14,  -1,   False, "maze/maze_wn_1.jpg",       False ,    0 , False, 0,   "sp_wn_pillar"          ,"sp_no_special")
    $ room14 = Room(14,"room14", -1  , -1    , -1,  13,   False, "maze/maze_we.jpg",         True ,     0 , False, 0,   "sp_w_wallblocked"      ,"sp_no_special")
    $ room15 = Room(15,"room15", -1  , -1    , -1,   4,   False, "maze/maze_we.jpg",         True ,     0 , False, 0,   "sp_we_crack1"          ,"sp_steam")



    $ room16   = Room(16  ,"room16", -1  ,  9    , 17,   29,   False, "maze/maze_wes_1.jpg", True ,    0 , False, 0,    "maze/love_door1_closed.png"    ,"sp_no_special")
    $ room17   = Room(17  ,"room17", -1  , -1    , 18,   16,   False, "maze/maze_we.jpg",    False ,    0 , False, 0,   "sp_no_special"          ,"sp_no_special")
    $ room18   = Room(18  ,"room18", 19  , -1    , -1,   17,   False, "maze/maze_ne_1.jpg",  False ,    0 , False, 0,   "sp_no_special"          ,"sp_no_special")
    $ room19   = Room(19  ,"room19", 20  , 18    , -1,   -1,   False, "maze/maze_ns_0.jpg",  False ,    0 , False, 0,   "sp_no_special"          ,"sp_no_special")
    $ room20   = Room(20  ,"room20", 21  , 19    , -1,   -1,   False, "maze/maze_ns_2.jpg",  True  ,    0 , False, 0,   "maze/love_room2_shadow.png"          ,"sp_no_special")

    $ room21   = Room(21  ,"room21", -1  , 20    , -1,   22,   False, "maze/maze_se_1.jpg",  False ,    0 , False, 0,   "sp_no_special"          ,"sp_no_special")
    $ room22   = Room(22  ,"room22", -1  , -1    , 21,   23,   False, "maze/maze_we.jpg",    True ,    0 , False, 0,    "maze/sp_we_grate.png"   ,"sp_no_special")
    $ room23   = Room(23  ,"room23", -1  , 24    , 22,   -1,   False, "maze/maze_ws_1.jpg",  False ,    0 , False, 0,   "sp_no_special"          ,"sp_no_special")
    $ room24   = Room(24  ,"room24", 23  , -1    , -1,   25,   False, "maze/maze_ne_1.jpg",  False ,    0 , False, 0,   "maze/love_sokkawashere.png"          ,"sp_no_special")
    $ room25   = Room(25  ,"room25", -1  , -1    , 24,   26,   False, "maze/maze_we.jpg",    False ,    0 , False, 0,   "maze/sp_northwall_pillars.png"          ,"sp_no_special")

    $ room26   = Room(26  ,"room26", -1  , 27    , 25,   -1,   False, "maze/maze_ws_1.jpg",  False ,    0 , False, 0,   "maze/sp_roots_2.png"          ,"sp_no_special")
    $ room27   = Room(27  ,"room27", 26  , 28    , -1,   -1,   False, "maze/maze_ns_0.jpg",  False ,    0 , False, 0,   "maze/sp_roots_1.png"          ,"sp_no_special")
    $ room28   = Room(28  ,"room28", 27  , -1    , 29,   -1,   True, "maze/maze_wn_1.jpg",   True ,     0 , False, 0,   "maze/love_scroll_1.png"          ,"sp_no_special")
    $ room29   = Room(29  ,"room29", -1  , -1    , 16,   28,   False, "maze/maze_we.jpg",    False ,    0 , False, 0,   "maze/sp_floortiles_3.png"          ,"sp_no_special")
    $ room30   = Room(30  ,"room30", -1  , 16    , -1,   -1,   False, "maze/love_room1.jpg", True ,    0 , False, 0,    "maze/love_room1_shadow.png"          ,"sp_no_special")


    $ roomlist = [room0,room1, room2,room3,room4,room5,room6,room7,room8,room9, room10, room11, 
                      room12, room13, room14, room15, room16,room17,room18,room19,room20,room21,
                      room22, room23, room24, room25, room26, room27, room28, room29, room30]

    $ current_room = room1
    $ previous_room = current_room
    return



label love_bk3_init_maze_3:


    $ room31  = Room(31,"room31",  32  , 10    , -1 , -1,    False,"maze/maze_ns_0.jpg",         False ,    0 , False, 0,   "sp_no_special"    ,"sp_no_special")
    $ room32  = Room(32,"room32",  -1  , 31    , 33 , 45,    False,"maze/maze_wes_1.jpg",        False ,    0 , False, 0,   "sp_no_special"    ,"sp_no_special")
    $ room33  = Room(33,"room33",  -1  , -1    , 34 , 32,    False,"maze/maze_we.jpg",           False ,    0 , False, 0,   "sp_no_special"    ,"sp_no_special")
    $ room34  = Room(34,"room34",  35  , -1    , -1 , 33,    False,"maze/maze_ne_1.jpg",         False ,    0 , False, 0,   "sp_no_special"    ,"sp_no_special")
    $ room35  = Room(35,"room35",  37  , 34    , 36 , -1,    False,"maze/maze_ns_2.jpg",         True ,    0 , False, 0,   "maze/sp_ns_metaldoor_open.png"    ,"sp_no_special")

    $ room36  = Room(36,"room36",  -1  , -1    , -1 , 35,    False,"maze/maze_s_1.jpg",          True ,     0 , False, 0,   "maze/love_metaldoor_2_open.png"    ,"bk3/suki/headlock/body_front.png")
    $ room37  = Room(37,"room37",  39  , 35    , 38 , 41,    True,"maze/maze_ns_3.jpg",         False ,    0 , False, 0,   "maze/love_wall_opening.png"    ,"maze/love_sped_3.png")
    $ room38  = Room(38,"room38",  -1  , -1    , -1 , 37,    False,"maze/maze2_s_1.jpg",         False ,    0 , False, 0,  "maze/love_roots_1.png"    ,"maze/love_metaldoor_2_open.png")
    $ room39  = Room(39,"room39",  -1  , 37    , -1 , 40,    False,"maze/maze_se_1.jpg",         False ,    0 , False, 0,   "maze/sp_roots_1.png"    ,"sp_no_special")
    $ room40  = Room(40,"room40",  -1  , -1    , 39 , -1,    False,"maze/maze_we.jpg",           True ,    0 , False, 0,   im.Flip("maze/sp_westwall_1.png",horizontal = True)    ,"sp_no_special")

    $ room41  = Room(41,"room41",  -1  , -1    , 37 , 42,    False,im.Flip("maze/maze_we.jpg",horizontal = True),         False ,    0 , False, 0,   "sp_no_special"    ,"sp_no_special")
    $ room42  = Room(42,"room42",  -1  , -1    , 41 , 43,    False,"maze/maze_we.jpg",           True ,    0 , False, 0,   "sp_no_special"    ,"sp_no_special")
    $ room43  = Room(43,"room43",  -1  , 44    , 42 , -1,    False,"maze/maze_ws_1.jpg",         False ,    0 , False, 0,   "sp_no_special"    ,"sp_no_special")
    $ room44  = Room(44,"room44",  43  , 45    , -1 , -1,    False,"maze/maze_ns_0.jpg",         False ,    0 , False, 0,   "sp_no_special"    ,"sp_no_special")
    $ room45  = Room(45,"room45",  44  , -1    , 32 , -1,    False,"maze/maze_wn_1.jpg",         False ,    0 , False, 0,   "sp_no_special"    ,"sp_no_special")
    $ room46  = Room(46,"room46",  -1  , 42    , -1 , -1,    False,"maze/love_room1.jpg",        True ,    0 , False, 0,   "maze/black50.png"    ,"sp_no_special")



    $ roomlist = [room0,room1, room2,room3,room4,room5,room6,room7,room8,room9, room10, room11, 
                      room12, room13, room14, room15, room16,room17,room18,room19,room20,room21,
                      room22, room23, room24, room25, room26, room27, room28, room29, room30, room31, room32, room33, room34, room35,
                      room36, room37, room38, room39, room40, room41, room42, room43, room44, room45, room46]

    $ current_room = room1
    $ previous_room = current_room
    return


label love_bk3_init_maze_4:




    $ room47  = Room(47,"room47",  48  , -1   , 49 , 14,    False,"maze/maze_we.jpg",     False ,    0 , False, 0,   "maze/sp_n_doorway_1.png"   ,"maze/sp_northwall_pillars.png")
    $ room48  = Room(48,"room48",  -1  , 47   , -1 , -1,    False,"maze/maze_s_1.jpg",     False ,    0 , False, 0,   "maze/sp_ceiling_rubble.png"   ,"sp_no_special")
    $ room49  = Room(49,"room49",  -1  , -1   , 50 , 47,    False,"maze/love_maze_we.jpg",     False ,    0 , False, 0,   "sp_no_special"   ,"sp_no_special")
    $ room50  = Room(50,"room50",  -1  , -1   , 51 , 49,    False,"maze/maze_we.jpg",     False ,    0 , False, 0,   "maze/sp_e_door_0.png"   ,"sp_no_special")
    $ room51  = Room(51,"room51",  -1  , -1   , 52 , 50,    False,"maze/love_maze_we.jpg",     False ,    0 , False, 0,   "maze/sp_e_door_1.png"   ,"sp_no_special")

    $ room52  = Room(52,"room52",  56  , 53   , -1 , 51,    False,im.Flip("maze/maze_nsw_1.jpg",horizontal = True),     False ,    0 , False, 0,   "maze/sp_floortiles_1.png"   ,"sp_no_special")
    $ room53  = Room(53,"room53",  52  , 54   , -1 , -1,    False,"maze/maze_ns_0.jpg",     False ,    0 , False, 0,   "sp_double_torches"   ,"sp_no_special")
    $ room54  = Room(54,"room54",  53  , -1   , -1 , 55,    False,"maze/maze_ne_1.jpg",     False ,    0 , False, 0,   im.Flip("maze/sp_eastwall_3.png",horizontal = True)   ,"sp_no_special")
    $ room55  = Room(55,"room55",  -1  , -1   , 54 , -1,    False,"maze/maze_we.jpg",     True ,    0 , False, 0,   "maze/sp_eastwall_1.png"   ,"sp_no_special")
    $ room56  = Room(56,"room56",  57  , 52   , -1 , -1,    False,"maze/maze_ns_0.jpg",     False ,    0 , False, 0,   "maze/sp_floortiles_2.png"   ,"sp_no_special")

    $ room57  = Room(57,"room57",  -1  , 56   , 58 , 59,    False,"maze/maze_wes_1.jpg",     False ,    0 , False, 0,   "sp_no_special"   ,"sp_no_special")
    $ room58  = Room(58,"room58",  -1  , -1   , -1 , 57,    False,"maze/love_jinshackles_room.jpg",       True ,    0 , False, 0,   "sp_no_special"   ,"sp_no_special")
    $ room59  = Room(59,"room59",  -1  , -1   , 57 , 60,    False,"maze/love_maze_we.jpg",   False ,    0 , False, 0,   "sp_no_special"   ,"sp_no_special")
    $ room60  = Room(60,"room60",  -1  , -1   , 59 , 61,    False,"maze/maze_we.jpg",        False ,    0 , False, 0,   "sp_no_special"   ,"sp_no_special")
    $ room61  = Room(61,"room61",  -1  , -1   , 60 , 62,    False,"maze/love_maze_we.jpg",   True ,    0 , False, 0,   "sp_no_special"   ,"sp_no_special")

    $ room62  = Room(62,"room62",  -1  , -1   , 61 , -1,    False,"maze/maze_we.jpg",      True ,    0 , False, 0,   im.Flip("maze/sp_westwall_1.png",horizontal = True)   ,"maze/love_wallchalk.png")
    $ room63  = Room(63,"room63",  -1  , 55   , -1 , -1,    False,"maze/love_room1.jpg",     True ,    0 , False, 0,   "maze/love_room1_shadow.png"   ,"sp_no_special")



    $ roomlist = [room0,room1, room2,room3,room4,room5,room6,room7,room8,room9, room10, room11, 
                      room12, room13, room14, room15, room16,room17,room18,room19,room20,room21,
                      room22, room23, room24, room25, room26, room27, room28, room29, room30, room31, room32, room33, room34, room35,
                      room36, room37, room38, room39, room40, room41, room42, room43, room44, room45, room46, room47, room48, room49,
                      room50, room51, room52, room53, room54, room55, room56, room57, room58, room59, room60, room61, room62, room63]

    $ current_room = room1
    $ previous_room = current_room
    return

label love_bk3_init_maze_5:



    $ room64  = Room(64,"room64",  65  , -1   , 73 , 15,    False, "maze/maze2_wne_0.jpg",     False ,    0 ,    False, 0,   "sp_no_special"   ,"sp_no_special")
    $ room65  = Room(65,"room65",  66  , 64   , -1 , -1,    False, "maze/maze2_ns_0.jpg",        False ,    0 ,    False, 0,   "sp_no_special"   ,"sp_no_special")
    $ room66  = Room(66,"room66",  -1  , 65   , 67 , -1,    True, "maze/maze2_ws.jpg",        False ,    0 ,    False, 0,   "sp_no_special"   ,"sp_no_special")

    $ room67  = Room(67,"room67",  -1  , -1   , 68 , 66,    False, "maze/maze2_we.jpg",        False ,    0 ,    False, 0,   "sp_no_special"   ,"sp_no_special")
    $ room68  = Room(68,"room68",  -1  , 74   , 69 , 67,    False, "maze/maze2_wes.jpg",        False ,    0 ,    False, 0,   "sp_no_special"   ,"sp_no_special")

    $ room69  = Room(69,"room69",  -1  , -1   , -1 , 68,    False, "maze/maze2_we.jpg",        False ,    0 ,    False, 0,   "sp_no_special"   ,"sp_no_special")
    $ room70  = Room(70,"room70",  -1  , 71   , -1 , -1,    False, im.Flip("maze/maze2_s_1.jpg", horizontal = True),        True ,    0 ,    False, 0,   "sp_no_special"   ,"sp_no_special")

    $ room71  = Room(71,"room71",  70  , -1   , -1 , 72,    True, "maze/maze2_ne.jpg",        False ,    0 ,    False, 0,   "maze/love_brokenwall.png"   ,"sp_no_special")
    $ room72  = Room(72,"room72",  74  , -1   , 71 , 73,    False, "maze/love_maze2_nwe.jpg",        False ,    0 ,    False, 0,   "sp_no_special"   ,"sp_no_special")

    $ room73  = Room(73,"room73",  -1  , -1   , 72 , 64,    False, "maze/maze2_wes.jpg",        False ,    0 ,    False, 0,   "sp_no_special"   ,"sp_no_special")
    $ room74  = Room(74,"room74",  68  , 72   , -1 , -1,    False, "maze/love_maze2_ns_2.jpg",   True ,    0 ,    False, 0,   "sp_no_special"   ,"sp_no_special")
    $ room75  = Room(75,"room75",  -1  , -1   , -1 , -1,    False, "maze/maze2_nagaroom.jpg",   False ,    0 ,    False, 0,   "sp_no_special"   ,"sp_no_special")



    $ room76  = Room(76,"room76",  77  , 25   , -1 , -1,    False, "maze/maze_ns_0.jpg",       False ,    0 ,    False, 0,   "maze/love_shadow1.png"   ,"sp_no_special")
    $ room77  = Room(77,"room77",  79  , 76   , -1 , -1,    False, "maze/love_maze_ns1.jpg",   False ,    0 ,    False, 0,   "sp_no_special"   ,"sp_no_special")

    $ room78  = Room(78,"room78",  -1  , -1   , -1 , 79,    False, im.Flip("maze/love_dungeon_we.jpg",horizontal = True), True ,    0 ,    False, 0,   "maze/love_dung_bclose.png"   ,"sp_no_special")
    $ room79  = Room(79,"room79",  -1  , 77   , 78 , 80,    False, "maze/love_dungeon_we.jpg"                           , True ,    0 ,    False, 0,   im.Flip("maze/love_dung_bclose.png",horizontal = True)   ,"sp_no_special")
    $ room80  = Room(80,"room80",  -1  , -1   , 79 , 81,    False, im.Flip("maze/love_dungeon_we.jpg",horizontal = True), True ,    0 ,    False, 0,   "maze/love_dung_bclose.png"   ,"sp_no_special")
    $ room81  = Room(81,"room81",  -1  , -1   , 80 , -1,    False, "maze/love_dung_guardroom.jpg"                       , True ,    0 ,    False, 0,   "sp_no_special"   ,"sp_no_special")




    $ roomlist = [room0,room1, room2,room3,room4,room5,room6,room7,room8,room9, room10, room11, 
                      room12, room13, room14, room15, room16,room17,room18,room19,room20,room21,
                      room22, room23, room24, room25, room26, room27, room28, room29, room30, room31, room32, room33, room34, room35,
                      room36, room37, room38, room39, room40, room41, room42, room43, room44, room45, room46, room47, room48, room49,
                      room50, room51, room52, room53, room54, room55, room56, room57, room58, room59, room60, room61, room62, room63,
                      room64, room65, room66, room67, room68, room69, room70, room71, room72, room73, room74, room75, room76, room77,
                      room78, room79, room80, room81]

    $ current_room = room1
    $ previous_room = current_room
    return




label love_bk3_init_maze_6:



    $ room82  = Room(82,"room82",  -1  , 83   , 63, -1,    False, "maze/maze2_ws.jpg",     False ,    0 ,    False, 0,   "sp_no_special"   ,"sp_no_special")
    $ room83  = Room(83,"room83",  82  , -1   , 84, -1,    False, "maze/maze2_wns.jpg",     False ,    0 ,    False, 0,   "sp_no_special"   ,"sp_no_special")
    $ room84  = Room(84,"room84",  -1  , 86   , 85, 83,    False, "maze/maze2_wes.jpg",     False ,    0 ,    False, 0,   "sp_no_special"   ,"sp_no_special")
    $ room85  = Room(85,"room85",  -1  , -1   , -1, 84,    False, im.Flip("maze/maze2_we.jpg",horizontal=True),     False ,    0 ,    False, 0,   im.Flip("maze/sp_e_wall.png",horizontal=True)    ,"sp_no_special")

    $ room86  = Room(86,"room86",  84  , 87   , -1, -1,    False, "maze/maze2_ns_0.jpg",     False ,    0 ,    False, 0,   "sp_no_special"   ,"sp_no_special")
    $ room87  = Room(87,"room87",  86  , -1   , -1, -1,    False, "maze/maze2_ns_1.jpg",     False ,    0 ,    False, 0,   "sp_no_special"   ,"sp_no_special")
    $ room88  = Room(88,"room88",  -1  , -1   , 89, 87,    False, im.Flip("maze/maze2_we.jpg",horizontal=True),     False ,    0 ,    False, 0,   "sp_no_special"   ,"sp_no_special")
    $ room89  = Room(89,"room89",  -1  , -1   , 90, 88,    False, "maze/maze2_we.jpg",     False ,    0 ,    False, 0,   "sp_no_special"   ,"sp_no_special")

    $ room90  = Room(90,"room90",  91  , -1   , -1, 89,    False, "maze/maze2_ne.jpg",     False ,    0 ,    False, 0,   "sp_no_special"   ,"sp_no_special")
    $ room91  = Room(91,"room91",  92  , 90   , -1, -1,    False, "maze/maze2_ns_1.jpg",     False ,    0 ,    False, 0,   "sp_no_special"   ,"sp_no_special")
    $ room92  = Room(92,"room92",  95  , 91   , -1, -1,    False, "maze/maze2_ns_0.jpg",     True ,    0 ,    False, 0,   "sp_no_special"   ,"sp_no_special")
    $ room93  = Room(93,"room93",  -1  , -1   , 92, -1,    False, "maze/maze2_we.jpg",     True ,    0 ,    False, 0,   "maze/sp_e_wall.png"   ,"maze/snakedoor_smallring.png")

    $ room94  = Room(94,"room94",  -1  , -1   , -1, 92,    False, "maze/maze2_nagaroom2.jpg",     False ,    0 ,    False, 0,   "sp_no_special"   ,"sp_no_special")
    $ room95  = Room(95,"room95",  96  , 92   , -1, -1,    False, "maze/maze2_ns_1.jpg",     False ,    0 ,    False, 0,   "maze/sp_n_brokenwall.png"   ,"sp_no_special")
    $ room96  = Room(96,"room96",  -1  , 95   , -1, 97,    False, "maze/maze2_se.jpg",     False ,    0 ,    False, 0,   "sp_no_special"   ,"sp_no_special")
    $ room97  = Room(97,"room97",  -1  , -1   , 96, 69,    False, im.Flip("maze/maze2_we.jpg",horizontal=True),     False ,    0 ,    False, 0,   "sp_no_special"   ,"sp_no_special")




    $ roomlist = [room0,room1, room2,room3,room4,room5,room6,room7,room8,room9, room10, room11, 
                      room12, room13, room14, room15, room16,room17,room18,room19,room20,room21,
                      room22, room23, room24, room25, room26, room27, room28, room29, room30, room31, room32, room33, room34, room35,
                      room36, room37, room38, room39, room40, room41, room42, room43, room44, room45, room46, room47, room48, room49,
                      room50, room51, room52, room53, room54, room55, room56, room57, room58, room59, room60, room61, room62, room63,
                      room64, room65, room66, room67, room68, room69, room70, room71, room72, room73, room74, room75, room76, room77,
                      room78, room79, room80, room81, room82, room83, room84, room85, room86, room87, room88, room89, room90, room91,
                      room92, room93, room94, room95, room96, room97]

    $ current_room = room1
    $ previous_room = current_room
    return






label love_bk3_init_maze_7:



    $ room98  = Room(98,"room98",  99  , 5   , -1, -1,    False, "maze/love_spiralstairs.jpg",     False ,    0 ,    False, 0,   "sp_no_special"   ,"sp_no_special")
    $ room99  = Room(99,"room99",  100  , 98   , -1, -1,    False, "maze/maze_ns_1.jpg",     False ,    0 ,    False, 0,   "sp_no_special"   ,"sp_no_special")
    $ room100  = Room(100,"room100",  -1  , 99   , 101, 107,    False, "maze/maze_wes_1.jpg",     False ,    0 ,    False, 0,   "sp_no_special"   ,"sp_no_special")
    $ room101  = Room(101,"room101",  102  , -1   , -1, 100,    False, "maze/maze_ne_1.jpg",     False ,    0 ,    False, 0,   "sp_no_special"   ,"sp_no_special")
    $ room102  = Room(102,"room102",  103  , 101  , -1, -1,    False, "maze/maze_ns_0.jpg",     False ,    0 ,    False, 0,   "sp_no_special"   ,"sp_no_special")
    $ room103  = Room(103,"room103",  111  , 102   , -1, 104,    False, im.Flip("maze/maze_nsw_1.jpg",horizontal=True),     False ,    0 ,    False, 0,   "sp_no_special"   ,"sp_no_special")
    $ room104  = Room(104,"room104",  -1  , -1   , 103, 105,    False, "maze/maze_we.jpg",     False ,    0 ,    False, 0,   "sp_no_special"   ,"sp_no_special")
    $ room105  = Room(105,"room105",  109  , 106   , 104, -1,    False, "maze/maze_nsw_1.jpg",     False ,    0 ,    False, 0,   "sp_no_special"   ,"sp_no_special")
    $ room106  = Room(106,"room106",  105  , 107   , -1, 108,    False, im.Flip("maze/maze_nsw_1.jpg",horizontal=True),     False ,    0 ,    False, 0,   "sp_no_special"   ,"sp_no_special")
    $ room107  = Room(107,"room107",  106  , -1   , 100, -1,    False, "maze/maze_wn_1.jpg",     False ,    0 ,    False, 0,   "sp_no_special"   ,"sp_no_special")
    $ room108  = Room(108,"room108",  -1  , -1   , 106, -1,    False, "maze/maze_we.jpg",     True ,    0 ,    False, 0,   im.Flip("maze/sp_westwall_1.png",horizontal=True)   ,"sp_no_special")
    $ room109  = Room(109,"room109",  110  , 105   , -1, -1,    False, "maze/maze_ns_2.jpg",     False ,    0 ,    False, 0,   "sp_no_special"   ,"sp_no_special")
    $ room110  = Room(110,"room110",  -1  , 109   , -1, -1,    False, "maze/maze_s_1.jpg",     False ,    0 ,    False, 0,   "maze/cage_toph_closed.png"   ,"sp_no_special")
    $ room111  = Room(111,"room111",  -1  , 103   , -1, -1,    False, "maze/appa_bg.jpg",     False ,    0 ,    False, 0,   "sp_no_special"   ,"sp_no_special")
    $ room112  = Room(112,"room112",  -1  , 108   , -1, -1,    False, "maze/maze_s_1.jpg",     False ,    0 ,    False, 0,   "sp_no_special"   ,"sp_no_special")

    $ room113  = Room(113,"room113",  61  , -1   , -1, 114,    False, "maze/sokka_room.jpg",     True ,    0 ,    False, 0,   "sp_no_special"   ,"sp_no_special")

    $ room114  = Room(114,"room114",  -1  , -1   , 113, 115,    True, "maze/sokka_room2.jpg",     False ,    0 ,    False, 0,   "sp_no_special"   ,"sp_no_special")
    $ room115  = Room(115,"room115",  -1  , -1   , 114, -1,    False, "maze/sokka_room2.jpg",     False ,    0 ,    False, 0,   "maze/sokka_room2_bars.png"   ,"sp_no_special")




    $ roomlist = [room0,room1, room2,room3,room4,room5,room6,room7,room8,room9, room10, room11, 
                      room12, room13, room14, room15, room16,room17,room18,room19,room20,room21,
                      room22, room23, room24, room25, room26, room27, room28, room29, room30, room31, room32, room33, room34, room35,
                      room36, room37, room38, room39, room40, room41, room42, room43, room44, room45, room46, room47, room48, room49,
                      room50, room51, room52, room53, room54, room55, room56, room57, room58, room59, room60, room61, room62, room63,
                      room64, room65, room66, room67, room68, room69, room70, room71, room72, room73, room74, room75, room76, room77,
                      room78, room79, room80, room81, room82, room83, room84, room85, room86, room87, room88, room89, room90, room91,
                      room92, room93, room94, room95, room96, room97, room98, room99, room100,room101, room102,room103,room104,
                      room105,room106,room107,room108,room109,room110,room111, room112, room113, room114, room115]

    $ current_room = room1
    $ previous_room = current_room
    return




label love_bk3_maze_start:
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
        call bk3_init_maze_1 from _call_bk3_init_maze_1_1

    if bk3_update_maze == 1:
        $ bk3_update_maze = 2
        call love_bk3_init_maze_2 from _call_love_bk3_init_maze_2



    if bk3_update_maze == 2:
        $ bk3_update_maze = 3
        call love_bk3_init_maze_3 from _call_love_bk3_init_maze_3



    if bk3_update_maze == 3:
        $ bk3_update_maze = 4
        call love_bk3_init_maze_4 from _call_love_bk3_init_maze_4

    if bk3_update_maze == 4:
        $ bk3_update_maze = 5
        call love_bk3_init_maze_5 from _call_love_bk3_init_maze_5



    if bk3_update_maze == 5:
        $ bk3_update_maze = 6
        call love_bk3_init_maze_6 from _call_love_bk3_init_maze_6





    if bk3_update_maze == 6:
        $ bk3_update_maze = 7
        call love_bk3_init_maze_7 from _call_love_bk3_init_maze_7




    $ current_room.visit = current_room.visit + 1



    if current_room == room0:
        jump love_backtotherealworld



    scene black



    show expression current_room.maze_bg



    if current_room.special_touch != "sp_no_special":
        show expression current_room.special_touch
    if current_room.special_touch2 != "sp_no_special":
        show expression current_room.special_touch2






    if current_room.roomnr in [1,4,5,7,9,10,14,15,16,20,22,25,28,30,32,35,36,38,40,42,46,47,55,57,58,61,62,63,70,74,75,76,
        77,78,79,80,81,82,85,87,88,89,90,92,93,94,96,98,108,109,110,111,112,113,114]:

        $ renpy.jump ("love_unique_"+current_room.rname)




    $ bk3_enemyreturn_rooms = [3]



    if current_room.roomnr in bk3_enemyreturn_rooms:
        if current_room.visit >= 6:
            if (current_room.visit%6) == 0:
                jump love_maze_enemies



    if current_room.maze_enemy:
        jump love_maze_enemies


    call screen love_maze_directions



screen love_maze_directions:




    imagemap:

        ground "maze/directions.png"
        hover "maze/directions_on.png"
        idle "maze/directions_transparent.png"













        if current_room.north >= 0:
            hotspot (465, 524, 101, 112) action [SetVariable("previous_room",current_room), SetVariable("current_room",roomlist[current_room.north]), Jump("love_bk3_maze_start")]
            key "focus_up" action [SetVariable("previous_room",current_room),SetVariable("current_room",roomlist[current_room.north]), Jump("love_bk3_maze_start")]

        if current_room.south >= 0:
            hotspot (363, 635, 300, 84) action [SetVariable("previous_room",current_room), SetVariable("current_room",roomlist[current_room.south]), Jump("love_bk3_maze_start")]
            key "focus_down" action [SetVariable("previous_room",current_room),SetVariable("current_room",roomlist[current_room.south]), Jump("love_bk3_maze_start")]

        if current_room.west >= 0:
            hotspot (363, 524, 104, 110) action [SetVariable("previous_room",current_room), SetVariable("current_room",roomlist[current_room.west]), Jump("love_bk3_maze_start")]
            key "focus_left" action [SetVariable("previous_room",current_room),SetVariable("current_room",roomlist[current_room.west]), Jump("love_bk3_maze_start")]

        if current_room.east >= 0:
            hotspot (566, 526, 98, 110) action [SetVariable("previous_room",current_room), SetVariable("current_room",roomlist[current_room.east]), Jump("love_bk3_maze_start")]
            key "focus_right" action [SetVariable("previous_room",current_room),SetVariable("current_room",roomlist[current_room.east]), Jump("love_bk3_maze_start")]

        if current_room.sp_item == True and current_room.sp_used == False:
            hotspot (sp_item_xpos, sp_item_ypos, sp_item_width, sp_item_height) action Jump("love_unique_"+current_room.rname+"_activate")

        if love_bk3_map:
            textbutton "{color=#000000}map" action Jump("love_maze_map_screen") xpos 0.28 ypos 10
        if maze_fight_tutorial:
            textbutton "{color=#000000}Character stats" action Jump("love_maze_character_screen") xpos 0.375 ypos 10
        if maze_fight_tutorial:
            if toph_tunnel_training !=1 and not suki_headlocking:
                if bk3_rescue_idiots <3 or bk3_rescue_idiots >3:
                    if bk3love_freetoph < 1 or love_toph_freed:
                        textbutton "{color=#000000}entrance" action Jump("love_backtotherealworld") xpos 0.62 ypos 10
        if jd_break_hypno >=2:
            if bk3_rescue_idiots <3 or bk3_rescue_idiots >3:
                textbutton "{color=#000000}find ajala" action Jump("love_find_ajala") xpos 0.1 ypos 10

label love_maze_character_screen:
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
    show screen love_bk3_level_up_stats1
    show ctc
    pause
    hide ctc
    hide screen love_bk3_level_up_stats1
    jump love_bk3_maze_start

label love_maze_map_screen:
    show map_dungeonentry
    show ctc
    pause
    hide ctc
    hide map_dungeonentry
    jump love_bk3_maze_start



label love_treasure_chest:

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







label love_maze_enemies:


    if current_room.roomnr in [66,71]:
        show expression "maze/maze_enemies_badgermole.png" with hpunch
    else:
        show expression "maze/maze_enemies.png" with hpunch

    menu:
        "Run for your life!":

            $ current_room = previous_room
            scene black with Dissolve(1.0)
            "You quickly retreat. The enemy doesn't follow you."
            jump love_bk3_maze_start
        "Attack!":


            if current_room.roomnr in [66,71]:
                hide expression "maze/maze_enemies_badgermole.png"
            elif current_room.roomnr == 47:
                hide expression "maze/love_ajala_angry.png"
                $ room47.maze_enemy = False
            else:
                hide expression "maze/maze_enemies.png"

            jump love_bk3_start_the_fight








label love_unique_room1:


    if bk3love_freetoph == 1:
        show expression "maze/sokka_idle.png"
        sok "Dude! They got their hands on Toph!!"
        y "Do you know where they're keeping her?"
        sok "I don't, but I did see that buff Ajala woman go into a secret passage."
        y "Okay, that's as good as any place to start looking."
        y "Where?"
        sok "Up, up right. I'll wait for you there."
        hide expression "maze/sokka_idle.png" with Dissolve(1.5)
        "Sokka dashes off in the direction he just described."
        $ bk3love_freetoph = 2


    if not love_ajala_visited:
        $ love_ajala_visited = True
        if jd_break_hypno ==1:
            show dark_tunnel
            show tomc tomc01
            with dissolve
            ct "who...?"
            show tomc tomc03 with dissolve
            ct "what the..."
            show tomc tomc05
            with dissolve
            ct "avatar!"
            if ajala_jd_hypno_fight:
                y "i still need your help with some hypno equipment, ajala."
                ct "no!"
                y "fine, if i have to beat it out of you, i will!"
                menu:
                    "fight ajala":
                        y "come on!"
                        hide tomc
                        jump love_bk3_start_the_fight
                    "leave":

                        y "i'll be back!"
                        hide tomc
                        hide dark_tunnel
                        with dissolve

                        pass
            else:
                y "hey, listen, i need your help."
                show tomc_surpise with dissolve
                ct "what?"
                hide tomc_surpise with dissolve
                ct "no!"
                y "look, i need your help remixing some hypno equipment."
                y "if you don't help me willingly, i'm gonna have to fight it out of you."
                ct "come and get it!"
                $ ajala_jd_hypno_fight = True
                menu:
                    "fight ajala":
                        y "fine then!"
                        hide tomc
                        jump love_bk3_start_the_fight
                    "leave":

                        y "i'll be back!"

                        hide tomc
                        hide dark_tunnel
                        with dissolve
                        jump love_bk3_maze_start



    if bk3_rescue_idiots == 1 and earthbending != 28:

        $ bk3_room38_guardsex = False
        $ bk3_rescue_idiots = 2
        show expression "maze/love_ajala_surprise.png"
        ct "Avatar! Please help me!" with hpunch
        y "...Aren't we supposed to be enemies?"
        y "With benefits, but still..."
        ct "Well, yeah, technically, but I really need your help."
        y "What's wrong?"
        ct "You've met two guards down here, one with twintails and the other with her hair in buns."
        ct "They're pretty much always together and to be honest completely incompetent..."
        y "Oh... eh, yeah, I guess."
        y "Why?"
        ct "They're missing!"
        y "......"
        ct "Abducting girls seems to be your speciality..."
        ct "I... I do realize it's a bit weird for me to ask this, but could you track them down?"
        y "Well, I don't know where they are and if they aren't down here I wouldn't know where to look."
        ct "I think I have an idea, but can't go look myself."
        ct "There's these badgermoles... I hate them..."
        ct "they're like super big rats and they make my skin crawl."
        ct "They dig tunnels and sometimes break through walls down here."
        y "You think badgermoles abducted the guards?"
        ct "I really don't know, but the room in which they were has a big hole and it's connected to badgermole tunnels."
        y "So you want me to check those out."
        ct "Please."
        ct "The girls are idiots, but they're my idiots."
        y "...fine."
        y "But you're going to owe me for this."
        y "Like, bigtime."
        ct "I understand."
        hide expression "maze/love_ajala_surprise.png"

    elif bk3_rescue_idiots ==3:
        $ bk3_rescue_idiots = 4
        show expression "maze/love_ajala_surprise.png" with hpunch
        ct "You found the girls!"
        ct "And they're safe and sound again!"
        hide expression "maze/love_ajala_surprise.png"
        show expression "maze/love_ajala_delight.png"
        with Dissolve(1.5)
        ct "Thank you."
        ct "And I'm guessing you'd like your reward now?"
        y "Yes, please."
        ct "Close your eyes."
        menu:
            "Keep them open":
                y "It's not that I don't trust you, but..."
                y "I did knock you out using a similar trick."
                y "So... I'll just keep them open."
                ct "Then I'll just show you something instead."
                hide expression "maze/love_ajala_delight.png"
                show expression "maze/love_ajala_toys.png":
                    linear 5.0 ypos -150
                with Dissolve(1.5)
                $ renpy.pause()
                ct "Whenever I miss you... I use these."
                ct "They're a poor substitute for the real thing though."
                y "....."
                "As you stare at Ajala's bottom you hear someone shouting."
                ct "I gotta go!"
                hide expression "maze/love_ajala_toys.png" with Dissolve(1.5)
                bk3_g1 "Hey dude!!!" with hpunch
                y "Oh, it's you guys...."
                bk3_g2 "Right on the money."
                bk3_g2 "Thanks again for saving us."
                bk3_g2 "Was that Ajala just now?!"
                y "Yeah, and you ruined something nice, damn it."
                bk3_g1 "Oh don't worry about it."
                bk3_g1 "Ajala is superhot for your dick."
                bk3_g1 "She ain't going anywhere."
                bk3_g2 "Yeah, but not just hot for your dick but also, you know.... "
                y "...what?"
                bk3_g1 "Looks to me like she's smitten with you!"
                y "Smitten? I didn't know that world still existed."
                y "Anyway, then why did she just run off like that?"
                bk3_g2 "Ajala is strange to begin with. "
                bk3_g2 "Mix some strong emotions in there and *BAM!* Weirdness all over the place."
                bk3_g1 "She didn't even fingerbang us!"
                bk3_g1 "She {i}ALWAYS{/i} fingerbangs us!"
                bk3_g2 "Don't know what you did to her, but please don't do it to us."
                bk3_g1 "Well, gotta go."
                bk3_g1 "see ya!"
                bk3_g2 "Later, man."
            "close your eyes":


                show expression "maze/black.png" with Dissolve(1.5)
                y "This better not be a trap."
                play sound "audio/kiss.mp3"
                show pink with dissolve
                hide expression "maze/black.png"
                $ renpy.pause(1.0)
                hide pink with Dissolve(1.5)
                ct "Hihi... I... I have to go..."
                hide expression "maze/love_ajala_delight.png" with Dissolve(1.5)
                "You still feel Ajala's soft lips on yours as she runs... no... skips off."
                y "...what!?!"
                y "This doesn't count as a proper reward!"
                y "Can someone explain to me wtf just happened?"
                bk3_g1 "Hey dude!!!" with hpunch
                y "AAAh!!"
                y "It's you guys!?"
                bk3_g2 "Right on the money."
                bk3_g2 "Thanks again for saving us."
                bk3_g1 "Oh and to answer your questions..."
                bk3_g1 "it looks like she's genuinely starting to... love you."
                bk3_g2 "Yeah, not just hot for your dick but actual feelings and all... "
                y "....really?"
                bk3_g1 "Certainly looks like it to me."
                bk3_g1 "You're dangerous, man!"
                y "Then why did she just run off like that?"
                bk3_g2 "Emotions and stuff?"
                bk3_g1 "She didn't even fingerbang us!"
                bk3_g1 "She {i}ALWAYS{/i} fingerbangs us!"
                bk3_g2 "Don't know what you did to her, but please don't do it to us."
                bk3_g1 "Well, gotta go."
                bk3_g1 "see ya!"
                bk3_g2 "Later, man."





    call screen love_maze_directions

label love_unique_room1_activate:

    call screen love_maze_directions  










label love_unique_room4:


    $ sp_item_xpos = 100
    $ sp_item_ypos = 140
    $ sp_item_width = 220
    $ sp_item_height = 200

    if current_room.sp_used:
        show open_treasurechest at Position(xpos=sp_item_xpos, ypos=sp_item_ypos, xanchor=0, yanchor=0)
    else:
        show closed_treasurechest at Position(xpos=sp_item_xpos, ypos=sp_item_ypos, xanchor=0, yanchor=0)

    call screen love_maze_directions

label love_unique_room4_activate:
    call love_treasure_chest from _call_love_treasure_chest
    $ bk3_lifepotions +=1
    play sound "audio/win2.mp3"
    "you found a life potion!"
    call screen love_maze_directions       







label love_unique_room5:


    $ sp_item_xpos = 340
    $ sp_item_ypos = 1
    $ sp_item_width = 340
    $ sp_item_height = 260

    if current_room.sp_content == 1:
        show expression "maze/love_secretdoor.png"


    if bk3love_freetoph == 2:
        $ current_room.sp_item = True
        show expression "maze/sokka_idle.png"
        sok "This is it! She did something here between the pillars."
        y "Thanks Sokka, I owe you."
        sok "What? No dog, we're in this together!"
        sok "You should come visit me again after getting toph to safety."
        sok "In fact I'll go tidy up."
        sok "Wouldn't want my sewer room to be all messy when I get a visitor."
        y "Uhhh, you're not coming along?"
        sok "No man, I'd just be in your way."
        sok "See ya!"
        hide expression "maze/sokka_idle.png" with Dissolve(1.5)
        $ bk3love_freetoph =3






    call screen love_maze_directions

label love_unique_room5_activate:
    if current_room.sp_item == True and current_room.sp_content == 0:
        "You press a specific stone in the wall and feel something move."
        play sound "audio/stonegrind.mp3"
        show expression "maze/love_secretdoor.png" with Dissolve(1.5)
        $ current_room.sp_content = 1
        $ current_room.north = 98

    elif current_room.sp_item == True and current_room.sp_content == 1:
        "You close the secret door."
        play sound "audio/stonegrind.mp3"
        hide expression "maze/love_secretdoor.png" with Dissolve(1.5)
        $ current_room.sp_content = 0
        $ current_room.north = -1

    call screen love_maze_directions  






label love_unique_room7:


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


    call screen love_maze_directions

label love_unique_room7_activate:
    play audio "audio/open_chest.mp3"
    $ renpy.pause (0.5)


    hide closed_treasurechest
    show open_treasurechest at Position(xpos=sp_item_xpos, ypos=sp_item_ypos, xanchor=0, yanchor=0)

    jump love_maze_enemies






label love_unique_room9:


    $ sp_item_xpos = 400
    $ sp_item_ypos = 10
    $ sp_item_width = 200
    $ sp_item_height = 250

    if current_room.visit==1:
        if sp_maze_key1:
            y "hmm... a closed door. Maybe my key will fit?"
        else:
            y "a closed door... but I don't have a key for it."

    if current_room.maze_enemy == True and current_room.sp_content == 1:
        y "Shit! That bitch is still here!"
        jump love_maze_enemies

    call screen love_maze_directions



label love_unique_room9_activate:

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
                "When you turn the key, the door swings open and someone jumps out through it!"
                ya "ah!"
                ya "fuck surprises!"
                jump love_maze_enemies
            "leave the door locked":

                "You leave it alone."

    if sp_maze_key1 == False:
        "I have no key which will unlock this door...yet."

    if sp_maze_key1 == True and current_room.maze_enemy == False and current_room.sp_content == 1:

        if current_room.special_touch2 == "sp_n_opendoors_1":
            $ current_room.special_touch2 = "sp_n_closeddoors_1"
            show expression current_room.special_touch2
            play sound "audio/thud.mp3"

            $ current_room.north = -1
        else:
            $ current_room.special_touch2 = "sp_n_opendoors_1"
            show expression current_room.special_touch2
            play sound "audio/door.mp3"

            $ current_room.north = 16




    call screen love_maze_directions







label love_unique_room10:


    $ sp_item_xpos = 400
    $ sp_item_ypos = 10
    $ sp_item_width = 200
    $ sp_item_height = 250

    if current_room.north == -1 and current_room.visit == 1:
        if maze_sections == 0:
            "You knock on the wall to the north, it seems there's a room behind it."
            "Too bad your earthbending is still too weak to break through it."
        else:
            "You knock on the north wall, it seems there's a room behind it."
            "You might be able to earthbend your way through it."

    call screen love_maze_directions

label love_unique_room10_activate:
    if current_room.north == -1  and maze_sections >= 1:

        menu:
            "break through":
                play audio "audio/rock_crumble.mp3"

                $ current_room.special_touch = "maze/maze_unblockedn.png"
                show expression current_room.special_touch with Dissolve(2.0)
                $ current_room.sp_used = True
                $ current_room.north = 31
                y "nice!"
            "let's not mess with this right now":

                "You leave it alone."
    else:
        "My earthbending is still too weak."

    call screen love_maze_directions



label love_unique_room11:
    show npc_emptyshackles at Position(xpos=sp_item_xpos, ypos=sp_item_ypos, xanchor=0, yanchor=0)

    call screen love_maze_directions

label love_unique_room11_activate:


    $ sp_item_xpos = 200
    $ sp_item_ypos = 0
    $ sp_item_width = 170
    $ sp_item_height = 300

    show npc_emptyshackles at Position(xpos=sp_item_xpos, ypos=sp_item_ypos, xanchor=0, yanchor=0)

    call screen love_maze_directions





label love_unique_room14:


    $ sp_item_xpos = 1
    $ sp_item_ypos = 1
    $ sp_item_width = 140
    $ sp_item_height = 430


    if current_room.west == -1 and current_room.visit == 1:
        if maze_sections == 0:
            "You knock on the west wall, it seems there's a room behind it."
            "Too bad your earthbending is still too weak to break through it."
        else:
            "You knock on the wall to the west, it seems there's a room behind it."
            "You might be able to earthbend your way throught it."

    call screen love_maze_directions

label love_unique_room14_activate:
    if current_room.west == -1  and maze_sections >= 2:

        menu:
            "break through":
                play audio "audio/rock_crumble.mp3"



                $ current_room.sp_used = True
                $ current_room.west = 47
                $ current_room.special_touch = "maze/sp_westwall_breakthrough.png"
                show expression current_room.special_touch with Dissolve(2.0)
            "let's not mess with this right now":

                "You leave it alone."
    else:
        "I'm still too weak to break through this wall."

    call screen love_maze_directions   





label love_unique_room15:


    $ sp_item_xpos = 10
    $ sp_item_ypos = 20
    $ sp_item_width = 200
    $ sp_item_height = 600



    if current_room.west == -1:
        if maze_sections >=3 and current_room.visit == 1:
            "Hot steam escapes from a crack in the ground."
            y "I think I can close it without opening up a new crack under my feet."

        elif current_room.visit == 1:
            "Hot steam escapes from a crack in the ground."
            y "There's a chance a new crack will open up right under me if I try and close it with earthbending."
            y "Let's not mess with this until I'm a more experienced earthbender."
    if maze_sections >= 3 and current_room.sp_used == False:
        y "I think I can close this now."


    call screen love_maze_directions

label love_unique_room15_activate:

    if current_room.west == -1  and maze_sections >= 3:

        menu:
            "Close the crack":
                play audio "audio/rock_crumble.mp3"
                show expression current_room.maze_bg with hpunch


                $ current_room.sp_used = True
                $ current_room.west = 64
                $ current_room.special_touch2 = "sp_no_special"
                $ current_room.special_touch = "sp_no_special"
                hide expression current_room.special_touch with Dissolve(2.0)
                hide expression current_room.special_touch2 with Dissolve(2.0)
            "let's not mess with this right now":


                "You leave it alone."
    else:
        "There's nothing I can do about this right now. I'll need to be a stronger earthbender."

    call screen love_maze_directions   



label love_unique_room16:

    $ sp_item_xpos = 560
    $ sp_item_ypos = 1
    $ sp_item_width = 195
    $ sp_item_height = 240




    if room30.sp_content == 1:
        $ room30.sp_content = 2
        "just as you want to step outside the room you hear two voices approaching."
        y "i'm just gonna hide in the shadows reeeaaal quick..."
        show expression "maze/love_guards_shadow.png":
            xpos 1000 ypos 100
            linear 1 xpos 300
        $ renpy.pause(1)
        bk3_g1 "what the- oh, balls."
        bk3_g2 "what? oh. that's not good."
        bk3_g1 "I think our androgynous kidnappee just got away."
        bk3_g1 "did we ever find out if it was a boy or a girl?"
        bk3_g2 "come on, don't call them kidnappees, you know it makes me feel guilty."
        bk3_g1 "what? we're kidnapping people, what am i supposed to call them?"
        bk3_g2 "i don't know... \"presents\"? \"surprises\"?"
        bk3_g1 "you want me to call our kidnappees \"surprises\"?"
        bk3_g1 "actually, I have noticed that there are a lot of surprises down here."
        bk3_g1 "it's practically a haunted-house. i keep getting jumped by jessica."
        bk3_g1 "i'm starting to think she does that on purpose."
        bk3_g2 "is she the one the hangs out by the door? super limber?"
        bk3_g1 "that's her."
        bk3_g2 "yeah, she does that to me, too. i'm getting ulcers."
        bk3_g2 "but, look, saying \"one of the surprises got out\" really puts a positive spin on things."
        bk3_g1 "you know, that's fair."
        bk3_g1 "but still, one of them got out."
        bk3_g1 "and you know what that means..."
        bk3_g2 "Yeah...."
        bk3_g2 "Ajala is going to fingerbang the shit out of us when she hears about this. "
        bk3_g2 "man..."
        bk3_g1 "Isn't it funny how her rewards and punishments are the same thing?"
        bk3_g1 "I wouldn't mind it so much if it wasn't done with the strength of a gorilla."
        bk3_g2 "Soooo....now what?"
        bk3_g2 "We could chase after the thing. Maybe we can catch her?"
        bk3_g1 "Did you see that girl run? There's no way we'll be able to do that."
        bk3_g2 "maybe we could blame jessica?"
        bk3_g1 "the door bitch? i could get on board that plan."
        bk3_g1 "maybe we could skip the shortstack altogether and just go kneecap jessica."
        bk3_g2 "i like it. but let's at least make an {i}attempt{/i} to catch the midget."
        bk3_g1 "alright, how's this..."
        bk3_g1 "{size=+10}Stop little boy! er...girl! We have free candy!{/size=+10}"
        "A very faint sound of someone screaming \"fuck you, skanks!\" can be heard in the distance. "
        bk3_g2 "Nice try."
        bk3_g1 "*sigh* "
        bk3_g2 "that sounds like a sigh that needs unpacking."
        bk3_g2 "resist that temptation."
        bk3_g1 "these masks are so uncomfortable. I can't see shit."
        bk3_g1 "Ajala has some really odd tastes. "
        bk3_g2 "Just make sure she never hears you say that."
        bk3_g1 "trust me, i know."
        bk3_g1 "nothing like a corporate-sponsored finger up the booty to keep order."
        bk3_g2 "so, what now?"
        bk3_g1 "uh.... jessica?"
        bk3_g2 "jessica."
        show expression "maze/love_guards_shadow.png":
            xpos 300 ypos 100
            linear 1 ypos 850 xzoom 1.5 yzoom 1.5
        $ renpy.pause(1)

        hide expression "maze/love_guards_shadow.png"
        y "I'm certain Smellerbee can get away from those two slowpokes."
        y "...and fuck jessica."


    call screen love_maze_directions

label love_unique_room16_activate:

    if current_room.sp_content == 0:
        $ current_room.sp_content = 1
        y "huh."
        y "There's a small piece of paper stuck to this doorpost."
        show text "Warning!\n\n Don't open this door!\n We haven't gotten word back on whether \n this one will receive hypno sessions or not! \n Subject is female, but lacking in feminine traits. \n\n\n Ajala":
            ypos 350
        $ renpy.pause()
        y "interesting...."

    if room16.north == -1:


        $ current_room.special_touch = "maze/love_door1_open.png"
        $ current_room.north = 30
        $ current_room.visit -= 1
        jump love_bk3_maze_start

    elif room16.north != -1:

        $ current_room.special_touch = "maze/love_door1_closed.png"
        $ current_room.north = -1
        $ current_room.visit -= 1
        jump love_bk3_maze_start








label love_unique_room20:


    $ sp_item_xpos = 670
    $ sp_item_ypos = 275
    $ sp_item_width = 315
    $ sp_item_height = 435

    if current_room.sp_content < 10:
        show tojl tojl01

    if current_room.sp_content == 0 and current_room.visit == 1:
        ju "Hey! You!"
    elif (current_room.visit%2==0) and current_room.sp_content == 0:
        ju "Stop ignoring me, you asshole!"


    call screen love_maze_directions

label love_unique_room20_activate:

    show expression "maze/maze_ns_2.jpg":
        xzoom 2 yzoom 1.5 xpos -1000 ypos -300
    hide tojl
    show tojl tojl02


    if current_room.sp_content == 0:
        $ current_room.sp_content = 1
        ju "You don't look anything like the bitches who imprisoned me here..."
        ju "Who are y-"
        "you see her glance at your tattoos."
        ju "...uhh, never mind..."
        ju "Get me out of here!"
        y "Do I know you?"
        ju "Let's go with no."
        y "This isn't some sort of kinky sexplay you do for the kicks you get out of it?"
        ju "fuck no!"
        ju "Someone knocked me unconscious and chained me up in this thing."
        y "How does this open? I don't see a keyhole."
        ju "There's a combination lock on the side."
        ju "the right combination should open it."
        ju "But there's a problem."
        y "you don't have the combination?"
        ju "Yep."
        y "this is starting to sound like a lot of work."

        ju "I'd offer you money but I'm kinda without any at the moment..."
        ju "...but I'll let you cum on my face and in my mouth after you free me."
        ju "Agreed?"
        y "Girl...you just found the key to my heart..."
        menu:
            "But I want to do it now!":

                y "Call it an investment in the future."
                ju "...fine... it's not like I have much of a choice."
                show tojl tojl04
                call june_headlock_scene from _call_june_headlock_scene
            "Agreed, payment after the job is done":

                $ current_room.sp_content = 2
                $ june_sympathy += 1
                y "Pretty lady, you have a deal!"

        hide expression "maze/maze_ns_2.jpg"
        jump love_unique_room20


    menu:
        "come here often?":
            ju "Can you just get me out of here?"
            y "Still working on it."
            jump love_unique_room20_activate
        "unlock her":




            jump start_headlock
        "exit":

            hide expression "maze/maze_ns_2.jpg"
            jump love_unique_room20


    label start_headlock:

        $ headbar_1 = 640
        $ headbar_1_add = 0

        $ headbar_2 = 640
        $ headbar_2_add = 0

        $ headbar_3 = 640
        $ headbar_3_add = 0

        image bk3_numberbar = "bk3/june/headlock/headlock_numberbar.png"

    label start_headlock_1:


        if headbar_1 <= 190:
            $ headbar_1 = 690
        if headbar_2 <= 190:
            $ headbar_2 = 690
        if headbar_3 <= 190:
            $ headbar_3 = 690

        show bk3_numberbar at Move((headbar_1, 275), (headbar_1 - headbar_1_add, 275), 1.0)
        show bk3_numberbar as bk3_numberbar_2 at Move((headbar_2, 340), (headbar_2 - headbar_2_add, 340), 1.0)
        show bk3_numberbar as bk3_numberbar_3 at Move((headbar_3, 405), (headbar_3 - headbar_3_add, 405), 1.0)

        $ headbar_1 -= headbar_1_add
        $ headbar_2 -= headbar_2_add
        $ headbar_3 -= headbar_3_add

        $ headbar_1_add = 0
        $ headbar_2_add = 0
        $ headbar_3_add = 0

        show expression "bk3/june/headlock/headlock_mechanism.png"


        if headbar_1 == 390 and headbar_2 == 440 and headbar_3 == 540:

            "The cylinder unlocks and june is freed."
            hide expression "bk3/june/headlock/headlock_mechanism.png"
            hide bk3_numberbar
            hide bk3_numberbar_2
            hide bk3_numberbar_3

            $ june_freed = True
            $ june_headlock = False
            show tojl tojl03
            ju "Thanks! I'm getting the fuck out of here!"

            $ current_room.special_touch2 = "bk3/june/headlock/headlock.png"
            if current_room.sp_content == 2:
                y "Aren't you forgetting something?"
                ju "Fine... A deal's a deal."
                show tojl tojl05
                call june_headlock_scene from _call_june_headlock_scene_1
                ju "See ya later. I'm out of here!"
            $ current_room.sp_content = 10
            $ current_room.sp_used = True
            jump love_bk3_maze_start

        call screen headlock_buttons

        screen headlock_buttons:
            imagemap:

                ground "bk3/june/headlock/transparent_fullscreen.png"



                textbutton "I give up" xpos 800 ypos 300 action Jump("end_headlock_1")
                textbutton "reset" xpos 800 ypos 350 action Jump("start_headlock")
                hotspot (692, 275, 59, 62) action [SetVariable("headbar_1_add", 50), Jump("start_headlock_1")]
                hotspot (692, 345, 60, 60) action [SetVariable("headbar_2_add", 50), Jump("start_headlock_1")]
                hotspot (691, 410, 62, 58) action [SetVariable("headbar_3_add", 50), Jump("start_headlock_1")]

        label end_headlock_1:
            hide expression "maze/maze_ns_2.jpg"
            hide expression "bk3/june/headlock/headlock_mechanism.png"
            hide bk3_numberbar
            hide bk3_numberbar_2
            hide bk3_numberbar_3
            jump love_unique_room20_activate



    call screen love_maze_directions 



label love_unique_room22:

    $ sp_item_xpos = 727
    $ sp_item_ypos = 181
    $ sp_item_width = 85
    $ sp_item_height = 50

    call screen love_maze_directions

label love_unique_room22_activate:

    if current_room.sp_content == 0:
        $ current_room.sp_content = 1
        "You hear the sound of someone humming a song coming from the grate."
        y "Hmmm, nothing there... looks like sound travels far in these tunnels."


    call screen love_maze_directions  





label love_unique_room25:


    $ sp_item_xpos = 340
    $ sp_item_ypos = 1
    $ sp_item_width = 340
    $ sp_item_height = 260

    if current_room.sp_content == 1:
        show expression "maze/love_secretdoor.png"

    if love_bk3_map:
        if not bk3_jd_dungeon:
            y "there's something suspicious about this wall..."
        $ bk3_jd_dungeon = True










    if bk3_jd_dungeon == True:
        $ current_room.sp_item = True
    else:
        $ current_room.sp_item = False


    call screen love_maze_directions

label love_unique_room25_activate:
    if current_room.sp_item == True and current_room.sp_content == 0:
        "You press a specific stone in the wall and feel something moving."
        play sound "audio/stonegrind.mp3"
        show expression "maze/love_secretdoor.png" with Dissolve(1.5)
        $ current_room.sp_content = 1
        $ current_room.north = 76

    elif current_room.sp_item == True and current_room.sp_content == 1:
        "The door is closing!"
        play sound "audio/stonegrind.mp3"
        hide expression "maze/love_secretdoor.png" with Dissolve(1.5)
        $ current_room.sp_content = 0
        $ current_room.north = -1



    call screen love_maze_directions       






label love_unique_room28:

    $ sp_item_xpos = 755
    $ sp_item_ypos = 4
    $ sp_item_width = 244
    $ sp_item_height = 410

    if current_room.sp_content == 1:
        $ current_room.maze_enemy = True
        $ current_room.sp_content = 0


    if current_room.maze_enemy == True:
        show expression "maze/love_scroll_girl.png"
        if current_room.visit == 1:
            "You see a woman reading a scroll hanging from the wall, oblivious to the world around her."


    call screen love_maze_directions

label love_unique_room28_activate:




    if current_room.maze_enemy == True:
        "Leave me alone! I'm trying to memorize this number before they take it down!"
        menu:
            "leave her alone":
                call screen love_maze_directions
            "pester the girl":


                y " Maybe I can help by calling out random numbers. 7, 1, 4, 3, 4..."
                "I'll make you pay for that!"
                hide expression "maze/love_scroll_girl.png"
                jump love_maze_enemies

            "Divert her attention" if room30.sp_content == 2:

                y "Hey! A prisoner escaped and they need your help catching her!"
                "Oh shit! Thanks for telling me! "
                hide expression "maze/love_scroll_girl.png" with dissolve
                y "I'm sure that won't endanger Smellerbee... "
                y "...probably?"
                y "......"
                y "eh, she seems scrappy."
                $ current_room.maze_enemy = False
                $ current_room.sp_content = 1
                call screen love_maze_directions
    else:



        show expression "maze/love_scroll_big.png"
        $ renpy.pause()
        $ current_room.visit -= 1
        hide expression "maze/love_scroll_big.png"
        call screen love_maze_directions



    call screen love_maze_directions



label love_unique_room30:
    $ sp_item_xpos = 109
    $ sp_item_ypos = 355
    $ sp_item_width = 155
    $ sp_item_height = 195


    if current_room.sp_content == 0:
        show expression "maze/love_smellerbee_shadow.png"
        "*SNOOOOORREEE!!*"

    if current_room.visit == 1:
        "You see a small shadow lying on a heap of straw in an otherwise barren, dark room."




    call screen love_maze_directions

label love_unique_room30_activate:

    if current_room.sp_content == 0:
        $ current_room.sp_content = 1
        "*scratch* *scratch*"
        "*SNOOOOORREEE!!*"
        y "Hey!"
        y "....thing!"
        y "Wake up!"
        mv "Huhh... wha...?"
        mv "lay off, you skanks!"
        mv "Haven't you groped me enough yet!?"
        y "uh, firstly: i want to hear more about that."
        y "and secondly, but more importantly: Calm your tits."
        y "I'm not part of whatever is going on down here."
        hide expression "maze/love_smellerbee_shadow.png" with None

        show expression "maze/love_smellerbee.png":
            ypos 320
            linear 2.5 ypos 0
        with Dissolve(2.0)
        y "........."
        y "never mind about the tits."
        y "i see you have those well under control."
        sb "Hey, it's you!"
        sb "Are you breaking me out of this place!?"
        y "Oh hi... you..."
        sb "you don't remember me?"
        y "no, no, i... i totally do."
        y "It's just... kinda dark in here, so... you know, help a guy out?"
        sb "It's me! Smellerbee!"
        sb "I was looking for Jet."
        sb "He disappeared, and all of a sudden these weirdos here kidnapped me!"
        y "Yeah, they've been abducting people and hypnotizing them down here."
        sb "Why would they do that?"
        y "Oh, you know, to turn the victims into their mindless puppets and sex slaves."
        y "the usual."
        sb "That's horrible!"
        sb "Do you think they've got Jet down here somewhere?"
        y "No idea, but so far I've only seen them kidnap women."
        sb "Hmm, if you're already searching this place, it might be better for me to keeping looking for him in basingse."
        sb "Thanks Aang, I owe you big time."
        sb "I'm sure we'll meet again."
        sb "See ya!"
        hide expression "maze/love_smellerbee.png" with dissolve
        y "...huh."
        y "I can understand that part in the note about her lacking feminine traits.... "
        show expression "maze/love_smellerbee.png" with hpunch
        ya "AAAaaah!!"
        y "fuck."
        y "don't... do that."
        y "everyone keeps appearing suddenly."
        y "it keeps happening down here, and i am not a fan."
        y "just gradually come into view like a normal person, damn."

        sb "Sorry to bother you but... could you lend me some money?"
        sb "i don't wanna ask, but I think these skanks took my money while I was asleep."
        y "How much did they steal?"
        sb "37 coins, but 10 coins should be enough to get me through the day."
        menu:
            "give 10" if emoney >= 10:
                $ emoney -= 10
                y "Sure, here you go."
                sb "hey, thanks!"
            "give 50" if emoney >= 50:
                $ emoney -= 50
                y "Here, take 50 instead."
                $ smellerbee_sympathy +=1
                sb "wow!"
                sb "thanks, mister!"
            "Sorry, I don't have enough":
                y "Ask me again later. I'm pretty much broke myself, currently."
                sb "Ah damn. No worries, I'll figure something out."
        hide expression "maze/love_smellerbee.png" with dissolve
        y "........"
        y "Is... is she gone?"
        y "this place is giving me Chihuahua-level anxiety."
        call screen love_maze_directions

    if current_room.sp_content >= 1:

        "You search the straw and find 37 coins!"
        $ current_room.sp_item = False
        $ emoney += 37



    call screen love_maze_directions






label love_unique_room32:
    if room32.sp_content == 0:
        $ room32.sp_content = 1
        "just as you're about to turn the corner, you hear footsteps approach."

        bk3_g1 "Shit... are you still sore, too?"
        bk3_g2 "am i still-?"
        bk3_g2 "yes, i'm still fucking sore!"
        bk3_g2 "i can't walk a straight fucking line after the punishment ajala gave me..."
        bk3_g1 "Yeah... fingers like sausages, i'm telling you."
        bk3_g2 "nah, it's not that they're thick, it's that she puts her whole damn arm into-"

        show expression "maze/love_guards_shadow.png":
            xpos -200 ypos -20
            linear 1 xpos 300 ypos 50
        $ renpy.pause(1)
        bk3_g2 "WAAAH!!!" with hpunch
        bk3_g2 "Damn, you scared the shit out of me, bro!"
        bk3_g2 "Didn't expect anyone else to be here."
        bk3_g1 "Oh... fuck... This is bad."
        bk3_g2 "Why? It's an intruder, we've had those before."
        bk3_g2 "Two against one, this'll be fun."
        bk3_g2 "We'll smack him around a bit and dump his ass in the sewers."
        bk3_g2 "Just like we did with that water tribe boy."
        bk3_g1 "Don't you see those blue tattoos?"
        bk3_g2 "Yeah, so? I got one of a molerat myself."
        bk3_g1 "no, he's-"
        bk3_g1 "wait, you do?"
        bk3_g1 "you never told me that!"
        bk3_g2 "It never seemed like a good moment to tell you."
        bk3_g2 "also, this is a workplace environment, and i don't think that sort of talk is appropriate."
        bk3_g1 "......."
        bk3_g1 "we were just talking about being fingerbanged!"
        bk3_g2 "yeah, from our {i}boss."
        bk3_g2 "there's a line between what's acceptable for-"
        bk3_g1 "finger! banged!"
        bk3_g2 "*sigh*"
        bk3_g2 "i don't have time to go into the specifics of h.r. policy."
        bk3_g1 "h... what?"
        bk3_g2 "human resources?"
        bk3_g1 "we have a human resources department?"
        bk3_g2 "yeah, how do you think we get paid?"
        bk3_g1 "we get paid?"
        menu:
            "sneak past the guards":
                pass
            "keep listening":

                bk3_g1 "well... can I see it, anyway?"
                bk3_g1 "Where did you have it put?"
                bk3_g2 "well, since molerats dig these long dark tunnels I'd thought it'd be funny to..."
                bk3_g1 "...no, you mean you...?"
                bk3_g2 "You think it's too trashy?"
                bk3_g1 "obviously! but who gives a shit?"
                bk3_g1 "people take vaginas too seriously."
                bk3_g2 "right? it's like... it's a hole near my butt where i pee."
                bk3_g2 "i don't even know what it looks like!"
                bk3_g1 "...you don't?"
                bk3_g1 "you've never put a mirror down there?"
                bk3_g2 "no, why would i want to?"
                bk3_g1 "well i want to see it."
                bk3_g2 "...."
                bk3_g2 "is this sexual harrassment?"
                bk3_g1 "we're just a couple of girls having fun... being stupid..."
                bk3_g1 "just stupid... like, wouldn't it be funny if i took your pants off and stuck my face-"
                bk3_g2 "damn it, krystal! with your stripper-ass name!"
                bk3_g2 "for the last time, leave me alone!"
                bk3_g2 "stop trying to get me naked!"
                bk3_g1 "you know you want-"
                "Just when things are starting to get interesting, they notice you again."
                bk3_g1 "Oh shit... the avatar is still here."
                bk3_g1 "dude... why haven't you snuck off yet?"
                bk3_g2 "The avatar? That's a little above our pay grade."
                bk3_g1 "That's what I was thinking."
                bk3_g1 "Ahum.... We'll let you go this time, avatar!"
                bk3_g1 "But when we meet again we'll..."
                bk3_g2 "....probably run away, if there's no one to rat us out."
                bk3_g1 "Let's go, before anyone else shows up and we have to make an effort for appearances."
                bk3_g2 "Right behind you."
                show expression "maze/love_guards_shadow.png":
                    linear 1 xpos 1250


    elif room36.sp_content == 7:
        $ room36.sp_content = 8
        show expression "maze/love_ajala_angry.png"
        ct "you!"
        ct "bitch!"
        y "What? me?"
        ct "yeah, i said \"bitch\", didn't i?"
        ya "i'm not the bitch! you're the bitch!"
        ct "I'm not letting you get away this time!"
        ct "I'll make sure Suki is the last girl you help escape from here."
        ct "You're ruining all my fun!"
        ct "And without that little earthbending tart, you're helpless against me."
        y "That's right, Toph! Knock her out! Just like we did before!"
        ct "What?!"
        "ajala quickly turns around, expecting to see Toph."
        "Before she realizes you're bluffing, you step in and hit her square on her jaw."
        play sound "audio/thud.mp3"
        hide expression "maze/love_ajala_angry.png" with dissolve

        "She crumples to the floor. Unconscious."
        hide expression "maze/love_ajala_angry.png"
        y "lucky shot!"
        y "i can't believe you fell for that."
        y "....what's this?"
        if obsidian <=1:
            play sound "audio/win2.mp3"
            $ obsidian +=1
            "you found {b}1{/b} obsidian!"
            y "cool, looks useful."
            y "and... what's this?"

        play sound "audio/win2.mp3"
        "you find an odd-looking device...."
        y "this is a weird lantern."
        y "why was she carrying this?"
        y "i'll worry about that later."
        y "but first...."

        menu:
            "Run away while she's still out cold!":
                $ room36.sp_content = 12
            "Lock her up":
                y "Hehehe..."
                scene black
                show text "{color=#fff}With a lot of effort, you manage to drag Ajala's limp and heavy body to the room in which you found Suki.{/color}"
                $ renpy.pause()
                $ current_room = room36
                if room35.west == -1:
                    $ room35.special_touch = "maze/sp_ns_metaldoor_open.png"
                    $ room35.west = 36
                    $ room36.east = 35
                    $ room36.special_touch = "maze/love_metaldoor_2_open.png"
                jump love_bk3_maze_start

    elif room36.sp_content == 10:
        $ room36.special_touch2 = "bk3/ajala/headlock/headlock_broken.png"
        $ room36.sp_content = 11
        if room35.west == -1:
            $ room35.special_touch = "maze/sp_ns_metaldoor_open.png"
            $ room35.west = 36
            $ room36.east = 35
            $ room36.special_touch = "maze/love_metaldoor_2_open.png"

    elif room36.sp_content == 12:
        $ room36.sp_content = 8
        show expression "maze/love_ajala_angry.png"
        ct "you again!"
        ct "I'm not letting you get away this time!"
        y "That's right, Toph! Knock her out! Just like we did before!"
        ct "What?!"
        "ajala quickly turns around, expecting to see Toph."
        "Before she realizes you're bluffing, you step in and hit her square on her jaw."
        play sound "audio/thud.mp3"
        hide expression "maze/love_ajala_angry.png" with dissolve
        "She crumples to the floor. Unconscious."
        hide expression "maze/love_ajala_angry.png"
        y "i can't believe you fell for that again."
        menu:
            "Run away while she's still out cold!":
                $ room36.sp_content = 12
            "Lock her up":
                y "Hehehe..."
                scene black
                show text "{color=#fff}With a lot of effort, you manage to drag Ajala's limp and heavy body to the room in which you found Suki.{/color}"
                $ renpy.pause()
                $ current_room = room36
                if room35.west == -1:
                    $ room35.special_touch = "maze/sp_ns_metaldoor_open.png"
                    $ room35.west = 36
                    $ room36.east = 35
                    $ room36.special_touch = "maze/love_metaldoor_2_open.png"
                jump love_bk3_maze_start

    call screen love_maze_directions





label love_unique_room35:
    $ sp_item_xpos = 292
    $ sp_item_ypos = 73
    $ sp_item_width = 141
    $ sp_item_height = 440

    if room36.sp_content == 5:
        bk3_g1 "Aaaahh!!" with hpunch
        bk3_g1 "Stop scaring me like that!!"
        bk3_g1 "And why are you not in your cell?!"
        bk3_g2 "Yeah, the door is still locked, and we have the only key!"
        y "And now you'll give it to me, or so help me, I'll fist your anuses while holding an apple."
        bk3_g1 "Yuck... apples."
        y "....really? that's your takeaway?"
        bk3_g2 "Okay, we'll give you the key... but only because we dislike wasting food like that."
        bk3_g1 "We do?"
        bk3_g1 "because i definitely saw you throwing away an entire meal yesterday because it had pieces of carrot in it."
        bk3_g2 "That was different!"
        bk3_g1 "Really tiny pieces, I wouldn't even have noticed them in there if you hadn't told me about it."
        bk3_g2 "Just trust me on this, okay?!"
        bk3_g1 "You literally needed a microscope to see them."

        "The girl with the buns throws you the key."
        bk3_g2 "Ajala is on her way here so he's not going to escape anyway."
        bk3_g2 "Let's get out of here!"
        bk3_g1 "Go-go-go!!"
        $ room36.sp_content = 6
        y "Okay, I have the key so I should be able to unlock Suki's cell door now."


    call screen love_maze_directions

label love_unique_room35_activate:
    if room36.sp_content >= 5:

        if current_room.west == -1:
            $ current_room.special_touch = "maze/sp_ns_metaldoor_open.png"
            $ current_room.west = 36
            $ room36.east = 35
            $ room36.special_touch = "maze/love_metaldoor_2_open.png"
        else:
            $ current_room.special_touch = "maze/sp_ns_metaldoor_closed.png"
            $ current_room.west = -1
            $ room36.east = -1
            $ room36.special_touch = "maze/love_metaldoor_2_closed.png"

        $ current_room.visit -= 1
        jump love_bk3_maze_start

    call screen love_maze_directions









label love_unique_room36:
    $ sp_item_xpos = 236
    $ sp_item_ypos = 186
    $ sp_item_width = 328
    $ sp_item_height = 325

    if current_room.sp_content >= 2:
        $ sp_item_xpos = 47
        $ sp_item_ypos = 154
        $ sp_item_width = 180
        $ sp_item_height = 230

    if current_room.sp_content >= 10:
        $ sp_item_xpos = 236
        $ sp_item_ypos = 186
        $ sp_item_width = 328
        $ sp_item_height = 325



    if current_room.sp_content == 8:
        $ current_room.special_touch2 = "bk3/ajala/headlock/headlock_ajala.png"
        $ current_room.sp_content = 9
        jump love_bk3_maze_start

    if current_room.sp_content == 9:
        with fade
        ct "Whu... whut happened?"
        show ctc
        pause
        hide ctc
        ct "where- what the hell?!"
        y "well... you called me a \"bitch\", and I didn't like that."
        y "so, I knocked you out... and locked your unconscious ass into this contraption."
        ct "You got lucky! I'll tear off your head when I get out of here!!"
        jump ajala_assfuck_menu

        label ajala_assfuck_menu:
            menu:
                "Fuck her in her ass":
                    y "You like putting things in people's asses right?"
                    ct "umm... no?"
                    y "liar."
                    y "I'm going to give you some of your own medicine."
                    ct "w-wait... hold on..."
                    ct "you don't have to... that's not necessary..."
                    ct "let's... let's talk about this-"
                    show expression "maze/love_ceilingview_1.jpg"
                    hide tosh
                    show tosh tosh11
                    with dissolve
                    ct "hold on!"
                    show ctc
                    pause
                    hide ctc
                    ct "don't do anything... anything stupid!"
                    ct "we can... we can work this out!"
                    y "you know... i don't think we can."
                    ct "W-what are you going to do?"
                    y "oh, that's right... you can't see what's happening back here, can you?"

                    y "I'm going to put something in your ass."
                    y "Just like you did to Suki."

                    y "but don't worry... I won't put a piece of metal in there."
                    y "I'll use something harder, thicker and longer."
                    ct "d-don't."
                    ct "i-i'm serious. don't... don't do that!"
                    y "well, i might change my mind..."
                    y "If you're a good girl."
                    ct "...what... can i do?"
                    y "i'll give you three seconds to figure it out."
                    y "three."
                    ct "w-what?"
                    y "two."
                    ct "wait!"
                    ct "i'm sorry! i'm-i'm a stupid slut!"
                    ct "and... and..."
                    y "and?"
                    show tosh tosh15 with dissolve
                    show ctc
                    pause
                    hide ctc
                    ct "and... i know i deserve a cock in my ass, but..."
                    y "ha! ass-butt."
                    ct "no... no... please, i'm... i'm just a caretaker!"
                    ct "I just take care of the tunnels!"
                    ct "please let me go!"
                    show tosh tosh17 with dissolve
                    y "you're not just a caretaker, you're the head guard, and a total cunt."
                    ct "...yes! yes, it's true!"
                    ct "i'm a total, raging cunt!"
                    ct "please! whatever you need me to say, i'll say!"
                    ct "i'm the head bitch!"
                    y "with a big, tasty ass."
                    ct "w-with a big, t-tasty ass..."
                    y "you've had cocks in it before, i bet."
                    ct "j-just toys!"
                    ct "please......"
                    y "hmm... you've begged very well..."
                    y "maybe i'll let you go."
                    ct "thank-"

                    show tosh tosh12 with Dissolve(1.5)
                    "her ass is resistant, but with a little push past her entrance..."
                    "...you slide the head of your dick in surprisingly smoothly."
                    ct "aaahhh!!"

                    show ctc
                    pause
                    hide ctc
                    y "That's right. How you like that, huh?"
                    ct "ah! hgngh..."
                    show tosh tosh12_1
                    ct "you- you asshole!"
                    y "no, let's focus on {i}your{/i} asshole."
                    ct "pull it ou-"
                    show tosh tosh101

                    ct "nnnnhhhghhh!!"
                    show ctc
                    pause
                    hide ctc
                    ct "you said you'd let me go!"
                    ct "*ah!* *mmng!* *ngh!*"
                    show tosh tosh101_1
                    ct "i'll *ungh!* kill you when *ah!* i get out!"
                    y "{i}if{/i} you get out."
                    y "besides, what about all that sexy talk you were doing?"
                    y "about your tasty ass?"
                    show tosh tosh101
                    ct "*hngh!* *ah!* *ngh...*"
                    ct "you... hgh... made me..."
                    y "we both know what you were really begging for."
                    ct "ahh... ohhn..."
                    y "starting to enjoy it, huh?"
                    ct "n-no... oh... ohhh... anhh...."
                    show ctc
                    pause
                    hide ctc
                    show tosh tosh101_1
                    ct "I can't... ngh... believe this is happening... ah... this can't really be happening..."
                    y "I bet you didn't expect to get some dick up your ass today, huh?"
                    y "Maybe getting some of what you've been dishing out will make you think twice in the future."

                    ct "f-fuck... you..."
                    show tosh tosh101
                    show ctc
                    pause
                    hide ctc
                    y "bitch, i can see your pussy... hell, i can {i}smell{/i} your pussy."
                    y "you are more turned on than anyone i've ever seen."
                    y "and i've known some sluts."

                    ct "nghg... mmm... ah.... ngh... not... not true..."
                    y "oh, damn... you're close to cumming aren't you?"
                    ct "ahh... ah... ohhh... ngh....."
                    ct "nnn.... ha.... no..."
                    y "should i stop?"
                    show tosh tosh101_1
                    ct "don't... almost... ahh..."
                    y "you gonna cream, slut?"
                    ct "ohhhhhhhh......."
                    y "are you really gonna-"
                    ct "{size=+4}uuhhhh....."
                    show tosh tosh101
                    ct "{size=+10}fuck!!!!" with vshake
                    ct "{size=+10}me!!!!" with vshake
                    show tosh tosh102

                    show ctc
                    pause
                    hide ctc
                    y "oh, fuck you got tight!"
                    ct "{size=+10}mmmmmmmnghghpph!!! ahhh!!" with vshake
                    y "hngh!"

                    ct "{size=+10}yes!!!" with vshake
                    show tosh tosh12
                    play sound "audio/splurt2.ogg"
                    with flash
                    y "fuck!"
                    ct "{size=+10}unngh!"
                    ct "{size=+10}fill it!"
                    play sound "audio/splurt1.ogg"
                    show tosh tosh14
                    with flash
                    ct "{size=+10}yes!"
                    show tosh tosh14_1
                    ct "{size=+10}do it! fill my ass!"

                    play sound "audio/splurt2.ogg"
                    show tosh tosh12
                    with flash
                    ct "ohh...."
                    hide tosh tosh12_1
                    hide expression "maze/love_ceilingview_1.jpg"
                    show tosh tosh16
                    with Dissolve(1.5)

                    ct "{size=-5}.......fuck."
                    show ctc
                    pause
                    hide ctc
                    y "....have fun?"
                    ct "don't... don't say anything."

                    ct "don't fucking talk to me right now..."
                    y "alright, but..."
                    y "I left you something nice to remember me by."
                    y "...."
                    y "It's sperm. I left my sperm in your ass."
                    ct "I'll... i'll remember this..."
                    y "While longing for more?"
                    ct "n-no...."
                    ct "......"
                    ct "..........."
                    ct ".................."
                    y "you sure?"
                    ct "....i've...."
                    ct "I've never...."
                    ct "....never been fucked like that...."
                    ct "ever...."
                    ct ".........."


                    $ ajala_headlock_fuckedinass = True
                    hide tosh
                    show expression "bk3/katara/blowjob/sperm1.png":
                        xpos -350 ypos -15
                    with dissolve
                    ct "you know...."
                    ct "i'm thinking...."
                    ct "maybe... maybe we can be..."
                    ct "enemies with benefits?"

                    menu:
                        "maybe":
                            y "....i'll think about it."
                        "sure, and i'll cum on your face to seal the deal":
                            y "i think that could be fun."
                            y "hmm... hard to shake your hand when you're in there...."
                            y "how about i cum on your face to seal the deal?"
                            ct "i... what?"
                            ct "don't... do that."
                            y "Oh, but i'm gonna."
                            "you unzip your pants and begin masturbating."
                            ct "i'm already sticky full with cum-"
                            y "*fap* *fap* *fap*"
                            ct "i don't want a sploogy face!"
                            y "*fap* *fap* *fap*"
                            ct "i swear, if you blow a disgusting load on-"
                            y "take this, slut!"
                            play sound "audio/splurt2.ogg"
                            show expression "bk3/jin/sucks/sperm_inmouth.png":
                                xpos -452 ypos -115

                            with flash
                            show ctc
                            pause
                            hide ctc
                            play sound "audio/spit.mp3"
                            ct "*pbt!*"
                            ct "you got jizz in my fucking mouth, you douchebag!"
                            ct "ugh... and it's all over my face..."
                            ct "i have a pretty fucking face! i don't want cum on it!"
                            ct "....this is fucking disgusting."
                            y "good."
                            ct "......"
                            ct "fuck, i hate you."
                            y "I hate you, too."

                    ct "you know that i'm still gonna kill you if i get the chance, right?"
                    y "and i'll still fuck you if i get the chance."
                    ct "sounds like... a rush."
                    ct "this is gonna be fun."
                    y "....you're fucked up."
                    ct "ditto, asshole."
                    ct "come back and plow my ass again sometime."
                    show ctc
                    pause
                    hide ctc
                    $ current_room.sp_content = 10
                    jump love_backtotherealworld
                "talk smack":

                    y "no, you won't, dumbass."
                    y "I managed to knock you out with the oldest trick in the book."
                    y "I guess those muscles take away the blood needed for your brain."
                    ct "This won't hold me forever!"
                    y "oh, but i'm not planning to stay here forever... just long enough."
                    ct "long enough... for what?"
                    y "Just long enough to look at that naked ass and those tits of yours."
                    y "......"
                    y "Wait a minute... "
                    y "are you... getting moist down there?"
                    ct "no!!"
                    y "Yes, you are!"
                    y "You're actually enjoying this situation, aren't you?!"
                    ct "No, it's just really damp in these underground rooms!"
                    y "Don't be ashamed, slut."
                    y "I have a few weird kinks myself."
                    y "for example... i love putting musclehead whores in their place."
                    $ current_room.sp_content = 10
                    jump ajala_assfuck_menu
                "exit":

                    $ current_room.sp_content = 10

            jump love_bk3_maze_start



    if room40.sp_content == 1 and room36.sp_content <6:
        show tosh tosh06
        y "You won't fit through the opening at the end of the tunnel, but I'll find a way to get the key and free you. That's a promise!"
        suki "I have faith in you Aang."

    if current_room.visit == 1:
        show tosh tosh02
        "A big round ass is turned towards the open door."
        y "well... hello there."
        suki "okay, who the fuck is that!?"
        y "No, no... this is the part where you say \"general kenobi!\""
        suki "Assholes! If I ever get the chance I'll kill the lot of you!!"
        y "Relax girl, I'm here to free prisoners like you."
        suki "That voice!"
        suki "...is...is that you, Aang!?"
        y "Yep. Bald head, blue tats, it's all here."
        y "Who are you?"
        suki "It's me! Suki!"
        suki "I'm so glad you're here!"
        suki "Are you alone?"
        suki "Where's Katara, Toph and Sokka?"
        y "It's just me right now."
        y "...enjoying the view."
        suki "well... this is an embarassing way to reconnect."
        suki "Could you come and stand where I can see you? "
        y "I'm kinda enjoying this angle."
        suki "....."
        y "....okay, fine."
        show tosh tosh01 with Dissolve(1.5)
        suki "thanks, that's... better?"
        suki "Please get me out of here quickly, Aang."
        suki "There's some really twisted people guarding this place."
        y "I've come across a few of them already."
        y "So how did you end up here?"
        suki "I was attacked by some fire nation bitches and afterwards woke up here."
        suki "But let's save the stories for later."
        suki "We need to leave this place!"
        y "Sure, but I don't have the key to this contraption."
        y "Any ideas where I can find it?"
        suki "It's in the back."
        "You walk around suki and start searching the room."

        show tosh tosh02 with Dissolve(1.5)
        y "I'm not seeing it."
        suki "It's... ehm... it's {i}in{/i} the back."
        y "....seriously....?"
        suki "It's not like I put it there!"
        suki "it's this crazy headguard."
        y "Ajala?"
        suki "Who knows. she's buff and considers all of this place her own little kingdom."
        suki "She... enjoys torturing her captives in sick ways and..."
        suki "...she inserted the key in... my ass. "
        y "sounds like my kinda woman, honestly."
        suki "would you just-!"
        suki "...I know this is weird, Aang, but please...."
        suki "I can't believe I'm asking this..."
        suki "Please stick you finger in my bum and get the key so we can get out of here."
        y "Can't you just... go number two?"
        suki "They haven't fed me since I got here and that would take far too long, anyway."
        menu:
            "Fine, but I have to do something else first":
                suki "seriously!?"
                suki "come on!"
                show tosh tosh01 with Dissolve(1.5)
            "Start the cavity search":
                $ current_room.visit += 1
                jump suki_headlock_removal
    if current_room.sp_content == 2:
        $ current_room.east = -1
        $ current_room.special_touch = "maze/love_metaldoor_2_closed.png"
        $ room35.special_touch = "maze/sp_ns_metaldoor_closed.png"
        show expression "maze/love_metaldoor_2_open.png"

        show tosh tosh05

        suki "Oh, man... you can't believe how good it feels to be able and stand up straight!"
        y "Gotta be honest, something of mine is standing up straight, too."
        suki "About that... let's not tell anyone else what happened here... in detail."
        suki "okay?"
        hide tosh
        hide expression "maze/love_metaldoor_2_open.png"
        show expression "maze/love_metaldoor_2_closed.png"
        play sound "audio/thud.mp3"
        show tosh tosh05
        "*BANG!*" with hpunch
        $ room35.west = -1
        $ room40.sp_item = True

        y "uh... shit."
        y "...."
        y "well, that's not what you want."
        suki "What happened?!"
        y "Someone threw the door shut."
        show tosh tosh06:
            xzoom -1
        with Dissolve(1.5)

        bk3_g2_bars "That's right!!"
        bk3_g2_bars "We were waiting for a chance to lock you up in here!"
        bk3_g1_bars "It was a trap all along, dumbass!!"
        bk3_g1_bars "Hahaha!"
        y "as long as i'm in here and your breath is out there."
        bk3_g1_bars "....."
        bk3_g1_bars "i'm gonna kick your ass!"
        y "come in here and try it."
        bk3_g2_bars "come on, don't fall for that, krystal."
        bk3_g2_bars "he's just trying to rile you up."
        bk3_g1_bars "you're right, my breath's not that bad."
        bk3_g2_bars ".........."
        bk3_g1_bars "....is my breath bad?"
        bk3_g2_bars "i mean... maybe don't eat chimichangas for lunch every day..."
        bk3_g1_bars "...are you serious right now?"
        bk3_g2_bars "it's just... it's a lot of garlic! i'm sorry!"
        bk3_g1_bars "....am i the reason we have to wear these masks?"
        bk3_g2_bars "............"
        bk3_g1_bars "are you serious?!?"
        bk3_g1_bars "i'm gonna kill you, avatar!"
        bk3_g2_bars "it's not that bad, really. we're all used to it."

        bk3_g1_bars "i can't help it, they're just so affordable!"
        bk3_g2_bars "i know, i know."
        y "I feel like I should've seen this coming."
        bk3_g1_bars "you know, avatar..."
        bk3_g1_bars "we could've locked you in here earlier, but...."
        bk3_g2_bars "...but that ass finger action was looking kinda hot and we didn't want to interrupt it."
        bk3_g1_bars "And now we're going to get Ajala while you're trapped in here!"
        bk3_g1_bars "High five!"
        play sound "audio/slap.mp3"
        bk3_g2_bars "High five!"
        "You hear the two guards laughing as they walk away."
        show tosh tosh06:
            xzoom 1
        y "those two need to 69 and get it over with."
        suki "well... now what?"
        suki "can you earthbend us out of here?"
        y "These walls are too thick to take down with my level of training."
        suki "So, we're fucked?"
        y "I mean, if you need it, I can probably-"
        suki "i {i}meant{/i}, are we in real trouble?"
        y "oh, yeah... right. i was kidding?"
        suki "...."
        y "...yeah, looks like we're screwed."
        show tosh tosh06:
            xzoom -1
        bk3_g1_bars "Hey!!" with hpunch
        y "Aahh!"
        y "What the hell do you want?"
        y "Weren't you going to get Ajala?"
        bk3_g1_bars "Yeah, i just came back to tell you that fingerbanging was seriously hot..."
        bk3_g1_bars "and I'm going to ask Ajala to make you guys do that again."
        bk3_g1_bars "To each other... at the same time."
        bk3_g1_bars "I'm getting wet just imagining it."
        bk3_g1_bars "Well, Gotta go!"
        show tosh tosh06:
            xzoom 1
        with Dissolve(1.5)
        suki "Fucking bitch."
        y "we have to get out of here, no matter what."
        suki "Maybe we can find a weak spot in the walls somewhere."
        "Both of you start to closely examine the walls of the cell."

        hide tosh with Dissolve(1.5)
    if current_room.sp_content == 4:

        $ room35.west = -1

        $ room35.special_touch = "maze/sp_ns_metaldoor_closed.png"
        $ current_room.sp_content = 5

        $ current_room = room40

        jump love_bk3_maze_start
    if current_room.sp_content == 6:
        show tosh tosh06
        y "Okay, time to get out of here, suki!"
        y "Make a right and keep following the tunnel in a straight line."
        y "That'll get you to the exit. "
        y "There's a small village close by where you'll find Katara."
        suki "What about you?"
        y "I'll be following, but the most important thing is for you to get out of here."
        suki "Thanks, Aang!"
        "She gives you a little peck on the cheek as she dashes out of the cell."
        hide tosh with Dissolve(1.5)
        y "Fingerbanging a girl before even getting the first kiss on the cheek."
        y "Now that's what I call the proper order of things. "
        $ suki_freed = True
        $ current_room.sp_content = 7

    call screen love_maze_directions

label suki_headlock_removal:
    $ suki_headlocking = True
    hide tosh
    show expression "bk3/suki/headlock/ani_torso.png"
    show tosh tosh03
    with Dissolve(1.5)
    show ctc
    pause
    hide ctc
    y "Okay... so how should I go about it?"
    y "Lick it first to loosen you up?"
    suki "What?! NO!"
    suki "I couldn't ever face you again!"
    y "Well, in that case, just try to relax."
    y "I don't have any lubricant with me, and I'm guessing you don't want me to cum on your ass to help glide it in?"
    suki "....are you seriously asking me whether you should cum on my ass?"
    y "hey, i'm just trying to be a friend."
    suki "Just... just go in dry."
    show tosh tosh04 with dissolve
    y "alright, but you asked for it."
    y "I'll do my best, but this won't be a fun experience {size=9}....for you....{/size}"
    y "Just imagine this is a prostate exam."
    suki "Isn't that a guy thing?"
    y "{i}worldstar!!!"
    show tosh tosh100
    suki "ah!"
    show ctc
    pause
    hide ctc
    "suki squeezes your finger tightly; it's clear that her rear has never been penetrated before."
    y "you gotta relax a little, suki... it's like i'm wearing a ring, here."
    suki "Hnngh... you're going in so deep..."
    y "Just trying to get that key."
    show ctc
    pause
    hide ctc
    suki "What's taking so long?"
    y "I'm trying my best, but you're somehow both too tight and too slippery."
    y "it would certainly help if you'd stop squirming."
    suki "Sorry, it's just that... having a friend digging in my ass is... awkward."
    y "speaking of awkward... if you see me with a raging boner, that's totally a normal physical reaction to this situation."
    show ctc
    pause
    hide ctc
    y "Wait, I think I felt something just now!"
    show tosh tosh04
    play sound "audio/win2.mp3"
    show expression "maze/prisonkey.png" with Dissolve (1.5)
    "you found the key!"
    y "damn girl... what else can that ass do?"
    suki "let's find that out later."
    y "....i like you."
    hide expression "maze/prisonkey.png" with dissolve
    hide tosh
    hide expression "bk3/suki/headlock/ani_torso.png"
    with dissolve
    suki "all right! Open the lock! Quickly!"

    $ current_room.sp_content = 1


    jump love_bk3_maze_start

label love_unique_room36_activate:

    if current_room.sp_content < 1:

        suki "Finally! Can you please get the key so we can leave this place?"
        menu:
            "Almost":
                suki "Please hurry!"
                call screen love_maze_directions
            "Yep, let's get crackin.":
                jump suki_headlock_removal

    elif current_room.sp_content == 1:
        $ current_room.special_touch2 = "bk3/suki/headlock/headlock.png"
        $ current_room.sp_content = 2
        $ current_room.special_touch = "sp_no_special"

        jump love_bk3_maze_start

    elif current_room.sp_content == 2:

        y "mmmmh, what's this?"
        y "This looks promising."
        y "I think this stone can be moved..."
        "You manage to push the heavy stone away."
        "Behind it lies a very dark and narrow corridor."
        play sound "audio/earthquake.mp3"
        $ current_room.special_touch2 = "bk3/suki/headlock/headlock_secret.png"
        $ current_room.sp_content = 3
        jump love_bk3_maze_start
    elif current_room.sp_content == 3:
        if room40.sp_content == 0:
            y "Hmmm... it's very cramped."
            show tosh tosh06
            suki "Beats hanging around here."
            y "yeah, but... there's no need for us both risk getting stuck."
            y "I'll check it out first."
            y "I'll come back and let you out... if this doesn't turn out to be a dead end."
            suki "Good luck!"

        scene black
        "you work your way through the small dark tunnel and..."
        $ generic_counter = 0
        if room40.sp_content != 0:
            $ generic_counter = 4
        while generic_counter < 4:
            "You come across a split."
            menu:
                "take a right":
                    if generic_counter == 2:
                        "You can feel a small draft. You must be going the right way."
                "take a left":
                    if generic_counter == 3:
                        "You see light!!"
                        show expression current_room.maze_bg
                        show expression current_room.special_touch
                        show expression current_room.special_touch2
                        show tosh tosh06
                        suki "Did you find a way out of here?!"
                        y "Sorry, false alarm, I must have taken a wrong turn somewhere and ended up here again."
                        suki "Please hurry up, Aang!"
                        y "Let's try this again."
                        scene black
                        $ generic_counter = -1
            $ generic_counter += 1
            "You crawl along further and ..."
        $ current_room.sp_content = 4
        if room40.sp_content == 0:
            "You see a dim light."
            y "Feels like a loose stone..."
            y "Gotta push it..."
            y "....nnnngg."
            $ suki_headlocking = False
        else:
            "you easily find your way this time."
        $ current_room = room40
        $ room40.special_touch2 =  "maze/love_loosestone_cover.png"
        jump love_bk3_maze_start
    elif current_room.sp_content == 7:
        $ current_room = room40
        jump love_bk3_maze_start

    elif current_room.sp_content == 10:
        menu:
            "Ride her ass":
                y "You like putting things in people's asses right?"
                ct "umm... no?"
                y "liar."
                y "I'm going to give you some of your own medicine."
                ct "w-wait... hold on..."
                ct "you don't have to... that's not necessary..."
                ct "let's... let's talk about this-"
                show expression "maze/love_ceilingview_1.jpg"
                hide tosh
                show tosh tosh11
                with dissolve
                ct "hold on!"
                show ctc
                pause
                hide ctc
                ct "don't do anything... anything stupid!"
                ct "we can... we can work this out!"
                y "you know... i don't think we can."
                ct "W-what are you going to do?"
                y "oh, that's right... you can't see what's happening back here, can you?"

                y "I'm going to put something in your ass."
                y "Just like you did to Suki."

                y "but don't worry... I won't put a piece of metal in there."
                y "I'll use something harder, thicker and longer."
                ct "d-don't."
                ct "i-i'm serious. don't... don't do that!"
                y "well, i might change my mind..."
                y "If you're a good girl."
                ct "...what... can i do?"
                y "i'll give you three seconds to figure it out."
                y "three."
                ct "w-what?"
                y "two."
                ct "wait!"
                ct "i'm sorry! i'm-i'm a stupid slut!"
                ct "and... and..."
                y "and?"
                show tosh tosh15 with dissolve
                show ctc
                pause
                hide ctc
                ct "and... i know i deserve a cock in my ass, but..."
                y "ha! ass-butt."
                ct "no... no... please, i'm... i'm just a caretaker!"
                ct "I just take care of the tunnels!"
                ct "please let me go!"
                show tosh tosh17 with dissolve
                y "you're not just a caretaker, you're the head guard, and a total cunt."
                ct "...yes! yes, it's true!"
                ct "i'm a total, raging cunt!"
                ct "please! whatever you need me to say, i'll say!"
                ct "i'm the head bitch!"
                y "with a big, tasty ass."
                ct "w-with a big, t-tasty ass..."
                y "you've had cocks in it before, i bet."
                ct "j-just toys!"
                ct "please......"
                y "hmm... you've begged very well..."
                y "maybe i'll let you go."
                ct "thank-"

                show tosh tosh12 with Dissolve(1.5)
                "her ass is resistant, but with a little push past her entrance..."
                "...you slide the head of your dick in surprisingly smoothly."
                ct "aaahhh!!"

                show ctc
                pause
                hide ctc
                y "That's right. How you like that, huh?"
                ct "ah! hgngh..."
                show tosh tosh12_1
                ct "you- you asshole!"
                y "no, let's focus on {i}your{/i} asshole."
                ct "pull it ou-"
                show tosh tosh101

                ct "nnnnhhhghhh!!"
                show ctc
                pause
                hide ctc
                ct "you said you'd let me go!"
                ct "*ah!* *mmng!* *ngh!*"
                show tosh tosh101_1
                ct "i'll *ungh!* kill you when *ah!* i get out!"
                y "{i}if{/i} you get out."
                y "besides, what about all that sexy talk you were doing?"
                y "about your tasty ass?"
                show tosh tosh101
                ct "*hngh!* *ah!* *ngh...*"
                ct "you... hgh... made me..."
                y "we both know what you were really begging for."
                ct "ahh... ohhn..."
                y "starting to enjoy it, huh?"
                ct "n-no... oh... ohhh... anhh...."
                show ctc
                pause
                hide ctc
                show tosh tosh101_1
                ct "I can't... ngh... believe this is happening... ah... this can't really be happening..."
                y "I bet you didn't expect to get some dick up your ass today, huh?"
                y "Maybe getting some of what you've been dishing out will make you think twice in the future."

                ct "f-fuck... you..."
                show tosh tosh101
                show ctc
                pause
                hide ctc
                y "bitch, i can see your pussy... hell, i can {i}smell{/i} your pussy."
                y "you are more turned on than anyone i've ever seen."
                y "and i've known some sluts."

                ct "nghg... mmm... ah.... ngh... not... not true..."
                y "oh, damn... you're close to cumming aren't you?"
                ct "ahh... ah... ohhh... ngh....."
                ct "nnn.... ha.... no..."
                y "should i stop?"
                show tosh tosh101_1
                ct "don't... almost... ahh..."
                y "you gonna cream, slut?"
                ct "ohhhhhhhh......."
                y "are you really gonna-"
                ct "{size=+4}uuhhhh....."
                show tosh tosh101
                ct "{size=+10}fuck!!!!" with vshake
                ct "{size=+10}me!!!!" with vshake
                show tosh tosh102

                show ctc
                pause
                hide ctc
                y "oh, fuck you got tight!"
                ct "{size=+10}mmmmmmmnghghpph!!! ahhh!!" with vshake
                y "hngh!"

                ct "{size=+10}yes!!!" with vshake
                show tosh tosh12
                play sound "audio/splurt2.ogg"
                with flash
                y "fuck!"
                ct "{size=+10}unngh!"
                ct "{size=+10}fill it!"
                play sound "audio/splurt1.ogg"
                show tosh tosh14
                with flash
                ct "{size=+10}yes!"
                show tosh tosh14_1
                ct "{size=+10}do it! fill my ass!"

                play sound "audio/splurt2.ogg"
                show tosh tosh12
                with flash
                ct "ohh...."
                hide tosh tosh12_1
                hide expression "maze/love_ceilingview_1.jpg"
                show tosh tosh16
                with Dissolve(1.5)

                ct "{size=-5}.......fuck."
                show ctc
                pause
                hide ctc
                y "....have fun?"
                ct "don't... don't say anything."

                ct "don't fucking talk to me right now..."
                y "alright, but..."
                y "I left you something nice to remember me by."
                y "...."
                y "It's sperm. I left my sperm in your ass."
                ct "I'll... i'll remember this..."
                y "While longing for more?"
                ct "n-no...."
                ct "......"
                ct "..........."
                ct ".................."
                y "you sure?"
                ct "....i've...."
                ct "I've never...."
                ct "....never been fucked like that...."
                ct "ever...."
                ct ".........."


                $ ajala_headlock_fuckedinass = True
                hide tosh
                show expression "bk3/katara/blowjob/sperm1.png":
                    xpos -350 ypos -15
                with dissolve
                ct "you know...."
                ct "i'm thinking...."
                ct "maybe... maybe we can be..."
                ct "enemies with benefits?"

                menu:
                    "maybe":
                        y "....i'll think about it."
                    "sure, and i'll cum on your face to seal the deal":
                        y "i think that could be fun."
                        y "hmm... hard to shake your hand when you're in there...."
                        y "how about i cum on your face to seal the deal?"
                        ct "i... what?"
                        ct "don't... do that."
                        y "Oh, but i'm gonna."
                        "you unzip your pants and begin masturbating."
                        ct "i'm already sticky full with cum-"
                        y "*fap* *fap* *fap*"
                        ct "i don't want a sploogy face!"
                        y "*fap* *fap* *fap*"
                        ct "i swear, if you blow a disgusting load on-"
                        y "take this, slut!"
                        play sound "audio/splurt2.ogg"
                        show expression "bk3/jin/sucks/sperm_inmouth.png":
                            xpos -452 ypos -115

                        with flash
                        show ctc
                        pause
                        hide ctc
                        play sound "audio/spit.mp3"
                        ct "*pbt!*"
                        ct "you got jizz in my fucking mouth, you douchebag!"
                        ct "ugh... and it's all over my face..."
                        ct "i have a pretty fucking face! i don't want cum on it!"
                        ct "....this is fucking disgusting."
                        y "good."
                        ct "......"
                        ct "fuck, i hate you."
                        y "I hate you, too."

                ct "you know that i'm still gonna kill you if i get the chance, right?"
                y "and i'll still fuck you if i get the chance."
                ct "sounds like... a rush."
                ct "this is gonna be fun."
                y "....you're fucked up."
                ct "ditto, asshole."
                ct "come back and plow my ass again sometime."
                show ctc
                pause
                hide ctc
                $ current_room.sp_content = 10
                jump love_backtotherealworld
            "exit":
                pass
    elif current_room.sp_content == 11:
        y "looks like ajala managed to free herself."


    elif current_room.sp_content >= 12:
        y "Nothing to do here."



    call screen love_maze_directions  



label love_unique_room38:
    $ sp_item_xpos = 333
    $ sp_item_ypos = 127
    $ sp_item_width = 350
    $ sp_item_height = 380


    if bk3_room38_guardsex == True:
        $ current_room.sp_item = True
    else:
        $ current_room.sp_item = False

    if current_room.sp_content in [1,2] and current_room.sp_item == True:

        show expression "maze/love_nudeguards.png"


    call screen love_maze_directions 


label love_unique_room38_activate:

    if current_room.sp_content < 1:
        call screen love_maze_directions 



    if current_room.sp_content == 2:
        menu:
            "I wanna see you do each other":


                if totq_fucked_with == 'realdick':
                    bk3_g1_b "Okay, Let me prepare."
                    hide expression "maze/love_nudeguards.png"
                    show totq totq54 with Dissolve(1.0)

                    bk3_g1_b "A few drops from this bottle and...."
                    show totq totq55 with Dissolve(0.7)
                    show totq totq56 with Dissolve(0.7)
                    show totq totq57 with Dissolve(0.7)
                    show totq totq58 with Dissolve(0.7)
                    bk3_g1_b "Presto!"
                else:


                    bk3_g1_b "Nice! Let me get ready."
                    hide expression "maze/love_nudeguards.png"
                    show totq totq50 with Dissolve(1.0)

                    bk3_g1_b "We take this big floppy pink dildo."
                    show totq totq51
                    bk3_g1_b "Hnnnng... push it in..."
                    show totq totq52 with Dissolve(1.5)
                    bk3_g1_b "and we're ready for action"



                call room38_guardfuck_1 from _call_room38_guardfuck_1

                y "But this needs the kind of closure only I can give."
                y "Sit down in front of me."
                show totq totq01
                hide totq with Dissolve(1.5)
                show totq totq00
                if totq_fucked_with == 'realdick':
                    show expression "bk3/guards/herma/donedick.png"
                else:
                    show expression "bk3/guards/herma/donedildo.png"
                with Dissolve(1.5)

                "you start masturbating and within less than a minute you empty your balls in one massive explosion."
                play sound "audio/splurt2.ogg"
                show expression "bk3/guards/herma/sperm_face.png"
                with flash
                y "Ahhh, now that's the way to end things."
                bk3_g1_b "We're feeling kinda tired, maybe we can do this again tomorrow but for today we're done."
                bk3_g1_b "Besides we have to go back to our cell anyway."
                bk3_g1_b "See ya later!"

                show expression "maze/black.png" with Dissolve(1.5)
                show text "The two guards unsteadily waddle out of the room."
                $ renpy.pause()

                $ bk3_room38_guardsex = False


                hide expression "maze/love_nudeguards.png"
                hide totq
                if totq_fucked_with == 'realdick':
                    hide expression "bk3/guards/herma/donedick.png"
                else:
                    hide expression "bk3/guards/herma/donedildo.png"
                hide expression "bk3/guards/herma/sperm_face.png"
                hide text
                hide expression "maze/black.png"

                jump love_unique_room38
            "Let's fuck":


                call room38_guardfuck_2 from _call_room38_guardfuck_2

        call screen love_maze_directions



    if current_room.sp_content == 1:

        show totq totq00 with Dissolve(1.5)
        hide expression "maze/love_nudeguards.png"



        bk3_g1_b "Hey avatar, nice you could make it!"
        y "You're naked."
        y "....."
        y "wherever this is going, I like where it's starting."
        bk3_g2_b "I'm cold."
        y "so, why did you ask me to come here?"
        bk3_g1_b "Well, first let me ask you a question."
        bk3_g1_b "How do you feel about chicks with dicks?"
        menu:
            "I want to believe they're real":
                $ current_room.sp_content = 2
                $ totq_fucked_with = 'realdick'
                bk3_g1_b "Nice! Because I came into possession of a potion which can grow a dick."
                bk3_g1_b "A few drops will make one which lasts a minute."
                bk3_g1_b "Here, I'll show."

                show totq totq54 with Dissolve(1.0)

                bk3_g1_b "A few drops from this bottle and...."

                show totq totq55 with Dissolve(0.7)
                show totq totq56 with Dissolve(0.7)
                show totq totq57 with Dissolve(0.7)
                show totq totq58 with Dissolve(0.7)
                bk3_g1_b "Presto!"
            "The stuff of nightmares":


                $ current_room.sp_content = 2
                $ totq_fucked_with = 'doubledildo'
                y "There are no chicks with dicks, only men with tits."
                y "But if you're talking about strapons or something, I'm down with those."
                bk3_g1_b "Nice! Because I got one of those double dildo things."
                bk3_g1_b "Here, I'll show."

                show totq totq50
                bk3_g1_b "We take this big floppy pink dildo."
                show totq totq51 with Dissolve(1.5)
                bk3_g1_b "...Hnnnng..."
                bk3_g1_b "...push it in..."
                show totq totq52 with Dissolve(1.5)
                bk3_g1_b "...and we're ready for action."
            "Don't have time for this right now.":

                y "Okay, I have a feeling where this is going, but I don't have time right now."
                y "I'll come back sometime later, okay?"
                bk3_g1_b " Aaawhh."
                bk3_g1_b "Okay, come visit us when you have the time!"
                call screen love_maze_directions



        $ current_room.sp_content = 2
        y "Okay so what's this all about?"
        bk3_g2_b "While we were \"hanging around\" we figured... hey why haven't we fucked each other?"
        bk3_g1_b "And since you're usually around here, you might as well watch us for that extra kick."
        y "You want me to watch you two bang each other?"
        bk3_g2_b "You seem like the kind of person who'd be down for watching some girl on girl action."
        y "You guessed right, but I want something in return."
        bk3_g1_b "Like what?"
        y "I don't know yet."
        y "But I'll come up with something."
        call room38_guardfuck_1 from _call_room38_guardfuck_1_1

        y "Take a break, girls."
        hide totq
        show totq totq00
        if totq_fucked_with == 'realdick':
            show expression "bk3/guards/herma/donedick.png"
        else:
            show expression "bk3/guards/herma/donedildo.png"
        $ renpy.pause()

        bk3_g1_b "Wow, we worked up quite a sweat."
        if totq_fucked_with == 'realdick':
            bk3_g2_b "Ah, the potion is already losing it's effect."
            hide expression "bk3/guards/herma/donedick.png" with Dissolve(1.7)
        else:
            bk3_g2_b "Ah, let me put this thing aside."
            hide expression "bk3/guards/herma/donedildo.png" with Dissolve(1.7)


        menu:
            "My turn now":
                y "As much fun as it is to watch, participating is even better."
                y "I have quite some experience so I'll give you something to compare against."
            "I got things to do":
                y "That was nice, but I have to go now."
                hide expression "maze/black.png"

                hide text



                hide totq
                hide totq_other

                jump love_unique_room38


        call room38_guardfuck_2 from _call_room38_guardfuck_2_1


        call screen love_maze_directions

label room38_guardfuck_1:
    hide totq
    $ totq_fucked = 'peanut'

    show totq totq01 with Dissolve(1.5):
        xzoom 0.7 yzoom 0.7
    bk3_g1_b "Enjoy the show, Avatar!"
    bk3_g1_b "No time for foreplay!! In it goes!"
    show totq totq100

    bk3_g2_b "Aaah... it's so big..." with hpunch
    show ctc
    pause
    hide ctc
    bk3_g2_b "You're splitting my poor pussy open!"
    bk3_g1_b "Don't give me that shit."
    bk3_g1_b "You're loving this!"
    bk3_g1_b "Admit it!"
    bk3_g1_b "You're getting a kick out of me forcefully pushing it in."
    bk3_g2_b "...you're right! Keep plowing!"
    bk3_g2_b "Slam it in there as if the warranty is still valid!"
    bk3_g1_b "You asked for it!"
    show totq totq101
    bk3_g2_b "AAAAAAAH!!!"
    show ctc
    pause
    hide ctc
    bk3_g1_b "That's it! take it like the bitch you are!"
    bk3_g1_b "Swallow my \"carrot\"!"
    bk3_g2_b "Hhhhnnnngg!! So... big... so... so gooood..."
    bk3_g1_b "You like watching this, avatar!?"
    bk3_g1_b "You like me giving it to this bitch in heat!!"
    bk3_g2_b "Ss...sswitch places with me!"

    if totq_fucked_with == 'realdick':
        bk3_g1_b "Too bad that potion didn't grow balls too or I could've cum inside you."
        bk3_g1_b "Oh whatever."
        bk3_g1_b "Okay, let's switch!"
    else:
        bk3_g1_b "I wish this dildo had some sort of squirt action build in."
        bk3_g1_b "I'd love to \"cum\" inside her and see my seed drip out!"
        bk3_g1_b "Oh whatever. Okay, let's switch!"

    show totq totq01
    show expression "maze/black.png" with dissolve
    hide text
    show text "{color=fff} The girls switch places and immediately get back to work.{/color}"
    $ renpy.pause()
    hide text
    $ totq_fucked = 'krystal'
    hide totq

    show totq totq101:
        xpos -200
    hide expression "maze/black.png"
    with dissolve

    bk3_g2_b "AAAAAaaaand in it goes!"
    bk3_g1_b "Hnnnnnnngggg!!!"
    show ctc
    pause
    hide ctc
    bk3_g1_b "You... you could've started out slow you know!!"
    bk3_g2_b "No time for that, we have to entertain our guest."
    bk3_g2_b "Are you enjoying yourself so far, avatar?"
    y "It's always good to see girls explore other girls!"

    return

label room38_guardfuck_2:

    y "Get on all fours and turn your butt towards me."
    hide totq
    show totq_other
    show totq totq17
    bk3_g1_b "Like this?"
    show ctc
    pause
    hide ctc
    y "Exactly like that."


    $ totq_fucked = 'krystal'
    show totq totq10

    bk3_g1_b "AAAahhhh!!!" with vpunch
    show ctc
    pause
    hide ctc
    y "That's right, no waiting in line for you."
    bk3_g1_b "Ah! Ah! You're pushing so hard against my womb!"
    y "Well, that's your fault for having such a shapely behind. "
    y "it wants me to plant my dick deep within it."
    $ renpy.pause()
    bk3_g2_b "Aaawhh, no fair! I wanted it more."
    $ totq_fucked = 'peanut'
    bk3_g2_b "HHHHHNNNNNGGGG!!!!" with vpunch
    show ctc
    pause
    hide ctc
    bk3_g2_b "So... so hard and big... *pant* *pant*"
    y "You're clamping down pretty hard on me."
    bk3_g1_b "I can clamp down hard too! Come and see for yourself!"
    bk3_g2_b "Hnnngg... don't... try and steal my dick!"
    bk3_g2_b "It's my turn now."
    $ renpy.pause()
    $ totq_fucked = 'krystal'
    y "Some for you!" with vpunch
    $ totq_fucked = 'peanut'
    y "For you again!" with vpunch
    $ totq_fucked = 'krystal'
    y "And back to you!" with vpunch
    y "I think both of you are ready for the real deal."
    bk3_g2_b "Do it!!"
    bk3_g1_b "Wait! Wai-"
    show totq totq16
    bk3_g1_b "tttttt!!!" with vpunch
    bk3_g2_b "Hahaha, sissy!"
    $ totq_fucked = 'peanut'
    bk3_g2_b "HIiiiiiiii!!!!" with vpunch
    bk3_g1_b "Hahaha, take that!"
    bk3_g2_b "g-g-gladly!!"
    bk3_g1_b ".....Shit!! Do me! Do me!"
    menu:
        "switch girls":
            $ totq_fucked = 'krystal'
            bk3_g1_b "Yay!"
            bk3_g2_b "Aaaaawwwh!!"
            $ renpy.pause()
        "stay with this one":

            bk3_g1_b "Awwwh!"
            bk3_g2_b "I win!!!"
            $ renpy.pause()



    y "I really understand why Ajala loves to reward or punish you with a fingerbang."
    y "It's like I'm being sucked in."
    y "Hmmmmm.... I'm..."
    y "I'm about to cum!"

    menu:
        "On their masks":
            y "Show me your faces!!"
            hide totq
            show totq totq00
            "As soon as the girls turn around you unload in one massive explosion."
            play sound "audio/splurt2.ogg"
            show expression "bk3/guards/herma/sperm_face.png"
            with flash
            y "Ahhh, now that's the way to end things."
            bk3_g2_b "We're feeling kinda tired, maybe we can do this again tomorrow but for today we're done"
            bk3_g1_b "Besides we have to go back to our cell anyway."
            bk3_g1_b "See ya later!"

            show expression "maze/black.png" with Dissolve(1.5)
            show text "The two guards unsteadily waddle out of the room."
            $ renpy.pause()

            hide totq
            hide expression "bk3/guards/herma/sperm_face.png"
        "Cum inside them":


            $ totq_fucked = 'peanut'
            show totq totq12 with vpunch
            y "ngh!"
            play sound "audio/splurt2.ogg"
            with flash
            y "fuck!"
            $ totq_fucked = 'krystal'
            show totq totq12 with vpunch
            y "take it, whore!"
            play sound "audio/splurt2.ogg"
            with flash

            show totq totq59 with Dissolve(1.5)
            $ renpy.pause()
            "The sperm you just unloaded has filled up the girls and is now dripping out their pussies."
            bk3_g2_b "So that's how it feels when you're filled with sperm..."
            bk3_g1_b "Creamy!"
            y "And there's more where that came from!"
            y "But not right now."
            y "I need to make more."

            bk3_g1_b "Good because we're feeling kinda tired."
            bk3_g1_b "Maybe we can do this again later, but for today we're done."
            bk3_g1_b "Besides, we have to go back to our cell before anyone finds out we're missing."
            bk3_g1_b "It was fun. Seeya later!"

            show expression "maze/black.png" with Dissolve(1.5)
            show text "The two guards unsteadily waddle out of the room."

            $ renpy.pause()


    hide expression "maze/black.png"
    hide expression "maze/love_nudeguards.png"
    hide text
    $ bk3_room38_guardsex = False


    hide totq
    hide totq_other

    jump love_unique_room38

    return
    call screen love_maze_directions 



label love_unique_room40:

    $ sp_item_xpos = 898
    $ sp_item_ypos = 164
    $ sp_item_width = 101
    $ sp_item_height = 177




    if room36.sp_content == 4 and current_room.sp_content == 0:
        play sound "audio/thud.mp3"
        "With a lot of effort you manage to wiggle yourself through the opening." with hpunch
        $ current_room.sp_content = 1
    if room36.sp_content == 4:
        $ room36.sp_content = 5
        y "There's no way a big hipped girl like Suki will fit through that opening."



    call screen love_maze_directions

label love_unique_room40_activate:

    if room36.sp_content == 5:
        scene black
        "You make your way back to Suki"
        $ room36.sp_content = 3
        $ current_room = room36
        jump love_bk3_maze_start


    if room36.sp_content >= 6:
        "I already have the key to open the celldoor. There's no need to go back that way."
        call screen love_maze_directions

    call screen love_maze_directions



label love_unique_room42:

    $ sp_item_xpos = 556
    $ sp_item_ypos = 2
    $ sp_item_width = 210
    $ sp_item_height = 243

    if current_room.north == 46:
        hide expression "maze/love_door1_closed.png"
        show expression "maze/love_door1_open.png"
    else:
        hide expression "maze/love_door1_open.png"
        show expression "maze/love_door1_closed.png"



    call screen love_maze_directions



label love_unique_room42_activate:
    if toph_chat <=9:
        y "what's this note say?"
        show text "{color=#ffffff}\"i have occupants in mind for this room, so keep it empty until I say so.\"\n signed - Ajala"
        show ctc
        pause
        hide ctc
        hide text
        y "guess it's not being used right now."
        call screen love_maze_directions

    if current_room.sp_content == 0:
        y "hey look, a note."
        show text "{color=#ffffff}\"I'm very happy with this haul and I'm going to be very sad and very angry if someone let's them escape.\"\nsigned - Ajala"
        $ current_room.sp_content = 1
        $ renpy.pause()
        hide text

    if current_room.north == 46:
        $ current_room.north = -1
    else:
        $ current_room.north = 46

    jump love_unique_room42

    call screen love_maze_directions


label love_unique_room46:

    $ sp_item_xpos = 556
    $ sp_item_ypos = 206
    $ sp_item_width = 264
    $ sp_item_height = 278





    if toph_chat <=9:
        call screen love_maze_directions

    if meangirls_escapedmaze in [0,1]:
        show tomg tomg10
    if current_room.visit == 1:
        "You see three naked girls huddled together in the corner of the room..."
        y "There's something familiar about them...."

    call screen love_maze_directions



label love_unique_room46_activate:

    if current_room.sp_content == 0:
        $ current_room.sp_content = 1

        show tomg tomg11
        with Dissolve(1.5)
        "girl 1" "We're sorry!! We're sorry!"
        "girl 1" "please, we won't ever bother you or your girlfriend again, but please let us go!!"
        show ctc
        pause
        hide ctc
        y "(It's the three hyena girls who were bullying Toph on the street!)"
        y "(Wait a minute... Do they think I had something to do with their abduction?)"
        y "(That's... interesting.)"

        menu:
            "Tell them the truth":
                y "I had nothing to do with this."
                "girl 1" "but..."
                y "It's purely a coincidence I found you here."
                y "I'm actually here to find and help free you guys."
                "girl 1" "r...really..?"
                y "Yeah, and although you guys were pretty obnoxious..."
                y "nobody deserves to be brainwashed into being Ajala's sex slaves."
                y "How did you end up here anyway?"
                "girl 1" "When we were walking home that night after... you know..."
                "girl 1" "a woman asked us if anything was wrong. "
                "girl 1" "The next thing we remember is waking up here."
                y "(Oh crap, could this partly be my fault?)"
                y "There's a hospital in a small village close by."
                y "It's run by a girl called Katara."
                y "She'll help you and send you on your way afterwards."
                y "Oh, and avoid anyone wearing a mask down here or you'll find yourselves locked up again."
                "girls" "......"
                y "Well? What are you waiting for? Run, you fools!"
                show tomg tomg12
                "girl 1" "Thank you, thank you so much!!"
                show ctc
                pause
                hide ctc
                "girl 1" "And we're really sorry about before!!"
                "With that last word, the girls quickly run out of the cell."
                $ meangirls_escapedmaze = 3
                hide tomg with Dissolve(1.5)
                y "Wow, I really didn't expect to see those girls again."
            "Abuse the situation":

                $ meangirls_escapedmaze = 1
                y "Hahaha!"
                y "You didn't really think we were done, did you?"
                y "This is all part of my revenge on you for what you did earlier!"
                show tomg tomg12 with dissolve
                "girl 1" "Please let us go... we'll do whatever you want!"
                y "Maybe I'll let you go if the three of you lick my cock simultaneously... maybe."
                show tomg tomg11 with dissolve
                "girl 1" "But... but we've never done anything like that."
                y "Then you'll learn on the job."
                y "Kneel in front of me."

                $ meangirls_number_oflicks = 0
                call meangirls_maze_licking from _call_meangirls_maze_licking
                show tomg tomg13

                with Dissolve(1.5)
                show ctc
                pause
                hide ctc
                "girl 1" "Wa-was that good? Can we go now?"
                menu:
                    "You're free to go":
                        y "Yeah get the fuck out of here, you cocksluts."
                        $ meangirls_escapedmaze = 2
                        hide tomg

                        with Dissolve(1.5)
                    "I need to give it some more thought":

                        y "maybe later... if you're good girls."
                        "With crushingly disappointed faces, the girls huddle together in the corner of the room."

                        show tomg tomg10
                        with Dissolve(1.5)




        call screen love_maze_directions

    if meangirls_escapedmaze == 1:

        show tomg tomg11
        with Dissolve(1.5)
        "Girl 1" "Yes?"
        menu:
            "Time for my licking girls":
                y "Kneel in front of me."
                call meangirls_maze_licking from _call_meangirls_maze_licking_1
                show tomg tomg13
                with Dissolve(1.5)
                "girl 1" "Wa-was that good? Can we go now?"
                y "I'll think about it."
                show tomg tomg10
            "Tell them they can leave":

                $ meangirls_escapedmaze = 2
                y "I think it's time for you girls to go home."
                y "But keep the following in mind..."
                y "If you bother me or my girl again I'll introduce your uterus to my cock."
                show tomg tomg12
                "girl 1" "We'll never ever bother you or your girl again!!! We promise!!"
                "girl 2 and 3" "We promise!!!"
                y "Good, now get out of here, you cocksluts."
                hide tomg with Dissolve(1.5)
            "exit":
                show tomg tomg10
                with Dissolve(1.5)



    call screen love_maze_directions




label love_unique_room47:

    if current_room.maze_enemy == True:

        show expression "maze/love_ajala_angry.png"
        ct "You're going down!" with hpunch
        ct "I won't fall for your cheap tricks again."

        if room47.sp_content == 1:
            ct "jessica told me all about the awful things you said!"
            ct "I can't let that go unpunished."

        elif room47.sp_content == 2:
            ct "I saw jessica walking around with the dildo i'd hidden away."
            ct "Apparently, she got it from you!"
            ct "You're not only stealing my prisoners, but my other toys too?!"
            y "Really? So that dildo wasn't something you stole from Suki?"
            y "Why were you hiding it behind that stone in the first place?"
            ct "Half of the girls here would be using it if I didn't."



        ct "Tell you what..."
        ct "I'm so certain you can't beat me in a fair fight, I'll make a wager."
        ct "If you can beat me without tricks...."
        hide expression "maze/love_ajala_angry.png"
        show expression "maze/love_ajala_delight.png"
        with dissolve

        ct "You can claim your... reward."

        if ajala_headlock_fuckedinass == True:
            y "You really enjoyed getting it in your ass last time, huh?"
            ct "Maybe, but you'll have to earn it if you want to stick it in my ass again."
            y "Ass? I'm feeling more like doing pussy today."
            ct "You'll have to beat me first."
            ct "and don't think I'll hold back just because it felt a little nice last time."
        else:
            y "Which is?"
            ct "You can pound my pussy till I can feel the burn.... IF you win."
            y "If schmiff. In about five minutes I'm going to cream all over you. "
            y "Or in you. I haven't made up my mind about that. "
            ct "Hah! Talk is cheap. Let's see you prove that!"

        menu:
            "bribe her with pornlove" if b3love_pornlove1_own == True:

                y "ooooor I could give you this old pornlove and you stop blocking this part of the maze forever. "
                y "I don't feel like rough-housing with you."
                "You show the cover of the pornlove."
                hide expression "maze/love_ajala_delight.png"
                show expression "maze/love_ajala_surprise.png"
                ct "Oh, wow! that's an old one..."
                ct "kinda rare, too... "
                ct "I want it!"
                hide expression "maze/love_ajala_surprise.png"
                show expression "maze/love_ajala_angry.png"
                ct "SO what's stopping me from taking it by force?"
                y "If we fight, it's bound to tear."
                y "Or I'll just burn it right here."
                y "I can firebend, you know."
                ct "You barbarian!!"
                ct "Fine, deal."
                ct "Give me the pornlove and I'll let you go... THIS time."
                "You hand Ajala the pornlove after which she walks away."
                ya "What the fuck did I just do?!?"
                $ b3love_pornlove1_own = False
                $ room47.maze_enemy = False
                hide expression "maze/love_ajala_angry.png"
                call screen love_maze_directions
            "Disengage!":


                $ current_room = previous_room
                scene black with Dissolve(1.0)
                "You quickly retreat. Ajala doesn't follow you."
                ct "I'll be waiting here!"
                jump love_bk3_maze_start
            "Attack!":


                hide expression "maze/love_ajala_delight.png"
                $ room47.maze_enemy = False
                jump love_bk3_start_the_fight


    call screen love_maze_directions





label love_unique_room55:
    $ sp_item_xpos = 556
    $ sp_item_ypos = 2
    $ sp_item_width = 210
    $ sp_item_height = 243

    if current_room.north == 63:
        show expression "maze/love_door1_open.png"
    else:
        show expression "maze/love_door1_closed.png"

    call screen love_maze_directions

label love_unique_room55_activate:

    if current_room.sp_content == 0:
        $ current_room.sp_content = 1
        y "Huh, a note."
        y "Let's see what it says."
        show text "{color=#fff} Jessica, don't feed these two until I say otherwise.  \n xxx Ajala{/color}"
        y "Ah, some more victims of Ajala."
        hide text

    if current_room.north == 63:
        $ current_room.north = -1
        show expression "maze/love_door1_open.png"
    else:
        $ current_room.north = 63
        show expression "maze/love_door1_closed.png"
    jump love_bk3_maze_start



    call screen love_maze_directions



label love_unique_room57:

    if current_room.maze_enemy:
        show expression "maze/maze_enemies.png" with hpunch
        bk3_g3_jess "Hey! You aren't supposed to be here!"
        y "I heard you have the key to Jin's shackles? I want it."
        bk3_g3_jess "And you think I'm just going to hand it over?!"

        menu:
            "Fight her fair!":

                hide expression "maze/maze_enemies.png"
                jump love_bk3_start_the_fight
            "Go for her vulnerability!":

                y "Fat pig says what?"
                bk3_g3_jess "What?"
                y "it's a shame you have all those rolls, or someone might like you."
                y "Aren't the guards here supposed to be pretty?"
                bk3_g3_jess "That's... that's really low!"
                bk3_g3_jess "I'm not fat!"
                bk3_g3_jess "I could lose a few pounds sure, but..."
                y "Yeah, keep lying to yourself."
                bk3_g3_jess "I... I... I'm going to tell Ajala you were mean to me!"
                show expression "maze/maze_enemies.png":
                    ypos 720
                    linear 0.5 ypos 1440
                "the girl bumps into you as she runs past you crying."
                "Something falls out of her pocket."
                y "Ah shit, i feel horrible about that."
                y "This might come back to bite me in the ass."
                $ room47.sp_content = 1
                $ current_room.maze_enemy = False
            "Try to bribe her!":


                y "Look, just give me the damn key."
                y "I'll pay you for it."
                bk3_g3_jess "I don't need money, Ajala hardly ever lets us go anywhere to spend it, anyway."
                y "is there... something else I can help you with?"
                bk3_g3_jess "I'll trade it for a dildo."
                y "Why would I have a dildo on me?"
                bk3_g3_jess "Don't know, don't care. I lost mine, so I want a new one."
                bk3_g3_jess "Do you have one?"
                if b3love_dildo_gotit == True:
                    menu:
                        "Give her the Kyoshi statue.":

                            y "Is this okay?"
                            "You hand her the dildo in the shape of a Kyoshi statue."
                            bk3_g3_jess "Oooh! That's a nice one! Okay, we have a deal."
                            $ current_room.maze_enemy = False
                            hide expression "maze/maze_enemies.png" with Dissolve(1.0)
                            $ b3love_dildo_gotit = False
                            $ room47.sp_content = 2
                            jump love_bk3_maze_start
                        "No (lie) ":
                            pass
                else:

                    y "I don't."
                bk3_g3_jess "Then we fight!"
                hide expression "maze/maze_enemies.png" with Dissolve(1.0)
                jump love_bk3_start_the_fight


    if current_room.maze_enemy == False and current_room.sp_content == 1:
        play sound "audio/win2.mp3"
        show expression "maze/prisonkey.png" with Dissolve(2.0)
        "You got the key to open jin's shackles!"
        hide expression "maze/prisonkey.png" with Dissolve(1.0)
        $ b3love_jin_key = True
        $ current_room.sp_content = 2

    call screen love_maze_directions


label love_unique_room58:

    $ sp_item_xpos = 349
    $ sp_item_ypos = 247
    $ sp_item_width = 269
    $ sp_item_height = 250





    if current_room.sp_content == 0:
        show expression "maze/love_jin_shackles_0.png"
    elif current_room.sp_content < 4:
        show expression "maze/love_jin_shackles_1.png"
    elif current_room.sp_content == 4:
        show expression "maze/love_jin_shackles_2.png"
        show tojc tojc07

        jin "Thanks! I'm going to get out of here and cuntpunt every bitch along the way!"
        $ current_room.sp_content = 5
        hide tojc tojc07 with Dissolve(1.5)
        $ love_jin_freed = True
    elif current_room.sp_content == 5:
        show expression "maze/love_jin_shackles_2.png"


    call screen love_maze_directions



label love_unique_room58_activate:

    show expression "bk3/jin/shackles/bg.jpg"


    if current_room.sp_content >= 4:
        y "There's nothing here."


    if current_room.sp_content == 2:

        show tojc tojc00
        jin "Thanks again! It was like an itch you can't scratch!"
        jin "Now please figure out how to get rid of these shackles so we can get out of here."
        menu:
            "exit":
                pass
            "unlock shackles" if b3love_jin_key == True:
                y "I found the key."
                y "I'll have you out of here in no time."
                play sound "audio/shackles_gone.mp3"
                $ renpy.pause(1.0)
                $ current_room.sp_content = 4
                $ room47.maze_enemy = True


    if current_room.sp_content == 1:

        show tojc tojc00
        jin "Please help me!"
        menu:
            "help her out (sex)":
                $ current_room.sp_content = 2
                call jin_had_mazesex from _call_jin_had_mazesex

            "unlock shackles" if b3love_jin_key == True:
                play sound "audio/shackles_gone.mp3"
                "You take the key you found earlier and free Jin."
                $ current_room.sp_content = 4
                $ room47.maze_enemy = True
            "find a way to free her":
                y "It's more important to find a way to free you first."


    if current_room.sp_content == 0:



        show tojc tojc00
        jin "Who's there? I can hear you!"
        jin "Is that you, ajala?"
        jin "Still afraid of me after I kicked you in the cunt?!"
        jin "Sure looks like it, with the way you've shackled me."
        menu:
            "leave":
                pass
            "remove blindfold":
                $ current_room.sp_content = 1

                y "Wow, you're a feisty one!"
                jin "Who are you?"
                y "Let me take that blindfold off first."
                $ tojc_face = 'neutral'
                jin "Thanks, but I still have no idea who you are."
                y "Really? That doesn't happen too often."
                jin "Oh wait... those tattoos..."
                jin "Could it be you're the avatar?!"
                y "That's me."
                jin "So, you don't belong to these people?!"
                jin "Excellent!"
                jin "Please fuck me!!"
                y "uhhh, wouldn't you like me to free you?"
                jin "There's this gorilla woman who has been trying to mindbreak me."
                y "Yeah, I know all about her."
                jin "She's been driving me crazy by licking me, but always stops right before I orgasm."
                jin "She told me she'd let me orgasm if I'd ask her nicely."
                jin "i eventually caved, but she still didn't let me!"
                jin "i think she's trying to break me!"
                jin "I'm at my wits end!"
                menu:
                    "help her out (sex)":
                        $ current_room.sp_content = 2
                        call jin_had_mazesex from _call_jin_had_mazesex_1
                    "Find a way to free her":

                        y "Let me see if I can free you first."

                    "unlock shackles" if b3love_jin_key == True:
                        play sound "audio/shackles_gone.mp3"
                        "You take the key you found earlier and free Jin."
                        $ current_room.sp_content = 4







    jump love_bk3_maze_start

    call screen love_maze_directions





label love_unique_room61:


    $ sp_item_xpos = 723
    $ sp_item_ypos = 177
    $ sp_item_width = 95
    $ sp_item_height = 60



    show expression "maze/sp_we_grate.png"
    if current_room.visit == 1:
        mv "Psstt!"
        mv "Hey you! Down here!"

    call screen love_maze_directions      

label love_unique_room61_activate:

    if bk3love_freetoph >= 4:
        menu:
            "enter":
                $ current_room = room113
                jump love_bk3_maze_start
            "exit":
                jump love_bk3_maze_start


    show expression "maze/grate_eyes.jpg"
    y "uhh... anyone there?"
    show expression "maze/grate_eyes1.png"


    if bk3love_freetoph == 3:
        sok "Hey have you freed Toph already?"
        y "Oh shit... I'll be right back."
        jump love_bk3_maze_start


    if current_room.sp_content == 0:
        $ current_room.sp_content = 1
        mv "Ahem, hey."
        mv "You don't know me, so if my voice sounds familiar it's a coincidence."
        y "Sure, sure."
        y "If that's all, I'll be going now."
        mv "Wait! I want to make a deal!"
        y "What kind of deal?"
        mv "I like dirty panties."
        y "...."
        mv "I like to sniff them, lick them, rub them all over my..."
        y "Too many details!!"
        mv "Oh, sorry."
        mv "Anyway, they must be girl panties and obviously have been worn by a girl."
        y "So... what about this deal?"
        mv "If you can get me a dirty panty, I'll give you something good."
        y "Meaning?"
        mv "Maybe money, maybe information..."
        y "Got any pornloves instead?"
        mv "Absolutely, but I'm keeping those for myself."
        y "Hmmm..."
        y "well, if I happen to come across some dirty laundry, I might bring it to you..."
        y "{i}might."
        mv "And remember, you don't know me!"
        mv "So, don't say anything about this to Katara."
        y "...."
    else:
        mv "Hey man! Got some panties for me?"
        if b3love_sokkapanties >= 1:
            menu:
                "Yeah, here's one":
                    $ b3love_sokkapanties -= 1

                    "You push a pair of dirty panties through the opening of the grate."
                    "A sound of someone deeply inhaling can be heard."
                    mv "Aaah... good shit, man."
                    mv "Okay, what can I give you?"
                    menu:
                        "pornlove" if b3love_pornlove1_own == False:
                            mv "hmmm...."
                            mv "well, okay... but only because you got me a really good pair."
                            mv "I made a copy of a vintage black and white issue."
                            mv "It's super old and not that good, but rare."
                            mv "You can have the copy."
                            play sound "audio/win2.mp3"
                            $ b3love_pornlove1_own = True
                            "You got an old pornlove edition! You can read it in your home!"
                            mv "Btw... there's a bit of a backstory to this edition. Wanna hear it?"
                            menu:
                                "No thanks":
                                    pass
                                "Sure":
                                    mv "It depicts a watertribe girl and three fire nation soldiers."
                                    mv "Some say it's a typical story setup to make the porn more interesting...."
                                    mv "But some say the watertribe girl was a real prisoner and the guards forced her to do this."
                                    mv "Nobody knows the truth but there's this weird story about how the three soldiers/actors died."
                                    y "...How did they die?"
                                    mv "Their dicks exploded as if too much blood was pumped in them...."
                                    y "Oh, wow, that must be the worst way to go..."
                                    mv "Well, whatever."
                                    mv "Have fun with the copy."
                                    mv "sorry I can't give you the original, but that one is worth a small fortune."
                        "I like money":

                            mv "Don't we all. Here's 50 gold."
                            play sound "audio/money.mp3"
                            $ emoney += 50
                        "Give me some info":

                            mv "Sometimes Ajala walks by this grate towards the east."
                            mv "I can hear some sopping noises and moaning afterwards and then she returns."
                            mv "It's a deadend and I can't see what she's doing, but maybe you could investigate it."
                            y "I was hoping for something better."
                            mv "I don't have anything else right now."




                    jump love_bk3_maze_start
                "Nope":

                    pass

        y "Sorry, nothing right now."

    jump love_bk3_maze_start




label love_unique_room62:

    $ sp_item_xpos = 898
    $ sp_item_ypos = 164
    $ sp_item_width = 101
    $ sp_item_height = 177

    if current_room.sp_content != 0:
        show expression "maze/love_loosestone_cover.png"

    call screen love_maze_directions

label love_unique_room62_activate:

    if current_room.sp_content ==0:
        "you discovered a loose stone!"
        menu:
            "Don't mess with it":
                call screen love_maze_directions
            "Remove the stone":

                $ current_room.sp_content = 1
                play sound "audio/stonegrind.mp3"   
                show expression "maze/love_loosestone_cover.png" with Dissolve(1.5)
                y "Looks like a hiding place for something!"
                jump love_unique_room62




    if current_room.sp_content == 1:
        y "There's something in the hole..."
        play sound "audio/win2.mp3"
        show expression "maze/kyoshi_dildo.png" with Dissolve(2.0)
        $ b3love_dildo_gotit = True
        $ current_room.sp_content = 2
        y "This is clearly a dildo disguised as a kyoshi statue."
        hide expression "maze/kyoshi_dildo.png" with Dissolve(1.0)
        y "I could give it to Toph for her birthday!"
        y "Whenever that is...."
        y "maybe I should ask Katara."
        y "then again, I don't know Katara's birthday, either."
        y "Let's not walk into that minefield."

    call screen love_maze_directions





label love_unique_room63:
    $ sp_item_xpos = 277
    $ sp_item_ypos = 65
    $ sp_item_width = 505
    $ sp_item_height = 460




    if bk3_rescue_idiots > 0:
        show expression "maze/love_holeinwall.png"
        $ current_room.sp_item = False
        if current_room.east != 82:
            "you enter the room and see a big gaping hole to your right leading into a dark tunnel."
            y "Fuck... this looks bad."
            y "Well at least there isn't a trail of blood to follow."
            y "That's like a good sign, right?"
            y "Well, let's find those two. "

        $ current_room.east = 82

        call screen love_maze_directions
    else:
        show expression "maze/love_guards_shadow_1.png"
        call screen love_maze_directions



label love_unique_room63_activate:

    hide expression "maze/love_guards_shadow_1.png"
    show expression "maze/love_guards_shackled.png"
    with dissolve



    if current_room.sp_content == 0:
        $ current_room.sp_content = 1


        bk3_g1_b "Hey! It's our buddy, the avatar!"
        y "...the fuck..."
        bk3_g2_b "I know we have our differences, but I always felt there was this deep soul connection between us, man."

        y "Oh, shut it."
        y "What are you doing here?"

        bk3_g1_b "Well, we had an evalution interview with our h.r. department."
        bk3_g2_b "and we've been demoted to a trainee position."

        bk3_g1_b "I know you're into freeing naked chicks, but please restrain your urges in this particular case."
        bk3_g2_b "Ajala will calm down sooner or later and let us go."

        bk3_g1_b "But come around from time to time and talk to us."
        bk3_g1_b "we've run out of interesting stories to tell each other."


    menu:
        "Quit the conversation":

            show expression "maze/love_guards_shadow_1.png"
            hide expression "maze/love_guards_shackled.png"
            with dissolve
            call screen love_maze_directions
        "Tell me about this part of the maze":

            bk3_g2_b "It has tunnels, naked girls... nothing out of the ordinary."

        "Where can I find the key for Jin?" if room58.sp_content >= 1 and room58.sp_content < 4:
            bk3_g1_b "Who's jin?"
            y "Dark haired girl who apparently kicked Ajala in the pussy?"
            bk3_g1_b "Ooohhh... that girl."
            bk3_g1_b "Yeah, Ajala wasn't happy about that."
            bk3_g1_b "..."
            y "...so?"
            y "Where are they keeping the key to her shackles?"
            bk3_g2_b "It's in Krystal's butt......"
            bk3_g2_b "Haha, no just kidding."
            bk3_g2_b "Ajala wouldn't trust us with something like that."
            bk3_g1_b "I think Jessica has it."
            bk3_g2_b "Hey, wait, don't we have like five jessicas?"
            bk3_g1_b "The one who's insecure about her weight."
            bk3_g2_b "Oooh... her."
            bk3_g2_b "Yeah, she weighs the same as us but somehow thinks she's fat."
            bk3_g1_b "That's probably because I rigged her scale."
            bk3_g2_b "Why did you do that?"
            bk3_g1_b "I don't really know."
            bk3_g1_b "I guess I just was in a bitchy mood that day."
            bk3_g1_b "Also... she didn't say hi when I passed her three weeks ago."
            bk3_g2_b "Well, I guess she deserved it then."
            y "Okay, where can I find this jessica?"
            bk3_g1_b "She checks up on the prisoners regularly and feeds them."
            bk3_g1_b "You should run into her sooner or later if you hang around the prisoner."
            bk3_g1_b "Speaking of Jessica... wasn't she supposed to bring us something to eat by now?"
            bk3_g2_b "She's late."
            bk3_g1_b "Yeah. I'm starting to feel peckish."
            if room57.sp_content == 0:
                $ room57.sp_content = 1
                $ room57.maze_enemy = True

        "Tell them you freed Jin." if room58.sp_content >= 5:
            bk3_g1_b "Oh, well at least we have an alibi. There's no way Ajala can pin this on us."

        "Tell them you fucked Ajala." if b3love_ajala_mazevag > 0:
            bk3_g1_b "Good for you! Maybe that'll get her in a better mood."
            bk3_g2_b "So.. did you do her in the pussy or ass?"
            if ajala_headlock_fuckedinass == True:
                y "Both!"
            else:
                y "I plowed her pussy like it's planting season"
                if b3love_ajala_mazevag == 2:
                    y "In fact, I drenched her womb in my sperm."

            bk3_g1_b "Nice! I wouldn't mind giving her some of what she's given us lately!"
            bk3_g2_b "Next time you fuck her, give her a thrust for us.. but don't tell her we said so."
        "Search the room":


            if room61.sp_content >= 1 and current_room.sp_content == 1:
                "You rummage through the room and find a pair of panties among a pile of dirty clothes."
                bk3_g1_b "uh... that's mine."
                y "Shouldn't there be two pairs here?"
                bk3_g2_b "Ajala was kind of rough with mine when pulling them off, so they're all torn up."
                bk3_g1_b "Why are you touching them anyway?"
                menu:
                    "never mind":
                        "You throw the panties back on the pile of dirty clothes."
                        y "You're right, I don't want to get a disease."
                        bk3_g1_b "That's mean..."
                    "I'm taking these":


                        bk3_g1_b "I feel kind of flattered you'd even want those, but still..."
                        bk3_g1_b "...pervert."
                        y "They're not for me."
                        bk3_g1_b "Of course! It's for a friend..."
                        play sound "audio/win2.mp3"
                        show expression "maze/love_panty_1.png" with Dissolve(1.5)
                        "You got a pair of dirty panties!"
                        hide expression "maze/love_panty_1.png" with Dissolve(2.0)
                        $ b3love_sokkapanties += 1
                        $ current_room.sp_content = 2
            else:
                if not laundry_obsidian:
                    "you look through the pile of dirty clothes."
                    $ laundry_obsidian = True
                    y "what's this?"
                    $ obsidian +=1
                    play sound "audio/win2.mp3"
                    "you found {b}1 obsidian!"
                    y "neat."
                else:
                    "All you can find is a pile of dirty clothes."

    jump love_unique_room63_activate





label love_unique_room70:
    $ sp_item_xpos = 622
    $ sp_item_ypos = 60
    $ sp_item_width = 212
    $ sp_item_height = 380


    if room74.sp_content < 2:
        show expression im.Flip("maze/sp2_wallbuttgirl.png", horizontal = True)

        if current_room.visit == 1:
            y "Tylee?"
            ty "Hi!"


    if room75.sp_content == 1:
        $ room75.sp_content = 2
        show expression im.Flip("maze/stairway_down.png", horizontal = True)
        y "Let's just close this right the fuck back up and never ever open it again."
        play sound "audio/stonegrind.mp3"
        hide expression im.Flip("maze/stairway_down.png", horizontal = True) with Dissolve(1.5)

    if room74.sp_content == 2:
        show ty_idle_ff_nude with dissolve
        ty "I looked around and... there's nothing here."
        ty "Just an empty room."
        ty "Aaw... I wanted some adventure!"
        ty "Or a cute guy... or both!"
        ty "You know... You look sorta cute."
        y "Hold that thought, we've got some treasure hunting to finish first."
        y "The room is empty... suspiciously empty."
        y "I can try something."
        y "Toph taught me a trick where I can see with earthbending instead of my eyes."
        ty "...does she have bigger boobies than I have?"
        y "Let's just say Toph could've jumped through the hole which had you stuck."
        ty "So I also have bigger hips?"
        ty "Two points for me!"
        ty "Do you need my help doing this trick of yours?"

        y "No..."
        y "You just move back a little and stand still being all pretty and naked."
        ty "No problem!"

        show expression "maze/black.png" with Dissolve(1.5)
        show text "{color=#fff}You close your eyes... and concentrate.{/color}"
        $ renpy.pause()
        $ temp_boolean = False
        while temp_boolean == False:
            hide text
            menu:
                "stomp the ground - focus on the walls":
                    play sound "audio/thud.mp3"
                    show text "{color=#fff}You sense nothing out of the ordinary.{/color}" with hpunch
                    $ renpy.pause()
                "stomp the ground - focus on the ceiling":

                    play sound "audio/thud.mp3"
                    show text "{color=#fff}You sense nothing out of the ordinary." with hpunch
                    $ renpy.pause()
                "stomp the ground - focus on the floor":
                    hide text
                    play sound "audio/thud.mp3" 
                    show expression "maze/black.png" with hpunch
                    show expression "maze/love_secret_stairs.png" with Dissolve(1.5)

                    hide expression "maze/love_secret_stairs.png" with Dissolve(1.5)
                    hide expression "maze/black.png" with Dissolve(1.5)
                    y "Found something."
                    y "There's a hidden entryway to a lower level."
                    $ temp_boolean = True

        play sound "audio/stonegrind.mp3"
        show expression im.Flip("maze/stairway_down.png", horizontal = True) with Dissolve(2.0)

        ty "Oooh! It's a secret stairway!"
        $ room74.sp_content = 3
        hide ty_idle_ff_nude with dissolve
        "Before you know it, Tylee jumps down the stairs."
        y "Wait... a moment..."
        show expression "maze/love_mini_tylee.png"
        ty "What's taking you so long?"
        ty "Let's go! It's adventure time!"
        y "You do realize there could be big hairy spiders down there, right?"
        ty "I... I didn't."
        ty "I guess I can wait. "
        $ room74.sp_content = 3
        $ current_room = room75
        jump love_bk3_maze_start

    call screen love_maze_directions


label love_unique_room70_activate:

    if room74.sp_content == 1:
        ty "Still waiting."

    if room74.sp_content == 0:
        y "seriously... Tylee?!"
        ty "...yeah, that's me."

        ty "are you angry with me for trying to capture you?"
        y "maybe I should be, but some stuff happens in the future that makes it impossible for me to dislike you."
        ty "....really?"
        y "Yeah, it'll be awesome."
        y "By the way, you really should start a tavern when you return to the fire nation."
        ty "You think I could?"
        ty "It sorta has been a life long dream of mine, but I never figured I could."
        ty "especially while i'm working with azula."
        y "don't worry about it - you've got what it takes."
        ty "Well, okay! thanks!"
        y "So..."
        y "What are you doing here?"
        ty "...I got stuck."
        y "How? Why?"
        ty "um... speaking of azula..."
        y "what?"
        ty "well... she threw me in here!"
        ty "I don't know why!"
        ty "I was just flirting with a boy and she got so mad!"
        y "maybe she was jealous."
        ty "of me? but she's perfect!"
        y "okay..."
        y "it sounds like you just don't want to admit that azula betrayed you."
        ty "I... i don't think..."
        y "anyway, did she put you in this hole?"
        ty "no, i escaped my cell..."
        ty "I just overheard something about a treasure which was supposed to be around here."
        ty "I wanted to sneak into this room, but I got stuck."
        ty "I took off my clothes to fit through here, but..."
        y "you got stuck anyway."
        ty "yeah..."
        ty "Can you get me out?"
        y "I could try earthbending, but if anything goes wrong you could go \"splat\"."
        ty "I don't like that."
        y "Me neither."
        y "Want me to just pull you through?"
        ty "I'd lose all the skin on my hips!"
        y "Hmmmm."
        y "I think I'll walk around and see if something can be done from the other side."
        ty "Please do!"

        $ room74.sp_content = 1
    call screen love_maze_directions







label love_unique_room74:
    $ sp_item_xpos = 453
    $ sp_item_ypos = 261
    $ sp_item_width = 127
    $ sp_item_height = 226

    if current_room.sp_content < 2:
        show expression "maze/love_tylee_stuck.png"

    if current_room.visit == 1:
        $ room38.sp_content = 1
        $ bk3_room38_guardsex = True

        y "What... ?"
        show expression "maze/love_guards_shadow.png":
            xzoom 0.2 yzoom 0.2 xpos 750 ypos 220 alpha 0.0
            linear 2.0 xzoom 0.8 yzoom 0.8 xpos 580 ypos 150 alpha 1.0

        $ renpy.pause(2.0)
        bk3_g1 "Oh hey, there you are!"
        bk3_g2 "We've been looking for you everywhere, man."
        y "Uhhh... what's going on here?"
        bk3_g2 "There's a naked butt sticking out of the wall."
        bk3_g2 "get your eyes checked."
        y "no, i mean, {i}why{/i} is there a butt?"
        bk3_g1 "huh. yeah. good question."
        bk3_g1 "That's definitly unusual."
        bk3_g1 "Makes me wanna pinch it..."
        y "You guys didn't do this?"
        bk3_g1 "dude, we aren't even supposed to be walking around."
        bk3_g2 "As far as Ajala knows we're still being punished for incompetence."
        bk3_g1 "We make sure to return to our cell regularly in case someone comes along, and just pretend we're still shackled."
        bk3_g1 "We know all the secret shortcuts around here!"
        bk3_g1 "Oh, and before you ask, no we can't share those with you."
        bk3_g1 "It's bad enough that watertribe boy is using them as well."
        y "Don't they see you walking around?"
        bk3_g2 "That's why these masks are so great!"
        bk3_g2 "As long as you keep your distance, no one notices."
        bk3_g1 "Wait... we're getting distracted!"
        bk3_g1 "This is not why we came here!"
        bk3_g2 "Oh, right."
        bk3_g2 "Uhhhh.... what did we come here to do?"
        bk3_g1 "Avatar, we need your help!!"
        bk3_g1 "Come find us at that unused cell when you're.... done here?"
        bk3_g2 "Do you remember where we locked you up earlier?"
        bk3_g2 "In that room with that suki girl?"
        menu:
            "No.":
                bk3_g2 "We slammed the door shut with you and that girl in it and started mocking you for falling into our trap."
                bk3_g2 "When you enter the maze just go straight up, take a right and go up again."
            "How could I forget?":
                bk3_g2 "Yeah, that ass-fingering was damn hot..."
                bk3_g2 "Did you ever get any further with that girl?"
                bk3_g2 "I can't imagine someone getting their ass worked over like that and not come back for more."

        bk3_g2 "Aaaah... good times."
        bk3_g2 "Anyway..."
        bk3_g2 "There's a cell right next to it with big roots."
        bk3_g2 "That's where we'll be."
        bk3_g1 "Don't worry, it's not a trap this time."
        bk3_g1 "Well, have fun doing whatever you're doing here and see you later!"

        show expression "maze/love_guards_shadow.png":
            xzoom 0.8 yzoom 0.8 xpos 580 ypos 150
            linear 2.0 xzoom 0.2 yzoom 0.2 xpos 750 ypos 220
        hide expression "maze/love_guards_shadow.png" with Dissolve(2.0)

        y "Hmmm... I wonder what those two dumbasses are planning. "
        y "Probably nothing wholesome."




        show expression "maze/love_guards_shadow.png":
            xzoom 0.2 yzoom 0.2 xpos 750 ypos 220 alpha 0.0
            linear 1.0 xzoom 0.8 yzoom 0.8 xpos 580 ypos 150 alpha 1.0

        $ renpy.pause(1.0)

        if meangirls_escapedmaze == 3:
            bk3_g1 "By the way, you let those three girls escape earlier, didn't you?"
            y "That's my thing, isn't it?"
            bk3_g2 "Yeah sure, but we didn't smell cum in the room so we weren't sure it was you."
            bk3_g1 "When it's your handywork, there's usually cum all over the place, so we were a little surprised."
            bk3_g2 "You're a pretty awesome dude."
            bk3_g2 "I wouldn't be surprised if those girls will reward you someday."
            bk3_g1 "If they haven't already."

        elif meangirls_escapedmaze == 0:
            bk3_g1 "Btw, there's some girls you still haven't freed; three of 'em in the same room."
            bk3_g2 "Are you losing your touch?"
            if meangirls_number_oflicks >= 1:
                bk3_g1 "And it reeks of sperm in there."
                bk3_g2 "... which isn't unusual since you've been visiting the tunnels."
                bk3_g1 "but the girls are still there which {i}is{/i} out of the ordinary for you."
                bk3_g2 "I gotta be honest, man... I think you've wasted your chance to be rewarded by them."
                bk3_g2 "Even if you'd free them now the damage is already done."
                y "Meh, I already got my reward."
            elif meangirls_number_oflicks == 0:
                bk3_g2 "They're all alone waiting for a savior to come and save them."
                bk3_g2 "Who knows, maybe they'll reward you if you free them without abusing the situation."
                y "That's... interesting."

        elif meangirls_escapedmaze == 2:
            bk3_g1 "By the way, you let those three girls escape earlier didn't you?"
            y "That's my thing isn't it?"
            bk3_g2 "Sure, and the room did smell of cum which is a clear sign you've been around, but..."
            bk3_g2 "...it also smelled of regret and fear."
            bk3_g1 "I dunno man, but I think whatever chance you had at getting some reward for letting them go is gone now."
            y "Meh, I already got a reward out of it."


        bk3_g1 "That's all."
        bk3_g1 "Don't forget to visit us in the cell next to where you stuck your finger in the ass of that Suki girl."
        bk3_g1 "If you don't see us there, try the next day."
        bk3_g2 "See ya!"

        show expression "maze/love_guards_shadow.png":
            xzoom 0.8 yzoom 0.8 xpos 580 ypos 150
            linear 2.0 xzoom 0.2 yzoom 0.2 xpos 750 ypos 220
        hide expression "maze/love_guards_shadow.png" with Dissolve(2.0)

    call screen love_maze_directions


label love_unique_room74_activate:
    show expression "bk3/tylee/footjob/bg_wall.jpg"

    if current_room.sp_content == 2:
        y "You alright?"
        ty "Yep! A bit shaken, but not stirred!"
        y "....what?"
        ty "Walk around and join me!"

    if current_room.sp_content == 1:
        show totf_upper up1:
            alpha 0.3
        show totf totf01
        ty "Did you come up with something?"

        menu:
            "Nope, I'll need a bit more time.":
                ty "Okay, please don't take too long."
            "Lubricate her thighs with sperm":

                call b3l_spermontysass from _call_b3l_spermontysass

    if current_room.sp_content == 0:

        show totf totf01
        $ renpy.pause()

        menu:
            "speak":

                $ current_room.sp_content = 1
                y "Ahem, hello?"
                mv "Is... is someone there?"
                menu:
                    "yes":
                        pass
                    "no":
                        y "....no?"
                        mv "okay, i'll try again later."
                        y "....."
                        mv "is there someone there now?"
                y "I'll ask the questions."
                y "Who are you?"
                y "what are you doing here?"
                y "Your voice sounds oddly familiar."
                mv "it does?"
                mv "\"good\" familiar or \"bad\" familiar?"
                y "Wait a minute..."
                y "Tylee?!?"

                show totf_upper up1:
                    alpha 0.0
                    linear 2.0 alpha 0.3
                hide totf
                show totf totf01
                ty "hello!"
                ty "who are you?"
                ty "that's my butt and not my face."
                ty "so... i can't see you."
                y "i'm the avatar."
                ty "oh."
                ty "that's... um."
                ty "....."
                ty "are you angry with me for trying to capture you?"
                y "maybe I should be, but some stuff happens in the future that makes it impossible for me to dislike you."
                ty "....really?"
                y "Yeah, it'll be awesome."
                y "By the way, you really should start a tavern when you return to the fire nation."
                ty "You think I could?"
                ty "It sorta has been a life long dream of mine, but I never figured I could."
                ty "especially while i'm working with azula."
                y "don't worry about it - you've got what it takes."
                ty "Well, okay! thanks!"
                y "So..."
                y "What are you doing here?"
                ty "...I got stuck."
                y "How? Why?"
                ty "um... speaking of azula..."
                y "what?"
                ty "well... she threw me in here!"
                ty "I don't know why!"
                ty "I was just flirting with a boy and she got so mad!"
                y "maybe she was jealous."
                ty "of me? but she's perfect!"
                y "okay..."
                y "and she put you in this hole?"
                ty "no, i escaped my cell..."
                ty "I just overheard something about a treasure which was supposed to be around here."
                ty "I couldn't get into a room which looked promising, so I tried taking an alternative route."
                ty "I took off my clothes to fit through here, but..."
                y "you got stuck anyway."
                ty "yeah..."
                ty "Can you get me out?"
                y "I don't know... earthbending seems kinda dangerous."
                y "I don't want you to go \"splat\" if something goes wrong."
                ty "Then what should we do?"
                menu:
                    "I'll have to think it over":
                        y "I'm not sure, but I'll find a way."
                        y "I'll return when I've thought of something."
                        ty "Okay, please don't take too long."
                    "Suggest sperm":

                        call b3l_spermontysass from _call_b3l_spermontysass_1
            "Exit":
                pass


    hide expression "bk3/tylee/footjob/bg_wall.jpg"
    jump love_bk3_maze_start





label love_unique_room75:
    $ sp_item_xpos = 453
    $ sp_item_ypos = 261
    $ sp_item_width = 127
    $ sp_item_height = 226

    if current_room.sp_content == 0:
        show expression "maze/maze2_nagaeyes.png"
        show expression "maze/black.png"
        show text "{color=#fff}Your eyes slowly adjust to the darkness as you carefully walk down the stairs.{/color}"
        $ renpy.pause()
        hide text
        $ renpy.pause(0.05)
        show ty_idle_ff_nude:
            xzoom -1
        hide expression "maze/black.png"
        with Dissolve(2.0)

        y "Aaah!!!!" with hpunch
        ty "Don't be scared, silly!"
        ty "It's just a statue."
        y "It reminds me of someone I've had a lot of trouble with."
        ty "You know someone with snakehair?!"
        y "No, it's just... forget it."
        y "It's a long story."
        ty "talking about stories... there's one about this statue."
        ty "Wanna hear it?"
        y "Is it going to take long?"
        ty "No, it's just pieces I caught while eavesdropping."
        menu:
            "Sure, let's hear it.":
                ty "Once there were two sisters..."
                ty "one insane and loving, the other calculating and jealous."
                ty "They desired the same thing..."
                y "What kind of thing?"
                ty " I don't know."
                y "It's a guy, right?"
                y "They wanted the same guy."
                ty "I don't know."
                ty "Anyway... but only both could have it."
                y "That... doesn't make any sense."
                ty "I'm just telling you what I heard."
                ty "Neither wanted the other to have what they themselves desired."
                ty "And thus they are fated to never get what they want."
                y "So what does that have to do with the snake chick?"
                ty "She's one of the sisters."
                y "which one? And why would anyone look up to either?"
                ty "No idea, but it's said she could take away nightmares and such."
                y "She's a nightmare to look at!"
                y "Except for the boobies."
                y "Hey, maybe they wanted legs!"
                y "And they're one of those conjoined twins from the hips up!"
                y "So if one got legs the other would have them too! "
                y "It all makes sense now!!!"
                ty "You think so?"
                y "nah, just kidding."
                y "Who knows what's true or false about hearsay legends."
                y "The only thing I'm interested in is treasure... so..."
            "Nope":

                y "Nah, I'm just here for the gold."

        y "Where's the gold?"
        ty "I can't see any!"
        ty "The eyes look to be gems though."
        ty "That's nice."
        ty "One for you, one for me!"
        y "Hmm... well, it's easier to carry than a statue made of gold so it's fine, I guess."
        ty "Could you take them? I'd do it myself, but I'm slippery with your sperm."
        y "No prob."
        "you carefully pry the eyes loose."
        hide expression "maze/maze2_nagaeyes.png"
        "Just as you're about to give one of them to Tylee..."
        show expression "maze/maze2_nagaeyes1.png" with dissolve
        "{i}Thanksss avatar, you may keep the eyes."
        hide expression "maze/maze2_nagaeyes1.png" with dissolve
        y "...Fuuuuuuuuck me."
        ty "......"
        ty "...I didn't hear that. "
        ty "I didn't hear that, i didn't see that, and I'm never going to mention or admit this ever happened."
        ty "You can keep they eyes! Both of them. I'm outta here!"
        y "but..."
        ty "Thanks for freeing me!"
        ty "I'll visit you again sometime later!"
        hide ty_idle_ff_nude with dissolve
        "Tylee dashes up the stairs taking 5 steps at a time."
        y "I don't really feel like hanging around here either."
        y "oh, wait, what's this?"
        play sound "audio/win2.mp3"
        $ obsidian +=2
        "you found 2 obsidian!"
        y "fun."

        $ current_room.north = 70
        $ current_room.sp_content = 1
        $ love_naga_eyes = True

    call screen love_maze_directions



label love_unique_room75_activate:
    "test"
    call screen love_maze_directions





label love_unique_room76:
    if previous_room == room77:
        show expression "maze/black.png"
        show text "{color=#fff}After a long time you find your way back to the tunnels under lake laogai."
        $ renpy.pause()
        hide text
        hide expression "maze/black.png" with Dissolve(1.5)

    call screen love_maze_directions





label love_unique_room77:



    if room78.sp_content == 4:
        if current_room.maze_enemy == True:
            jump love_bk3_start_the_fight



        if room81.sp_content == 3 and room81.maze_enemy == False and room76.sp_content == 0:
            show expression "bk3_fight/dailee_1.png" with Dissolve(1.5)
            dl "I just arrived here to start my shift when I saw the guy I had to relieve lying collapsed on the floor."
            dl "That guy is a dick so I don't mind you fucking him up, but you know I can't just let you leave right?"

            menu:
                "Really? Why not?":
                    y "...Really? Why not?"
                    y "You can just pretend you didn't see me and that other guy I punched out will have to take all responsibility."
                    dl "Mmmmmhh, I hadn't thought of it like that... "
                    dl "Okay fine, I won't try and stop you."
                    dl "But I'm going to earthbend this part shut so you can't sneak up on me when it's my shift."
                    y "Go for it dude."
                    y "I have all I wanted from here."
                    $ room77.north = -1
                    $ room76.north = -1
                "Just try and stop me":
                    $ previous_room = room25
                    $ current_room.maze_enemy = True
                    hide expression "bk3_fight/dailee_1.png"
                    $ room76.sp_content = 1
                    $ current_room.maze_enemy = True
                    jump love_unique_room77



        elif room81.sp_content == 0:
            show expression "bk3_fight/dailee_1.png" with hpunch
            $ room81.sp_content = 4
            dl "I thought I heard something!"
            dl "Don't think you can get out of here unharmed!!"
            dl "You'll pay for messing up my afternoon nap!"
            y "Oh reeeeally?"

            menu:
                "Freeze":
                    $ room81.sp_item = False
                    hide expression "bk3_fight/dailee_1.png"
                    show expression "maze/love_guard_frozen.png":
                        rotate 0 xalign 0.5 yalign 0.5
                    with Dissolve(1.5)

                    $ renpy.pause(1.0)
                    show expression "maze/love_guard_frozen.png":
                        parallel:
                            xpos 500
                            linear 1.0 xpos 1000
                        parallel:
                            ypos 360
                            linear 1.0 ypos 920 rotate 90

                    $ renpy.pause (2.0)
                    play sound "audio/thud.mp3"
                    y "...ooops..."
                "It's clobbering time!":


                    $ previous_room = room25
                    $ current_room.maze_enemy = True
                    hide expression "bk3_fight/dailee_1.png"
                    $ current_room.sp_item = True
                    $ current_room.maze_enemy = True
                    jump love_unique_room77




    if previous_room == room76:
        show expression "maze/black.png"
        show text "{color=#fff}Time passes as you search your way through the dark corridors."
        $ renpy.pause()
        if current_room.visit == 1:
            show text "{color=#fff}Even though you have a map you still have to backtrack a few times in this maze within a maze."
            $ renpy.pause()
            show text "{color=#fff}Suddenly you hear the sound of a woman softly crying up ahead."
            $ renpy.pause()
        hide text
        hide expression "maze/black.png" with Dissolve(1.5)

    call screen love_maze_directions



label love_unique_room78:
    $ sp_item_xpos = 390
    $ sp_item_ypos = 1
    $ sp_item_width = 220
    $ sp_item_height = 370
    call screen love_maze_directions

label love_unique_room78_activate:
    show expression "maze/love_dung_cell.jpg"
    if current_room.sp_content == 4:
        show expression "maze/love_dung_jd3.png"

    if current_room.sp_content == 0:
        $ current_room.sp_content = 1
        "The dark shadows make it hard to see anything."
        menu:
            "whisper Joodee's name":

                y "Joodee, are you in there?"
                y "It's me, the avatar."
            "exit":
                call screen love_maze_directions  

        "You hear something scrape along the floor and approach the cell door."
        "Joodee slowly crawls towards the bars and presses herself against them."
        show expression "maze/love_dung_jd1.png"
        jd " H-have you come to... to get me out of here?"

        y "Fuck yeah, I did!"
        y "Consider it my apology for treating your titties so roughly a while ago."

        jd "It's safer if you just forget about me."
        jd "The walls are reinforced with iron and the..."
        "she unvoluntarily shudders."
        jd "the guard is dangerous..."
        y "Hey, I'm not exactly a pushover either."
        y "Don't worry about it."

        if room77.sp_content == 1 and room81.sp_content != 3:
            y "I already met him and got the key."
            y "Hold on."
            show expression "maze/love_dung_cry.png"
            jd "*sob...*"
            jd "thank you for not forgetting about me..."
            jd "I was afraid I'd never get out of here."
            y "Don't cry."
            hide expression "maze/love_dung_cry.png" with Dissolve(1.5)

        elif room81.sp_content >= 3 and room81.maze_enemy == False:
            y "I already took care of that guy."
            y "When he wakes up, his body will hurt so much he'll wish he stayed unconscious."
            y "I'll get you out of here in no time."
            show expression "maze/love_dung_cry.png"
            jd "*sob...*"
            jd "thank you for not forgetting about me..."
            jd "I was afraid I'd spend the rest of my life here."

            jump love_bk3_maze_start
        else:
            y "I'll go pay him a visit."
            y "You'll be out of here in no time."
            show expression "maze/love_dung_cry.png"
            jd "*sob...*"
            jd "thank you for not forgetting about me..."
            jd "I was certain I'd never see sunlight again."
            jump love_bk3_maze_start




    if current_room.sp_content == 1:

        if room77.sp_content == 0:
            y "Hey, Joodee."
            y "You still there?"
            show expression "maze/love_dung_jd1.png" with dissolve
            jd "Do... do you have they key?"
            y "Ah shit, I knew I had forgotten something."
            y "Back in a jiffy."
            jump love_bk3_maze_start
        else:

            show expression "maze/love_dung_jd1.png"
            y "I'll have you out of here in a second."
            y "Move a bit back so I can open this."
            hide expression "maze/love_dung_jd1.png"
            with Dissolve(1.5)
            "You stick the key in the lock and turn it."
            play sound "audio/door4.mp3"
            "the cell opens with a creaking sound."
            show expression "maze/love_dung_jd2.png" with Dissolve(1.5)
            $ current_room.special_touch = "maze/love_dung_bopen.png"
            $ current_room.sp_content = 2


    if current_room.sp_content == 2:
        show expression "maze/love_dung_jd2.png"
        "the cell is open, but Joodee is too weak to travel a long way."
        y "I have to give her a healing potion."

        if bk3_lifepotions > 0:
            menu:
                "Make her drink a lifepotion.":
                    $ bk3_lifepotions -= 1
                    $ current_room.sp_content = 3
                    y "Here, drink this."
                    y "It'll give you strength."
                    "You carefully make her drink the potion."
                    y "There you go."
                "Hold on a bit longer Joodee.":

                    pass
        else:
            y "Shit, I'm all out of lifepotions."

    if current_room.sp_content == 3:
        y "Okay, time for us to get out of here."
        $ current_room.sp_content = 4
        $ jd_free = True
        y "if we get separated, go to the hospital in the village."
        jump love_bk3_maze_start


    call screen love_maze_directions  



label love_unique_room79:
    $ sp_item_xpos = 390
    $ sp_item_ypos = 1
    $ sp_item_width = 220
    $ sp_item_height = 370
    call screen love_maze_directions

label love_unique_room79_activate:
    show expression im.Flip("maze/love_dung_cell.jpg", horizontal=True)
    if room78.sp_content == 0:
        menu:
            "whisper Joodee's name":
                y "Joodee, are you in there?"
                y "It's me, the avatar."
                "there's no reply."
            "exit":
                pass

    "There's nothing here."
    call screen love_maze_directions 


label love_unique_room80:
    $ sp_item_xpos = 390
    $ sp_item_ypos = 1
    $ sp_item_width = 220
    $ sp_item_height = 370

    call screen love_maze_directions


label love_unique_room80_activate:
    show expression "maze/love_dung_cell.jpg"
    if room78.sp_content == 0:
        menu:
            "whisper Joodee's name":
                y "Joodee, are you in there?"
                y "It's me, the avatar."
                "there's no reply."
            "exit":
                pass

    "There's... nothing here."

    call screen love_maze_directions 


label love_unique_room81:

    if current_room.sp_content == 4:
        $ current_room.sp_item = False

    if current_room.sp_content == 0:
        $ sp_item_xpos = 700
        $ sp_item_ypos = 1
        $ sp_item_width = 320
        $ sp_item_height = 710

    if current_room.sp_content == 1 and current_room.maze_enemy == True:
        $ sp_item_xpos = 700
        $ sp_item_ypos = 1
        $ sp_item_width = 320
        $ sp_item_height = 710



    if current_room.sp_content == 1 or current_room.sp_content == 3:
        if current_room.maze_enemy == False:
            $ current_room.sp_content = 3

            if room77.sp_content == 0:
                $ sp_item_xpos = 700
                $ sp_item_ypos = 320
                $ sp_item_width = 80
                $ sp_item_height = 80
            else:
                $ current_room.sp_item = False

    if room77.sp_content == 0:
        show expression "maze/love_dung_key.png"

    if current_room.maze_enemy == True:
        show expression "maze/love_guard_dailee_0.png"
        $ renpy.pause(1.0)
        hide expression "maze/love_guard_dailee_0.png"
        show expression "maze/love_guard_dailee.png"

        "dailee" "Back for more bitch?!"
        hide expression "maze/love_guard_dailee.png"
        jump love_bk3_start_the_fight

    if current_room.visit ==1:
        $ current_room.visit +=1
        show expression "maze/love_guard_dailee_0.png"
        show text "{color=#fff}{size=+50}zzzzz{/size}":
            xpos 1000 ypos 40
            linear 6.0 xpos 0
            repeat
        y "A dai lee agent!"
        y "Is... he asleep standing up?"
        y "If there's a key to the cells somewhere it has to be here..."
        y "Maybe I should feel in his pockets..."



    elif current_room.sp_content <= 0:
        if current_room.sp_content == 0 and current_room.maze_enemy == False:
            show expression "maze/love_guard_dailee_0.png"
            show text "{color=#fff}{size=+50}zzzzz{/size}":
                xpos 1000 ypos 40
                linear 6.0 xpos 0
                repeat


    call screen love_maze_directions

label love_unique_room81_activate:
    if current_room.sp_content <= 1:
        "you carefully approach him when..."
        dl "Ahh... no!"
        dl "...no mommy..."
        dl "That's my special place..."
        menu:
            "Don't touch him":
                call screen love_maze_directions 
            "Try his left pocket":

                if room77.sp_content != 1:
                    $ room77.sp_content = 1
                    hide text with dissolve
                    "You found a key!"
                    jump love_bk3_maze_start
                else:
                    "it's empty."
                    call screen love_maze_directions 
            "try his right pocket":

                $ current_room.maze_enemy = True
                $ current_room.sp_content = 1
                hide text
                hide expression "maze/love_guard_dailee_0.png"
                show expression "maze/love_guard_dailee.png"
                dl "waaahaht??" with hpunch
                dl "What the fuck?"
                dl "Who are you?"
                dl "What are you doing here?"
                y "Uuuuuh..."
                dl "You're going down!"
                hide expression "maze/love_guard_dailee.png"
                jump love_bk3_start_the_fight
            "Hit him in his solar plexus":

                y "I guess it's a bit below the belt to K.O. a sleeping person, but he probably deserves it."
                hide expression "maze/love_guard_dailee_0.png"
                show expression "maze/love_guard_dailee.png":
                    ypos 80
                    linear 2.0 ypos 720
                hide text
                show text "{color=#fff}{size=+100}UGH!!{/size}" with hpunch
                $ current_room.sp_content = 1
                $ current_room.maze_enemy = False
                hide text with Dissolve(2.0)
                play sound "audio/thud.mp3"
                "The Dai Lee agent crumples into an unconscious heap."
                jump love_bk3_maze_start
            "Wake him up":

                $ current_room.maze_enemy = True
                $ current_room.sp_content = 1
                y "Hey you!"
                hide expression "maze/love_guard_dailee_0.png"
                show expression "maze/love_guard_dailee.png"
                hide text
                dl "Huh... wha...?" with hpunch
                y "The fuck did you do to JooDee, you dick?!"
                dl "Oh, it's the avatar."
                dl "I don't mind telling you."
                dl "Since her hypno treatments were compromised she's useless to us as a sleeper agent and we locked her up here."
                y "Why lock her up?"
                y "Why not instead just not use her anymore?"
                dl "We can still have some fun with her this way."
                dl "I made the dumb cow slap her own tits so hard she started to cry."
                dl "That was fun."
                dl "I think I'm gonna do it again later."
                dl "And that's just the start of what I'll do to her."
                hide expression "maze/love_guard_dailee.png"
                show expression "bk3_fight/dailee_1.png"
                y "....."
                dl "Don't worry... I'll put you in a cell right next to her so you can enjoy the show."
                y "No you won't."
                y "you're wrong on both counts, because I'm going to hurt you."
                y "I'm going to hurt you real bad... right now."
                dl "You don't scare me."
                y "Enjoy that state of idiocy while it lasts."
                hide expression "bk3_fight/dailee_1.png"
                jump love_bk3_start_the_fight



    if current_room.sp_content > 1:
        "you grab the key from the table."
        "You also notice a small bottle standing hidden within the shadows as you reach for the key."
        play sound "audio/win2.mp3"
        "You found a lifepotion!"
        $ bk3_lifepotions += 1
        $ current_room.sp_item = False
        hide expression "maze/love_dung_key.png"
        $ room77.sp_content = 1
        call screen love_maze_directions 






label love_unique_room82:

    if room69.west == -1:

        if previous_room.rname == 'room63':
            show expression "maze/black.png"
            show text "{color=#fff}You search your way through the tunnels for what feels like hours."
            $ current_room = room83
            $ renpy.pause()
            hide text
            hide expression "maze/black.png"
            jump love_bk3_maze_start

        elif previous_room.rname == 'room83':
            y "This is where I came from."
            y "I need to find those girls first."
            $ current_room = room83
            jump love_bk3_maze_start

    elif bk3_rescue_idiots >= 3:
        if previous_room.rname == 'room63':
            show expression "maze/black.png"
            show text "{color=#fff}You wander through the tunnels for what feels like hours."
            $ current_room = room83
            $ renpy.pause()
            hide text
            jump love_bk3_maze_start


        elif previous_room.rname == 'room83':
            show expression "maze/black.png"
            show text "{color=#fff}You wander through the tunnels until you finally find your way back to the cell."
            $ current_room = room63
            $ renpy.pause()
            hide text
            jump love_bk3_maze_start





    call screen love_maze_directions


label love_unique_room85:

    if current_room.visit == 1 and current_room.west == -1:
        y "hmmm... a big fat wall."
        y "I don't think I can get through this by force."
        $ room87.sp_content = 1



    call screen love_maze_directions



label love_unique_room87:

    if current_room.visit == 1:

        image bmole_dig:
            "maze/bmole_sidedig_3.png"
            0.3
            "maze/bmole_sidedig_4.png"
            0.3
            repeat

        image bmole_dig_up:
            "maze/badgermole_dig.png"
            0.3
            im.Flip("maze/badgermole_dig.png", horizontal=True )
            0.3
            repeat

        image bmole_digging = LiveComposite(
            (1000, 720),
            (0, 0), "maze/bmole_sidedig_2.png",
            (0, 0), "bmole_dig",
            )



        y "A dead end."


    if current_room.sp_content == 1:
        "A light tremor shakes the floor beneath you." with hpunch
        show expression "maze/bmole_sidedig_1.png" with Dissolve(1.5)
        y "AAAh! the fuck!?"


        hide expression "maze/bmole_sidedig_1.png"
        show bmole_digging:
            linear 18.0 xpos -400

        show expression "maze/bmole_sidedig_0.png"
        with Dissolve(1.5)
        $ current_room.maze_bg = "maze/maze2_wns.jpg"
        y "Hey, it's digging a new tunnel, filling up the one it came from..."
        y "Guess I'll follow him?"

        $ current_room.sp_content = 2
        hide bmole_digging
        hide expression "maze/bmole_sidedig_0.png"
        show expression im.Flip("maze/maze2_easthole.png",horizontal=True)
        with Dissolve(1.5)

        $ current_room.special_touch = im.Flip("maze/maze2_easthole.png",horizontal=True)



        $ current_room.west = 88
        $ current_room.sp_content = 3


    call screen love_maze_directions



label love_unique_room88:

    if current_room.visit == 1:
        show bmole_digging:
            xpos -200
            linear 11.0 xpos -300

        y "hmmm... you're actually using earthbending to dig these tunnels, aren't you?!"
        y "I feel like I can pick up a few things from just watching you."
        y "Hey! Come to think of it, wasn't that big hairy thing on the posters I had also supposed to fly?"
        y "Is he using airbending to do that?"
        hide bmole_digging with Dissolve(1.5)

    call screen love_maze_directions


label love_unique_room89:

    if current_room.visit == 1:
        show bmole_digging:
            xpos -200
            linear 5.0 xpos -300

        y "I guess you can't talk, but you didn't happen to stumble upon two lost girls?"

        hide bmole_digging with Dissolve(1.5)
        y "Hey, wait for me!"

    call screen love_maze_directions



label love_unique_room90:

    if current_room.visit == 1:
        show bmole_dig_up:
            ypos 0

        $ room69.west = 97
        y "They're wearing masks and... let's just say they don't think too hard or deep about things..."
        y "Ah fuck! For all I know it's luring me to it's nest to feed me to its young!"
        y "I'm going to make a furcoat out of you if it turns out you ate those girls!"
        y "I know this girl called Nami, who knows someone else and..."

        hide bmole_dig_up
        show bmole_dig_up:
            ypos 0
            linear 3.0 ypos 0 xpos 230 xzoom 0.5 yzoom 0.3 alpha 0.0
        menu:
            "Call it names.":
                y "I don't why ajala is afraid of you guys."
                y "My cat has caught bigger rats than you."
                show expression "bk3_fight/badgermole_1.png":
                    xzoom 0.2 yzoom 0.2 xpos 400 ypos 1
                    linear 1.0 xzoom 1.0 yzoom 1.0 xpos 0 ypos 0
                y "crap..."
                hide expression "bk3_fight/badgermole_1.png"
                jump love_bk3_start_the_fight
            "Just keep following it.":
                pass


        hide bmole_digging with Dissolve(1.5)


    call screen love_maze_directions



label love_unique_room92:
    $ sp_item_xpos = 700
    $ sp_item_ypos = 112
    $ sp_item_width = 240
    $ sp_item_height = 510

    if current_room.sp_item == True:
        "you hear some odd sounds... like muffled crying."

    call screen love_maze_directions



label love_unique_room92_activate:
    y "Sounds like it's coming from behind here."
    $ renpy.pause(1.0)
    y "Okay, I think I can earthbend this wall without bringing the ceiling down on me."
    y "and perhaps the entire contents of lake Laogai... "
    menu:
        "let's... not do this just yet":
            pass
        "Fuck it. I can do this!":
            $ current_room.east = 93
            $ current_room.sp_item = False
            $ current_room.special_touch2 = "maze/maze2_easthole.png"
            play sound "audio/rock_crumble.mp3"
            show expression "maze/maze2_easthole.png" with Dissolve(1.5)
            jump love_bk3_maze_start
    call screen love_maze_directions




label love_unique_room93:
    $ sp_item_xpos = 402
    $ sp_item_ypos = 47
    $ sp_item_width = 140
    $ sp_item_height = 160

    if current_room.visit == 1:
        $ bk3_rescue_idiots = 3
        show expression "maze/love_guards_found.png"
        bk3_g1_b "AAAhh!! It's you!!!" with hpunch
        bk3_g2_b "Oh my god, you have noooo idea how happy we are to see you!"
        bk3_g1_b "We managed to survive on a bag of doritos I had with me, but I just ate the last one!"
        bk3_g2_b "And we had no dip sauce, so you know how desperate we were!"
        bk3_g2_b "Let me tell you what happened."


        menu:
            "Keep listening":
                bk3_g2_b "So we were just hanging around when we heard this strange rumbling sound."
                bk3_g2_b "I knew I wasn't that hungry, but before I could ask Krystal anything the wall caved in!"
                bk3_g1_b "I thought we were going to die right then and there!"
                bk3_g2_b "There was this badgermole sticking his nose through the hole and he had this stupid look on his face."
                bk3_g2_b "You know, that really punchable kind."
                bk3_g2_b "He turned around and was gone again in a flash."
                bk3_g1_b "And... well we were bored out of our skulls, so decided to investigate."
                y "Weren't you afraid of it?"
                bk3_g2_b "Nah, they're mostly harmless unless you really pick a fight with them."
                bk3_g1_b "Ajala is really afraid of them though."
                bk3_g2_b "Anyway, we discovered this weird turning wheel in the shape of two snakes trying to eat each other."
                bk3_g2_b "We played around with it, turning it left and right and all of a sudden this wall came down!"
                bk3_g1_b "We heard a click when we turned the wheel and after four of those... BAM! No way out!"
                bk3_g1_b "Freaky shit man!!"
                bk3_g2_b "We couldn't go anywhere anymore."
                bk3_g2_b "Stuck as fuck!"
                bk3_g1_b "We turned it some more, but couldn't get four clicks anymore."
                bk3_g1_b "So we decided to wait it out and hope for a rescue party to find us."
                bk3_g2_b "We figured you'd show up since you've been saving chicks."
                bk3_g1_b "We even thought about taking off our clothes since that seems to be one of the requirements to be rescued by you."
                bk3_g2_b "Yeah, but then we got into an argument about why the fuck two snakes would be eating eachother and forgot all about it."
                bk3_g2_b "You should take a look at it yourself. It's right behind us."
                bk3_g1_b "so... eh... did you talk to ajala? She's not going to punish us is she?"
            "Cut her off.":


                y "I think it's better for you to get out of here first and go find Ajala."
                bk3_g2_b "Why?"


        y "Ajala asked me to go look for you after you disappeared."
        y "She's more worried than angry so I don't think you're in too much trouble."
        bk3_g1_b "That's good to hear."
        bk3_g2_b "Thanks man."
        bk3_g1_b "We won't forget this."
        y "Do you think you can find your way back by yourself?"
        bk3_g2_b "Only one way to find out!! See you later Avatar!"
        hide expression "maze/love_guards_found.png" with Dissolve(1.5)
        y "Hm. Now what were they saying about a turning wheel?"






    call screen love_maze_directions

label love_unique_room93_activate:

    show expression "maze/snakepuzzle_bg.jpg"

    if current_room.sp_content == 0:

        $ current_room.sp_content = 1
        $ snakedoor_eyes = 0
        $ snakedoor_rotation = 0
        $ snakedoor_turns = 1
        $ snakedoor_sequence_1 = [0,90,180,270,360]
        $ snakedoor_sequence_2 = [0,90,180,270,180]

        image snakedoor_ring = LiveComposite(
            (400, 400),
            (0, 0), "maze/snakedoor_ring.png",
            (0, 0), ConditionSwitch( 
                "snakedoor_eyes == 0", "transparent.png", 
                "snakedoor_eyes == 1", "maze/snakedoor_eyes_1.png", 
                "snakedoor_eyes == 2", "maze/snakedoor_eyes_2.png", 
                "snakedoor_eyes == 4", "transparent.png",)
            )

        show snakedoor_ring:
            xpos 240 ypos 20
            linear 0.5 rotate snakedoor_rotation

        y "So this is what those two were messing with."
        y "Two snakes trying to eat eachother? That seems... ineffective."
        y "Maybe I should give it a try."

    if current_room.sp_content <= 2:
        show snakedoor_ring:
            xpos 240 ypos 20 rotate snakedoor_rotation

        while snakedoor_turns < 5:


            call screen snakedoor_puzzle_love          

            show snakedoor_ring:
                xpos 240 ypos 20
                linear 0.5 rotate snakedoor_rotation


            if current_room.sp_content == 1:
                if snakedoor_sequence_1[snakedoor_turns] == snakedoor_rotation:
                    $ snakedoor_turns = snakedoor_turns + 1
                    show text "{color=#fff}click":
                        xpos 400 ypos 100
                    pause 0.5
                    hide text
                    with dissolve
                    $ renpy.pause(0.4)
                else:

                    $ snakedoor_turns = 1

            if current_room.sp_content == 2:
                if snakedoor_sequence_2[snakedoor_turns] == snakedoor_rotation:
                    $ snakedoor_turns = snakedoor_turns + 1
                    show text "{color=#fff}click":
                        xpos 400 ypos 100
                    pause 0.5
                    hide text
                    with dissolve
                    $ renpy.pause(0.4)
                else:

                    $ snakedoor_turns = 1


            if snakedoor_turns > 4:

                show snakedoor_ring with hpunch

                if current_room.sp_content == 1:
                    $ snakedoor_eyes = 1
                    "One eye is now open."
                    y "It felt like something heavy moved."
                    $ current_room.sp_content = 2
                    $ room92.west = 94
                    $ room92.special_touch= "maze/maze2_westhole.png"
                    $ snakedoor_rotation = 0
                    $ snakedoor_turns = 1
                    jump love_bk3_maze_start

                elif current_room.sp_content == 2:
                    $ snakedoor_eyes = 2
                    "Both eyes are now open."
                    y "It felt like something heavy moved."
                    $ current_room.sp_content = 3
                    $ room85.west = 93
                    $ room93.east = 85
                    $ room85.special_touch = im.Flip("maze/sp_e_sunkenwall.png",horizontal = True)
                    $ room93.special_touch = "maze/sp_e_sunkenwall.png"


    if current_room.sp_content == 3:
        show snakedoor_ring:
            xpos 240 ypos 20 rotate snakedoor_rotation

        y "Hmmm... I can't turn it any further, it's stuck."




    jump love_bk3_maze_start

    screen snakedoor_puzzle_love:
        vbox xalign 0.9 yalign 0.4:
            textbutton _("turn right") action [SetVariable("snakedoor_rotation", snakedoor_rotation + 90), Return]
            textbutton _("turn left") action [SetVariable("snakedoor_rotation", snakedoor_rotation - 90), Return]
            textbutton _("reset") action [SetVariable("snakedoor_rotation", 0), SetVariable("snakedoor_turns", 1), Return]
            textbutton _("exit") action [ Jump("love_bk3_maze_start")]



label love_unique_room94:

    if current_room.visit == 1 and love_naga_claw == False:

        y "Ahhh!! Snaketitties!!!"
        y "Fuck no... not another statue..."
        y "Why the hell would they make two of 'em?"
        y "One wasn't enough?"
        y "well, i'm definitely not gonna touch this one."
        y "....."
        y "i wonder why there's no head?"
        y "Well whatever."
        y "Let's get outta here while I can."
        "{i}...It'sssss her!!{/i}" with hpunch
        y "...Who said that...?"
        y "Ah fuck, who am I kidding."
        y "That amount of s's is enough of a giveaway."
        "{i}NOOO! Not herrr! {/i}"
        y "Okay then who are you?"
        "{i}a ssshadow... a footprint... the ssshedding of a ssskin... perhapsssss more...{/i}"
        "{i}When you took the ssstonesss... {/i}"
        "{i}latched on... neccesssity... sssurvival...{/i}"
        "{i}We need to talk, but I am weak here...{/i}"
        y "So... there's another snake lady?"
        "{i}yesss...."
        y "why is the head of this statue smashed?"
        "{i}sssecretsss..."
        y "does this have something to do with the snake puzzle?"
        y "the two snakes eating each other?"
        "{i}yesss... locked in a ssstruggle... to consssume..."
        y "and one of them is you?"
        "{i}....."
        "{i} Tooo tired. We shall ssspeak...in your dreamsss when I'm ready."
        "...."
        y "Hello?! ......You still there?"
        y "Creepy snake dreams in the night?"
        y "Now there's something to look forward to..."
        y "Getting the fuck out of here."
        $ love_begin_snake_dream = True

    elif current_room.visit == 1 and love_naga_battle == False:
        y "Ahhh!! Snaketitties!!!"
        y "Fuck no... not another statue..."
        y "Why the hell would they make two of 'em?"
        y "One wasn't enough?"
        y "well, i'm definitely not gonna touch this one."
        y "....."
        y "i wonder why there's no head?"
        y "Well whatever."
        y "Let's get outta here while I can."
        "{i}...It'sssss her!!{/i}" with hpunch
        y "...Who said that...?"
        y "Ah fuck, who am I kidding."
        y "That amount of s's is enough of a giveaway."
        "{i}NOOO! Not herrr! {/i}"
        y "Okay then who are you?"
        "{i}a ssshadow... a footprint... the ssshedding of a ssskin... perhapsssss more...{/i}"
        "{i}When you took the ssstonesss... {/i}"
        "{i}latched on... neccesssity... sssurvival...{/i}"
        "{i}We need to talk, but I am weak here...{/i}"
        y "So... there's another snake lady?"
        "{i}yesss...."
        y "why is the head of this statue smashed?"
        "{i}sssecretsss..."
        y "does this have something to do with the snake puzzle?"
        y "the two snakes eating each other?"
        "{i}yesss... locked in a ssstruggle... to consssume..."
        y "and one of them is you?"
        "{i}....."
        "{i} Tooo tired. We shall ssspeak...in your dreamsss when I'm ready."
        "...."
        y "Hello?! ......You still there?"
        y "Creepy snake dreams in the night?"
        y "Now there's something to look forward to..."
        y "Getting the fuck out of here."

    elif current_room.visit == 1:

        y "Ahhh!! Snaketitties!!!"
        y "Fuck no... not another statue..."
        y "Why the hell would they make two of 'em?"
        y "One wasn't enough?"
        y "well, i'm definitely not gonna touch this one."
        y "....."
        y "i wonder why there's no head?"
        y "Well whatever."
        y "Let's get outta here while I can."

    call screen love_maze_directions



label love_unique_room96:

    if bk3_rescue_idiots < 3:
        y "I feel like I missed something important."
        y "Let's stick around til I figure out what."
        $ current_room = room95
        jump love_bk3_maze_start
    call screen love_maze_directions







label love_unique_room98:

    if current_room.maze_enemy == True:
        jump love_bk3_start_the_fight

    if current_room.visit == 1:

        show expression "maze/love_ajala_delight.png"
        ct "Hey!"
        y "Oh, uh, hey Ajala."
        y "What are you doing here?"
        ct "I thought long and hard, and decided to help you!"
        y "That's great!"
        show expression "maze/love_ajala_delight.png":
            xzoom -1.0 xpos 1000
        ct "By capturing you and putting you in a cell."
        y "Ehh... what?"
        ct "It'll be a super nice cell!"
        ct "And we can spend our time together there."
        ct "Long Feng will never stop trying to get rid of you using all kinds of underhanded methods!"
        ct "But I can keep you safe. I promise!"
        y "uh... thank you? But no thanks."
        y "I can take care of my own."
        y "And I'll take care of Long Feng too if he stands in my way"
        hide expression "maze/love_ajala_delight.png"
        show expression "maze/love_ajala_delight.png"
        with Dissolve(1.5)
        ct "I'd like to believe that, but just for your sake I'll have to prevent you from going any further."
        ct "I really wish it wouldn't come down to this."
        menu:
            "\"i'm sorry, but I love toph\"":
                y "It may be a little twisted, but I do appreciate your concern."
                y "Sorry Ajala, I can't run away from this."
                y "Toph is somewhere down there and I'll tear through anything to get to her."
                ct "I... I understand, but I have to at least try."
                ct "I also have someone I want to protect."
                y "Let's do this."
                $ ajala_choice = 'fightyou'
                hide expression "maze/love_ajala_delight.png" with Dissolve(1.5)
                $ current_room.maze_enemy = True
                jump love_bk3_start_the_fight
            "\"i really like you, help me out?\"":
                $ ajala_choice = 'helpyou'
                y "I have to do this Ajala."
                y "People are depending on me."
                y "If we fight, you might win, but if I win and proceed, I'll be at an disadvantage during my next fight."
                y "Do you want that?"
                ct "...no..."
                y "Than help me by stepping aside."
                ct "Aaaah... fine."
                ct "the things we do for love..."
                ct "Please be careful."
                "she gives you a quick kiss before leaving."
                play sound "audio/kiss.mp3"

                show expression "bk3/toph/walk/pink.png" with dissolve
                hide expression "bk3/toph/walk/pink.png" with dissolve



                hide expression "maze/love_ajala_delight.png" with Dissolve(1.5)
    else:

        pass

    call screen love_maze_directions



label love_unique_room108:
    $ sp_item_xpos = 556
    $ sp_item_ypos = 2
    $ sp_item_width = 210
    $ sp_item_height = 243

    if current_room.north == 112:
        show expression "maze/love_door1_open.png"
    else:
        show expression "maze/love_door1_closed.png"

    call screen love_maze_directions


label love_unique_room108_activate:

    if current_room.sp_content == 0:
        $ current_room.sp_content = 1
        y "There's a small piece of paper stuck to the doorpost."
        show text "Subject tries to bribe guards with sexual favors... but bites! Be careful.":
            ypos 350
        $ renpy.pause()
        hide text

    if room108.north == -1:


        $ current_room.special_touch2 = "maze/love_door1_open.png"
        $ current_room.north = 112
        $ current_room.visit -= 1
        jump love_bk3_maze_start

    elif room108.north != -1:

        $ current_room.special_touch2 = "maze/love_door1_closed.png"
        $ current_room.north = -1
        $ current_room.visit -= 1
        jump love_bk3_maze_start



    call screen love_maze_directions




label love_unique_room109:
    if current_room.maze_enemy == True:
        show expression "maze/love_guardmob.jpg"
        show expression "maze/black50.png"
        jump love_bk3_start_the_fight


    if current_room.sp_content ==  0 and current_room.visit == 1:
        $ current_room.maze_enemy = True
        show expression "maze/love_guardmob.jpg":
            alpha 0.0
        show expression "bk3/longfeng/idle_body.png":
            xpos 400
            linear 2.0 xpos 0
        lf "Avatar."
        lf "This is as far as you go."
        y "Long Feng! Just the person I wanted to talk to."
        y "Where's Toph?!"
        lf "You're mistaken, avatar."
        lf "You're not here to talk, you're here to listen."
        lf "You'll leave the earth kingdom and won't come back."
        lf "In return, nothing... harmful... will happen to the girl."
        y "You piece of shit."
        y "Trying to burn down my house with me in it was one thing, but this... "
        y "You're going to tell me where Toph is."
        y "With or without teeth."
        y "Your choice."
        lf "Such a shame."
        lf "I was hoping we could do things the easy way."
        "long feng snaps his fingers..."
        show expression "maze/love_guardmob.jpg":
            linear 2.0 alpha 1.0
        "...and a small army of Dai Lee agents pour into the tunnel."
        y "Oh shit..."

        show expression "bk3/longfeng/idle_body.png"
        with Dissolve(1.5)
        lf "You might be strong, but having numbers is it's own kind of strong."
        y "All that does is buy you some extra time."
        y "Give me Toph or I'll make you regret it for the rest of your short life."
        lf "We'll see."
        lf "I'll start you off with just one opponent."
        $ current_room.sp_content = 1
        hide expression "bk3/longfeng/idle_body.png" with Dissolve(1.5)

        jump love_bk3_start_the_fight

    if current_room.sp_content == 1:



        show expression "maze/love_guardmob.jpg"
        show expression "maze/black50.png"
        show expression "bk3/longfeng/idle_body.png"

        lf "Congratulations avatar, you've won."
        lf "Now let's see you hold your own against four opponents at the same time."


        if ajala_choice == 'fightyou':


            lf "Who knows... maybe that girl of yours will still be alive when you're done."
            y "..."
            y "....what the fuck did you say...?"
            y "{size=+25}.... what... the fuck... did YOU SAY?!?!{/size}" with hpunch
            "A sudden rage evelops you."
            "It feels like someone is pushing a hot poker into your brain..."
            "and something deep within you goes... *click*"
            show expression "maze/avastate.png" with Dissolve(1.5)
            show expression "maze/avastate_glow.png" with Dissolve(1.5)
            show expression "maze/avastate_glow.png":
                linear 1.0 alpha 1.0
                linear 1.0 alpha 0.5
                repeat
            y "I don't know what's happening... "
            y "but I feel tremendous raw power... surging through me."
            hide expression "maze/love_guardmob.jpg"
            hide expression "bk3/longfeng/idle_body.png"
            show expression "maze/love_guardmobsmall.png"
            with Dissolve(1.5)
            "The Dai Lee agents take one look at your glowing eyes and shuffle backwards as one entity."
            show expression "maze/love_guard_dailee.png"
            with Dissolve(1.5)
            dl "Pffff, you think some fluorescent shit is going to scare me?"
            dl "I'm going to beat you up, and afterwards, me and my buddies will gangbang that shrimp."
            dl "Like we should've done from the start. "
            dl "Right guys?!?"
            "...nobody answers..."

            hide expression "maze/love_guard_dailee.png"
            show expression "maze/love_daicrunch1.png"
            play sound "audio/skeleton_crunch.mp3" 

            $ renpy.pause(1.3)

            hide expression "maze/love_daicrunch1.png"
            show expression "maze/love_daicrunch2.png"
            play sound "audio/skeleton_crunch.mp3" 


            $ renpy.pause(0.3)
            hide expression "maze/love_daicrunch2.png"
            show expression "maze/love_daicrunch2.png":
                ypos 0 xpos 0
                linear 1.6 ypos 1300 xpos 0

            y "{color=#66FFFF}{size=+15}WHERE IS SHE, LONG FENG?!?{/color}"
            "Long Feng, hiding within the group of Dai Lee agents, gets forcefully pushed to the front."
            dl "Let him deal with this. "
            dl "I didn't sign up for this shit."
            show expression "bk3/longfeng/idle_body.png"
            show expression "bk3/longfeng/idle_scared.png"
            with Dissolve(1.5)
            lf "She's up ahead! Perfectly healthy and not in any danger!!"
            y "{color=#66FFFF}{size=+15}GOOD, BECAUSE IF SHE ISN'T....{/color}"
            y "{color=#66FFFF}{size=+15}ALL OF YOU WILL DIE.{/color}"
            "The Dai Lee agents watch in horror at the hat lying in front of them. "
            y "{color=#66FFFF}{size=+15}NOW PUT THIS PIECE OF SHIT IN A CELL.{/color}"
            y "{color=#66FFFF}{size=+15}PRAY I WON'T FIND REASON TO VISIT YOU, LONG FENG.{/color}"
            "The Dai Lee agents quickly put Long feng in shackles and silently (but quickly) leave."

            hide expression "maze/love_guardmobsmall.png"
            hide expression "bk3/longfeng/idle_body.png"
            hide expression "maze/love_guardmob.jpg"
            hide expression "bk3/longfeng/idle_scared.png"
            with Dissolve(1.5)
            hide expression "maze/black50.png"
            hide expression "maze/avastate.png"
            hide expression "maze/avastate_glow.png"
            with Dissolve(1.5)
            "And just as quickly as the power surged through you, it leaves you again, making you feel exhausted."
            y "Did, did I just enter the avatar state...??"
            y "Oh fuck... that was crazy..."
            y "Whatever. "
            y "Gotta find Toph!"

            $ current_room.sp_content = 3
        else:


            show expression "bk3/longfeng/idle_body.png":
                xzoom -1.0
            bk3_g1 "Wait! Stop!" with hpunch
            lf "Some of Ajala's guards? What is it?"
            bk3_g1 "Oh fuck... *pant...* gimme a minute... *pant...*"
            bk3_g1 "I came here running and now it feels like someone is stabbing me in the side with a knife."
            bk3_g1 "Is... is that normal?"
            bk3_g1 "You don't think I broke something do you?"
            lf "......"
            bk3_g2 "Sorry sir!"
            bk3_g2 "We got an important message."
            lf "...yes?"

            bk3_g1 "Oh yeah... uhhh... have you guys noticed anything strange lately?"
            lf "No, explain yourself."
            bk3_g2 "What she's trying to say is something horrible happened!"
            bk3_g1 "Yeah! Jessica got fat! But for real this time!"
            bk3_g1 "We didn't fuck around with her scale, she gained like 40 pounds!"
            bk3_g2 "I'm actually starting to worry."
            bk3_g2 "What if she gets too fat to walk through these tunnels?"
            bk3_g2 "Because if we can't pass her we'll be stuck!"
            bk3_g1 "As fuck!"
            lf "What the hell is wrong with you two?!"
            lf "I'll have to talk to Ajala about this after all is done here."
            bk3_g1 "Speaking of Ajala, there she is!"
            "Ajala comes running towards Long Feng, followed by a bunch of other female guards."
            show expression "maze/love_ajala_delight.png"
            ct "Sorry I'm late!"
            y "Damn it Ajala!"
            y "I thought we had agreed you'd step aside..."
            lf "Step aside...? "
            lf "We'll need to have a talk after this has been settled, Ajala."
            lf "Now be gone."
            lf "Your help isn't needed here."
            lf "Return to your post and take your guards with you."
            ct "Sir..."
            ct "Shut the fuck up."
            ct "I was talking to the avatar."
            show expression "bk3/longfeng/idle_angry.png":
                xzoom -1
            lf "Wha...{i}WHAT{/i}?!?!"

            ct "Sorry I'm late, Aang!"
            ct "I needed to round up some of my strongest girls."
            y "Are... are you saying you're here to help me out?!"
            ct "Of course!"
            ct "You just go free your girlfriend."
            hide expression "maze/love_ajala_delight.png"
            show expression "maze/love_ajala_angry.png"
            with Dissolve(1.5)
            ct "and we'll take care of the riffraff here."
            y "Wow, thanks Ajala, that's awesome."
            ct "Sure, now get going!"
            ct "Your girl should be up ahead."
            lf "You dare betray me?!"
            lf "You will regret this!"
            lf "When I say a certain phrase you'll have no choice but to obey."
            ct "No I won't. "
            ct "I've removed any hypnotic influence you had over me."
            ct "A certain someone inspired me."
            bk3_g1 "We helped with that!"
            bk3_g2 "And we totally didn't implement a new command only we know about!"
            bk3_g1 "Let's just say, we're getting a raise this month!! Wooohooo!!"

            hide expression "maze/love_ajala_angry.png"
            hide expression "bk3/longfeng/idle_body.png"
            hide expression "bk3/longfeng/idle_angry.png"
            with Dissolve(1.5)
            bk3_g1 "Enough talk! Let's fight!"
            bk3_g1 "Boys against the girls!!! The spice must flowww!!! SPOOON!!!!"
            bk3_g2 "What are you doing?"
            bk3_g1 "I'm trying out battle cries. "
            bk3_g2 "OH... In that case... I WILL MAKE BLOOD RAIN DOWN ON YOU!!"
            $ renpy.sound.play("audio/barfight.mp3", loop=True, fadein=2.0)
            scene black with Dissolve(1.5)
            show text "{color=#fff}A crazy fight breaks out between the Dai Lee agents and Ajala's guards.{/color}"
            $ renpy.pause()
            show text "{color=#fff}You deflect a fist, sidestep a kick and jump away from a bodyblow.{/color}"
            $ renpy.pause()
            hide text
            bk3_g2 "{size=+10}GIVE THEM NOTHING! AND TAKE FROM THEM EVERYTHING!!"
            bk3_g1 "Is that some sort of movie reference? Also... {size=+10}SPOOOOOOON!!!!!"

            show expression "maze/love_guard_dailee.png":
                alpha 0.0 ypos 500
                linear 1.0 alpha 1.0 ypos 0
            with vpunch

            dl "Avatar!! Save me!"
            show expression "maze/love_guard_dailee.png":
                alpha 1.0
                linear 3.0 alpha 0.0 xpos -1500
            dl "*Gurgle*!"
            y "These people are fuckin crazy!!!"
            y "Let's find Toph while Ajala and her guards keep the Dai lee agents busy."
            hide expression "maze/love_guardmob.jpg"
            hide expression "maze/black50.png"
            with Dissolve(1.5)
            $ current_room.sp_content = 2
            $ current_room.south = -1

    if current_room.sp_content == 2 and room110.visit >= 1:
        $ current_room.sp_content = 4
        y "Where's everyone? "
        y "Just a few minutes ago there was a major battle going on here..."
        bk3_g1 "Hey!"
        bk3_g1 "So... Ajala asked me to tell you what happened."
        bk3_g2 "We whooped ass is what happened!"
        bk3_g1 "Actually Ajala got Long Feng in a headlock when he tried to sneak away."
        bk3_g1 "When she threatened to break his neck the Dai Lee agents didn't feel like fighting anymore."
        bk3_g2 "She's putting him somewhere in a secret cell right now."
        y "That's... great. Thanks!"
        bk3_g1 "oh!"
        bk3_g1 "ajala wants you to visit her later."
        y "ajala wants me to visit her later?"
        bk3_g1 "yes, ajala wants you to vist her later."
        bk3_g1 "Well, we still got stuff to do so talk to you later!"
        t "Wow... you really made a difference down here..."
        y "That's what the avatar does!"





    call screen love_maze_directions




label love_unique_room110:

    if current_room.visit == 1:
        if ajala_choice == 'helpyou':
            stop sound fadeout 7.0
        $ bk3love_freetoph = 4
        "you see a big iron box standing in the middle of the room."
        y "Toph! Are you in there? Are you okay??!!"
        t "Yeah! Just give me a minute. I'll be out soon."
        play sound "audio/thud.mp3"
        show expression "maze/cage_toph_batter1.png" with hpunch
        y "Oh wow... you're doing that with your bare hands?! How?"
        t "Iron has some small earth particles in it and I can bend those."
        play sound "audio/thud.mp3"
        show expression "maze/cage_toph_batter2.png" with hpunch
        y "That's crazy impressive."
        y "How long have you been able to do this?!"
        t "I figured it out just now."
        t "I got this surge of energy when I heard you and just felt like nothing could stop me."
        play sound "audio/thud.mp3"
        show expression "maze/cage_toph_batter3.png" with hpunch
        y "Okay, I'm convinced you can get out by yourself, but would you mind me giving a hand?"
        t "Sure... *pant...* if you really feel like it."
        "together you and toph break her out of the iron contraption."
        hide expression "maze/cage_toph_batter1.png"
        hide expression "maze/cage_toph_batter2.png"
        hide expression "maze/cage_toph_batter3.png"
        play sound "audio/metal_tearing.mp3"
        show expression "maze/cage_toph_batter4.png"
        show expression "maze/cage_toph_inside.png"
        with Dissolve(1.5)
        t "Open sesame!"
        y "Toph... I'm really happy to see you're alright."
        hide expression "maze/cage_toph_inside.png"
        show expression "maze/love_toph_hug.png"
        with Dissolve(1.5)
        t "Shut up and gimme a big hug!"
        show expression "maze/black.png" with Dissolve(1.5)
        show text "{color=#fff}Toph literally jumps in your arms and refuses to let go for the next five minutes.{/color}"
        $ renpy.pause()
        hide text
        hide expression "maze/black.png"
        hide expression "maze/love_toph_hug.png"
        with Dissolve(1.5)
        t "Okay, what happened?"
        t "I heard a lot of ruckus, but that's it."
        "You quickly fill her in."
        if ajala_choice == 'fightyou':
            t "Really? You went all avatar state? I'd like to see that!"
            y "It was more of an accident than anything else. "
            y "I have no idea how to do it again."
        else:
            t "Hmmm, I'm happy Ajala helped you out. "
            t "Let's see if we can help her."
            t "I hope she left some for us!"
        t "Oh I just remembered! We'll have to free appa!"
        if room111.visit >= 1:
            y "No worries, that has been dealt with."
            t "Great!"
        else:
            y "You certain he's here?"
            t "Yeah, I heard him not long ago."
        t "I'll go ahead. See you later!"

        $ love_toph_freed = True

        $ room109.south = 105
        $ current_room.special_touch2 = "maze/cage_toph_batter4.png"

    call screen love_maze_directions



label love_unique_room111:

    if current_room.visit == 1:
        show expression "maze/appa_body.png"
        show expression "maze/appa_chains_on.png"
        show expression "maze/appa_head1.png"
        y "AAAAhh!!! What the fuck!"
        hide expression "maze/appa_head1.png"
        play sound "audio/deepgrowl.mp3"
        show expression "maze/appa_head2.png":
            linear 2.0 ypos 30
            linear 1.0 ypos 0
            repeat
        y "Oh it's you! "
        y "Ap-something! "
        y "I recognize you from the posters..."
        y "Wow. That really feels like an eternity ago."
        y "Do you recognize me, boy?"
        play sound "audio/deepgrowl.mp3"
        hide expression "maze/appa_head2.png"
        show expression "maze/appa_head3.png":
            linear 2.0 ypos 30
            linear 1.0 ypos 0
            repeat
        y "Yeah, yeah just don't get your spit all over me."
        y "So you're supposed to be able to fly? You're a big one."
        y "How did they get you in here?"
        y "And more importantly, how do I get you out?"
        "You're eyes track the room and you notice the high ceiling."
        show expression "maze/appa_bg_hatch.jpg":
            xpos 0 ypos -280
        with Dissolve(1.5)
        show expression "maze/appa_bg_hatch.jpg":
            xpos 0 ypos -280
            linear 4.0 ypos 0
        $ renpy.pause()
        y "Some sort of hatch up there?"
        y "No idea how they open but... some earthbending... and..."
        show expression "maze/appa_bg_hatch.jpg":
            xpos 0 ypos 0
        play sound "audio/stonegrind.mp3"
        show expression "maze/appa_bg_air.png" with Dissolve(1.5)
        y "Presto!"
        hide expression "maze/appa_bg_hatch.jpg"
        hide expression "maze/appa_bg_air.png"
        with Dissolve(1.5)
        y "Fly away!... Oh shit, right."
        play sound "audio/shackles_gone.mp3"
        hide expression "maze/appa_chains_on.png"
        show expression "maze/appa_chains_off.png"
        $ current_room.special_touch = "maze/appa_chains_off.png"
        y "Well, come on. Get out of here! We'll meet up later."
        $ love_appa_freed = True
    call appa_tug from _call_appa_tug

    call screen love_maze_directions



label love_unique_room112:
    if current_room.sp_content == 0:
        show expression "maze/jet_shackled.png"
        show expression "maze/sp_twotorches_3.png":
            xpos -650 ypos -160
        show expression "maze/black.png":
            alpha 0.8

        "The room is dark but you can see a dark silhouette sitting against a wall."
        "stranger" "What the fuck do you want from me this time?!"
        y "I'm pretty certain I'm not who you think I am."
        "stranger" "I don't care. Fuck you."

        menu:
            "Fuck you too(leave)":
                pass
            "Create some light":
                "You shoot a small fireball and light the torch hanging from the wall."

                hide expression "maze/sp_twotorches_3.png"
                show sp_double_torches:
                    xpos -650 ypos -160
                hide expression "maze/black.png"
                "stranger" "A firebender? Here? Wait..."
                show expression "maze/jet_surprise.png" with hpunch
                "stranger" "Aang?! I can't believe it!"
                "stranger" "You've come to rescue me!"
                y "Shit, I was hoping for a girl with a deep and husky voice, but you seem to be a guy."
                "stranger" "Can you get me out of these shackles?"
                y "Eeeeh... I guess?"
                hide expression "maze/jet_surprise.png"
                "stranger" "I see... You want a sexual favor from me first?"
                "stranger" "That's okay, Aang! I'll suck you off right here and now!"
                y "NO! Nonononono!"
                y "(who the fuck is this guy?)"

                "Suddenly an idea pops into your mind."
                y "I just have to be careful you aren't an imposter so..."
                y "Tell me about yourself so I can verify you're the real one."
                "stranger" "You certainly have become a lot more distrusting...."
                "jet" "I'm Jet."
                "jet" "I used to be the leader of a gang called the Freedom Fighters, but disbanded after we met you, Katara and Sokka."
                "jet" "Together with Longshot and Smellerbee I came to Ba sing Se to start a new life, but that kinda didn't work out."
                "jet" "And now I'm here, abducted by some weirdos."

                if room30.sp_content >= 1:
                    y "Ohhh! Now I remember. Smellerbee mentioned you. She has been looking for you."
                    "jet" "She must be really worried."
                    y "Yeah, I guess. But now you can tell her you're still alive."
                y "You convinced me. I'll open up those shackles. After that, you're on your own."
                y "Go find your friends."
                "you fidget with the locks on the shackles and manage to get them off."
                play sound "audio/shackles_gone.mp3"
                hide expression "maze/jet_shackled.png"
                show expression "maze/jet_stand.png" with Dissolve(1.5)
                "jet" "Thanks man. I owe you."
                "jet" "You certain you don't want me to give you a quick blowie?"
                y "I'm positive."
                $ current_room.sp_content = 1
                "jet" "Your loss. Thanks man!"
                hide expression "maze/jet_stand.png" with Dissolve(1.5)
                "Jet winks and throws you a handkiss while walking out of the room."
                y "*shiver*"
                $ love_jet_freed = True

    if current_room.sp_content == 1:
        show sp_double_torches:
            xpos -650 ypos -160


    call screen love_maze_directions




label love_unique_room113:
    $ sp_item_xpos = 450
    $ sp_item_ypos = 80
    $ sp_item_width = 150
    $ sp_item_height = 250

    if current_room.visit == 1:
        show expression "maze/sokka_idle.png"
        sok "Hey man, awesome of you to drop by."
        sok "Just don't tell Katara about this."
        y "No worries man. I wouldn't rat on you."
        sok "Yeah, us handsome folk need to look out for each other."
        sok "All these player haters hatin' on our style, you know"
        y "Eh... yeah."
        sok "Okay my man, make yourself comfortable."
        sok "Mi casa es su casa. I'm out for a bit."
        sok "Hunting for them steamy dirty panties..."
        y "That's... that's... really..."
        sok "I sometimes wear them as a hat!!"
        sok "See ya!!"
        hide expression "maze/sokka_idle.png" with Dissolve(1.5)
        show expression "maze/sokka_idle.png" with hpunch
        sok "You're welcome to peruse my pornloves, but some stupid crab shredded and ate pretty much all of them."
        y "Aaaawhh."
        sok "Yeah I only got my vintage pornlove left."
        sok "Just make sure you don't take a right here."
        sok "That crab is a total cunt."
        hide expression "maze/sokka_idle.png" with Dissolve(1.5)
        y "Sokka's a really weird and super perverted guy... "
        y "I like him."



    call screen love_maze_directions


label love_unique_room113_activate:

    "You flip through the little material still left."


    menu:
        "Look through the vintage pornlove":
            show expression "bk3/pornlove_old/pornlove_old_1.jpg"
            $ renpy.pause()
            show expression "bk3/pornlove_old/pornlove_old_2.jpg"
            $ renpy.pause()
            show expression "bk3/pornlove_old/pornlove_old_3.jpg"
            $ renpy.pause()
            jump love_bk3_maze_start
        "Look at the pages you saved from the crab" if room114.sp_content == 2:
            show expression "maze/pornlove_meng/meng1.jpg"
            $ renpy.pause()
            show expression "maze/pornlove_meng/meng2.jpg"
            $ renpy.pause()
            jump love_bk3_maze_start
        "exit":
            pass



    call screen love_maze_directions





label love_unique_room114:

    if current_room.sp_content == 1 and current_room.maze_enemy == True:
        jump love_maze_enemies
    if current_room.visit == 1:
        $ current_room.east = -1
        $ renpy.pause(1.0)

        show expression "bk3_fight/sewercrab.png":
            xzoom 0.1 yzoom 0.1 xpos 1000 alpha 0.1 ypos 200
            linear 3.0 xzoom 1.0 yzoom 1.0 xpos 0 alpha 1.0 ypos 0
        "You see a rugged crab shuffling forward."

        y "So you're the bastard who shredded Sokka's pornloves?"
        y "You're... really big..."
        y "Too bad I've got nothing to gain from it or I'd make crab soup out of you."
        "You could swear the crab is sizing you up."
        "It's as if he's telling you: \"I'll let you go this time but next time, imma gonna fuck you up.\""
        $ current_room.sp_content = 1

    if current_room.maze_enemy == False and current_room.sp_content ==1:
        "you find a couple of pages of a pornlove which weren't shredded."
        y "I guess I'll stick these in with Sokka's one surviving pornlove."
        $ current_room.east = 115
        $ current_room.sp_content = 2


    call screen love_maze_directions













label love_backtotherealworld:
    $ love_ajala_visited = False
    $ bk3_day = False
    $ current_room = roomlist[1]
    $ previous_room = roomlist[1]
    jump love_bk3_village_background













label june_headlock_scene:

    ju "Go ahead."
    show tojl_tug
    ju "mmmm... yeah pump that cock..."
    show ctc
    pause
    hide ctc
    y "Hnngg..."
    ju "....."
    ju "Oh, watch out for Ajala if you keep running through these tunnels."
    y "NNgg... who's that?"
    ju "She's the head of the guards here and has biceps as thick as her thighs."
    ju "I've heard some scary stories about her"
    y "I'll keep it... in mind."
    y "By...the...way... I'm looking for... someone to run... my tavern."
    y "There's hard liquor... tips.."
    ju "Certainly sounds like something I'd enjoy."
    ju "I'll think about it."
    y "Good..."
    y "Gimme some dirty talk to speed things up here."
    ju "...look at that disgusting, smelly cock..."
    y "hey..."
    ju "just pumping recklessly right in my face..."
    ju "I bet you'd stick that in a girl without washing it and not even feel ashamed!"
    y "Go on!"
    ju "You filthy pig! You're the worst! You're a disgrace to all decency!"
    ju "Gonna blast your sperm all over my face!?"
    ju "Do it!"
    y "Wraaah!!"
    hide tojl_tug
    play sound "audio/splurt2.ogg"
    show expression "bk3/june/headlock/tug1.png":
        xpos 545 ypos 390
    show expression "bk3/june/headlock/sperm1.png":
    ju "mmm..."
    y "fuck you, bitch!"
    play sound "audio/splurt1.ogg"
    show expression "bk3/june/headlock/sperm2.png":
    hide expression "bk3/june/headlock/sperm1.png"
    ju "i... wow. well done."
    ju "i'm impressed... i've never seen such a big load before."
    ju "you... are something special."
    show ctc
    pause
    hide ctc
    y "Fuck that was nice."
    y "You have a great face for cumming on!"
    ju "....thank you, i suppose."
    ju "i hope you feel happily sated... this was certainly new for me."
    hide expression "bk3/june/headlock/tug1.png" with dissolve
    hide expression "bk3/june/headlock/sperm2.png" with Dissolve(1.5)
    return




label meangirls_maze_licking:


    show tomg tomg01 with Dissolve(1.5)
    show ctc
    pause
    hide ctc
    y "Ready to lick yourself some cock girls?"
    if meangirls_number_oflicks == 0:
        "girls" "... do we really have to?"
        y "only if you want the chance to leave."
        y "So, I'll ask again."
        y "Are you ready to lick my dick like your freedom depends on it?"

    "girls" "....yes...."

    y "Good."
    show tomg tomg02 with dissolve
    show ctc
    pause
    hide ctc
    if meangirls_number_oflicks == 0:
        y "Since this is your first time I'll explain how this works."
        y "This is my cock, and you're going to lick the tip until I tell you to stop..."
        y "and only when I tell you to stop."
    elif meangirls_number_oflicks == 1:
        y "You've done this before, so you should already know how this goes down..."
        y "but i'll repeat it anyway."
        y "just so we're all clear."
        y "You're going ot lick the tip of my dick until I say stop."
        y "No matter how smelly or gross it is, you'll keep going."
    elif meangirls_number_oflicks >= 1:
        y "How many times have we done this before?"
        y "I think [meangirls_number_oflicks] times, right?"
        y "Time to show me how much you've improved."

    show tomg tomg03 with Dissolve(1.5)
    show ctc
    pause
    hide ctc
    if meangirls_number_oflicks == 0:
        y "Well? What are you waiting for?"
        y "Lick it. It's not going to lick itself."
        y "...if only it could...."
    elif meangirls_number_oflicks >= 0:
        y "Same smelly cock as last time girls."
        y "No need to hesitate."
        y "Come on, dig in."

    show tomg tomg100
    show ctc
    pause
    hide ctc
    if meangirls_number_oflicks == 0:
        y "Hmmmm... yeah..."
        y "...you guys are really bad at this, but that awkwardness has it's own charm."
        y "I'm going to give you codenames. "
        y "I think I'll adopt the power ranger way of naming you."
        y "The color of those pompoms, or whatever's in your hair, will be your new name."
        y "So White, Red, and Pink."
        "The girls keep licking you at a steady pace with awkward little laps."
        "It's very clear they have no idea what they're doing."

    "*schlurp, schlurp, schlurp*"
    y "Mmmmm, yeah... keep licking the tip, red."
    y "Short little laps."
    y "Yeah, that's it."
    y "Focus on the edge, white and pink."
    y "It might take the three of you working in tandem to get a halfway decent erection..."
    y "...but I can see you're trying your best."
    "The girls keep licking you until you finally start feeling the urge to unload upon them."

    y "Hnng... about to cum..."
    y "turn your faces towards me!"
    show tomg tomg04
    show tomg tomg01 with Dissolve(1.5)
    show ctc
    pause
    hide ctc
    y "Red gets it first!"
    play sound "audio/splurt2.ogg"
    show expression "bk3/meangirls/maze/sperm1.png"
    y "Pink is up next!"
    play sound "audio/splurt1.ogg"
    show expression "bk3/meangirls/maze/sperm2.png"
    y "And white can have the leftovers."
    play sound "audio/splurt2.ogg"
    show expression "bk3/meangirls/maze/sperm3.png"
    show ctc
    pause
    hide ctc
    y "AAaaaah, that was nice."
    hide expression "bk3/meangirls/maze/sperm1.png"
    hide expression "bk3/meangirls/maze/sperm2.png"
    hide expression "bk3/meangirls/maze/sperm3.png"
    hide tomg
    $ meangirls_number_oflicks += 1
    return


label jin_had_mazesex:

    if b3love_dildo_gotit == True:
        menu:
            "Want me to use my dick?":
                jin "Yes! Give me dick!!"
            "Or a dildo?":

                jin "I don't care what it is, just put it in me!"
                jump jin_had_dildo_sex

    $ b3love_jin_mazesex = 1
    $ tojc_face = 'lookdown'
    show tojc tojc100
    jin "Yes! that's it!"
    $ tojc_face = 'lusty'
    jin "Hmmmm, finally!!"
    show ctc
    pause
    hide ctc
    jin "You have no idea how long I've been wanting this!!"
    jin "Don't hold back! Slam that fucker in me!"
    show tojc tojc101
    jin "Ahh!"
    show ctc
    pause
    hide ctc
    y "I'm going to cum!!"
    jin "CUM INSIDE ME!!"
    y "...can do!"
    hide tojc
    show tojc tojc08
    show tojc tojc09 with Dissolve(1.5)
    play sound "audio/gltch2b.mp3"
    $ renpy.pause(0.6)
    play sound "audio/gltch2b.mp3"        
    show expression "bk3/jin/shackles/big_sperm_inside.png":
        alpha 0.0
        linear 2.0 alpha 1.0
    jin "fuuck!!"
    jin "you're drowning my womb in sperm!"
    show ctc
    pause
    hide ctc
    hide expression "bk3/jin/shackles/big_sperm_inside.png"
    show tojc tojc10
    with Dissolve(1.5)
    jin "Aaaaah! That was great."
    jin "thank you!"
    show ctc
    pause
    hide ctc
    $ tojc_face = 'neutral'
    return

label jin_had_dildo_sex:
    show tojc tojc11
    $ b3love_jin_mazesex = 2
    $ tojc_face = 'lookdown'
    jin "Aaaaah! That's great."
    $ tojc_face = 'lusty'
    show tojc tojc12
    jin "Aawh, i don't know what you're shoving in me but it feels fantastic!"
    show tojc tojc13

    jin "....nhhh!"
    show tojc tojc14 with hpunch
    show tojc tojc15 with Dissolve(1.5)
    jin "Ooooh... fuck, that was great."
    $ tojc_face = 'neutral'
    return

label ajala_wonfight_1:
    show expression "ebackgrounds/bg_tunnelwall.jpg"
    show totv totv01
    ct "oooh... what happened?"
    y "I beat your ass."
    y "Fair and square, no less."
    y "And guess what?"
    menu:
        "I'm not going to fuck you":
            ct "But you promised to..."
            y "No, I didn't."
            y "See ya!"
            hide totv
            jump love_bk3_maze_start
        "I'm going to collect my reward now":

            $ b3love_ajala_mazevag = 1
            pass

    jump ajala_wonfight_1_cont

label ajala_wonfight_1_cont:
    y "Now spread those legs of yours."
    y "I wanna see my prize."

    show totv totv02 with Dissolve(1.5)
    $ renpy.pause()
    y "That's a nice looking pussy."
    y "People can say what they want about your body, but your tits and puss are as fine as any other out there."
    y "I'm going to pound that so hard you'll be walking bowlegged for the rest of the week."

    show totv totv03 with Dissolve(1.5)
    bk3_ajavag "....prove it."
    y "Oh, I will."
    y "You're a big girl, so I'll jump right in."


    show totv totv04

    bk3_ajavag "Hnnnnngh..."
    y "Oh, you're surprisingly tight."
    y "You training your pussy muscles too?"
    y "Doesn't matter."
    y "I'll tear down that soft fortress of yours..."
    y "one thrust at a time."
    $ renpy.pause()
    bk3_ajavag "You... ah... could go a little slower..."
    y "You want me to slow down?"
    bk3_ajavag "ah... just a... little..."

    y "You're absolutely right... I could do that."

    show totv totv03
    show totv_fuck_fast
    bk3_ajavag1 "{size=+4}AAAAAAh!!!"
    y "Or I could slam it in as hard as I can!"
    bk3_ajavag2 "Ah!! Sooo deep!"
    y "Come on, girl!"
    y "If you can't take my ramrod at full thrust, nobody can."
    y "Take one for the team!"
    y "And then another one! and another one!"
    $ renpy.pause()
    bk3_ajavag2 "Fuck.... fuck.... fuck...."
    y "I'm getting close!"
    y "veerry close..."
    bk3_ajavag2 "Ah! D-don't stop!"
    bk3_ajavag2 "Keep slamming it in!"
    y "Did I awaken your taste for cock?"
    bk3_ajavag2 "Yes! I need it! I need it badly!"

    hide totv_fuck_fast
    show totv_fuck_fastest
    y "Ready or not... here I cum!"


    menu:
        "cum inside":
            hide totv_fuck_fastest
            $ b3love_ajala_mazevag = 2
            show totv totv06 with Dissolve(1.5)

            show totv totv07 with Dissolve(1.5)

            y "Sharing is caring."
            $ renpy.pause(0.8)
            play sound "audio/gltch.mp3"
            $ renpy.pause(0.8)
            play sound "audio/gltch2.mp3"            
            show expression "bk3/ajala/vag/cum_xray.png" with Dissolve(3.0)
            $ renpy.pause()

            hide expression "bk3/ajala/vag/cum_xray.png"
            show totv totv08
            with Dissolve(1.5)
            y "Man, I came buckets!"


            show totv totv09
            show expression "bk3/ajala/vag/sperm_outside_4.png"
            with Dissolve(1.5)

            show expression "bk3/ajala/vag/sperm_outside_5.png" behind totv:
                xpos 550 ypos 550
                linear 3.0 ypos 590 xpos 530
            $ renpy.pause(3.5)
            y "Looks like she's out cold!"
        "cum outside":


            hide totv_fuck_fastest
            show totv totv02 with Dissolve(1.5)
            y "Here's some moisturizer for your skin."
            play sound "audio/gltch.mp3"
            show expression "bk3/ajala/vag/sperm_outside_1.png" with Dissolve(1.5)
            play sound "audio/gltch2.mp3"
            show expression "bk3/ajala/vag/sperm_outside_2.png" with Dissolve(1.5)
            play sound "audio/gltch2b.mp3"
            show expression "bk3/ajala/vag/sperm_outside_3.png" with Dissolve(1.5)
            y "That felt awesome."
            y "We absolutely need to do this again sometime."






    $ renpy.pause()
    y "Just enjoy the afterglow, you luscious muscle maiden."
    y "Fuck you next time."

    scene black with Dissolve(2.0)
    jump love_bk3_maze_start

label ajala_wonfight_10:
    show expression "ebackgrounds/bg_tunnelwall.jpg"
    show totv totv01
    ct "oooh..."
    y "okay, you're gonna tell me how to make that equipment undo hypnosis."
    ct "fine..."
    ct "what you do is..."
    show black with dissolve
    "ajala tells you how you'll have to change the equipment to get it to fully undo hypnosis."
    hide black with dissolve
    y "and that will do it?"
    ct "that will do it..."
    y "great!"
    y "and now..."
    $ jd_break_hypno = 2
    menu:
        "i'm gonna fuck you":
            y "I'm gonna slam that pussy."
            $ b3love_ajala_mazevag = 1
            jump ajala_wonfight_1_cont
        "i'm gonna leave":

            y "i'll see you later."
            ct "hhrgh..."
            scene black with dissolve
            jump love_bk3_maze_start

label b3l_spermontysass:
    y "I have an idea. You're pretty limber right?"
    ty "I'm the limberest!"
    y "Okay, that's good to hear."
    y "raise your legs."
    ty "Like this?"
    show totf totf03 with Dissolve(1.5)
    show ctc
    pause
    hide ctc
    y "yeah... that's nice... like really, really nice..."
    y "Now try and hold my dick with your feet."
    ty "Your dick? What good will that do?"
    y "I'm going to cum all over your ass."
    y "The sperm will act as a lubricant."
    y "Together with a good push I should be able to force it in."
    ty "It?"
    y "I mean I'll force you in... the room."
    y "Not my dick in you... unless you want to?"
    y "Sorry, I'm feeling distracted with that full moon right in front of me."
    ty "Let's focus on freeing me first."
    ty "Do you really think you have enough sperm?"
    y "That's why I need your feet.... To milk out every drop I have."
    ty "Oooh! Good idea, I'll give it my best!"

    show totf totf04 with dissolve
    show totf totf05 with Dissolve(1.5)
    y "Start massaging it until I cum."
    ty "Aye aye!"
    show totf totf06
    show ctc
    pause
    hide ctc
    y "Hnng..."
    ty "Is it working?"
    y "...yeah, keep going. "
    y "let's talk about that treasure while you keep using your feet."
    y "What sort of treasure are we talking here?"
    ty "it's supposed to be some sort of super old statue of a spirit which people used to worship."
    ty "I don't really expect to find it, but I overheard some guards here and since I had nothing better to do.."
    y "What's valuable about a statue?"
    ty "I don't know, but maybe it's made out of gold?"
    y "Now that's interesting!"
    y "Wanna partner up?"
    ty "And share the treasure? I dunno...."
    y "Moving a golden statue by yourself would be hard."
    y "besides, you're still stuck here and I'm helping you get out."
    ty "Okay, sure! We'll split any treasure we'll find!"
    y "If you speed things up, we can start looking for it."
    show totf totf07
    ty "Okidoki!"
    y "FFuuuuuuck!"
    show ctc
    pause
    hide ctc
    y "HNNNNNNGGG!!!"
    y "Spread those legs!"
    y "I'm about to unload all over that silky white ass of yours!!"

    show totf totf04 with dissolve
    $ renpy.pause(1.0)
    play sound "audio/splurt2.ogg"
    show expression "bk3/tylee/footjob/sperm1.png"
    with flash
    $ renpy.pause()
    play sound "audio/splurt2.ogg"
    show expression "bk3/tylee/footjob/sperm2.png"
    with flash
    $ renpy.pause()
    play sound "audio/splurt2.ogg"
    show expression "bk3/tylee/footjob/sperm3.png"
    with flash
    $ renpy.pause()
    show totf totf03
    show ctc
    pause
    hide ctc
    y "This should be enough to do the trick."
    y "I'm going to give you a good shove."

    ty "Okidoki!"
    scene black with Dissolve(1.5)
    play sound "audio/thud.mp3"
    show text "{color=#fff}With a hard push you manage to force Ty Lee's voluptuous thighs through the hole in the wall{/color}."
    $ renpy.pause()
    hide text
    $ current_room.sp_content = 2
    return

label love_find_ajala:

    if love_toph_freed:
        jump ajala_dunk
    else:

        scene black
        scene dark_tunnel
        show tomc tomc04
        with dissolve
        ct "what are you doing here?"
        y "i was hoping for some... uh... 1-v-1 time."
        show tomc tomc07 with dissolve
        ct "you're gonna have to earn it!"
        y "fine, let's do this thing."
        show tomc tomc05 with dissolve
        ct "come on!"
        $ ajala_jd_hypno_fight = True
        hide tomc
        jump love_bk3_start_the_fight


label appa_tug:

    show expression "maze/appa_body.png"
    hide expression "maze/appa_head3.png"
    show expression "maze/appa_head2.png":
        linear 2.0 ypos 10
        linear 1.0 ypos 0
        repeat


    if current_room.sp_content == 0:
        show toxi toxi09a:
            xpos 300
            linear 2.0 xpos 0

        $ current_room.sp_content = 1
        "ropegirl" "Hey Fluffy, I'm back!"
        "ropegirl" "Did you miss me? I'm wearing your favorite outfit!"
        "ropegirl" "We can do all sorts of sick shit today!"
        "The girl hasn't noticed you apparently."
        menu:
            "Tap on her shoulder":
                pass
            "Keep listening":
                "ropegirl" "Have you been looking forward to today? I know I have!"
                "ropegirl" "We finally have the entire day to ourselves!"
                "ropegirl" "Noone to disturb us!"
                "ropegirl" "I've done some calculations and I think we can do that thing I talked about earlier."
                "ropegirl" "And to think I was afraid of you in the beginning!"
                "ropegirl" "We've really been missing out huh!"
                "ropegirl" "I've had dreams about you. Somehow with buckets of lubricant..."
                "ropegirl" "you managed to slip into my pussy and then you came so hard I had to barf your cum!"
                "ropegirl" "Crazy right! There's a bigger chance Long Feng stops being a dipshit than you being able to penetrate me."
                "ropegirl" " ...awhh, I made myself sad..."
                y "Ahum."
        show toxi toxi02 with vpunch
        "ropegirl" "Ahhh!! Who are you, what's going on here?!"
        y "That's what I'd like to know..."
        "ropegirl" "Are you the avatar?"
        "ropegirl" "Have you come to free fluffy?"
        y "Let's say yes. Who are you? "
        y "Why are you all... roped up?"
        y "It looks great on you, but still... wtf."
        "ropegirl" "Oh this... well..."
        show toxi toxi01
        "ropegirl" "I don't want to be mean to animals and I was feeling sorry for fluffy."
        "ropegirl" " I was appointed to be his caretaker."
        "ropegirl" "I feed him, shovel out his shit, etc..."
        "ropegirl" "I did my best to make everything to his liking, or at least as much as possible."
        "ropegirl" "But he was always so terribly sad."
        "ropegirl" "And as a sign of sympathy I tied myself up, just like he was."
        "ropegirl" "I was hoping he'd see me more as a friend in the same situation by doing so....."
        y "......"
        "ropegirl" "Okay, okay... I might have had a few too many drinks that evening."
        "ropegirl" "And there might have been a dare going on in the background."
        "ropegirl" "But it worked like nothing else ever had!"
        "ropegirl" "He started licking me all over and well... things progressed from there."
        y "...Wow."
        y "...just. wow."
        "ropegirl" "I swear he reaaally likes it! "
        "ropegirl" "Here let me show you! I'll prove it!"
        y "You... you wanna show me how you have sex with Appa?"
        "ropegirl" "I call him Fluffy, but yes."
        "ropegirl" "There's something I've always wanted to try."
        "ropegirl" "I call it \"the rocket\"!"
        y "Hmmmm... now I'm starting to get curious..."
    else:

        show toxi toxi01 with Dissolve(1.5)
        "ropegirl" "Ah! You're back!"
        "ropegirl" "Wanna watch me become a sperm propelled rocket with Fluffy's help?"




    menu:
        "Okay, show me your worst.":
            pass
        "Nah. I'm fine without.":
            if current_room.visit == 1:
                y "Gonna have to decline."
                y "Make sure he can leave whenever he wants from now on, understood?"
                "ropegirl" "I'd be sad to see him leave, but I won't prevent him."
                "ropegirl" "And of course if he does need to leave he can come back whenever he wants!"
                y "Good."
                y "You okay with this arrangement Appa?"
                play sound "audio/deepgrowl.mp3"
                "Appa has a look on his face which seems to say \"gonna fuck me some human pussy tonight\""
                y "Well, okay then."
                y "I might have need for you sometime in the future, but until then, have fun!"
                "Appa's face seems to say \"it's a deal dude! You can come and watch me have sex with this freak whenever you want in the future!\""
                y "Man, I have awesome face reading skills."
                y "I should play more poker!"
            return

    hide expression "maze/appa_head2.png"
    show expression "maze/appa_head3.png"
    hide toxi
    show toxi toxi101:
        parallel:
            xpos 50
            linear 4.0 xpos -250
            linear 4.0 xpos 50
            repeat
        parallel:
            ypos 0
            linear 1.0 ypos 15
            linear 1.0 ypos 0
            repeat
    "ropegirl" "First a little dance, to get him in the mood."
    $ renpy.pause()
    show toxi toxi102
    $ renpy.pause()
    "ropegirl" "He loves it when I shake my tushy!"
    y "Well, it's a fine tushy."
    hide toxi

    hide expression "maze/appa_body.png"
    hide expression "maze/appa_head3.png"
    hide expression "bk3/appa/tug/appa_tughead.png"
    show expression "bk3/appa/tug/appa_body.png"
    show expression "bk3/appa/tug/appa_tughead.png":
        linear 4.0 ypos -20
        linear 4.0 ypos 0
        repeat
    with Dissolve(1.5)

    "Appa turns over and..."
    show expression "bk3/appa/tug/appa_solodick.png":
        ypos 450 xpos 30
        linear 3.0 ypos 0 xpos 0
    "ropegirl" "Isn't it big!"
    y "Well... you know, it's only normal for an animal his size."

    show toxi toxi01:
        xpos 500
        linear 2.0 xpos 0

    hide toxi
    show toxi toxi101
    "ropegirl" "Now for some light buttocks action while pressing against his shaft..."
    $ renpy.pause()
    show toxi toxi09a
    play sound "audio/kiss.mp3"
    "ropegirl" "A kiss on the tip"

    hide toxi
    hide expression "bk3/appa/tug/appa_solodick.png"
    show toxi toxi03
    with Dissolve(2.0)
    "ropegirl" "And now that he's nice and hard... I smack his dick!"
    play sound "audio/slap.mp3"
    show toxi toxi04
    $ renpy.pause(0.1)
    play sound "audio/deepgrowl.mp3"
    $ renpy.pause(1.0)
    "ropegirl" "like this!"
    $ temp_int = 1
    while temp_int <8:
        show toxi toxi03
        $ renpy.pause(0.5)

        show toxi toxi04
        play sound "audio/slap.mp3"

        $ renpy.pause(0.5)
        $ temp_int += 1


    "ropegirl" "He really loves this shit!"
    show toxi toxi05
    "ropegirl" "But his favorite is a handsjob."
    "ropegirl" "Just one hand isn't going to cut it here, so it needs to be a handsjob."
    "ropegirl" "You like that, donchya boy!"
    "ropegirl" "You like having that pillar of flesh you call a penis caressed by my hands."
    "ropegirl" "I'm sad it can't fit inside me, but we can come up with other fun things to do!"
    "ropegirl" "Who's a good boy?! Who's a good boy?!"
    "ropegirl" "How about some fast strokes!"

    show toxi toxi06
    $ renpy.pause()
    "ropegirl" "It's like jacking a treetrunk!!"
    "ropegirl" "Are you almost there Fluffy?!"
    play sound "audio/deepgrowl.mp3" 
    $ renpy.pause(0.5)
    play sound "audio/deepgrowl.mp3"
    "ropegirl" "Good, because I can't wait any longer!!"
    show toxi toxi07 with Dissolve(1.5)
    "ropegirl" "Do it Fluffy!!"
    "ropegirl" "Fill me with your cum!! Launch me!!"
    play sound "audio/bigsplurt.mp3"
    show toxi toxi07 with vpunch

    hide toxi


    show toxi toxi08


    hide expression "bk3/appa/tug/appa_solodick.png"
    show expression "bk3/appa/tug/minime.png":
        xanchor 0.5 yanchor 0.5

        xpos 530 ypos 700
        parallel:
            rotate 0
            linear 2.0 rotate 360
            repeat
        parallel:
            linear 5.0 ypos -300

    show expression "bk3/appa/tug/minisperm.png":
        xpos 400 ypos 600
        linear 4.0 ypos -300
    $ renpy.pause(4.0)

    hide expression "bk3/appa/tug/minime.png"
    hide expression "bk3/appa/tug/minisperm.png"


    "ropegirl" "Team rocket blasting off again!"
    "ropegirl" "This is awesome!!"
    "ropegirl" "I can see forever!!"
    "ropegirl" "I'm... still gaining altitude...?"


    hide toxi
    show expression "bk3/appa/tug/appa_solodick.png"
    y "I know you'd like to enjoy that afterglow buddy... but if you want more in the future..."
    y "better go and make sure she doesn't go splat. "
    play sound "audio/deepgrowl.mp3"
    hide expression "bk3/appa/tug/appa_solodick.png"
    hide expression "bk3/appa/tug/appa_body.png"
    hide expression "bk3/appa/tug/appa_tughead.png"
    with Dissolve(1.5)
    $ renpy.pause(1.0)
    "Appa jumps up..."
    show toxi toxi08
    hide toxi_appafly
    show toxi_appafly:
        ypos 300 xpos 200
        linear 9.0 ypos -500 xzoom 0.5 yzoom 0.5
    "...and flies after the girl"
    hide toxi_appafly
    hide toxi toxi08
    show expression "bk3/appa/tug/minime_caught.png"
    show expression "bk3/appa/tug/minime_caught2.png"
    show toxi_appahat:
        xpos 110 ypos 80 xzoom 0.8 yzoom 0.8
        linear 3.0 ypos 90
        linear 3.0 ypos 80
        repeat

    play sound "audio/thud.mp3"
    y "Good boy!" with vpunch
    hide expression "bk3/appa/tug/minime_caught2.png"
    show toxi toxi10:
        ypos 120
    with Dissolve(1.5)

    "ropegirl" "Wow! That was wild!"
    "ropegirl" "I could sell tickets for a ride like this!"
    y "You better not start pimping out my skybison...."
    "ropegirl" "It's just a joke!"

    if current_room.sp_content <= 1:
        $ current_room.sp_content = 2
        y "Well, I guess... Fluffy... isn't so bad off here."
        y "Just make sure he can leave if I need him and you can ride his firehydrant as long as he enjoys it."
        "ropegirl" "Really?!"
        y "Sure."
        "ropegirl" "Will do! Thanks!"
    return


label ajala_dunk:
    show expression "ebackgrounds/ajala_dunkscene.jpg"
    $ temp_boolean = False
    show toxf toxf00
    ct "Hi, aang."
    ct "Could you help me with something?"
    y "Again?"
    stop music
    play music "audio/Unwritten Return.mp3"
    hide toxf
    show toxf toxf01
    with Dissolve(1.5)
    y "uhhh, what are you doing?"
    ct "Holding this position is great for your abs... but more importantly..."
    ct "I want you to rip my pussy to shreds!"
    y "I certainly can, figuratively speaking."
    y "But don't you want me to earn it?"
    ct "No! I mean yes I do, but I can't enjoy it as much when I'm already worn out from fighting you."
    ct "I want to savor the experience."
    ct "Mark me as yours, avatar!"

    hide toxf
    show toxf toxf10:
        xpos 0 ypos 0
    with Dissolve(1.5)
    show toxf toxf10:
        linear 4.0 ypos -280

    ct "No matter what you think of my muscles, my pussy is still as soft and penetrable as any other girl's."
    menu:
        "Admire her fit body and pussy":

            y "I think you have an awesome body."
            y "And your muscular physique is a big part of that."
            y "You have to train hard to get like this and it makes you all the more attractive."
            y "....but waving that pussy in front of my face certainly seals the deal."
        "Only acknowledge her pussy.":

            y "You have a gorgeous pussy."
            y "And I'm going to wreck it."
            "Ajala looks slightly disappointed, as if she was hoping to hear something more, but quickly regains herself."

    ct "Would you like to see... all the way inside? "

    menu:
        "Gape that cunt for me, baby!":
            show toxf toxf11:
                linear 2.0 ypos -350
            y "That's a lovely cervix."

            hide toxf
            show toxf toxf03
            with Dissolve(1.5)
            y "...let's see if I can push into it."
        "No time for sightseeing":

            y "No need, my one eyed snake will take a more direct look for me."



    hide toxf
    show toxf toxf04
    with Dissolve(1.5)
    ct "Ooohh... I can't wait any longer! Do it!"


    show toxf toxf05 with Dissolve(1.5)
    "You lift up Ajala's legs."
    ct "Why...?"
    y "I can go in deeper like this."
    y "Now taste my cock!"
    show toxf toxf08 with hpunch
    $ renpy.pause(1.0)
    show toxf toxf05 with Dissolve(1.5)



    show toxf toxf100
    ct "Aaaahh!!"
    $ renpy.pause()
    y "You're insides feel so hot!"
    y "Let's speed this up!"

    show toxf toxf101
    ct "Ah! Ah! Ah!"

    $ renpy.pause()

    show toxf toxf102
    y "This time with some more force!!!"
    $ renpy.pause()
    "You push down hard into Ajala's cunt, forcibly smacking your balls against her ass in the process."
    y "Take this! And this!"
    ct "AAAaah!! I'm going crazy!!!"

    menu:
        "cum inside":
            $ temp_boolean = False
            show toxf toxf08
            play sound "audio/gltch2b.mp3"
            with flash
            $ renpy.pause()
            play sound "audio/gltch2b.mp3"
            with flash
            $ renpy.pause()
            show toxf toxf09
            show expression "bk3/ajala/dunk/spermin.png":
                xpos 20 ypos 30
            with Dissolve(1.5)
            ct "I'm so full...."
            hide expression "bk3/ajala/dunk/spermin.png"
            hide toxf
            show toxf toxf10:
                ypos -210
            show expression "bk3/ajala/dunk/spermin2.png":
                ypos -210
            show expression "bk3/ajala/dunk/frontbody_lewdface.png":
                ypos -210
            $ renpy.pause()
            scene black
        "cum in gaping cunt":


            $ temp_boolean = False
            hide toxf
            show toxf toxf04
            with Dissolve(1.5)
            y "Open it up for me."
            show toxf toxf02
            y "awesome"
            hide toxf
            show toxf toxf11:
                linear 2.0 ypos -350
            y "Gonna drown that womb in my cum."
            show expression "bk3/ajala/dunk/frontdick.png" with Dissolve(1.5)
            show toxf toxf11:
                ypos -350
            play sound "audio/gltch2b.mp3"
            show expression "bk3/ajala/dunk/frontsperm1.png"
            with flash
            $ renpy.pause()
            play sound "audio/gltch2b.mp3"
            show expression "bk3/ajala/dunk/frontsperm2.png"
            with flash
            $ renpy.pause()
            play sound "audio/gltch2b.mp3"
            show expression "bk3/ajala/dunk/frontsperm3.png"
            with flash
            $ renpy.pause()
            scene black
        "cum outside":


            $ temp_boolean = True
            hide toxf
            show toxf toxf04
            with Dissolve(1.5)
            y "Here I cum!"


            play sound "audio/gltch2b.mp3"
            show toxf_spermshot
            show expression "bk3/ajala/dunk/spermout1.png"

            y "Hnngg..."
            play sound "audio/gltch2b.mp3"
            show toxf_spermshot
            show expression "bk3/ajala/dunk/spermout2.png"
            y "Nnnghhh!!!"
            $ renpy.pause()
            play sound "audio/gltch2b.mp3"
            show toxf_spermshot
            show expression "bk3/ajala/dunk/spermout3.png"
            ct "You could provide for a small village with this amount!"
            y "It wouldn't be the first time."
            $ renpy.pause()
            scene black


    hide toxf
    if temp_boolean == True:
        show expression "ebackgrounds/ajala_dunkscene.jpg"
        show toxf toxf00b:
            xpos 0 ypos 0
            linear 5.0 ypos -200
        with Dissolve(1.5)
    else:
        show expression "ebackgrounds/ajala_dunkscene.jpg"
        show toxf toxf00a:
            xpos 0 ypos -780
            linear 7.0 ypos -100
        with Dissolve(1.5)
        $ renpy.pause(5.0)

    ct "Thanks, Aang."
    ct "..."

    scene black with dissolve
    "you head back to the village."
    $ bk3_day = False
    jump love_bk3_village_background
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
