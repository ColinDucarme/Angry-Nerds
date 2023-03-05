import pygame
import random

pygame.init()
Fnt= pygame.font.Font('PressStart2P-Regular.ttf', 50)
screen_width = 1000
screen_height = 1000
cloud_x = 0
cloud_y = 30
clock=pygame.time.Clock()
scrn = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("startscreen")
imp = pygame.image.load("startscreen.png").convert()
pygame.display.flip()
status = True
cloud=pygame.image.load("cloud_g.png")
sprite1=pygame.image.load("sprite1.png")
sprite1= pygame.transform.scale(sprite1,(200,200))
sprite2=pygame.image.load("sprite2.png")
sprite2= pygame.transform.scale(sprite2,(200,200))
sprite = pygame.sprite.Sprite()
sprite.image = sprite1
sprite.rect = sprite1.get_rect()
sprite.rect.centerx = 500
sprite.rect.centery = 400
frame=0
color=(0,0,0)
txtsurf = Fnt.render("Waiting For Start", True, color)
move_speed = 4
cloud_speed = 4
move_direction = 'up'
while status:
    scrn.blit(imp, (0, 0))
    frame+=1
    if frame%10==0:
        if(sprite.image==sprite1):
            sprite.image = sprite2
        else:
            sprite.image = sprite1
    scrn.blit(cloud, (cloud_x, cloud_y))
    scrn.blit(sprite.image,sprite.rect)
    if move_direction == 'up':
        sprite.rect.centery -= move_speed
        if sprite.rect.top < (screen_height/2)-150:
            move_direction = 'down'
    elif move_direction == 'down':
        sprite.rect.centery += move_speed
        if sprite.rect.bottom > (screen_height/2)+150:
            move_direction = 'up'
    
    cloud_x += cloud_speed
    if cloud_x > screen_width:
        cloud_y=random.randint(0,screen_height/2)
        cloud_x = -cloud.get_width()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            status = False
    scrn.blit(txtsurf,(70, 200))
    pygame.display.flip()
    clock.tick(30)
    
pygame.quit()