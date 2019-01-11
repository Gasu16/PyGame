# Random pixels on the screen

import pygame
from pygame.locals import *
import random

pygame.init()


#### IMAGE ####
img = pygame.image.load('rsz_1danganronpagifend.gif')

white = (255,255,255)
blue = (0,0,255)

width = 640
height = 480

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True
timer = 1000

#pygame.draw.rect(screen,blue,(200,150,100,50))
img_x = 140
img_y = 0

while running:
    if timer > 0:
        img_y+=0.1
        timer-=1
        print(timer)
    x = random.randint(0, width-1)
    y = random.randint(0, height-1)
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    screen.set_at((x, y), (red, green, blue))
    screen.blit(img,(img_x,img_y))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            if event.key == K_RETURN:
                print("START")
                
#    pygame.display.update()
    pygame.display.flip()
    clock.tick(240)


pygame.quit()


