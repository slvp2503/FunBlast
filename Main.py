import pygame
import time
pygame.init()
from pygame import mixer
#From here -----
import sys
import os
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
#To Here , so that the EXE function runs clearly -----
window = pygame.display.set_mode((999, 625))
pygame.display.set_caption(" Fun Blast - Vara1803 ")
Gokuui = pygame.image.load(resource_path('Goku UI.png'))
Gokublue = pygame.image.load(resource_path('Goku Blue.png'))
VegetaBlue = pygame.image.load(resource_path("Vegeta Blue.png"))
VegetaUg = pygame.image.load(resource_path('Vegeta UG.png'))
Ichigo = pygame.image.load(resource_path("VEG.png"))
ubg = pygame.image.load(resource_path('ubg.png'))
bg=pygame.transform.scale(ubg,(999,625))
Ki = pygame.image.load(resource_path("Ki Blast.png"))
Explosion = pygame.image.load(resource_path("Explosion.png"))
mixer.music.load(resource_path("Viper-Sue.wav"))
mixer.music.play(-1)
text1 = "Instructions : First to reach 25 points WINS , ALL THE BEST !"
text2="P1: Arrows move, Numpad 5/1/2/3 attack (direction change mid-blast), 4 transform."
text3="P2: WASD move, IJKL attack (direction change mid-blast), U transform. "
text4="Unlock epic transformations with Goku and Vegeta! Player 1 press 4, Player 2 press U."
text5="With Goku and Vegeta Become invincible for 10 seconds, then 10 seconds cooldown!"

px = 250
py = 400
speedx = 0
speedy = 0
ex = 250
ey = 200
speedex = 0
speedey = 0
speedatk = 10 
kiblasts = []
explosions =[]
firetime = 0
cooldown = 500
gtstime = 0
gtscooldown = 10000
gtsduration = 10000
gtsactive = False
pgtstime = 0
pgtscooldown = 10000
pgtsduration = 10000
pgtsactive = False
efiretime = 0
ecooldown = 500
a1x = 0
a1y = 0
a2x = 0
a2y = 0
scorep = 0
escorep = 0
execollision = False
kh1 = "none"
kh2 = "none"
ch = "Not choosed"
ech = "Not choosed"
chr = None
echr = None
font = pygame.font.Font('freesansbold.ttf',32)
font1 = pygame.font.Font('freesansbold.ttf',21)
def choosechr():
    if(ch=="Not choosed"):
        chrs = font.render("PLAYER 1 : CHOOSE YOUR CHARACTER",True,(255,255,255))
        window.blit(chrs,(250,0))
def choosingchr ():
    if(ch=="Not choosed"):
        window.blit(Gokublue,(200,150))
        cgoku= font.render("1",True,(255,255,255))
        window.blit(cgoku,(200,200))
        window.blit(VegetaBlue,(300,150))
        cvegeta=font.render("2",True,(255,255,255))
        window.blit(cvegeta,(300,200))
        window.blit(Ichigo,(400,150))
        cichigo=font.render("3",True,(255,255,255))
        window.blit(cichigo,(400,200))
        Instructions1=font1.render(text1,True,(255,255,255))
        window.blit(Instructions1,(0,300))
        Instructions2=font1.render(text2,True,(255,255,255))
        window.blit(Instructions2,(0,325))
        Instructions3=font1.render(text3,True,(255,255,255))
        window.blit(Instructions3,(0,350))
        Instructions4=font1.render(text4,True,(255,255,255))
        window.blit(Instructions4,(0,375))
        Instructions5=font1.render(text5,True,(255,255,255))
        window.blit(Instructions5,(0,400))
def echoosechr():
    if(ech=="Not choosed" and ch=="choosed"):
        chrs = font.render("PLAYER 2 : CHOOSE YOUR CHARACTER",True,(255,255,255))
        window.blit(chrs,(250,0))
def echoosingchr ():
    if(ech=="Not choosed" and ch=="choosed"):
        window.blit(Gokublue,(200,150))
        cgoku= font.render("A",True,(255,255,255))
        window.blit(cgoku,(200,200))
        window.blit(VegetaBlue,(300,150))
        cvegeta=font.render("S",True,(255,255,255))
        window.blit(cvegeta,(300,200))
        window.blit(Ichigo,(400,150))
        cichigo=font.render("D",True,(255,255,255))
        window.blit(cichigo,(400,200))        
def showscorep(i,j):
    if(ech=="choosed" and ch=="choosed"):
        score = font.render("Player 1 Score : " + str(scorep) , True , (255,255,255))
        window.blit(score,(i,j))
def showscoree(i,j):
    if(ech=="choosed" and ch=="choosed"):
        score = font.render("Player 2 Score : " + str(escorep) , True , (255,255,255))
        window.blit(score,(i,j))    
def player(a):
    window.blit(a, (px, py))
kcollision=False
def enemy(a):
    window.blit(a, (ex, ey))
def kicollision (a,b,c,d):
    global scorep
    global kcollision
    distance = ((((a+12)-c)**2) + ((b+15-d)**2))**0.5
    if not pgtsactive:
        if distance <=23:
            kcollision = True
            scorep+=1 
        else:
            kcollision = False
    else:
            kcollision = False
def excollision (a,b,c,d):
    global escorep
    global execollision
    distance = ((((a+12)-c)**2) + ((b+15-d)**2))**0.5
    if not gtsactive:
        if distance <=23:
            execollision = True
            escorep+=1 
        else:
            execollision = False 
    else:
            execollision = False                                    
def kiatk():
    if ech=="choosed":
        for blasts in kiblasts[:]:
            if(kh1=="2"):
                blasts[1] += speedatk
            elif(kh1=="5"):
                blasts[1] -= speedatk  
            elif(kh1=="1"):
                blasts[0] -= speedatk
            elif(kh1=="3"):
                blasts[0] += speedatk
            window.blit(Ki, (blasts[0], blasts[1]))         
            kicollision (ex,ey,blasts[0],blasts[1])            
            if kcollision:
                kiblasts.remove(blasts)
            elif blasts[1] <= 0 or blasts[1] >= 625 or blasts[0] <= 0 or blasts[0] >= 999 :
                kiblasts.remove(blasts)
def expatk():
    if ech=="choosed":
        for exps in explosions[:]:
            if(kh2=="k"):
                exps[1] += speedatk
            elif(kh2=="i"):
                exps[1] -= speedatk  
            elif(kh2=="j"):
                exps[0] -= speedatk
            elif(kh2=="l"):
                exps[0] += speedatk
            window.blit(Explosion, (exps[0], exps[1]))
            excollision (px,py,exps[0],exps[1])
            if execollision:
                explosions.remove(exps)
            elif exps[1] >= 625 or exps[1]<=0 or exps[0]<=0 or exps[0]>999:
                explosions.remove(exps) 
def Vegetatransformation(a,b,c,d,e,f,g,h):
    if(a==h or a ==f):
        if keys[g] and not b and c - d >= e:
            a = f
            b = True
            d = c

        if b and c - d >= e:
            a = h
            b = False
            d = c 
    return a,b,d 
def winner(a,b):
    if(a>=25 or b>=25):
        window.fill((0,0,0))
        if(a>=25):
            win="Player 1 " 

        elif(b>=25):
            win="Player 2 "
        winscreen=font.render(f"{win} has won!" , True, (255,255,255))
        window.blit(winscreen,(375,250))            
                        
                                       
run = True
while run:
    clock = pygame.time.Clock()
    window.fill((0, 255, 0))
    window.blit(bg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False              

    keys = pygame.key.get_pressed()

    if keys[pygame.K_KP1]:
        kh1="1"
        currenttime = pygame.time.get_ticks()
        if currenttime - firetime >= cooldown:
            a1x = px
            a1y = py
            kiblasts.append([a1x, a1y])
            firetime = currenttime
    if keys[pygame.K_KP2]:
        kh1="2"
        currenttime = pygame.time.get_ticks()
        if currenttime - firetime >= cooldown:
            a1x = px
            a1y = py
            kiblasts.append([a1x, a1y])
            firetime = currenttime
    if keys[pygame.K_KP3]:
        kh1="3"
        currenttime = pygame.time.get_ticks()
        if currenttime - firetime >= cooldown:
            a1x = px
            a1y = py
            kiblasts.append([a1x, a1y])
            firetime = currenttime
    if keys[pygame.K_KP5]:
        kh1="5"
        currenttime = pygame.time.get_ticks()
        if currenttime - firetime >= cooldown:
            a1x = px
            a1y = py
            kiblasts.append([a1x, a1y])
            firetime = currenttime                                

    if keys[pygame.K_j]:
        kh2="j"
        ecurrenttime = pygame.time.get_ticks()
        if ecurrenttime - efiretime >= ecooldown:
            a2x = ex
            a2y = ey
            explosions.append([a2x, a2y])
            efiretime = ecurrenttime
    if keys[pygame.K_k]:
        kh2="k"
        ecurrenttime = pygame.time.get_ticks()
        if ecurrenttime - efiretime >= ecooldown:
            a2x = ex
            a2y = ey
            explosions.append([a2x, a2y])
            efiretime = ecurrenttime
    if keys[pygame.K_l]:
        kh2="l"
        ecurrenttime = pygame.time.get_ticks()
        if ecurrenttime - efiretime >= ecooldown:
            a2x = ex
            a2y = ey
            explosions.append([a2x, a2y])
            efiretime = ecurrenttime  
    if keys[pygame.K_i]:
        kh2="i"
        ecurrenttime = pygame.time.get_ticks()
        if ecurrenttime - efiretime >= ecooldown:
            a2x = ex
            a2y = ey
            explosions.append([a2x, a2y])
            efiretime = ecurrenttime                                              
    if (ch=="Not choosed"):
        if keys[pygame.K_KP1]:
            chr=Gokublue
            ch="choosed"
        if keys[pygame.K_KP2]:
            chr=VegetaBlue  
            ch="choosed"
        if keys[pygame.K_KP3]:
            chr=Ichigo
            ch="choosed"
    if (ch=="choosed"):  
        if (ech=="Not choosed"):
            if keys[pygame.K_a]:
                echr=Gokublue
                ech="choosed"
            if keys[pygame.K_s]:
                echr=VegetaBlue  
                ech="choosed"
            if keys[pygame.K_d]:
                echr=Ichigo
                ech="choosed"                                         

    if keys[pygame.K_LEFT]:
        speedx = -5
    elif keys[pygame.K_RIGHT]:
        speedx = 5
    else:
        speedx = 0

    if keys[pygame.K_UP]:
        speedy = -5
    elif keys[pygame.K_DOWN]:
        speedy = 5
    else:
        speedy = 0

    if keys[pygame.K_a]:
        speedex = -5
    elif keys[pygame.K_d]:
        speedex = 5
    else:
        speedex = 0

    if keys[pygame.K_w]:
        speedey = -5
    elif keys[pygame.K_s]:
        speedey = 5
    else:
        speedey = 0

    ecurrent_time = pygame.time.get_ticks()
    pcurrent_time = pygame.time.get_ticks()
    if(chr==Gokublue or chr ==Gokuui):
        if keys[pygame.K_KP4] and not gtsactive and ecurrent_time - gtstime >= gtscooldown:
            chr = Gokuui 
            gtsactive = True
            gtstime = ecurrent_time

        if gtsactive and ecurrent_time - gtstime >= gtsduration:
            chr = Gokublue
            gtsactive = False
            gtstime = ecurrent_time
    if(echr==Gokublue or echr ==Gokuui):
        if keys[pygame.K_u] and not pgtsactive and pcurrent_time - pgtstime >= pgtscooldown:
            echr = Gokuui 
            pgtsactive = True
            pgtstime = pcurrent_time

        if pgtsactive and pcurrent_time - pgtstime >= pgtsduration:
            echr = Gokublue
            pgtsactive = False
            pgtstime = pcurrent_time
    if chr==Ichigo :
        khush= pygame.image.load(resource_path("Heart.png"))
        Ki=khush
    if echr==Ichigo :
        khush= pygame.image.load(resource_path("Heart.png"))
        Explosion=khush        

           
    px += speedx
    py += speedy
    ex += speedex
    ey += speedey

    if px >= 950:
        px = 950
    if py >= 550:
        py = 550
    if px <= 0:
        px = 0
    if py <= 0:
        py = 0
    if ex >= 950:
        ex = 950
    if ey >= 550:
        ey = 550
    if ex <= 0:
        ex = 0
    if ey <= 0:
        ey = 0
    echr,pgtsactive,pgtstime=Vegetatransformation(echr,pgtsactive,pcurrent_time,pgtstime,pgtscooldown,VegetaUg,pygame.K_u,VegetaBlue)
    chr,gtsactive,gtstime=Vegetatransformation(chr,gtsactive,ecurrent_time,gtstime,gtscooldown,VegetaUg,pygame.K_KP4,VegetaBlue)    

    kiatk()
    expatk() 
    choosechr()
    choosingchr()
    echoosechr()
    echoosingchr()                                                    

    if (ch=="choosed" and ech=="choosed"):
        enemy(echr)
        player(chr)

    showscorep(10,590)
    showscoree(0,0)
    winner(scorep,escorep)

    if scorep>=25:
        escorep=0
    if escorep>=25: 
        scorep=0

    pygame.display.update()
    clock.tick(90)