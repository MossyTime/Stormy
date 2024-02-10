import sys
import pygame
import random
import math

pygame.mixer.init()
pygame.mixer_music.load("data/tittle_music.mp3")
pygame.mixer_music.play(-1)
boss_flyby_sound=pygame.mixer.Sound("data/boss_flyby.mp3")
explosion_sound=pygame.mixer.Sound("data/explosion_sound.mp3")
laser_sound=pygame.mixer.Sound("data/laser_sound.mp3")
roar_sound=pygame.mixer.Sound("data/roar_sound.mp3")
rotation_sound=pygame.mixer.Sound("data/rotation_sound.mp3")
wind_sound=pygame.mixer.Sound("data/wind_sound.mp3")
dash_sound=pygame.mixer.Sound("data/dash_sound.mp3")
dash_warn_sound=pygame.mixer.Sound("data/dash_warn_sound.mp3")
rotation_warn_sound=pygame.mixer.Sound("data/rotation_warn_sound.mp3")


def rotate(surface, angle, pivot, offset):

    rotated_image = pygame.transform.rotozoom(surface, -angle, 1)
    rotated_offset = offset.rotate(angle)

    rect = rotated_image.get_rect(center=pivot+rotated_offset)
    return rotated_image, rect

pygame.init()

pygame.display.set_caption("Stormy")
screen=pygame.display.set_mode((1500,700))
clock=pygame.time.Clock()

bg=pygame.image.load("data/phase1_background.png")
bg=pygame.transform.scale(bg,(1500,700))

tittle_screen=pygame.image.load("data/tittle_screen.png")
tittle_screen=pygame.transform.scale(tittle_screen,(1500,700))

retry_screen=pygame.image.load("data/retry_screen.png")
retry_screen=pygame.transform.scale(retry_screen,(1500,700))

my_font=pygame.font.SysFont('malgungothic', 500,False,True)

text_tittle=my_font.render("Stormy", False, (255, 150, 50))
text_tittle=pygame.transform.scale(text_tittle,(600,200))

text_tittle_prep=my_font.render("I present", False, (255, 150, 50))
text_tittle_prep=pygame.transform.scale(text_tittle_prep,(600,200))

text_tittle_shadow=my_font.render("Stormy", False, (0, 0, 0))
text_tittle_shadow=pygame.transform.scale(text_tittle_shadow,(600,200))\

text_retry=my_font.render("Never Give Up", False, (255, 0, 100))
text_retry=pygame.transform.scale(text_retry,(600,200))

text_retry_shadow=my_font.render("Never Give Up", False, (0, 0, 0))
text_retry_shadow=pygame.transform.scale(text_retry_shadow,(600,200))

text_retry_button=my_font.render("Retry", False, (100, 0, 255))
text_retry_button=pygame.transform.scale(text_retry_button,(300,150))

player=pygame.image.load("data/sun.png")
player=pygame.transform.scale(player,(100,100))

laser=pygame.image.load("data/laser_beam.png")
laser=pygame.transform.scale(laser,(1600,70))

lightning=pygame.image.load("data/lightning.png")

wall_v=pygame.transform.scale(lightning,(50,700))
wall_h=pygame.transform.scale(lightning,(1500,50))

teleport=pygame.transform.scale(lightning,(300,50))

ball=pygame.image.load("data/ball.png")
ball=pygame.transform.scale(ball,(150,150))

ball_boss=pygame.image.load("data/ball_boss.png")
ball_boss=pygame.transform.scale(ball_boss,(400,400))

roar_lines=pygame.image.load("data/roar_lines.png")
roar_lines=pygame.transform.scale(roar_lines,(1500,700))

boss=pygame.image.load("data/boss.png")
boss=pygame.transform.scale(boss,(300,200))

logo_boss=pygame.image.load("data/boss.png")

dash_trail=pygame.image.load("data/dash_trail.png")
dash_trail=pygame.transform.scale(dash_trail,(500,200))


player_pos=[100,300]
player_movement=[0,0,0,0]

tittle=True

clicked=False

boss_music_flag=True

retry_music_flag=True

tittle_music_flag=True

retry=False

entrance=True

entrance_sounds=True

roar_flag=True

victory=False

attack_chose=True

hp=20000

tittle_prep=0

tittle_prep_flag=True

boss_prep=True

boss_prep_flag=True

choise_flag=True

dash_col=pygame.rect.Rect(0,0,0,0)

collision_up=pygame.rect.Rect(0,0,1500,1)
collision_down=pygame.rect.Rect(0,700,1500,1)
collision_left=pygame.rect.Rect(0,0,1,700)
collision_right=pygame.rect.Rect(1450,0,1,700)

retry_button=pygame.rect.Rect(600,500,300,150)

col_boss=pygame.rect.Rect(0,0,0,0)

black_screen=pygame.rect.Rect(0,0,1500,700)

while True:
    while tittle:

        while tittle_prep>=0 and tittle_prep<480:

            if tittle_prep_flag:
                tittle_n=0
                tittle_text_n=-200
                text_tittle_prep.set_alpha(tittle_n)
                tittle_prep_flag=False

            screen.fill((0,0,0))

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            if tittle_prep>=0 and tittle_prep<90:
                text_tittle_prep.set_alpha(tittle_n)
                screen.blit(text_tittle_prep,(450,250))

                tittle_n+=2.83

            if tittle_prep>=90 and tittle_prep<270:
                screen.blit(text_tittle_prep,(450,250))

            if tittle_prep>=270 and tittle_prep<360:
                text_tittle_prep.set_alpha(tittle_n)
                screen.blit(text_tittle_prep,(450,250))

                tittle_n-=2.83

            if tittle_prep>=360 and tittle_prep<480:
                tittle_screen.set_alpha(tittle_n)

                screen.blit(tittle_screen,(0,0))

                screen.blit(ball_boss,(350,tittle_text_n-150))
                screen.blit(logo_boss,(450,tittle_text_n))

                screen.blit(text_tittle_shadow,(455,tittle_text_n+5))
                screen.blit(text_tittle,(450,tittle_text_n))

                tittle_n+=2.83
                tittle_text_n+=3

            tittle_prep+=1
            pygame.display.update()
            clock.tick(60)                

        screen.fill((0,0,0))
        screen.blit(tittle_screen,(0,0)) 
        screen.blit(ball_boss,(350,0))
        screen.blit(logo_boss,(450,150))
        screen.blit(text_tittle_shadow,(455,155))
        screen.blit(text_tittle,(450,150))
        
        text_play=my_font.render("Ready?", False, (0, 0, 0))
        text_play=pygame.transform.scale(text_play,(300,150))
        start_button=pygame.rect.Rect(600,500,300,150) 
        start_button_shadow=pygame.rect.Rect(595,495,310,160)
        pygame.draw.rect(screen,(255,255,0),start_button)

        screen.blit(text_play,(600,490))

        mouse_pos=pygame.mouse.get_pos()
        if pygame.rect.Rect.collidepoint(start_button,mouse_pos):
            pygame.draw.rect(screen,(255,255,255),start_button_shadow)
            pygame.draw.rect(screen,(100,255,0),start_button)
            text_play=my_font.render("Ready?", False, (255, 255, 255))
            text_play=pygame.transform.scale(text_play,(300,150))
            screen.blit(text_play,(600,490))

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.MOUSEBUTTONUP:
                mouse_pos=pygame.mouse.get_pos()
                if pygame.rect.Rect.collidepoint(start_button,mouse_pos):
                    pygame.mixer_music.stop()
                    tittle=False
        
        pygame.display.flip() 
        pygame.display.update()
        clock.tick(60)     
    #end of tittle
        
    while retry:

        if retry_music_flag:

            pygame.mixer_music.stop()
            pygame.mixer_music.load("data/retry_music.mp3")
            pygame.mixer.music.play(-1)
            retry_music_flag=False

        screen.fill((0,0,0))
        screen.blit(retry_screen,(0,0)) 

        player_pos=[700,600]
        player_movement=[0,0,0,0]

        screen.blit(text_retry_shadow,(455,155))
        screen.blit(text_retry,(450,150))

        pygame.draw.rect(screen,(255,100,0),retry_button)

        mouse_pos=pygame.mouse.get_pos()
        if pygame.rect.Rect.collidepoint(retry_button,mouse_pos):
            pygame.draw.rect(screen,(0,255,255),retry_button)

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.MOUSEBUTTONUP:
                mouse_pos=pygame.mouse.get_pos()
                if pygame.rect.Rect.collidepoint(retry_button,mouse_pos):
                    pygame.mixer_music.stop()

                    retry=False

                    retry_music_flag=True

                    player_pos=[100,300]
                    player_movement=[0,0,0,0]

                    tittle=True

                    clicked=False

                    boss_music_flag=True

                    retry_music_flag=True

                    retry=False

                    entrance=True

                    entrance_sounds=True

                    roar_flag=True

                    victory=False

                    attack_chose=True

                    boss_prep=True

                    hp=20000

                    boss_prep_flag=True

                    choise_flag=True

                    collision_up=pygame.rect.Rect(0,0,1500,1)
                    collision_down=pygame.rect.Rect(0,700,1500,1)
                    collision_left=pygame.rect.Rect(0,0,1,700)
                    collision_right=pygame.rect.Rect(1450,0,1,700)

                    retry_button=pygame.rect.Rect(600,500,300,150)

                    col_boss=pygame.rect.Rect(0,0,0,0)

                    dash_col=pygame.rect.Rect(0,0,0,0)

                    

        screen.blit(text_retry_button,(600,490))

        pygame.display.flip() 
        pygame.display.update()
        clock.tick(60)
    #end of retry
        
    if hp<=0:
        victory=True

    if boss_music_flag:

        pygame.mixer_music.load("data/phase1_music.mp3")
        pygame.mixer_music.set_volume(0.5)
        pygame.mixer_music.play(-1)
        boss_music_flag=False

    while boss_prep:
        le_time=int(pygame.time.get_ticks()/1000)

        if boss_prep_flag:
            boss_prep_n=0
            boss_prep_time=0
            boss_flyby_sound_flag=True
            boss_prep_flag=False

        screen.fill((0,0,0))
        screen.blit(bg,(0,0)) 
        screen.blit(player,player_pos)

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()

        if boss_prep_time==60:
            boss_prep_n=0

        if boss_prep_time>=60 and boss_prep_time<180:
            if boss_flyby_sound_flag:
                pygame.mixer.Sound.play(boss_flyby_sound)
                boss_flyby_sound_flag=False

            screen.blit(boss,(-300+(boss_prep_n*1.8),700-boss_prep_n))

        if boss_prep_time==180:
            boss_prep_n=0
            boss_flyby_sound_flag=True

        if boss_prep_time>=180 and boss_prep_time<300:

            if boss_flyby_sound_flag:
                pygame.mixer.Sound.play(boss_flyby_sound)
                boss_flyby_sound_flag=False
            screen.blit(boss,(1500-(boss_prep_n*1.8),700-boss_prep_n))

        if boss_prep_time==300:
            boss_rot_of=900
            boss_rot_angle=90

        if boss_prep_time>=360 and boss_prep_time<540:
            of=pygame.math.Vector2(boss_rot_of,0)
            rot_boss,rect=rotate(boss,boss_rot_angle,(600,300),of)
            screen.blit(boss,(rect[0]+50,rect[1]+50))

            boss_rot_angle+=10

            if boss_rot_of>0:
                boss_rot_of-=5
            elif boss_rot_of<=0:
                boss_rot_of=0


        boss_prep_n+=40
        if boss_prep_time>=540 and boss_prep_time<660:

            if roar_flag:
                pygame.mixer.Sound.play(roar_sound)
                roar_flag=False

            screen.blit(boss,(550,250))
            screen.blit(roar_lines,(0,0))

            if boss_prep_time%2==0:
                pygame.draw.rect(screen,(0,0,0),black_screen)

        if boss_prep_time>=780:
            boss_prep=False

        boss_prep_time+=1

        pygame.display.update()
        clock.tick(60)
    #end of boss prep

    screen.fill((0,0,0))
    screen.blit(bg,(0,0)) 
    screen.blit(player,player_pos)
    collision_player=pygame.rect.Rect(player_pos[0]+15,player_pos[1]+15,70,70)

    if attack_chose:
        if choise_flag:
            choise=random.randint(1,1)
            choise_flag=False
            dash_flag=True
            rotation_flag=True
            wind_flag=True
        
        if choise==1:
            curent_attack="dash"

            if dash_flag:
                dash_x=1350
                dash_time=0
                dash_flag=False
                dash_n=0
                dash_sound_flag=True

            if dash_time==0:
                dash_y=random.randint(0,700)
                dash_x=1350
                
            if dash_time>=0 and dash_time<30:

                screen.blit(boss,(dash_x,dash_y))
                col_boss=pygame.rect.Rect(dash_x,dash_y,300,200)

            if dash_time==30:
                dash_sound_flag=True
            
            if dash_time>=30 and dash_time<60:
                if dash_sound_flag:
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound(dash_sound))
                    dash_sound_flag=False

                screen.blit(dash_trail,(dash_x+100,dash_y))
                screen.blit(boss,(dash_x,dash_y))
                dash_col=pygame.rect.Rect(dash_x,dash_y,300,200)
                col_boss=pygame.rect.Rect(dash_x,dash_y,300,200)

                dash_x-=50

            dash_time+=1

            if dash_time==60:
                dash_col=pygame.rect.Rect(dash_x,dash_y,0,0)
                col_boss=pygame.rect.Rect(dash_x,dash_y,0,0)
                dash_n+=1
                dash_time=0

            if dash_n==4:
                choise_flag=True
            
        if choise==2:
            curent_attack="rotation"

        if choise==3:
            curent_attack="wind"

    if pygame.rect.Rect.colliderect(collision_player,collision_up):
        player_movement[0]=0

    if pygame.rect.Rect.colliderect(collision_player,collision_down):
        player_movement[1]=0
    
    if pygame.rect.Rect.colliderect(collision_player,collision_left):
        player_movement[2]=0

    if pygame.rect.Rect.colliderect(collision_player,collision_right):
        player_movement[3]=0

    
    if pygame.rect.Rect.colliderect(collision_player,dash_col):
        retry=True

    player_pos[0]+=player_movement[2]
    player_pos[0]+=player_movement[3]
    player_pos[1]+=player_movement[0]
    player_pos[1]+=player_movement[1]

    mouse_pos=pygame.mouse.get_pos()
    mouse_x=pygame.mouse.get_pos()[0]
    mouse_y=pygame.mouse.get_pos()[1]

    if clicked:
        mouse_y-=50
        mouse_x-=50
        pygame.mixer.Sound.play(laser_sound)
        dx=mouse_x-player_pos[0]
        dy=mouse_y-player_pos[1]
        rads=math.atan2(-dy,dx)
        rads%=2*math.pi
        degs=math.degrees(rads)

        of=pygame.math.Vector2(850,0)
        rot_laser,rect=rotate(laser,-degs,player_pos,of)
        screen.blit(rot_laser,(rect[0]+50,rect[1]+50))
    
        screen.blit(ball,(player_pos[0]-25,player_pos[1]-25))

        col_l_x=player_pos[0]
        col_l_y=player_pos[1]
        for i in range(50):
            
            col_rot_laser=pygame.rect.Rect(col_l_x,col_l_y,100,100)

            if mouse_x>player_pos[0]:
                nx=1
            else:
                nx=-1

            if mouse_y>player_pos[1]:
                ny=1
            else:
                ny=-1
            col_l_x+=(nx*rect[2])/20
            col_l_y+=(ny*rect[3])/20

            if pygame.Rect.colliderect(col_rot_laser,col_boss):
                hp-=1

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type==pygame.KEYDOWN:

            if event.key==pygame.K_w:
                player_movement[0]-=10
            if event.key==pygame.K_s:
                player_movement[1]+=10
            if event.key==pygame.K_a:
                player_movement[2]-=10
            if event.key==pygame.K_d:
                player_movement[3]+=10

        if event.type==pygame.KEYUP:
            if event.key==pygame.K_w:
                player_movement[0]=0
            if event.key==pygame.K_s:
                player_movement[1]=0
            if event.key==pygame.K_a:
                player_movement[2]=0
            if event.key==pygame.K_d:
                player_movement[3]=0

        if event.type==pygame.MOUSEBUTTONDOWN:
            clicked=True
        
        if event.type==pygame.MOUSEBUTTONUP:
            clicked=False


    pygame.display.update()
    clock.tick(60)

