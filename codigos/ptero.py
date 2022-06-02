import pygame.sprite
from random import choice


class Ptero(pygame.sprite.Sprite):
    '''Classe para representar o obstáculo ptero'''
    def __init__(self, sheet):
        pygame.sprite.Sprite.__init__(self)
        img = sheet.subsurface((3*32, 0), (32, 32))
        img = pygame.transform.scale(img, (64, 64))
        img2 = sheet.subsurface((4*32, 0), (32, 32))
        img2 = pygame.transform.scale(img2, (64, 64))
        self.images = [img, img2]
        self.index = 0
        self.vel = 10
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.topright = (640, 250)
        self.mask = pygame.mask.from_surface(self.image)
        self.atualizar = False

    def update(self):
        '''Anima o objeto e o atualiza na tela'''
        if self.atualizar and self.rect.x == 700:
            self.rect.topright = (640, choice((250, 300, 350, 400)))
        if self.atualizar:
            self.index += 0.20
            self.rect.x -= self.vel
            if self.rect.topright[0] <= 0:
                self.rect.topright = (700, 250)
                self.atualizar = False
            if self.index >= len(self.images):
                self.index = 0
            self.image = self.images[int(self.index)]
        else:
            self.rect.x = 700
