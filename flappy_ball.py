import pygame,random
pygame.init()
running = True
WIDTH = 850
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("FLAPPY BALL")
fps = 20
clock = pygame.time.Clock()
#COLOURS:
blue = (0,0,255)
green = (0,255,0)
black = (0,0,0)
white = (255,255,255)

#BALL:
ball_x = 50
ball_y = HEIGHT//2
ball_radius = 20
ball_vel = 0
gravity = 0.5
bounce_strength = -8

#PIPE:
pipe_width = 50
pipe_gap = 150
pipe_x = WIDTH
pipe_height = random.randint(100,400)

#GAME LOOP

while running:
    screen.fill(blue)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                ball_vel = bounce_strength
    ball_vel+=gravity
    ball_y+=ball_vel
    pygame.draw.circle(screen,white,(ball_x,int(ball_y)),ball_radius)
    pipe_x -= 4
    if pipe_x + pipe_width < 0:
        pipe_x = WIDTH
        pipe_height = random.randint(100,400)
    pygame.draw.rect(screen,green,(pipe_x,0,pipe_width,pipe_height))
    pygame.draw.rect(screen,green,(pipe_x,pipe_height+pipe_gap,pipe_width,HEIGHT))
    if ball_y - ball_radius <= 0 or ball_y+ball_radius >= HEIGHT or (pipe_x<ball_x+ball_radius<pipe_x+pipe_width and (ball_y<pipe_height or ball_y>pipe_height+pipe_gap)):
        print("GAME OVER")
        pygame.time.delay(1000)
        ball_vel = 0
        ball_x = 50
        ball_y = HEIGHT//2
        pipe_x = WIDTH
        pipe_height = random.randint(100,400)
        #Try quitting after collision as well to deeper understand collision conditions.
    pygame.display.update()
    clock.tick(fps)
    
                

        