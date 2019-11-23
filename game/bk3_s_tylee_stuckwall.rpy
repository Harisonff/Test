






image tosw tosw01 = LiveComposite(
    (1000, 720),    
    (450, 0), "bk3/tylee/stuckwall/head1.png",
    (450, 0), "tosw_blink",    
    )

image tosw tosw02 = LiveComposite(
    (1000, 720),    
    (450, 0), "bk3/tylee/stuckwall/head1.png",
    (450, 0), "bk3/tylee/stuckwall/dick1.png",
    (450, 0), "tosw_blink",
    )

image tosw tosw02_1 = LiveComposite(
    (1000, 720),    
    (450, 0), "bk3/tylee/stuckwall/head1.png",
    (450, 0), "tosw_ashamed",
    (450, 0), "bk3/tylee/stuckwall/dick1.png",
    (450, 0), "tosw_blink",
    )

image tosw tosw03 = LiveComposite(
    (1000, 720),    
    (450, 0), "bk3/tylee/stuckwall/head1.png",
    (-5, -22), "bk3/tylee/stuckwall/openspermmouth.png",
    (450, 0), "tosw_blink",
    )

image tosw tosw04 = LiveComposite(
    (1000, 720),    
    (450, 0), "bk3/tylee/stuckwall/head1.png",
    (-5, -22), "bk3/tylee/stuckwall/openmouth.png",
    (470, 100), "bk3/tylee/stuckwall/dick1.png",
    (450, 0), "tosw_blink",
    )

image tosw tosw05 = LiveComposite(
    (1000, 720),    
    (450, 0), "bk3/tylee/stuckwall/head1.png",
    (450, 0), "bk3/tylee/stuckwall/dicksuck1.png",
    )
image tosw tosw06 = LiveComposite(
    (1000, 720),    
    (450, 0), "bk3/tylee/stuckwall/head2.png",
    (450, 0), "bk3/tylee/stuckwall/dicksuck2.png",
    )
image tosw tosw07 = LiveComposite(
    (1000, 720),    
    (450, 0), "bk3/tylee/stuckwall/head3.png",
    (450, 0), "bk3/tylee/stuckwall/dicksuck3.png",
    )
image tosw tosw08 = LiveComposite(
    (1000, 720),    
    (450, 0), "bk3/tylee/stuckwall/head4.png",
    (450, 0), "bk3/tylee/stuckwall/dicksuck4.png",
    )

image tosw tosw09 = LiveComposite(
    (1000, 720),    
    (450, 0), "bk3/tylee/stuckwall/head1.png",
    (0, 0), "bk3/tylee/stuckwall/hands2.png",
    (450, 0), "bk3/tylee/stuckwall/dicksuck1.png",
    )
image tosw tosw10 = LiveComposite(
    (1000, 720),    
    (450, 0), "bk3/tylee/stuckwall/head2.png",
    (0, 30), "bk3/tylee/stuckwall/hands2.png",
    (450, 0), "bk3/tylee/stuckwall/dicksuck2.png",
    )
image tosw tosw11 = LiveComposite(
    (1000, 720),    
    (450, 0), "bk3/tylee/stuckwall/head3.png",
    (20, 90), "bk3/tylee/stuckwall/hands2.png",
    (450, 0), "bk3/tylee/stuckwall/dicksuck3.png",
    )
image tosw tosw12 = LiveComposite(
    (1000, 720),    
    (450, 0), "bk3/tylee/stuckwall/head4.png",
    (30, 130), "bk3/tylee/stuckwall/hands2.png",
    (450, 0), "bk3/tylee/stuckwall/dicksuck4.png",
    )



image tosw_surprise:
    "bk3/tylee/stuckwall/face_surprise.png"
    xpos 610 ypos 575
image tosw_ashamed:
    "bk3/tylee/stuckwall/face_ashamed.png"
    xpos 610 ypos 575
image tosw_lookdown:
    "bk3/tylee/stuckwall/face_lookdown.png"
    xpos 610 ypos 575






image tosw tosw100:
    "tosw tosw05"
    0.3
    "tosw tosw06"
    0.3
    "tosw tosw07"
    0.3
    "tosw tosw08"
    0.3
    "tosw tosw07"
    0.3
    "tosw tosw06"
    0.3
    repeat

image tosw tosw101:
    "tosw tosw05"
    0.3
    "tosw tosw08"
    0.3
    "tosw tosw07"
    0.3
    "tosw tosw06"
    0.3
    repeat

image tosw tosw102:

    "tosw tosw12" with vpunch
    1.3
    "tosw tosw11"
    0.2
    "tosw tosw10"
    0.2


    repeat

image tosw_blink:
    "transparent.png"
    2
    "bk3/tylee/stuckwall/blink.png"
    0.3
    "transparent.png"
    6
    "bk3/tylee/stuckwall/blink.png"
    0.3
    "transparent.png"
    4
    "bk3/tylee/stuckwall/blink.png"
    0.3
    repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
