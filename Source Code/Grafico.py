import pygame
from pygame.locals import *
from Variables import *

class Grafico:
    def cargar(self, ruta):
        return pygame.image.load(ruta)

    def __init__(self, imagenes, x, y):
        self.parado   = self.cargar(imagenes['parado'])
        self.up       = self.cargar(imagenes['up'])
        self.down     = self.cargar(imagenes['down'])
        self.right    = self.cargar(imagenes['right'])
        self.left     = self.cargar(imagenes['left'])
        self.currentImage  = self.parado
        self.img_rect = self.currentImage.get_rect()
        self.img_rect.move((x, y))

    def pintar(self, x, y):
        DISPLAYSURF.blit(self.currentImage, (x,y))
    
    def cambiarRight(self):
        self.currentImage = self.right
    
    def cambiarLeft(self):
        self.currentImage = self.left

    def cambiarDown(self):
        self.currentImage = self.down

    def cambiarUp(self):
        self.currentImage = self.up

    def cambiarParado(self):
        self.currentImage = self.parado
