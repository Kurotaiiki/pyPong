from telnetlib import theNULL
from turtle import screensize
import pygame
pygame.init()

#colores 
black=(0,0,0)
white=(255,255,255)
screen_size=(800,600)
player_width=15
player_height=90



screen=pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()

#coordenadas y velocidad player 1  

#x,y,velocidad
player_1=[50,255,player_width,player_height]
player_1_speed=0




#coordenadas y velocidad player 2

#x,y,ancho,alto
player_2=[750,255,player_width,player_height,0]
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
            if event.key==  pygame.K_UP:
                player_2_speed=-3
            if event.key==  pygame.K_DOWN:
                player_2_speed= 3 

        if event.type==pygame.KEYUP:
            #mandos jugador 1
            if event.key==  pygame.K_w:
                player_1_speed=0
            if event.key==  pygame.K_s:
                player_1_speed=0
            #mandos jugador 2
            if event.key==  pygame.K_UP:
                player_2_speed=0
            if event.key==  pygame.K_DOWN:
                player_2_speed=0

    #generamos el movimiento 

    player_1[1] += player_1_speed   
    player_2[1] += player_2_speed

    #zona de logica



    screen.fill(black)
    #zona de dibujo

    player_1_render=pygame.draw.rect(screen,white,(player_1[0],player_1[1],player_1[2],player_1[3]))
    player_2_render=pygame.draw.rect(screen,white,(player_2[0],player_2[1],player_2[2],player_2[3]))

    ball_render=pygame.draw.circle(screen,white,ball_position,10)



    pygame.display.flip()
    clock.tick(60)
pygame.quit()
