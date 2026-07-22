import pygame
pygame.init()
running = True
WIDTH = 700
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("SNOWMAN PYGAME")
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
class shapes:
    def __init__(self,colour,coord1,coord2,radius,border):
        self.colour = colour
        self.coord1 = coord1
        self.coord2 = coord2
        self.radius = radius
        self.border = border
    def circle(self):
        pygame.draw.circle(screen,self.colour,(self.coord1),self.radius,self.border)
    def line(self):
        pygame.draw.line(screen,self.colour,(self.coord1),(self.coord2),self.border)
shape1 = shapes(black,(350,500),0,200,5)
shape2 = shapes(black,(350,200),0,100,5)   
shape3 = shapes(blue,(310,200),0,20,5)    
shape4 = shapes(blue,(390,200),0,20,5)
shape5 = shapes(black,(320,250),(380,250),0,5)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(white)
    shape1.circle()
    shape2.circle()
    shape3.circle()
    shape4.circle()
    shape5.line()
    pygame.display.update()

