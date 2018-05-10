import pygame
from pygame.locals import *

class Estado:  
    def getImage(self):
        return self.image
   
class Parado(Estado):
    def __init__(self, personaje):
        self.image = pygame.image.load(personaje.imagenes['parado'])

    def avanza(self, personaje):
        pass

"""class MovingRight(Estado):
    def avanza(self, grafico):
        new_pos_x = self.pos_x + 5
        if new_pos_x + 120 < 600:
            self.pos_x = new_pos_x
            self.currentImage = grafico.right
            self.img_rect = self.img_rect.move((5, 0))
        else
            self.currentImage = grafico.parado"""

class MovingLeft(Estado):
    def __init__(self, personaje):
        self.image = pygame.image.load(personaje.imagenes['left'])

    def avanza(self, personaje):
        personaje.moveLeft()

class MovingRight(Estado):
    def __init__(self, personaje):
        self.image = pygame.image.load(personaje.imagenes['right'])

    def avanza(self, personaje):
        personaje.moveRight()
    
        