import pygame
from pygame.locals import *

class Grafico:
    def __init__(self, personaje):
        self.parado   = cargar(personaje.imagenes['parado'])
        self.up       = cargar(personaje.imagenes['up'])
        self.down     = cargar(personaje.imagenes['down'])
        self.right    = cargar(personaje.imagenes['right'])
        self.left     = cargar(personaje.imagenes['left'])

        currentImage  = self.parado
        self.img_rect = self.currentImage.get_rect()
        self.img_rect.move((personaje.pos_x, personaje.pos_y))

    def cargar(self, ruta):
        return pygame.image.load(ruta)

    def pintar(self):
        DISPLAYSURF.blit(currentImage, img_rect)
    
    def cambiarDerecha(self):
        self.currentImage = self.right
        # self. = pygame.transform.scale(self.right, (54, 112))
    
    def cambiarIzquierda(self):
        self.currentImage = self.left

    def cambiarAbajo(self):
        self.currentImage = self.down

    def cambiarArriba(self):
        self.currentImage = self.up

    def cambiarParado(self):
        self.currentImage = self.parado
