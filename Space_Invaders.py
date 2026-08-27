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
    screen.blit(healthtexty,(10,20))
    screen.blit(healthtextr,(650,20))
    screen.blit(yellowspaceshipnew,(yellow.x,yellow.y))
    screen.blit(redspaceshipnew,(red.x,red.y))
    for bullet in red_bullets:
        pygame.draw.rect(screen,red_colour,bullet)
    for bullet in yellow_bullets:
        pygame.draw.rect(screen,yellow_colour,bullet)
    pygame.display.update()

def yellow_movement(keyspressed,yellow):
    if keyspressed[pygame.K_a] and yellow.x - shipvelocity >0:
        yellow.x-=shipvelocity
    if keyspressed[pygame.K_d] and yellow.x + shipvelocity + spaceshipwidth <border.x:
        yellow.x+=shipvelocity
    if keyspressed[pygame.K_s] and yellow.y + shipvelocity + spaceshipheight <HEIGHT - 15:
        yellow.y+=shipvelocity
    if keyspressed[pygame.K_w] and yellow.y - shipvelocity >0:
        yellow.y-=shipvelocity

def red_movement(keyspressed,red):
    if keyspressed[pygame.K_LEFT] and red.x - shipvelocity > border.x + 10:
        red.x-=shipvelocity
    if keyspressed[pygame.K_RIGHT] and red.x +shipvelocity +spaceshipwidth <WIDTH:
        red.x+=shipvelocity
    if keyspressed[pygame.K_DOWN] and red.y + shipvelocity + spaceshipheight < HEIGHT - 15:
        red.y+=shipvelocity
    if keyspressed[pygame.K_UP] and red.y - shipvelocity >0:
        red.y-=shipvelocity

def bullet_handling(yellow_bullets,red_bullets,yellow,red):
    for bullet in yellow_bullets:
        bullet.x+=bulletvelocity
        #
        #
    for bullet in red_bullets:
        bullet.x-=bulletvelocity
        #       
        #

def winnertext():
    