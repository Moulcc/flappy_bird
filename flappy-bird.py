#! /usr/bin/env python3
import sys
from collections import deque

import pygame
import os
import glob
from pygame.locals import *

FPS = 60
image_paths = glob.glob(os.path.join('./images', '*.png'))
w, h = 500, 400
# ANIMATION_SPEED = 0.18  # pixels per millisecond

# 先做一个长方形 往左边动
# 在长方形里填充png





# 需要调整的数值或函数：
# 1. 窗口大小 背景的贴合度
# 2. pipes: 宽度，长度，移动速度
# 3. bird: 初始位置，每次点击上升的设定 和 下降设定
# 4. buttons: 大小 位置
# 5. ranking board: 设计和大小 位置

'''The screen
1. update all the time
'''

'''The bird
1. inited in a fixed position
2. when press space, fly up, then sink down in a determined function(simply liner for now)
'''

'''The pipes
1. pipes contain two parts, top_pipe and bottom_pipe
2. every pipes_init_time msec, the pipes would show in right and move from right to left
'''


def load_image():
    images = {}
    paths = glob.glob(os.path.join('./images', '*.png'))
    print(paths)
    for path in paths:
        img = pygame.image.load(path).convert()
        img_name = os.path.splitext(os.path.basename(path))[0]
        images.update({img_name: img})

    return images

def bird_init():
    bird = pygame.image.load('images/bird_wing_up.png')
    return bird

def pipes_pair_init():
    pygame.image.load('images/pipe_body.png')
    space = 100

def collapse(bird, pipes_que):
    #  鸟碰到边界
    #  鸟碰到柱子
    return False

def main():
    "1. show the start page"
    pygame.init()

    screen = pygame.display.set_mode((w, h))
    screen_rect = screen.get_rect()
    pygame.display.set_caption('Flappy Bird')

    clock = pygame.time.Clock()
    #    score_font = pygame.font.SysFont(None, 32, bold=True)  # default font
    images = load_image()

    "2. ranking board"

    "3. start game"
    "new bird case and pipe case"
    bird = bird_init()
    bird_rect = bird.get_rect()
    bird_rect.center = screen_rect.center
    bird_rect.x -= 100
    frame_clock = 0

    pipes_que = deque()

    "continuous collapse detection"

    "4. exit game"
    end = 0
    while not end:
        clock.tick(FPS)

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

        screen.blit(images['background'], (0, 0))
        screen.blit(images['background'], (w / 2, 0))
        screen.blit(bird, bird_rect)
        pygame.display.flip()

        frame_clock += 1
        if bird_rect.y <= 0:
            end = 1

if __name__ == '__main__':
    main()