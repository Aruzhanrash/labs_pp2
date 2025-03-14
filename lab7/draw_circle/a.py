import pygame
pygame.init()
screen=pygame.display.set_mode((400, 300))
done=False
x=200
y=150
step=20
radius=25
clock=pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    screen.fill((255,255,255))
    pygame.draw.circle(screen,(255,0,0),(x,y),radius)
    pressed=pygame.key.get_pressed()
    if pressed[pygame.K_UP] and y - step - radius >= 0:
        y -=step
    if pressed[pygame.K_DOWN] and y + step + radius <= 300:
        y +=step
    if pressed[pygame.K_LEFT]and x - step - radius >= 0:
        x -=step
    if pressed[pygame.K_RIGHT] and x + step + radius <= 400:
        x +=step
    pygame.display.flip()
    clock.tick(60)