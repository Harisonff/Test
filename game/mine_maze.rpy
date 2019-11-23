label mine_maze:
    menu:
        y "which way should i go?"
        "left":

            "you take a left and press on. You feel like you're moving in a large circle."
            scene black with dissolve
            "you find your way back to the first cavern."
            y "great."
            y "let's try this again."
            jump mine_maze
        "right":

            "you take a right and press on."
            scene dimgray with dissolve
            "it gets a little lighter."
            jump mine_maze1

label mine_maze1:
    y "huh. a second fork."

    menu:
        y "which way should i go now?"
        "left":

            "you take a left and press on. You feel like you're moving in a large circle."
            scene black with dissolve
            "you find your way back to the first cavern."
            y "great."
            y "let's try this again."
            jump mine_maze
        "right":

            "you take a right and press on."
            scene grey with dissolve
            "it gets a little lighter."
            jump mine_maze2

label mine_maze2:
    y "a third fork?! Are you kidding me?"
    menu:
        y "okay, fine. which way now?"
        "left":

            "you take a left and press on."
            scene darkgray with dissolve
            "it gets a little lighter."
            jump mine_maze3
        "right":

            "you take a right and press on. You feel like you're moving in a large circle."
            scene black with dissolve
            "you find your way back to the first cavern."
            y "great."
            y "let's try this again."
            jump mine_maze

label mine_maze3:
    y "..."
    menu:
        "left":

            scene bg_k_mine_treasureroom with dissolve
            "you take a left and find your way to an old mine entrance."
            "you see sunlight on the other side, and a big gap you can slip through."
            y "someone's obviously been coming and going through here."
            "you take a quick look around and find a box with a diary in it."
            so "Dear diary: it's only women here, and i still can't get laid!"
            so "what the hell?!"
            so "Those three from the elder council have been looking at me in a funny way, though..."
            so "one of them keeps winking at me and that's not cool man....not cool at all."
            so "i'm gonna have to go find some pussy."
            so "my balls are as blue as this damn ocean."
            y "huh. that poor guy."
            "you look in the box..."
            play sound "audio/win2.mp3"
            show sokka_dirtymagazine_00 with dissolve
            show ctcblink
            $ renpy.pause()
            hide ctcblink
            "you found a sticky magazine!"
            play sound "audio/win2.mp3"
            "and a super rare white stone!"
            $ items.append("sticky magazine")
            $ items.append("the rarest prize of all - friendship! just kidding, you got a super rare white stone")
            $ sokka_treasure +=1
            y "nice."
            "you leave and decide that going down strange mining tunnels may not be worth it."
            hide sokka_dirtymagazine_00
            hide bg_k_mine_treasureroom
            $ stones +=1
            jump tribe2
        "right":

            "you take a right and press on. You feel like you're moving in a large circle."
            scene black with dissolve
            "you find your way back to the first cavern."
            y "aargh!"
            y "this is such bullshit!"
            jump mine_maze
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
