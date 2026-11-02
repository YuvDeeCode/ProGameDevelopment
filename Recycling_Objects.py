import pygame,random,os
pygame.init()
running=True
WIDTH = 900
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Recycling Objects")
timer = pygame.time.Clock()
fps = 20
score = 0

#COLOURS:
blue = (0,0,255)
red = (255,0,0)
green = (0,255,0)
black = (0,0,0)
white = (255,255,255)

#FONT(S):
font1 = pygame.font.SysFont("Times New Roman",20)

#IMAGES:
pe = os.path.join("images","pencil.png")
pa = os.path.join("images","paper_bag.png")
pl = os.path.join("images","plastic_bag.png")
w = os.path.join("images","wooden_box.png")
b = os.path.join("images","bin.png")
penc = pygame.image.load(pe)
paper = pygame.image.load(pa)
plastic = pygame.image.load(pl)
wooden = pygame.image.load(w)
bn = pygame.image.load(b)
bn_r = pygame.transform.scale(bn,(10,20))
paper_r = pygame.transform.scale(paper,(10,15))
plastic_r = pygame.transform.scale(plastic,(10,10))
bg = os.path.join("images","rocket_bg.png")
background = pygame.image.load(bg)

screen.blit("rocket.png",(WIDTH,HEIGHT))

#RECTANGLES:

bn_rect = pygame.Rect(30,30,10,20)
recyclable_items = [paper_r,wooden,penc]
non_recyclable = []
recyclable = []
for i in range(50):
    img = random.choice(recyclable_items)
    r = img.get_rect(x=random.randrange(900),y=random.randrange(700))
    recyclable.append((img,r))
for i in range(17):
    img = plastic_r
    r = img.get_rect(x=random.randrange(900),y=random.randrange(700))
    non_recyclable.append((img,r))

while running:
    timer.tick(fps)
    