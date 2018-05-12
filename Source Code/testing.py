import pygame, sys
from pygame.locals import *

pygame.init()
FPS = 30
DISPLAYSURF = pygame.display.set_mode((600, 400))
fpsClock = pygame.time.Clock()
block = pygame.image.load('images/Plain_Block.png')
pj = pygame.image.load('images/parado.gif')
while True:

    DISPLAYSURF.fill((255, 255, 255))
    
    for j in range(0, 560, 50):
        for i in range(0, 321, 40):
            DISPLAYSURF.blit(block, (j,i))
    DISPLAYSURF.blit(pj, (100, 100))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
fpsClock.tick(FPS)

