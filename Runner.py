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
    start_time = pygame.time.get_ticks()
    old_theme_rgb = (135, 206, 250)
    new_theme_rgb = (250, 125, 23)
    theme = old_theme_rgb

    death_sound = pygame.mixer.Sound("Death.wav")
    shrink_sound = pygame.mixer.Sound("shrink.mp3")
    destroy_sound = pygame.mixer.Sound("destroy.mp3")
    #pickup_sound = pygame.mixer.Sound("pickup.mp3")
    shoot_sound = pygame.mixer.Sound("shoot.mp3")
    clock_sound = pygame.mixer.Sound("clock.mp3")

    WIDTH = min(pygame.display.Info().current_w, pygame.display.Info().current_h)
    screen = pygame.display.set_mode([WIDTH, WIDTH])
    # background = pygame.image.load('bg.png').convert()
    # background = pygame.transform.smoothscale(background, screen.get_size())

    startscreen(screen)

    pygame.mixer.music.load("Musique 8 BITS.mp3")
    pygame.mixer.music.play(loops=-1)
    bird = Bird.Player()
    obstacles = pygame.sprite.Group()
    powers = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    clouds = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(bird)

    surf1 = pygame.image.load('destruction.png')
    surf1 = pygame.transform.scale(surf1, (50, 50))
    surf2 = pygame.image.load('time.png')
    surf2 = pygame.transform.scale(surf2, (50, 50))
    surf3 = pygame.image.load('small.png')
    surf3 = pygame.transform.scale(surf3, (50, 50))

    ADDENEMY = pygame.USEREVENT + 1
    POWER_EFFECT = pygame.USEREVENT + 2
    pygame.time.set_timer(ADDENEMY, 150)
    pygame.time.set_timer(POWER_EFFECT, 800)
    ADDCLOUD = pygame.USEREVENT + 3
    pygame.time.set_timer(ADDCLOUD, 500)

    params = Param(bird)

    spawn_proba = 10

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == ADDENEMY:
                if random.randint(1, spawn_proba) == 1:
                    new_obstacle = Obstacles.Enemy(params.speed)
                    obstacles.add(new_obstacle)
                    all_sprites.add(new_obstacle)
            elif event.type == POWER_EFFECT:
                if random.randint(1, 10) == 1:
                    pow = Powers.Power(random.choice(["destruction", "time", "small"]))
                    powers.add(pow)
                    all_sprites.add(pow)
            elif event.type == ADDCLOUD:
                if random.randint(1, 4) == 1:
                    cloud = Clouds.Cloud()
                    clouds.add(cloud)

        # Check if new Obstacle is sent
        if server.obs.change:
            new_obstacle = Obstacles.Enemy(params.speed, server.obs)
            obstacles.add(new_obstacle)
            all_sprites.add(new_obstacle)
            server.obs.change = False

        clouds.update()
        screen.fill(theme)
        for cloud in clouds:
            screen.blit(cloud.surf, cloud.rect)
        bird.update(coords, frame)
        obstacles.update()
        powers.update()
        bullets.update()

        # Check if power is launched
        if coords.fist and params.time.timer is None:
            params.time.effect(params)
            if params.time.timer is not None:
                clock_sound.play()
                clock_sound.fadeout(1500)
        elif coords.bottom_hand and params.small.timer is None:
            params.small.effect(params)
            if params.small.timer is not None :
                shrink_sound.set_volume(0.1)
                shrink_sound.play()
        elif coords.gun and len(bullets) == 0:
            if params.destruction.mun > 0:
                shoot_sound.set_volume(0.5)
                shoot_sound.play()
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
            pygame.mixer.music.stop()
            death_sound.play()
            pygame.time.wait(1000)
            return game_over(screen, WIDTH)

        collision = pygame.sprite.spritecollideany(bird, powers)
        if collision:
            collision.effect(params)
            collision.kill()
            #pickup_sound.play()
        if pygame.sprite.groupcollide(bullets, obstacles, True, True):
            params.destruction.timer = None
            destroy_sound.play()

        counting_time = pygame.time.get_ticks() - start_time

        # change milliseconds into minutes, seconds, milliseconds
        counting_minutes = str(counting_time // 60000).zfill(2)
        if frame == 1800 :
            theme = new_theme_rgb
            pygame.mixer.music.stop()
            pygame.mixer.music.load("new_theme.mp3")
            pygame.mixer.music.play(loops=-1)
        counting_seconds = str((counting_time % 60000) // 1000).zfill(2)
        counting_millisecond = str(counting_time % 1000).zfill(3)[0]
        if frame%600==0:
            spawn_proba-=1

        counting_string = "Time : %s:%s:%s    : X%d     : X%d     : X%d" % (
        counting_minutes, counting_seconds, counting_millisecond, params.destruction.mun, params.time.mun,
        params.small.mun)

        pygame.draw.rect(screen, theme, (WIDTH / 6, 0, 2*WIDTH/3, 50))
        screen.blit(surf1, (WIDTH / 2-90, 0))
        screen.blit(surf2, (WIDTH / 2 + 50, 0))
        screen.blit(surf3, (WIDTH / 2 + 175, 0))
        pygame.draw.line(screen,(0,0,0), (WIDTH / 6, 50), (5*WIDTH / 6,50), width=3)
        pygame.draw.line(screen, (0, 0, 0), (WIDTH / 6, 0), (WIDTH / 6, 50), width=3)
        pygame.draw.line(screen, (0, 0, 0), (5*WIDTH / 6, 0), (5 * WIDTH / 6, 50), width=3)

        counting_text = pygame.font.Font("PressStart2P-Regular.ttf", 15).render(str(counting_string), 1,
                                                                                (255, 255, 255))
        counting_rect = counting_text.get_rect(center=(WIDTH / 2, 25))
        screen.blit(counting_text, counting_rect)

        pygame.display.flip()
        clock.tick(30)
        frame += 1
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


def startscreen(scrn):
    pygame.mixer.music.load("waiting_screen.mp3")
    pygame.mixer.music.play(loops=-1)
    pygame.mixer.music.set_volume(0.3)
    Fnt = pygame.font.Font('PressStart2P-Regular.ttf', 50)
    cloud_x = 0
    cloud_y = 30
    clock = pygame.time.Clock()
    screen_height = pygame.display.Info().current_w
    screen_width = screen_height
    pygame.display.set_caption("startscreen")
    imp = pygame.image.load("startscreen.png").convert()
    imp = pygame.transform.scale(imp, (screen_width, screen_width))
    pygame.display.flip()
    status = True
    cloud = pygame.image.load("cloud_g.png")
    sprite1 = pygame.image.load("player_1.png")
    sprite1 = pygame.transform.scale(sprite1, (200, 200))
    sprite2 = pygame.image.load("player_2.png")
    sprite2 = pygame.transform.scale(sprite2, (200, 200))
    sprite = pygame.sprite.Sprite()
    sprite.image = sprite1
    sprite.rect = sprite1.get_rect()
    sprite.rect.centerx = 500
    sprite.rect.centery = 400
    frame = 0
    color = (0, 0, 0)
    txtsurf = Fnt.render("Waiting For Start", True, color)
    move_speed = 4
    cloud_speed = 4
    move_direction = 'up'
    while status:
        scrn.blit(imp, (0, 0))
        frame += 1
        if frame % 10 == 0:
            if (sprite.image == sprite1):
                sprite.image = sprite2
            else:
                sprite.image = sprite1
        scrn.blit(cloud, (cloud_x, cloud_y))
        scrn.blit(sprite.image, sprite.rect)
        if move_direction == 'up':
            sprite.rect.centery -= move_speed
            if sprite.rect.top < (screen_height / 2) - 150:
                move_direction = 'down'
        elif move_direction == 'down':
            sprite.rect.centery += move_speed
            if sprite.rect.bottom > (screen_height / 2) + 150:
                move_direction = 'up'

        cloud_x += cloud_speed
        if cloud_x > screen_width:
            cloud_y = random.randint(0, screen_height // 2)
            cloud_x = -cloud.get_width()
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                status = False
        if server.obs.connected:
            status=False
        scrn.blit(txtsurf, (screen_height/2-txtsurf.get_width()/2, 200))
        pygame.display.flip()
        clock.tick(30)
    pygame.mixer.music.stop()
    transi_sound = pygame.mixer.Sound("transi.mp3")
    transi_sound.play()
    pygame.time.wait(1750)


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
