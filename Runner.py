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

    bird = Bird.Player()
    obstacles = pygame.sprite.Group()
    powers = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(bird)

    POWER_EFFECT = pygame.USEREVENT + 2
    pygame.time.set_timer(POWER_EFFECT, 1000)

    params = Param(bird)

    running = True
    while running:
        frame += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
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

        screen.fill((255, 255, 255))
        bird.update(coords, frame)
        obstacles.update()
        powers.update()

        # Check if power is launched
        if coords.fist:
            params.time.effect(params)
        elif coords.bottom_hand:
            params.small.effect(params)

        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)

        if pygame.sprite.spritecollideany(bird, obstacles):
            height = min(pygame.display.Info().current_w, pygame.display.Info().current_h)
            bird.kill()
            screen.fill((0, 0, 0))
            font = pygame.font.SysFont('copperplate', 40)
            title = font.render('Game Over', True, (255, 255, 255))
            restart_button = font.render('Restart', True, (255, 255, 255))
            quit_button = font.render('Quit', True, (255, 255, 255))
            t_up = pygame.image.load('thumbs_up.png')
            t_up = pygame.transform.scale(t_up, (30, 30))
            t_down = pygame.transform.flip(t_up, False, True)
            screen.blit(t_up, (height/2 - t_up.get_width() - 150, height/2 - t_up.get_height()))
            screen.blit(t_down, (height/2 - t_down.get_width() - 150, height / 2 - t_down.get_height() +100))
            screen.blit(title, (height / 2 -title.get_width()/2, height / 2 - title.get_height()/2 -100))
            screen.blit(restart_button, (height / 2 - restart_button.get_width()/2 , height/2 -restart_button.get_height()))
            screen.blit(quit_button, (height / 2 - quit_button.get_width()/2, height/2-quit_button.get_height() +100))

            pygame.display.flip()
            pygame.time.wait(2000)
            if coords.thumb :
                pygame_play()
            else:
                running = False
        pygame.display.flip()
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


def load_home(screen):
    height = min(pygame.display.Info().current_w, pygame.display.Info().current_h)
    screen.fill((0, 0, 0))
    font = pygame.font.SysFont('copperplate', 40)
    title = font.render('Start Game', True, (255, 255, 255))
    screen.blit(title, (height / 2 - title.get_width() / 2, height / 2 - title.get_height() / 2))
    pygame.display.flip()

    bol = True
    pygame.time.wait(10)
    while bol:
        if coords.y > 0:
            bol = False
        else:
            bol = False
            pygame.mixer.music.stop()
            pygame.mixer.quit()
            pygame.quit()

    pygame.display.flip()


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
