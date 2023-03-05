import pygame
import Bird
import Obstacles
import Powers
import Server
import threading
import Hand_capture
import random

class Param:

    def __init__(self, bird, speed=15):
        self.bird = bird
        self.speed = speed
        self.destruction = Powers.Destruction_Power()
        self.time = Powers.Time_Power()
        self.small = Powers.Size_Power()


def pygame_play():
    pygame.mixer.init()
    pygame.init()
    clock = pygame.time.Clock()
    frame = 0

    pygame.mixer.music.load("Musique 8 BITS.mp3")
    pygame.mixer.music.play(loops=-1)
    death_sound = pygame.mixer.Sound("Death.wav")

    WIDTH = min(pygame.display.Info().current_w, pygame.display.Info().current_h)
    screen = pygame.display.set_mode([WIDTH, WIDTH])
    background = pygame.image.load('bg.png').convert()
    background = pygame.transform.smoothscale(background, screen.get_size())

    bird = Bird.Player()
    obstacles = pygame.sprite.Group()
    powers = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(bird)

    ADDENEMY = pygame.USEREVENT + 1
    POWER_EFFECT = pygame.USEREVENT + 2
    pygame.time.set_timer(ADDENEMY, 1000)
    pygame.time.set_timer(POWER_EFFECT, 1000)

    params = Param(bird)

    running = True
    while running:
        frame+=1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == ADDENEMY:
                new_obstacle = Obstacles.Enemy(params.speed)
                obstacles.add(new_obstacle)
                all_sprites.add(new_obstacle)
            elif event.type == POWER_EFFECT:
                pow = Powers.Power(random.choice(["destruction", "time", "small"]))
                powers.add(pow)
                all_sprites.add(pow)

        # Check if new Obstacle is sent
        if server.obs.change:
            new_obstacle = Obstacles.Enemy(params.speed, server.obs)
            obstacles.add(new_obstacle)
            all_sprites.add(new_obstacle)
            server.obs.change = False

        screen.blit(background, (0, 0))
        bird.update(coords, frame)
        obstacles.update()
        powers.update()

        # Check if power is launched
        if coords.fist :
            params.time.effect(params)
        elif coords.bottom_hand :
            params.small.effect(params)

        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)

        if pygame.sprite.spritecollideany(bird, obstacles):
            bird.kill()
            running = False
        collision = pygame.sprite.spritecollideany(bird, powers)
        if collision:
            collision.effect(params)
            collision.kill()

        pygame.display.flip()
        clock.tick(30)
    pygame.mixer.music.stop()
    death_sound.play()
    pygame.time.wait(1000)
    pygame.mixer.quit()
    pygame.quit()


if __name__ == '__main__':
    coords = Hand_capture.Coord()
    server = Server.Socket()

    threads = list()
    x = threading.Thread(target=pygame_play)
    x.start()
    threads.append(x)
    y = threading.Thread(target=Hand_capture.run, args=(coords,), daemon=True)
    y.start()
    threads.append(y)
    z = threading.Thread(target=server.run, daemon=True)
    z.start()
    threads.append(z)
    x.join()
