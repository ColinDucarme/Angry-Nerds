import pygame
import Bird
import Obstacles
import Powers
import Server
import Clouds
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
    # background = pygame.image.load('bg.png').convert()
    # background = pygame.transform.smoothscale(background, screen.get_size())

    bird = Bird.Player()
    obstacles = pygame.sprite.Group()
    powers = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    clouds = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(bird)

    ADDENEMY = pygame.USEREVENT + 1
    POWER_EFFECT = pygame.USEREVENT + 2
    pygame.time.set_timer(ADDENEMY, 1000)
    pygame.time.set_timer(POWER_EFFECT, 15000)
    ADDCLOUD = pygame.USEREVENT + 3
    pygame.time.set_timer(ADDCLOUD, 1000)

    params = Param(bird)

    running = True
    while running:
        frame += 1
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
            elif event.type == ADDCLOUD:
                if random.randint(1, 3) == 1:
                    cloud = Clouds.Cloud()
                    clouds.add(cloud)

        # Check if new Obstacle is sent
        if server.obs.change:
            new_obstacle = Obstacles.Enemy(params.speed, server.obs)
            obstacles.add(new_obstacle)
            all_sprites.add(new_obstacle)
            server.obs.change = False

        clouds.update()
        screen.fill((135, 206, 250))
        for cloud in clouds:
            screen.blit(cloud.surf, cloud.rect)
        bird.update(coords, frame)
        obstacles.update()
        powers.update()
        bullets.update()

        # Check if power is launched
        if coords.fist and params.time.timer is None:
            params.time.effect(params)
        elif coords.bottom_hand and params.small.timer is None:
            params.small.effect(params)
        elif coords.gun and len(bullets) == 0:
            if params.destruction.mun > 0:
                bullet = Powers.Bullet(params)
                bullets.add(bullet)
                all_sprites.add(bullet)
            params.destruction.effect(params)

        # Check if power time is finished
        if params.small.timer is not None:
            params.small.reset(params)
        elif params.time.timer is not None:
            params.time.reset(params)

        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)

        if pygame.sprite.spritecollideany(bird, obstacles):
            bird.kill()
            return game_over(screen, WIDTH)

        collision = pygame.sprite.spritecollideany(bird, powers)
        if collision:
            collision.effect(params)
            collision.kill()
        if pygame.sprite.groupcollide(bullets, obstacles, True, True):
            params.destruction.timer = None

        pygame.display.flip()
        clock.tick(30)
    pygame.mixer.music.stop()
    death_sound.play()
    pygame.time.wait(1000)
    pygame.mixer.quit()
    pygame.quit()


def game_over(screen, WIDTH):
    screen.fill((0, 0, 0))
    font = pygame.font.SysFont('copperplate', 40)
    title = font.render('Game Over', True, (255, 255, 255))
    restart_button = font.render('Restart', True, (255, 255, 255))
    quit_button = font.render('Quit', True, (255, 255, 255))
    t_up = pygame.image.load('thumbs_up.png')
    t_up = pygame.transform.scale(t_up, (30, 30))
    t_down = pygame.transform.flip(t_up, False, True)
    screen.blit(t_up, (WIDTH / 2 - t_up.get_width() - 150, WIDTH / 2 - t_up.get_height()))
    screen.blit(t_down, (WIDTH / 2 - t_down.get_width() - 150, WIDTH / 2 - t_down.get_height() + 100))
    screen.blit(title, (WIDTH / 2 - title.get_width() / 2, WIDTH / 2 - title.get_height() / 2 - 100))
    screen.blit(restart_button,
                (WIDTH / 2 - restart_button.get_width() / 2, WIDTH / 2 - restart_button.get_height()))
    screen.blit(quit_button,
                (WIDTH / 2 - quit_button.get_width() / 2, WIDTH / 2 - quit_button.get_height() + 100))

    pygame.display.flip()
    pygame.time.wait(2000)
    if coords.thumb:
        return pygame_play()


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
