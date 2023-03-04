import pygame
import random


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.WIDTH = min(pygame.display.Info().current_w, pygame.display.Info().current_h)
        self.surf = pygame.image.load('Svg_example3.svg')
        self.surf = pygame.transform.scale(self.surf, (50, 50))
        self.rect = self.surf.get_rect(center=(random.randint(0, self.WIDTH), 250))

    def update(self):
        self.rect.move_ip(0, 1)
        if self.rect.bottom > self.WIDTH:
            self.kill()
