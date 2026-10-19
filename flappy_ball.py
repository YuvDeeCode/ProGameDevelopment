import pygame,random
pygame.init()
running = True
WIDTH = 850
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("FLAPPY BALL")
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
    pygame.draw.circle(screen,white,ball_x,ball_y,ball_radius)
    
                

        