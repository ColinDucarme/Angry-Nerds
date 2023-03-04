import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super(Player, self).__init__()
        self.WIDTH = min(pygame.display.Info().current_w, pygame.display.Info().current_h)
        self.surf = pygame.image.load('031ddc5900aa502b7344037391fa7650.svg')
        self.surf = pygame.transform.scale(self.surf, (100, 100))
        self.rect = self.surf.get_rect(center=(self.WIDTH / 2, self.WIDTH / 2))

    def update(self, coords):
        self.rect = self.surf.get_rect(center=(self.WIDTH * coords.x, 2 * self.WIDTH / 3))
