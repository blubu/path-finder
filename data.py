
import pygame
from collections import deque

# constants
WIDTH = 500
HEIGHT = 500
CELL_DIM = 50
BACKGROUND = (0, 0, 0)

# variables
running = True
visited = []
colored = []
grids = [(4, 7), (5, 6), (6, 5), (7, 4)]
row = [0, 1, 0, -1]
col = [1, 0, -1, 0]

# queue
q = deque()
start = (2, 2)
q.append([start])
final = (9, 9)


def set_window(window, obstacles):
    # set obstacles
    for i, j in obstacles:
        rect = pygame.Rect((i-1)*50+2, (j-1)*50+2, 48, 48)
        pygame.draw.rect(window, 'white', rect)

    # establishing grids
    for x in range(0, 500, CELL_DIM):
        pygame.draw.line(window, 'white', (x, 0), (x, HEIGHT), 2)
        pygame.draw.line(window, 'white', (0, x), (WIDTH, x), 2)


# set endpoints
def endpoints(window):
    # set start point
    rect = pygame.Rect((start[0] - 1) * CELL_DIM + 2, (start[1] - 1) * CELL_DIM + 2, CELL_DIM - 2, CELL_DIM - 2)
    pygame.draw.rect(window, 'green', rect)

    # set end point
    rect = pygame.Rect((final[0] - 1) * CELL_DIM + 2, (final[1] - 1) * CELL_DIM + 2, CELL_DIM - 2, CELL_DIM - 2)
    pygame.draw.rect(window, 'red', rect)


# run event function
def run(a, b, c, d, app):
    global q, final, start
    start = (int(a), int(b))
    final = (int(c), int(d))
    q.append([start])
    app.quit()
