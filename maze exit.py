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
font = pygame.font.SysFont('arial', 60)
text = font.render('You Win!', True, (0, 255, 0))
door_textures = []
for i in range(1, 5):
    door_textures.append(pygame.image.load(f'image_door{i}.png'))

class Wall:
    def __init__(self):
        self.pos = []
        self.texture = pygame.image.load('wall.png')

    def return_walls_coords(self):
        return self.pos

    def get_coord(self, x, y):
        self.pos.append((x, y))

    def draw(self):
        for pos in self.pos:
            screen.blit(self.texture, pos)


class Exit:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, texture):
        screen.blit(door_textures[texture], (self.x, self.y))



class Player:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.texture = pygame.image.load('player.png')
        self.step = CELL_SIDE
        self.direction = Direction.NONE

    def get_pos(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        screen.blit(self.texture, (self.x, self.y))

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
        self.wall = Wall()
        self.player = Player()
        self.open = 0
        for i in range(HEIGHT):
            for j in range(WIDTH):
                if MAP[i][j] == '#':
                    self.wall.get_coord(j * BLOCK_SIDE, i * BLOCK_SIDE)
                elif MAP[i][j] == "@":
                    self.player.get_pos(j * BLOCK_SIDE, i * BLOCK_SIDE)
                elif MAP[i][j] == 'X':
                    self.exit = Exit(j * BLOCK_SIDE, i * BLOCK_SIDE)
        self.pos = self.wall.return_walls_coords()

    def draw(self):
        self.wall.draw()
        self.player.draw()
        self.exit.draw(self.open)

    def win(self):
       if self.get_player_cell() == (self.exit.x, self.exit.y):
           for i in range(4):
                self.exit.draw(i)
           return True

    def set_player_direction(self, direction):
        if self.player_can_move(direction):
            self.player.direction = direction
        else:
            self.player.direction = Direction.NONE

    def player_can_move(self, direction):
        pcx, pcy = self.get_player_cell()
        if direction == 1 and (pcy - CELL_SIDE < 0 or (pcx, pcy - CELL_SIDE) in self.pos):
            return False
        if direction == 2 and (pcy + CELL_SIDE > SCREEN_HEIGHT or (pcx, pcy + CELL_SIDE) in self.pos):
            return False
        if direction == 3 and (pcx - CELL_SIDE < 0 or (pcx - CELL_SIDE, pcy) in self.pos):
            return False
        if direction == 4 and (pcx + CELL_SIDE > SCREEN_WIDTH or (pcx + CELL_SIDE, pcy) in self.pos):
            return False
        if direction == 0:
            return None
        return True

    def move_player(self):
        self.set_player_direction(self.player.direction)
        self.player.move()

    def get_player_cell(self):
        return (self.player.x, self.player.y)


def start_level():
    maze = Maze()

    running = True
    while running:
        if maze.win():
            return
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
        pygame.time.wait(100)
    pygame.quit()


def show_win_message():
    screen.blit(text, (CELL_SIDE * 2, SCREEN_HEIGHT - CELL_SIDE - 60))
    pygame.display.flip()
    pygame.time.wait(1000)

while True:
    start_level()
    show_win_message()