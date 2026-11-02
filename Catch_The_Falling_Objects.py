import pygame,random
pygame.init()
running = True
WIDTH = 600
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Catch The Falling Objects Game")
fps = 20
timer = pygame.time.Clock()#Helps keep track of the frame rate etc.
score = 0


#COLOURS:
blue = (0,0,255)
green = (0,255,0)
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)



#BASKET
basket_x = WIDTH/2
basket_y = HEIGHT-100
basket_height = 25
basket_width = 50
basket = pygame.Rect(basket_x,basket_y,basket_width,basket_height)
#OBJECTS
object_y = 0
object_vel = random.randint(3,5)
#You could add acceleration due to gravity to make the simulation more realistic.
object_x = random.randint(10,WIDTH-10)
#GAME LOOP
while running:
    screen.fill(green)
    basket = pygame.Rect(basket_x,basket_y,basket_width,basket_height)
    mouse_x,mouse_y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == pygame.MOUSEMOTION:
            basket_x = mouse_x
    pygame.draw.rect(screen,red,basket)
    object_y+=object_vel
    pygame.draw.circle(screen,blue,(object_x,object_y),10)
    if object_y == HEIGHT:
        print("GAME_OVER")
        print("Score: "+str(score))
        pygame.quit()
    if object_y == basket_y+basket_height and basket_x<object_x<basket_x+basket_width:
        score+=1
        object_y*=-1#This is just a check to see if the object and the basket actually collide.
    pygame.display.update()
    timer.tick(fps)



