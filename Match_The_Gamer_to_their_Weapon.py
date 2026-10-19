#COLLIDERECT(Between TWO rectangles) VS COLLIDEPOINT
import pygame, os, random
pygame.init()
running = True
WIDTH = 700
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Match The Logo")
w = os.path.join("images","wizard.png")
a = os.path.join("images","archer.png")
n = os.path.join("images","ninja.jpg")
wi = pygame.image.load(w)
ar = pygame.image.load(a)
ni = pygame.image.load(n)
wizard = pygame.transform.scale(wi,(50,50))
archer = pygame.transform.scale(ar,(50,50))
ninja = pygame.transform.scale(ni,(50,50))
screen.fill((255,255,255))
screen.blit(wizard,(150,100))
screen.blit(archer,(150,300))
screen.blit(ninja,(150,500))
font1 = pygame.font.SysFont("Times New Roman",45)
black = (0,0,0)
#Make these words shuffled.
wiz = font1.render("Wand",True,black)
arch = font1.render("Bow",True,black)
nin = font1.render("Shuriken",True,black)
screen.blit(wiz,(300,100))
screen.blit(arch,(300,300))
screen.blit(nin,(300,500))
pygame.display.update()
wizr = pygame.Rect(300,100,100,50)
archr = pygame.Rect(300,300,100,50)
ninr = pygame.Rect(300,500,100,50)
wizardr = pygame.Rect(150,100,50,50)
archerr = pygame.Rect(150,300,50,50)
ninjar = pygame.Rect(150,500,50,50)
start_pos = None
end_pos = None
dragging = False
images = [(wizardr,wizr),(archerr,archr),(ninjar,ninr)]
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:#Programs what happens when you click the top right cross.
            running = False
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button==1:
                pos = event.pos
                for i_r,w_r in images:
                    if i_r.collidepoint(pos):
                        start_pos = i_r.center
                        dragging = True
                        break
            '''pos = pygame.mouse.get_pos()
            pygame.draw.circle(screen,(black),(pos),20,0)'''
            pygame.display.update()
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button==1 and dragging:
                end_pos = event.pos
                correct = False
                for i_r,w_r in images:
                      if i_r.collidepoint(start_pos):
                        if w_r.collidepoint(end_pos):
                            correct=True
                            break
                if correct:
                     colour = (0,255,0)
                else:
                     colour = (255,0,0)
                pygame.draw.line(screen,colour,start_pos,end_pos,5)
                '''pos2 = pygame.mouse.get_pos()
            pygame.draw.line(screen,black,pos,pos2,5)
            pygame.draw.circle(screen,black,pos,20,0)'''
                pygame.display.update()
                dragging = False
                start_point = None
                end_point = None
    '''if wizr.colliderect(pos2) and wizardr.colliderect(pos):
        pygame.draw.line(screen,(0,255,0),(pos),(pos2),5)
    elif archr.colliderect(pos2) and archerr.colliderect(pos):
            pygame.draw.line(screen,(0,255,0),(pos),(pos2),5)
    elif ninr.colliderect(pos2) and ninjar.colliderect(pos):
            pygame.draw.line(screen,(0,255,0),(pos),(pos2),5)'''
            
    