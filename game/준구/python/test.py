import sys
import pygame
from pygame.locals import *
import time


TARGET_FPS = 30
clock = pygame.time.Clock()

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

pygame.init()
screen = pygame.display.set_mode((1200, 900), DOUBLEBUF) 
pygame.display.set_caption('돌림판')

img = pygame.image.load('./game/준구/python/images.png')
img2 = pygame.image.load('./game/준구/python/images2.png')

degree = 0
flag = True
rad = 10
stop_time = 0.008

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.guit()
            sys.exit()
    
        if event.type == KEYDOWN:
            if event.key == 32:
             if flag ==True:
                flag = False

    screen.fill(WHITE)
    
    x = 600
    y = 450
    rotated = pygame.transform.rotate(img,degree)
    rect = rotated.get_rect()
    rect.center = (x, y)
    screen.blit(rotated, rect)

    if flag == True:
        degree += rad
    elif flag == False:
        if rad > 0: 
            rad -= stop_time
            degree += rad

    screen.blit(img2, (200, 430))
    pygame.display.flip()