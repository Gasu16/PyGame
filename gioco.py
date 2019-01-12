import pygame
from pygame.locals import *



def funz():
    pygame.init()

    #### SET THE SCREEN ####
    img = pygame.image.load('screengioco.png')

    width = 640
    height = 480
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    run = True

    while run:
        screen.blit(img, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False
        pygame.display.flip()
        clock.tick(240)

#G = Gioco()
#G.__init__()
pygame.quit()
