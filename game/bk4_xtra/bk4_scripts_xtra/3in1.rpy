















image kg = "bk4/backgrounds/park_day_1.jpg"
init python:
    import time
    style.mcnn=Style(style.default)
    style.mcnn.set_parent(style.button)
    style.mcnn.color="#beddff"
    style.mcnn.size=70
    style.mcnn.outlines=[(2,"#6e6e6e",0,0)]
    def krib():
        global cl1,cl2,cl3,cl4,cl5,cl6,cl7,kricol,krix,krix0,pointka,ktmr,clp1,clp2,clp3,clp4,clp5,clp6,clp7
        for i in range(0,9):
            if cl1[i]>0:
                clzz=1
                if i<7:
                    if cl1[i]==cl1[i+1]==cl1[i+2]:
                        pointka+=(cl1[i]+cl1[i+1]+cl1[i+2])*2
                        if i<6 and cl1[i]==cl1[i+3]:
                            if i<5 and cl1[i]==cl1[i+4]:
                                pointka+=cl1[i+4]*4
                                ktmr+=4
                                cl1[i+4]=0
                            pointka+=cl1[i+3]*3
                            ktmr+=2
                            cl1[i+3]=0
                        clzz,cl1[i+1],cl1[i+2]=0,0,0
                if cl1[i]==cl2[i]==cl3[i]:
                    pointka+=(cl1[i]+cl2[i]+cl3[i])*2
                    if cl1[i]==cl4[i]:
                        if cl1[i]==cl5[i]:
                            pointka+=cl5[i]*4
                            ktmr+=4
                            cl5[i]=0
                        pointka+=cl4[i]*3
                        ktmr+=2
                        cl4[i]=0
                    clzz,cl2[i],cl3[i]=0,0,0
                if clzz==0:
                    cl1[i]=0
        renpy.pause(0.05)
        for i in range(0,9):
            if cl2[i]>0:
                clzz=1
                if i<7:
                    if cl2[i]==cl2[i+1]==cl2[i+2]:
                        pointka+=(cl2[i]+cl2[i+1]+cl2[i+2])*2
                        if i<6 and cl2[i]==cl2[i+3]:
                            if i<5 and cl2[i]==cl2[i+4]:
                                pointka+=cl2[i+4]*4
                                ktmr+=4
                                cl2[i+4]=0
                            pointka+=cl2[i+3]*3
                            ktmr+=2
                            cl2[i+3]=0
                        clzz,cl2[i+1],cl2[i+2]=0,0,0
                if cl2[i]==cl3[i]==cl4[i]:
                    pointka+=(cl2[i]+cl3[i]+cl4[i])*2
                    if cl2[i]==cl5[i]:
                        if cl2[i]==cl6[i]:
                            pointka+=cl6[i]*4
                            ktmr+=4
                            cl6[i]=0
                        pointka+=cl5[i]*3
                        ktmr+=2
                        cl5[i]=0
                    clzz,cl3[i],cl4[i]=0,0,0
                if clzz==0:
                    cl2[i]=0
        renpy.pause(0.05)
        for i in range(0,9):
            if cl3[i]>0:
                clzz=1
                if i<7:
                    if cl3[i]==cl3[i+1]==cl3[i+2]:
                        pointka=(cl3[i]+cl3[i+1]+cl3[i+2])*2
                        if i<6 and cl3[i]==cl3[i+3]:
                            if i<5 and cl3[i]==cl3[i+4]:
                                pointka+=cl3[i+4]*4
                                ktmr+=4
                                cl3[i+4]=0
                            pointka+=cl3[i+3]*3
                            ktmr+=2
                            cl3[i+3]=0
                        clzz,cl3[i+1],cl3[i+2]=0,0,0
                if cl3[i]==cl4[i]==cl5[i]:
                    pointka+=(cl3[i]+cl4[i]+cl5[i])*2
                    if cl3[i]==cl6[i]:
                        pointka+=cl6[i]*3
                        ktmr+=2
                        cl6[i]=0
                    clzz,cl4[i],cl5[i]=0,0,0
                if clzz==0:
                    cl3[i]=0
        renpy.pause(0.05)
        for i in range(0,9):
            if cl4[i]>0:
                clzz=1
                if i<7:
                    if cl4[i]==cl4[i+1]==cl4[i+2]:
                        pointka+=(cl4[i]+cl4[i+1]+cl4[i+2])*2
                        if i<6 and cl4[i]==cl4[i+3]:
                            if i<5 and cl4[i]==cl4[i+4]:
                                pointka+=cl4[i+4]*4
                                ktmr+=4
                                cl4[i+4]=0
                            pointka+=cl4[i+3]*3
                            ktmr+=2
                            cl4[i+3]=0
                        clzz,cl4[i+1],cl4[i+2]=0,0,0
                if cl4[i]==cl5[i]==cl6[i]:
                    pointka+=(cl4[i]+cl5[i]+cl6[i])*2
                    clzz,cl5[i],cl6[i]=0,0,0
                if clzz==0:
                    cl4[i]=0
        renpy.pause(0.05)
        for i in range(0,7):
            if cl5[i]>0:
                if cl5[i]==cl5[i+1]==cl5[i+2]:
                    pointka+=(cl5[i]+cl5[i+1]+cl5[i+2])*2
                    if i<6 and cl5[i]==cl5[i+3]:
                        if i<5 and cl5[i]==cl5[i+4]:
                            pointka+=cl5[i+4]*4
                            ktmr+=4
                            cl5[i+4]=0
                        pointka+=cl5[i+3]*3
                        ktmr+=2
                        cl5[i+3]=0
                    cl5[i],cl5[i+1],cl5[i+2]=0,0,0
        renpy.pause(0.05)
        for i in range(0,7):
            if cl6[i]>0:
                if cl6[i]==cl6[i+1]==cl6[i+2]:
                    pointka+=(cl6[i]+cl6[i+1]+cl6[i+2])*2
                    if i<6 and cl6[i]==cl6[i+3]:
                        if i<5 and cl6[i]==cl6[i+4]:
                            pointka+=cl6[i+4]*4
                            ktmr+=4
                            cl6[i+4]=0
                        pointka+=cl6[i+3]*3
                        ktmr+=2
                        cl6[i+3]=0
                    cl6[i],cl6[i+1],cl6[i+2]=0,0,0
        for i in range(0,9):
            if cl6[i]==0:
                clp5[i]-=32
                if cl5[i]>0:
                    cl6[i]=cl5[i]
                    cl5[i]=0
                elif cl4[i]>0:
                    cl6[i]=cl4[i]
                    cl4[i]=0
                elif cl3[i]>0:
                    cl6[i]=cl3[i]
                    cl3[i]=0
                elif cl2[i]>0:
                    cl6[i]=cl2[i]
                    cl2[i]=0
                elif cl1[i]>0:
                    cl6[i]=cl1[i]
                    cl1[i]=0
                else:
                    cl6[i]=renpy.random.randint(1,6)
                for q in range(4):
                    clp5[i]+=8
                    renpy.pause(.0000001)
                ktmr+=0.1
        for i in range(0,9):
            if cl5[i]==0:
                clp5[i]-=32
                if cl4[i]>0:
                    cl5[i]=cl4[i]
                    cl4[i]=0
                elif cl3[i]>0:
                    cl5[i]=cl3[i]
                    cl3[i]=0
                elif cl2[i]>0:
                    cl5[i]=cl2[i]
                    cl2[i]=0
                elif cl1[i]>0:
                    cl5[i]=cl1[i]
                    cl1[i]=0
                else:
                    cl5[i]=renpy.random.randint(1,6)
                for q in range(4):
                    clp5[i]+=8
                    renpy.pause(.0000001)
                ktmr+=0.1
        for i in range(0,9):
            if cl4[i]==0:
                clp4[i]-=32
                if cl3[i]>0:
                    cl4[i]=cl3[i]
                    cl3[i]=0
                elif cl2[i]>0:
                    cl4[i]=cl2[i]
                    cl2[i]=0
                elif cl1[i]>0:
                    cl4[i]=cl1[i]
                    cl1[i]=0
                else:
                    cl4[i]=renpy.random.randint(1,6)
                for q in range(4):
                    clp4[i]+=8
                    renpy.pause(.0000001)
                ktmr+=0.1
        for i in range(0,9):
            if cl3[i]==0:
                clp3[i]-=32
                if cl2[i]>0:
                    cl3[i]=cl2[i]
                    cl2[i]=0
                elif cl1[i]>0:
                    cl3[i]=cl1[i]
                    cl1[i]=0
                else:
                    cl3[i]=renpy.random.randint(1,6)
                for q in range(4):
                    clp3[i]+=8
                    renpy.pause(.0000001)
                ktmr+=0.1
        for i in range(0,9):
            if cl2[i]==0:
                clp2[i]-=32
                if cl1[i]>0:
                    cl2[i]=cl1[i]
                    cl1[i]=0
                else:
                    cl2[i]=renpy.random.randint(1,6)
                for q in range(4):
                    clp2[i]+=8
                    renpy.pause(.0000001)
                ktmr+=0.1
        for i in range(0,9):
            if cl1[i]==0:
                clp1[i]-=32
                cl1[i]=renpy.random.randint(1,6)
                for w in range(4):
                    clp1[i]+=8
                    renpy.pause(.0000001)
                ktmr+=0.1
        return
screen krix:
    text "[pointk]" style "mcnn"
    text str(int(ktmr)) style "mcnn" xalign .99
    timer 1 repeat True action If(ktmr>0,true=SetVariable('ktmr',ktmr-1),false=Return())
    for z in range(1,7):
        for i in range(0,9):
            imagebutton idle ("bk4_xtra/3in1/k"+str(globals()["cl"+str(z)][i])+".png") xpos (i*80+260) ypos (z*80+20) action [SetVariable('krix',i),SetVariable('kriy',z),ui.callsinnewcontext("krich")]

    textbutton "I give up!" style "mcnn" xalign 0.5 yalign 0.9 action [SetVariable('ktmr',1)]

    if temp_int < 2:

        textbutton "Try again" style "mcnn" xalign 0.8 yalign 0.9 action [SetVariable('pointka',0), 

            SetVariable('temp_int', temp_int+1),  Jump("krix")]


screen krixx:
    text "[pointk]" style "mcnn"
    text str(int(ktmr)) style "mcnn" xalign .99
    timer 1 repeat True action If(ktmr>0,true=SetVariable('ktmr',ktmr-1),false=Return())
    for z in range(1,7):
        for i in range(0,9):
            add ("bk4_xtra/3in1/k"+str(globals()["cl"+str(z)][i])+".png") xpos (i*80+260) ypos (z*80+20+globals()["clp"+str(z)][i])
label krich:
    show screen krixx
    if krix>=0:
        if krix in(krix0+1,krix0-1)and kriy==kriy0:
            pass
        elif kriy in(kriy0+1,kriy0-1)and krix==krix0:
            pass
        else:
            jump krich3
        if krix0>=0:
            $ krixxx=globals()["cl"+str(kriy)][krix]
            $ globals()["cl"+str(kriy)][krix]=globals()["cl"+str(kriy0)][krix0]
            $ globals()["cl"+str(kriy0)][krix0]=krixxx
            label krich2:
                $ krib()
                if pointka>0:
                    $ pointloop+=1
                    $ pointk+=pointka
                    $ pointka=0
                    jump krich2
                if pointloop==0:
                    $ krixxx=globals()["cl"+str(kriy0)][krix0]
                    $ globals()["cl"+str(kriy0)][krix0]=globals()["cl"+str(kriy)][krix]
                    $ globals()["cl"+str(kriy)][krix]=krixxx
                $ pointloop=0
                $ krix=-1
                $ krix0=-1
        else:
            label krich3:
                $ krix0=krix
                $ kriy0=kriy
    return
label krix:
    scene kg:
        ypos 0
    python:
        cl0,cl1,cl2,cl3,cl4,cl5,cl6,cl7,krix,kriy,kris,krin,kriw,krie,kricol,krix,krix0,kriy,kriy0,pointk,pointloop,ktmr,pointka=[],[],[],[],[],[],[],[],0,0,0,0,0,0,0,-1,-1,-1,-1,0,0,60,0
        for z in range(1,7):
            for i in range(0,9):
                globals()["cl"+str(z)].append(renpy.random.randint(1,6))
        clp0,clp1,clp2,clp3,clp4,clp5,clp6,clp7=[],[],[],[],[],[],[],[]
        for z in range(1,7):
            for i in range(0,9):
                globals()["clp"+str(z)].append(0)
    call screen krix
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
