import pygame.sprite


class Cacto(pygame.sprite.Sprite):
    def __init__(self, sheet):
        pygame.sprite.Sprite.__init__(self)
        img = sheet.subsurface((32*5, 0), (32, 32))
        img = pygame.transform.scale(img, (32*2, 32*2))
        self.image = img
        self.vel = 10
        self.rect = self.image.get_rect()
        self.rect.bottomright = (640, 480-32)
        self.mask = pygame.mask.from_surface(self.image)
        self.atualizar = False

    def update(self):
        if self.atualizar and self.rect.x == 700:
            self.rect.bottomright = (640, 480-32)
        if self.atualizar:
            self.rect.x -= self.vel
            if self.rect.bottomright[0] <= 0:
                self.rect.bottomright = (700, 480-32)
                self.atualizar = False
        else:
            self.rect.x = 700
