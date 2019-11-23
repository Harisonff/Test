

init python:
    class Worldroom:
        def __init__(self, wr_name, wr_background,  wr_north, wr_south, wr_west, wr_east, wr_enemy, wr_content):
            self.wr_name = wr_name
            self.wr_background = wr_background            
            self.wr_north = wr_north
            self.wr_south = wr_south
            self.wr_west = wr_west
            self.wr_east = wr_east
            self.wr_enemy = wr_enemy
            self.wr_content = wr_content


init:

    $ b4_zhuli_exists = True
    $ b4_ginger_exists = True
    $ b4_jinora_exists = False
    $ b4_korra_exists = False

    $ b4_update_worldrooms = 0

    $ become_a_star = 0

    $ b4_walkingdirection = 'right'


    $ korra_xpos = 700
    $ korra_ypos = 300

    default b4_inaccessible = []

    $ sandan_x = 500
    $ sandan_y = 500

    $ sandan_x_new = 0
    $ sandan_y_new = 0


    $ sandan = 'still'

    $ b4_activate_actor = False

    $ b4_locals = [ [-1,-1,'none','none','none'],  
                    [-1,-1,'none','none','none'],
                    [-1,-1,'none','none','none'],
                    [-1,-1,'none','none','none'],
                    [-1,-1,'none','none','none'],
                    [-1,-1,'none','none','none']]


    $ sandan_character = 'tenzin'

    image sandan_image01 = LiveComposite(
    (108, 168),    
    (0, 0), ConditionSwitch(        
        "sandan_character == 'tenzin'",  "bk4/worldrooms/sandan1.png",
        "sandan_character == 'amon'",  "bk4/worldrooms/tenzinamon_01.png",
        "sandan_character == 'spirit'", "bk4/worldrooms/playerspirit_01.png"), 
    )
    image sandan_image02 = LiveComposite(
    (108, 168),    
    (0, 0), ConditionSwitch(        
        "sandan_character == 'tenzin'",  "bk4/worldrooms/sandan2.png",
        "sandan_character == 'amon'",  "bk4/worldrooms/tenzinamon_02.png",
        "sandan_character == 'spirit'",    "bk4/worldrooms/playerspirit_02.png"), 
    )



    image im_sandan sandan_still:
        xanchor 0.5
        yanchor 0.5
        "sandan_image01"


    image im_sandan sandan_walk:
        xanchor 0.5
        yanchor 0.5
        "sandan_image01"
        0.2
        "sandan_image02"
        0.2
        repeat

    image im_sandan sandan_walkleft:
        xanchor 0.5
        yanchor 0.5 xzoom -1.0
        "sandan_image01"
        0.2
        "sandan_image02"
        0.2
        repeat

    image zhuli_chibi:
        xanchor 0.5 yanchor 0.5
        im.Flip("bk4/worldrooms/actor_02.png", horizontal=True)
        1.0
        "bk4/worldrooms/actor_02.png"
        9.0
        repeat



    image ginger_chibi ginger_still:
        xanchor 0.5 yanchor 0.5
        "bk4/worldrooms/actor_01.png"

    image ginger_chibi ginger_walksright:
        xanchor 0.5 yanchor 0.5
        "bk4/worldrooms/actor_01.png"
        0.3
        "bk4/worldrooms/actor_01a.png"
        0.3
        repeat

    image ginger_chibi ginger_walksleft:
        xanchor 0.5 yanchor 0.5
        im.Flip("bk4/worldrooms/actor_01.png", horizontal = True)
        0.3
        im.Flip("bk4/worldrooms/actor_01a.png", horizontal = True)
        0.3
        repeat


    image chibi_kyoshispirit misc_still:
        xanchor 0.5 yanchor 0.5
        "bk4/worldrooms/kyoshispirit_01.png"

    image chibi_kyoshispirit misc_walksleft:
        xanchor 0.5 yanchor 0.5
        "bk4/worldrooms/kyoshispirit_01.png"
        0.3
        "bk4/worldrooms/kyoshispirit_02.png"
        0.3
        repeat

    image chibi_kyoshi misc_walksright:
        xanchor 0.5 yanchor 0.5
        im.Flip("bk4/worldrooms/kyoshispirit_01.png", horizontal = True)
        0.3
        im.Flip("bk4/worldrooms/kyoshispirit_02.png", horizontal = True)
        0.3
        repeat




    image korra_chibi korra_still:
        "bk4/worldrooms/korra.png"
        xanchor 0.5 yanchor 0.5

    image korra_chibi korra_walksleft:
        xanchor 0.5 yanchor 0.5
        "bk4/worldrooms/korra.png"
        0.3
        "bk4/worldrooms/korra1.png"
        0.3
        repeat

    image korra_chibi korra_walksright:
        xanchor 0.5 yanchor 0.5
        im.Flip("bk4/worldrooms/korra.png", horizontal = True)
        0.3
        im.Flip("bk4/worldrooms/korra1.png", horizontal = True)
        0.3
        repeat




label start_worldrooms:

    if b4_update_worldrooms == 0:
        $ b4_update_worldrooms = 1





        $ worldroom0   = Worldroom("wroom0",  "bk4/worldrooms/bg_000.jpg", -1,        -1,      -1,         1,      True,           0 )
        $ worldroom1   = Worldroom("wroom1",  "bk4/worldrooms/bg_001.jpg", -1,        -1,       0,         2,      True,           0 )
        $ worldroom2   = Worldroom("wroom2",  "bk4/worldrooms/bg_002.jpg", -1,        -1,       1,        -1,      False,          0 )




        $ worldroom10  = Worldroom("wroom10", "bk4/worldrooms/bg_010.jpg", -1,        11,      -1,        13,      False,         0 )
        $ worldroom11  = Worldroom("wroom11", "bk4/worldrooms/bg_011.jpg", 10,        -1,      -1,        12,      False,         0 )
        $ worldroom12  = Worldroom("wroom12", "bk4/worldrooms/bg_012.jpg", 13,        -1,      11,        -1,      True,          0 )
        $ worldroom13  = Worldroom("wroom13", "bk4/worldrooms/bg_013.jpg", -1,        12,      10,        -1,      True,          0 )



        $ worldroom14  = Worldroom("wroom14", "bk4/worldrooms/bg_dreamscape_0.jpg", 15,        14,      14,        14,      False,          0 )
        $ worldroom15  = Worldroom("wroom15", "bk4/worldrooms/bg_dreamscape_1.jpg", 14,        14,      16,        14,      False,          0 )
        $ worldroom16  = Worldroom("wroom16", "bk4/worldrooms/bg_016.jpg",          -1,        -1,      -1,        -1,      False,          0 )
        $ worldroom17  = Worldroom("wroom17", "bk4/worldrooms/bg_dreamscape_1.jpg", -1,        -1,      -1,        -1,      False,          0 )


        $ worldroom_list = [worldroom0, worldroom1, worldroom2, "filler3", "filler4", "filler5",
                            "filler6", "filler7", "filler7", "filler9", worldroom10, worldroom11,
                            worldroom12, worldroom13, worldroom14, worldroom15,worldroom16, worldroom17]

        $ current_worldroom = worldroom1
        $ previous_worldroom = current_worldroom




    return




label b4_draw_worldroom:

    if not b4_music_day_on:
        $ b4_music_day_on = True
        stop music fadeout 1
        play music "audio/bounce_town.mp3"


    scene

    show expression current_worldroom.wr_background

    show im_sandan sandan_still:
        pos (sandan_x,  sandan_y)

    show screen travel_easier

    $ renpy.jump (current_worldroom.wr_name)







label wroom0:


    $ b4_locals = [  [ -1, -1 ,  'none' ,        'gone',         'none'],
                    [ -1, -1 ,  'none' ,        'gone',         'none'],
                    [ -1, -1 ,  'none' ,        'gone',         'none'],
                    [ -1, -1 ,  'none' ,        'gone',         'none'],
                    [ -1, -1 ,  'none',         'gone',         'none'],
                    [ -1, -1 ,  'none',         'gone',         'none']]


    $ b4_inaccessible = [[100,300],[100,400],[100,500],
                        [200,300], [200,400],
                        [300,300],
                        [400,100],
                        [500,100],
                        [600,100],
                        [700,100],
                        [800,100],
                        [900,100]]

    jump check_sandan_coordinates





label wroom1:



    $ b4_locals = [  [korra_xpos, korra_ypos,   ['ginger_chibi ginger_still',
                                                'ginger_chibi ginger_walksleft',
                                                'ginger_chibi ginger_walksright'],    'exists',       'b4_label_ginger'],
                                                                                                          
                    [600,200,                   'zhuli',                                'exists',       'b4_label_zhuli'],
                    [300,100,                   'none',                                 'gone',         'none'],
                    [ -1, -1 ,                  'none',                                 'gone',         'none'],
                    [ -1, -1 ,                  'none',                                 'gone',         'none'],
                    [ -1, -1 ,                  'none',                                 'gone',         'none']
                    ]

    $ b4_inaccessible = [[100,100], [200,100], [400,100], [500,100], [600,100], [700,100], [800,100], [900,100], [1000,100]]


    if current_worldroom.wr_content == 0:
        $ current_worldroom.wr_content = 1
        hide screen travel_easier    
        show expression "bk4/worldrooms/bg_001.jpg"
        show bfazh bfazh01
        zh "Excuse me, could I have a moment of your time?"
        hide expression "bk4/worldrooms/bg_001.jpg"
        hide bfazh
        with dissolve
        show screen travel_easier  



    if b4_ginger_exists == True:
        $ b4_locals[0][3] = 'exists'
    else:
        $ b4_locals[0][3] = 'gone'

    if b4_zhuli_exists == True:
        $ b4_locals[1][3] = 'exists'
    else:
        $ b4_locals[1][3] = 'gone'




    $ temp_int = renpy.random.choice([450,900,700,900])

    show expression "bk4/worldrooms/car_01.png":
        xpos 1100 ypos temp_int xanchor 0.5 yanchor 0.5 xzoom 1.0
        linear 5 xpos -100 ypos temp_int




    if b4_locals[1][3] == 'exists':
        show zhuli_chibi:
            xanchor 0.5 yanchor 0.5
            xpos b4_locals[1][0] ypos b4_locals[1][1]

    if b4_locals[0][3] == 'exists':
        jump b4_move_actor1

    jump check_sandan_coordinates




label wroom2:


    $ b4_locals =  [[ -1, -1 ,          'none',         'gone',         'none'], 
                    [ 600, 100 ,        'tree',         'exists',       'b4_label_treehouse'],
                    [ 600, 200 ,        'tree',         'exists',       'b4_label_treehouse'],
                    [ 300, 200 ,        'none',         'exists',       'b4_label_oogi_takeoff'],
                    [ 400, 200 ,        'none',         'exists',       'b4_label_oogi_takeoff'],                    
                    [ 500, 200 ,        'none',         'exists',       'b4_label_oogi_takeoff']]


    $ b4_inaccessible = [[100,100], 
                        [200,100], 
                        [300,100],
                        [400,100], 
                        [500,100], 
                        [700,100], 
                        [800,100], 
                        [900,100],]





    show expression "bk4/worldrooms/oogi_landed.png"
    hide im_sandan
    show im_sandan sandan_still
    show expression "bk4/worldrooms/trees_foreground.png"

    jump check_sandan_coordinates








label wroom10:


    $ b4_locals =  [[ -1, -1 ,          'none',         'gone',         'none'],
                    [ 300, 200 ,        'none',         'exists',       'b4_label_oogi_takeoff'],
                    [ 400, 200 ,        'none',         'exists',       'b4_label_oogi_takeoff'],
                    [ 400, 300 ,        'none',         'exists',       'b4_label_oogi_takeoff'],
                    [ 500, 200 ,        'none',         'exists',       'b4_label_oogi_takeoff'],
                    [ -1, -1 ,          'none',         'gone',         'none']]


    $ b4_inaccessible = [[100,100], [200,100], [400,100], [500,100], [600,100], [700,100], [800,100], [900,100], 
        [900,600], [800,600], [700,600]]

    show expression "bk4/worldrooms/oogi_landed.png"

    hide im_sandan
    show im_sandan sandan_still
    show expression "bk4/worldrooms/aang_statue.png"



    jump check_sandan_coordinates










label wroom11:


    $ b4_locals =  [[ -1, -1 ,          'none',         'gone',         'none'], 
                    [ 900, 200 ,        'none',         'exists',       'b4_inside_aangstatue'],
                    [ 200, 200 ,        'chibi_jinora', 'exists',       'b4_label_chibijinora'],
                    [ -1, -1 ,          'none',         'gone',         'none'],
                    [ -1, -1 ,          'none',         'gone',         'none'],
                    [ -1, -1 ,          'none',         'gone',         'none']]

    $ b4_inaccessible = [   [700,100], [700,200],  [700,300], 
                            [800,100], [800,200], [800,300], 
                            [900,100],  
                        ]



    if b4_jinora_exists == True:
        $ b4_locals[2][3] = 'exists'
    else:
        $ b4_locals[2][3] = 'gone'





    if b4_locals[2][3] == 'exists':
        show expression "bk4/worldrooms/chibi_jinora.png":
            xpos 200 ypos 200 xanchor 0.5 yanchor 0.5

    jump check_sandan_coordinates





label wroom12:


    $ b4_locals =  [[ korra_xpos, korra_ypos ,  ['korra_chibi korra_still', 
                                                 'korra_chibi korra_walksleft',
                                                 'korra_chibi korra_walksright'],       'exists',       'b4_label_chibikorra'],                                             
                    [ -1, -1 ,                  'none',                                 'gone',         'none'],
                    [ -1, -1 ,                  'none',                                 'gone',         'none'],
                    [ -1, -1 ,                  'none',                                 'gone',         'none'],
                    [ -1, -1 ,                  'none',                                 'gone',  'none'],
                    [ -1, -1 ,                  'none',                                 'gone',  'none']]


    $ b4_inaccessible = [   [100,100], [200,100], [300,100], [400,100],
                            [100,200], [200,200], [300,200], [400,200],
                            [300,200], [300,300], 
                            [100, 300], [200, 300]
                            
                        ]



    show im_sandan behind sakuratree




    if b4_korra_exists == True:
        $ b4_locals[0][3] = 'exists'
    else:
        $ b4_locals[0][3] = 'gone'






    if b4_locals[0][3] == 'exists':
        jump b4_move_actor1

    show expression "bk4/worldrooms/sakura.png" as sakuratree

    jump check_sandan_coordinates




label wroom13:



    $ b4_locals =  [[ -1, -1 ,          'none',         'gone',         'none'], 
                    [ 500, 200 ,        'none',         'exists',       'b4_label_bioculars'],
                    [ -1, -1 ,          'none',         'gone',         'none'],
                    [ -1, -1 ,          'none',         'gone',         'none'],
                    [ -1, -1 ,          'none',         'gone',         'none'],
                    [ -1, -1 ,          'none',         'gone',         'none']]

    $ b4_inaccessible = [   [100,100], [200,100],  [300,100], [400,100],[500,100], [600,100],[700,100], [800,100],[900,100], 
                            [100,200], [200,200],  [300,200], [400,200],         [600,200],[700,200], [800,200],[900,200],
                            [100,600], [200,600],
                        ]

    show expression "bk4/worldrooms/aang_statue_2.png"

    jump check_sandan_coordinates






label wroom14:



    $ b4_locals = [ [-1,-1,'none','none','none'],  
                    [-1,-1,'none','none','none'],
                    [-1,-1,'none','none','none'],
                    [-1,-1,'none','none','none'],
                    [-1,-1,'none','none','none'],
                    [-1,-1,'none','none','none']]
    $ b4_inaccessible = []


    if temp_int == 1:
        $ temp_int = 0

        hide screen travel_easier
        b4_yn "Where... am I?"
        b4_yn "What's happening?"
        b4_yn "How do I get out of here?"
        b4_yn "when are the olympics?"
        show screen travel_easier

    if worldroom16.wr_content >= 1 and current_worldroom.wr_content == 0:
        $ current_worldroom.wr_content = 1
        hide screen travel_easier
        b4_ya "....."
        b4_ya "fuck."
        b4_ya "This is where I started."
        b4_ya "Let's find that snake spirit again."
        show screen travel_easier


    jump check_sandan_coordinates



label wroom15:


    $ b4_locals = [ [-1,-1,'none','none','none'],  
                    [-1,-1,'none','none','none'],
                    [-1,-1,'none','none','none'],
                    [-1,-1,'none','none','none'],
                    [-1,-1,'none','none','none'],
                    [-1,-1,'none','none','none']]
    $ b4_inaccessible = []



    jump check_sandan_coordinates




label wroom16:


    $ b4_locals = [ [-1,-1,'none','none','none'],  
                    [500,100,'none','exists','b4_label_nagaprime'],
                    [500,200,'none','exists','b4_label_nagaprime'],
                    [500,300,'none','exists','b4_label_nagaprime'],
                    [-1,-1,'none','none','none'],
                    [-1,-1,'none','none','none']]

    $ b4_inaccessible = []


    jump check_sandan_coordinates


label wroom17:



    $ b4_locals =  [[ -1, -1 ,                    'none',         'gone',         'none'],
                                             
                    [ 200, 100 ,                  'none',         'exists',       'b4_label_nagachibi'],
                    [ 200, 200 ,                  'none',         'exists',       'b4_label_nagachibi'],
                    [ 800, 100 ,                  'none',         'exists',       'b4_label_nagachibi'],
                    [ 800, 200 ,                  'none',         'exists',       'b4_label_nagachibi'],
                    [ -1, -1 ,                    'none',         'gone',         'none']]


    $ b4_inaccessible = [ ]

    show expression "bk4/worldrooms/snakesisters.png":
        linear 2.0 ypos 10
        linear 2.0 ypos 0
        repeat


    hide im_sandan
    show im_sandan sandan_still:
        xpos sandan_x ypos sandan_y



    $ renpy.pause()
    "This should never be reached 2200."
    jump check_sandan_coordinates


label check_sandan_coordinates:




    $ b4_location_accesible = True


    if [sandan_x_new,sandan_y_new] in b4_inaccessible:
        $ b4_location_accesible = False


    if b4_location_accesible == True:

        if sandan_x_new == sandan_x and sandan_y_new != sandan_y:
            show im_sandan sandan_walkleft at Move((sandan_x, sandan_y), 
                                                   (sandan_x_new, sandan_y_new), 1.0, xanchor="center", yanchor="center")
        elif sandan_x_new < sandan_x:
            show im_sandan sandan_walk at Move((sandan_x, sandan_y), 
                                               (sandan_x_new, sandan_y_new), 1.0, xanchor="center", yanchor="center")
        elif sandan_x_new > sandan_x:
            show im_sandan sandan_walkleft at Move((sandan_x, sandan_y), 
                                                   (sandan_x_new, sandan_y_new), 1.0, xanchor="center", yanchor="center")
        else:
            show im_sandan sandan_still at Move((sandan_x, sandan_y), 
                                                (sandan_x_new, sandan_y_new), 1.0, xanchor="center", yanchor="center")


        $ sandan_x = sandan_x_new
        $ sandan_y = sandan_y_new






        if sandan_x_new in [1000, 0] or sandan_y_new in [700, 0]:

            hide screen travel_easier   
            $ renpy.pause(1.0)
            show screen travel_easier

            if current_worldroom.wr_east != -1 and sandan_x_new == 1000:
                $ previous_worldroom = current_worldroom
                $ current_worldroom = worldroom_list[current_worldroom.wr_east]
                $ sandan_x = 100
                $ sandan_x_new = 100
                jump b4_draw_worldroom

            if current_worldroom.wr_west != -1 and sandan_x_new == 0:
                $ previous_worldroom = current_worldroom
                $ current_worldroom = worldroom_list[current_worldroom.wr_west]
                $ sandan_x = 900
                $ sandan_x_new = 900
                jump b4_draw_worldroom

            if current_worldroom.wr_south != -1 and sandan_y_new == 700:
                $ previous_worldroom = current_worldroom
                $ current_worldroom = worldroom_list[current_worldroom.wr_south]
                $ sandan_y = 200
                $ sandan_y_new = 200
                jump b4_draw_worldroom

            if current_worldroom.wr_north != -1 and sandan_y_new == 0:
                $ previous_worldroom = current_worldroom
                $ current_worldroom = worldroom_list[current_worldroom.wr_north]
                $ sandan_y = 600
                $ sandan_y_new = 600
                jump b4_draw_worldroom








    elif b4_location_accesible == False:


        show expression "bk4/worldrooms/nogo_area.png":
            pos (sandan_x_new, sandan_y_new) xanchor 0.5
            yanchor 0.5
        $ renpy.pause(0.3)
        hide expression "bk4/worldrooms/nogo_area.png"








    python:

        b4_activate_actor = False

        for x in range(0,6):
            
            if sandan_x == b4_locals[x][0] and sandan_y == b4_locals[x][1] and b4_locals[x][3]=='exists':
                b4_activate_actor = True
                b4_actor_label = b4_locals[x][4]





    if b4_activate_actor == True:

        hide screen travel_easier
        $ renpy.pause(1.0)

        show im_sandan sandan_still:
            xpos sandan_x_new ypos sandan_y_new



        $ b4_activate_actor = False
        $ sandan = 'still'
        show im_sandan sandan_still
        $ renpy.jump(b4_actor_label)


    $ renpy.pause(1.0)
    show im_sandan sandan_still


    $ renpy.pause(0.1)

    show im_sandan sandan_still:
        xpos sandan_x ypos sandan_y

    if not first_traverse:
        $ first_traverse = True
        "click on the screen to move your character. you can use your arrow keys to change rooms quickly."




    if b4_locals[0][3] == 'exists':
        jump b4_move_actor1

    $ renpy.pause()



    jump b4_draw_worldroom











screen travel_easier:
    imagemap:


        hover "bk4/worldrooms/groot_hover_test.png"
        idle "bk4/worldrooms/groot_idle_test.png"


        if current_worldroom.wr_north != -1:
            key "focus_up" action [SetVariable("b4_walkingdirection", 'up'), Jump("b4_check_walkingdirection")]

        if current_worldroom.wr_south != -1:
            key "focus_down" action [SetVariable("b4_walkingdirection", 'down'), Jump("b4_check_walkingdirection")]

        if current_worldroom.wr_west != -1:
            key "focus_left" action [SetVariable("b4_walkingdirection", 'left'), Jump("b4_check_walkingdirection")]

        if current_worldroom.wr_east != -1:
            key "focus_right" action [SetVariable("b4_walkingdirection", 'right'), Jump("b4_check_walkingdirection")]




        if current_worldroom.wr_north != -1:
            add "bk4/worldrooms/arrow_up.png" xalign 0.5 yalign 0.0 xanchor 0.5 yanchor 0.0
        if current_worldroom.wr_west != -1:
            add "bk4/worldrooms/arrow_left.png" xalign 0.0 yalign 0.5 xanchor 0.0 yanchor 0.5
        if current_worldroom.wr_east != -1:
            add "bk4/worldrooms/arrow_right.png" xalign 1.0 yalign 0.5 xanchor 1.0 yanchor 0.5
        if current_worldroom.wr_south != -1:
            add "bk4/worldrooms/arrow_down.png" xalign 0.5 yalign 1.0 xanchor 0.5 yanchor 1.0







        hotspot (  50, 50, 100, 100) action [SetVariable("sandan_x_new", 100), SetVariable("sandan_y_new", 100), Jump("check_sandan_coordinates")]
        hotspot ( 150, 50, 100, 100) action [SetVariable("sandan_x_new", 200), SetVariable("sandan_y_new", 100), Jump("check_sandan_coordinates")]
        hotspot ( 250, 50, 100, 100) action [SetVariable("sandan_x_new", 300), SetVariable("sandan_y_new", 100), Jump("check_sandan_coordinates")]
        hotspot ( 350, 50, 100, 100) action [SetVariable("sandan_x_new", 400), SetVariable("sandan_y_new", 100), Jump("check_sandan_coordinates")]
        hotspot ( 450, 50, 100, 100) action [SetVariable("sandan_x_new", 500), SetVariable("sandan_y_new", 100), Jump("check_sandan_coordinates")]
        hotspot ( 550, 50, 100, 100) action [SetVariable("sandan_x_new", 600), SetVariable("sandan_y_new", 100), Jump("check_sandan_coordinates")]
        hotspot ( 650, 50, 100, 100) action [SetVariable("sandan_x_new", 700), SetVariable("sandan_y_new", 100), Jump("check_sandan_coordinates")]
        hotspot ( 750, 50, 100, 100) action [SetVariable("sandan_x_new", 800), SetVariable("sandan_y_new", 100), Jump("check_sandan_coordinates")]
        hotspot ( 850, 50, 100, 100) action [SetVariable("sandan_x_new", 900), SetVariable("sandan_y_new", 100), Jump("check_sandan_coordinates")]




        hotspot (  50, 150, 100, 100) action [SetVariable("sandan_x_new", 100), SetVariable("sandan_y_new", 200), Jump("check_sandan_coordinates")]
        hotspot ( 150, 150, 100, 100) action [SetVariable("sandan_x_new", 200), SetVariable("sandan_y_new", 200), Jump("check_sandan_coordinates")]
        hotspot ( 250, 150, 100, 100) action [SetVariable("sandan_x_new", 300), SetVariable("sandan_y_new", 200), Jump("check_sandan_coordinates")]
        hotspot ( 350, 150, 100, 100) action [SetVariable("sandan_x_new", 400), SetVariable("sandan_y_new", 200), Jump("check_sandan_coordinates")]
        hotspot ( 450, 150, 100, 100) action [SetVariable("sandan_x_new", 500), SetVariable("sandan_y_new", 200), Jump("check_sandan_coordinates")]
        hotspot ( 550, 150, 100, 100) action [SetVariable("sandan_x_new", 600), SetVariable("sandan_y_new", 200), Jump("check_sandan_coordinates")]
        hotspot ( 650, 150, 100, 100) action [SetVariable("sandan_x_new", 700), SetVariable("sandan_y_new", 200), Jump("check_sandan_coordinates")]
        hotspot ( 750, 150, 100, 100) action [SetVariable("sandan_x_new", 800), SetVariable("sandan_y_new", 200), Jump("check_sandan_coordinates")]
        hotspot ( 850, 150, 100, 100) action [SetVariable("sandan_x_new", 900), SetVariable("sandan_y_new", 200), Jump("check_sandan_coordinates")]



        hotspot (  50, 250, 100, 100) action [SetVariable("sandan_x_new", 100), SetVariable("sandan_y_new", 300), Jump("check_sandan_coordinates")]
        hotspot ( 150, 250, 100, 100) action [SetVariable("sandan_x_new", 200), SetVariable("sandan_y_new", 300), Jump("check_sandan_coordinates")]
        hotspot ( 250, 250, 100, 100) action [SetVariable("sandan_x_new", 300), SetVariable("sandan_y_new", 300), Jump("check_sandan_coordinates")]
        hotspot ( 350, 250, 100, 100) action [SetVariable("sandan_x_new", 400), SetVariable("sandan_y_new", 300), Jump("check_sandan_coordinates")]
        hotspot ( 450, 250, 100, 100) action [SetVariable("sandan_x_new", 500), SetVariable("sandan_y_new", 300), Jump("check_sandan_coordinates")]
        hotspot ( 550, 250, 100, 100) action [SetVariable("sandan_x_new", 600), SetVariable("sandan_y_new", 300), Jump("check_sandan_coordinates")]
        hotspot ( 650, 250, 100, 100) action [SetVariable("sandan_x_new", 700), SetVariable("sandan_y_new", 300), Jump("check_sandan_coordinates")]
        hotspot ( 750, 250, 100, 100) action [SetVariable("sandan_x_new", 800), SetVariable("sandan_y_new", 300), Jump("check_sandan_coordinates")]
        hotspot ( 850, 250, 100, 100) action [SetVariable("sandan_x_new", 900), SetVariable("sandan_y_new", 300), Jump("check_sandan_coordinates")]




        hotspot (  50, 350, 100, 100) action [SetVariable("sandan_x_new", 100), SetVariable("sandan_y_new", 400), Jump("check_sandan_coordinates")]
        hotspot ( 150, 350, 100, 100) action [SetVariable("sandan_x_new", 200), SetVariable("sandan_y_new", 400), Jump("check_sandan_coordinates")]
        hotspot ( 250, 350, 100, 100) action [SetVariable("sandan_x_new", 300), SetVariable("sandan_y_new", 400), Jump("check_sandan_coordinates")]
        hotspot ( 350, 350, 100, 100) action [SetVariable("sandan_x_new", 400), SetVariable("sandan_y_new", 400), Jump("check_sandan_coordinates")]
        hotspot ( 450, 350, 100, 100) action [SetVariable("sandan_x_new", 500), SetVariable("sandan_y_new", 400), Jump("check_sandan_coordinates")]
        hotspot ( 550, 350, 100, 100) action [SetVariable("sandan_x_new", 600), SetVariable("sandan_y_new", 400), Jump("check_sandan_coordinates")]
        hotspot ( 650, 350, 100, 100) action [SetVariable("sandan_x_new", 700), SetVariable("sandan_y_new", 400), Jump("check_sandan_coordinates")]
        hotspot ( 750, 350, 100, 100) action [SetVariable("sandan_x_new", 800), SetVariable("sandan_y_new", 400), Jump("check_sandan_coordinates")]
        hotspot ( 850, 350, 100, 100) action [SetVariable("sandan_x_new", 900), SetVariable("sandan_y_new", 400), Jump("check_sandan_coordinates")]



        hotspot (  50, 450, 100, 100) action [SetVariable("sandan_x_new", 100), SetVariable("sandan_y_new", 500), Jump("check_sandan_coordinates")]
        hotspot ( 150, 450, 100, 100) action [SetVariable("sandan_x_new", 200), SetVariable("sandan_y_new", 500), Jump("check_sandan_coordinates")]
        hotspot ( 250, 450, 100, 100) action [SetVariable("sandan_x_new", 300), SetVariable("sandan_y_new", 500), Jump("check_sandan_coordinates")]
        hotspot ( 350, 450, 100, 100) action [SetVariable("sandan_x_new", 400), SetVariable("sandan_y_new", 500), Jump("check_sandan_coordinates")]
        hotspot ( 450, 450, 100, 100) action [SetVariable("sandan_x_new", 500), SetVariable("sandan_y_new", 500), Jump("check_sandan_coordinates")]
        hotspot ( 550, 450, 100, 100) action [SetVariable("sandan_x_new", 600), SetVariable("sandan_y_new", 500), Jump("check_sandan_coordinates")]
        hotspot ( 650, 450, 100, 100) action [SetVariable("sandan_x_new", 700), SetVariable("sandan_y_new", 500), Jump("check_sandan_coordinates")]
        hotspot ( 750, 450, 100, 100) action [SetVariable("sandan_x_new", 800), SetVariable("sandan_y_new", 500), Jump("check_sandan_coordinates")]
        hotspot ( 850, 450, 100, 100) action [SetVariable("sandan_x_new", 900), SetVariable("sandan_y_new", 500), Jump("check_sandan_coordinates")]


        hotspot (  50, 550, 100, 100) action [SetVariable("sandan_x_new", 100), SetVariable("sandan_y_new", 600), Jump("check_sandan_coordinates")]
        hotspot ( 150, 550, 100, 100) action [SetVariable("sandan_x_new", 200), SetVariable("sandan_y_new", 600), Jump("check_sandan_coordinates")]
        hotspot ( 250, 550, 100, 100) action [SetVariable("sandan_x_new", 300), SetVariable("sandan_y_new", 600), Jump("check_sandan_coordinates")]
        hotspot ( 350, 550, 100, 100) action [SetVariable("sandan_x_new", 400), SetVariable("sandan_y_new", 600), Jump("check_sandan_coordinates")]
        hotspot ( 450, 550, 100, 100) action [SetVariable("sandan_x_new", 500), SetVariable("sandan_y_new", 600), Jump("check_sandan_coordinates")]
        hotspot ( 550, 550, 100, 100) action [SetVariable("sandan_x_new", 600), SetVariable("sandan_y_new", 600), Jump("check_sandan_coordinates")]
        hotspot ( 650, 550, 100, 100) action [SetVariable("sandan_x_new", 700), SetVariable("sandan_y_new", 600), Jump("check_sandan_coordinates")]
        hotspot ( 750, 550, 100, 100) action [SetVariable("sandan_x_new", 800), SetVariable("sandan_y_new", 600), Jump("check_sandan_coordinates")]
        hotspot ( 850, 550, 100, 100) action [SetVariable("sandan_x_new", 900), SetVariable("sandan_y_new", 600), Jump("check_sandan_coordinates")]





        if current_worldroom.wr_south != -1:
            hotspot ( 0, 653, 1000, 100) action [SetVariable("sandan_x_new", 500), SetVariable("sandan_y_new", 700),  Jump("check_sandan_coordinates")]

        if current_worldroom.wr_west != -1:
            if current_worldroom.wr_name == 'wroom12':
                hotspot ( 0, 0, 45, 720) action [SetVariable("sandan_x_new", 0), SetVariable("sandan_y_new", 600),  Jump("check_sandan_coordinates")]
            else:
                hotspot ( 0, 0, 45, 720) action [SetVariable("sandan_x_new", 0), SetVariable("sandan_y_new", 300),  Jump("check_sandan_coordinates")]

        if current_worldroom.wr_north != -1:
            hotspot ( 0, 0, 1000, 50) action [SetVariable("sandan_x_new", 500), SetVariable("sandan_y_new", 0),  Jump("check_sandan_coordinates")]


        if current_worldroom.wr_east != -1:
            if current_worldroom.wr_name == 'wroom11':
                hotspot ( 955, 0, 50, 720) action [SetVariable("sandan_x_new", 1000), SetVariable("sandan_y_new", 600),  Jump("check_sandan_coordinates")]
            else:
                hotspot ( 955, 0, 50, 720) action [SetVariable("sandan_x_new", 1000), SetVariable("sandan_y_new", 300),  Jump("check_sandan_coordinates")]






label b4_check_walkingdirection:


    if b4_walkingdirection == 'up':
        $ previous_worldroom = current_worldroom
        $ current_worldroom = worldroom_list[current_worldroom.wr_north]

        $ sandan_y = 600
        $ sandan_y_new = 600
        $ sandan_x = 500
        $ sandan_x_new = 500

        jump b4_draw_worldroom

    elif b4_walkingdirection == 'down':
        $ previous_worldroom = current_worldroom
        $ current_worldroom = worldroom_list[current_worldroom.wr_south]

        $ sandan_y = 100
        $ sandan_y_new = 100
        $ sandan_x = 500
        $ sandan_x_new = 500

        jump b4_draw_worldroom

    elif b4_walkingdirection == 'left':
        $ previous_worldroom = current_worldroom
        $ current_worldroom = worldroom_list[current_worldroom.wr_west]

        $ sandan_x = 900
        $ sandan_x_new = 900
        $ sandan_y = 500
        $ sandan_y_new = 500


        jump b4_draw_worldroom

    elif b4_walkingdirection == 'right':
        $ previous_worldroom = current_worldroom
        $ current_worldroom = worldroom_list[current_worldroom.wr_east]

        $ sandan_x = 100
        $ sandan_x_new = 100
        $ sandan_y = 500
        $ sandan_y_new = 500

        jump b4_draw_worldroom





label b4_label_citystreets_arrival:

    scene
    call start_worldrooms from _call_start_worldrooms
    hide screen travel_easier        

    show expression "bk4/worldrooms/bg_002.jpg"
    show expression "bk4/worldrooms/oogi_fly.png":
        ypos -200
        linear 0.4 ypos 0
    pause(0.4)

    hide expression "bk4/worldrooms/oogi_fly.png"
    show expression "bk4/worldrooms/oogi_landed.png"

    $ current_worldroom = worldroom2

    $ sandan_x_new = 600
    $ sandan_y_new = 400
    $ sandan_x = 400
    $ sandan_y = 200

    if lin_rub_equal ==2:
        jump lin_rub_cont

    jump b4_draw_worldroom




label b4_label_sai_arrival:


    scene
    call start_worldrooms from _call_start_worldrooms_1
    hide screen travel_easier     

    show expression "bk4/worldrooms/bg_010.jpg"
    show expression "bk4/worldrooms/aang_statue.png"

    show expression "bk4/worldrooms/oogi_fly.png":
        ypos -200
        linear 0.4 ypos 0
    $ renpy.pause(0.4)
    hide expression "bk4/worldrooms/oogi_fly.png"
    show expression "bk4/worldrooms/oogi_landed.png"

    $ current_worldroom = worldroom10

    $ sandan_x_new = 500
    $ sandan_y_new = 500
    $ sandan_x = 400
    $ sandan_y = 200


    jump b4_draw_worldroom




label b4_onaboat:


    "Boattime!"
    jump b4_draw_worldroom



label b4_label_bioculars:

    hide screen travel_easier 

    menu:
        b4_tn "It wants a coin to operate."
        "No way!":

            pass
        "Well... what do I have to lose?":

            if bk4_money >=1:
                play sound "audio/money.mp3"
                $ bk4_money -=1
                "you look through the telescope."
                show black with dissolve
                show ctc
                pause
                hide ctc
                tn "...."
                tn "what..."
                tn "this thing doesn't even work!"
                hide black
                b4_ta "Damn it!"
                ta "Give me back my coin!"
                "the telescope doesn't respond. smugly."
                ta "i hope your swivel breaks!"
                "the telescope remains strong in the face of your insults."
            else:
                tn "i don't have a coin."
                tn "...damn, i'm broke."

    $ sandan_x_new = 500
    $ sandan_y_new = 300

    jump b4_draw_worldroom




label b4_label_ginger:
    hide screen travel_easier  




    menu:


        "audition" if become_a_star == 5 or become_a_star >= 7:
            show expression "bk4/worldrooms/bg_001.jpg"
            show bfat bfat08

            b4_tn "How about doing an \"audition\" ?"
            b4_tn "I'll audition you balls deep."
            gin "Follow me."
            call fuck_ginger_1 from _call_fuck_ginger_1
            jump b4_draw_worldroom
        "talk":

            show expression "bk4/worldrooms/bg_001.jpg"
            show bfat bfat08

            if become_a_star in [5, 7]:
                gin "Thanks again for scouting me!"

            elif become_a_star in [ 4, 6 ]:
                gin "I'm still waiting for you to make me a star."
                b4_tn "Soon!"


            elif become_a_star == 3:
                b4_tn "I found my camera."
                "You show your camera to the redhead. "
                show bfat bfat10
                "It's clearly convincing her you can help her career as she pushes her chest forward."
                gin "Now what was it again you were saying about turning me into a star?"
                b4_tn "Like I said earlier, I think you have a lot of really nice looking talent. However..."
                menu:
                    "Leave her panties alone":

                        $ become_a_star = 6
                        b4_tn "I don't think I'll need to take any photographs."
                        b4_tn "If all goes well a stuckup woman from \"Varrick Global Industries\" will contact you."
                        b4_tn "She'll take it from there. But don't forget, I was the one who got the ball rolling."
                        gin "If this really turns into something lucrative... I wouldn't mind rolling your balls."
                        gin "As thanks."
                    "Try to get into her panties":


                        $ become_a_star = 4
                        b4_tn "There's a lot of talented girls out there who'd like to become rich and famous."
                        b4_tn "You wouldn't believe what some of those young girls are willing to do."
                        b4_tn "You'll have to convince me I need to pick you over the others."
                        show bfat bfat09
                        gin "I see."
                        gin "Well, I can assure you I'm fully prepared to do whatever it takes."
                        b4_tn "Really?"
                        tn "Because you'd have to do an audition first to show me your ass...ets as an actor."
                        b4_tn "I'd have to plunge right into you...r pros and cons to see if you really have what it takes to make it in show business."
                        b4_tn "Do you think that'll be a problem?"
                        gin "Not at all. I'll **** and **** anyone or anything who can help me get to the top."
                        gin "And I have a good feeling about you!"
                        b4_tn "That's great to hear."
                        tn "but i'm more impressed with how you spoke asterisks."
                        tn "that's a rare talent."
                        gin "then how about this..."
                        gin "i'll suck and fuck your cock, however you want, if you make me famous."
                        b4_tn "...is there any place close by where I can give you your audition?"
                        gin "Sure, follow me."
                        "The girl takes you to a dilapitated building close by."

                        call fuck_ginger_1 from _call_fuck_ginger_1_1

                jump b4_draw_worldroom

            elif become_a_star == 2:
                gin "Do you have your camera?"
                b4_tn "Almost!"

            elif become_a_star == 1:
                b4_tn "Hi, I can see you have a lot of talent."
                b4_tn "I can take that talent and turn you into a star."
                b4_tn "You'll be famous and rich."
                gin "...."
                gin "So where's your business card?"
                b4_tn "Oh, right. Here it is."
                "You hand over Zhuli's card."
                gin "Are you like... a photographer?"
                b4_tn "Not really, but-"
                gin "Because I'll need to have some proof you're a professional."
                tn "then... yes."
                b4_tn "I'll... go get my camera."

                hide bfat


                b4_tn "Shit where do I get a camera?"
                b4_tn "Those are probably expensive as fuck.... Unless I can get a broken one?"
                b4_tn "I think I can wing it with something that only looks like the real deal."
                $ become_a_star = 2
                hide expression "bk4/worldrooms/bg_001.jpg"
            else:





                gin "Sorry, I'm busy right now."
                b4_tn "...okay."


            jump b4_draw_worldroom
        "exit":



            jump b4_draw_worldroom





    show screen travel_easier    
    $ renpy.pause()

    "broken 928"
    jump b4_draw_worldroom








label b4_label_zhuli:

    hide screen travel_easier  

    menu:
        "talk":

            show expression "bk4/worldrooms/bg_001.jpg"
            show bfazh bfazh01

            if lin_rub_quest >=2:
                if lin_rub_quest ==3:
                    zh "i have nothing else to say to you right now."
                    jump b4_draw_worldroom
                if lin_rub_quest ==2:
                    $ lin_rub_quest = 3
                    zh "i'm very busy, what did you want?"
                    tn "hello, how are you?"
                    zh "what do you want?"
                    tn "nice weather we're-"
                    zh "{i}what{/i} do you {i}want{/i}?"
                    tn "i guess cordiality is a lost art."
                    zh "...goodbye."
                    tn "wait, wait, hold on."
                    tn "i need more information on the equalists."
                    zh "...and what makes you think i know anything?"
                    tn "you've already helped me once."
                    tn "look, i'm not trying to put you or varrick in any shit, i just need {i}something{/i}."
                    tn "think of it this way, i'm in the perfect position to misdirect the police."
                    zh "mm."
                    zh "that... is not inaccurate."
                    tn "give me mostly fluff, but give me something real."
                    zh "and inexchange... a favor to be repaid at a later date?"
                    tn "you got it, toots."
                    zh "....."
                    zh "..........."
                    zh "very well."
                    zh "amon used to operate... out of the statue."
                    tn "wait, the avatar aang statue?"
                    tn "on statue island?"
                    zh "yes."
                    tn "but... i went in there!"
                    tn "nothing seemed out of place."
                    zh "there is a hidden room."
                    tn "dang. that's badass."
                    tn "but he's abandoned it?"
                    zh "he found better headquarters and viewed the statue as... a liability."
                    zh "amon prides himself on being mobile... and uncatchable."
                    zh "he has not earned that reputation by staying in one place for long..."
                    zh "...or by returning to old haunts."
                    tn "okay, okay, so, old amon hideout, safe from equalists and police."
                    zh "it appears that way."
                    tn "what can i do with that information?"
                    zh "there may be something of future industries there that could incriminate mr. sato."
                    tn "...why are you helping me get information on mr. sato?"
                    zh "future industries is a powerful force in the market, and if it is toppled..."
                    zh "...by acts of treason, for example..."
                    zh "...there would be a power vaccuum."
                    zh "varrick global industries would be forced to step in and fulfill the many, many unfulfilled contracts."
                    zh "it would be unfortunate, but we would take on the necessary burden."
                    tn "ah, so you're trying to get rid of a rival."
                    zh "nature hates a vaccuum, mr. tenzin-look-alike."
                    tn "hm."
                    tn "I'll have to think on this."
                    zh "don't harm yourself."
                    tn "ha. ha. ha."
                    tn "anything else you can give me?"
                    zh "well, it's a small thing, but there will be another equalist rally soon."
                    tn "where?"
                    zh "near here, in fact."
                    zh "in the streets."
                    tn "thanks, zhu li."
                    zh "don't thank me, just... be ready."
                    zh "you are substantially in our debt."
                    tn "yeah, i got it."
                    tn "jeez."
                    zh "good day."
                    jump b4_draw_worldroom


            if become_a_star == 6:
                b4_tn "See that redhead over there?"
                zh "Yeah, did you know she's using a product from us to color her hair?"
                zh "I gave her a free sample earlier."
                zh "I asked whether she wanted to become an actress for the movers, but she thought it was just a scam to sell her loads of hairdye."
                b4_tn "Well, I took care of it."
                tn "She'll be more receptive from now on."
                zh "That's good news!"
                b4_tn "I feel I've earned some sort of commission!"
                zh "ugh, very well, here."
                $ bk4_money +=20
                play sound "audio/money.mp3"
                "you got 20 coins!"
                tn "that's... not much..."
                zh "oh, and about the equalists..."
                tn "yes?"
                zh "i expect us to have a long, efficient, hard-working relationship."
                zh "is that understood?"
                tn "okay..."
                zh "in that case... here."
                play sound "audio/win2.mp3"
                "zhuli hands you a photo."
                tn "who... am i looking at?"
                zh "this is mr. sato."
                zh "head of sato industries."
                tn "this is asami's dad?!"
                zh "yes."
                zh "shaking hands with amon."
                zh "be careful with that."
                tn "(i can't give this to lin... i should save this as blackmail...)"
                tn "anything else you could give me? any information?"
                zh "well..."
                zh "here is the location of some outdated weapons."
                play sound "audio/win2.mp3"
                "zhuli hands you an address on a piece of paper."
                zh "it's in an anonymous warehouse, so it's untraceable."
                zh "and the weapons are certainly useless to us now."
                zh "good luck, mr. looks-like-tenzin."
                $ b4_zhuli_exists = False
                $ become_a_star = 7
                hide bfazh with Dissolve(1.5)
                jump b4_draw_worldroom



            elif become_a_star == 4:
                b4_tn "See that redhead over there?"
                zh "Yeah, I had my eye on her and even offered her an audition, but she thought I was joking."
                b4_tn "Really? Why?"
                zh "She said no serious headhunter had ever approached her without trying to get into her panties."
                zh "Since I'm not into that and didn't try she wouldn't believe me. "
                b4_tn "Well, I solved your problem."
                tn "Just approach her again and tell her I sent you."
                zh "For real?!"
                zh "That's...great! Wait, how did you....."
                b4_tn "Balls deep."
                tn "she couldn't stop herself from screaming while I was plowing her pussy... if you're wondering."
                zh "I wasn't."
                b4_tn "Anyway, I feel I've earned some sort of commission!"
                zh "You're a pig... but this does make things a lot easier for me so here's a pittance. "
                $ bk4_money +=20
                play sound "audio/money.mp3"
                "you got 20 coins!"
                tn "did i just get paid to fuck a redhead?"
                tn "truly this is the best timeline."
                zh "oh, and about the equalists..."
                tn "yes?"
                zh "i expect us to have a long, efficient, hard-working relationship."
                zh "is that understood?"
                tn "okay..."
                zh "in that case... here."
                play sound "audio/win2.mp3"
                "zhuli hands you a photo."
                tn "who... am i looking at?"
                zh "this is mr. sato."
                zh "head of sato industries."
                tn "this is asami's dad?!"
                zh "yes."
                zh "shaking hands with amon."
                zh "be careful with that."
                tn "(i can't give this to lin... i should save this as blackmail...)"
                tn "anything else you could give me? any information?"
                zh "well..."
                zh "here is the location of some outdated weapons."
                play sound "audio/win2.mp3"
                "zhuli hands you an address on a piece of paper."
                zh "it's in an anonymous warehouse, so it's untraceable."
                zh "and the weapons are certainly useless to us now."
                zh "good luck, mr. looks-like-tenzin."
                $ b4_zhuli_exists = False
                $ become_a_star = 5
                hide bfazh with Dissolve(1.5)
                jump b4_draw_worldroom

            elif become_a_star == 3:
                zh "Yes?"
                b4_tn "Let's say I find you some real talent for that mover business... will I get a finder's fee?"
                zh "That wouldn't be unreasonable."

            elif become_a_star == 2:
                b4_tn "Do you have a camera I can borrow?"
                zh "Absolutely not."

            elif become_a_star == 1:
                zh "Yes?"
                b4_tn "Let's say I find you some real talent for that mover business... will I get a finder's fee?"
                zh "That woudn't be unreasonable."

            elif become_a_star == 0:

                $ temp_int = 0

                menu:
                    b4_tn "This woman...."
                    "is clearly a prostitute":
                        $ temp_int = 1

                        b4_tn "I'm not usually into hookers, but I bet you'd look nice with your hair down."
                        b4_tn "Besides, it's been a long time since I fucked a girl with glasses."
                        b4_tn "Okay, you talked me into it. "
                        tn "Let's do this!"
                        tn "And by \"this\" I mean you."
                        zh "....."
                        b4_tn "So is this going to happen in an alley or do you have a cheap room close by?"
                        zh "i..."
                        b4_tn "Good choice on the prissy clothes and hairdo."
                        b4_tn "It has that stern schoolteacher vibe and it really makes me want to ravage you."
                        zh "i'm not-"
                        b4_tn "...leaving you exhausted afterwards, covered in sweat and my sperm."
                        tn "Your legs spread, pussy all gaping."
                        zh "I'm not a prostitute. sir."
                        tn "then why did i get a boner?"
                        zh "i'm... i... have no idea."
                        tn "you too, huh?"
                        tn "alright buddy, down."
                        tn "no, not right now. get down. stop it."
                        zh "...."
                        tn "can never control this thing."
                        zh "i... can imagine."
                        b4_tn "so what can i do for you?"
                    "is probably human":

                        b4_tn "Yes?"
                        zh "I'm sorry, but did you make that tenzin outfit yourself?"
                        zh "Do you do your own make-up?"
                        zh "Forgive my directness, but I could use someone with talents like that."
                        b4_tn "uh..."

                zh "I just thought that's a great cosplay outfit and makeup."
                zh "Would you like to work in show business?"
                b4_tn "cos... wait, you think i'm pretending to be tenzin?"
                tn "What makes you think I'm not the real Tenzin?"

                if temp_int == 1:
                    zh "I wasn't sure at first, but the way you approached me just now..."
                    zh "The real one is a boring but well respected council member. "
                else:
                    zh "The color of the arrows is wrong. Should be darker."

                b4_tn "Really..."
                tn "You know what? This works out fine for me."
                b4_tn "what sort of show business are you talking about?"
                zh "We're developing an entirely new sort of entertainment."
                zh "Moving pictures! We call them \"movers\"."
                b4_tn "Oh... uh, wow?"
                tn "Isn't that name already copyrighted?"
                b4_tn "\"movers\" sounds like... furniture haulers."
                zh "Well, that is how mister Varrick started his business."
                b4_tn "Varrick?"
                zh "As in \"Varrick Global Industries\". He already owns all the rights to the name."
                zh "I'm his assistant."
                b4_tn "Okay."
                zh "Ah, disbelief. But it's all true."
                zh "This new technology will revolutionize the entertainment industry."
                zh "Movers are the future and will undoubtedly come to dominate."

                if temp_int == 1:
                    b4_tn "Is... is it a porn mover?"
                    tn "Do you want me to star in a porn mover so I can bang chicks and get paid for it?!?"
                    zh "What?! {i}NO! "
                    zh "How could you come up with such a vile idea? We're not pornlove!"
                    b4_tn "Really? Well if you change your mind..."
                    zh "{i}NO!{/i} I just figured you'd be good at making clothes for the actors and actresses."
                else:
                    b4_tn "No, I believe you."
                    tn "In fact, I might have to invest in some of that company."
                    b4_tn "I'm convinced it's going to be big."
                    b4_tn "So what would you need me for?"
                    zh "Making clothes for the actors and actresses."

                zh "Here's my card."
                "Zhuli hands you a black card with a fine gold imprint."
                "It says: \"Varrick Global Industries\"."
                b4_tn "I'll have to think it over."
                zh "Certainly."
                tn "but first..."
                tn "do you know anything about equalists?"
                zh "i might."
                tn "are you willing to tell me something?"
                zh "maybe."
                zh "if you find a way to make my life easier..."
                zh "...i'll consider it."

                $ become_a_star = 1
            else:


                zh "I'm busy right now."


            hide expression "bk4/worldrooms/bg_001.jpg"
            hide bfazh
        "exit":







            pass



    show screen travel_easier
    $ renpy.pause()
    "broken 866"


label b4_inside_aangstatue:

    if statue_key:
        if korra_scroll2 <2:
            play sound "audio/door_open.mp3"
            "the mysterious key fits in the lock!"
            tn "neat!"

        scene
        hide screen travel_easier    
        show expression "bk4/worldrooms/aangstatue_inside.jpg":
            ypos 0

        if lin_rub_quest >=3:
            if not sato_weapon:
                tn "still nothing here..."
                tn "hmm... there has to be a switch somewhere."
                hide black
                show black with dissolve
                "you look around the room for a few minutes."
                tn "there!"
                play sound "audio/door4.mp3"
                "you find a hidden latch and a wall opens..."
                scene expression "bk4/backgrounds/bg_hangkorra.jpg":
                    ypos -300
                with dissolve
                tn "oh, yes."
                tn "this will do nicely."
                tn "now let's look for something incriminating on mr. sato..."
                "you look around the room."
                "there's a box in a corner."
                tn "what's this?"
                play sound "audio/win2.mp3"
                "there's a futuristic, prototype-looking weapon with \"future industries\" emblazoned on the side."
                tn "ah, i've got you now."
                tn "time to call asami."
                $ sato_weapon = True
            else:
                tn "this room will come in handy."

        if korra_scroll2 <2:
            tn "hm. i like this room."
            tn "this is a nice room."
            tn "oh, there's something on the ground..."
            tn "it's an airbending scroll!"
            play sound "audio/win2.mp3"
            "you found an airbending scroll."
            tn "neat, again!"
            $ korra_scroll2 = 2
            $ b4_daytime = False

        if not sato_weapon:
            tn "this room has potential."
            tn "i'll think of something."
    else:

        tn "there's a locked door hidden in the shadows."
        tn "i wonder where the key is?"

    $ sandan_x_new = 800
    $ sandan_y_new = 400
    $ sandan_x = 900
    $ sandan_y = 300

    jump b4_draw_worldroom
    "broken 94741"





label b4_label_nagaprime:




    hide screen travel_easier 
    "{b}Ah, you're back!"
    if worldroom16.wr_content == 0:
        b4_yn "I'm pretty sure this is the first time I'm here?"
        "{b}Hmmmm... maybe from your perspective."
    elif worldroom16.wr_content == 1:
        b4_yn "yeah, there is nothing else here."
        b4_yn "so... this time i'm back for real."
        "{b}real, unreal... what's the difference?"
        b4_yn "There's a difference... there's a big difference."
        b4_yn "Say... can you teleport me out of here or something?"
        "{b}sure. Here you go."
        $ worldroom16.wr_content = 2
        $ current_worldroom = worldroom14
        jump b4_draw_worldroom

    elif worldroom16.wr_content == 2:

        b4_yn "This sucks."
        b4_yn "I don't wanna spend the rest of my life alone... in this weird place."
        b4_yn "No offense, but I need less scaly beings around for my sanity."
        "{b}Mmmm... alone... I never considered the concept of being alone."
        "{b}You know what?"
        "{b}I think I'll split myself into two."
        "{b}It'll be fun!"
        "{b}Always someone else to talk to."
        "{b}Someone asss sssmart and pretty asss I am."
        b4_yn "what just happened to your s's?"
        b4_yn "Wait, that sounds like a bad idea."
        b4_yn "if you're gonna do that at least wait till I'm away."
        "{b}Didn't you become one with a spirit?"
        "{b}why can't I become two?"
        "{b}It'll be twice the fun."
        b4_yn "No, seriously, don't start experimenting while i'm stuck hanging around here!"
        "{b}Too late!"
        "{b}My mind is made up."

        show text "rip!" with hpunch
        scene black
        b4_yn "oooh... my head... feels weird."


        $ current_worldroom = worldroom17
        jump b4_draw_worldroom




    menu:
        "Who are you":
            "{b}I'm Naga, the great serpent."
            "{b}I command time, dreams, illusions and a couple of other things."
            b4_yn "Oh, that's really impressive and not at all scary."
            b4_yn "Gotta go now."
            $ sandan_x_new = 600
            $ sandan_y_new = 400
            $ worldroom16.wr_content = 1







    show screen travel_easier
    jump b4_draw_worldroom
    "broken 886"



label b4_label_nagachibi:

    hide screen travel_easier 



    if current_worldroom.wr_content == 0:
        $ current_worldroom.wr_content = 1


    if sandan_x == 800 and sandan_y in [100,200]:

        if current_worldroom.wr_content == 3:
            "{i}I think it's best if you get out of here."
            "{i}I don't really like how my \"sister\" is eyeing you."
            "{i}I don't even like how ssshe's eyeing me!"
            b4_yn "How do I get out of here?"
            "{i}I'm not sure, but do it soon."

            $ current_worldroom.wr_content = 4

            "You close your eyes and try to find your center."
            b4_yn "yeah, i have no idea what i'm-"
            scene black with Dissolve(1.5)
            $ sandan_character = 'tenzin'
            jump b4_meet_kyoshi_1

        if current_worldroom.wr_content == 1:
            "{i}I thought this would be a lot more fun, but my other ssself is..."
            "{i}not really all that nice."
            b4_yn "Can you turn things back to how it was?"
            "{i}I can't reunite with her, not without her cooperation."
            "{i}I don't think we sssplit evenly.."
            b4_yn "Great... "

            $ current_worldroom.wr_content = 2








    elif sandan_x == 200 and sandan_y in [100,200]:

        if current_worldroom.wr_content == 3:
            "The snake-lady is looking at you while licking her lips."

        elif current_worldroom.wr_content == 2:
            "{i}I thought this would be a lot more fun, but my other ssself is..."
            "{i}...a dumb bitch."
            b4_yn "Can't you... like... unsplit yourself?"
            "{i}sssilence! I'll do as I wish!"
            "{i}This is all your fault to begin with!!"
            "{i}Anger me and I'll eat you... fatten myself with your spiritual energy..."
            b4_yn "........"
            b4_yn "fuck that..."
            $ current_worldroom.wr_content = 3

            show screen travel_easier 

            $ sandan_x_new = 500
            $ sandan_y_new = 300

            jump check_sandan_coordinates

        elif current_worldroom.wr_content == 1:
            "The snakelady just stares at you in a very creepy way."
















    show screen travel_easier
    jump b4_draw_worldroom
    "broken 886"



label b4_label_oogi_takeoff:
    hide screen travel_easier 

    hide im_sandan
    hide expression "bk4/worldrooms/oogi_landed.png"
    show expression "bk4/worldrooms/oogi_fly.png":
        ypos 0
        linear 1.0 ypos -500
    $ renpy.pause(1.0)

    menu:
        "Aang statue island":
            jump b4_label_sai_arrival
        "city streets":
            jump b4_label_citystreets_arrival
        "leave":
            if not b4_daytime:
                jump b4_airtemple_map1
            else:
                jump b4_repcity_map1






label b4_label_treehouse:

    if sandan_x == 600 and sandan_y == 200:
        $ sandan_x_new = 600
        $ sandan_y_new = 100
        jump b4_draw_worldroom

    hide screen travel_easier


    show expression "bk4/worldrooms/bg_treehouse.jpg"
    menu:
        "Look around":
            b4_tn "Hmmm.... just a kids' treehouse."
            "You see a heap of mostly broken junk in one of the corners."
            b4_tn "Some kid's treasure."
            if become_a_star in [1,2]:
                $ become_a_star = 3
                b4_tn "Hey! This... yep a camera!"
                tn "It's all rusted inside, but it looks fine from the outside."
            else:
                tn "maybe something here will be useful later, but not right now."
                tn "i mean... what am i going to do with an old cup? or a camera?"
        "exit":



            pass

    $ sandan_x_new = 600
    $ sandan_y_new = 300
    $ sandan_x = 600
    $ sandan_y = 100

    show screen travel_easier    
    jump b4_draw_worldroom

    "broken 898"


label b4_label_chibijinora:

    hide screen travel_easier


    menu:
        "talk":
            show bfae jinora02
            if pema_bj <2:
                b4_tn "hey Jinora, what're you doing?"
                jino "Just feeding the koi."
                b4_tn "Oh. cool."
            if pema_bj >2:
                tn "Wow... you really make sure those Koi stay fed don't you?"
                jino "someone has to!"
            else:
                b4_tn "you're spending a lot of time with these fish."
                jino "i like them!"
                tn "ah."
                tn "well."
                tn "...i think we need to have a talk."
                jino "okay!"
                jino "about what?"
                tn "about... your feelings."
                show bfae jinora03 with dissolve
                jino "oh... um... it's not really... it's fine..."
                jino "i think i can hear mom calling me..."
                tn "...."
                tn "...we're on a completely different island."
                tn "i mean, pema can yell, probably, but..."
                tn "look, let's just address this, and then it's over."
                jino "I just..."
                jino "i've always thought you were pretty cool..."
                jino "and you spend so much time training with korra..."
                jino "and it made me a bit... jealous."
                tn "well, jinora... korra is as good at airbending as you are at firebending."
                tn "and by that, i mean she's fucking terrible."
                tn "sorry, swearing."
                tn "but she's genuinely terrible."
                tn "...and it's not my fault."
                tn "so she needs a lot of training."

                jino "maybe... that's not the only thing i'm jealous about..."
                menu:
                    "ew ew ew {size=+5}ew ew ew!! no! ew!! gross!!! ugh! why?!! no!":
                        pass
                    "absolutely not":
                        pass
                    "your feelings will pass":
                        pass
                    "that's normal, but the answer is no":
                        pass
                    "well...":
                        menu:
                            "{size=+5}that's a horrible, horrible idea":
                                pass
                            "i'm sorry, but no":
                                pass
                            "that's a terrible idea":
                                pass
                            "i can't even think about it":
                                pass
                            "be ambiguous about it (and fail her as a father and human being)":
                                $ jinora_interest = True

                if not jinora_interest:
                    tn "i'm sorry jinora, but no."
                    tn "that's very, very far away from possible."
                    show bfae jinora10 with dissolve
                    tn "don't be upset."
                    tn "your feelings are completely natural, and they will pass."
                    jino "r-really?"
                    tn "yes, i promise."
                    jino "okay..."
                    show bfae jinora03 with dissolve
                    jino "i won't bring it up again."
                    show bfae jinora02 with dissolve
                    jino "thanks for the chat!"
                if jinora_interest:
                    tn "i promise to consider it."
                    show bfae jinora02 with dissolve
                    jino "okay!"
                    tn "(thank goodness for time travel and the fact that this isn't my real body.)"

                tn "come on, let's go home."
                jino "okay, i'll go on ahead."
                $ b4_jinora_exists = False
                $ b4_daytime = False
                $ pema_bj = 3

            hide bfae
        "leave":

            pass



    show screen travel_easier
    $ renpy.pause()

    "error 565 - shouldn't be reached"
    jump b4_draw_worldroom



label b4_label_chibikorra:


    hide screen travel_easier   


    menu:
        "talk":



            show expression "bk4/worldrooms/bg_012.jpg"
            show bfab bfab04
            with Dissolve(1.5)
            if korra_spank_bj ==3:
                if not bk4_rope or not amon_outfit:
                    tn "(some more gear would be helpful right now...)"
            if korra_spank_bj ==3 and bk4_rope and amon_outfit:
                hide screen bk4_money_date
                with dissolve
                kn "hey, what are you doing here?"
                tn "i wanted to come give you your protein shake."
                tn "thanks!"
                show bfab bfab09 with dissolve
                kn "i'll start stretching while you mix up my protein supplement."
                hide bfab
                with dissolve
                tn "well, it's now or never..."
                show bfar bfar00
                tx "here we go..."

                play sound "audio/splurt2.ogg"
                show bfar bfar00a with hpunch
                show bfar bfar00
                pause(0.5)
                play sound "audio/splurt3.ogg"
                show bfar bfar00a with hpunch
                show bfar bfar00
                pause(0.5)
                play sound "audio/splurt1.ogg"
                show bfar bfar00a with hpunch
                hide bfar
                with dissolve
                "you tuck away your cock, and drop the powder into the drink."
                tn "ahem."
                tn "korra?"
                show bfar bfar01
                with dissolve
                kn "hey, yeah, is it ready?"
                show bfar bfar02
                tn "yup, here you go!"
                show bfar bfar03
                kn "thanks."
                show bfar bfar05
                "korra drinks it all down."
                "guzzling your cum and the sleeping powder with eagerness."
                show bfar bfar07
                kn "tastes a little different..."
                tn "does it?"
                show bfar bfar06
                kn "yeah, but not in a bad way."
                show bfar bfar08
                kn "just different, you know?"
                hide bfar with dissolve
                show bfab bfab28 with dissolve
                kn "now if you don't mind, I need to get back to..."
                show bfab bfab29 with dissolve
                kn "to... to..."
                kn "...something..."
                kn "....."
                play sound "audio/thud.mp3"
                hide bfab with moveoutbottom
                "*thud*" with hpunch
                "korra passes out hard."
                tn "...."
                tn "wow."
                tn "shady knows his stuff."
                scene black with dissolve
                "making sure no one is around, you pick korra up...."
                "....you carry her into the statue...."
                "....and you wait for her to awaken."
                show ctc
                pause
                hide ctc
                jump korra_blowjob1






            tn "how's it going?"
            kn "just getting in some exercise."
            if b4_jinora_exists:
                kn "jinora's around, by the way."
        "exit":





            pass


    jump b4_draw_worldroom




label b4_move_actor1:


    hide expression b4_locals[0][2][2]
    hide expression b4_locals[0][2][1]
    show expression b4_locals[0][2][0]:
        xpos korra_xpos ypos korra_ypos
    $ renpy.pause(1.0)


    hide expression b4_locals[0][2][2]
    hide expression b4_locals[0][2][1]
    show expression b4_locals[0][2][0]

    $ korra_xpos_new  = renpy.random.choice([500,700])
    $ korra_ypos_new  = renpy.random.choice([500,300])

    if korra_xpos_new == korra_xpos:
        jump b4_move_actor1


    if korra_xpos_new > korra_xpos:
        hide expression b4_locals[0][2][0]

        show expression b4_locals[0][2][2]:
            xanchor 0.5 yanchor 0.5
            xpos b4_locals[0][0] ypos b4_locals[0][1]
            linear 2.0 xpos korra_xpos_new ypos korra_ypos_new xanchor 0.5 yanchor 0.5
    else:


        hide expression b4_locals[0][2][0]

        show expression b4_locals[0][2][1]:
            xanchor 0.5 yanchor 0.5
            xpos b4_locals[0][0] ypos b4_locals[0][1]
            linear 2.0 xpos korra_xpos_new ypos korra_ypos_new xanchor 0.5 yanchor 0.5

    $ korra_xpos = korra_xpos_new
    $ korra_ypos = korra_ypos_new

    $ b4_locals[0][0] = korra_xpos
    $ b4_locals[0][1] = korra_ypos

    $ renpy.pause(2.0)

    hide expression b4_locals[0][2][2]
    hide expression b4_locals[0][2][1]

    show expression b4_locals[0][2][0]:
        xpos b4_locals[0][0] ypos b4_locals[0][1]

    $ renpy.pause(2.0)

    jump b4_move_actor1

    "error 738 - should not be reached"
    jump check_sandan_coordinates





label fuck_ginger_1:
    stop music
    play music "audio/Unwritten Return.mp3"
    hide screen bk4_money_date
    hide bfat
    show expression "bk4/worldrooms/bg_room_01.jpg":
        ypos 0
    show bfat bfat08
    $ renpy.pause()

    show expression "bk4/worldrooms/bg_room_01.jpg" at Move((0, 0), (0, -400), 4.0, bounce = True, repeat = False, delay=4.0)
    show bfat bfat08 at Move((0, 0), (0, -400), 4.0, bounce = True, repeat = False, delay=4.0)
    $ renpy.pause(4.0)

    show expression "bk4/worldrooms/bg_room_01.jpg":
        ypos 0
    hide bfat
    show bfat bfat08

    b4_tn "Show me the goods!"

    show expression "bk4/worldrooms/bg_room_01.jpg":
        ypos -400
    show bfat bfat01
    with dissolve
    show ctc
    pause
    hide ctc
    b4_tn "That's a nice looking behind."
    tn "you do this often?"
    gin "only when a serious role is on the table."

    show bfat bfat01a
    tn "well... i'm being totally honest with you."
    tn "you can trust me."
    gin "i... i hope so."

    show bfat bfat02 with Dissolve(1.5)
    show ctc
    pause
    hide ctc
    b4_tn "Raise your hips."
    gin "if... okay..."

    show bfat bfat03 with Dissolve(1.5)
    gin "like this?"
    show ctc
    pause
    hide ctc
    gin "Could you put it in sl-"

    show bfat bfat03a at Move((0, 0), (0, -20), .10, bounce=True, repeat=True, delay=.275)
    gin "Aahh!"
    show ctc
    pause
    hide ctc

    show bfat bfat04

    gin "uhhnngh...."
    show ctc
    pause
    hide ctc
    b4_tn "Showbiz is a cutthroat business."
    tn "you gotta be prepared to deal with a little pain."
    gin "...uhhgh..."
    gin "yes... I'll..."
    gin "i'll do whatever it takes to become a star!!"
    tn "convince me."
    gin "give... give it to me! give me your cock, sir!"
    gin "stuff my tight pussy!"
    b4_tn "Good. I like your attitude. In fact... I love it."



    show bfat bfat05
    gin "ahhn...."
    show ctc
    pause
    hide ctc

    b4_tn "Do your parents know you're looking for a career in show business?"
    gin "Hnngh, they... they think I'm still in college."
    gin "For accounting."
    b4_tn "That sounds boring."


    hide bfat

    show bfat bfat06:
        xpos 20
        easeout 0.2 xpos 0
        linear 0.5 xpos 20
        repeat
    gin "{size=+10}Ah!AH! AAAH!!{/size}"
    show ctc
    pause
    hide ctc
    b4_tx "That's it... take it like a bitch!"
    b4_tx "Take it all in!"
    b4_tx "If you're able walk away in a straight line after this... "
    gin "{size=+5}ah! ah! unngh! ahhh!"
    b4_tx "I'll consider it a failure on my part!"
    gin "Sss... slow down!!"
    show ctc
    pause
    hide ctc

    hide bfat
    show bfat_body_b:
        ypos -30
        easein 0.5 ypos -60
        repeat

    show bfat bfat07:
        ypos 0
        easeout 0.5 ypos -40
        repeat

    gin "Ah...!!!"
    gin "it... you're stretching it so wide!!!"
    b4_tn "GOOD!!"
    show ctc
    pause
    hide ctc
    b4_tn "Do you have a preference where I come?"
    gin "I-"
    b4_tn "Because I don't care what you want!"

    show ctc
    pause
    hide ctc


    menu:
        "inside":
            hide bfat_body_b
            hide bfat
            play sound "audio/splurt2.ogg"
            show bfat bfat03a at Move((0, 20), (0, -20), .20, bounce=True, repeat=True, delay=.275)
            b4_tx "Once!"
            play sound "audio/splurt3.ogg"
            show bfat bfat03a at Move((0, 20), (0, -20), .20, bounce=True, repeat=True, delay=.275)
            b4_tx "Twice!"
            play sound "audio/splurt1.ogg"
            show bfat bfat03a at Move((0, 20), (0, -20), .20, bounce=True, repeat=True, delay=.275)
            b4_tx "Done!"
            hide bfat
            show bfat bfat03b
            with Dissolve(1.5)
            "You step back, and as your cock slides out of ginger's pussy, the sperm flows back out."
            "ginger tries to catch it."
            gin "There's so much..."
        "outside":

            hide bfat_body_b
            hide bfat
            play sound "audio/splurt2.ogg"
            show bfat bfat01b at Move((0, 0), (10, 0), .10, bounce=True, repeat=False, delay=.275)
            hide bfat
            show bfat bfat01b

            show bfat_spermshot
            show expression "bk4/ginger/vag/spermonbut_1.png" with hpunch
            $ renpy.pause()
            play sound "audio/splurt3.ogg"
            show bfat_spermshot
            show expression "bk4/ginger/vag/spermonbut_2.png" with hpunch
            $ renpy.pause()
            play sound "audio/splurt1.ogg"
            show bfat_spermshot
            show expression "bk4/ginger/vag/spermonbut_3.png" with hpunch
            $ renpy.pause()
            b4_tx "And DONE!!!!"

    show ctc
    pause
    hide ctc

    gin "Aahhh... you're an animal..."
    b4_tn "Thanks!"


    gin "so will... will i be a star?"
    tn "sure, i'll get right on that."
    show ctc
    pause
    hide ctc
    $ b4_music_day_on = False
    return


label b4_meet_kyoshi:
    hide screen bk4_money_date 
    with dissolve
    "your dreams begin to take an odd turn..."
    stop music
    play music "audio/Blue_Dot_Sessions_-_05_-_Thread_of_Clouds.mp3"

    show expression "bk4/worldrooms/bg_dreamscape_1.jpg"
    with Dissolve(1.5)
    show bfay bfay00x:
        alpha 0.0 xpos -500
        linear 2.0 alpha 0.4 xpos 0
    kyo "Avatar..."
    b4_yn "whoa! what?"
    b4_yn "Is this a dream?"
    b4_yn "It feels dreamy."
    b4_yn "Hey... you look a lot like a girl I know..."
    kyo "I'm avatar Kyoshi, an avatar from the past."

    b4_yn "Oh... right."
    b4_yn "Well, Suki is a hardcore {i}fan{/i} of yours."
    b4_yn "get it?"
    b4_yn "because you use-"
    kyo " Wait a second..."
    show bfay bfay00x:
        linear 3.0 alpha 1.0
    pause(1.0)
    show bfay bfay02x:
        alpha 1.0
    with dissolve
    kyo "Can you see me better now?"
    b4_yn "oh, yeah."
    b4_yn "hey."
    b4_yn "You really do have that fan theme going on."
    b4_yn "could you help me to learn airbending? "
    b4_yn "I assume you know a lot about it?"
    show bfay bfay01x
    kyo "I'm here to help... yes, but not with that."
    kyo "You're having other problems..."
    b4_yn "I... well, I guess? "
    show bfay bfay01x
    kyo "You don't even know the cause of why you're here."
    b4_yn "I'm pretty sure I do."
    show bfay bfay02x
    kyo "Dig deeper."
    kyo "Go deep within yourself, meditate on the cause of your current predicament."
    kyo "The cause of why you're here."
    b4_ya "You want me to meditate in a dream?"
    b4_ya "Is that even possible?"
    b4_ya "I'm not sure I'm ready for this!"
    show bfay bfay03x with vpunch
    kyo "Then become ready!"
    $ temp_int = 1
    scene black with Dissolve(3.0)


    call start_worldrooms from _call_start_worldrooms_2

    $ current_worldroom = worldroom14

    $ sandan_x_new = 600
    $ sandan_y_new = 400
    $ sandan_x = 400
    $ sandan_y = 200

    $ sandan_character = 'spirit'


    jump b4_draw_worldroom

label b4_meet_kyoshi_1:
    scene black
    show expression "bk4/worldrooms/bg_dreamscape_1.jpg"
    show bfay bfay01x
    with Dissolve(2.0)
    b4_yn "oh. hey. that actually worked."
    b4_ya "What was all of that?" with hpunch
    b4_ya "Was that the past, or a memory, or what?"
    kyo "You're meddling with an old, powerful spirit that caused a fracture a long time ago."
    b4_ya "Hey, wait a minute!"
    b4_ya "if you didn't say all that shit about going deeper, none of this would've ever happened!"
    kyo "It was unavoidable because one way or another it already happened."
    b4_ya "That's bullshit!!"
    show bfay bfay03x with hpunch
    kyo "And now it's your shit... to deal with."
    show bfay bfay01x
    b4_ya "So the nagas I've met are fractures of the original and I somehow had a hand in that?"
    b4_ya "Do... do I need to glue them together?"
    b4_ya "do they make spirit-glue or something...?"
    kyo "I don't know."
    kyo "But be wary of deception."
    kyo "Don't let nice tits or ass distract you when the time comes to take action."
    b4_yn "but... that's my weakness."

    show bfay bfay00x with dissolve
    show bfay bfay00x:
        linear 2.0 alpha 0.5
    b4_yn "of course that's going to distract me."
    kyo "Appearances are just that... appearances."
    scene white
    show ctc
    pause
    hide ctc
    b4_yn "what the fuck..."
    with flash
    jump b4_airtemple_map1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
