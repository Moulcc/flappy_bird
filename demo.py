import glob
import os
import sys
from random import randint

# coding to do list
# 1. 加入帧和时间的设定
# 2. pipes deque

# 需要调整的数值或函数：
# 1. 窗口大小 背景的贴合度
# 2. pipes: 宽度，长度，移动速度
# 3. bird: 初始位置，每次点击上升的设定 和 下降设定（加速度）
# 4. buttons: 大小 位置 image
# 5. ranking board: 设计和大小 位置 rank[]=[7,5,3] 优先级队列
# 6. score

# 1. 一段时间之后增加难度
# 2. bgm
# 3. 场景变换 白天黑夜
# 4. bird colors
# 5. 吃金币：？
# 6. 单双人模式

import pygame

pygame.init()

w,h = 284*2 , 512

color1 = (45, 67, 80)
color2 = (120, 20, 30)

def load_image():
    images = {}
    paths = glob.glob(os.path.join('./images', '*.png'))
    for path in paths:
        img = pygame.image.load(path).convert()
        img_name = os.path.splitext(os.path.basename(path))[0]
        images.update({img_name: img})

    return images

screen_image = pygame.display.set_mode((w, h))
screen_rect = screen_image.get_rect()

pygame.display.set_caption("Demo")

bird = pygame.image.load('images/bird_wing_up.png')
bird_rect = bird.get_rect()
bird_rect.center = screen_rect.center

pipes = []
pipes_rect = []

# 512 = 32*16
# 十块
for i in range(10):
    rd = 3
    pipe = pygame.image.load('images/pipe_body.png')
    pipes_rect.append(pipe.get_rect())
    pipes_rect[i].x = w
    # top part
    if i <= 4:
        pipes_rect[i].y = 0 + 32 * (i-1)
    # bot part
    else:
        pipes_rect[i].y = 512 - 32 * (i - 1) + 32 * rd

    pipes.append(pipe)

for i in range(2):
    pipe = pygame.image.load('images/pipe_end.png')
    pygame.image.load('images/background.png')
    pipes_rect.append(pipe.get_rect())
    pipes_rect[i+10].x = w
    pipes_rect[i+10].y = 300 - i * 32
    pipes.append(pipe)


flag = 0
while not flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                bird_rect.y -= 10
            if event.key == pygame.K_DOWN:
                bird_rect.y += 10
            if event.key == pygame.K_LEFT:
                bird_rect.x -= 10
            if event.key == pygame.K_RIGHT:
                bird_rect.x += 10

    images = load_image()

    screen_image.blit(images['background'], (0, 0))
    screen_image.blit(images['background'], (w / 2, 0))

    for i in range(10):
        pipes_rect[i].x -= 1
    for i in range(10):
        screen_image.blit(pipes[i], pipes_rect[i])

    screen_image.blit(bird, bird_rect)

    for i in range(10):
        mask1 = pygame.mask.from_surface(bird)
        mask2 = pygame.mask.from_surface(pipes[i])
        offset = abs(bird_rect.x - pipes_rect[i].x), abs(bird_rect.y - pipes_rect[i].y)
        if mask1.overlap(mask2, offset) is not None:  # 已经碰撞
            print("已经碰撞")
            flag = 1

    pygame.display.flip()
