import pygame
from pygame.locals import *

class Estado:  
    def getImage(self):
        return self.image
    def isUp(self):
        return False
    def isDown(self):
        return False
    def isRight(self):
        return False
    def isLeft(self):
        return False
   
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

    def isLeft(self):
        return True

class MovingRight(Estado):
    def __init__(self, personaje):
        self.image = pygame.image.load(personaje.imagenes['right'])

    def avanza(self, personaje):
        personaje.moveRight()
    
    def isRight(self):
        return True

class MovingUp(Estado):
    def __init__(self, personaje):
        self.image = pygame.image.load(personaje.imagenes['up'])
    
    def avanza(self, personaje):
        personaje.moveUp()
    
    def isUp(self):
        return True

class MovingDown(Estado):
    def __init__(self, personaje):
        self.image = pygame.image.load(personaje.imagenes['down'])

    def avanza(self, personaje):
        personaje.moveDown()
    
    def isDown(self):
        return True
    
        