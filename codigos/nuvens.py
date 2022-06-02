import pygame
from random import randrange


class Nuvem(pygame.sprite.Sprite):
    '''Classe para representar as nuvens no cenário'''
    def __init__(self, sheet, size):
        pygame.sprite.Sprite.__init__(self)
        img = sheet.subsurface((32*7, 0), (32, 32))
        img = pygame.transform.scale(img, (96, 96))
        width, height = size
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.center = (randrange(480, width, 40), randrange(100, 300, 40))
        self.width, self.height = width, height

    def update(self):
        '''Movimenta as nuvens na tela'''
        self.rect.x -= 10
        if self.rect.topright[0] <= 0:
            self.rect.x = self.width
            self.rect.y = randrange(100, 300, 40)
