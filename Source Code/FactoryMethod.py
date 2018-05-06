import pygame
from Ente import *
from Direccion import *

class FactoryMethod:
    def crearPersonaje(self, x, y, direccion, dw, dh):
        return Personaje(x, y, direccion, dw, dh)

    def crearDerecha(self):
        return Derecha()
    
    def crearIzquierda(self):
        return Izquierda()
