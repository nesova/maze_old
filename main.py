import random
import sys
import pygame

MAP = [
    '####@#####',
    '#  K#   ##',
    '# ### # # ',
    '##    # # ',
    '# ########',
    '### #    #',
    '#X########',
]

BLOCK_SIDE = 50
CELL_SIDE = 50
WIDTH = len(MAP[0])
HEIGHT = len(MAP)
SCREEN_WIDTH = WIDTH * BLOCK_SIDE
SCREEN_HEIGHT = HEIGHT * BLOCK_SIDE

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
font = pygame.font.SysFont('arial', 60)

