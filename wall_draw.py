import pygame

MAZE_MAP = [
    '#######@#####',
    '#  K#     #K#',
    '# ### # # # #',
    '# #   # #   #',
    '# # # #######',
    '# # #       #',
    '# # ####### #',
    '# #     #K# #',
    '# ##### # # #',
    '#   #   # # #',
    '### # ### # #',
    '#     #     #',
    '#X###########',
]
BLOCK_SIDE = 64
CELL_SIDE = 64
WIDTH = len(MAZE_MAP[0])
HEIGHT = len(MAZE_MAP)

SCREEN_WIDTH = WIDTH * BLOCK_SIDE
SCREEN_HEIGHT = HEIGHT * BLOCK_SIDE
wall_image = pygame.image.load('wall.png')
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class Wall:
    def __init__(self, texture=None):
        self.image = wall_image


    def draw(self):
        for i in range(len(MAZE_MAP)):
            for j in range(len(MAZE_MAP[0])):
                if MAZE_MAP[i][j] == '#':
                    screen.blit(self.image,)

pygame.display.update()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
pygame.quit()