import pygame.transform

from dinogame.codigos import cacto


class Cacto2(cacto.Cacto):
    '''Classe que herda do cacto simples, mudando apenas a imagem que representa
    um cacto duplo'''
    def __init__(self, sheet, img):
        cacto.Cacto.__init__(self, sheet)
        img = pygame.transform.scale(img, (32*2, 32*2))
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.bottomright = (640, 480-32)
        self.mask = pygame.mask.from_surface(self.image)
