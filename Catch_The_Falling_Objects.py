import pygame,random
pygame.init()
running = True
WIDTH = 600
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Catch The Falling Objects Game")
fps = 60
timer = pygame.time.Clock()#Helps keep track of the frame rate etc.


#COLOURS:
blue = (0,0,255)
green = (0,255,0)
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

#OBJECTS
object_x = 0
object_y = random.randint(10,WIDTH-10)
object_vel = random.randint(5,15)
#You could add acceleration due to gravity to make the simulation more realistic.

#BASKET
basket_x = WIDTH/2
basket_y = HEIGHT-20
basket = pygame.Rect(basket_x,basket_y,50,25)

#GAME LOOP
while running:
    screen.fill(green)
    timer.tick(fps)
    basket = pygame.Rect(basket_x,basket_y,50,25)
    mouse_x,mouse_y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:#Not working
            running = False
            pygame.quit()
        if event.type == pygame.MOUSEMOTION:
            basket_x = mouse_x
            pygame.draw.rect(screen,red,basket)
    pygame.display.update()



