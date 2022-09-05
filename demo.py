import glob
import os
import sys
import pygame

pygame.init()

color1 = (45, 67, 80)
color2 = (120, 20, 30)

screen_image = pygame.display.set_mode((800, 600))
screen_rect = screen_image.get_rect()

pygame.display.set_caption("Demo")

bird = pygame.image.load('images/bird_wing_up.png')
bird_rect = bird.get_rect()
bird_rect.center = screen_rect.center

pipes = []
pipes_rect = []


for i in range(5):
    pipe = pygame.image.load('images/pipe_body.png')
    pipes_rect.append(pipe.get_rect())
    pipes_rect[i].x = 800
    if i > 2:
        pipes_rect[i].y = 300 + (i-2) * 32
    else:
        pipes_rect[i].y = 300 - i * 32
    pipes.append(pipe)

for i in range(2):
    pipe = pygame.image.load('images/pipe_end.png')
    pipes_rect.append(pipe.get_rect())
    pipes_rect[i].x = 800
    pipes_rect[i].y = 300 - i * 32
    pipes.append(pipe)

screen_image.fill(color1)

flag = 0
while not flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_rect.y -= 10

    for i in range(5):
        pipes_rect[i].x -= 1
    screen_image.fill(color1)
    for i in range(5):
        screen_image.blit(pipes[i], pipes_rect[i])
    screen_image.blit(bird, bird_rect)

    for i in range(5):
        mask1 = pygame.mask.from_surface(bird)
        mask2 = pygame.mask.from_surface(pipes[i])
        offset = abs(bird_rect.x - pipes_rect[i].x), abs(bird_rect.y - pipes_rect[i].y)
        if mask1.overlap(mask2, offset) is not None:  # 已经碰撞
            print("已经碰撞")
            flag = 1

    pygame.display.flip()
