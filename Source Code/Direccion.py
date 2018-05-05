# -*- coding: utf-8 -*-

from Personaje import *

class Direccion:
    def __init__(self):
            self.dir_x = 0
            self.dir_y = 0

    def avanza(self, alguien):
        alguien.muevete(self.dir_x, self.dir_y)
        
class Derecha(Direccion):
    nombre = 'derecha'
    def __init__(self):
        self.dir_x = 5
        self.dir_y = 0

class Izquierda(Direccion):
    nombre = 'izquierda'
    def __init__(self):
        self.dir_x = -5
        self.dir_y = 0