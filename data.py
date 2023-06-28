
import pygame

# constants
WIDTH = 700
CELL_DIM = 20
GRID = WIDTH//CELL_DIM
BACKGROUND = 'white'
FRAME = 500
SLOW_FRAME = 5


# variables
running = True
algo_type = ''
obstacles = []
visited = []
row = [0, 1, 0, -1]
col = [1, 0, -1, 0]

# create clock
clock = pygame.time.Clock()


def set_game_window(window):
    # establishing grids
    for x in range(0, WIDTH, CELL_DIM):
        pygame.draw.line(window, 'black', (x, 0), (x, WIDTH), 2)
        pygame.draw.line(window, 'black', (0, x), (WIDTH, x), 2)

    pygame.display.update()
    clock.tick(SLOW_FRAME)


# set endpoints
def endpoints(window, starts, finals):
    global obstacles
    # set start point
    rect = pygame.Rect((starts[0] - 1) * CELL_DIM + 2, (starts[1] - 1) * CELL_DIM + 2, CELL_DIM - 2, CELL_DIM - 2)
    pygame.draw.rect(window, 'green', rect)

    # set end point
    rect = pygame.Rect((finals[0] - 1) * CELL_DIM + 2, (finals[1] - 1) * CELL_DIM + 2, CELL_DIM - 2, CELL_DIM - 2)
    pygame.draw.rect(window, 'red', rect)


def get_position(position):
    pos = (position[0]//CELL_DIM + 1, position[1]//CELL_DIM + 1)
    return pos
