import pygame
import Bird
import Obstacles
import threading
import Hand_capture


def pygame_play():
    pygame.init()

    WIDTH = min(pygame.display.Info().current_w, pygame.display.Info().current_h)
    screen = pygame.display.set_mode([WIDTH, WIDTH])

    bird = Bird.Player()
    obstacles = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(bird)

    ADDENEMY = pygame.USEREVENT + 1
    pygame.time.set_timer(ADDENEMY, 250)

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == ADDENEMY:
                new_obstacle = Obstacles.Enemy()
                obstacles.add(new_obstacle)
                all_sprites.add(new_obstacle)

        screen.fill((255, 255, 255))
        bird.update(coords)
        obstacles.update()

        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)

        if pygame.sprite.spritecollideany(bird, obstacles):
            bird.kill()
            running = False

        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    coords = Hand_capture.Coord()

    threads = list()
    x = threading.Thread(target=pygame_play)
    x.start()
    threads.append(x)
    y = threading.Thread(target=Hand_capture.run, args=(coords, ), daemon=True)
    y.start()
    threads.append(y)
    x.join()

