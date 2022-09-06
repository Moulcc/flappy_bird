import glob
import os
import sys
from collections import deque

import pygame
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

clock = pygame.time.Clock()

pygame.init()

FPS = 60
w, h = 284 * 2, 512

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
bird_rect.x -= 100

pipes_que = deque()



# 512 = 32*16
# 十块

def init_pipes():
    pipes = []
    pipes_rect = []

    rd = randint(2, 7)  # maybe change between 3,4,5
    for i in range(9):
        pipe = pygame.image.load('images/pipe_body.png')
        pipes_rect.append(pipe.get_rect())
        pipes_rect[i].x = w
        # top part
        if i < rd:  # set 4 to rd
            pipes_rect[i].y = 0 + 32 * i
        # bot part
        else:
            pipes_rect[i].y = 512 - 32 - (i - rd) * 32
        pipes.append(pipe)

    pipe = pygame.image.load('images/pipe_end.png')
    pipes_rect.append(pipe.get_rect())
    pipes_rect[9].x = w
    pipes_rect[9].y = 0 + 32 * rd
    pipes.append(pipe)

    pipe = pygame.image.load('images/pipe_end.png')
    pipes_rect.append(pipe.get_rect())
    pipes_rect[10].x = w
    pipes_rect[10].y = 512 - (10 - rd) * 32
    pipes.append(pipe)

    pipes_que.append([pipes,pipes_rect])

#init_pipes()

images = load_image()

flag = 0
frames = 0
while not flag:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                bird_rect.y -= 10
            if event.key == pygame.K_DOWN:
                bird_rect.y += 10

    screen_image.blit(images['background'], (0, 0))
    screen_image.blit(images['background'], (w / 2, 0))

    if frames % 240 == 0:  #  每三秒初始化一组pipes，插入pipe_que
        init_pipes()

    # 渲染目前还在pipe_que里的pipes
    for k in range(len(pipes_que)):
        for i in range(11):
            pipes_que[k][1][i].x -= 1
            screen_image.blit(pipes_que[k][0][i], pipes_que[k][1][i])

    if pipes_que[0][1][1].x == -80:
        pipes_que.popleft()

    screen_image.blit(bird, bird_rect)

    # 检查最左第一根和第二根

    for i in range(11):
        mask1 = pygame.mask.from_surface(bird)
        mask2 = pygame.mask.from_surface(pipes_que[0][0][i])
        offset = abs(bird_rect.x - pipes_que[0][1][i].x), abs(bird_rect.y - pipes_que[0][1][i].y)
        if mask1.overlap(mask2, offset) is not None:  # 已经碰撞
            flag = 1

    if len(pipes_que) > 1:
        for i in range(11):
            mask1 = pygame.mask.from_surface(bird)
            mask2 = pygame.mask.from_surface(pipes_que[1][0][i])
            offset = abs(bird_rect.x - pipes_que[1][1][i].x), abs(bird_rect.y - pipes_que[1][1][i].y)
            if mask1.overlap(mask2, offset) is not None:  # 已经碰撞
                flag = 1


    frames += 1

    pygame.display.flip()
