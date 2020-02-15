#lets define some beautiful colours
black = [0,0,0]
white = [255,255,255]
blue= [0,0,255]
red = [200,0,0]
light_red = [255,0,0]
green = [0,170,0]
light_green = [0,255,0]
light_pink = [255,182,193]

#lets define some lovely fonts
import pygame
pygame.init()

tinyfont = pygame.font.SysFont('comicsansms', 15)
smallfont = pygame.font.SysFont("comicsansms",25)
medfont = pygame.font.SysFont("comicsansms",50)
largefont = pygame.font.SysFont("comicsansms",20)
superlargefont = pygame.font.SysFont("comicsansms",30)

#lets define the sizes

display_width=1100
display_height=500

size=[display_width,display_height]
screen=pygame.display.set_mode(size)
clock=pygame.time.Clock()
FPS=5

#lets write some wonderful functions

def text_objects(text,color,size):
    if size == "superlarge":
        textSurface = superlargefont.render(text,True,color)
    elif size == "large":
        textSurface = largefont.render(text,True,color)
    return textSurface,textSurface.get_rect()
   
def message_to_screen(msg,color,x_displace = 0, y_displace=0,size="large"):
    textSurf, textRect = text_objects(msg,color,size)
    textRect = x_displace, y_displace
    screen.blit(textSurf,textRect)
   
def valentine():
    count = 0
    colours = [black, green, red]
    valentine_ = True
    while valentine_:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill(light_pink)
        count += 1      
        if count%2 == 0:
            sel_color = colours[0]
        elif count%3 == 0:
            sel_color = colours[1]
        else:
            sel_color = colours[2]      
        message_to_screen("For the love of Code, Happy 1524th Valentine's Day!",sel_color,140,100,"superlarge")
        message_to_screen("It has been 1751 years since the death of St.Valentine,",sel_color,120,170,"superlarge")
        message_to_screen("the saint who performed weddings for soldiers forbidden to marry!",sel_color,70,240,"superlarge")
        message_to_screen("The remembrance of whom of what we call the day of romance.",sel_color,90,310,"superlarge")
        message_to_screen("Today, the 14th of February!",sel_color,310,380,"superlarge")
        pygame.display.update()
        clock.tick(FPS)
		
    pygame.quit()
    quit()		



#lets call that main valentine over there, he's gonna do everything for us
valentine()
