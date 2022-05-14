import pygame,sys
pygame.init()

#colores 
black=(0,0,0)
white=(255,255,255)
pink=(242, 39, 171)
yellow=(242, 208, 39)
screen_size=(800,480)
player_width=15
player_height=90
ball_color="pink"
up=False
down=True
score_1=10
score_2=10
playersito= pygame

font = pygame.font.SysFont(None,70)
font2 = pygame.font.SysFont(None,90)


def Esribir(text,font,color,surface,x,y):
        
    textobj=font.render(text,True,color)
    textrect=textobj.get_rect()
    textrect.topleft=(x,y)
    surface.blit(textobj,textrect)

    

def Marcador():
    
        pygame.draw.rect(screen,(19, 5, 69),(315,10,160,60))
        pygame.draw.rect(screen,(29, 15, 79),(305,15,180,50))
        Esribir(str(score_1),font,white,screen,330,20)
        Esribir(str(score_2),font,white,screen,410,20)
        






screen=pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()

#coordenadas y velocidad player 1  

#x,y
player_1=[50,195,player_width,player_height]
player_1_speed=3




#coordenadas y velocidad player 2

#x,y,ancho,alto
player_2=[750,195,player_width,player_height,0]
player_2_speed=3



#coordenadas pelota

ball_position=[395,300]
ball_movement=[3,3]

game_over=False

while not game_over:

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
                game_over=True
##-------------------SALIDA-----------------##

    # CAptura del teclado 

    keys=pygame.key.get_pressed()



    #Zona de logica -----------------------------------------------------------------------

    #Movimiento del jugador 

    if keys[pygame.K_w] and player_1[1]>0:
        player_1[1]-=player_1_speed
    if keys[pygame.K_s]and player_1[1]<390:
        player_1[1]+=player_1_speed

    if keys[pygame.K_o] and player_2[1]>0:
        player_2[1]-=player_1_speed
    if keys[pygame.K_l]and player_2[1]<390:
        player_2[1]+=player_2_speed
    #pelota

    #cambio de color

    if ball_position[0] < 400:
        ball_color=yellow
    else:
        ball_color=pink


    #si la pelota toca borde superior o inferior

    if ball_position[1] > 470 or ball_position[1] < 10 :
        ball_movement[1]*=-1
    
    #si la pelota sale de pantalla

    if ball_position[0] > 790:
        ball_position=[400,240]
        ball_movement[0]*=-1
        score_1+=1
    if ball_position[0] < 10:
        ball_position=[400,240]
        ball_movement[0]*=-1
        score_2+=1

    #por ultimo realizamos el movimiento

    ball_position[0]+=ball_movement[0]
    ball_position[1]+=ball_movement[1]

    #zona de logica ---------------------------------------------------------------------------



    screen.fill((39, 25, 89))
    #zona de dibujo


    
    
    player_1_render=pygame.draw.rect(screen,pink,(player_1[0],player_1[1],player_1[2],player_1[3]))
    player_2_render=pygame.draw.rect(screen,yellow,(player_2[0],player_2[1],player_2[2],player_2[3]))
    for y in range(5,595,5):
        pygame.draw.rect(screen,white,(395,y,1,2))

    ball_render=pygame.draw.circle(screen,ball_color,ball_position,10)

    Marcador()

    #colisiones

    if ball_render.colliderect(player_1_render):
        if ball_position[0]>70:
            ball_movement[0]*=-1
            ball_position[0]+=7
        else:
            ball_movement[1]*=-1
            if ball_movement[1]<0:
                ball_position[1]-=5
            else:
                ball_position[1]+=5
    
    
    if ball_render.colliderect(player_2_render):
        if ball_position[0]<756:
            ball_movement[0]*=-1
            ball_position[0]-=7
        else:
            ball_movement[1]*=-1
            if ball_movement[1]<0:
                ball_position[1]-=5
            else:
                ball_position[1]+=5
                


    
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
