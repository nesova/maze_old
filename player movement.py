import pygame

MAP = [
    '#######@###',
    '#         #',
    '# ### #####',
    '# # #     #',
    '# # # ### #',
    '#K# # # # #',
    '### # # # #',
    '#   # #   #',
    '# # # # # #',
    '# #   # # #',
    '#X#########',
]
BLOCK_SIDE = 50
CELL_SIDE = 50
WIDTH = len(MAP[0])
HEIGHT = len(MAP)

SCREEN_WIDTH = WIDTH * BLOCK_SIDE
SCREEN_HEIGHT = HEIGHT * BLOCK_SIDE
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


class Wall:
    def __init__(self, x, y):
        self.pos = (x, y)
        self.wall_image = pygame.image.load('wall.png')

    def draw(self):
        screen.blit(self.wall_image, self.pos)


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.player_image = pygame.image.load('player.png')
        self.step = CELL_SIDE
        self.direction = Direction.NONE

    def draw(self):
        screen.blit(self.player_image, (self.x, self.y))

    def move(self):
        if self.direction == 1:
            self.y -= self.step
        elif self.direction == 2:
            self.y += self.step
        elif self.direction == 3:
            self.x -= self.step
        elif self.direction == 4:
            self.x += self.step



class Direction:
    NONE = 0
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


class Maze:
    def __init__(self):    
        self.walls = set()
        for i in range(HEIGHT):
            for j in range(WIDTH):
                if MAP[i][j] == '#':
                    self.walls.add(Wall(j * BLOCK_SIDE, i * BLOCK_SIDE))
                elif MAP[i][j] == '@':
                    self.player = Player(j * BLOCK_SIDE, i * BLOCK_SIDE)

    def draw(self):
        for wall in self.walls:
            wall.draw()
        self.player.draw()

    def set_player_direction(self, direction):
        if self.player_can_move(direction):
            self.player.direction = direction
        else:
            self.player.direction = Direction.NONE

    def player_can_move(self, direction):
        pcx, pcy = self.get_player_cell()
        if direction == 1 and pcy - CELL_SIDE < 0:
            return False
        if direction == 2 and pcy + CELL_SIDE > SCREEN_HEIGHT:
            return False
        if direction == 3 and pcx - CELL_SIDE < 0:
            return False
        if direction == 3 and pcx + CELL_SIDE > SCREEN_WIDTH:
            return False
        if direction == 0:
            return None
        return True

    def move_player(self):
        self.set_player_direction(self.player.direction)
        self.player.move()

    def get_player_cell(self):
        return (self.player.x , self.player.y)


maze = Maze()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                maze.set_player_direction(Direction.UP)
            elif event.key == pygame.K_DOWN:
                maze.set_player_direction(Direction.DOWN)
            elif event.key == pygame.K_LEFT:
                maze.set_player_direction(Direction.LEFT)
            elif event.key == pygame.K_RIGHT:
                maze.set_player_direction(Direction.RIGHT)
        elif event.type == pygame.KEYUP:
            maze.set_player_direction(Direction.NONE)
        maze.move_player()

    screen.fill((0, 0, 0))
    maze.draw()

    pygame.display.flip()
    pygame.time.wait(66)
pygame.quit()
