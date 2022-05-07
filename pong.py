
import pygame
pygame.init()

#colores 
black=(0,0,0)
white=(255,255,255)
orange=(255,128,0)
green=(0,255,0)
screen_size=(800,480)
player_width=15
player_height=90
ball_color="orange"



screen=pygame.display.set_mode(screen_size)

backGround=pygame.image.load("Banner-Twitch.png").convert()
clock = pygame.time.Clock()

#coordenadas y velocidad player 1  

#x,y
player_1=[50,195,player_width,player_height]
player_1_speed=0




#coordenadas y velocidad player 2

#x,y,ancho,alto
player_2=[750,195,player_width,player_height,0]
player_2_speed=0



#coordenadas pelota

ball_position=[400,300]
ball_movement=[3,3]

game_over=False

while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
                game_over=True

        if event.type==pygame.KEYDOWN:
            #mandos jugador 1
            if event.key==  pygame.K_w:
                player_1_speed=-3
            if event.key==  pygame.K_s:
                player_1_speed=3
            #mandos jugador 2
            if event.key==  pygame.K_o:
                player_2_speed=-3
            if event.key==  pygame.K_l:
                player_2_speed= 3 

        if event.type==pygame.KEYUP:
            #mandos jugador 1
            if event.key==  pygame.K_w:
                player_1_speed=0
            if event.key==  pygame.K_s:
                player_1_speed=0
            #mandos jugador 2
            if event.key==  pygame.K_o:
                player_2_speed=0
            if event.key==  pygame.K_l:
                player_2_speed=0

    #generamos el movimiento 


    #Zona de logica -----------------------------------------------------------------------


    #jugadores
    


    if player_1[1] > 0 and player_1[1] < 390:
        player_1[1] += player_1_speed
    else:
        if player_1[1] <= 0:
          player_1[1]+=1
        if player_1[1] >= 390:
         player_1[1]-=1


    if player_2[1] > 0 and player_2[1] < 390:
        player_2[1] += player_2_speed
    else:
        if player_2[1] <= 0:
          player_2[1]+=1
        if player_2[1] >= 390:
         player_2[1]-=1

    #pelota

    #cambio de color

    if ball_position[0] < 400:
        ball_color=green
    else:
        ball_color=orange


    #si la pelota toca borde superior o inferior

    if ball_position[1] > 470 or ball_position[1] < 10 :
        ball_movement[1]*=-1

    ball_position[0]+=ball_movement[0]
    ball_position[1]+=ball_movement[1]
    
    #si la pelota sale de pantalla

    if ball_position[0] > 790 or ball_position[0] < 10:
        ball_position=[400,240]
        ball_movement[0]*=-1


    #zona de logica ---------------------------------------------------------------------------



    screen.blit(backGround,[-40,0])
    #zona de dibujo

    player_1_render=pygame.draw.rect(screen,orange,(player_1[0],player_1[1],player_1[2],player_1[3]))
    player_2_render=pygame.draw.rect(screen,green,(player_2[0],player_2[1],player_2[2],player_2[3]))
    for y in range(5,595,5):
        pygame.draw.rect(screen,white,(395,y,1,2))


    ball_render=pygame.draw.circle(screen,ball_color,ball_position,10)


    #colisiones

    if ball_render.colliderect(player_1_render) or ball_render.colliderect(player_2_render):
        ball_movement[0]*=-1


    pygame.display.flip()
    clock.tick(60)
pygame.quit()
