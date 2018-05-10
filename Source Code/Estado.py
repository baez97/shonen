class Estado:
    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y
        self.img_rect = self.currentImage.get_rect()
        self.img_rect.move((self.pos_x, self.pos_y))

    def pintar(self, grafico):
        DISPLAYSURF.blit(self.currentImage, pj.img_rect)
    
class Parado(Estado):
    def avanza(self, grafico):
        self.currentImage = grafico.parado

class movingRight(Estado):
    def avanza(self, grafico):
        new_pos_x = self.pos_x + 5
        if new_pos_x + 120 < self.display_width:
            self.pos_x = new_pos_x
            self.currentImage = grafico.right
            self.img_rect = self.img_rect.move((5, 0))
        else
            self.currentImage = grafico.parado

class movingLeft(Estado):
    def avanza(self, grafico):
        new_pos_x = self.pos_x - 5
        if new_pos_x > 0:
            self.pos_x = new_pos_x
            self.currentImage = grafico.left
            self.img_rect = self.img_rect.move((-5, 0))
        else
            self.currentImage = grafico.parado
        