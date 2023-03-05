import pygame
import io
import random
import Server

class Enemy(pygame.sprite.Sprite):
    def __init__(self, speed, obs=None):
        if obs != None :
            super(Enemy, self).__init__()
            self.WIDTH = min(pygame.display.Info().current_w, pygame.display.Info().current_h)
            self.surf = pygame.image.load(io.BytesIO(obs.svg.encode()))
            origin_width = self.surf.get_width()
            origin_height = self.surf.get_height()
            ratio = self.surf.get_height()/self.surf.get_width()
            ratio_width = (obs.Xmax-obs.Xmin)/self.surf.get_width()
            ratio_height = (obs.Ymax-obs.Ymin)/self.surf.get_height()*ratio
            self.surf = pygame.transform.scale(self.surf, (self.WIDTH/3, self.WIDTH/3*ratio))
            self.rect = pygame.Rect(self.surf.get_rect().left+obs.Xmin/origin_width*self.WIDTH/3, self.surf.get_rect().top+obs.Ymin/origin_height*self.WIDTH/3*ratio, self.WIDTH/3*ratio_width, self.WIDTH/3*ratio_height)
            self.rect = self.surf.get_rect(center=(self.WIDTH / 3 * (obs.col - 1) + self.WIDTH / 6, self.WIDTH / 6))
            self.speed = speed
        else :
            super(Enemy, self).__init__()
            self.WIDTH = min(pygame.display.Info().current_w, pygame.display.Info().current_h)
            self.surf = pygame.image.load('enemy.png')
            self.surf = pygame.transform.scale(self.surf, (100, 100))
            if random.choice([True, False]):
                self.surf = pygame.transform.flip(self.surf,True,False)
            self.rect = self.surf.get_rect(center=(random.randint(0, self.WIDTH), 25))
            self.speed = speed

    def update(self):
        self.rect.move_ip(random.randint(-5,5), self.speed)
        if self.rect.bottom > self.WIDTH:
            self.kill()
