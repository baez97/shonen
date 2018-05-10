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

# Main loop
while True:
    DISPLAYSURF.fill(WHITE)
    pj.pintar()
    pj.avanza()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                pj.estado = MovingLeft(pj)
                pj.avanza()
            elif event.key == K_RIGHT:
                pj.estado = MovingRight(pj)
                pj.avanza()
            elif event.key == K_UP:
                pj.estado = MovingUp(pj)
                pj.avanza()
            elif event.key == K_DOWN:
                pj.estado = MovingDown(pj)
                pj.avanza()

        elif event.type == KEYUP:
            if pj.estado.isUp() and event.key ==K_UP:
                pj.estado = Parado(pj)
            elif pj.estado.isDown() and event.key ==K_DOWN:
                pj.estado = Parado(pj)
            elif pj.estado.isRight() and event.key ==K_RIGHT:
                pj.estado = Parado(pj)
            elif pj.estado.isLeft() and event.key ==K_LEFT:
                pj.estado = Parado(pj)
            

    pygame.display.update()
   
    fpsClock.tick(FPS)

    


        
        