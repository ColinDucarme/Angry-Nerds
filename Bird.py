import pygame
import Runner

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((0, 0, 0))
        self.WIDTH = min(pygame.display.Info().current_w, pygame.display.Info().current_h)
        self.rect = self.surf.get_rect(center=(self.WIDTH/2, self.WIDTH/2))

    def update(self, coords):
        self.rect = self.surf.get_rect(center=(self.WIDTH*coords.x, 2*self.WIDTH/3))