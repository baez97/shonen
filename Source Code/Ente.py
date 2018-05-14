import pygame, sys
from pygame.locals import *
from Grafico import *
from Estado import *
from Variables import *
from StatusFactory import *

class Ente:

    def avanza(self):
        self.estado.avanza(self)

    def pintar(self):
        DISPLAYSURF.blit(self.estado.getImage(), (self.pos_x, self.pos_y))
        
class Personaje(Ente):

    def __init__(self, nombre, x, y):
        self.imagenes = {'parado':'images/parado.gif', 'left':'images/left.png', 'right':'images/right.png', 'up':'images/up.png', 'down':'images/down.png'}
        self.nombre  = nombre
        self.pos_x   = x
        self.pos_y   = y
        self.grafico = Grafico(self.imagenes, self.pos_x, self.pos_y)
        self.estado  = Parado(self)
        self.rect    = self.estado.getImage().get_rect()
        self.statusFactory = StatusFactory(self)
        self.rect.move((x,y))
        
        
    def pintar(self):
        self.grafico.pintar(self.pos_x, self.pos_y)
        #DISPLAYSURF.blit(self.estado.getImage(), (self.pos_x, self.pos_y))

    def moveLeft(self):
        if self.pos_x - 5 > 0:
            self.pos_x -= 5
            self.rect.move((-5, 0))
        else:
            self.cambiarParado()
        self.pintar()

    def moveRight(self):
        if self.pos_x + 5 < 550:
            self.pos_x += 5
            self.rect.move((5, 0))
        elif self.pos_x < 560:
            self.pos_x += 15
            self.rect.move((15, 0))
            self.cambiarParado()
        else:
            self.cambiarParado()
        self.pintar()

    def moveUp(self):
        if self.pos_y - 5 > 0:
            self.pos_y -= 5
            self.rect.move((0, -5))
        else:
            self.cambiarParado()
    
    def moveDown(self):
        if self.pos_y + 5 < 350:
            self.pos_y += 5
            self.rect.move((0, 5))
        else:
            self.pos_y -= 37
            self.rect.move((0, -37))
            self.cambiarParado()

    def cambiarParado(self):
        self.estado = self.statusFactory.parado
        self.grafico.cambiarParado()
    
    def cambiarUp(self):
        self.estado = self.statusFactory.movingUp
        self.grafico.cambiarUp()
    
    def cambiarDown(self):
        self.estado = self.statusFactory.movingDown
        self.grafico.cambiarDown()
    
    def cambiarRight(self):
        self.estado = self.statusFactory.movingRight
        self.grafico.cambiarRight()

    def cambiarLeft(self):
        self.estado = self.statusFactory.movingLeft
        self.grafico.cambiarLeft()
    
    def getGrafico(self):
        return self.grafico