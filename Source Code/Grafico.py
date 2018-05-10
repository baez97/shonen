import pygame
from pygame.locals import *

class Grafico:
    def __init__(self, p, u, d, r, l):
        self.parado = cargar(p)
        self.up     = cargar(u)
        self.down   = cargar(d)
        self.right  = cargar(r)
        self.left   = cargar(l)

    def cargar(self, cadena):
        return pygame.image.load(cadena)
    
