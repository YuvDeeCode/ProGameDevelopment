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
pongb = pygame.image.load(pb)
rectb = pygame.image.load(rb)
rectr = pygame.image.load(rr)
background = pygame.image.load(bg)
pongball = pygame.transform.scale(pongb,(20,20))
rectwidth = 10
rectheight = 50
rectrednew = pygame.transform.rotate(rectr,90)
rectbluenew = pygame.transform.rotate(rectb,90)
rectblue = pygame.transform.scale(rectbluenew,(rectwidth,rectheight))
rectred = pygame.transform.scale(rectrednew,(rectwidth,rectheight))
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
    screen.blit(rectred,(red.x,red.y))
    screen.blit(rectblue,(blue.x,blue.y))
    screen.blit(pongball,(ball.x,ball.y))
    #pygame.draw.circle(screen,(255,0,255),ball.x,ball.y,20)
    pygame.display.update()

def blue_movement(keyspressed,blue):
    if keyspressed[pygame.K_s] and blue.y + rectvelocity + rectheight <HEIGHT - 50:
            blue.y+=rectvelocity
    if keyspressed[pygame.K_w] and blue.y - rectvelocity >0:
            blue.y-=rectvelocity

def red_movement(keyspressed,red):
    if keyspressed[pygame.K_DOWN] and red.y + rectvelocity + rectheight <HEIGHT - 50:
            red.y+=rectvelocity
    if keyspressed[pygame.K_UP] and red.y - rectvelocity >0:
            red.y-=rectvelocity

     
def ball_handling(ball):
    global ball_vel_x
    global ball_vel_y
    ball.x+=ball_vel_x
    ball.y+=ball_vel_y
    if ball.x > WIDTH or ball.x<0:
          ball_vel_x*=-1
    if ball.y > HEIGHT or ball.y<0:
          ball_vel_y*=-1

def ball_collision(red,ball,blue): # Remember to call this and all functions.
    #Collision Program
    global ball_vel_x
    global ball_vel_y
    if ball.colliderect(red) and ball_vel_x > 0:
         ball_vel_x*= -1
         ball.right = red.left
    if ball.colliderect(blue) and ball_vel_x < 0:
         ball_vell_x*=-1
         ball.left = blue.right
    

def winnertextfunc(winnert):
    winnertext.render(str(winnert)+" wins!")

def main():
    red = pygame.Rect(600,300,rectwidth,rectheight)
    blue = pygame.Rect(100,300,rectwidth,rectheight)
    ball = pygame.Rect(300,300,30,30)
    red_health = 10
    blue_health = 10
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
        winnert = ""
        if red_health<=0:
            winnert = "Blue"
        elif blue_health<=0:
            winnert = "Red"
            if winnert != "":
                winnertextfunc(winnert)
                break
        keyspressed = pygame.key.get_pressed()
        draw_window(red_health,blue_health,red,blue,ball)
        red_movement(keyspressed,red)
        blue_movement(keyspressed,blue)
        ball_handling(ball)
        ball_collision(red,ball,blue)
        pygame.display.update()
main()
                      

                        

