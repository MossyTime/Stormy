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
rotation_cloud_sound=pygame.mixer.Sound("data/rotation_cloud_sound.mp3")
teleport_sound=pygame.mixer.Sound("data/teleport_sound.mp3")
dash_start_sound=pygame.mixer.Sound("data/dash_start_sound.mp3")
target_lock_sound=pygame.mixer.Sound("data/target_lock_sound.mp3")
end_sound=pygame.mixer.Sound("data/end_sound.mp3")


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
text_tittle_shadow=pygame.transform.scale(text_tittle_shadow,(600,200))

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

wall_v=pygame.transform.rotate(lightning,90)
wall_v=pygame.transform.scale(wall_v,(50,700))
wall_h=pygame.transform.scale(lightning,(1500,50))

teleport=pygame.transform.scale(lightning,(300,50))
final_light=pygame.transform.scale(lightning,(1500,200))

ball=pygame.image.load("data/ball.png")
ball=pygame.transform.scale(ball,(150,150))

explosion=pygame.image.load("data/boss_death.png")
explosion=pygame.transform.scale(explosion,(200,200))

cloud=pygame.image.load("data/cloud.png")
cloud=pygame.transform.scale(cloud,(400,300))

ball_boss=pygame.image.load("data/ball_boss.png")
ball_boss=pygame.transform.scale(ball_boss,(400,400))

roar_lines=pygame.image.load("data/roar_lines.png")
roar_lines=pygame.transform.scale(roar_lines,(1500,700))

boss=pygame.image.load("data/boss.png")
boss=pygame.transform.scale(boss,(300,200))

logo_boss=pygame.image.load("data/boss.png")

dash_trail=pygame.image.load("data/dash_trail.png")
dash_start=pygame.image.load("data/dash_trail.png")
fakeout_glow=pygame.image.load("data/dash_trail.png")
fakeout_glow=pygame.transform.rotate(fakeout_glow,90)
fakeout_glow=pygame.transform.scale(fakeout_glow,(500,300))
dash_start=pygame.transform.rotate(dash_start,180)
dash_start=pygame.transform.scale(dash_start,(300,700))
dash_trail=pygame.transform.scale(dash_trail,(500,200))

rotation_laser=pygame.image.load("data/rotation_beam.png")
rotation_laser=pygame.transform.scale(rotation_laser,(800,50))

rotation_shine=pygame.image.load("data/rotation_shine.png")
rotation_shine=pygame.transform.scale(rotation_shine,(300,300))

space=pygame.image.load("data/phase2_background.png")
space=pygame.transform.scale(space,(1500,700))

wind=pygame.image.load("data/wind.png")
wind=pygame.transform.scale(wind,(1500,700))

wind_up=pygame.transform.rotate(wind,270)
wind_down=pygame.transform.rotate(wind,90)
wind_left=pygame.transform.rotate(wind,180)
wind_right=wind

wind_warn=pygame.image.load("data/wind_warn.png")
wind_warn=pygame.transform.scale(wind_warn,(600,600))
wind_warn.set_alpha(50)

wind_warn_up=pygame.transform.rotate(wind,180)
wind_warn_down=wind_warn
wind_warn_left=pygame.transform.rotate(wind,90)
wind_warn_right=pygame.transform.rotate(wind,270)

rotation_up=pygame.transform.rotate(rotation_laser,270)
rotation_down=pygame.transform.rotate(rotation_laser,90)
rotation_left=pygame.transform.rotate(rotation_laser,180)
rotation_right=rotation_laser

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

fakeout=False

fakeout_flag=True

phase2=False

final_col=pygame.rect.Rect(0,0,0,0)

dash_col=pygame.rect.Rect(0,0,0,0)

collision_up=pygame.rect.Rect(0,0,1500,1)
collision_down=pygame.rect.Rect(0,700,1500,1)
collision_left=pygame.rect.Rect(0,0,1,700)
collision_right=pygame.rect.Rect(1500,0,1,700)

wall_up=pygame.rect.Rect(0,0,1500,50)
wall_down=pygame.rect.Rect(0,650,1500,50)
wall_left=pygame.rect.Rect(0,0,50,700)
wall_right=pygame.rect.Rect(1450,0,50,700)

wall_u=pygame.rect.Rect(0,0,1500,0)
wall_d=pygame.rect.Rect(0,690,1500,0)
wall_l=pygame.rect.Rect(0,0,0,700)
wall_r=pygame.rect.Rect(1490,0,0,700)

col_rotr_up_laser=pygame.rect.Rect(0,0,0,0)

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

                    tittle=False

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

                    fakeout=False

                    fakeout_flag=True

                    phase2=False

                    final_col=pygame.rect.Rect(0,0,0,0)

                    collision_up=pygame.rect.Rect(0,0,1500,1)
                    collision_down=pygame.rect.Rect(0,700,1500,1)
                    collision_left=pygame.rect.Rect(0,0,1,700)
                    collision_right=pygame.rect.Rect(1450,0,1,700)

                    wall_u=pygame.rect.Rect(0,0,1500,0)
                    wall_d=pygame.rect.Rect(0,690,1500,0)
                    wall_l=pygame.rect.Rect(0,0,0,700)
                    wall_r=pygame.rect.Rect(1490,0,0,700)

                    retry_button=pygame.rect.Rect(600,500,300,150)

                    col_boss=pygame.rect.Rect(0,0,0,0)

                    dash_col=pygame.rect.Rect(0,0,0,0)

                    col_rotr_up_laser=pygame.rect.Rect(0,0,0,0)

                    

        screen.blit(text_retry_button,(600,490))

        pygame.display.flip() 
        pygame.display.update()
        clock.tick(60)
    #end of retry
        
    if hp<=0:
        if not(phase2):
            fakeout=True
        else:
            victory=True
            end_sound_flag=True

    while fakeout:
        if fakeout_flag:
            fakeout_time=0
            fakeout_flag=False
            fall_down=250
            bg_down=0
            space_down=-700
            clouds_down=-100
            pygame.mixer_music.load("data/phase2_intro_music.mp3")
            pygame.mixer_music.play()
            pygame.mixer.Sound.play(explosion_sound)

        screen.fill((0,0,0))

        if fakeout_time>=0 and fakeout_time<300:
            screen.blit(bg,(0,0))
            screen.blit(boss,(600,fall_down))

            ex_x=random.randint(600,700)
            screen.blit(explosion,(ex_x,fall_down))

            fall_down+=1.5

        if fakeout_time==300:
            pygame.mixer.Sound.stop(explosion_sound)
            pygame.mixer.Sound.play(dash_start_sound)
            fall_down=700
        
        if fakeout_time>=300 and fakeout_time<420:
            screen.blit(bg,(0,0))
            screen.blit(fakeout_glow,(500,400))

        if fakeout_time>=420 and fakeout_time<480:
            screen.blit(bg,(0,0))
            screen.blit(boss,(600,fall_down))

            fall_down-=7.5

        if fakeout_time>=480 and fakeout_time<660:

            screen.blit(bg,(0,bg_down))
            screen.blit(space,(0,space_down))
            cloud_x=-200
            for i in range(20):
                screen.blit(cloud,(cloud_x,clouds_down))
                cloud_x+=100
            bg_down+=3.888
            space_down+=3.888
            clouds_down+=3.9
            screen.blit(boss,(600,250))

        if fakeout_time>=660 and fakeout_time<720:
            screen.blit(space,(0,0))
            screen.blit(boss,(600,250))

        if fakeout_time==720:
            pygame.mixer.Sound.play(teleport_sound)

        if fakeout_time>=720 and fakeout_time<810:
            screen.blit(space,(0,0))
            screen.blit(wall_v,(0,0))
            screen.blit(boss,(600,250))

        if fakeout_time>=810:
            fakeout=False
            attack_chose=False
            phase2=True
            clicked=False
            boss_music_flag=True
            hp=20000

        fakeout_time+=1

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()

        player_pos=[300,280]
        player_movement=[0,0,0,0]

        screen.blit(player,player_pos)
        
        pygame.display.update()
        clock.tick(60)
    #end of fakeout
        
    screen.fill((0,0,0))
         
    if phase2:

        if boss_music_flag:
            pygame.mixer_music.load("data/phase2_music.mp3")
            pygame.mixer_music.play(-1)
            bg1_x=0
            bg2_x=1500
            boss_music_flag=False
            phase2_time=0
        
        if bg2_x>0:
            screen.blit(space,(bg1_x,0))
        screen.blit(space,(bg2_x,0))

        if bg1_x==-1500:
            bg1_x=0
        if bg2_x==0:
            bg2_x=1500

        bg1_x-=20
        bg2_x-=20

        player_pos[0]-=9

        screen.blit(boss,(1100,250))
        col_boss=pygame.rect.Rect(900,150,300,200)

        if phase2_time==0:
            pygame.mixer.Channel(6).play(pygame.mixer.Sound(target_lock_sound))

        if phase2_time>=0 and phase2_time<60:
            if phase2_time%2==0:
                pygame.draw.circle(screen,(0,100,255),(player_pos[0]+50,player_pos[1]+50),70)

            else:
                pygame.draw.circle(screen,(255,255,0),(player_pos[0]+50,player_pos[1]+50),70)

        if phase2_time==60:
            final_x=player_pos[0]
            final_y=player_pos[1]

        if phase2_time>=60 and phase2_time<120:
            pygame.draw.circle(screen,(255,0,0),(final_x+50,final_y+50),70)

        if phase2_time==120:
            final_x-=50
            pygame.mixer.Channel(7).play(pygame.mixer.Sound(teleport_sound))
            dx=final_x-1250
            dy=final_y-350
            rads=math.atan2(-dy,dx)
            rads%=2*math.pi
            degs=math.degrees(rads)

            of=pygame.math.Vector2(800,0)
            rot_light,rect_light=rotate(final_light,-degs,(1250,350),of)

        if phase2_time>=120 and phase2_time<140:
            
            screen.blit(rot_light,(rect_light[0]+50,rect_light[1]+50))
            final_col=pygame.rect.Rect(final_x,final_y,100,100)

        phase2_time+=1

        if phase2_time>=140:

            final_col=pygame.rect.Rect(0,0,0,0)
            phase2_time=0

        screen.blit(wall_v,(0,0))
        wall_l=pygame.rect.Rect(0,0,40,700)
        

    while victory:
        end_screen=pygame.rect.Rect(0,0,1500,700)
        if end_sound_flag:
            pygame.mixer_music.stop()
            pygame.mixer_music.load("data/phase2_outro_music.mp3")
            pygame.mixer_music.play()
            pygame.mixer.Channel(1).play(end_sound)
            pygame.mixer.Channel(2).play(roar_sound)
            end_sound_flag=False

        screen.fill((0,0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.draw.rect(screen,(255,255,255),end_screen)

        pygame.display.update()
        clock.tick(60)


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

    if not(phase2):
        screen.blit(bg,(0,0))
    if clicked:
        screen.blit(ball,(player_pos[0]-25,player_pos[1]-25)) 
    screen.blit(player,player_pos)
    collision_player=pygame.rect.Rect(player_pos[0]+15,player_pos[1]+15,70,70)

    if attack_chose:
        if choise_flag:
            choise=random.randint(1,3)
            choise_flag=False
            dash_flag=True
            rotation_flag=True
            wind_flag=True
        
        if choise==1:
            curent_attack="dash"

            if dash_flag:
                dash_x=1350
                dash_time=-1
                dash_flag=False
                dash_n=0
                dash_sound_flag=True
                dash_start_flag=True
                dash_start_sound_flag=True
                dash_timer=0

            if dash_start_flag:

                if dash_start_sound_flag:
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound(dash_start_sound))
                    dash_start_sound_flag=False

                screen.blit(dash_start,(1200,0))

                dash_timer+=1

                if dash_timer>=120:
                    dash_start_flag=False
                    dash_time=0

            if dash_time==0:
                dash_y=random.randint(0,700)
                dash_x=1350
                
            if dash_time>=0 and dash_time<30:

                screen.blit(boss,(dash_x,dash_y))
                col_boss=pygame.rect.Rect(dash_x+50,dash_y+50,200,150)

            if dash_time==30:
                dash_sound_flag=True
            
            if dash_time>=30 and dash_time<60:
                if dash_sound_flag:
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound(dash_sound))
                    dash_sound_flag=False

                screen.blit(dash_trail,(dash_x+100,dash_y))
                screen.blit(boss,(dash_x,dash_y))
                dash_col=pygame.rect.Rect(dash_x+50,dash_y+50,200,150)
                col_boss=pygame.rect.Rect(dash_x+50,dash_y+50,200,150)

                dash_x-=50
            if not(dash_start_flag):
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
            
            if rotation_flag:
                rotation_flag=False
                rotation_angle=90
                rotation_time=0
                rotation_ofu=pygame.math.Vector2(0,-400)
                rotation_ofd=pygame.math.Vector2(0,400)
                rotation_ofl=pygame.math.Vector2(-400,0)
                rotation_ofr=pygame.math.Vector2(400,0)
                teleport_sound_flag=True
                rotation_sound_flag=True
                rotation_warn_sound_flag=True
                laser_angle=0
                boss_rotation_of=pygame.math.Vector2(50,0)
                ux=0
                uy=0
                r_angle=0
                rot_an=0

                

            if rotation_time>=0 and rotation_time<10:
                if teleport_sound_flag:
                    pygame.mixer.Channel(2).play(pygame.mixer.Sound(teleport_sound))
                    teleport_sound_flag=False

                screen.blit(teleport,(800,200))
                screen.blit(teleport,(800,250))
                screen.blit(teleport,(800,300))

            if rotation_time>=10 and rotation_time<30:
                screen.blit(boss,(750,150))

            if rotation_time>=30 and rotation_time<360:

                if rotation_time>=30 and rotation_time<150:
                    if rotation_warn_sound_flag:
                        pygame.mixer.Channel(2).play(pygame.mixer.Sound(rotation_warn_sound))
                        pygame.mixer.Channel(3).play(pygame.mixer.Sound(rotation_cloud_sound))
                        rotation_warn_sound_flag=False

                    rot_warn_v=pygame.rect.Rect(725,0,50,700)
                    rot_warn_h=pygame.rect.Rect(0,325,1500,50)
                    pygame.draw.rect(screen,(0,150,255),rot_warn_v)
                    pygame.draw.rect(screen,(0,150,255),rot_warn_h)

                    rot_cloud,cloud_rect=rotate(boss,rotation_angle,(800,400),boss_rotation_of)
                    screen.blit(boss,(cloud_rect))
                    col_boss=pygame.rect.Rect(700,300,100,100)

                    rotation_angle+=10

                if rotation_time>=150 and rotation_time<390:
                    if rotation_sound_flag:
                        pygame.mixer.Channel(2).play(pygame.mixer.Sound(rotation_sound))
                        rotation_sound_flag=False

                    rotr_up_laser,rotr_up_rect=rotate(rotation_up,laser_angle,(750,350),rotation_ofu)
                    screen.blit(rotr_up_laser,(rotr_up_rect))

                    rotr_down_laser,rotr_down_rect=rotate(rotation_down,laser_angle,(750,350),rotation_ofd)
                    screen.blit(rotr_down_laser,(rotr_down_rect))

                    rotr_left_laser,rotr_left_rect=rotate(rotation_left,laser_angle,(750,350),rotation_ofl)
                    screen.blit(rotr_left_laser,(rotr_left_rect))

                    rotr_right_laser,rotr_right_rect=rotate(rotation_right,laser_angle,(750,350),rotation_ofr)
                    screen.blit(rotr_right_laser,(rotr_right_rect))

                    laser_angle+=1
                    
                    ux=(800*math.cos(laser_angle/57))+750
                    uy=(800*math.sin(laser_angle/57))+350

                    col_r_x=750
                    col_r_y=350

                    dxr=ux-col_r_x
                    dyr=uy-col_r_y
                    radsr=math.atan2(-dyr,dxr)
                    radsr%=2*math.pi
                    degsr=math.degrees(radsr)

                    ofr=pygame.math.Vector2(0,0)
                    trrr,rrect=rotate(rotation_up,laser_angle,(col_r_x,col_r_y),ofr)

                    col_r_x=750
                    col_r_y=350
                    for i in range(25):
                        
                        col_rotr_up_laser=pygame.rect.Rect(col_r_x,col_r_y,25,25)

                        col_r_x+=(dxr)/20
                        col_r_y+=(dyr)/20
                        # pygame.draw.rect(screen,(0,0,255),rrect)
                        # pygame.draw.rect(screen,(255,0,0),col_rotr_up_laser)

                        if pygame.rect.Rect.colliderect(collision_player,col_rotr_up_laser):
                            retry=True

                    #up
                        
                    rx=(800*math.cos((laser_angle+90)/57))+750
                    ry=(800*math.sin((laser_angle+90)/57))+350

                    col_r_x=750
                    col_r_y=350

                    dxr=rx-col_r_x
                    dyr=ry-col_r_y
                    radsr=math.atan2(-dyr,dxr)
                    radsr%=2*math.pi
                    degsr=math.degrees(radsr)

                    ofr=pygame.math.Vector2(0,0)
                    trrr,rrect=rotate(rotation_right,laser_angle,(col_r_x,col_r_y),ofr)

                    col_r_x=750
                    col_r_y=350
                    for i in range(25):
                        
                        col_rotr_up_laser=pygame.rect.Rect(col_r_x,col_r_y,25,25)

                        col_r_x+=(dxr)/20
                        col_r_y+=(dyr)/20
                        # pygame.draw.rect(screen,(0,0,255),rrect)
                        # pygame.draw.rect(screen,(255,0,0),col_rotr_up_laser)

                        if pygame.rect.Rect.colliderect(collision_player,col_rotr_up_laser):
                            retry=True

                    #right
                        
                    dx=(800*math.cos((laser_angle+180)/57))+750
                    dy=(800*math.sin((laser_angle+180)/57))+350

                    col_r_x=750
                    col_r_y=350

                    dxr=dx-col_r_x
                    dyr=dy-col_r_y
                    radsr=math.atan2(-dyr,dxr)
                    radsr%=2*math.pi
                    degsr=math.degrees(radsr)

                    ofr=pygame.math.Vector2(0,0)
                    trrr,rrect=rotate(rotation_down,laser_angle,(col_r_x,col_r_y),ofr)

                    col_r_x=750
                    col_r_y=350
                    for i in range(25):
                        
                        col_rotr_up_laser=pygame.rect.Rect(col_r_x,col_r_y,25,25)

                        col_r_x+=(dxr)/20
                        col_r_y+=(dyr)/20
                        # pygame.draw.rect(screen,(0,0,255),rrect)
                        # pygame.draw.rect(screen,(255,0,0),col_rotr_up_laser)

                        if pygame.rect.Rect.colliderect(collision_player,col_rotr_up_laser):
                            retry=True

                    #down
                        
                    lx=(800*math.cos((laser_angle+270)/57))+750
                    ly=(800*math.sin((laser_angle+270)/57))+350

                    col_r_x=750
                    col_r_y=350

                    dxr=lx-col_r_x
                    dyr=ly-col_r_y
                    radsr=math.atan2(-dyr,dxr)
                    radsr%=2*math.pi
                    degsr=math.degrees(radsr)

                    ofr=pygame.math.Vector2(0,0)
                    trrr,rrect=rotate(rotation_left,laser_angle,(col_r_x,col_r_y),ofr)

                    col_r_x=750
                    col_r_y=350
                    for i in range(25):
                        
                        col_rotr_up_laser=pygame.rect.Rect(col_r_x,col_r_y,25,25)

                        col_r_x+=(dxr)/20
                        col_r_y+=(dyr)/20
                        # pygame.draw.rect(screen,(0,0,255),rrect)
                        # pygame.draw.rect(screen,(255,0,0),col_rotr_up_laser)

                        if pygame.rect.Rect.colliderect(collision_player,col_rotr_up_laser):
                            retry=True

                    #left
                        
                    rotation_angle+=10

                    rot_cloud,cloud_rect=rotate(boss,rotation_angle,(800,400),boss_rotation_of)
                    screen.blit(boss,(cloud_rect))
                    screen.blit(rotation_shine,(600,200))
                    col_boss=pygame.rect.Rect(700,300,100,100)

                if rotation_time>=390 and rotation_time<400:

                    if teleport_sound_flag:
                        pygame.mixer.Channel(2).play(pygame.mixer.Sound(teleport_sound))
                        teleport_sound_flag=False

                    screen.blit(teleport,(800,200))
                    screen.blit(teleport,(800,250))
                    screen.blit(teleport,(800,300))

            if rotation_time>=400:
                choise_flag=True

            rotation_time+=1

        if choise==3:
            curent_attack="wind"

            if wind_flag:
                wind_time=0
                wind_sound_flag=True
                boss_rot_angle=0

                wind_bp=(-500,-500)
                
                wind_n=[0,0]

                wc=[]
                wh=[]

                wu=[0,700]
                wd=[-700,0]
                wl=[-1500,0]
                wr=[1500,0]

                boss_cw=(0,0)

                wall_u=pygame.rect.Rect(0,0,1500,40)
                wall_d=pygame.rect.Rect(0,660,1500,40)
                wall_l=pygame.rect.Rect(0,0,40,700)
                wall_r=pygame.rect.Rect(1460,0,40,700)

                wind_flag=False

                for i in range(4):
                    w_choise=random.randint(1,4)
                    wh.append(w_choise)
                    if w_choise==1:
                        wc.append(wu)
                    if w_choise==2:
                        wc.append(wd)
                    if w_choise==3:
                        wc.append(wl)
                    if w_choise==4:
                        wc.append(wr)


            if wind_time>=0 and wind_time<30:
                if wind_sound_flag:
                    pygame.mixer.Channel(3).play(pygame.mixer.Sound(dash_warn_sound))
                    wind_sound_flag=False
                pygame.draw.rect(screen,(0,150,255),wall_up)
                pygame.draw.rect(screen,(0,150,255),wall_down)
                pygame.draw.rect(screen,(0,150,255),wall_left)
                pygame.draw.rect(screen,(0,150,255),wall_right)
            
            if wind_time==30:
                wind_sound_flag=True

            if wind_time>=30 and wind_time<540:
                if wind_sound_flag:
                    pygame.mixer.Channel(3).play(pygame.mixer.Sound(wind_sound))
                    wind_sound_flag=False

                screen.blit(wall_v,(0,0))
                screen.blit(wall_v,(1450,0))
                screen.blit(wall_h,(0,0))
                screen.blit(wall_h,(0,650))

                le_time=int(pygame.time.get_ticks()/1000)

                if le_time%2==0:
                    wind_show=True

                else:
                    wind_show=False
                    wind_n=[0,0]

                if wind_time>=90 and wind_time<210:

                    if wind_show:
                        screen.blit(wind,(wind_n[0],wind_n[1]))
                    
                    if wh[0]==1:
                        player_pos[1]-=6
                        wind_n[1]-=20
                        wind_bp=(750,700)
                        boss_cw=(550,600)
                    elif wh[0]==2:
                        player_pos[1]+=6
                        wind_n[1]+=20
                        wind_bp=(750,0)
                        boss_cw=(550,-100)
                    elif wh[0]==3:
                        player_pos[0]-=9
                        wind_n[0]-=20
                        wind_bp=(1500,350)
                        boss_cw=(1350,250)
                    elif wh[0]==4:
                        player_pos[0]+=9
                        wind_n[0]+=20
                        wind_bp=(0,350)
                        boss_cw=(-150,150)

                if wind_time>=210 and wind_time<320:

                    if wind_show:
                        screen.blit(wind,(wind_n[0],wind_n[1]))
                    if wh[1]==1:
                        player_pos[1]-=6
                        wind_n[1]-=20
                        wind_bp=(750,700)
                        boss_cw=(550,600)
                    elif wh[1]==2:
                        player_pos[1]+=6
                        wind_n[1]+=20
                        wind_bp=(750,0)
                        boss_cw=(550,-100)
                    elif wh[1]==3:
                        player_pos[0]-=9
                        wind_n[0]-=20
                        wind_bp=(1500,350)
                        boss_cw=(1350,250)
                    elif wh[1]==4:
                        player_pos[0]+=9
                        wind_n[0]+=20
                        wind_bp=(0,350)
                        boss_cw=(-150,150)

                if wind_time>=320 and wind_time<430:

                    if wind_show:
                        screen.blit(wind,(wind_n[0],wind_n[1]))
                    if wh[2]==1:
                        player_pos[1]-=6
                        wind_n[1]-=20
                        wind_bp=(750,700)
                        boss_cw=(550,600)
                    elif wh[2]==2:
                        player_pos[1]+=6
                        wind_n[1]+=20
                        wind_bp=(750,0)
                        boss_cw=(550,-100)
                    elif wh[2]==3:
                        player_pos[0]-=9
                        wind_n[0]-=20
                        wind_bp=(1500,350)
                        boss_cw=(1350,250)
                    elif wh[2]==4:
                        player_pos[0]+=9
                        wind_n[0]+=20
                        wind_bp=(0,350)
                        boss_cw=(-150,150)

                if wind_time>=430 and wind_time<540:

                    if wind_show:
                        screen.blit(wind,(wind_n[0],wind_n[1]))
                    if wh[3]==1:
                        player_pos[1]-=6
                        wind_n[1]-=20
                        wind_bp=(750,700)
                        boss_cw=(550,600)
                    elif wh[3]==2:
                        player_pos[1]+=6
                        wind_n[1]+=20
                        wind_bp=(750,0)
                        boss_cw=(550,-100)
                    elif wh[3]==3:
                        player_pos[0]-=9
                        wind_n[0]-=20
                        wind_bp=(1500,350)
                        boss_cw=(1350,250)
                    elif wh[3]==4:
                        player_pos[0]+=9
                        wind_n[0]+=20
                        wind_bp=(0,350)
                        boss_cw=(-150,150)

                    

                of=pygame.math.Vector2(50,0)
                rot_boss,rect=rotate(boss,boss_rot_angle,(wind_bp),of)
                screen.blit(boss,(rect[0]+50,rect[1]+50))
                col_boss=pygame.rect.Rect(boss_cw[0],boss_cw[1],300,200)

                boss_rot_angle+=1
                
            if wind_time>=540:
                wall_u=pygame.rect.Rect(0,0,1500,0)
                wall_d=pygame.rect.Rect(0,690,1500,0)
                wall_l=pygame.rect.Rect(0,0,0,700)
                wall_r=pygame.rect.Rect(1490,0,0,700)
                choise_flag=True
                boss_rot_angle=0

            wind_time+=1



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

    if pygame.rect.Rect.colliderect(collision_player,wall_u):
        retry=True

    if pygame.rect.Rect.colliderect(collision_player,wall_d):
        retry=True

    if pygame.rect.Rect.colliderect(collision_player,wall_l):
        retry=True

    if pygame.rect.Rect.colliderect(collision_player,wall_r):
        retry=True

    if pygame.rect.Rect.colliderect(collision_player,final_col):
        retry=True

    player_pos[0]+=player_movement[2]
    player_pos[0]+=player_movement[3]
    player_pos[1]+=player_movement[0]
    player_pos[1]+=player_movement[1]

    mouse_pos=pygame.mouse.get_pos()
    mouse_x=pygame.mouse.get_pos()[0]
    mouse_y=pygame.mouse.get_pos()[1]

    health_bar=pygame.rect.Rect(250,0,hp/25.0,10)
    pygame.draw.rect(screen,(255,0,0),health_bar)

    if clicked:
        mouse_y-=50
        mouse_x-=50
        pygame.mixer.Sound.play(laser_sound)
        dx=mouse_x-player_pos[0]
        dy=mouse_y-player_pos[1]
        rads=math.atan2(-dy,dx)
        rads%=2*math.pi
        degs=math.degrees(rads)

        of=pygame.math.Vector2(840,0)
        rot_laser,rect=rotate(laser,-degs,player_pos,of)
        screen.blit(rot_laser,(rect[0]+50,rect[1]+50))


        col_l_x=player_pos[0]
        col_l_y=player_pos[1]
        for i in range(25):
            
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
                if not(phase2):
                    hp-=2
                else:
                    hp-=3

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

