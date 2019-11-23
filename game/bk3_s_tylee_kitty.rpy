

image tylee tylee01 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/tylee/cat/bg.jpg",
    (0, 0), "bk3/tylee/cat/body_tylee.png",
    (0, 0), ConditionSwitch(        
        "catform == True", "bk3/tylee/cat/catform.png",
        "catform == False", "bk3/tylee/cat/transparent.png"), 
    (0, 0), ConditionSwitch(        
        "cattop == True", "bk3/tylee/cat/top.png",
        "cattop == False", "bk3/tylee/cat/transparent.png"), 
    (0, 0), ConditionSwitch(        
        "catbottom == True", "bk3/tylee/cat/bottom.png",
        "catbottom == False", "bk3/tylee/cat/transparent.png"), 
    (0, 0), "cat_blinkin",
    )

image tylee tylee02 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/tylee/cat/bg.jpg",
    (0, 0), "bk3/tylee/cat/body_tylee.png",
    (0, 0), ConditionSwitch(        
        "catform == True", "bk3/tylee/cat/catform.png",
        "catform == False", "bk3/tylee/cat/transparent.png"),  
    (0, 0), ConditionSwitch(        
        "cattop == True", "bk3/tylee/cat/top.png",
        "cattop == False", "bk3/tylee/cat/transparent.png"), 
    (0, 0), ConditionSwitch(        
        "catbottom == True", "bk3/tylee/cat/bottom.png",
        "catbottom == False", "bk3/tylee/cat/transparent.png"), 
    (0, 0), "bk3/tylee/cat/surprise.png",
    (0, 0), "cat_blinkin",
    )

image tylee tylee03 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/tylee/cat/bg.jpg",
    (0, 0), "bk3/tylee/cat/body_tylee.png",
    (0, 0), ConditionSwitch(        
        "catform == True", "bk3/tylee/cat/catform.png",
        "catform == False", "bk3/tylee/cat/transparent.png"),  
    (0, 0), ConditionSwitch(        
        "cattop == True", "bk3/tylee/cat/top.png",
        "cattop == False", "bk3/tylee/cat/transparent.png"), 
    (0, 0), ConditionSwitch(        
        "catbottom == True", "bk3/tylee/cat/bottom.png",
        "catbottom == False", "bk3/tylee/cat/transparent.png"), 
    (0, 0), "bk3/tylee/cat/surprise.png",
    (0, 0), "cat_blinkin",
    (0, 0), "cat_dickin",
    )

image tylee tylee04 = LiveComposite(
    (1000, 720),    
    (0, 0), "bk3/tylee/cat/bg.jpg",
    (0, 0), "bk3/tylee/cat/body_tylee.png",
    (0, 0), ConditionSwitch(        
        "catform == True", "bk3/tylee/cat/catform.png",
        "catform == False", "bk3/tylee/cat/transparent.png"),    
    (0, 0), ConditionSwitch(        
        "cattop == True", "bk3/tylee/cat/top.png",
        "cattop == False", "bk3/tylee/cat/transparent.png"), 
    (0, 0), ConditionSwitch(        
        "catbottom == True", "bk3/tylee/cat/bottom.png",
        "catbottom == False", "bk3/tylee/cat/transparent.png"), 
    (0, 0), "bk3/tylee/cat/surprise.png",
    (0, 0), "cat_blinkin",
    (0, 0), "cat_dickin_hard",
    )


image cat_dickin:

    "bk3/tylee/cat/dick1.png"
    0.3
    "bk3/tylee/cat/dick2.png"
    0.3
    "bk3/tylee/cat/dick3.png"
    0.3
    "bk3/tylee/cat/dick2.png"
    0.3
    repeat

image cat_dickin_hard:
    "bk3/tylee/cat/dick1.png"
    0.2
    "bk3/tylee/cat/dick3.png" with vshake
    0.5
    "bk3/tylee/cat/dick2.png"
    0.15
    repeat

image cat_blinkin:
    "bk3/tylee/cat/blink.png"
    0.3
    "bk3/tylee/cat/transparent.png"
    1.3

    repeat


screen kitty:
    vbox xalign 0.98 yalign 0.5:
        textbutton _("reset") action Jump("cat_start_over")
        textbutton _("cat") action Jump("cat_catform")
        textbutton _("top") action Jump("cat_top")
        textbutton _("bottom") action Jump("cat_bottom")
        textbutton _("stop") action Jump("cat_stop_pumpin")
        textbutton _("easy") action Jump("cat_dick_her1")
        textbutton _("hard") action Jump("cat_dick_her2")
        textbutton _("give her milk!") action Jump("cat_give_milk")
        textbutton _("end") action Jump("cat_end")

label cat_stop_pumpin:
    show tylee tylee01
    jump pussycrush2

label cat_bottom:
    if catbottom:
        $ catbottom = False
        jump pussycrush2
    else:
        $ catbottom = True
        $ catform = True
        jump cat_stop_pumpin

label cat_top:
    if cattop:
        $ cattop = False
        jump pussycrush2
    else:
        $ cattop = True
        jump pussycrush2

label cat_catform:
    if catform:
        $ catform = False
        $ catbottom = False
        jump pussycrush2
    else:
        $ catform = True
        jump pussycrush2


label cat_give_milk:
    scene black
    show expression "bk3/tylee/cat/bg.jpg"


    show tylee tylee03
    $ renpy.pause(2.0)


    play sound "audio/splurt3.ogg"
    $ renpy.pause(0.5)
    play sound "audio/splurt3.ogg"

    show tylee tylee01
    show expression "bk3/tylee/cat/came_in_pussy.png"
    with Dissolve(1.5)

    ty "Thanks for the pussy milk, mister!"
    $ renpy.pause(hard = True)

label pussycrush:
    hide screen earth_money_date
    $ catform = True
    $ cattop = True
    $ catbottom = True
    scene black with dissolve

    show expression "bk3/tylee/cat/white.png" with dissolve
    hide expression "bk3/tylee/cat/white.png"
    show tylee tylee01
    with dissolve

    ty "Hello mister, I'm just a lonely little kitty."
    ty "Can this poor pussy milk you?"







    jump pussycrush2

label pussycrush2:
    show screen kitty
    $ renpy.pause(hard = True)


label cat_dick_her1:
    $ catbottom = False
    show expression "bk3/tylee/cat/came_in_pussy.png"
    hide expression "bk3/tylee/cat/came_in_pussy.png"

    show tylee tylee03

    jump pussycrush2

label cat_dick_her2:
    $ catbottom = False

    show expression "bk3/tylee/cat/came_in_pussy.png"
    hide expression "bk3/tylee/cat/came_in_pussy.png"
    show tylee tylee04

    jump pussycrush2










label cat_end:
    ty "*purrrr....*"
    hide screen kitty
    jump bk3_village_background

label cat_start_over:
    $ catform = True
    $ cattop = True
    $ catbottom = True
    hide expression "bk3/tylee/cat/came_in_pussy.png"
    show tylee tylee01
    jump pussycrush2
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
