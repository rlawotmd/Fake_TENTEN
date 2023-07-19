# -*- coding: utf-8 -*-
import sys
import pygame
from pygame.locals import *
import time

#프래임
TARGET_FPS = 30
clock = pygame.time.Clock()

# 색정의
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

pygame.init()#라이브러리초기화
#디스플레이 초기화
screen = pygame.display.set_mode((600, 400), DOUBLEBUF) 
pygame.display.set_caption('돌림판')

#이미지 불러오기
img = pygame.image.load('./python/images.png')
