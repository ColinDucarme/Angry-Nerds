import pygame
import Bird
import Obstacles
import threading
import Hand_capture


def pygame_play():
    pygame.mixer.init()
    pygame.init()
    clock = pygame.time.Clock()

    pygame.mixer.music.load("Musique 8 BITS.mp3")
    pygame.mixer.music.play(loops=-1)

    WIDTH = min(pygame.display.Info().current_w, pygame.display.Info().current_h)
    screen = pygame.display.set_mode([WIDTH, WIDTH])

    bird = Bird.Player()
    obstacles = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(bird)

    ADDENEMY = pygame.USEREVENT + 1
    pygame.time.set_timer(ADDENEMY, 1000)

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
            width = 255
            height = 255
            bird.kill()
            screen.fill((0, 0, 0))
            font = pygame.font.SysFont('copperplate', 40)
            title = font.render('Game Over', True, (255, 255, 255))
            restart_button = font.render('Restart', True, (255, 255, 255))
            quit_button = font.render('Quit', True, (255, 255, 255))
            t_up = pygame.image.load('thumbs_up.png')
            t_up = pygame.transform.scale(t_up, (25, 25))
            t_down = pygame.transform.flip(t_up,False,True)
            screen.blit(t_up, (width , height))
            screen.blit(t_down, (width , 3*height/2))
            screen.blit(title, (width/2 , height/2 ))
            screen.blit(restart_button, (width / 2 , height))
            screen.blit(quit_button, (width/2, 3*height/2))

            pygame.display.flip()
            pygame.time.wait(4000)
            if coords.y > 0:
                pygame_play()
            else:
                running = False

        pygame.display.flip()

    pygame.mixer.music.stop()
    pygame.mixer.quit()
    pygame.quit()


if __name__ == '__main__':
    coords = Hand_capture.Coord()

    threads = list()
    x = threading.Thread(target=pygame_play)
    x.start()
    threads.append(x)
    y = threading.Thread(target=Hand_capture.run, args=(coords,), daemon=True)
    y.start()
    threads.append(y)
    x.join()
