import pygame
pygame.init()
WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("SHAPES PYGAME")
white = (255,255,255)
black = (0,0,0)
screen.fill(white)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(white)
    pygame.draw.rect(screen,black,(100,100,150,100))
    pygame.draw.rect(screen,black,(200,200,100,200),5)
    pygame.draw.circle(screen,black,(400,300),50)
    pygame.draw.circle(screen,black,(200,500),60,5)
    pygame.draw.line(screen,black,(500,500),(600,600))
    pygame.draw.line(screen,black,(400,400),(700,400),5)
    pygame.display.update()
#pygame.quit() Not needed necessarily as there is also line 12-14.
 