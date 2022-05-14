from cgitb import reset
from nbformat import write
import pygame,sys
pygame.init()

#/\/\/\/\/\/\/\/\/\/\/\/\/\/\esenciales\/\/\/\/\/\/\/\/\/\/\/\/\/
screen_size=(800,580)
screen=pygame.display.set_mode(screen_size)
scoreboard_size=100
clock = pygame.time.Clock()
game_finish=False
#\/\/\/\/\/\/\/\/\/\/\/\/\/\esenciales\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/

#//////////////////////////Visuales\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
black=(0,0,0)
white=(255,255,255)
pink=(242, 39, 171)
purple=(108,48,191)
darkPurple=(39,25,89)
yellow=(242, 208, 39)
blue=(27,181,242)
font=pygame.font.SysFont(None,70)
font2=pygame.font.SysFont(None,70)



#////////////////////Funciones\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

def DrawBox(color,x,y,width,height):

    return pygame.draw.rect(screen,color,(x,y,width,height))
    

def DrawRound(r,color,x,y):
    return pygame.draw.circle(screen,color,(x,y),r)
    

def Write(text,font,color,surface,x,y):
    
    textobj=font.render(text,True,color)
    textrect=textobj.get_rect()
    textrect.topleft=(x,y)
    surface.blit(textobj,textrect)



    


    

#/////////////////////////Clases\\\\\\\\\\\\\\\\\\\\\\\\
class Gameobject():
    
    form=0
    init_position=[0,0]
    pygame=pygame
    collider=0
    width=0
    height=0
    x=0
    y=0
    r=0

    def __init__(self,x,y):
        self.x=x
        self.y=y 
        self.init_position=[x,y]

    def rest_position(self):
        self.x=self.init_position[0]
        self.y=self.init_position[1]
    
    def Box(self,width=50,height=50,color=white):
        self.collider=DrawBox(color,self.x,self.y,width,height)

    def round(self,r=50,color=white):
        self.r=r
        self.collider=DrawRound(self.r,color,self.x,self.y)



class Scoreboard:


    scr_1=0
    scr_2=0
    win=0
    def __init__(self,winpoints):
        self.win=winpoints
        pass
    


    def point(self,jugador):
        if jugador<(screen_size[0]/2):
            self.scr_2+=1
        else:
            self.scr_1+=1

    def draw(self,scoreboard_size):
        DrawBox(purple,0,0,screen_size[0],scoreboard_size)
        DrawBox(yellow,0,90,screen_size[0],10)
        DrawBox(darkPurple,(screen_size[0]/2)-79,30,158,50)
        DrawBox(purple,(screen_size[0]/2)-5,52.5,10,5)
        text=str(self.scr_1)
        text="{:0>2}".format(text)
        Write(text,font,purple,screen,(screen_size[0]/2)-69,33)
        text2=str(self.scr_2)
        text2="{:0>2}".format(text2)
        Write(text2,font,purple,screen,(screen_size[0]/2)+12,33)

    def Winer(self):
        if self.scr_1>=self.win or self.scr_2 >=self.win:
            return True
        else:
            return False

class Flicker:

    on=0
    off=0
    reset=0
    flick=0

    def __init__(self,on,off):
        self.on=on
        self.off=off
        self.reset=self.on+self.off

    def Timmer(self):


        self.flick+=1

        if self.flick>=self.reset:
            self.flick=0
        elif self.flick<=self.on:
            return True
        elif self.flick>self.off:
            return False
        

        



#/////////////////////Variables\\\\\\\\\\\\\\\\\\\\\\\\\\\

player_width=15
player_height=90
ball_r_init=5
speed_player=5
speed_ball=[3,3]
winner=0


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
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
                game_finish=True

    screen.fill(darkPurple)

    Write("Pong Pygame ",font2,white,screen,220,30)
    Write("Pong Pygame ",font2,white,screen,220,30)






















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

    player.Box(player_width,player_height,pink)
    player2.Box(player_width,player_height,blue)
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