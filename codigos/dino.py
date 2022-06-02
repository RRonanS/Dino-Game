import pygame


class Dino(pygame.sprite.Sprite):
    def __init__(self, sheet):
        pygame.sprite.Sprite.__init__(self)
        self.imagens = []
        for i in range(3):
            img = sheet.subsurface((32*i, 0), (32, 32))
            img = pygame.transform.scale(img, (96, 96))
            self.imagens.append(img)
        self.index = 0
        self.image = self.imagens[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = (100, 416)
        self.y = self.rect.center[1]
        self.pulo = False
        self.descendo = False
        self.mask = pygame.mask.from_surface(self.image)

    def pular(self):
        self.pulo = True

    def update(self):
        if self.pulo:
            if self.descendo:
                self.rect.y += 10
                if self.rect.center[1] >= self.y:
                    self.rect.center = self.rect.center[0], self.y
                    self.descendo = self.pulo = False
            else:
                self.rect.y -= 10
                if self.rect.y <= 250:
                    self.descendo = True
        self.index += 0.25
        if self.index >= 2:
            self.index = 0
        self.image = self.imagens[int(self.index)]
