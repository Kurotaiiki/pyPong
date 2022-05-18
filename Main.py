import pygame,sys
from Utility import *
pygame.init()

#/\/\/\/\/\/\/\/\/\/\/\/\/\/\esenciales\/\/\/\/\/\/\/\/\/\/\/\/\/
clock = pygame.time.Clock()
game_finish=False
#\/\/\/\/\/\/\/\/\/\/\/\/\/\esenciales\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/

player_width=15
player_height=90
ball_r_init=5
speed_player=5
speed_ball=[3,3]
winner=0
color_player_1=""
color_player_2=""
cursor_pos=[125,230]
options_box_position=[100,150]


inicial_Y_player=( (screen_size[1] + scoreboard_size )/ 2 ) - player_height/2
inicial_X_player=50

inicial_X_ball=(screen_size[0]/2)-ball_r_init
inicial_Y_ball=(screen_size[1]+scoreboard_size)/2

up_limit=scoreboard_size
down_limit=screen_size[1]
    
#/////////////////////Objetos\\\\\\\\\\\\\\\\\\\\
player= Gameobject(inicial_X_player,inicial_Y_player)
player2= Gameobject(screen_size[0]-inicial_X_player,inicial_Y_player)
ball=Gameobject(inicial_X_ball,inicial_Y_ball)
score=Scoreboard(10)
flick=Flicker(30,30)

#////////////////////////////////antes de jugar\\\\\\\\\\\\\\\\\\\\\

while not game_finish:
    events = pygame.event.get()
    for event in events:
        if event.type==pygame.QUIT:
                game_finish=True

    color_player_1=white
    color_player_2=purple
    
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d and cursor_pos[0]<=500:
                cursor_pos[0]+=options_box_position[0]
            if event.key == pygame.K_a and cursor_pos[0]>=200:
                cursor_pos[0]-=options_box_position[0]

    screen.fill(darkPurple)
    Write("Pong Pygame ",font2,white,screen,220,30)
    if flick.Timmer():
        Write("^",font2,white,screen,cursor_pos[0],cursor_pos[1])
    else:
        pass 

    for i in range(len(colores)-1):
        i+=1
        DrawBox(colores[i],i*options_box_position[0],options_box_position[1],80,80)
    
    pygame.display.flip()
    
    clock.tick(80)

game_finish=False

#///////////////////////////////////////////////////////////////////////Zona de Juego\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

while not game_finish:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
                game_finish=True

#/////////////////////////////////////////////////////////////////////zona de logica\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

    keys=pygame.key.get_pressed()


#//////////////////////////////movimiento del jugador\\\\\\\\\\\\\\\\\\\
    
    if keys[pygame.K_w] and player.y>up_limit:
        player.y-=speed_player
    if keys[pygame.K_s] and player.y<(down_limit-player_height):
        player.y+=speed_player
    if keys[pygame.K_o] and player2.y>up_limit:
        player2.y-=speed_player
    if keys[pygame.K_l] and player2.y<(down_limit-player_height):
        player2.y+=speed_player

#/////////////////////////Movimiento de pelota\\\\\\\\\\\\\\\\\\\\\\\
    
    #rebote Superior e inferior---------------------------------------
    if ball.y<=(up_limit+ball.r) or ball.y>=(down_limit-ball.r):
        speed_ball[1]*=-1

    #Salir por bordes laterales -------------------------------------
    if ball.x<=(-ball.r) or ball.x>=screen_size[0]+ball.r:
        score.point(ball.x)
        ball.rest_position()
        speed_ball[0]*=-1
        speed_ball[1]*=-1    

    ball.x+=speed_ball[0]
    ball.y+=speed_ball[1]

#//////////////////////////////////////////////////////////////////zona de dibujo\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    
    #Background-----------------------------------------------------
    screen.fill(darkPurple)

    for y in range(5,screen_size[0],100):
        pygame.draw.rect(screen,yellow,((screen_size[0]/2)-5,y,10,80))

    score.draw(scoreboard_size)  

    #sprites------------------------------------------------------

    player.Box(player_width,player_height,color_player_1)
    player2.Box(player_width,player_height,color_player_2)
    ball.round(10,pink)
    
    #Colisiones----------------------------------------------------------

    if ball.collider.colliderect(player.collider):

        if ball.x>(player.x+player.width) and (ball.y>(player.y) or ball.y<((player.y+player.height))):
            speed_ball[0]*=-1
            ball.x+=ball.r
        else:
            if speed_ball[1]<0:
                ball.y+=ball.r
            if speed_ball[1]>0:
                ball.y-=ball.r
            ball.x-=ball.r 
            speed_ball[1]*=-1

    if ball.collider.colliderect(player2.collider):
        
        if ball.x<(player2.x) and ball.y>(player2.y+ball.r) or ball.y<((player2.y+player2.height)):
            speed_ball[0]*=-1
            ball.x-=ball.r
        else:
            if speed_ball[1]<0:
                ball.y+=(ball.r*speed_player)
            if speed_ball[1]>0:
                ball.y-=(ball.r*speed_player)
            ball.x+=(ball.r*2)
            speed_ball[1]*=-1   

    if score.Winer():
        game_finish=True     
        
#\/\/\/\/\/\/\/\/\/\/\/\/\/\esenciales\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
    
    pygame.display.flip()
    
    clock.tick(80)
    
#\/\/\/\/\/\/\/\/\/\/\/\/\/\esenciales\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/

game_finish=False

#/////////////////////////////termino el juego\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

while not game_finish:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
                game_finish=True

    keys=pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        game_finish=True
    
    screen.fill(darkPurple)
    score.draw(scoreboard_size)

    if score.scr_1>=score.win:
        Write("Jugador 1 Gana",font2,white,screen,210,180)
    
    if score.scr_2>=score.win:
        Write("Jugador 2 Gana",font2,white,screen,210,180)

    if flick.Timmer():
        Write("Escape para salir",font2,white,screen,200,250)
    else:
        pass    

    pygame.display.flip()
    
    clock.tick(80)

pygame.quit()