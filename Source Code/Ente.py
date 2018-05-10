import pygame, sys
from pygame.locals import *
from Grafico import *
from Estado import *

class Ente:
    def avanza(self):
        self.estado.avanza(grafico)

    def pintar(self):
        self.estado.pintar(grafico)
        
class Personaje(Ente):
    img = pygame.image.load('images/goku.png')
    img_left = pygame.image.load('images/leftarrow.png')
    img = pygame.transform.scale(img, (54, 112))
    img_rect = img.get_rect()
    img_rect = img_rect.move((100, 100))
    def __init__(grafico, nombre, estado):
        self.grafico = grafico
        self.nombre  = nombre
        self.estado  = estado

