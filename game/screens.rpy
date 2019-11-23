











screen say(who, what, side_image=None, two_window=False):


    default side_image = None
    default two_window = False
    default side_xalign = 0.0
    default side_yalign = 0.94
    default who_window_style = "say_who_window"



    if not two_window:


        window:
            id "window"

            has vbox:
                style "say_vbox"

            if who:
                text who id "who"

            text what id "what"

    else:


        vbox:
            style "say_two_window_vbox"

            if who:
                window:
                    style "say_who_window"

                    text who:
                        id "who"

            window:
                id "window"

                has vbox:
                    style "say_vbox"

                text what id "what"


    if side_image:
        add side_image
    else:
        add SideImage() xalign side_xalign yalign side_yalign


    use quick_menu








screen choice:

    window:
        style "menu_window"
        xalign 0.5
        yalign 0.5

        has vbox:
            style "menu"
            spacing 2

        for caption, action, chosen in items:

            if action:

                if "(locked)" in caption:
                    $ caption = caption.replace("(locked)", "")
                    button:
                        action None
                        style "menu_choice_button"

                        text caption style "menu_choice"
                else:
                    button:
                        action action
                        style "menu_choice_button"

                        text caption style "menu_choice"

            else:
                text caption style "menu_caption"

init -2:
    $ config.narrator_menu = True

    style menu_window is default

    style menu_choice is button_text clear


    style menu_choice_button is button:
        xminimum int(config.screen_width * 0.51)
        xmaximum int(config.screen_width * 0.51)








screen input(prompt):

    window style "input_window":
        has vbox

        text prompt style "input_prompt"
        input id "input" style "input_text" color "#00008b"

    use quick_menu







screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"


        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id


        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0

    use quick_menu







screen main_menu() tag menu:





    window:
        style "mm_root"


    frame:
        style_group "mm"
        xalign .98
        yalign .98

        has vbox
        textbutton _("New Game") action Start()
        textbutton _("Load Game") action ShowMenu("load")
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("Help") action Help()
        textbutton _("Support Us!") action OpenURL("http://www.patreon.com/mity")
        textbutton _("Disclaimer") action ShowMenu("disclaimer")
        textbutton _("Quit") action Quit(confirm=False)

    text "v0.8.3c" xpos 10 ypos 10

init -2:


    style mm_button:
        size_group "mm"









screen navigation():


    window:
        style "gm_root"


    frame:
        style_group "gm_nav"
        xalign .98
        yalign .98

        has vbox

        textbutton _("Return") action Return()
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("Save Game") action ShowMenu("save")
        textbutton _("Load Game") action ShowMenu("load")
        textbutton _("Main Menu") action MainMenu()
        textbutton _("Help") action Help()
        textbutton _("Patreon") action OpenURL("http://www.patreon.com/mity")
        textbutton _("Disclaimer") action ShowMenu("disclaimer")
        textbutton _("Quit") action Quit()

init -2:


    style gm_nav_button:
        size_group "gm_nav"












screen file_picker():

    frame:
        style "file_picker_frame"

        has vbox



        hbox:
            style_group "file_picker_nav"

            textbutton _("Previous"):
                action FilePagePrevious()

            textbutton _("Auto"):
                action FilePage("auto")

            textbutton _("Quick"):
                action FilePage("quick")

            for i in range(1, 9):
                textbutton str(i):
                    action FilePage(i)

            textbutton _("Next"):
                action FilePageNext()

        $ columns = 2
        $ rows = 5


        grid columns rows:
            transpose True
            xfill True
            style_group "file_picker"


            for i in range(1, columns * rows + 1):


                button:
                    action FileAction(i)
                    xfill True

                    has hbox


                    add FileScreenshot(i)

                    $ file_name = FileSlotName(i, columns * rows)
                    $ file_time = FileTime(i, empty=_("Empty Slot."))
                    $ save_name = FileSaveName(i)

                    text "[file_name]. [file_time!t]\n[save_name!t]"

                    key "save_delete" action FileDelete(i)


screen save() tag menu:




    use navigation
    use file_picker

screen load() tag menu:




    use navigation
    use file_picker

init -2:
    style file_picker_frame is menu_frame
    style file_picker_nav_button is small_button
    style file_picker_nav_button_text is small_button_text
    style file_picker_button is large_button
    style file_picker_text is large_button_text








screen preferences() tag menu:




    use navigation


    grid 3 1:
        style_group "prefs"
        xfill True


        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Display")
                textbutton _("Window") action Preference("display", "window")
                textbutton _("Fullscreen") action Preference("display", "fullscreen")

            frame:
                style_group "pref"
                has vbox

                label _("Transitions")
                textbutton _("All") action Preference("transitions", "all")
                textbutton _("None") action Preference("transitions", "none")

            frame:
                style_group "pref"
                has vbox

                label _("Text Speed")
                bar value Preference("text speed")

            frame:
                style_group "pref"
                has vbox

                textbutton _("Joystick...") action Preference("joystick")


        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Skip")
                textbutton _("Seen Messages") action Preference("skip", "seen")
                textbutton _("All Messages") action Preference("skip", "all")

            frame:
                style_group "pref"
                has vbox

                textbutton _("Begin Skipping") action Skip()

            frame:
                style_group "pref"
                has vbox

                label _("After Choices")
                textbutton _("Stop Skipping") action Preference("after choices", "stop")
                textbutton _("Keep Skipping") action Preference("after choices", "skip")

            frame:
                style_group "pref"
                has vbox

                label _("Auto-Forward Time")
                bar value Preference("auto-forward time")

                if config.has_voice:
                    textbutton _("Wait for Voice") action Preference("wait for voice", "toggle")

        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Music Volume")
                bar value Preference("music volume")

            frame:
                style_group "pref"
                has vbox

                label _("Sound Volume")
                bar value Preference("sound volume")

                if config.sample_sound:
                    textbutton _("Test"):
                        action Play("sound", config.sample_sound)
                        style "soundtest_button"

            if config.has_voice:
                frame:
                    style_group "pref"
                    has vbox

                    label _("Voice Volume")
                    bar value Preference("voice volume")

                    textbutton _("Voice Sustain") action Preference("voice sustain", "toggle")
                    if config.sample_voice:
                        textbutton _("Test"):
                            action Play("voice", config.sample_voice)
                            style "soundtest_button"

init -2:
    style pref_frame:
        xfill True
        xmargin 5
        top_margin 5

    style pref_vbox:
        xfill True

    style pref_button:
        size_group "pref"
        xalign 1.0

    style pref_slider:
        xmaximum 192
        xalign 1.0

    style soundtest_button:
        xalign 1.0








screen yesno_prompt(message, yes_action, no_action):

    modal True

    window:
        style "gm_root"

    frame:
        style_group "yesno"

        xfill True
        xmargin .05
        ypos .1
        yanchor 0
        ypadding .05

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("Yes") action yes_action
            textbutton _("No") action no_action


    key "game_menu" action no_action

init -2:
    style yesno_button:
        size_group "yesno"

    style yesno_label_text:
        text_align 0.5
        layout "subtitle"







screen quick_menu():


    hbox:
        style_group "quick"

        xalign 1.0
        yalign 1.0

        textbutton _("Back") action Rollback()
        textbutton _("Save") action ShowMenu('save')
        textbutton _("Q.Save") action QuickSave()
        textbutton _("Q.Load") action QuickLoad()
        textbutton _("Skip") action Skip()
        textbutton _("F.Skip") action Skip(fast=True, confirm=True)
        textbutton _("Auto") action Preference("auto-forward", "toggle")
        textbutton _("Prefs") action ShowMenu('preferences')

init -2:
    style quick_button is default:

        background None
        xpadding 5

    style quick_button_text is default:

        size 12
        idle_color "#8888"
        hover_color "#ccc"
        selected_idle_color "#cc08"
        selected_hover_color "#cc0"
        insensitive_color "#4448"





screen water_ex:
    imagemap:
        ground "images/water_ex.png"
        hover "images/water_hover.png"
        idle "images/water_earth.png"



        hotspot (15, 15, 120, 120) clicked Jump("water1")
        if earth_unlocked:
            hotspot (227, 302, 141, 137) clicked Jump("earth1")
        if fire_unlocked:
            hotspot (405, 218, 164, 118) clicked Jump("fire1")
        if air_unlocked:
            hotspot (591, 78, 123, 111) clicked Jump("air1")

init python:
    earth_unlocked = False
    fire_unlocked = False
    air_unlocked = False

screen mount_day:
    imagemap:
        ground "backgrounds/bg_k_mountain_imagemap/bg_k_mountain1.jpg"
        hover "backgrounds/bg_k_mountain_imagemap/bg_k_mountain_flower.png"

        hotspot (200, 200, 600, 600) clicked Jump("flower1")

screen mount_night:
    imagemap:
        ground "backgrounds/bg_k_mountain_imagemap/bg_k_mountain1.jpg"
        hover "backgrounds/bg_k_mountain_imagemap/bg_k_mountain_flower.png"

        hotspot (600, 600, 600, 600) clicked Jump("flower2")


screen oldsnowday:
    add "images/southpole.png"
    add SnowBlossom(Animation("images/snowflake3.png"), count=100, xspeed=(400, 600), yspeed=(500, 900), start=0)
    add SnowBlossom(Animation("images/snowflake3.png"), count=100, xspeed=(400, 600), yspeed=(500, 900), start=0)
    add SnowBlossom(Animation("images/snowflake3.png"), count=100, xspeed=(400, 600), yspeed=(500, 900), start=0)
    add SnowBlossom(Animation("images/snowflake3.png"), count=100, xspeed=(400, 600), yspeed=(500, 900), start=0)
    add SnowBlossom(Animation("images/snowflake3.png", 0.15, "images/snowflake1.png", 0.15), count=100, xspeed=(400, 600), yspeed=(500, 900), start=0)
    imagebutton auto "images/mineday_%s.png" xpos 25 ypos 50 action Jump("mine_day") focus_mask True
    imagebutton auto "images/mountainday_%s.png" xpos 345 ypos 25 action Jump("mountain") focus_mask True
    imagebutton auto "images/trainday_%s.png" xpos 570 ypos 77 action Jump("train_day") focus_mask True
    imagebutton auto "images/homeday_%s.png" xpos 14 ypos 280 action Jump("home_day") focus_mask True
    imagebutton auto "images/schoolday_%s.png" xpos 160 ypos 330 action Jump("school_day") focus_mask True
    imagebutton auto "images/marketday_%s.png" xpos 215 ypos 210 action Jump("market_day") focus_mask True
    imagebutton auto "images/kataraday_%s.png" xpos 570 ypos 280 action Jump("katara_day") focus_mask True
    imagebutton auto "images/huntday_%s.png" xpos 540 ypos 480 action Jump("hunt_day") focus_mask True

screen oldday:
    add "images/southpole.png"
    imagebutton auto "images/mineday_%s.png" xpos 25 ypos 50 action Jump("mine_day") focus_mask True
    imagebutton auto "images/mountainday_%s.png" xpos 345 ypos 25 action Jump("mountain") focus_mask True
    imagebutton auto "images/trainday_%s.png" xpos 570 ypos 77 action Jump("train_day") focus_mask True
    imagebutton auto "images/homeday_%s.png" xpos 14 ypos 280 action Jump("home_day") focus_mask True
    imagebutton auto "images/schoolday_%s.png" xpos 160 ypos 330 action Jump("school_day") focus_mask True
    imagebutton auto "images/marketday_%s.png" xpos 215 ypos 210 action Jump("market_day") focus_mask True
    imagebutton auto "images/kataraday_%s.png" xpos 570 ypos 280 action Jump("katara_day") focus_mask True
    imagebutton auto "images/huntday_%s.png" xpos 540 ypos 480 action Jump("hunt_day") focus_mask True


screen oldnight:
    add "images/southpolenight.png"
    imagebutton auto "images/mountainnight_%s.png" xpos 350 ypos 20 action Jump("mountain") focus_mask True
    imagebutton auto "images/homenight_%s.png" xpos 14 ypos 275 action Jump("home_night") focus_mask True
    imagebutton auto "images/schoolnight_%s.png" xpos 190 ypos 330 action Jump("school_night") focus_mask True
    imagebutton auto "images/marketnight_%s.png" xpos 220 ypos 200 action Jump("market_night") focus_mask True
    imagebutton auto "images/kataranight_%s.png" xpos 540 ypos 272 action Jump("katara_night") focus_mask True

screen dank:
    add "images/southpole.png"
    imagebutton auto "images/homeday_%s.png" xpos 15 ypos 280 action Jump("home_day") focus_mask True




screen aff_screen_day:
    frame:
        has vbox
        text "Affection: [katara_aff] points"
        text "Respect: [krespect] points"
        text "Waterbending: [Waterbending] points"
        text "times walked publicly: [kpubwalk]"
        hbox:
            label "Affection: " xminimum 100
            bar range aff_max value katara_aff xmaximum 400
        hbox:
            label "Respect: " xminimum 100
            bar range krespect_max value krespect xmaximum 400
        hbox:
            label "Waterbending: " xminimum 100
            bar range waterbending_max value Waterbending xmaximum 400
        textbutton "Return" action Jump("home_day_menu")

screen aff_screen_night:
    frame:
        has vbox
        text "Affection: [katara_aff] points"
        text "Respect: [krespect] points"
        text "Waterbending: [Waterbending] points"
        text "times walked publicly: [kpubwalk]"
        hbox:
            label "Affection: " xminimum 100
            bar range aff_max value katara_aff xmaximum 400
        hbox:
            label "Respect: " xminimum 100
            bar range krespect_max value krespect xmaximum 400
        hbox:
            label "Waterbending: " xminimum 100
            bar range waterbending_max value Waterbending xmaximum 400
        textbutton "Return" action Jump("home_night_menu")


screen disclaimer() tag menu:

    frame:
        background "lightblue"
        has vbox
        text "all characters have been aged up to 18 and exist in an alternate reality where events started years into the future."
        textbutton _("Return") action Return()

screen azula_letter:
    add "images/letters/letter0.jpg"
    text "{size=-5}dear [ozai1],\n\nheard [ozai2] things about some [ozai3] [ozai4]\nyou've [ozai5] recently.\nmake sure you don't [ozai6] him away. or else.\n[ozai7] [ozai8] are hard to [ozai9], and you can be\na bit [ozai10] with the personnel.\n\n[ozai11], your father, firelord ozai.\n\np.s. you'll be hearing from one of my agents soon.\ninstill him as one of our heads of operations." xpos 250 ypos 150

init python:

    import time as TimeModule



screen vstats:
    frame:
        xminimum 150
        has vbox
        text "your score: [your_score]"
        text "opponent score: [opp_score]"

screen volly1:
    add "fbackgrounds/bg_a_beach_01.jpg"
    add "emberisland/volleyball_net.png"
    use vstats
    timer 0.5 action Show("centermid1")

screen volly2:
    add "fbackgrounds/bg_a_beach_01.jpg"
    add "emberisland/volleyball_net.png"
    use vstats
    timer 0.5 action Show("rightcenter1")

screen volly3:
    add "fbackgrounds/bg_a_beach_01.jpg"
    add "emberisland/volleyball_net.png"
    use vstats
    timer 0.5 action Show("topleft1")

screen volly4:
    add "fbackgrounds/bg_a_beach_01.jpg"
    add "emberisland/volleyball_net.png"
    use vstats
    timer 0.5 action Show("bottomleft1")

screen volly5:
    add "fbackgrounds/bg_a_beach_01.jpg"
    add "emberisland/volleyball_net.png"
    use vstats
    timer 0.5 action Show("topcenter1")

screen volly6:
    add "fbackgrounds/bg_a_beach_01.jpg"
    add "emberisland/volleyball_net.png"
    use vstats
    timer 0.5 action Show("bottomright1")

screen volly7:
    add "fbackgrounds/bg_a_beach_01.jpg"
    add "emberisland/volleyball_net.png"
    use vstats
    timer 0.5 action Show("bottomcenter1")

screen centermid1:
    add "fbackgrounds/bg_a_beach_01.jpg"
    add "emberisland/volleyball_net.png"
    use vstats
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            idle "emberisland/volleyball1.png"
            hover "emberisland/volleyball1_hover.png"
            action [Hide("centermid1"), SetVariable("your_score", your_score+1), Jump("you_scores")]

    timer 0.2 action [Hide("centermid1"), Show("centermid2")]

screen centermid2:
    add "fbackgrounds/bg_a_beach_01.jpg"
    add "emberisland/volleyball_net.png"
    use vstats
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            idle "emberisland/volleyball2.png"
            hover "emberisland/volleyball2_hover.png"
            action [Hide("centermid2"), SetVariable("your_score", your_score+1), Jump("you_scores")]

    timer 0.14 action [Hide("centermid2"), Show("centermid3")]

screen centermid3:
    add "fbackgrounds/bg_a_beach_01.jpg"
    add "emberisland/volleyball_net.png"
    use vstats
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            idle "emberisland/volleyball3.png"
            hover "emberisland/volleyball3_hover.png"
            action [Hide("centermid3"), SetVariable("your_score", your_score+1), Jump("you_scores")]

    timer 0.12 action [Hide("centermid3"), Show("centermid4")]

screen centermid4:
    add "fbackgrounds/bg_a_beach_01.jpg"
    add "emberisland/volleyball_net.png"
    use vstats
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            idle "emberisland/volleyball4.png"
            hover "emberisland/volleyball4_hover.png"
            action [Hide("centermid4"), SetVariable("your_score", your_score+1), Jump("you_scores")]

    timer 0.1 action [Hide("centermid4"), Show("centermid5")]

screen centermid5:
    add "fbackgrounds/bg_a_beach_01.jpg"
    add "emberisland/volleyball_net.png"
    use vstats
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            idle "emberisland/volleyball5.png"
            hover "emberisland/volleyball5_hover.png"
            action [Hide("centermid5"), SetVariable("your_score", your_score+1), Jump("you_scores")]

    timer 0.08 action [Hide("centermid5"), SetVariable("opp_score", opp_score+1), Jump("opp_scores")]

screen rightcenter1:
    add "fbackgrounds/bg_a_beach_01.jpg"
    add "emberisland/volleyball_net.png"
    use vstats
    vbox xalign 0.9 yalign 0.4:
        imagebutton:
            idle "emberisland/volleyball1.png"
            hover "emberisland/volleyball1_hover.png"
            action [Hide("rightcenter1"), SetVariable("your_score", your_score+1), Jump("you_scores")]

    timer 0.2 action [Hide("rightcenter1"), Show("rightcenter2")]

screen rightcenter2:
    add "fbackgrounds/bg_a_beach_01.jpg"
    add "emberisland/volleyball_net.png"
    use vstats
    vbox xalign 0.9 yalign 0.4:
        imagebutton:
            idle "emberisland/volleyball2.png"
            hover "emberisland/volleyball2_hover.png"
            action [Hide("rightcenter2"), SetVariable("your_score", your_score+1), Jump("you_scores")]

    timer 0.18 action [Hide("rightcenter2"), Show("rightcenter3")]

screen rightcenter3:
    add "fbackgrounds/bg_a_beach_01.jpg"
    add "emberisland/volleyball_net.png"
    use vstats
    vbox xalign 0.9 yalign 0.4:
        imagebutton:
            idle "emberisland/volleyball3.png"
            hover "emberisland/volleyball3_hover.png"
            action [Hide("rightcenter3"), SetVariable("your_score", your_score+1), Jump("you_scores")]

    timer 0.16 action [Hide("rightcenter3"), Show("rightcenter4")]

screen rightcenter4:
    add "fbackgrounds/bg_a_beach_01.jpg"
    add "emberisland/volleyball_net.png"
    use vstats
    vbox xalign 0.9 yalign 0.4:
        imagebutton:
            idle "emberisland/volleyball4.png"
            hover "emberisland/volleyball4_hover.png"
            action [Hide("rightcenter4"), SetVariable("your_score", your_score+1), Jump("you_scores")]

    timer 0.14 action [Hide("rightcenter4"), Show("rightcenter5")]

screen rightcenter5:
    add "fbackgrounds/bg_a_beach_01.jpg"
    add "emberisland/volleyball_net.png"
    use vstats
    vbox xalign 0.9 yalign 0.4:
        imagebutton:
            idle "emberisland/volleyball5.png"
            hover "emberisland/volleyball5_hover.png"
            action [Hide("centermid5"), SetVariable("your_score", your_score+1), Jump("you_scores")]

    timer 0.12 action [Hide("rightcenter5"), SetVariable("opp_score", opp_score+1), Jump("opp_scores")]


screen topleft1:
    add "fbackgrounds/bg_a_beach_01.jpg"
    add "emberisland/volleyball_net.png"
    use vstats
    vbox xalign 0.15 yalign 0.2:
        imagebutton:
            idle "emberisland/volleyball1.png"
            hover "emberisland/volleyball1_hover.png"
            action [Hide("topleft1"), SetVariable("your_score", your_score+1), Jump("you_scores")]

    timer 0.2 action [Hide("topleft1"), Show("topleft2")]

screen topleft2:
    add "fbackgrounds/bg_a_beach_01.jpg"
    add "emberisland/volleyball_net.png"
    use vstats
    vbox xalign 0.15 yalign 0.2:
        imagebutton:
            idle "emberisland/volleyball2.png"
            hover "emberisland/volleyball2_hover.png"
            action [Hide("topleft2"), SetVariable("your_score", your_score+1), Jump("you_scores")]

    timer 0.18 action [Hide("topleft2"), Show("topleft3")]

screen topleft3:
    add "fbackgrounds/bg_a_beach_01.jpg"
    add "emberisland/volleyball_net.png"
    use vstats
    vbox xalign 0.15 yalign 0.2:
        imagebutton:
            idle "emberisland/volleyball3.png"
            hover "emberisland/volleyball3_hover.png"
            action [Hide("topleft3"), SetVariable("your_score", your_score+1), Jump("you_scores")]

    timer 0.16 action [Hide("topleft3"), Show("topleft4")]

screen topleft4:
    add "fbackgrounds/bg_a_beach_01.jpg"
    add "emberisland/volleyball_net.png"
    use vstats
    vbox xalign 0.15 yalign 0.2:
        imagebutton:
            idle "emberisland/volleyball4.png"
            hover "emberisland/volleyball4_hover.png"
            action [Hide("topleft4"), SetVariable("your_score", your_score+1), Jump("you_scores")]

    timer 0.14 action [Hide("topleft4"), Show("topleft5")]

screen topleft5:
    add "fbackgrounds/bg_a_beach_01.jpg"
    add "emberisland/volleyball_net.png"
    use vstats
    vbox xalign 0.15 yalign 0.2:
        imagebutton:
            idle "emberisland/volleyball5.png"
            hover "emberisland/volleyball5_hover.png"
            action [Hide("topleft5"), SetVariable("your_score", your_score+1), Jump("you_scores")]

    timer 0.12 action [Hide("topleft5"), SetVariable("opp_score", opp_score+1), Jump("opp_scores")]


screen bottomleft1:
    add "fbackgrounds/bg_a_beach_01.jpg"
    add "emberisland/volleyball_net.png"
    use vstats
    vbox xalign 0.1 yalign 0.8:
        imagebutton:
            idle "emberisland/volleyball1.png"
            hover "emberisland/volleyball1_hover.png"
            action [Hide("bottomleft1"), SetVariable("your_score", your_score+1), Jump("you_scores")]

    timer 0.16 action [Hide("bottomleft1"), Show("bottomleft2")]

screen bottomleft2:
    add "fbackgrounds/bg_a_beach_01.jpg"
    add "emberisland/volleyball_net.png"
    use vstats
    vbox xalign 0.1 yalign 0.8:
        imagebutton:
            idle "emberisland/volleyball2.png"
            hover "emberisland/volleyball2_hover.png"
            action [Hide("bottomleft2"), SetVariable("your_score", your_score+1), Jump("you_scores")]

    timer 0.14 action [Hide("bottomleft2"), Show("bottomleft3")]

screen bottomleft3:
    add "fbackgrounds/bg_a_beach_01.jpg"
    add "emberisland/volleyball_net.png"
    use vstats
    vbox xalign 0.1 yalign 0.8:
        imagebutton:
            idle "emberisland/volleyball3.png"
            hover "emberisland/volleyball3_hover.png"
            action [Hide("bottomleft3"), SetVariable("your_score", your_score+1), Jump("you_scores")]

    timer 0.12 action [Hide("bottomleft3"), Show("bottomleft4")]

screen bottomleft4:
    add "fbackgrounds/bg_a_beach_01.jpg"
    add "emberisland/volleyball_net.png"
    use vstats
    vbox xalign 0.1 yalign 0.8:
        imagebutton:
            idle "emberisland/volleyball4.png"
            hover "emberisland/volleyball4_hover.png"
            action [Hide("bottomleft4"), SetVariable("your_score", your_score+1), Jump("you_scores")]

    timer 0.1 action [Hide("bottomleft4"), Show("bottomleft5")]

screen bottomleft5:
    add "fbackgrounds/bg_a_beach_01.jpg"
    add "emberisland/volleyball_net.png"
    use vstats
    vbox xalign 0.1 yalign 0.8:
        imagebutton:
            idle "emberisland/volleyball5.png"
            hover "emberisland/volleyball5_hover.png"
            action [Hide("bottomleft5"), SetVariable("your_score", your_score+1), Jump("you_scores")]

    timer 0.08 action [Hide("bottomleft5"), SetVariable("opp_score", opp_score+1), Jump("opp_scores")]


screen topcenter1:
    add "fbackgrounds/bg_a_beach_01.jpg"
    add "emberisland/volleyball_net.png"
    use vstats
    vbox xalign 0.45 yalign 0.1:
        imagebutton:
            idle "emberisland/volleyball1.png"
            hover "emberisland/volleyball1_hover.png"
            action [Hide("topcenter1"), SetVariable("your_score", your_score+1), Jump("you_scores")]

    timer 0.2 action [Hide("topcenter1"), Show("topcenter2")]

screen topcenter2:
    add "fbackgrounds/bg_a_beach_01.jpg"
    add "emberisland/volleyball_net.png"
    use vstats
    vbox xalign 0.45 yalign 0.1:
        imagebutton:
            idle "emberisland/volleyball2.png"
            hover "emberisland/volleyball2_hover.png"
            action [Hide("topcenter2"), SetVariable("your_score", your_score+1), Jump("you_scores")]

    timer 0.18 action [Hide("topcenter2"), Show("topcenter3")]

screen topcenter3:
    add "fbackgrounds/bg_a_beach_01.jpg"
    add "emberisland/volleyball_net.png"
    use vstats
    vbox xalign 0.45 yalign 0.1:
        imagebutton:
            idle "emberisland/volleyball3.png"
            hover "emberisland/volleyball3_hover.png"
            action [Hide("topcenter3"), SetVariable("your_score", your_score+1), Jump("you_scores")]

    timer 0.16 action [Hide("topcenter3"), Show("topcenter4")]

screen topcenter4:
    add "fbackgrounds/bg_a_beach_01.jpg"
    add "emberisland/volleyball_net.png"
    use vstats
    vbox xalign 0.45 yalign 0.1:
        imagebutton:
            idle "emberisland/volleyball4.png"
            hover "emberisland/volleyball4_hover.png"
            action [Hide("topcenter4"), SetVariable("your_score", your_score+1), Jump("you_scores")]

    timer 0.14 action [Hide("topcenter4"), Show("topcenter5")]

screen topcenter5:
    add "fbackgrounds/bg_a_beach_01.jpg"
    add "emberisland/volleyball_net.png"
    use vstats
    vbox xalign 0.45 yalign 0.1:
        imagebutton:
            idle "emberisland/volleyball5.png"
            hover "emberisland/volleyball5_hover.png"
            action [Hide("topcenter5"), SetVariable("your_score", your_score+1), Jump("you_scores")]

    timer 0.12 action [Hide("topcenter5"), SetVariable("opp_score", opp_score+1), Jump("opp_scores")]


screen bottomright1:
    add "fbackgrounds/bg_a_beach_01.jpg"
    add "emberisland/volleyball_net.png"
    use vstats
    vbox xalign 0.8 yalign 0.9:
        imagebutton:
            idle "emberisland/volleyball1.png"
            hover "emberisland/volleyball1_hover.png"
            action [Hide("bottomright1"), SetVariable("your_score", your_score+1), Jump("you_scores")]

    timer 0.2 action [Hide("bottomright1"), Show("bottomright2")]

screen bottomright2:
    add "fbackgrounds/bg_a_beach_01.jpg"
    add "emberisland/volleyball_net.png"
    use vstats
    vbox xalign 0.8 yalign 0.9:
        imagebutton:
            idle "emberisland/volleyball2.png"
            hover "emberisland/volleyball2_hover.png"
            action [Hide("bottomright2"), SetVariable("your_score", your_score+1), Jump("you_scores")]

    timer 0.18 action [Hide("bottomright2"), Show("bottomright3")]

screen bottomright3:
    add "fbackgrounds/bg_a_beach_01.jpg"
    add "emberisland/volleyball_net.png"
    use vstats
    vbox xalign 0.8 yalign 0.9:
        imagebutton:
            idle "emberisland/volleyball3.png"
            hover "emberisland/volleyball3_hover.png"
            action [Hide("bottomright3"), SetVariable("your_score", your_score+1), Jump("you_scores")]

    timer 0.16 action [Hide("bottomright3"), Show("bottomright4")]

screen bottomright4:
    add "fbackgrounds/bg_a_beach_01.jpg"
    add "emberisland/volleyball_net.png"
    use vstats
    vbox xalign 0.8 yalign 0.9:
        imagebutton:
            idle "emberisland/volleyball4.png"
            hover "emberisland/volleyball4_hover.png"
            action [Hide("bottomright4"), SetVariable("your_score", your_score+1), Jump("you_scores")]

    timer 0.14 action [Hide("bottomright4"), Show("bottomright5")]

screen bottomright5:
    add "fbackgrounds/bg_a_beach_01.jpg"
    add "emberisland/volleyball_net.png"
    use vstats
    vbox xalign 0.8 yalign 0.9:
        imagebutton:
            idle "emberisland/volleyball5.png"
            hover "emberisland/volleyball5_hover.png"
            action [Hide("bottomright5"), SetVariable("your_score", your_score+1), Jump("you_scores")]

    timer 0.12 action [Hide("bottomright5"), SetVariable("opp_score", opp_score+1), Jump("opp_scores")]

screen bottomcenter1:
    add "fbackgrounds/bg_a_beach_01.jpg"
    add "emberisland/volleyball_net.png"
    use vstats
    vbox xalign 0.65 yalign 0.8:
        imagebutton:
            idle "emberisland/volleyball1.png"
            hover "emberisland/volleyball1_hover.png"
            action [Hide("bottomcenter1"), SetVariable("your_score", your_score+1), Jump("you_scores")]

    timer 0.2 action [Hide("bottomcenter1"), Show("bottomcenter2")]

screen bottomcenter2:
    add "fbackgrounds/bg_a_beach_01.jpg"
    add "emberisland/volleyball_net.png"
    use vstats
    vbox xalign 0.65 yalign 0.8:
        imagebutton:
            idle "emberisland/volleyball2.png"
            hover "emberisland/volleyball2_hover.png"
            action [Hide("bottomcenter2"), SetVariable("your_score", your_score+1), Jump("you_scores")]

    timer 0.18 action [Hide("bottomcenter2"), Show("bottomcenter3")]

screen bottomcenter3:
    add "fbackgrounds/bg_a_beach_01.jpg"
    add "emberisland/volleyball_net.png"
    use vstats
    vbox xalign 0.65 yalign 0.8:
        imagebutton:
            idle "emberisland/volleyball3.png"
            hover "emberisland/volleyball3_hover.png"
            action [Hide("bottomcenter3"), SetVariable("your_score", your_score+1), Jump("you_scores")]

    timer 0.16 action [Hide("bottomcenter3"), Show("bottomcenter4")]

screen bottomcenter4:
    add "fbackgrounds/bg_a_beach_01.jpg"
    add "emberisland/volleyball_net.png"
    use vstats
    vbox xalign 0.65 yalign 0.8:
        imagebutton:
            idle "emberisland/volleyball4.png"
            hover "emberisland/volleyball4_hover.png"
            action [Hide("bottomcenter4"), SetVariable("your_score", your_score+1), Jump("you_scores")]

    timer 0.14 action [Hide("bottomcenter4"), Show("bottomcenter5")]

screen bottomcenter5:
    add "fbackgrounds/bg_a_beach_01.jpg"
    add "emberisland/volleyball_net.png"
    use vstats
    vbox xalign 0.65 yalign 0.8:
        imagebutton:
            idle "emberisland/volleyball5.png"
            hover "emberisland/volleyball5_hover.png"
            action [Hide("bottomcenter5"), SetVariable("your_score", your_score+1), Jump("you_scores")]

    timer 0.12 action [Hide("bottomcenter5"), SetVariable("opp_score", opp_score+1), Jump("opp_scores")]


screen ember_island_shop:
    imagemap:
        ground "fbackgrounds/bg_a_armory.jpg"
        hover "emberisland/ember_shop_hover.jpg"

        if not ember_shopspot1:
            hotspot (63, 170, 118, 189) clicked Jump("ember_shop1")
        if not ember_shopspot2:
            hotspot (136, 322, 83, 211) clicked Jump("ember_shop2")
        if not ember_shopspot3:
            hotspot (326, 114, 350, 225) clicked Jump("ember_shop3")
        if not ember_shopspot4:
            hotspot (616, 412, 186, 100) clicked Jump("ember_shop4")

screen pin_mustache:
    imagemap:
        ground "fbackgrounds/bg_a_island_avatarposter.jpg"
        hover "fbackgrounds/bg_a_island_avatarposter.jpg"

        hotspot (0, 0, 1000, 720) clicked Jump("mustache_pin")

screen pin_knife:
    imagemap:
        ground "devil_aang"
        hover "devil_aang"

        hotspot (0, 0, 1000, 720) clicked Jump("knife_pin")

screen pin_knife1:
    add "emberisland/devilmarks.png"
    imagemap:
        ground "devil_aang1"
        hover "devil_aang1"

        hotspot (0, 0, 1000, 720) clicked Jump("knife_pin1")

screen pin_knife2:
    add "emberisland/devilmarks.png"
    imagemap:
        ground "devil_aang2"
        hover "devil_aang2"

        hotspot (0, 0, 1000, 720) clicked Jump("knife_pin2")


screen bluffstats:
    frame:
        xminimum 150
        has vbox
        text "bluffs remaining: [remaining_bluffs]"
        text "your wins: [player_shady_wins]"
        text "shady's wins: [shady_wins]"


screen crabstats:
    frame:
        xminimum 150
        has vbox
        if not crab_standin:
            text "your health: [crab_player_health]"
        if crab_standin:
            if crab_standin_normal:
                text "ally \"normal\" crab health: [crab_standin_health]"
            if crab_standin_strong:
                text "ally \"strong\" crab health: [crab_standin_health]"
            if crab_standin_legend:
                text "ally \"legendary\" crab health: [crab_standin_health]"
            if crab_standin_bessie:
                text "ally \"bessie\" crab health: [crab_standin_health]"
            if crab_standin_musky:
                text "ally \"ol' musky\" crab health: [crab_standin_health]"
            if crab_standin_stank:
                text "ally \"the stank\" crab health: [crab_standin_health]"
        text "crab health: [crab_health]"
        text "pocket crabs: [crabs_caught]"
        text "your level: [crabs_killed]"

screen tourney_crabstats:
    frame:
        xminimum 150
        has vbox
        if not crab_standin:
            text "your health: [crab_player_health]"
        if crab_standin:
            if crab_standin_normal:
                text "ally \"normal\" crab health: [crab_standin_health]"
            if crab_standin_strong:
                text "ally \"strong\" crab health: [crab_standin_health]"
            if crab_standin_legend:
                text "ally \"legendary\" crab health: [crab_standin_health]"
            if crab_standin_bessie:
                text "ally \"bessie\" crab health: [crab_standin_health]"
            if crab_standin_musky:
                text "ally \"ol' musky\" crab health: [crab_standin_health]"
            if crab_standin_stank:
                text "ally \"the stank\" crab health: [crab_standin_health]"

        text "crab health: [crab_health]"
        text "pocket crabs: [crabs_caught]"
        if crab_tournament_invite:
            text "enemy crabs remaining: [remaining_enemy_crabs]"
        text "your level: [crabs_killed]"

screen battle_stats:
    frame:
        xminimum 150
        has vbox
        text "Health: [health]"

screen fps_battle:
    add "bg_a_armory.jpg"
    use battle_stats

    timer 1.0 action Show("near_slow_level1")
    timer 3 action Show("far_slow_level1")
    timer 4.5 action Show("mid_slow_level1")
    timer 5.5 action Show("mid_right_slow_level1")
    timer 8.0 action Show("mid_left_slow_level1")
    timer 10.0 action Show("near_slow_level1")
    timer 11.7 action Show("far_slow_level1")
    timer 12.0 action Show("near_slow_level1")
    timer 13.5 action Show("far_slow_level1")
    timer 14.9 action Show("mid_right_slow_level1")
    timer 16.9 action Show("far_slow_level1")
    timer 17.0 action Show("mid_left_slow_level1")
    timer 17.5 action Show("mid_slow_level1")

    timer 21.0 action Return()


screen near_slow_level1:


    use battle_stats
    vbox xalign 0.5 yalign 1.0:
        imagebutton:
            idle "enemy.png"
            hover "enemy_hit.png"
            action [Hide("near_slow_level1"), SetVariable("shopfight", shopfight+1), Jump("fps_shop_battle")]
    timer 1.5 action [SetVariable("health", health-15), If(health <= 0, true=Return())]
    timer 3.0 action [SetVariable("health", health-15), If(health <= 0, true=Return())]
    timer 5.0 action [SetVariable("health", health-15), If(health <= 0, true=Return())]
    timer 7.0 action [SetVariable("health", health-15), If(health <= 0, true=Return())]
    timer 9.0 action [SetVariable("health", health-15), If(health <= 0, true=Return())]
    timer 11.0 action [SetVariable("health", health-15), If(health <= 0, true=Return())]
    timer 13.0 action [SetVariable("health", health-15), If(health <= 0, true=Return())]
    timer 15.0 action [SetVariable("health", health-15), If(health <= 0, true=Return())]
    timer 17.0 action [SetVariable("health", health-15), If(health <= 0, true=Return())]
    timer 19.0 action [SetVariable("health", health-15), If(health <= 0, true=Return())]


screen far_slow_level1:


    use battle_stats
    vbox xalign 0.5 yalign 0.25:
        imagebutton:
            idle "enemy.png"
            hover "enemy_hit.png"
            action [Hide("far_slow_level1"), SetVariable("shopfight", shopfight+1), Jump("fps_shop_battle")]
    timer 1.5 action [SetVariable("health", health-15), If(health <= 0, true=Return())]
    timer 3.0 action [SetVariable("health", health-15), If(health <= 0, true=Return())]
    timer 5.0 action [SetVariable("health", health-15), If(health <= 0, true=Return())]
    timer 7.0 action [SetVariable("health", health-15), If(health <= 0, true=Return())]
    timer 9.0 action [SetVariable("health", health-15), If(health <= 0, true=Return())]
    timer 11.0 action [SetVariable("health", health-15), If(health <= 0, true=Return())]
    timer 13.0 action [SetVariable("health", health-15), If(health <= 0, true=Return())]
    timer 15.0 action [SetVariable("health", health-15), If(health <= 0, true=Return())]
    timer 17.0 action [SetVariable("health", health-15), If(health <= 0, true=Return())]
    timer 19.0 action [SetVariable("health", health-15), If(health <= 0, true=Return())]


screen mid_slow_level1:


    use battle_stats
    vbox xalign 0.6 yalign 0.5:
        imagebutton:
            idle "enemy.png"
            hover "enemy_hit.png"
            action [Hide("mid_slow_level1"), SetVariable("shopfight", shopfight+1), Jump("fps_shop_battle")]
    timer 1.5 action [SetVariable("health", health-15), If(health <= 0, true=Return())]
    timer 3.0 action [SetVariable("health", health-15), If(health <= 0, true=Return())]
    timer 5.0 action [SetVariable("health", health-15), If(health <= 0, true=Return())]
    timer 7.0 action [SetVariable("health", health-15), If(health <= 0, true=Return())]
    timer 9.0 action [SetVariable("health", health-15), If(health <= 0, true=Return())]
    timer 11.0 action [SetVariable("health", health-15), If(health <= 0, true=Return())]
    timer 13.0 action [SetVariable("health", health-15), If(health <= 0, true=Return())]
    timer 15.0 action [SetVariable("health", health-15), If(health <= 0, true=Return())]
    timer 17.0 action [SetVariable("health", health-15), If(health <= 0, true=Return())]
    timer 19.0 action [SetVariable("health", health-15), If(health <= 0, true=Return())]

screen mid_right_slow_level1:


    use battle_stats
    vbox xalign 0.8 yalign 0.7:
        imagebutton:
            idle "enemy.png"
            hover "enemy_hit.png"
            action [Hide("mid_right_slow_level1"), SetVariable("shopfight", shopfight+1), Jump("fps_shop_battle")]
    timer 1.5 action [SetVariable("health", health-15), If(health <= 0, true=Return())]
    timer 3.0 action [SetVariable("health", health-15), If(health <= 0, true=Return())]
    timer 5.0 action [SetVariable("health", health-15), If(health <= 0, true=Return())]
    timer 7.0 action [SetVariable("health", health-15), If(health <= 0, true=Return())]
    timer 9.0 action [SetVariable("health", health-15), If(health <= 0, true=Return())]
    timer 11.0 action [SetVariable("health", health-15), If(health <= 0, true=Return())]
    timer 13.0 action [SetVariable("health", health-15), If(health <= 0, true=Return())]
    timer 15.0 action [SetVariable("health", health-15), If(health <= 0, true=Return())]
    timer 17.0 action [SetVariable("health", health-15), If(health <= 0, true=Return())]
    timer 19.0 action [SetVariable("health", health-15), If(health <= 0, true=Return())]

screen mid_left_slow_level1:


    use battle_stats
    vbox xalign 0.1 yalign 0.4:
        imagebutton:
            idle "enemy.png"
            hover "enemy_hit.png"
            action [Hide("mid_left_slow_level1"), SetVariable("shopfight", shopfight+1), Jump("fps_shop_battle")]
    timer 1.5 action [SetVariable("health", health-15), If(health <= 0, true=Return())]
    timer 3.0 action [SetVariable("health", health-15), If(health <= 0, true=Return())]
    timer 5.0 action [SetVariable("health", health-15), If(health <= 0, true=Return())]
    timer 7.0 action [SetVariable("health", health-15), If(health <= 0, true=Return())]
    timer 9.0 action [SetVariable("health", health-15), If(health <= 0, true=Return())]
    timer 11.0 action [SetVariable("health", health-15), If(health <= 0, true=Return())]
    timer 13.0 action [SetVariable("health", health-15), If(health <= 0, true=Return())]
    timer 15.0 action [SetVariable("health", health-15), If(health <= 0, true=Return())]
    timer 17.0 action [SetVariable("health", health-15), If(health <= 0, true=Return())]
    timer 19.0 action [SetVariable("health", health-15), If(health <= 0, true=Return())]


screen right_and_left1:


    use battle_stats

    if one and two:
        vbox xalign 0.8 yalign 0.7:
            imagebutton:
                idle "enemy.png"
                hover "enemy_hit.png"
                action [SetVariable("shopfight", shopfight+1), SetVariable("one", False)]

        vbox xalign 0.1 yalign 0.4:
            imagebutton:
                idle "enemy.png"
                hover "enemy_hit.png"
                action [SetVariable("shopfight", shopfight+1), SetVariable("two", False)]

        timer 1.5 action [SetVariable("health", health-30), If(health <= 0, true=Return())]
        timer 3.0 action [SetVariable("health", health-30), If(health <= 0, true=Return())]
        timer 5.0 action [SetVariable("health", health-30), If(health <= 0, true=Return())]
        timer 7.0 action [SetVariable("health", health-30), If(health <= 0, true=Return())]
        timer 9.0 action [SetVariable("health", health-30), If(health <= 0, true=Return())]
        timer 11.0 action [SetVariable("health", health-30), If(health <= 0, true=Return())]
        timer 13.0 action [SetVariable("health", health-30), If(health <= 0, true=Return())]
        timer 15.0 action [SetVariable("health", health-30), If(health <= 0, true=Return())]
        timer 17.0 action [SetVariable("health", health-30), If(health <= 0, true=Return())]
        timer 19.0 action [SetVariable("health", health-30), If(health <= 0, true=Return())]

    if not one and two:
        vbox xalign 0.1 yalign 0.4:
            imagebutton:
                idle "enemy.png"
                hover "enemy_hit.png"
                action [Hide("right_and_left1"), SetVariable("shopfight", shopfight+1), SetVariable("two", False), Jump("fps_shop_battle")]

        timer 1.5 action [SetVariable("health", health-15), If(health <= 0, true=Return())]
        timer 3.0 action [SetVariable("health", health-15), If(health <= 0, true=Return())]
        timer 5.0 action [SetVariable("health", health-15), If(health <= 0, true=Return())]
        timer 7.0 action [SetVariable("health", health-15), If(health <= 0, true=Return())]
        timer 9.0 action [SetVariable("health", health-15), If(health <= 0, true=Return())]
        timer 11.0 action [SetVariable("health", health-15), If(health <= 0, true=Return())]
        timer 13.0 action [SetVariable("health", health-15), If(health <= 0, true=Return())]
        timer 15.0 action [SetVariable("health", health-15), If(health <= 0, true=Return())]
        timer 17.0 action [SetVariable("health", health-15), If(health <= 0, true=Return())]
        timer 19.0 action [SetVariable("health", health-15), If(health <= 0, true=Return())]


    if one and not two:
        vbox xalign 0.8 yalign 0.7:
            imagebutton:
                idle "enemy.png"
                hover "enemy_hit.png"
                action [Hide("right_and_left1"), SetVariable("shopfight", shopfight+1), SetVariable("one", False), Jump("fps_shop_battle")]

        timer 1.5 action [SetVariable("health", health-15), If(health <= 0, true=Return())]
        timer 3.0 action [SetVariable("health", health-15), If(health <= 0, true=Return())]
        timer 5.0 action [SetVariable("health", health-15), If(health <= 0, true=Return())]
        timer 7.0 action [SetVariable("health", health-15), If(health <= 0, true=Return())]
        timer 9.0 action [SetVariable("health", health-15), If(health <= 0, true=Return())]
        timer 11.0 action [SetVariable("health", health-15), If(health <= 0, true=Return())]
        timer 13.0 action [SetVariable("health", health-15), If(health <= 0, true=Return())]
        timer 15.0 action [SetVariable("health", health-15), If(health <= 0, true=Return())]
        timer 17.0 action [SetVariable("health", health-15), If(health <= 0, true=Return())]
        timer 19.0 action [SetVariable("health", health-15), If(health <= 0, true=Return())]

screen puzzlebox:
    vbox xalign 0.9 yalign 0.9:
        textbutton _("back") action Jump("puzzlefail")

screen puzzle_letter:
    add "images/letters/letter0.jpg"
    text "{size=-5}as i age, i fear forgetfulness.\n\nso, here i have kept my greatest treasure... and ozai will never\nknow!\nshe was a mongrel when she came to this family. i chose her\nbecause she is a descendant of roku and will fulfill the\nprophecy.\nwhen ozai breeds with her, she will bring great power to our\nfamily.\n\nbut she knows she is a mongrel bitch, and knows i have the \npower to treat her as i choose.\n\ni could have her killed and i doubt ozai would even care.\n\nnow, i am too old to perform perhaps.... but not too old to watch.\ni have here two exquisite examples that i made her sit for\nto get her picture taken.\n\nif i ever forget, may these two pictures remind me of that busty, \nfilthy slut.... ursa. \n\nphotos attached.\n\nazulon." xpos 250 ypos 150


screen basingse_map:

    imagemap:

        ground "ebackgrounds/basingse_city_1.jpg"
        hover "ebackgrounds/basingse_imagemap/basingse_icons.png"
        idle "ebackgrounds/basingse_imagemap/basingse_locations.png"

        hotspot (31, 45, 278, 223) clicked Jump("bk3_jasmine")
        hotspot (754, 33, 217, 220) clicked Jump("bk3_palace")
        hotspot (411, 37, 214, 213) clicked Jump("bk3_fountain")
        hotspot (772, 318, 213, 217) clicked Jump("bk3_market")
        hotspot (99, 472, 167, 166) clicked Jump("bk3_home")
        hotspot (403, 331, 216, 211) clicked Jump("bk3_arena")






    add "emberisland_cloud1"

    if we_poor:
        add "calender_and_money.png"
        hbox:
            xalign 0.6
            yalign 0.02
            text "[emoney]"
        hbox:
            xalign 0.45
            yalign 0.02
            text "[ecalendar]"

    if bk3_village_access:
        imagebutton idle "bk3/icons/bk3_village_off.png" hover "bk3/icons/bk3_village_on.png" xpos 0.25 ypos 0 action Jump("bk3_village")




    if bk3_stats:
        imagebutton idle "stats_button.png" hover "stats_button_dark.png" xpos 0.7 ypos 0 action [ Jump("stat_screen_earth_day")]

    if bk3_day and laogai_travel:
        imagebutton idle "bk3/icons/bk3_maze_off.png" hover "bk3/icons/bk3_maze_on.png" xpos 0.18 ypos 0 action Jump("bk3_maze_start1")


screen basingse_night_map:

    imagemap:

        ground "ebackgrounds/basingse_city_1.jpg"
        hover "ebackgrounds/basingse_imagemap/basingse_icons.png"
        idle "ebackgrounds/basingse_imagemap/basingse_locations.png"

        hotspot (31, 45, 278, 223) clicked Jump("bk3_jasmine_night")
        hotspot (754, 33, 217, 220) clicked Jump("bk3_palace_night")
        hotspot (411, 37, 214, 213) clicked Jump("bk3_fountain_night")
        hotspot (772, 318, 213, 217) clicked Jump("bk3_market_night")
        hotspot (99, 472, 167, 166) clicked Jump("bk3_home_night")
        hotspot (403, 331, 216, 211) clicked Jump("bk3_arena_night")





    add "backgrounds/background_fade_purpleish.png"

    if we_poor:
        add "calender_and_money.png"
        hbox:
            xalign 0.6
            yalign 0.02
            text "[emoney]"
        hbox:
            xalign 0.45
            yalign 0.02
            text "[ecalendar]"

    if bk3_village_access and suki_tylee !=4:
        imagebutton idle "bk3/icons/bk3_village_off.png" hover "bk3/icons/bk3_village_on.png" xpos 0.25 ypos 0 action Jump("bk3_village_night")




    if bk3_stats:
        imagebutton idle "stats_button.png" hover "stats_button_dark.png" xpos 0.7 ypos 0 action [ Jump("stat_screen_earth_day")]


screen earth_journal:
    add "misc/bk3_scroll.jpg"
    hbox:
        xalign 0.2
        yalign 0.1
        text "{b}Previous Entry...."

    hbox:
        xalign 0.47
        yalign 0.17
        text "\"we’re on our way to ba sing se! we’ll tell the earth king \nabout the eclipse, and then… hopefully i find appa. \ni’m coming, buddy. - aang\""


    hbox:
        xalign 0.17
        yalign 0.28
        text "{b}Entry 1"
    hbox:
        xalign 0.5
        yalign 0.41
        text "\"well, i’ve arrived in basingse, and it’s… surprisingly calm. \nthe city seems peaceful and orderly on the surface, \nbut I have a sneaking suspicion that not all is as it seems. \nI need to meet with the king and tell him about the upcoming \neclipse, and how it’ll leave the firebenders powerless. \nApparently it’s important.\""


    if quest2:
        hbox:
            xalign 0.17
            yalign 0.58
            text "{b}Entry 2"

        hbox:
            xalign 0.52
            yalign 0.8
            text "\"well, i got kicked out of the damn city. that 'peace and order' \ni mentioned before seems to be a facade for some kind of \ntyranny. looks like this “long feng” guy (who’s a total choad) \nis actually running the city, and doesn’t want me \nupsetting it. Well, I’m not very good at following orders, \nbut for now I’m going to look for Katara. \nAlso, I wanna dick that Toph girl.\""

screen earth_journal2:



    add "misc/bk3_scroll.jpg"
    hbox:
        xalign 0.17
        yalign 0.1
        text "{b}Entry 3"

    hbox:
        xalign 0.47
        yalign 0.2
        text "\"Found Katara at Iroh’s tea shop, the Jasmine Dragon. \nIroh has me thinking about turning this \"become a \npowerful bender to save the spirit world\" thing to my \nadvantage. I’ve got to think about it for a while. \nKatara hinted that she knows what’s going on, but… I don’t \nknow how that’s possible. Maybe I can get \nmore information out of her next time I see her. \nOn the plus side, she seems to be as deviant as I left her. \nI should find Toph.\""


    if quest4:
        hbox:
            xalign 0.17
            yalign 0.46
            text "{b}Entry 4"
        hbox:
            xalign 0.35
            yalign 0.58
            text "\"Toph has me running scams in the market for money \nso that I can build a house in the village. Apparently, \nI can buy the 5 wood and 5 steel that I need at \nthe shop in the market. I’ll meet toph in the village \nonce i get them.\""


    if quest5:
        hbox:
            xalign 0.17
            yalign 0.68
            text "{b}Entry 5"

        hbox:
            xalign 0.52
            yalign 0.85



























screen earth_clicker:
    modal True
    timer .5 repeat True action [If(tug_points <= -420, true=SetVariable("tug_points", tug_points), false=SetVariable("tug_points", tug_points - tug_plus))]
    button:
        background "bk3_fight/earth_attack1.png"
        xpos 358
        ypos -tug_points
        xysize (275, 275)
        action [SetVariable("clicked", True), If(tug_points >= tug_max_point, true=Jump("earth_clicer_win"), false=SetVariable("tug_points", tug_points + tug_plus))]
    if tug_points >=1:
        add "bk3_fight/earth_attack1.png" xpos 358 ypos -tug_points
    if tug_points ==0:
        add "bk3_fight/earth_attack1.png" xpos 358 ypos tug_points


screen housefire_1:
    if lovehousefire ==2:

        vbox xalign 0.7 yalign 0.4:
            imagebutton:
                idle "tocs_fire2"
                hover "tocs_fire2"
                action Jump ("housefirescores")
    if lovehousefire ==3:
        add "ebackgrounds/lake_laogai_2.jpg"
        vbox xalign 0.7 yalign 0.4:
            imagebutton:
                idle "misc/waterwhirl.png"
                hover "misc/waterwhirl.png"
                action Jump ("housefirescores")

screen housefire_2:
    if lovehousefire ==2:

        vbox xalign 0.4 yalign 0.9:
            imagebutton:
                idle "tocs_fire2"
                hover "tocs_fire2"
                action Jump ("housefirescores")
    if lovehousefire ==3:
        add "ebackgrounds/lake_laogai_2.jpg"
        vbox xalign 0.4 yalign 0.9:
            imagebutton:
                idle "misc/waterwhirl.png"
                hover "misc/waterwhirl.png"
                action Jump ("housefirescores")

screen housefire_3:
    if lovehousefire ==2:

        vbox xalign 0.1 yalign 0.1:
            imagebutton:
                idle "tocs_fire2"
                hover "tocs_fire2"
                action Jump ("housefirescores")
    if lovehousefire ==3:
        add "ebackgrounds/lake_laogai_2.jpg"
        vbox xalign 0.1 yalign 0.1:
            imagebutton:
                idle "misc/waterwhirl.png"
                hover "misc/waterwhirl.png"
                action Jump ("housefirescores")

screen housefire_4:
    if lovehousefire ==2:

        vbox xalign 0.9 yalign 0.9:
            imagebutton:
                idle "tocs_fire2"
                hover "tocs_fire2"
                action Jump ("housefirescores")
    if lovehousefire ==3:
        add "ebackgrounds/lake_laogai_2.jpg"
        vbox xalign 0.9 yalign 0.9:
            imagebutton:
                idle "misc/waterwhirl.png"
                hover "misc/waterwhirl.png"
                action Jump ("housefirescores")

screen housefire_5:
    if lovehousefire ==2:

        vbox xalign 0.8 yalign 0.3:
            imagebutton:
                idle "tocs_fire2"
                hover "tocs_fire2"
                action Jump ("housefirescores")
    if lovehousefire ==3:
        add "ebackgrounds/lake_laogai_2.jpg"
        vbox xalign 0.8 yalign 0.3:
            imagebutton:
                idle "misc/waterwhirl.png"
                hover "misc/waterwhirl.png"
                action Jump ("housefirescores")

screen basingse_home_clue_screen2:

    imagemap:
        ground "ebackgrounds/basingse_home_2.jpg"
        hover "ebackgrounds/basingse_home_2_hover.jpg"

        hotspot (80, 80, 180, 180) clicked Jump("bk3_home_curtain_clue")
        hotspot (115, 450, 218, 180) clicked Jump("bk3_home_cushion_clue1")
        hotspot (319, 500, 200, 180) clicked Jump("bk3_home_cushion_clue2")
        hotspot (450, 100, 460, 200) clicked Jump("bk3_home_rug_clue")

screen dl_countdown:
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('dl_countdown'), Jump(dl_timer_jump)])
    bar value time range dl_timer_range xalign 0.5 yalign 0.9 xmaximum 300 at alpha_dissolve

screen fuzzy_edges:
    add "misc/fuzzy_edge.png"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
