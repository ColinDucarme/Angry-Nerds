from random import random
import random
import pygame
from pygame import RLEACCEL


class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud, self).__init__()
        self.surf = pygame.image.load("cloud.png").convert()
        self.surf.set_alpha(125)
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.WIDTH = min(pygame.display.Info().current_w, pygame.display.Info().current_h)

        self.rect = self.surf.get_rect(
            center=(random.randint(0, self.WIDTH), 0)
        )

    def update(self):
        self.rect.move_ip(-1, 8)

        if self.rect.top > self.WIDTH or self.rect.right < 0:
            self.kill()