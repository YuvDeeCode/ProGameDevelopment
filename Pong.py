import pygame,os,time
pygame.init()
running = True
WIDTH = 700
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Pong")
pb = os.path.join("images","pong_ball.png")
rb = os.path.join("images","bluerect.png")
rr = os.path.join("images","redrect.jpg")
bg = os.path.join("images","rocket_bg.png")
pongb = pygame.image.load(rb)
rectb = pygame.image.load(rb)
rectr = pygame.image.load(rr)
background = pygame.image.load(bg)
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
ball_vel_x = 2
ball_vel_y = 2
fps = 60


def draw_window(red_health,blue_health,red,blue,ball):
    screen.blit(background,(0,0))
    healthtextb = font1.render(("Health: "+str(blue_health)),True,white)
    healthtextr = font1.render(("Health: "+str(red_health)),True,white)
    screen.blit(healthtextb,(10,20))
    screen.blit(healthtextr,(650,20))
    screen.blit(rectrednew,(red.x,red.y))
    screen.blit(rectbluenew,(blue.x,blue.y))
    screen.blit(pongb,(ball.x,ball.y))
    pygame.draw.circle(screen,(255,0,255),ball.x,ball.y,20)
    pygame.display.update()

def blue_movement(keyspressed,blue):
    if keyspressed[pygame.K_s] and blue.y + rectvelocity + rectheight <HEIGHT - 50:
            blue.y+=rectvelocity
    if keyspressed[pygame.K_w] and blue.y - rectvelocity >0:
            blue.y-=rectvelocity

def red_movement(keyspressed,red):
    if keyspressed[pygame.K_UP] and red.y + rectvelocity + rectheight <HEIGHT - 50:
            red.y+=rectvelocity
    if keyspressed[pygame.K_DOWN] and red.y - rectvelocity >0:
            red.y-=rectvelocity

'''def ball_handling(red,blue,ball):
    ball.x+=ball_vel_x
    ball.y+=ball_vel_y
    #if ball.x > WIDTH or ball.x<0:
     #     ball.x*=-1
    if ball.y > HEIGHT or ball.y<0:
          ball_vel_y*=-1
    #Collision Program'''


def winnertext(winnert):
    winnertext.render(str(winnert)+" wins!")

def main():
    red = pygame.Rect(600,300,rectwidth,rectheight)
    blue = pygame.Rect(100,300,rectwidth,rectheight)
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

        keyspressed = pygame.key.get_pressed()
        red_movement(keyspressed,red)
        blue_movement(keyspressed,blue)
        pygame.display.update()
main()
                      

                        

