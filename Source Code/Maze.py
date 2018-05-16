from Grafico import *
from Variables import *
class Maze:
    def __init__():
        self.celdas = [[]]
        
        DISPLAYSURF.fill(WHITE)

        for x in range(0, 600, 50):
            DISPLAYSURF.blit(grass, (x, 0))
        for x in range(0, 560, 50):
            for y in range(40, 321, 40):
                DISPLAYSURF.blit(block, (x,y))
                
        DISPLAYSURF.blit(grass, (0, 20))

class Tile:
    def __init__():
        self.grafico = TileGrafico(self)
    def pintar():
        self.grafico.pintar()

class GrassTile(Tile):
    def __init__():
        self.imagen = 'images/grass.png'
        super(GrassTile, self).__init__()