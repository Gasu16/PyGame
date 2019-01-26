import pygame
from pygame.locals import *
import random



pygame.init()

#### FILE MP3 ####
# SETTIAMO LA MUSICA DEL MENU'
filemp3 = 'DanganRonpaTheAnimationEnding.mp3'
pygame.mixer.init()
pygame.mixer.music.load(filemp3)
pygame.mixer.music.play()

#### IMAGE ####
# METTIAMO L'IMMAGINE INIZIALE CHE SCORRE
img = pygame.image.load('rsz_1danganronpagifend.gif')

white = (255,255,255)
blue = (0,0,255)

width = 640
height = 480

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True
timer = 2000

#pygame.draw.rect(screen,blue,(200,150,100,50))
img_x = 140
img_y = 0

class Player(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self) # Call sprite initializer
		self.image = pygame.image.load("play1.png").convert()
		self.Rpos = self.image.get_rect()
		self.Rpos.x = 0
		self.Rpos.y = 330
	
	def __walk__(self):
		key = pygame.key.get_pressed()
		dist = 1

		if key[pygame.K_LEFT]:
			self.Rpos.x -= dist
		if key[pygame.K_RIGHT]:
			self.Rpos.x += dist
		if key[pygame.K_UP]:
			self.Rpos.y -= dist
		if key[pygame.K_DOWN]:
			self.Rpos.y += dist
		
# QUANDO VIENE PREMUTO INVIO E INIZIA IL GIOCO VERO E PROPRIO
def funz():
    #pygame.init()
    P = Player()
    #### SET THE SCREEN ####
    img = pygame.image.load('screengioco.png')
    #image = pygame.image.load("play.png").convert()
    #WHITE = (255, 255, 255)
    #image.set_colorkey(WHITE)
    #rect = image.get_rect()
    width = 640
    height = 480
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    run = True
    P.__init__()
    
    while run:
        screen.blit(img, (0,0))
        screen.blit(P.image, (P.Rpos.x, P.Rpos.y))
        
        P.__walk__()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False
        pygame.display.flip()
        clock.tick(240)

# AVVIO DEL GIOCO (SCHERMATA MENU')
while running:
    if timer > 0:
        img_y+=0.05
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
                running = False
                pygame.mixer.music.stop()
                funz()
                
#    pygame.display.update()
    pygame.display.flip()
    clock.tick(240)



#G = Gioco()
#G.__init__()
pygame.quit()
