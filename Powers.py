import pygame
import random
import Runner


class Power(pygame.sprite.Sprite):

    def __init__(self, state):
        self.state = state
        super(Power, self).__init__()
        self.WIDTH = min(pygame.display.Info().current_w, pygame.display.Info().current_h)
        if self.state == "destruction":
            self.surf = pygame.image.load('destruction.png')
            self.surf = pygame.transform.scale(self.surf, (100, 100))
        elif self.state == "time":
            self.surf = pygame.image.load('time.png')
            self.surf = pygame.transform.scale(self.surf, (100 * self.surf.get_width() / self.surf.get_height(), 100))
        elif self.state == "small":
            self.surf = pygame.image.load('small.png')
            self.surf = pygame.transform.scale(self.surf, (100 * self.surf.get_width() / self.surf.get_height(), 100))
        self.rect = self.surf.get_rect(center=(random.randint(0, self.WIDTH), 25))

    def update(self):
        self.rect.move_ip(0, 15)
        if self.rect.bottom > self.WIDTH:
            self.kill()

    def effect(self, params):
        if self.state == "destruction":
            params.destruction.mun += 1
        elif self.state == "time":
            params.time.mun += 1
        elif self.state == "small":
            params.small.mun += 1

    def reset(self, params):
        params.speed = 15
        params.bird.surf = pygame.transform.scale(params.bird.surf, (100, 100))


class Destruction_Power():

    def __init__(self):
        self.mun = 0

    def effect(self, params):
        if self.mun > 0:
            self.mun -= 1

class Time_Power():

    def __init__(self):
        self.mun = 0
        self.timer = None

    def effect(self, params):
        if self.mun > 0:
            self.timer = pygame.time.get_ticks()
            params.speed = 8
            self.mun -= 1

    def reset(self, params):
        if pygame.time.get_ticks() - self.timer >= 5000:
            self.timer = None
            params.speed = 15


class Size_Power():

    def __init__(self):
        self.mun = 0
        self.timer = None

    def effect(self, params):
        if self.mun > 0:
            self.timer = pygame.time.get_ticks()
            params.bird.size = 75
            self.mun -= 1

    def reset(self, params):
        if pygame.time.get_ticks() - self.timer >= 5000:
            self.timer = None
            params.bird.size = 150


class Bullet(pygame.sprite.Sprite):
    def __init__(self, params):
        super(Bullet, self).__init__()
        self.surf = pygame.image.load('bullet.png')
        self.surf = pygame.transform.scale(self.surf, (20, 20))
        self.rect = self.surf.get_rect(center=(params.bird.rect.left + params.bird.size / 2, params.bird.rect.top))

    def update(self):
        self.rect.move_ip(0, -20)
        if self.rect.top < 0:
            self.kill()
