import pygame
from Ente import *
from Direccion import *

class FactoryMethod:
    def crearPersonaje(self, nombre, x, y):
        return Personaje(nombre, x, y)

    def crearDerecha(self):
        return Derecha()
    
    def crearIzquierda(self):
        return Izquierda()
