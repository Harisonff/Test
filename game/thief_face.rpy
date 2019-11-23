image thief_face = LiveComposite(
    (1000, 720),
    (0, 0), "black",
    (0, 0), "player/base_neutral.png",
    (0, 0), ConditionSwitch(
        "tnose == 'small'", "player/nose_small.png",
        "tnose == 'medium'", "player/nose_mediocre.png",
        "tnose == 'big'", "player/nose_big.png",),
    (0, 0), ConditionSwitch(
        "textra2 == 'eyepatch'", "player/xtra_eyepatch.png",
        "textra2 == 'glasses'", "player/xtra_glasses.png",
        "textra2 == 'none'", "transparent.png"),
    (0, 0), ConditionSwitch(
        "textra3 == 'scar'", "player/xtra_scar.png",
        "textra3 == 'none'", "transparent.png",
        ),
    (0, 0), ConditionSwitch(
        "tchin == 'none'", "transparent.png",
        "tchin == 'beard'", "player/xtra_beard.png",
        "tchin == 'round'", "player/xtra_chinround.png",
        "tchin == 'square'", "player/xtra_chinsquare.png",
        ),
    (0, 0), ConditionSwitch(
        "thair == 'blonde1'", "player/hair_straightblond.png",
        "thair == 'bald'", "player/hair_bald.png",
        "thair == 'brown1'", "player/hair_darkwild.png",
        "thair == 'blonde2'", "player/hair_blondcurly.png",
        "thair == 'brown2'", "player/hair_darkcurly.png",
        "thair == 'brown3'", "player/hair_darkponytail.png",
        ),
    )

image thief_face1 = LiveComposite(
    (1000, 720),
    (0, 0), "player/base_neutral.png",
    (0, 0), ConditionSwitch(
        "tnose == 'small'", "player/nose_small.png",
        "tnose == 'medium'", "player/nose_mediocre.png",
        "tnose == 'big'", "player/nose_big.png",),
    (0, 0), ConditionSwitch(
        "textra2 == 'eyepatch'", "player/xtra_eyepatch.png",
        "textra2 == 'glasses'", "player/xtra_glasses.png",
        "textra2 == 'none'", "transparent.png"),
    (0, 0), ConditionSwitch(
        "textra3 == 'scar'", "player/xtra_scar.png",
        "textra3 == 'none'", "transparent.png",
        ),
    (0, 0), ConditionSwitch(
        "tchin == 'none'", "transparent.png",
        "tchin == 'beard'", "player/xtra_beard.png",
        "tchin == 'round'", "player/xtra_chinround.png",
        "tchin == 'square'", "player/xtra_chinsquare.png",
        ),
    (0, 0), ConditionSwitch(
        "thair == 'blonde1'", "player/hair_straightblond.png",
        "thair == 'bald'", "player/hair_bald.png",
        "thair == 'brown1'", "player/hair_darkwild.png",
        "thair == 'blonde2'", "player/hair_blondcurly.png",
        "thair == 'brown2'", "player/hair_darkcurly.png",
        "thair == 'brown3'", "player/hair_darkponytail.png",
        ),
    )


image thief_face_angry = LiveComposite(
    (1000, 720),
    (0, 0), "black",
    (0, 0), "player/base_angry.png",
    (0, 0), ConditionSwitch(
        "tnose == 'small'", "player/nose_small.png",
        "tnose == 'medium'", "player/nose_mediocre.png",
        "tnose == 'big'", "player/nose_big.png",),
    (0, 0), ConditionSwitch(
        "textra1 == 'beard'", "player/xtra_beard.png",
        "textra1 == 'none'", "transparent.png",),
    (0, 0), ConditionSwitch(
        "textra2 == 'eyepatch'", "player/xtra_eyepatch.png",
        "textra2 == 'none'", "transparent.png"),
    (0, 0), ConditionSwitch(
        "textra3 == 'scar'", "player/xtra_scar.png",
        "textra3 == 'none'", "transparent.png"
        ),
    (0, 0), ConditionSwitch(
        "thair == 'blonde'", "player/hair_straightblond.png",
        "thair == 'bald'", "player/hair_bald.png",
        "thair == 'brown'", "player/hair_darkwild.png",
        ),
    )

image thief_face_confused = LiveComposite(
    (1000, 720),
    (0, 0), "black",
    (0, 0), "player/base_confused.png",
    (0, 0), ConditionSwitch(
        "tnose == 'small'", "player/nose_small.png",
        "tnose == 'medium'", "player/nose_mediocre.png",
        "tnose == 'big'", "player/nose_big.png",),
    (0, 0), ConditionSwitch(
        "textra1 == 'beard'", "player/xtra_beard.png",
        "textra1 == 'none'", "transparent.png",),
    (0, 0), ConditionSwitch(
        "textra2 == 'eyepatch'", "player/xtra_eyepatch.png",
        "textra2 == 'none'", "transparent.png"),
    (0, 0), ConditionSwitch(
        "textra3 == 'scar'", "player/xtra_scar.png",
        "textra3 == 'none'", "transparent.png"
        ),
    (0, 0), ConditionSwitch(
        "thair == 'blonde'", "player/hair_straightblond.png",
        "thair == 'bald'", "player/hair_bald.png",
        "thair == 'brown'", "player/hair_darkwild.png",
        ),
    )

image thief_face_grin = LiveComposite(
    (1000, 720),
    (0, 0), "black",
    (0, 0), "player/base_grin.png",
    (0, 0), ConditionSwitch(
        "tnose == 'small'", "player/nose_small.png",
        "tnose == 'medium'", "player/nose_mediocre.png",
        "tnose == 'big'", "player/nose_big.png",),
    (0, 0), ConditionSwitch(
        "textra1 == 'beard'", "player/xtra_beard.png",
        "textra1 == 'none'", "transparent.png",),
    (0, 0), ConditionSwitch(
        "textra2 == 'eyepatch'", "player/xtra_eyepatch.png",
        "textra2 == 'none'", "transparent.png"),
    (0, 0), ConditionSwitch(
        "textra3 == 'scar'", "player/xtra_scar.png",
        "textra3 == 'none'", "transparent.png"
        ),
    (0, 0), ConditionSwitch(
        "thair == 'blonde'", "player/hair_straightblond.png",
        "thair == 'bald'", "player/hair_bald.png",
        "thair == 'brown'", "player/hair_darkwild.png",
        ),
    )


label face_build:
    show thief_face with dissolve
    jump face_build1

label face_build1:
    menu:
        "hair":
            jump face_build_hair

            label face_build_hair:
                menu:
                    "brown 1":
                        $ thair = "brown1"
                        jump face_build_hair
                    "brown 2":

                        $ thair = "brown2"
                        jump face_build_hair
                    "brown 3":

                        $ thair = "brown3"
                        jump face_build_hair
                    "bald":

                        $ thair = "bald"
                        jump face_build_hair
                    "blonde 1":

                        $ thair = "blonde1"
                        jump face_build_hair
                    "blonde 2":

                        $ thair = "blonde2"
                        jump face_build_hair
                    "back":

                        jump face_build1
        "nose":

            jump face_build_nose

            label face_build_nose:
                menu:
                    "small":
                        $ tnose = "small"
                        jump face_build_nose
                    "medium":

                        $ tnose = "medium"
                        jump face_build_nose
                    "big":

                        $ tnose = "big"
                        jump face_build_nose
                    "back":

                        jump face_build1
        "chin":

            jump face_build_chin

            label face_build_chin:
                menu:
                    "standard":
                        $ tchin = "none"
                        jump face_build_chin
                    "standard with beard":

                        $ tchin = "beard"
                        jump face_build_chin
                    "round":

                        $ tchin = "round"
                        jump face_build_chin
                    "square":

                        $ tchin = "square"
                        jump face_build_chin
                    "back":

                        jump face_build1
        "extras":
            jump face_build_extras

            label face_build_extras:
                menu:
                    "scar":

                        $ textra3 = "scar"
                        jump face_build_extras
                    "eyepatch":

                        $ textra2 = "eyepatch"
                        jump face_build_extras
                    "glasses":

                        $ textra2 = "glasses"
                        jump face_build_extras
                    "none":

                        $ textra2 = "none"
                        $ textra3 = "none"
                        jump face_build_extras
                    "back":

                        jump face_build1
        "finished":

            hide thief_face with dissolve
            jump prison_after_face
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
