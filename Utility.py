import pygame,sys
pygame.init()

logo=pygame.image.load("GGM.png")
logo=pygame.transform.smoothscale(logo,(70.5,67.6))

screen_size=(800,580)
screen=pygame.display.set_mode(screen_size)
scoreboard_size=100

black=(0,0,0)
white=(255,255,255)
pink=(242, 39, 171)
purple=(108,48,191)
darkPurple=(39,25,89)
yellow=(242, 208, 39)
blue=(27,181,242)

colors=[black,white,pink,purple,yellow,blue]

font=pygame.font.SysFont(None,70)


#/////////////////////////// Funciones \\\\\\\\\\\\\\\\\\\\\\\\\\\\\

def DrawBox(color,x,y,width,height):

    return pygame.draw.rect(screen,color,(x,y,width,height))
    

def DrawRound(r,color,x,y): 
    
    return pygame.draw.circle(screen,color,(x,y),r)
    

def Write(text,font,color,surface,x,y,size=0,bezel=(False,0)):
    if size!=0:
        font=pygame.font.SysFont(None,size)
    if bezel[0]:
        Write(text,font,black,surface,x,y+bezel[1],size)
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
    center=0
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
    
    def Box(self,width=50,height=50,color=(0,0,0)):
        self.collider=DrawBox(color,self.x,self.y,width,height)
        self.width=width
        self.height=height

    def round(self,r=50,color=(0,0,0)):
        self.r=r
        self.collider=DrawRound(self.r,color,self.x,self.y)
        self.center=self.collider.center
        

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
        

        