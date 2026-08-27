import pygame,os,time
pygame.init()
running = True
WIDTH = 700
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Pong")
rb = os.path.join("images","bluerect.png")
rr = os.path.join("images","redrect.jpg")
rectb = pygame.image.load(rb)
rectr = pygame.image.load(rr)
rectwidth = 10
rectheight = 50
rectblue = pygame.transform.scale(rectb,(rectwidth,rectheight))
rectred = pygame.transform.scale(rectr,(rectwidth,rectheight))
rectrednew = pygame.transform.rotate(rectred,90)
rectbluenew = pygame.transform.rotate(rectblue,90)
font1 = pygame.font.SysFont("Times New Roman",45)
winnertext = pygame.font.SysFont("Times New Roman",70)
rectvelocity = 5
white = (255,255,255)
def draw_window(red_health,blue_health):
    healthtexty = font1.render(("Health: "+str(blue_health)),True,white)
    healthtextr = font1.render(("Health: "+str(red_health)),True,white)
