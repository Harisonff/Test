


init python:
    class Card:
        def __init__(self, cardnr, cname, owned, card_bg):
            self.cardnr = cardnr
            self.cname = cname
            self.owned = owned 
            self.card_bg = card_bg

screen go_fish_score:
    vbox:
        text "your score: [gfp_score]":
            xalign .2 yalign .2
        text "opp score: [gfo_score]"
        text "deck: [gf_deck_remaining]"

label go_fish_begin:
    hide screen earth_money_date



    jump card_init


label card_init:
    $ match_sets_checked = False
    $ gf_deck_remaining = 52
    $ gf_player_turn = True
    $ go_fishing = False
    $ opp_go_fishing = False
    $ gf_player_turn = True
    $ gf_card_finder = False
    $ gf_opp_card_finder = False

    $ gfp_score = 0
    $ gfo_score = 0

    $ p1 = "none"
    $ p2 = "none"
    $ p3 = "none"
    $ p4 = "none"
    $ p5 = "none"
    $ p6 = "none"
    $ p7 = "none"
    $ p8 = "none"
    $ p9 = "none"

    $ o1 = "none"
    $ o2 = "none"
    $ o3 = "none"
    $ o4 = "none"
    $ o5 = "none"
    $ o6 = "none"
    $ o7 = "none"
    $ o8 = "none"
    $ o9 = "none"

    $ card1  = Card(1,"2", 0,"d/2c.png")
    $ card2  = Card(2,"2", 0,"d/2d.png")
    $ card3  = Card(3,"2", 0,"d/2h.png")
    $ card4  = Card(4,"2", 0,"d/2s.png")
    $ card5  = Card(5,"3", 0,"d/3c.png")
    $ card6  = Card(6,"3", 0,"d/3d.png")
    $ card7  = Card(7,"3", 0,"d/3h.png")
    $ card8  = Card(8,"3", 0,"d/3s.png")
    $ card9  = Card(9,"4", 0,"d/4c.png")
    $ card10  = Card(10,"4", 0,"d/4d.png")
    $ card11  = Card(11,"4", 0,"d/4h.png")
    $ card12  = Card(12,"4", 0,"d/4s.png")
    $ card13  = Card(13,"5", 0,"d/5c.png")
    $ card14  = Card(14,"5", 0,"d/5d.png")
    $ card15  = Card(15,"5", 0,"d/5h.png")
    $ card16  = Card(16,"5", 0,"d/5s.png")
    $ card17  = Card(17,"6", 0,"d/6c.png")
    $ card18  = Card(18,"6", 0,"d/6d.png")
    $ card19  = Card(19,"6", 0,"d/6h.png")
    $ card20  = Card(20,"6", 0,"d/6s.png")
    $ card21  = Card(21,"7", 0,"d/7c.png")
    $ card22  = Card(22,"7", 0,"d/7d.png")
    $ card23  = Card(23,"7", 0,"d/7h.png")
    $ card24  = Card(24,"7", 0,"d/7s.png")
    $ card25  = Card(25,"8", 0,"d/8c.png")
    $ card26  = Card(26,"8", 0,"d/8d.png")
    $ card27  = Card(27,"8", 0,"d/8h.png")
    $ card28  = Card(28,"8", 0,"d/8s.png")
    $ card29  = Card(29,"9", 0,"d/9c.png")
    $ card30  = Card(30,"9", 0,"d/9d.png")
    $ card31  = Card(31,"9", 0,"d/9h.png")
    $ card32  = Card(32,"9", 0,"d/9s.png")
    $ card33  = Card(33,"10", 0,"d/10c.png")
    $ card34  = Card(34,"10", 0,"d/10d.png")
    $ card35  = Card(35,"10", 0,"d/10h.png")
    $ card36  = Card(36,"10", 0,"d/10s.png")
    $ card37  = Card(37,"jack", 0,"d/jc.png")
    $ card38  = Card(38,"jack", 0,"d/jd.png")
    $ card39  = Card(39,"jack", 0,"d/jh.png")
    $ card40  = Card(40,"jack", 0,"d/js.png")
    $ card41  = Card(41,"queen", 0,"d/qc.png")
    $ card42  = Card(42,"queen", 0,"d/qd.png")
    $ card43  = Card(43,"queen", 0,"d/qh.png")
    $ card44  = Card(44,"queen", 0,"d/qs.png")
    $ card45  = Card(45,"king", 0,"d/kc.png")
    $ card46  = Card(46,"king", 0,"d/kd.png")
    $ card47  = Card(47,"king", 0,"d/kh.png")
    $ card48  = Card(48,"king", 0,"d/ks.png")
    $ card49  = Card(49,"ace", 0,"d/ac.png")
    $ card50  = Card(50,"ace", 0,"d/ad.png")
    $ card51  = Card(51,"ace", 0,"d/ah.png")
    $ card52  = Card(52,"ace", 0,"d/as.png")


    $ cardlist = [card1,card2,card3,card4,card5,card6,card7,card8,card9,card10,card11,card12,card13,card14,card15,card16,card17,card18,card19,card20,
        card21,card22,card23,card24,card25,card26,card27,card28,card29,card30,card31,card32,card33,card34,card35,card36,card37,card38,card39,card40,card41,
        card42,card43,card44,card45,card46,card47,card48,card49,card50,card51,card52]

    if gf_count ==0:
        k3_n "do you need instructions?"
        menu:
            "how to play":
                jump go_fish_instructions

                label go_fish_instructions:
                    "each player starts with 7 cards."
                    "the goal is to collect \"pairs\" -- a pair is two cards of the same number."
                    "if you have a matching pair, those cards are removed from your hand, and you score a point."
                    "on your turn, you choose one of your own cards to ask from your opponent."
                    "if they have the card, both cards are removed, you score a point, and get to ask again."
                    "if they don't have the card, they say \"go fish\" and you draw a card."
                    "if you run out of cards in your hand, you draw another from the deck."
                    "when there are no cards left in the deck, the player with the highest score wins."
                    menu:
                        "instructions again":
                            jump go_fish_instructions
                        "i got it":

                            pass
            "no, i'm good":

                y "i'm set."
                k3_n "cool."

    jump first_deal


label first_deal:

    $ renpy.random.shuffle(cardlist)
    if p1 == "none":
        $ gf_deck_remaining -=1
        $ player_card1 = cardlist.pop()
        $ p1 = player_card1
        $ player_card1.owned = 1
        $ pcard1_xpos = 6
        $ pcard1_ypos = 400
    if p2 == "none":
        $ gf_deck_remaining -=1
        $ player_card2 = cardlist.pop()
        $ p2 = player_card2
        $ player_card2.owned = 1
        $ pcard2_xpos = 106
        $ pcard2_ypos = 400
    if p3 == "none":
        $ gf_deck_remaining -=1
        $ player_card3 = cardlist.pop()
        $ p3 = player_card3
        $ player_card3.owned = 1
        $ pcard3_xpos = 206
        $ pcard3_ypos = 400
    if p4 == "none":
        $ gf_deck_remaining -=1
        $ player_card4 = cardlist.pop()
        $ p4 = player_card4
        $ player_card4.owned = 1
        $ pcard4_xpos = 306
        $ pcard4_ypos = 400
    if p5 == "none":
        $ gf_deck_remaining -=1
        $ player_card5 = cardlist.pop()
        $ p5 = player_card5
        $ player_card5.owned = 1
        $ pcard5_xpos = 406
        $ pcard5_ypos = 400
    if p6 == "none":
        $ gf_deck_remaining -=1
        $ player_card6 = cardlist.pop()
        $ p6 = player_card6
        $ player_card6.owned = 1
        $ pcard6_xpos = 506
        $ pcard6_ypos = 400
    if p7 == "none":
        $ gf_deck_remaining -=1
        $ player_card7 = cardlist.pop()
        $ p7 = player_card7
        $ player_card7.owned = 1
        $ pcard7_xpos = 606
        $ pcard7_ypos = 400
















    if o1 == "none":
        $ gf_deck_remaining -=1
        $ opp_card1 = cardlist.pop()
        $ o1 = opp_card1
        $ opp_card1.owned = 2
        $ ocard1_xpos = 900
        $ ocard1_ypos = 10
    if o2 == "none":
        $ gf_deck_remaining -=1
        $ opp_card2 = cardlist.pop()
        $ o2 = opp_card2
        $ opp_card2.owned = 2
        $ ocard2_xpos = 800
        $ ocard2_ypos = 10
    if o3 == "none":
        $ gf_deck_remaining -=1
        $ opp_card3 = cardlist.pop()
        $ o3 = opp_card3
        $ opp_card3.owned = 2
        $ ocard3_xpos = 700
        $ ocard3_ypos = 10
    if o4 == "none":
        $ gf_deck_remaining -=1
        $ opp_card4 = cardlist.pop()
        $ o4 = opp_card4
        $ opp_card4.owned = 2
        $ ocard4_xpos = 600
        $ ocard4_ypos = 10
    if o5 == "none":
        $ gf_deck_remaining -=1
        $ opp_card5 = cardlist.pop()
        $ o5 = opp_card5
        $ opp_card5.owned = 2
        $ ocard5_xpos = 500
        $ ocard5_ypos = 10
    if o6 == "none":
        $ gf_deck_remaining -=1
        $ opp_card6 = cardlist.pop()
        $ o6 = opp_card6
        $ opp_card6.owned = 2
        $ ocard6_xpos = 400
        $ ocard6_ypos = 10
    if o7 == "none":
        $ gf_deck_remaining -=1
        $ opp_card7 = cardlist.pop()
        $ o7 = opp_card7
        $ opp_card7.owned = 2
        $ ocard7_xpos = 300
        $ ocard7_ypos = 10
















    if go_fish_talk:
        k3_h "oh, this looks good."

    jump card_background



label card_background:
    show screen go_fish_score








    if p1 != "none":
        show expression p1.card_bg:
            xpos pcard1_xpos ypos pcard1_ypos
    if p2 != "none":
        show expression p2.card_bg:
            xpos pcard2_xpos ypos pcard2_ypos
    if p3 != "none":
        show expression p3.card_bg:
            xpos pcard3_xpos ypos pcard3_ypos
    if p4 != "none":
        show expression p4.card_bg:
            xpos pcard4_xpos ypos pcard4_ypos
    if p5 != "none":
        show expression p5.card_bg:
            xpos pcard5_xpos ypos pcard5_ypos
    if p6 != "none":
        show expression p6.card_bg:
            xpos pcard6_xpos ypos pcard6_ypos
    if p7 != "none":
        show expression p7.card_bg:
            xpos pcard7_xpos ypos pcard7_ypos
    if p8 != "none":
        show expression p8.card_bg:
            xpos pcard8_xpos ypos pcard8_ypos
    if p9 != "none":
        show expression p9.card_bg:
            xpos pcard9_xpos ypos pcard9_ypos

    if p1 == "none":
        hide expression p1.card_bg
    if p2 == "none":
        hide expression p2.card_bg
    if p3 == "none":
        hide expression p3.card_bg
    if p4 == "none":
        hide expression p4.card_bg
    if p5 == "none":
        hide expression p5.card_bg
    if p6 == "none":
        hide expression p6.card_bg
    if p7 == "none":
        hide expression p7.card_bg
    if p8 == "none":
        hide expression p8.card_bg
    if p9 == "none":
        hide expression p9.card_bg

    if o1 != "none":
        show expression "d/blank1.png":
            xpos ocard1_xpos ypos ocard1_ypos
    if o2 != "none":
        show expression "d/blank2.png":
            xpos ocard2_xpos ypos ocard2_ypos
    if o3 != "none":
        show expression "d/blank3.png":
            xpos ocard3_xpos ypos ocard3_ypos
    if o4 != "none":
        show expression "d/blank4.png":
            xpos ocard4_xpos ypos ocard4_ypos
    if o5 != "none":
        show expression "d/blank5.png":
            xpos ocard5_xpos ypos ocard5_ypos
    if o6 != "none":
        show expression "d/blank6.png":
            xpos ocard6_xpos ypos ocard6_ypos
    if o7 != "none":
        show expression "d/blank7.png":
            xpos ocard7_xpos ypos ocard7_ypos
    if o8 != "none":
        show expression "d/blank8.png":
            xpos ocard8_xpos ypos ocard8_ypos
    if o9 != "none":
        show expression "d/blank9.png":
            xpos ocard9_xpos ypos ocard9_ypos

    if o1 == "none":
        hide expression "d/blank1.png"
    if o2 == "none":
        hide expression "d/blank2.png"
    if o3 == "none":
        hide expression "d/blank3.png"
    if o4 == "none":
        hide expression "d/blank4.png"
    if o5 == "none":
        hide expression "d/blank5.png"
    if o6 == "none":
        hide expression "d/blank6.png"
    if o7 == "none":
        hide expression "d/blank7.png"
    if o8 == "none":
        hide expression "d/blank8.png"
    if o9 == "none":
        hide expression "d/blank9.png"

    jump match_sets

screen card_selecter:

    imagemap:
        ground "d/trans_ground.png"
        hover "d/blue_hover.png"

        if p1 != "none":
            hotspot (pcard1_xpos, pcard1_ypos, 93, 133) action Return(1)
        if p2 != "none":
            hotspot (pcard2_xpos, pcard2_ypos, 93, 133) action Return(2)
        if p3 != "none":
            hotspot (pcard3_xpos, pcard3_ypos, 93, 133) action Return(3)
        if p4 != "none":
            hotspot (pcard4_xpos, pcard4_ypos, 93, 133) action Return(4)
        if p5 != "none":
            hotspot (pcard5_xpos, pcard5_ypos, 93, 133) action Return(5)
        if p6 != "none":
            hotspot (pcard6_xpos, pcard2_ypos, 93, 133) action Return(6)
        if p7 != "none":
            hotspot (pcard7_xpos, pcard3_ypos, 93, 133) action Return(7)
        if p8 != "none":
            hotspot (pcard8_xpos, pcard4_ypos, 93, 133) action Return(8)
        if p9 != "none":
            hotspot (pcard9_xpos, pcard5_ypos, 93, 133) action Return(9)


label match_sets:

    if opp_go_fishing:
        $ gfo_score -=1
        $ opp_go_fishing = False

        jump gf_opp_fish
    if go_fishing:
        $ gfp_score -=1
        $ go_fishing = False
        $ rand_grumble = 0
        $ rand_grumble = renpy.random.randint(1,2)
        if rand_grumble ==1:
            y "mumble grumble..."
        jump gf_player_fish

    if p1 != "none" and p2 != "none" and p1.cname == p2.cname:
        "you have two matching cards!"
        play sound "audio/win2.mp3"
        $ p1.owned = 3
        $ p1 = "none"
        $ p2.owned = 3
        $ p2 = "none"
        $ gfp_score +=1
    if p1 != "none" and p3 != "none" and p1.cname == p3.cname:
        "you have two matching cards!"
        play sound "audio/win2.mp3"
        $ p1.owned = 3
        $ p1 = "none"
        $ p3.owned = 3
        $ p3 = "none"
        $ gfp_score +=1
    if p1 != "none" and p4 != "none" and p1.cname == p4.cname:
        "you have two matching cards!"
        play sound "audio/win2.mp3"
        $ p1.owned = 3
        $ p1 = "none"
        $ p4.owned = 3
        $ p4 = "none"
        $ gfp_score +=1
    if p1 != "none" and p5 != "none" and p1.cname == p5.cname:
        "you have two matching cards!"
        play sound "audio/win2.mp3"
        $ p1.owned = 3
        $ p1 = "none"
        $ p5.owned = 3
        $ p5 = "none"
        $ gfp_score +=1
    if p1 != "none" and p6 != "none" and p1.cname == p6.cname:
        "you have two matching cards!"
        play sound "audio/win2.mp3"
        $ p1.owned = 3
        $ p1 = "none"
        $ p6.owned = 3
        $ p6 = "none"
        $ gfp_score +=1
    if p1 != "none" and p7 != "none" and p1.cname == p7.cname:
        "you have two matching cards!"
        play sound "audio/win2.mp3"
        $ p1.owned = 3
        $ p1 = "none"
        $ p7.owned = 3
        $ p7 = "none"
        $ gfp_score +=1
    if p1 != "none" and p8 != "none" and p1.cname == p8.cname:
        "you have two matching cards!"
        play sound "audio/win2.mp3"
        $ p1.owned = 3
        $ p1 = "none"
        $ p8.owned = 3
        $ p8 = "none"
        $ gfp_score +=1
    if p1 != "none" and p9 != "none" and p1.cname == p9.cname:
        "you have two matching cards!"
        play sound "audio/win2.mp3"
        $ p1.owned = 3
        $ p1 = "none"
        $ p9.owned = 3
        $ p9 = "none"
        $ gfp_score +=1
    if p2 != "none" and p3 != "none" and p2.cname == p3.cname:
        "you have two matching cards!"
        play sound "audio/win2.mp3"
        $ p2.owned = 3
        $ p2 = "none"
        $ p3.owned = 3
        $ p3 = "none"
        $ gfp_score +=1
    if p2 != "none" and p4 != "none" and p2.cname == p4.cname:
        "you have two matching cards!"
        play sound "audio/win2.mp3"
        $ p2.owned = 3
        $ p2 = "none"
        $ p4.owned = 3
        $ p4 = "none"
        $ gfp_score +=1
    if p2 != "none" and p5 != "none" and p2.cname == p5.cname:
        "you have two matching cards!"
        play sound "audio/win2.mp3"
        $ p2.owned = 3
        $ p2 = "none"
        $ p5.owned = 3
        $ p5 = "none"
        $ gfp_score +=1
    if p2 != "none" and p6 != "none" and p2.cname == p6.cname:
        "you have two matching cards!"
        play sound "audio/win2.mp3"
        $ p2.owned = 3
        $ p2 = "none"
        $ p6.owned = 3
        $ p6 = "none"
        $ gfp_score +=1
    if p2 != "none" and p7 != "none" and p2.cname == p7.cname:
        "you have two matching cards!"
        play sound "audio/win2.mp3"
        $ p2.owned = 3
        $ p2 = "none"
        $ p7.owned = 3
        $ p7 = "none"
        $ gfp_score +=1
    if p2 != "none" and p8 != "none" and p2.cname == p8.cname:
        "you have two matching cards!"
        play sound "audio/win2.mp3"
        $ p2.owned = 3
        $ p2 = "none"
        $ p8.owned = 3
        $ p8 = "none"
        $ gfp_score +=1
    if p2 != "none" and p9 != "none" and p2.cname == p9.cname:
        "you have two matching cards!"
        play sound "audio/win2.mp3"
        $ p2.owned = 3
        $ p2 = "none"
        $ p9.owned = 3
        $ p9 = "none"
        $ gfp_score +=1
    if p3 != "none" and p4 != "none" and p3.cname == p4.cname:
        "you have two matching cards!"
        play sound "audio/win2.mp3"
        $ p3.owned = 3
        $ p3 = "none"
        $ p4.owned = 3
        $ p4 = "none"
        $ gfp_score +=1
    if p3 != "none" and p5 != "none" and p3.cname == p5.cname:
        "you have two matching cards!"
        play sound "audio/win2.mp3"
        $ p3.owned = 3
        $ p3 = "none"
        $ p5.owned = 3
        $ p5 = "none"
        $ gfp_score +=1
    if p3 != "none" and p6 != "none" and p3.cname == p6.cname:
        "you have two matching cards!"
        play sound "audio/win2.mp3"
        $ p3.owned = 3
        $ p3 = "none"
        $ p6.owned = 3
        $ p6 = "none"
        $ gfp_score +=1
    if p3 != "none" and p7 != "none" and p3.cname == p7.cname:
        "you have two matching cards!"
        play sound "audio/win2.mp3"
        $ p3.owned = 3
        $ p3 = "none"
        $ p7.owned = 3
        $ p7 = "none"
        $ gfp_score +=1
    if p3 != "none" and p8 != "none" and p3.cname == p8.cname:
        "you have two matching cards!"
        play sound "audio/win2.mp3"
        $ p3.owned = 3
        $ p3 = "none"
        $ p8.owned = 3
        $ p8 = "none"
        $ gfp_score +=1
    if p3 != "none" and p9 != "none" and p3.cname == p9.cname:
        "you have two matching cards!"
        play sound "audio/win2.mp3"
        $ p3.owned = 3
        $ p3 = "none"
        $ p9.owned = 3
        $ p9 = "none"
        $ gfp_score +=1
    if p4 != "none" and p5 != "none" and p4.cname == p5.cname:
        "you have two matching cards!"
        play sound "audio/win2.mp3"
        $ p4.owned = 3
        $ p4 = "none"
        $ p5.owned = 3
        $ p5 = "none"
        $ gfp_score +=1
    if p4 != "none" and p6 != "none" and p4.cname == p6.cname:
        "you have two matching cards!"
        play sound "audio/win2.mp3"
        $ p4.owned = 3
        $ p4 = "none"
        $ p6.owned = 3
        $ p6 = "none"
        $ gfp_score +=1
    if p4 != "none" and p7 != "none" and p4.cname == p7.cname:
        "you have two matching cards!"
        play sound "audio/win2.mp3"
        $ p4.owned = 3
        $ p4 = "none"
        $ p7.owned = 3
        $ p7 = "none"
        $ gfp_score +=1
    if p4 != "none" and p8 != "none" and p4.cname == p8.cname:
        "you have two matching cards!"
        play sound "audio/win2.mp3"
        $ p4.owned = 3
        $ p4 = "none"
        $ p8.owned = 3
        $ p8 = "none"
        $ gfp_score +=1
    if p4 != "none" and p9 != "none" and p4.cname == p9.cname:
        "you have two matching cards!"
        play sound "audio/win2.mp3"
        $ p4.owned = 3
        $ p4 = "none"
        $ p9.owned = 3
        $ p9 = "none"
        $ gfp_score +=1
    if p5 != "none" and p6 != "none" and p5.cname == p6.cname:
        "you have two matching cards!"
        play sound "audio/win2.mp3"
        $ p5.owned = 3
        $ p5 = "none"
        $ p6.owned = 3
        $ p6 = "none"
        $ gfp_score +=1
    if p5 != "none" and p7 != "none" and p5.cname == p7.cname:
        "you have two matching cards!"
        play sound "audio/win2.mp3"
        $ p5.owned = 3
        $ p5 = "none"
        $ p7.owned = 3
        $ p7 = "none"
        $ gfp_score +=1
    if p5 != "none" and p8 != "none" and p5.cname == p8.cname:
        "you have two matching cards!"
        play sound "audio/win2.mp3"
        $ p5.owned = 3
        $ p5 = "none"
        $ p8.owned = 3
        $ p8 = "none"
        $ gfp_score +=1
    if p5 != "none" and p9 != "none" and p5.cname == p9.cname:
        "you have two matching cards!"
        play sound "audio/win2.mp3"
        $ p5.owned = 3
        $ p5 = "none"
        $ p9.owned = 3
        $ p9 = "none"
        $ gfp_score +=1
    if p6 != "none" and p7 != "none" and p6.cname == p7.cname:
        "you have two matching cards!"
        play sound "audio/win2.mp3"
        $ p6.owned = 3
        $ p6 = "none"
        $ p7.owned = 3
        $ p7 = "none"
        $ gfp_score +=1
    if p6 != "none" and p8 != "none" and p6.cname == p8.cname:
        "you have two matching cards!"
        play sound "audio/win2.mp3"
        $ p6.owned = 3
        $ p6 = "none"
        $ p8.owned = 3
        $ p8 = "none"
        $ gfp_score +=1
    if p6 != "none" and p9 != "none" and p6.cname == p9.cname:
        "you have two matching cards!"
        play sound "audio/win2.mp3"
        $ p6.owned = 3
        $ p6 = "none"
        $ p9.owned = 3
        $ p9 = "none"
        $ gfp_score +=1
    if p7 != "none" and p8 != "none" and p7.cname == p8.cname:
        "you have two matching cards!"
        play sound "audio/win2.mp3"
        $ p7.owned = 3
        $ p7 = "none"
        $ p8.owned = 3
        $ p8 = "none"
        $ gfp_score +=1
    if p7 != "none" and p9 != "none" and p7.cname == p9.cname:
        "you have two matching cards!"
        play sound "audio/win2.mp3"
        $ p7.owned = 3
        $ p7 = "none"
        $ p9.owned = 3
        $ p9 = "none"
        $ gfp_score +=1
    if p8 != "none" and p9 != "none" and p8.cname == p9.cname:
        "you have two matching cards!"
        play sound "audio/win2.mp3"
        $ p8.owned = 3
        $ p8 = "none"
        $ p9.owned = 3
        $ p9 = "none"
        $ gfp_score +=1



    if o1 != "none" and o2 != "none" and o1.cname == o2.cname:
        "your opponent has two matching cards!"
        $ o1.owned = 3
        $ o1 = "none"
        $ o2.owned = 3
        $ o2 = "none"
        $ gfo_score +=1
    if o1 != "none" and o3 != "none" and o1.cname == o3.cname:
        "your opponent has two matching cards!"
        $ o1.owned = 3
        $ o1 = "none"
        $ o3.owned = 3
        $ o3 = "none"
        $ gfo_score +=1
    if o1 != "none" and o4 != "none" and o1.cname == o4.cname:
        "your opponent has two matching cards!"
        $ o1.owned = 3
        $ o1 = "none"
        $ o4.owned = 3
        $ o4 = "none"
        $ gfo_score +=1
    if o1 != "none" and o5 != "none" and o1.cname == o5.cname:
        "your opponent has two matching cards!"
        $ o1.owned = 3
        $ o1 = "none"
        $ o5.owned = 3
        $ o5 = "none"
        $ gfo_score +=1
    if o1 != "none" and o6 != "none" and o1.cname == o6.cname:
        "your opponent has two matching cards!"
        $ o1.owned = 3
        $ o1 = "none"
        $ o6.owned = 3
        $ o6 = "none"
        $ gfo_score +=1
    if o1 != "none" and o7 != "none" and o1.cname == o7.cname:
        "your opponent has two matching cards!"
        $ o1.owned = 3
        $ o1 = "none"
        $ o7.owned = 3
        $ o7 = "none"
        $ gfo_score +=1
    if o1 != "none" and o8 != "none" and o1.cname == o8.cname:
        "your opponent has two matching cards!"
        $ o1.owned = 3
        $ o1 = "none"
        $ o8.owned = 3
        $ o8 = "none"
        $ gfo_score +=1
    if o1 != "none" and o9 != "none" and o1.cname == o9.cname:
        "your opponent has two matching cards!"
        $ o1.owned = 3
        $ o1 = "none"
        $ o9.owned = 3
        $ o9 = "none"
        $ gfo_score +=1
    if o2 != "none" and o3 != "none" and o2.cname == o3.cname:
        "your opponent has two matching cards!"
        $ o2.owned = 3
        $ o2 = "none"
        $ o3.owned = 3
        $ o3 = "none"
        $ gfo_score +=1
    if o2 != "none" and o4 != "none" and o2.cname == o4.cname:
        "your opponent has two matching cards!"
        $ o2.owned = 3
        $ o2 = "none"
        $ o4.owned = 3
        $ o4 = "none"
        $ gfo_score +=1
    if o2 != "none" and o5 != "none" and o2.cname == o5.cname:
        "your opponent has two matching cards!"
        $ o2.owned = 3
        $ o2 = "none"
        $ o5.owned = 3
        $ o5 = "none"
        $ gfo_score +=1
    if o2 != "none" and o6 != "none" and o2.cname == o6.cname:
        "your opponent has two matching cards!"
        $ o2.owned = 3
        $ o2 = "none"
        $ o6.owned = 3
        $ o6 = "none"
        $ gfo_score +=1
    if o2 != "none" and o7 != "none" and o2.cname == o7.cname:
        "your opponent has two matching cards!"
        $ o2.owned = 3
        $ o2 = "none"
        $ o7.owned = 3
        $ o7 = "none"
        $ gfo_score +=1
    if o2 != "none" and o8 != "none" and o2.cname == o8.cname:
        "your opponent has two matching cards!"
        $ o2.owned = 3
        $ o2 = "none"
        $ o8.owned = 3
        $ o8 = "none"
        $ gfo_score +=1
    if o2 != "none" and o9 != "none" and o2.cname == o9.cname:
        "your opponent has two matching cards!"
        $ o2.owned = 3
        $ o2 = "none"
        $ o9.owned = 3
        $ o9 = "none"
        $ gfo_score +=1
    if o3 != "none" and o4 != "none" and o3.cname == o4.cname:
        "your opponent has two matching cards!"
        $ o3.owned = 3
        $ o3 = "none"
        $ o4.owned = 3
        $ o4 = "none"
        $ gfo_score +=1
    if o3 != "none" and o5 != "none" and o3.cname == o5.cname:
        "your opponent has two matching cards!"
        $ o3.owned = 3
        $ o3 = "none"
        $ o5.owned = 3
        $ o5 = "none"
        $ gfo_score +=1
    if o3 != "none" and o6 != "none" and o3.cname == o6.cname:
        "your opponent has two matching cards!"
        $ o3.owned = 3
        $ o3 = "none"
        $ o6.owned = 3
        $ o6 = "none"
        $ gfo_score +=1
    if o3 != "none" and o7 != "none" and o3.cname == o7.cname:
        "your opponent has two matching cards!"
        $ o3.owned = 3
        $ o3 = "none"
        $ o7.owned = 3
        $ o7 = "none"
        $ gfo_score +=1
    if o3 != "none" and o8 != "none" and o3.cname == o8.cname:
        "your opponent has two matching cards!"
        $ o3.owned = 3
        $ o3 = "none"
        $ o8.owned = 3
        $ o8 = "none"
        $ gfo_score +=1
    if o3 != "none" and o9 != "none" and o3.cname == o9.cname:
        "your opponent has two matching cards!"
        $ o3.owned = 3
        $ o3 = "none"
        $ o9.owned = 3
        $ o9 = "none"
        $ gfo_score +=1
    if o4 != "none" and o5 != "none" and o4.cname == o5.cname:
        "your opponent has two matching cards!"
        $ o4.owned = 3
        $ o4 = "none"
        $ o5.owned = 3
        $ o5 = "none"
        $ gfo_score +=1
    if o4 != "none" and o6 != "none" and o4.cname == o6.cname:
        "your opponent has two matching cards!"
        $ o4.owned = 3
        $ o4 = "none"
        $ o6.owned = 3
        $ o6 = "none"
        $ gfo_score +=1
    if o4 != "none" and o7 != "none" and o4.cname == o7.cname:
        "your opponent has two matching cards!"
        $ o4.owned = 3
        $ o4 = "none"
        $ o7.owned = 3
        $ o7 = "none"
        $ gfo_score +=1
    if o4 != "none" and o8 != "none" and o4.cname == o8.cname:
        "your opponent has two matching cards!"
        $ o4.owned = 3
        $ o4 = "none"
        $ o8.owned = 3
        $ o8 = "none"
        $ gfo_score +=1
    if o4 != "none" and o9 != "none" and o4.cname == o9.cname:
        "your opponent has two matching cards!"
        $ o4.owned = 3
        $ o4 = "none"
        $ o9.owned = 3
        $ o9 = "none"
        $ gfo_score +=1
    if o5 != "none" and o6 != "none" and o5.cname == o6.cname:
        "your opponent has two matching cards!"
        $ o5.owned = 3
        $ o5 = "none"
        $ o6.owned = 3
        $ o6 = "none"
        $ gfo_score +=1
    if o5 != "none" and o7 != "none" and o5.cname == o7.cname:
        "your opponent has two matching cards!"
        $ o5.owned = 3
        $ o5 = "none"
        $ o7.owned = 3
        $ o7 = "none"
        $ gfo_score +=1
    if o5 != "none" and o8 != "none" and o5.cname == o8.cname:
        "your opponent has two matching cards!"
        $ o5.owned = 3
        $ o5 = "none"
        $ o8.owned = 3
        $ o8 = "none"
        $ gfo_score +=1
    if o5 != "none" and o9 != "none" and o5.cname == o9.cname:
        "your opponent has two matching cards!"
        $ o5.owned = 3
        $ o5 = "none"
        $ o9.owned = 3
        $ o9 = "none"
        $ gfo_score +=1
    if o6 != "none" and o7 != "none" and o6.cname == o7.cname:
        "your opponent has two matching cards!"
        $ o6.owned = 3
        $ o6 = "none"
        $ o7.owned = 3
        $ o7 = "none"
        $ gfo_score +=1
    if o6 != "none" and o8 != "none" and o6.cname == o8.cname:
        "your opponent has two matching cards!"
        $ o6.owned = 3
        $ o6 = "none"
        $ o8.owned = 3
        $ o8 = "none"
        $ gfo_score +=1
    if o6 != "none" and o9 != "none" and o6.cname == o9.cname:
        "your opponent has two matching cards!"
        $ o6.owned = 3
        $ o6 = "none"
        $ o9.owned = 3
        $ o9 = "none"
        $ gfo_score +=1
    if o7 != "none" and o8 != "none" and o7.cname == o8.cname:
        "your opponent has two matching cards!"
        $ o7.owned = 3
        $ o7 = "none"
        $ o8.owned = 3
        $ o8 = "none"
        $ gfo_score +=1
    if o7 != "none" and o9 != "none" and o7.cname == o9.cname:
        "your opponent has two matching cards!"
        $ o7.owned = 3
        $ o7 = "none"
        $ o9.owned = 3
        $ o9 = "none"
        $ gfo_score +=1
    if o8 != "none" and o9 != "none" and o8.cname == o9.cname:
        "your opponent has two matching cards!"
        $ o8.owned = 3
        $ o8 = "none"
        $ o9.owned = 3
        $ o9 = "none"
        $ gfo_score +=1

    if gf_deck_remaining <=0:
        "there are no cards left!"
        jump gf_score_calc

    if not match_sets_checked:
        $ match_sets_checked = True
        if go_fish_talk and not k_gf_start_check:
            $ k_gf_start_check = True
            if gfo_score >=1:
                pass

        jump card_background

    if p1 == "none" and p2 == "none" and p3 == "none" and p4 == "none" and p5 == "none" and p6 == "none" and p7 == "none" and p8 == "none" and p9 == "none":
        y "looks like i need to draw another card..."
        jump gf_player_fish

    if o1 == "none" and o2 == "none" and o3 == "none" and o4 == "none" and o5 == "none" and o6 == "none" and o7 == "none" and o8 == "none" and o9 == "none":
        k3 "i'll just draw another..."
        jump gf_opp_fish

    if not gf_player_turn:
        $ gf_player_turn = True
        jump gf_opp_turn

    if go_fish_talk:
        if go_fish_convo ==1:
            $ go_fish_convo = 2
            k3_n "there's just so many schemes and people..."
            k3_n "maybe i'm crazy."
        elif go_fish_convo ==3:
            $ go_fish_convo = 4
            k3_p "you think that, too?"
            y "yeah, where i come from back in repub... er..."
            k3_s "hmm?"
            y "...back at the air temple, life was pretty simple."
        elif go_fish_convo ==5:
            $ go_fish_convo = 6
            k3_u "that had to be rough."
            y "it was."
            y "so i just didn't bother."
            k3_n "what do you mean?"
        elif go_fish_convo ==7:
            $ go_fish_convo = 8
            k3_s "you're right, sorry."
            k3_s "we've all come a long way."
            y "i was thrust into this... and i've done my best to do my share."
            k3_n "...i know."
            y "i know you do."
            y "i don't know {i}how{/i} you do... but i won't ask."


    if match_sets_checked:
        jump card_chooser

label card_chooser:
    jump gf_player_card_find

label gf_player_card_find:
    if p1 == "none":
        if p2 == "none":
            if p3 == "none":
                if p4 == "none":
                    if p5 == "none":
                        if p6 == "none":
                            if p7 == "none":
                                if p8 == "none":
                                    if p9 == "none":
                                        pass
                                    else:
                                        $ p1 = p9
                                        $ p9 = "none"
                                else:

                                    $ p1 = p8
                                    $ p8 = "none"
                            else:

                                $ p1 = p7
                                $ p7 = "none"
                        else:

                            $ p1 = p6
                            $ p6 = "none"
                    else:

                        $ p1 = p5
                        $ p5 = "none"
                else:

                    $ p1 = p4
                    $ p4 = "none"
            else:

                $ p1 = p3
                $ p3 = "none"
        else:

            $ p1 = p2
            $ p2 = "none"


    if p2 == "none":
        if p3 == "none":
            if p4 == "none":
                if p5 == "none":
                    if p6 == "none":
                        if p7 == "none":
                            if p8 == "none":
                                if p9 == "none":
                                    pass
                                else:
                                    $ p2 = p9
                                    $ p9 = "none"
                            else:
                                $ p2 = p8
                                $ p8 = "none"
                        else:
                            $ p2 = p7
                            $ p7 = "none"
                    else:
                        $ p2 = p6
                        $ p6 = "none"
                else:
                    $ p2 = p5
                    $ p5 = "none"
            else:
                $ p2 = p4
                $ p4 = "none"
        else:
            $ p2 = p3
            $ p3 = "none"

    if p3 == "none":
        if p4 == "none":
            if p5 == "none":
                if p6 == "none":
                    if p7 == "none":
                        if p8 == "none":
                            if p9 == "none":
                                pass
                            else:
                                $ p3 = p9
                                $ p9 = "none"
                        else:
                            $ p3 = p8
                            $ p8 = "none"
                    else:
                        $ p3 = p7
                        $ p7 = "none"
                else:
                    $ p3 = p6
                    $ p6 = "none"
            else:
                $ p3 = p5
                $ p5 = "none"
        else:
            $ p3 = p4
            $ p4 = "none"

    if p4 == "none":
        if p5 == "none":
            if p6 == "none":
                if p7 == "none":
                    if p8 == "none":
                        if p9 == "none":
                            pass
                        else:
                            $ p4 = p9
                            $ p9 = "none"
                    else:
                        $ p4 = p8
                        $ p8 = "none"
                else:
                    $ p4 = p7
                    $ p7 = "none"
            else:
                $ p4 = p6
                $ p6 = "none"
        else:
            $ p4 = p5
            $ p5 = "none"

    if p5 == "none":
        if p6 == "none":
            if p7 == "none":
                if p8 == "none":
                    if p9 == "none":
                        pass
                    else:
                        $ p5 = p9
                        $ p9 = "none"
                else:
                    $ p5 = p8
                    $ p8 = "none"
            else:
                $ p5 = p7
                $ p7 = "none"
        else:
            $ p5 = p6
            $ p6 = "none"

    if p6 == "none":
        if p7 == "none":
            if p8 == "none":
                if p9 == "none":
                    pass
                else:
                    $ p6 = p9
                    $ p9 = "none"
            else:
                $ p6 = p8
                $ p8 = "none"
        else:
            $ p6 = p7
            $ p7 = "none"

    if p7 == "none":
        if p8 == "none":
            if p9 == "none":
                pass
            else:
                $ p7 = p9
                $ p9 = "none"
        else:
            $ p7 = p8
            $ p8 = "none"

    if p8 == "none":
        if p9 == "none":
            pass
        else:
            $ p7 = p9
            $ p9 = "none"

    jump gf_opp_card_finder

label gf_opp_card_finder:
    if o1 == "none":
        if o2 == "none":
            if o3 == "none":
                if o4 == "none":
                    if o5 == "none":
                        if o6 == "none":
                            if o7 == "none":
                                if o8 == "none":
                                    if o9 == "none":
                                        pass
                                    else:
                                        $ o1 = o9
                                        $ o9 = "none"
                                else:

                                    $ o1 = o8
                                    $ o8 = "none"
                            else:

                                $ o1 = o7
                                $ o7 = "none"
                        else:

                            $ o1 = o6
                            $ o6 = "none"
                    else:

                        $ o1 = o5
                        $ o5 = "none"
                else:

                    $ o1 = o4
                    $ o4 = "none"
            else:

                $ o1 = o3
                $ o3 = "none"
        else:

            $ o1 = o2
            $ o2 = "none"


    if o2 == "none":
        if o3 == "none":
            if o4 == "none":
                if o5 == "none":
                    if o6 == "none":
                        if o7 == "none":
                            if o8 == "none":
                                if o9 == "none":
                                    pass
                                else:
                                    $ o2 = o9
                                    $ o9 = "none"
                            else:
                                $ o2 = o8
                                $ o8 = "none"
                        else:
                            $ o2 = o7
                            $ o7 = "none"
                    else:
                        $ o2 = o6
                        $ o6 = "none"
                else:
                    $ o2 = o5
                    $ o5 = "none"
            else:
                $ o2 = o4
                $ o4 = "none"
        else:
            $ o2 = o3
            $ o3 = "none"

    if o3 == "none":
        if o4 == "none":
            if o5 == "none":
                if o6 == "none":
                    if o7 == "none":
                        if o8 == "none":
                            if o9 == "none":
                                pass
                            else:
                                $ o3 = o9
                                $ o9 = "none"
                        else:
                            $ o3 = o8
                            $ o8 = "none"
                    else:
                        $ o3 = o7
                        $ o7 = "none"
                else:
                    $ o3 = o6
                    $ o6 = "none"
            else:
                $ o3 = o5
                $ o5 = "none"
        else:
            $ o3 = o4
            $ o4 = "none"

    if o4 == "none":
        if o5 == "none":
            if o6 == "none":
                if o7 == "none":
                    if o8 == "none":
                        if o9 == "none":
                            pass
                        else:
                            $ o4 = o9
                            $ o9 = "none"
                    else:
                        $ o4 = o8
                        $ o8 = "none"
                else:
                    $ o4 = o7
                    $ o7 = "none"
            else:
                $ o4 = o6
                $ o6 = "none"
        else:
            $ o4 = o5
            $ o5 = "none"

    if o5 == "none":
        if o6 == "none":
            if o7 == "none":
                if o8 == "none":
                    if o9 == "none":
                        pass
                    else:
                        $ o5 = o9
                        $ o9 = "none"
                else:
                    $ o5 = o8
                    $ o8 = "none"
            else:
                $ o5 = o7
                $ o7 = "none"
        else:
            $ o5 = o6
            $ o6 = "none"

    if o6 == "none":
        if o7 == "none":
            if o8 == "none":
                if o9 == "none":
                    pass
                else:
                    $ o6 = o9
                    $ o9 = "none"
            else:
                $ o6 = o8
                $ o8 = "none"
        else:
            $ o6 = o7
            $ o7 = "none"

    if o7 == "none":
        if o8 == "none":
            if o9 == "none":
                pass
            else:
                $ o7 = o9
                $ o9 = "none"
        else:
            $ o7 = o8
            $ o8 = "none"

    if o8 == "none":
        if o9 == "none":
            pass
        else:
            $ o7 = o9
            $ o9 = "none"

    if not gf_card_finder:
        $ gf_card_finder = True
        jump card_background
    else:

        $ gf_card_finder = False
        jump gf_card_chooser

label gf_card_chooser:

    if not gf_my_turn:
        $ gf_my_turn = True
        y "alright, i'll start."
        y "it's my turn... i gotta pick a card."
    $ match_sets_checked = False
    call screen card_selecter
    if _return == 1:
        y "Do you have a [p1.cname]?"
        if o1 != "none" and o1.cname == p1.cname:
            k3_h "yes!"
            $ o1.owned = 3
            $ o1 = "none"
            $ p1.owned = 3
            $ p1 = "none"
        elif o2 != "none" and o2.cname == p1.cname:
            k3_h "yes!"
            $ o2.owned = 3
            $ o2 = "none"
            $ p1.owned = 3
            $ p1 = "none"
        elif o3 != "none" and o3.cname == p1.cname:
            k3_h "yes!"
            $ o3.owned = 3
            $ o3 = "none"
            $ p1.owned = 3
            $ p1 = "none"
        elif o4 != "none" and o4.cname == p1.cname:
            k3_h "yes!"
            $ o4.owned = 3
            $ o4 = "none"
            $ p1.owned = 3
            $ p1 = "none"
        elif o5 != "none" and o5.cname == p1.cname:
            k3_h "yes!"
            $ o5.owned = 3
            $ o5 = "none"
            $ p1.owned = 3
            $ p1 = "none"
        elif o6 != "none" and o6.cname == p1.cname:
            k3_h "yes!"
            $ o6.owned = 3
            $ o6 = "none"
            $ p1.owned = 3
            $ p1 = "none"
        elif o7 != "none" and o7.cname == p1.cname:
            k3_h "yes!"
            $ o7.owned = 3
            $ o7 = "none"
            $ p1.owned = 3
            $ p1 = "none"
        elif o8 != "none" and o8.cname == p1.cname:
            k3_h "yes!"
            $ o8.owned = 3
            $ o8 = "none"
            $ p1.owned = 3
            $ p1 = "none"
        elif o9 != "none" and o9.cname == p1.cname:
            k3_h "yes!"
            $ o9.owned = 3
            $ o9 = "none"
            $ p1.owned = 3
            $ p1 = "none"
        else:
            k3_h "go fish!"
            $ go_fishing = True
    elif _return == 2:
        y "Do you have a [p2.cname]?"
        if o1 != "none" and o1.cname == p2.cname:
            k3_h "yes!"
            $ o1.owned = 3
            $ o1 = "none"
            $ p2.owned = 3
            $ p2 = "none"
        elif o2 != "none" and o2.cname == p2.cname:
            k3_h "yes!"
            $ o2.owned = 3
            $ o2 = "none"
            $ p2.owned = 3
            $ p2 = "none"
        elif o3 != "none" and o3.cname == p2.cname:
            k3_h "yes!"
            $ o3.owned = 3
            $ o3 = "none"
            $ p2.owned = 3
            $ p2 = "none"
        elif o4 != "none" and o4.cname == p2.cname:
            k3_h "yes!"
            $ o4.owned = 3
            $ o4 = "none"
            $ p2.owned = 3
            $ p2 = "none"
        elif o5 != "none" and o5.cname == p2.cname:
            k3_h "yes!"
            $ o5.owned = 3
            $ o5 = "none"
            $ p2.owned = 3
            $ p2 = "none"
        elif o6 != "none" and o6.cname == p2.cname:
            k3_h "yes!"
            $ o6.owned = 3
            $ o6 = "none"
            $ p2.owned = 3
            $ p2 = "none"
        elif o7 != "none" and o7.cname == p2.cname:
            k3_h "yes!"
            $ o7.owned = 3
            $ o7 = "none"
            $ p2.owned = 3
            $ p2 = "none"
        elif o8 != "none" and o8.cname == p2.cname:
            k3_h "yes!"
            $ o8.owned = 3
            $ o8 = "none"
            $ p2.owned = 3
            $ p2 = "none"
        elif o9 != "none" and o9.cname == p2.cname:
            k3_h "yes!"
            $ o9.owned = 3
            $ o9 = "none"
            $ p2.owned = 3
            $ p2 = "none"
        else:
            k3_h "go fish!"
            $ go_fishing = True
    elif _return == 3:
        y "Do you have a [p3.cname]?"
        if o1 != "none" and o1.cname == p3.cname:
            k3_h "yes!"
            $ o1.owned = 3
            $ o1 = "none"
            $ p3.owned = 3
            $ p3 = "none"
        elif o2 != "none" and o2.cname == p3.cname:
            k3_h "yes!"
            $ o2.owned = 3
            $ o2 = "none"
            $ p3.owned = 3
            $ p3 = "none"
        elif o3 != "none" and o3.cname == p3.cname:
            k3_h "yes!"
            $ o3.owned = 3
            $ o3 = "none"
            $ p3.owned = 3
            $ p3 = "none"
        elif o4 != "none" and o4.cname == p3.cname:
            k3_h "yes!"
            $ o4.owned = 3
            $ o4 = "none"
            $ p3.owned = 3
            $ p3 = "none"
        elif o5 != "none" and o5.cname == p3.cname:
            k3_h "yes!"
            $ o5.owned = 3
            $ o5 = "none"
            $ p3.owned = 3
            $ p3 = "none"
        elif o6 != "none" and o6.cname == p3.cname:
            k3_h "yes!"
            $ o6.owned = 3
            $ o6 = "none"
            $ p3.owned = 3
            $ p3 = "none"
        elif o7 != "none" and o7.cname == p3.cname:
            k3_h "yes!"
            $ o7.owned = 3
            $ o7 = "none"
            $ p3.owned = 3
            $ p3 = "none"
        elif o8 != "none" and o8.cname == p3.cname:
            k3_h "yes!"
            $ o8.owned = 3
            $ o8 = "none"
            $ p3.owned = 3
            $ p3 = "none"
        elif o9 != "none" and o9.cname == p3.cname:
            k3_h "yes!"
            $ o9.owned = 3
            $ o9 = "none"
            $ p3.owned = 3
            $ p3 = "none"
        else:
            k3_h "go fish!"
            $ go_fishing = True
    elif _return == 4:
        y "Do you have a [p4.cname]?"
        if o1 != "none" and o1.cname == p4.cname:
            k3_h "yes!"
            $ o1.owned = 3
            $ o1 = "none"
            $ p4.owned = 3
            $ p4 = "none"
        elif o2 != "none" and o2.cname == p4.cname:
            k3_h "yes!"
            $ o2.owned = 3
            $ o2 = "none"
            $ p4.owned = 3
            $ p4 = "none"
        elif o3 != "none" and o3.cname == p4.cname:
            k3_h "yes!"
            $ o3.owned = 3
            $ o3 = "none"
            $ p4.owned = 3
            $ p4 = "none"
        elif o4 != "none" and o4.cname == p4.cname:
            k3_h "yes!"
            $ o4.owned = 3
            $ o4 = "none"
            $ p4.owned = 3
            $ p4 = "none"
        elif o5 != "none" and o5.cname == p4.cname:
            k3_h "yes!"
            $ o5.owned = 3
            $ o5 = "none"
            $ p4.owned = 3
            $ p4 = "none"
        elif o6 != "none" and o6.cname == p4.cname:
            k3_h "yes!"
            $ o6.owned = 3
            $ o6 = "none"
            $ p4.owned = 3
            $ p4 = "none"
        elif o7 != "none" and o7.cname == p4.cname:
            k3_h "yes!"
            $ o7.owned = 3
            $ o7 = "none"
            $ p4.owned = 3
            $ p4 = "none"
        elif o8 != "none" and o8.cname == p4.cname:
            k3_h "yes!"
            $ o8.owned = 3
            $ o8 = "none"
            $ p4.owned = 3
            $ p4 = "none"
        elif o9 != "none" and o9.cname == p4.cname:
            k3_h "yes!"
            $ o9.owned = 3
            $ o9 = "none"
            $ p4.owned = 3
            $ p4 = "none"
        else:
            k3_h "go fish!"
            $ go_fishing = True
    elif _return == 5:
        y "Do you have a [p5.cname]?"
        if o1 != "none" and o1.cname == p5.cname:
            k3_h "yes!"
            $ o1.owned = 3
            $ o1 = "none"
            $ p5.owned = 3
            $ p5 = "none"
        elif o2 != "none" and o2.cname == p5.cname:
            k3_h "yes!"
            $ o2.owned = 3
            $ o2 = "none"
            $ p5.owned = 3
            $ p5 = "none"
        elif o3 != "none" and o3.cname == p5.cname:
            k3_h "yes!"
            $ o3.owned = 3
            $ o3 = "none"
            $ p5.owned = 3
            $ p5 = "none"
        elif o4 != "none" and o4.cname == p5.cname:
            k3_h "yes!"
            $ o4.owned = 3
            $ o4 = "none"
            $ p5.owned = 3
            $ p5 = "none"
        elif o5 != "none" and o5.cname == p5.cname:
            k3_h "yes!"
            $ o5.owned = 3
            $ o5 = "none"
            $ p5.owned = 3
            $ p5 = "none"
        elif o6 != "none" and o6.cname == p5.cname:
            k3_h "yes!"
            $ o6.owned = 3
            $ o6 = "none"
            $ p5.owned = 3
            $ p5 = "none"
        elif o7 != "none" and o7.cname == p5.cname:
            k3_h "yes!"
            $ o7.owned = 3
            $ o7 = "none"
            $ p5.owned = 3
            $ p5 = "none"
        elif o8 != "none" and o8.cname == p5.cname:
            k3_h "yes!"
            $ o8.owned = 3
            $ o8 = "none"
            $ p5.owned = 3
            $ p5 = "none"
        elif o9 != "none" and o9.cname == p5.cname:
            k3_h "yes!"
            $ o9.owned = 3
            $ o9 = "none"
            $ p5.owned = 3
            $ p5 = "none"
        else:
            k3_h "go fish!"
            $ go_fishing = True
    elif _return == 6:
        y "Do you have a [p6.cname]?"
        if o1 != "none" and o1.cname == p6.cname:
            k3_h "yes!"
            $ o1.owned = 3
            $ o1 = "none"
            $ p6.owned = 3
            $ p6 = "none"
        elif o2 != "none" and o2.cname == p6.cname:
            k3_h "yes!"
            $ o2.owned = 3
            $ o2 = "none"
            $ p6.owned = 3
            $ p6 = "none"
        elif o3 != "none" and o3.cname == p6.cname:
            k3_h "yes!"
            $ o3.owned = 3
            $ o3 = "none"
            $ p6.owned = 3
            $ p6 = "none"
        elif o4 != "none" and o4.cname == p6.cname:
            k3_h "yes!"
            $ o4.owned = 3
            $ o4 = "none"
            $ p6.owned = 3
            $ p6 = "none"
        elif o5 != "none" and o5.cname == p6.cname:
            k3_h "yes!"
            $ o5.owned = 3
            $ o5 = "none"
            $ p6.owned = 3
            $ p6 = "none"
        elif o6 != "none" and o6.cname == p6.cname:
            k3_h "yes!"
            $ o6.owned = 3
            $ o6 = "none"
            $ p6.owned = 3
            $ p6 = "none"
        elif o7 != "none" and o7.cname == p6.cname:
            k3_h "yes!"
            $ o7.owned = 3
            $ o7 = "none"
            $ p6.owned = 3
            $ p6 = "none"
        elif o8 != "none" and o8.cname == p6.cname:
            k3_h "yes!"
            $ o8.owned = 3
            $ o8 = "none"
            $ p6.owned = 3
            $ p6 = "none"
        elif o9 != "none" and o9.cname == p6.cname:
            k3_h "yes!"
            $ o9.owned = 3
            $ o9 = "none"
            $ p6.owned = 3
            $ p6 = "none"
        else:
            k3_h "go fish!"
            $ go_fishing = True
    elif _return == 7:
        y "Do you have a [p7.cname]?"
        if o1 != "none" and o1.cname == p7.cname:
            k3_h "yes!"
            $ o1.owned = 3
            $ o1 = "none"
            $ p7.owned = 3
            $ p7 = "none"
        elif o2 != "none" and o2.cname == p7.cname:
            k3_h "yes!"
            $ o2.owned = 3
            $ o2 = "none"
            $ p7.owned = 3
            $ p7 = "none"
        elif o3 != "none" and o3.cname == p7.cname:
            k3_h "yes!"
            $ o3.owned = 3
            $ o3 = "none"
            $ p7.owned = 3
            $ p7 = "none"
        elif o4 != "none" and o4.cname == p7.cname:
            k3_h "yes!"
            $ o4.owned = 3
            $ o4 = "none"
            $ p7.owned = 3
            $ p7 = "none"
        elif o5 != "none" and o5.cname == p7.cname:
            k3_h "yes!"
            $ o5.owned = 3
            $ o5 = "none"
            $ p7.owned = 3
            $ p7 = "none"
        elif o6 != "none" and o6.cname == p7.cname:
            k3_h "yes!"
            $ o6.owned = 3
            $ o6 = "none"
            $ p7.owned = 3
            $ p7 = "none"
        elif o7 != "none" and o7.cname == p7.cname:
            k3_h "yes!"
            $ o7.owned = 3
            $ o7 = "none"
            $ p7.owned = 3
            $ p7 = "none"
        elif o8 != "none" and o8.cname == p7.cname:
            k3_h "yes!"
            $ o8.owned = 3
            $ o8 = "none"
            $ p7.owned = 3
            $ p7 = "none"
        elif o9 != "none" and o9.cname == p7.cname:
            k3_h "yes!"
            $ o9.owned = 3
            $ o9 = "none"
            $ p7.owned = 3
            $ p7 = "none"
        else:
            k3_h "go fish!"
            $ go_fishing = True
    elif _return == 8:
        y "Do you have a [p8.cname]?"
        if o1 != "none" and o1.cname == p8.cname:
            k3_h "yes!"
            $ o1.owned = 3
            $ o1 = "none"
            $ p8.owned = 3
            $ p8 = "none"
        elif o2 != "none" and o2.cname == p8.cname:
            k3_h "yes!"
            $ o2.owned = 3
            $ o2 = "none"
            $ p8.owned = 3
            $ p8 = "none"
        elif o3 != "none" and o3.cname == p8.cname:
            k3_h "yes!"
            $ o3.owned = 3
            $ o3 = "none"
            $ p8.owned = 3
            $ p8 = "none"
        elif o4 != "none" and o4.cname == p8.cname:
            k3_h "yes!"
            $ o4.owned = 3
            $ o4 = "none"
            $ p8.owned = 3
            $ p8 = "none"
        elif o5 != "none" and o5.cname == p8.cname:
            k3_h "yes!"
            $ o5.owned = 3
            $ o5 = "none"
            $ p8.owned = 3
            $ p8 = "none"
        elif o6 != "none" and o6.cname == p8.cname:
            k3_h "yes!"
            $ o6.owned = 3
            $ o6 = "none"
            $ p8.owned = 3
            $ p8 = "none"
        elif o7 != "none" and o7.cname == p8.cname:
            k3_h "yes!"
            $ o7.owned = 3
            $ o7 = "none"
            $ p8.owned = 3
            $ p8 = "none"
        elif o8 != "none" and o8.cname == p8.cname:
            k3_h "yes!"
            $ o8.owned = 3
            $ o8 = "none"
            $ p8.owned = 3
            $ p8 = "none"
        elif o9 != "none" and o9.cname == p8.cname:
            k3_h "yes!"
            $ o9.owned = 3
            $ o9 = "none"
            $ p8.owned = 3
            $ p8 = "none"
        else:
            k3_h "go fish!"
            $ go_fishing = True
    elif _return == 9:
        y "Do you have a [p9.cname]?"
        if o1 != "none" and o1.cname == p9.cname:
            k3_h "yes!"
            $ o1.owned = 3
            $ o1 = "none"
            $ p9.owned = 3
            $ p9 = "none"
        elif o2 != "none" and o2.cname == p9.cname:
            k3_h "yes!"
            $ o2.owned = 3
            $ o2 = "none"
            $ p9.owned = 3
            $ p9 = "none"
        elif o3 != "none" and o3.cname == p9.cname:
            k3_h "yes!"
            $ o3.owned = 3
            $ o3 = "none"
            $ p9.owned = 3
            $ p9 = "none"
        elif o4 != "none" and o4.cname == p9.cname:
            k3_h "yes!"
            $ o4.owned = 3
            $ o4 = "none"
            $ p9.owned = 3
            $ p9 = "none"
        elif o5 != "none" and o5.cname == p9.cname:
            k3_h "yes!"
            $ o5.owned = 3
            $ o5 = "none"
            $ p9.owned = 3
            $ p9 = "none"
        elif o6 != "none" and o6.cname == p9.cname:
            k3_h "yes!"
            $ o6.owned = 3
            $ o6 = "none"
            $ p9.owned = 3
            $ p9 = "none"
        elif o7 != "none" and o7.cname == p9.cname:
            k3_h "yes!"
            $ o7.owned = 3
            $ o7 = "none"
            $ p9.owned = 3
            $ p9 = "none"
        elif o8 != "none" and o8.cname == p9.cname:
            k3_h "yes!"
            $ o8.owned = 3
            $ o8 = "none"
            $ p9.owned = 3
            $ p9 = "none"
        elif o9 != "none" and o9.cname == p9.cname:
            k3_h "yes!"
            $ o9.owned = 3
            $ o9 = "none"
            $ p9.owned = 3
            $ p9 = "none"
        else:
            k3_h "go fish!"
            $ go_fishing = True

    $ gfp_score +=1
    $ gf_player_turn = False
    if p1 == "none" and p2 == "none" and p3 == "none" and p4 == "none" and p5 == "none" and p6 == "none" and p7 == "none" and p8 == "none" and p9 == "none":
        y "looks like i need to draw another card..."
        if gf_deck_remaining <=0:
            "there's none left!"
            jump gf_score_calc
        $ gfp_score +=1
        $ go_fishing = True
        $ gf_player_turn = True
    if not go_fishing:
        $ gf_player_turn = True
    jump card_background


label gf_player_fish:
    if p1 == "none":
        $ gf_deck_remaining -=1
        $ player_card1 = cardlist.pop()
        $ p1 = player_card1
        $ player_card1.owned = 1
        $ pcard1_xpos = 6
        $ pcard1_ypos = 400

    elif p2 == "none":
        $ gf_deck_remaining -=1
        $ player_card2 = cardlist.pop()
        $ p2 = player_card2
        $ player_card2.owned = 1
        $ pcard2_xpos = 106
        $ pcard2_ypos = 400

    elif p3 == "none":
        $ gf_deck_remaining -=1
        $ player_card3 = cardlist.pop()
        $ p3 = player_card3
        $ player_card3.owned = 1
        $ pcard3_xpos = 206
        $ pcard3_ypos = 400

    elif p4 == "none":
        $ gf_deck_remaining -=1
        $ player_card4 = cardlist.pop()
        $ p4 = player_card4
        $ player_card4.owned = 1
        $ pcard4_xpos = 306
        $ pcard4_ypos = 400

    elif p5 == "none":
        $ gf_deck_remaining -=1
        $ player_card5 = cardlist.pop()
        $ p5 = player_card5
        $ player_card5.owned = 1
        $ pcard5_xpos = 406
        $ pcard5_ypos = 400

    elif p6 == "none":
        $ gf_deck_remaining -=1
        $ player_card6 = cardlist.pop()
        $ p6 = player_card6
        $ player_card6.owned = 1
        $ pcard6_xpos = 506
        $ pcard6_ypos = 400

    elif p7 == "none":
        $ gf_deck_remaining -=1
        $ player_card7 = cardlist.pop()
        $ p7 = player_card7
        $ player_card7.owned = 1
        $ pcard7_xpos = 606
        $ pcard7_ypos = 400

    elif p8 == "none":
        $ gf_deck_remaining -=1
        $ player_card8 = cardlist.pop()
        $ p8 = player_card8
        $ player_card8.owned = 1
        $ pcard8_xpos = 706
        $ pcard8_ypos = 400

    elif p9 == "none":
        $ gf_deck_remaining -=1
        $ player_card9 = cardlist.pop()
        $ p9 = player_card9
        $ player_card9.owned = 1
        $ pcard9_xpos = 806
        $ pcard9_ypos = 400
    else:

        "your hand is full, you can't draw any more!"

    jump card_background

label gf_opp_turn:
    if go_fish_talk:
        if go_fish_convo ==0:
            $ go_fish_convo = 1
            k3_n "things seem so complicated nowadays, don't they?"
            y "what do you mean?"
        elif go_fish_convo ==2:
            $ go_fish_convo = 3
            y "you're definitely not crazy."
            y "i think the world just turned out to be bigger than we expected."
        elif go_fish_convo ==4:
            $ go_fish_convo = 5
            k3_n "you didn't get up to much trouble?"
            y "i mean, a little, but not really."
            y "the avatar before me was so celebrated, they were still all the people could talk about..."
            y "even after i was discovered."
        elif go_fish_convo ==6:
            $ go_fish_convo = 7
            y "i mean that i didn't bother to learn anything."
            k3_p "but... you're the avatar!"
            k3_p "it's your duty to-"
            y "i know, okay? i know."
            y "I heard it all."
            y "and... i've come a long way since then."
        elif go_fish_convo ==8:
            $ go_fish_convo = 9
            k3_n "thank you."
            k3_p "now, and this is important..."
            k3_s "tits."
            y "what?"
            k3_n "boobs."
            k3_h "massive knockers."
            y "you're... just trying to distract me."
            y "take your turn."
            k3_h "you got me..."
            k3_n "alright, let's just play for a bit."

    $ match_sets_checked = False
    $ rand_opp_card = renpy.random.randint(1,9)
    if rand_opp_card == 1:
        $ gf_rand_card = o1
        if o1 == "none":
            jump gf_opp_turn
    if rand_opp_card == 2:
        $ gf_rand_card = o2
        if o2 == "none":
            jump gf_opp_turn
    if rand_opp_card == 3:
        $ gf_rand_card = o3
        if o3 == "none":
            jump gf_opp_turn
    if rand_opp_card == 4:
        $ gf_rand_card = o4
        if o4 == "none":
            jump gf_opp_turn
    if rand_opp_card == 5:
        $ gf_rand_card = o5
        if o5 == "none":
            jump gf_opp_turn
    if rand_opp_card == 6:
        $ gf_rand_card = o6
        if o6 == "none":
            jump gf_opp_turn
    if rand_opp_card == 7:
        $ gf_rand_card = o7
        if o7 == "none":
            jump gf_opp_turn
    if rand_opp_card == 8:
        $ gf_rand_card = o8
        if o8 == "none":
            jump gf_opp_turn
    if rand_opp_card == 9:
        $ gf_rand_card = o9
        if o9 == "none":
            jump gf_opp_turn

    if gf_rand_card == o1:
        k3_n "do you have a [o1.cname]?"

        if p1 != "none" and o1.cname == p1.cname:
            y "i do..."
            $ o1.owned = 3
            $ o1 = "none"
            $ p1.owned = 3
            $ p1 = "none"
        elif p2 != "none" and o1.cname == p2.cname:
            y "i do..."
            $ o1.owned = 3
            $ o1 = "none"
            $ p2.owned = 3
            $ p2 = "none"
        elif p3 != "none" and o1.cname == p3.cname:
            y "i do..."
            $ o1.owned = 3
            $ o1 = "none"
            $ p3.owned = 3
            $ p3 = "none"
        elif p4 != "none" and o1.cname == p4.cname:
            y "i do..."
            $ o1.owned = 3
            $ o1 = "none"
            $ p4.owned = 3
            $ p4 = "none"
        elif p5 != "none" and o1.cname == p5.cname:
            y "i do..."
            $ o1.owned = 3
            $ o1 = "none"
            $ p5.owned = 3
            $ p5 = "none"
        elif p6 != "none" and o1.cname == p6.cname:
            y "i do..."
            $ o1.owned = 3
            $ o1 = "none"
            $ p6.owned = 3
            $ p6 = "none"
        elif p7 != "none" and o1.cname == p7.cname:
            y "i do..."
            $ o1.owned = 3
            $ o1 = "none"
            $ p7.owned = 3
            $ p7 = "none"
        elif p8 != "none" and o1.cname == p8.cname:
            y "i do..."
            $ o1.owned = 3
            $ o1 = "none"
            $ p8.owned = 3
            $ p8 = "none"
        elif p9 != "none" and o1.cname == p9.cname:
            y "i do..."
            $ o1.owned = 3
            $ o1 = "none"
            $ p9.owned = 3
            $ p9 = "none"
        else:
            y "go fish."
            $ opp_go_fishing = True

    if gf_rand_card == o2:
        k3_n "do you have a [o2.cname]?"
        if p1 != "none" and o2.cname == p1.cname:
            y "i do..."
            $ o2.owned = 3
            $ o2 = "none"
            $ p1.owned = 3
            $ p1 = "none"
        elif p2 != "none" and o2.cname == p2.cname:
            y "i do..."
            $ o2.owned = 3
            $ o2 = "none"
            $ p2.owned = 3
            $ p2 = "none"
        elif p3 != "none" and o2.cname == p3.cname:
            y "i do..."
            $ o2.owned = 3
            $ o2 = "none"
            $ p3.owned = 3
            $ p3 = "none"
        elif p4 != "none" and o2.cname == p4.cname:
            y "i do..."
            $ o2.owned = 3
            $ o2 = "none"
            $ p4.owned = 3
            $ p4 = "none"
        elif p5 != "none" and o2.cname == p5.cname:
            y "i do..."
            $ o2.owned = 3
            $ o2 = "none"
            $ p5.owned = 3
            $ p5 = "none"
        elif p6 != "none" and o2.cname == p6.cname:
            y "i do..."
            $ o2.owned = 3
            $ o2 = "none"
            $ p6.owned = 3
            $ p6 = "none"
        elif p7 != "none" and o2.cname == p7.cname:
            y "i do..."
            $ o2.owned = 3
            $ o2 = "none"
            $ p7.owned = 3
            $ p7 = "none"
        elif p8 != "none" and o2.cname == p8.cname:
            y "i do..."
            $ o2.owned = 3
            $ o2 = "none"
            $ p8.owned = 3
            $ p8 = "none"
        elif p9 != "none" and o2.cname == p9.cname:
            y "i do..."
            $ o2.owned = 3
            $ o2 = "none"
            $ p9.owned = 3
            $ p9 = "none"
        else:
            y "go fish."
            $ opp_go_fishing = True

    if gf_rand_card == o3:
        k3_n "do you have a [o3.cname]?"
        if p1 != "none" and o3.cname == p1.cname:
            y "i do..."
            $ o3.owned = 3
            $ o3 = "none"
            $ p1.owned = 3
            $ p1 = "none"
        elif p2 != "none" and o3.cname == p2.cname:
            y "i do..."
            $ o3.owned = 3
            $ o3 = "none"
            $ p2.owned = 3
            $ p2 = "none"
        elif p3 != "none" and o3.cname == p3.cname:
            y "i do..."
            $ o3.owned = 3
            $ o3 = "none"
            $ p3.owned = 3
            $ p3 = "none"
        elif p4 != "none" and o3.cname == p4.cname:
            y "i do..."
            $ o3.owned = 3
            $ o3 = "none"
            $ p4.owned = 3
            $ p4 = "none"
        elif p5 != "none" and o3.cname == p5.cname:
            y "i do..."
            $ o3.owned = 3
            $ o3 = "none"
            $ p5.owned = 3
            $ p5 = "none"
        elif p6 != "none" and o3.cname == p6.cname:
            y "i do..."
            $ o3.owned = 3
            $ o3 = "none"
            $ p6.owned = 3
            $ p6 = "none"
        elif p7 != "none" and o3.cname == p7.cname:
            y "i do..."
            $ o3.owned = 3
            $ o3 = "none"
            $ p7.owned = 3
            $ p7 = "none"
        elif p8 != "none" and o3.cname == p8.cname:
            y "i do..."
            $ o3.owned = 3
            $ o3 = "none"
            $ p8.owned = 3
            $ p8 = "none"
        elif p9 != "none" and o3.cname == p9.cname:
            y "i do..."
            $ o3.owned = 3
            $ o3 = "none"
            $ p9.owned = 3
            $ p9 = "none"
        else:
            y "go fish."
            $ opp_go_fishing = True

    if gf_rand_card == o4:
        k3_n "do you have a [o4.cname]?"
        if p1 != "none" and o4.cname == p1.cname:
            y "i do..."
            $ o4.owned = 3
            $ o4 = "none"
            $ p1.owned = 3
            $ p1 = "none"
        elif p2 != "none" and o4.cname == p2.cname:
            y "i do..."
            $ o4.owned = 3
            $ o4 = "none"
            $ p2.owned = 3
            $ p2 = "none"
        elif p3 != "none" and o4.cname == p3.cname:
            y "i do..."
            $ o4.owned = 3
            $ o4 = "none"
            $ p3.owned = 3
            $ p3 = "none"
        elif p4 != "none" and o4.cname == p4.cname:
            y "i do..."
            $ o4.owned = 3
            $ o4 = "none"
            $ p4.owned = 3
            $ p4 = "none"
        elif p5 != "none" and o4.cname == p5.cname:
            y "i do..."
            $ o4.owned = 3
            $ o4 = "none"
            $ p5.owned = 3
            $ p5 = "none"
        elif p6 != "none" and o4.cname == p6.cname:
            y "i do..."
            $ o4.owned = 3
            $ o4 = "none"
            $ p6.owned = 3
            $ p6 = "none"
        elif p7 != "none" and o4.cname == p7.cname:
            y "i do..."
            $ o4.owned = 3
            $ o4 = "none"
            $ p7.owned = 3
            $ p7 = "none"
        elif p8 != "none" and o4.cname == p8.cname:
            y "i do..."
            $ o4.owned = 3
            $ o4 = "none"
            $ p8.owned = 3
            $ p8 = "none"
        elif p9 != "none" and o4.cname == p9.cname:
            y "i do..."
            $ o4.owned = 3
            $ o4 = "none"
            $ p9.owned = 3
            $ p9 = "none"
        else:
            y "go fish."
            $ opp_go_fishing = True

    if gf_rand_card == o5:
        k3_n "do you have a [o5.cname]?"
        if p1 != "none" and o5.cname == p1.cname:
            y "i do..."
            $ o5.owned = 3
            $ o5 = "none"
            $ p1.owned = 3
            $ p1 = "none"
        elif p2 != "none" and o5.cname == p2.cname:
            y "i do..."
            $ o5.owned = 3
            $ o5 = "none"
            $ p2.owned = 3
            $ p2 = "none"
        elif p3 != "none" and o5.cname == p3.cname:
            y "i do..."
            $ o5.owned = 3
            $ o5 = "none"
            $ p3.owned = 3
            $ p3 = "none"
        elif p4 != "none" and o5.cname == p4.cname:
            y "i do..."
            $ o5.owned = 3
            $ o5 = "none"
            $ p4.owned = 3
            $ p4 = "none"
        elif p5 != "none" and o5.cname == p5.cname:
            y "i do..."
            $ o5.owned = 3
            $ o5 = "none"
            $ p5.owned = 3
            $ p5 = "none"
        elif p6 != "none" and o5.cname == p6.cname:
            y "i do..."
            $ o5.owned = 3
            $ o5 = "none"
            $ p6.owned = 3
            $ p6 = "none"
        elif p7 != "none" and o5.cname == p7.cname:
            y "i do..."
            $ o5.owned = 3
            $ o5 = "none"
            $ p7.owned = 3
            $ p7 = "none"
        elif p8 != "none" and o5.cname == p8.cname:
            y "i do..."
            $ o5.owned = 3
            $ o5 = "none"
            $ p8.owned = 3
            $ p8 = "none"
        elif p9 != "none" and o5.cname == p9.cname:
            y "i do..."
            $ o5.owned = 3
            $ o5 = "none"
            $ p9.owned = 3
            $ p9 = "none"
        else:
            y "go fish."
            $ opp_go_fishing = True

    if gf_rand_card == o6:
        k3_n "do you have a [o6.cname]?"
        if p1 != "none" and o6.cname == p1.cname:
            y "i do..."
            $ o6.owned = 3
            $ o6 = "none"
            $ p1.owned = 3
            $ p1 = "none"
        elif p2 != "none" and o6.cname == p2.cname:
            y "i do..."
            $ o6.owned = 3
            $ o6 = "none"
            $ p2.owned = 3
            $ p2 = "none"
        elif p3 != "none" and o6.cname == p3.cname:
            y "i do..."
            $ o6.owned = 3
            $ o6 = "none"
            $ p3.owned = 3
            $ p3 = "none"
        elif p4 != "none" and o6.cname == p4.cname:
            y "i do..."
            $ o6.owned = 3
            $ o6 = "none"
            $ p4.owned = 3
            $ p4 = "none"
        elif p5 != "none" and o6.cname == p5.cname:
            y "i do..."
            $ o6.owned = 3
            $ o6 = "none"
            $ p5.owned = 3
            $ p5 = "none"
        elif p6 != "none" and o6.cname == p6.cname:
            y "i do..."
            $ o6.owned = 3
            $ o6 = "none"
            $ p6.owned = 3
            $ p6 = "none"
        elif p7 != "none" and o6.cname == p7.cname:
            y "i do..."
            $ o6.owned = 3
            $ o6 = "none"
            $ p7.owned = 3
            $ p7 = "none"
        elif p8 != "none" and o6.cname == p8.cname:
            y "i do..."
            $ o6.owned = 3
            $ o6 = "none"
            $ p8.owned = 3
            $ p8 = "none"
        elif p9 != "none" and o6.cname == p9.cname:
            y "i do..."
            $ o6.owned = 3
            $ o6 = "none"
            $ p9.owned = 3
            $ p9 = "none"
        else:
            y "go fish."
            $ opp_go_fishing = True

    if gf_rand_card == o7:
        k3_n "do you have a [o7.cname]?"
        if p1 != "none" and o7.cname == p1.cname:
            y "i do..."
            $ o7.owned = 3
            $ o7 = "none"
            $ p1.owned = 3
            $ p1 = "none"
        elif p2 != "none" and o7.cname == p2.cname:
            y "i do..."
            $ o7.owned = 3
            $ o7 = "none"
            $ p2.owned = 3
            $ p2 = "none"
        elif p3 != "none" and o7.cname == p3.cname:
            y "i do..."
            $ o7.owned = 3
            $ o7 = "none"
            $ p3.owned = 3
            $ p3 = "none"
        elif p4 != "none" and o7.cname == p4.cname:
            y "i do..."
            $ o7.owned = 3
            $ o7 = "none"
            $ p4.owned = 3
            $ p4 = "none"
        elif p5 != "none" and o7.cname == p5.cname:
            y "i do..."
            $ o7.owned = 3
            $ o7 = "none"
            $ p5.owned = 3
            $ p5 = "none"
        elif p6 != "none" and o7.cname == p6.cname:
            y "i do..."
            $ o7.owned = 3
            $ o7 = "none"
            $ p6.owned = 3
            $ p6 = "none"
        elif p7 != "none" and o7.cname == p7.cname:
            y "i do..."
            $ o7.owned = 3
            $ o7 = "none"
            $ p7.owned = 3
            $ p7 = "none"
        elif p8 != "none" and o7.cname == p8.cname:
            y "i do..."
            $ o7.owned = 3
            $ o7 = "none"
            $ p8.owned = 3
            $ p8 = "none"
        elif p9 != "none" and o7.cname == p9.cname:
            y "i do..."
            $ o7.owned = 3
            $ o7 = "none"
            $ p9.owned = 3
            $ p9 = "none"
        else:
            y "go fish."
            $ opp_go_fishing = True

    if gf_rand_card == o8:
        k3_n "do you have a [o8.cname]?"
        if p1 != "none" and o8.cname == p1.cname:
            y "i do..."
            $ o8.owned = 3
            $ o8 = "none"
            $ p1.owned = 3
            $ p1 = "none"
        elif p2 != "none" and o8.cname == p2.cname:
            y "i do..."
            $ o8.owned = 3
            $ o8 = "none"
            $ p2.owned = 3
            $ p2 = "none"
        elif p3 != "none" and o8.cname == p3.cname:
            y "i do..."
            $ o8.owned = 3
            $ o8 = "none"
            $ p3.owned = 3
            $ p3 = "none"
        elif p4 != "none" and o8.cname == p4.cname:
            y "i do..."
            $ o8.owned = 3
            $ o8 = "none"
            $ p4.owned = 3
            $ p4 = "none"
        elif p5 != "none" and o8.cname == p5.cname:
            y "i do..."
            $ o8.owned = 3
            $ o8 = "none"
            $ p5.owned = 3
            $ p5 = "none"
        elif p6 != "none" and o8.cname == p6.cname:
            y "i do..."
            $ o8.owned = 3
            $ o8 = "none"
            $ p6.owned = 3
            $ p6 = "none"
        elif p7 != "none" and o8.cname == p7.cname:
            y "i do..."
            $ o8.owned = 3
            $ o8 = "none"
            $ p7.owned = 3
            $ p7 = "none"
        elif p8 != "none" and o8.cname == p8.cname:
            y "i do..."
            $ o8.owned = 3
            $ o8 = "none"
            $ p8.owned = 3
            $ p8 = "none"
        elif p9 != "none" and o8.cname == p9.cname:
            y "i do..."
            $ o8.owned = 3
            $ o8 = "none"
            $ p9.owned = 3
            $ p9 = "none"
        else:
            y "go fish."
            $ opp_go_fishing = True

    if gf_rand_card == o9:
        k3_n "do you have a [o9.cname]?"
        if p1 != "none" and o9.cname == p1.cname:
            y "i do..."
            $ o9.owned = 3
            $ o9 = "none"
            $ p1.owned = 3
            $ p1 = "none"
        elif p2 != "none" and o9.cname == p2.cname:
            y "i do..."
            $ o9.owned = 3
            $ o9 = "none"
            $ p2.owned = 3
            $ p2 = "none"
        elif p3 != "none" and o9.cname == p3.cname:
            y "i do..."
            $ o9.owned = 3
            $ o9 = "none"
            $ p3.owned = 3
            $ p3 = "none"
        elif p4 != "none" and o9.cname == p4.cname:
            y "i do..."
            $ o9.owned = 3
            $ o9 = "none"
            $ p4.owned = 3
            $ p4 = "none"
        elif p5 != "none" and o9.cname == p5.cname:
            y "i do..."
            $ o9.owned = 3
            $ o9 = "none"
            $ p5.owned = 3
            $ p5 = "none"
        elif p6 != "none" and o9.cname == p6.cname:
            y "i do..."
            $ o9.owned = 3
            $ o9 = "none"
            $ p6.owned = 3
            $ p6 = "none"
        elif p7 != "none" and o9.cname == p7.cname:
            y "i do..."
            $ o9.owned = 3
            $ o9 = "none"
            $ p7.owned = 3
            $ p7 = "none"
        elif p8 != "none" and o9.cname == p8.cname:
            y "i do..."
            $ o9.owned = 3
            $ o9 = "none"
            $ p8.owned = 3
            $ p8 = "none"
        elif p9 != "none" and o9.cname == p9.cname:
            y "i do..."
            $ o9.owned = 3
            $ o9 = "none"
            $ p9.owned = 3
            $ p9 = "none"
        else:
            y "go fish."
            $ opp_go_fishing = True

    $ gf_player_turn = True
    $ gfo_score +=1
    if o1 == "none" and o2 == "none" and o3 == "none" and o4 == "none" and o5 == "none" and o6 == "none" and o7 == "none" and o8 == "none" and o9 == "none":
        k3 "i'll just draw another..."
        if gf_deck_remaining ==0:
            "there's none left!"
            jump gf_score_calc
        $ gfo_score +=1
        $ opp_go_fishing = True
        $ gf_player_turn = False
    if not opp_go_fishing:
        $ gf_player_turn = False
    jump card_background

label gf_opp_fish:
    $ rand_darn = 0
    $ rand_darn = renpy.random.randint(1,2)
    if rand_darn ==1:
        k3_p "darn..."
    if o1 == "none":
        $ gf_deck_remaining -=1
        $ opp_card1 = cardlist.pop()
        $ o1 = opp_card1
        $ opp_card1.owned = 2
        $ ocard1_xpos = 900
        $ ocard1_ypos = 10
    elif o2 == "none":
        $ gf_deck_remaining -=1
        $ opp_card2 = cardlist.pop()
        $ o2 = opp_card2
        $ opp_card2.owned = 2
        $ ocard2_xpos = 800
        $ ocard2_ypos = 10
    elif o3 == "none":
        $ gf_deck_remaining -=1
        $ opp_card3 = cardlist.pop()
        $ o3 = opp_card3
        $ opp_card3.owned = 2
        $ ocard3_xpos = 700
        $ ocard3_ypos = 10
    elif o4 == "none":
        $ gf_deck_remaining -=1
        $ opp_card4 = cardlist.pop()
        $ o4 = opp_card4
        $ opp_card4.owned = 2
        $ ocard4_xpos = 600
        $ ocard4_ypos = 10
    elif o5 == "none":
        $ gf_deck_remaining -=1
        $ opp_card5 = cardlist.pop()
        $ o5 = opp_card5
        $ opp_card5.owned = 2
        $ ocard5_xpos = 500
        $ ocard5_ypos = 10
    elif o6 == "none":
        $ gf_deck_remaining -=1
        $ opp_card6 = cardlist.pop()
        $ o6 = opp_card6
        $ opp_card6.owned = 2
        $ ocard6_xpos = 400
        $ ocard6_ypos = 10
    elif o7 == "none":
        $ gf_deck_remaining -=1
        $ opp_card7 = cardlist.pop()
        $ o7 = opp_card7
        $ opp_card7.owned = 2
        $ ocard7_xpos = 300
        $ ocard7_ypos = 10
    elif o8 == "none":
        $ gf_deck_remaining -=1
        $ opp_card8 = cardlist.pop()
        $ o8 = opp_card8
        $ opp_card8.owned = 2
        $ ocard8_xpos = 200
        $ ocard8_ypos = 10
    elif o9 == "none":
        $ gf_deck_remaining -=1
        $ opp_card9 = cardlist.pop()
        $ o9 = opp_card9
        $ opp_card9.owned = 2
        $ ocard9_xpos = 100
        $ ocard9_ypos = 10
    else:

        "their hand is full, they can't draw any more!"

    jump card_background

label gf_score_calc:
    $ gf_count +=1
    if gfp_score > gfo_score:
        $ gf_win_count +=1
        $ gf_first_win = True
        y "i win!"
        k3_h "congrats!"
    if gfp_score < gfo_score:
        k3_h "you lose!"
        y "do you have to be so happy about it?"
        k3_h "sorry!"
    if gfp_score == gfo_score:
        k3_h "it's a tie!"
        y "huh."

    y "alright..."

    if go_fish_talk:
        k3_h "that's was pretty fun."
        k3_n "wanna play with me again?"
    else:
        if gf_count ==1:
            k3_n "round two!"
            jump go_fish_begin
        if gf_count ==2:
            if gf_win_count ==2:
                k3_n "looks like you win two out of three this time."
            if gf_win_count ==1:
                k3_n "ooo, we're tied so far!"
                pass
            if gf_win_count ==0:
                k3_n "looks like you won't win two out of three this time."
        if gf_count ==3:
            if gf_win_count >=2:
                k3_n "looks like you win two out of three this time."
            else:
                k3_n "looks like you won't win two out of three this time."

    menu:
        "play again":
            jump go_fish_begin
        "i think that's enough":

            hide screen go_fish_score
            if go_fish_talk:
                $ go_fish_talk = False
                jump after_gf
            else:
                y "no thanks."
                k3_n "okay."
                scene black with dissolve
                scene inside_hospital
                show toki toki01
                with dissolve
                jump love_bk3_village_hospital_menu
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
