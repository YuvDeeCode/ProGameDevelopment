import pygame, os, time
pygame.init()
WIDTH = 700
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("One Direction: UP")
bg = os.path.join("images","rocket_bg.png")#Do you need this step, or can you just go straight to image.load as it shows just image.load in the notes?
r = os.path.join("images","rocket.png")
background = pygame.image.load(bg)
rocket = pygame.image.load(r)
rx = 350
ry = 350
up = False
while ry<700:
    screen.blit(background,(0,0))
    screen.blit(rocket,(rx,ry))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                #up = True#Why can you not give ry-=10 here?
                if ry>0:
                    ry -= 10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                #up = False
                ry+=2.5
    #if up == True:#Can you just say if up. If so, why is that?
        '''if ry>0:
            ry -= 10
    ry+=2.5'''
    time.sleep(0.05)
print("Game Over")
