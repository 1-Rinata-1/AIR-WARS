import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, plane):
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 10, 20)
        self.color = (255, 0, 0)
        self.speed = 0.5
        self.rect.centerx = plane.rect.centerx
        self.rect.top = plane.rect.top
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
