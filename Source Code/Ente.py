import pygame, sys
from pygame.locals import *
from Grafico import *
from Estado import *
from Variables import *

class Ente:

    def avanza(self):
        self.estado.avanza(self)

    def pintar(self):
        self.estado.pintar(self)
        
class Personaje(Ente):

    def __init__(self, nombre, x, y):
        self.imagenes = {'parado':'images/parado.gif', 'left':'images/left.png', 'right':'images/right.png', 'up':'images/up.png', 'down':'images/down.png'}
        self.nombre  = nombre
        self.pos_x   = x
        self.pos_y   = y
        self.estado  = Parado(self)
        self.rect    = self.estado.getImage().get_rect()
        self.rect.move((x,y))

    def avanzaRight(self):
        if(self.pos_x + 20 < 400):
            self.estado.cambiarDerecha()

    def pintar(self):
        DISPLAYSURF.blit(self.estado.getImage(), (self.pos_x, self.pos_y))

    def moveLeft(self):
        if self.pos_x - 5 > 0:
            self.pos_x -= 5
            self.rect.move((-5, 0))
        else:
            self.estado = Parado(self)
        self.pintar()

    def moveRight(self):
        if self.pos_x + 5 < 550:
            self.pos_x += 5
            self.rect.move((5, 0))
        else:
            self.pos_x += 30
            self.rect.move((30, 0))
            self.estado = Parado(self)
        self.pintar()

    def moveUp(self):
        if self.pos_y - 5 > 0:
            self.pos_y -= 5
            self.rect.move((0, -5))
        else:
            self.estado = Parado(self)
    
    def moveDown(self):
        if self.pos_y + 5 < 370:
            self.pos_y += 5
            self.rect.move((0, 5))
        else:
            self.pos_y -= 37
            self.rect.move((0, -37))
            self.estado = Parado(self)
        