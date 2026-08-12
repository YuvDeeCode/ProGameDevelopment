import pygame,os,time
pygame.init()
running = True
WIDTH = 700
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Space Invaders")
sy = os.path.join("images","yellow_spaceship.png")
sr = os.path.join("images","red_spaceship.png")
bg = os.path.join("images","rocket_bg.png")
spaceshipy = pygame.image.load(sy)
spaceshipr = pygame.image.load(sr)
background = pygame.image.load(bg)
spaceshipwidth = 55
spaceshipheight = 40
yellowspaceship = pygame.transform.scale(spaceshipy,(spaceshipwidth,spaceshipheight))
redspaceship = pygame.transform.scale(spaceshipr,(spaceshipwidth,spaceshipheight))
yellowspaceshipnew = pygame.transform.rotate(yellowspaceship,90)
redspaceshipnew = pygame.transform.rotate(redspaceship,270)
white = (255,255,255)
yellow_colour = (255,255,0)
red_colour = (255,0,0)
black = (0,0,0)
font1 = pygame.font.SysFont("Times New Roman",45)
maxbullets = 3
bulletvelocity = 7
shipvelocity = 5
winnertext = pygame.font.SysFont("Times New Roman",70)
border = pygame.Rect(345,0,10,700)
def draw_window(red,yellow,red_bullets,yellow_bullets,red_health,yellow_health):
    screen.blit(background,(0,0))
    pygame.draw.rect(screen,black,border)
    healthtexty = font1.render(("Health: "+str(yellow_health)),True,white)
    healthtextr = font1.render(("Health: "+str(red_health)),True,white)

    