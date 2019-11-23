



image bfaq bfaq00 = LiveComposite(
    (1000, 720), 
    (0, 0), "bk4/asami/tits/body_1.png",
    (0, 0), "bk4/asami/tits/arms_holdjacket.png", 
    (0, 0), "bk4/asami/tits/tits1.png",  
    (0, 0), "bk4/asami/tits/head_1.png", 
    )

image bfaq bfaq01 = LiveComposite(
    (1000, 720), 
    (0, 0), "bk4/asami/tits/body_1.png",
    (0, 0), "bk4/asami/tits/arms_holdjacket.png", 
    (0, 0), "bk4/asami/tits/head_1.png", 
    (0, 0), "bfaq_titshake", 
    )

image bfaq bfaq02 = LiveComposite(
    (1000, 720),    
    (0, 0), im.Flip("bk4/asami/tits/body_1.png", horizontal=True),
    (0, 0), im.Flip("bk4/asami/tits/arms_holdjacket.png",  horizontal=True),
    (-30, 0), "bk4/asami/tits/head_1.png",
    (0, 0), "bfaq_titshake_right", 
    )


image bfaq bfaq03:
    "bfaq bfaq01"
    0.7
    "bfaq bfaq02"
    0.7
    repeat

image bfaq bfaq04 = LiveComposite(
    (1000, 720), 
    (0, 0), "bk4/asami/tits/body_1.png",
    (0, 0), "bk4/asami/tits/arms_behindhead.png", 
    (0, 0), "bk4/asami/tits/tits1.png",  
    (0, 0), "bk4/asami/tits/head_1.png", 
    )

image bfaq bfaq05 = LiveComposite(
    (1000, 720), 
    (0, 0), "bk4/asami/tits/body_1.png",
    (0, 0), "bk4/asami/tits/arms_behindhead.png", 
    (0, 0), "bfaq_titsupdown",
    (0, 0), "bfaq_headhair",  
     
    )

image bfaq bfaq06 = LiveComposite(
    (1000, 720), 
    (0, 0), "bk4/asami/tits/body_1.png",
    (0, 0), "bk4/asami/tits/arms_holdjacket.png", 
    (0, 0), "bk4/asami/tits/head_1.png",  
    (0, 0), "bfaq_titsdown", 
    )

image bfaq bfaq07 = LiveComposite(
    (1000, 720), 
    (0, 0), "bk4/asami/tits/body_1.png",
    (0, 0), "bk4/asami/tits/arms_holdjacket.png", 
    (0, 0), "bk4/asami/tits/tits_covered.png",  
    (0, 0), "bk4/asami/tits/head_1.png", 
    )


image bfaq bfaq08 = LiveComposite(
    (1000, 720), 
    (0, 0), "bk4/asami/tits/asami_body.png",
    (0, 0), "bk4/asami/tits/asami_ani_1.png",
    (0, 0), "bk4/asami/tits/asami_eyesup.png",
    (0, 0), "bfaq_asami_blink",
    )

image bfaq bfaq09 = LiveComposite(
    (1000, 720), 
    (0, 0), "bk4/asami/tits/asami_body.png",
    (0, 0), "bfaq_titsuck_asami", 
    (350, 0), "bfaq_titsuck_tenzin",
    (0, 0), "bfaq_asami_blink",
    )

image bfaq bfaq09a:
    "bfaq bfaq09"
    xpos 500
    linear 0.6 xpos 520
    linear 0.2 xpos 500
    repeat


image bfaq bfaq10 = LiveComposite(
    (1000, 720), 
    (0, 0), "bk4/asami/tits/korra_body.png",
    (0, 0), "bk4/asami/tits/korra_ani_1.png", 
    (0, 0), "bk4/asami/tits/korra_eyesup.png", 
    )

image bfaq bfaq10a = LiveComposite(
    (1000, 720), 
    (0, 0), "bk4/asami/tits/korra_body.png",
    (0, 0), "bk4/asami/tits/korra_ani_1.png", 
    (0, 0), "bk4/asami/tits/korra_body_grin.png", 
    )

image bfaq bfaq11 = LiveComposite(
    (1000, 720), 
    (0, 0), "bk4/asami/tits/korra_body.png",
    (0, 0), "bfaq_titsuck_korra", 
    (350, 0), "bfaq_titsuck_tenzin",
    )




image bfaq bfaq11a:
    "bfaq bfaq11"
    xpos 500
    linear 0.2 xpos 500
    linear 0.4 xpos 520
    linear 0.2 xpos 500
    repeat

image bfaq bfaq12 = LiveComposite(
    (1000, 720), 
    (0, 0), "bk4/asami/tits/z_asamibody.png",
    (0, 0), "bk4/asami/tits/z_asamibody_tits.png",
    (0, 0), "bk4/asami/tits/z_korrabody.png",
    (0, 0), "bk4/asami/tits/z_korrabody_tits.png",
    )

image bfaq bfaq13 = LiveComposite(
    (1000, 720), 
    (-70, 0), "bk4/asami/tits/z_asamibody.png",
    (50, 0), "bk4/asami/tits/z_korrabody.png",
    (0, 0), "bk4/asami/tits/z_tits_ani1.png",
    )
image bfaq bfaq14 = LiveComposite(
    (1000, 720), 
    (-60, 0), "bk4/asami/tits/z_asamibody.png",
    (40, 0), "bk4/asami/tits/z_korrabody.png",
    (0, 0), "bk4/asami/tits/z_tits_ani2.png",
    )
image bfaq bfaq15 = LiveComposite(
    (1000, 720), 
    (-50, 0), "bk4/asami/tits/z_asamibody.png",
    (30, 0), "bk4/asami/tits/z_korrabody.png",
    (0, 0), "bk4/asami/tits/z_tits_ani3.png",
    )

image bfaq bfaq16:
    "bfaq bfaq13"
    0.2
    "bfaq bfaq14"
    0.2
    "bfaq bfaq15"
    0.2
    "bfaq bfaq14"
    0.2
    repeat

image bfaq bfaq17 = LiveComposite(
    (1000, 720), 
    (0, 0), "bk4/asami/tits/z_kiss.png",    
    (0, 0), "bk4/asami/tits/z_kisshead_kiss.png",  
    )

image bfaq bfaq18 = LiveComposite(
    (1000, 720), 
    (-130, 0), "bk4/asami/tits/z_asamibody.png",
    (-130, 0), "bk4/asami/tits/z_asamibody_tits.png",
    (-130, 0), "bk4/asami/tits/z_asami_lookleft.png",
    (130, 0), "bk4/asami/tits/z_korrabody.png",
    (130, 0), "bk4/asami/tits/z_korrabody_tits.png",
    (130, 0), "bk4/asami/tits/z_korra_lookright.png",
    )

image bfaq bfaq19 = LiveComposite(
    (1000, 720), 
    (0, 0), "bk4/asami/tits/z_kiss.png",    
    (0, 0), "bk4/asami/tits/z_kisshead_tongue.png",  
    (0, 0), "bfaq_tongue", 
    )

image bfaq bfaq20 = LiveComposite(
    (1000, 720), 
    (0, 0), "bk4/asami/tits/z_asamibody.png",
    (0, 0), "bk4/asami/tits/z_asamibody_tits.png",
    (0, 0), "bk4/asami/tits/z_asami_lookforward.png",
    (0, 0), "bk4/asami/tits/z_korrabody.png",
    (0, 0), "bk4/asami/tits/z_korrabody_tits.png",
    (0, 0), "bk4/asami/tits/z_korra_lookforward.png",
    )

image bfaq_tongue:
    "bk4/asami/tits/z_tongues1.png"
    0.2
    "bk4/asami/tits/z_tongues2.png"
    0.2
    "bk4/asami/tits/z_tongues3.png"
    0.2
    "bk4/asami/tits/z_tongues2.png"
    0.2
    repeat

image bfaq_asami_blink:
    "bk4/asami/tits/asami_blink.png"
    0.25
    "bk4/misc/minipixel.png"
    2.0
    "bk4/asami/tits/asami_blink.png"
    0.25
    "bk4/misc/minipixel.png"
    7.0
    "bk4/asami/tits/asami_blink.png"
    0.25
    "bk4/misc/minipixel.png"
    8.0
    repeat


image bfaq_titsuck_korra:
    "bk4/asami/tits/korra_ani_1.png"
    0.2
    "bk4/asami/tits/korra_ani_2.png"
    0.2
    "bk4/asami/tits/korra_ani_3.png"
    0.2
    "bk4/asami/tits/korra_ani_2.png"
    0.2
    repeat

image bfaq_titsuck_asami:
    "bk4/asami/tits/asami_ani_1.png"
    0.2
    "bk4/asami/tits/asami_ani_2.png"
    0.2
    "bk4/asami/tits/asami_ani_3.png"
    0.2
    "bk4/asami/tits/asami_ani_2.png"
    0.2
    repeat

image bfaq_titsuck_tenzin:
    "bk4/asami/tits/tenzin_1.png"
    0.2
    "bk4/asami/tits/tenzin_2.png"
    0.2
    "bk4/asami/tits/tenzin_3.png"
    0.2
    "bk4/asami/tits/tenzin_2.png"
    0.2
    repeat


image bfaq_headhair:
    "bk4/asami/tits/head_hairdown.png"
    0.2
    "bk4/asami/tits/head_hairdown1.png"
    0.3
    "bk4/asami/tits/head_1.png"
    0.5
    repeat

image bfaq_titsdown:
    "bk4/asami/tits/tits1.png"
    0.10
    "bk4/asami/tits/tits_down1.png"
    0.15
    "bk4/asami/tits/tits_down.png"
    0.15
    "bk4/asami/tits/tits_down1.png"
    0.15
    "bk4/asami/tits/tits1.png"
    0.2



image bfaq_titsupdown:
    "bk4/asami/tits/tits_down.png"
    0.15
    "bk4/asami/tits/tits_down1.png"
    0.15
    "bk4/asami/tits/tits1.png"
    0.2
    "bk4/asami/tits/tits_up1.png"
    0.15
    "bk4/asami/tits/tits_up.png"
    0.15
    "bk4/asami/tits/tits_up1.png"
    0.10
    "bk4/asami/tits/tits1.png"
    0.10
    repeat

image bfaq_titshake:
    "bk4/asami/tits/tits1.png"
    0.1
    "bk4/asami/tits/tits2.png"
    0.1
    "bk4/asami/tits/tits3.png"
    0.1
    "bk4/asami/tits/tits4.png"
    0.1
    "bk4/asami/tits/tits3.png"
    0.1
    "bk4/asami/tits/tits2.png"
    0.1
    "bk4/asami/tits/tits1.png"
    0.1

    repeat

image bfaq_titshake_right:
    xzoom -1.0
    "bk4/asami/tits/tits1.png"
    0.1
    "bk4/asami/tits/tits2.png"
    0.1
    "bk4/asami/tits/tits3.png"
    0.1
    "bk4/asami/tits/tits4.png"
    0.1
    "bk4/asami/tits/tits3.png"
    0.1
    "bk4/asami/tits/tits2.png"
    0.1
    "bk4/asami/tits/tits1.png"
    0.1

    repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
