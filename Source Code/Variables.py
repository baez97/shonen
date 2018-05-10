import pygame
from pygame.locals import *

FPS            = 30
fpsClock       = pygame.time.Clock()

WHITE          = (255, 255, 255)

DISPLAY_WIDTH  = 600
DISPLAY_HEIGHT = 400
DISPLAYSURF    = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))