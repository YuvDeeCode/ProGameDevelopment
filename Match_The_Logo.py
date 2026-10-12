import pygame, os, random
pygame.init()
running = True
WIDTH = 700
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Match The Logo")
c = os.path.join("images","candycrush.jpg")
t = os.path.join("images","temple_run.png")
s = os.path.join("images","subway_surfers.png")
l = os.path.join("images","ludo.png")
images = [pygame.image.load(c),pygame.image.load(t),pygame.image.load(s),pygame.image.load(l)]
random.shuffle(images)
'''trun  = pygame.image.load(t)
subway = pygame.image.load(s)
ludo = pygame.image.load(l)'''
screen.fill((255,255,255))
#images = [candy,trun,subway,ludo]
#images = random.shuffle(images)#Random order at which images are placed.
screen.blit(images[0],(50,50))
screen.blit(images[1],(50,150))
screen.blit(images[2],(50,250))
screen.blit(images[3],(50,350))
font1 = pygame.font.SysFont("Times New Roman",45)
black = (0,0,0)
crush = font1.render("Candy Crush",True,black)
templerun = font1.render("Temple Run",True,black)
surfers = font1.render("Subway Surfers",True,black)
ldo = font1.render("Ludo",True,black)
screen.blit(crush,(200,50))
screen.blit(surfers,(200,150))
screen.blit(ldo,(200,250))
screen.blit(templerun,(200,350))
pygame.display.update()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:#Programs what happens when you click the top right cross.
            running = False
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            pygame.draw.circle(screen,(black),(pos),20,0)
            pygame.display.update()
        if event.type == pygame.MOUSEBUTTONUP:
            pos2 = pygame.mouse.get_pos()
            pygame.draw.line(screen,(black),(pos),(pos2),5)
            pygame.draw.circle(screen,(black),(pos),20,0)
            pygame.display.update()
            

