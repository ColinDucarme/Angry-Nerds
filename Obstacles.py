import pygame
import io


class Enemy(pygame.sprite.Sprite):
    def __init__(self, speed, obs):
        super(Enemy, self).__init__()
        self.WIDTH = min(pygame.display.Info().current_w, pygame.display.Info().current_h)
        self.surf = pygame.image.load(io.BytesIO(obs.svg.encode()))
        ratio = self.surf.get_height()/self.surf.get_width()
        ratio_width = (obs.Xmax-obs.Xmin)/self.surf.get_width()
        ratio_height = (obs.Ymax-obs.Ymin)/self.surf.get_height()*ratio
        self.surf = pygame.transform.scale(self.surf, (self.WIDTH/3, self.WIDTH/3*ratio))
        self.rect = self.surf.get_rect(center=(self.WIDTH/3*(obs.col-1)+self.WIDTH/6, 25))
        #self.surf = self.surf.subsurface((obs.Xmin, obs.Ymin, (obs.Xmax-obs.Xmin), (obs.Ymax-obs.Ymin)))
        self.speed = speed

    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.bottom > self.WIDTH:
            self.kill()
