# -*- coding: utf-8 -*-
import pygame, sys
from pygame.locals import *
from Ente          import *
from Direccion     import *
from Variables     import *
from FactoryMethod import *
from Estado import *

pygame.init()
factoria = FactoryMethod()
pj = factoria.crearPersonaje('Andy', 500, 100)
block = pygame.image.load('images/block.png')
grass = pygame.image.load('images/grass.png')

# Main loop
while True:
    DISPLAYSURF.fill(WHITE)
    
    for x in range(0, 560, 50):
        for y in range(60, 321, 40):
            DISPLAYSURF.blit(block, (x,y))
    for x in range(0, 600, 50):
        DISPLAYSURF.blit(grass, (x, 0))
    for y in range(40, 320, 40):
        DISPLAYSURF.blit(grass, (0, y))
    for y in range(40, 320, 40):
        DISPLAYSURF.blit(grass, (550, y))
    for x in range(0, 600, 50):
        DISPLAYSURF.blit(grass, (x, 320))
    
            
    pj.pintar()
    pj.avanza()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                pj.cambiarLeft()
                pj.avanza()
            elif event.key == K_RIGHT:
                pj.cambiarRight()
                pj.avanza()
            elif event.key == K_UP:
                pj.cambiarUp()
                pj.avanza()
            elif event.key == K_DOWN:
                pj.cambiarDown()
                pj.avanza()

        elif event.type == KEYUP:
            if pj.estado.isUp() and event.key ==K_UP:
                pj.cambiarParado()
            elif pj.estado.isDown() and event.key ==K_DOWN:
                pj.cambiarParado()
            elif pj.estado.isRight() and event.key ==K_RIGHT:
                pj.cambiarParado()
            elif pj.estado.isLeft() and event.key ==K_LEFT:
                pj.cambiarParado()
            

    pygame.display.update()
   
    fpsClock.tick(FPS)

    


        
        