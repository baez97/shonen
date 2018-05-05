# -*- coding: utf-8 -*-
import pygame, sys
from pygame.locals import *
from Personaje     import *
from Direccion     import *
from Variables     import *

pygame.init()

pj = Personaje(100, 100, Derecha(), DISPLAY_WIDTH, DISPLAY_HEIGHT)

# Main loop
while True:
    DISPLAYSURF.fill(WHITE)
    pj.avanza()
    DISPLAYSURF.blit(pj.pj_img, pj.pj_img_rect)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
   
    fpsClock.tick(FPS)

    


        
        