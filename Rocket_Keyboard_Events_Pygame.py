import pygame, os, time
pygame.init()
running = True
WIDTH = 700
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Rocket Moving")
bg = os.path.join("images","rocket_bg.png")
r = os.path.join("images","rocket.png")
background = pygame.image.load(bg)
rocket = pygame.image.load(r)
rx = 350
ry= 350
keys = [False,False,False,False]
while ry<700:#Main condition. Window dissolves when this is not obeyed. Hence, we can only display Game_Over in the terminal with this logic. Maybe it could work if you had while running = true and then you change the variable running to false after you show the game over screen.
    screen.blit(background,(0,0))
    screen.blit(rocket,(rx,ry))
    pygame.display.update()
    for event in pygame.event.get():#Checking between all events
        if event.type == pygame.QUIT:#If the event is quit,
            pygame.quit()#then quit.
        if event.type == pygame.KEYDOWN:#All events which involve a key being pressed.
            if event.key == pygame.K_UP: #If key up.
                keys[0] = True
            elif event.key == pygame.K_LEFT:
                keys[1]= True
            elif event.key == pygame.K_DOWN:
                keys[2] = True
            elif event.key == pygame.K_RIGHT:
                keys[3] = True
        if event.type == pygame.KEYUP:#All events which involve a key not being pressed/releasing the key.
            if event.key == pygame.K_UP:
                keys[0] = False
            elif event.key == pygame.K_LEFT:
                keys[1] = False
            elif event.key == pygame.K_DOWN:
                keys[2] = False
            elif event.key == pygame.K_RIGHT:
                keys[3] = False
    if keys[0]:
        if ry>0:
            ry -= 10
    if keys[2]:
        if ry<700:
            ry += 10
    if keys[1]:
        if rx>0:
            rx -= 10
    if keys[3]:
        if rx<650:
            rx += 10
    ry += 2.5
    time.sleep(0.05)
'''font = pygame.font.SysFont("Times New Roman",100)
text = font.render("GAME OVER",True,(255,0,0))
screen.blit(text,(350,350))'''   
print("Game_Over")
    