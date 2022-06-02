import pygame.sprite


class Chao(pygame.sprite.Sprite):
    def __init__(self, sheet, x):
        pygame.sprite.Sprite.__init__(self)
        img = sheet.subsurface((6*32, 0), (32, 32))
        img = pygame.transform.scale(img, (64, 64))
        self.image = img
        self.vel = 10
        self.rect = self.image.get_rect()
        self.rect.center = (x, 480-32)

    def update(self):
        self.rect.x -= self.vel
        if self.rect.topright[0] <= 0:
            self.rect.x = 640

