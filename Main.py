
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
speed_ball=[2,2]
winner=0
options_box_position=[100,300]
cursor_pos=[options_box_position[0]+25,options_box_position[1]+100]
option=0
choise_player=0
player_color=[0,0]
ball_color=""
dificult={"1":3,"2":4,"3":6}


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

#////////////////////////////////escogiendo colors\\\\\\\\\\\\\\\\\\\\\





while not game_finish:
    events = pygame.event.get()
    for event in events:
        if event.type==pygame.QUIT:
                game_finish=True

    
    for event in events:
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_d and cursor_pos[0]<(options_box_position[0]+25)*5:
                cursor_pos[0]+=options_box_position[0]
                option+=1
            elif event.key == pygame.K_a and cursor_pos[0]>options_box_position[0]+25:
                cursor_pos[0]-=options_box_position[0]
                option-=1
            elif event.key == pygame.K_SPACE:
                player_color[choise_player]=colors[option]               
                choise_player+=1
    if choise_player==2:
        game_finish=True

    screen.fill(darkPurple)
    Write("Pong Pygame",font,yellow,screen,170,40,100,(True,10))
    if flick.Timmer():
        Write("^",font,colors[option],screen,cursor_pos[0],cursor_pos[1])
    else:
        pass
    if not game_finish:
        Write("jugador_{}".format(choise_player+1),font,colors[option],screen,cursor_pos[0]-32,cursor_pos[1]+30,30)
        Write("Jugador {} escoge tu color".format(choise_player+1),font,blue,screen,options_box_position[0]-10,options_box_position[1]-100,0,(True,5))



    for i in range(len(colors)):
        i
        DrawBox(colors[i],((i+1)*options_box_position[0]),options_box_position[1],80,80)
       
    screen.blit(logo,(10,10))

    pygame.display.flip()
    
    clock.tick(80)

option=1
game_finish=False
options_box_position=[150,180]
cursor_pos=[options_box_position[0]+25,options_box_position[1]+5]


#////////////////////////////////escogiendo dificultad\\\\\\\\\\\\\\\\\\\\\

while not game_finish:
    events = pygame.event.get()
    for event in events:
        if event.type==pygame.QUIT:
                game_finish=True


    
    for event in events:
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_w and cursor_pos[1]>options_box_position[1]+50:
                cursor_pos[1]-=50
                option-=1
            elif event.key == pygame.K_s and cursor_pos[1]<options_box_position[1]+100:
                cursor_pos[1]+=50
                option+=1
            elif event.key == pygame.K_SPACE:
                game_finish=True
                speed_ball[0]=dificult[str(option)]
                speed_ball[1]=dificult[str(option)]
                if option==3:
                    speed_player+=4
    
    
    screen.fill(darkPurple)
    Write("Pong Pygame",font,yellow,screen,170,40,100,(True,10))

    if flick.Timmer():
        Write(">",font,white,screen,cursor_pos[0]+100,cursor_pos[1]+90)
    else:
        pass
    
    Write("Escoja La dificultad",font,blue,screen,options_box_position[0]-10,options_box_position[1],80,(True,8))
    Write("Facil",font,white,screen,options_box_position[0]+160,options_box_position[1]+100)
    Write("Normal",font,white,screen,options_box_position[0]+160,options_box_position[1]+150)
    Write("Dificil",font,white,screen,options_box_position[0]+160,options_box_position[1]+200)





    
    screen.blit(logo,(10,10))

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
    if speed_ball[0]>0:
        ball_color=player_color[0]
    else:
        ball_color=player_color[1]
        

    ball.x+=speed_ball[0]
    ball.y+=speed_ball[1]

#//////////////////////////////////////////////////////////////////zona de dibujo\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    
    #Background-----------------------------------------------------
    screen.fill(darkPurple)

    for y in range(5,screen_size[0],100):
        pygame.draw.rect(screen,yellow,((screen_size[0]/2)-5,y,10,80))

    score.draw(scoreboard_size)  

    #sprites------------------------------------------------------

    ball.round(10,black)
    ball.round(8,yellow)
    player.Box(player_width,player_height,player_color[0])
    player2.Box(player_width,player_height,player_color[1])
    
    
    #Colisiones----------------------------------------------------------
    
    if ball.collider.colliderect(player.collider):

        if ball.x>(player.x+player.width) and ball.y-ball.r>player.y and ball.y+ball.r<(player.y+player.height):
            speed_ball[0]*=-1
            ball.x+=ball.r
            
        else:
            if speed_ball[1]>0 and ball.y<player.y:
                speed_ball[1]*=-1   
                ball.y-=ball.r
            elif speed_ball[1]<0 and ball.y>player.y+player.height:
                speed_ball[1]*=-1   
                ball.y+=ball.r

    if ball.collider.colliderect(player2.collider):
        
        if ball.x<(player2.x) and ball.y-ball.r>player2.y and ball.y+ball.r<(player2.y+player2.height):
            speed_ball[0]*=-1
            ball.x-=ball.r
        else:
            if speed_ball[1]>0 and ball.y<player2.y:
                speed_ball[1]*=-1   
                ball.y-=ball.r
            elif speed_ball[1]<0 and ball.y>player2.y+player.height:
                speed_ball[1]*=-1   
                ball.y+=ball.r

    if score.Winer():
        game_finish=True     
        
#\/\/\/\/\/\/\/\/\/\/\/\/\/\esenciales\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
    
    
    screen.blit(logo,(10,10))

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
        Write("Jugador 1 Gana",font,white,screen,210,180)
    
    if score.scr_2>=score.win:
        Write("Jugador 2 Gana",font,white,screen,210,180)

    if flick.Timmer():
        Write("Escape para salir",font,white,screen,200,250)
    else:
        pass    

    screen.blit(logo,(10,10))
    
    pygame.display.flip()
    
    clock.tick(80)

pygame.quit()