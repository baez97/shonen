from Estado import *
class StatusFactory:
    def __init__(self, personaje):
        self.movingRight = MovingRight(personaje)
        self.movingLeft  = MovingLeft(personaje)
        self.movingUp    = MovingUp(personaje)
        self.movingDown  = MovingDown(personaje)
        self.parado      = Parado(personaje)
    