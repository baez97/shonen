import pygame, sys
from pygame.locals import *

class Ente:
    def avanza(self):
        self.direccion.avanza(self)
    def muevete(self, x, y):
        new_pos_x = self.pos_x + x
        new_pos_y = self.pos_y + y
        if new_pos_x + 120 < self.display_width and new_pos_x > 0:
            self.pos_x = new_pos_x
            self.pj_img_rect = self.pj_img_rect.move((x, 0))
            print 'Condition met'
        if new_pos_y + 100 < self.display_height and new_pos_y > 0:    
            self.pos_y += y
            self.pj_img_rect = self.pj_img_rect.move((0, y))

class Personaje(Ente):
    pj_img = pygame.image.load('images/goku.png')
    pj_img = pygame.transform.scale(pj_img, (54, 112))
    pj_img_rect = pj_img.get_rect()
    pj_img_rect = pj_img_rect.move((100, 100))
    
    def __init__(self, x, y, direccion, dw, dh):
        self.pos_x = x 
        self.pos_y = y 
        self.direccion = direccion
        self.display_width = dw 
        self.display_height = dh 

