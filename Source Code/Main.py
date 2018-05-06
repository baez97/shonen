# -*- coding: utf-8 -*-
import pygame, sys
from pygame.locals import *
from Ente          import *
from Direccion     import *
from Variables     import *
from FactoryMethod import *

pygame.init()
factoria = FactoryMethod()
pj = factoria.crearPersonaje(10, 100, factoria.crearDerecha(), DISPLAY_WIDTH, DISPLAY_HEIGHT)

# Main loop
while True:
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(pj.currentImg, pj.img_rect)
    pj.avanza()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                pj.direccion = Izquierda()
                pj.avanza()
            elif event.key == K_RIGHT:
                pj.direccion = Derecha()
                pj.avanza()

    pygame.display.update()
   
    fpsClock.tick(FPS)

    


        
        