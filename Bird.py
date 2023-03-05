import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super(Player, self).__init__()
        self.WIDTH = min(pygame.display.Info().current_w, pygame.display.Info().current_h)
        self.surf = pygame.image.load('player_1.png')
        self.size = 150
        self.player = 1
        self.surf = pygame.transform.scale(self.surf, (self.size, self.size))
        self.rect = self.surf.get_rect(center=(self.WIDTH / 2, 2*self.WIDTH / 3))

    def update(self, coords, frame):
        if frame%5==0 :
            if self.player == 1:
                self.surf = pygame.image.load('player_2.png')
                self.surf = pygame.transform.scale(self.surf, (self.size, self.size))
                self.player = 2
            else :
                self.surf = pygame.image.load('player_1.png')
                self.surf = pygame.transform.scale(self.surf, (self.size, self.size))
                self.player = 1
        self.rect = self.surf.get_rect(center=(self.WIDTH * coords.x, 2 * self.WIDTH / 3))