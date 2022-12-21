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
    '     #####',
    '#X########',
]

BLOCK_SIDE = 50
CELL_SIDE = 50
WIDTH = len(MAP[0])
HEIGHT = len(MAP)
SCREEN_WIDTH = WIDTH * BLOCK_SIDE
SCREEN_HEIGHT = HEIGHT * BLOCK_SIDE


class Wall:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.texture = pygame.image.load(f'images/wall.png')
        
    def draw(self):
        for i in range(HEIGHT):
            for j in range(WIDTH):
                if MAP[i][j] == '#':
                    screen.blit(self.texture, (j * CELL_SIDE, i * CELL_SIDE))


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    font = pygame.font.SysFont('arial', 60)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()
