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
screen = pygame.display.set_mode((600, 400), DOUBLEBUF) 
pygame.display.set_caption('돌림판')

img = pygame.image.load('images.png')
