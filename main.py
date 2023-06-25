import pygame

# importing modules
from data import *
from window import DialogueWindow
from collections import deque
import heapq

# start game
pygame.init()

# create window
game_window = pygame.display.set_mode((WIDTH, WIDTH))
game_window.fill(BACKGROUND)
pygame.display.set_caption('Path Algorithms')

# setting the window
set_game_window(game_window)
# dialog = DialogueWindow()
# start, final, algo_type = dialog.get_endpoints()
start = (2, 2)
final = (20, 22)
algo_type = 'a*'
obstacles.append(start)
endpoints(game_window, start, final)

# game loop
while running:
    # events
    for event in pygame.event.get():

        # close button
        if event.type == pygame.QUIT:
            running = False

        # mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                clicked_pos = get_position(event.pos)

                # adding obstacles
                if clicked_pos not in obstacles:
                    obstacles.append(clicked_pos)
                    rect = pygame.Rect((clicked_pos[0] - 1) * CELL_DIM + 2, (clicked_pos[1] - 1) * CELL_DIM + 2,
                                       CELL_DIM - 2, CELL_DIM - 2)
                    pygame.draw.rect(game_window, 'black', rect)

                # removing obstacles
                else:
                    obstacles.remove(clicked_pos)
                    rect = pygame.Rect((clicked_pos[0] - 1) * CELL_DIM + 2, (clicked_pos[1] - 1) * CELL_DIM + 2,
                                       CELL_DIM - 2, CELL_DIM - 2)
                    pygame.draw.rect(game_window, BACKGROUND, rect)

        if event.type == pygame.MOUSEMOTION:
            clicked_pos = get_position(event.pos)

            # adding obstacles
            if event.buttons[0]:
                if clicked_pos not in obstacles:
                    obstacles.append(clicked_pos)
                    rect = pygame.Rect((clicked_pos[0] - 1) * CELL_DIM + 2, (clicked_pos[1] - 1) * CELL_DIM + 2,
                                       CELL_DIM - 2, CELL_DIM - 2)
                    pygame.draw.rect(game_window, 'black', rect)

            # removing obstacles
            if event.buttons[2]:
                if clicked_pos in obstacles:
                    obstacles.remove(clicked_pos)
                    rect = pygame.Rect((clicked_pos[0] - 1) * CELL_DIM + 2, (clicked_pos[1] - 1) * CELL_DIM + 2,
                                       CELL_DIM - 2, CELL_DIM - 2)
                    pygame.draw.rect(game_window, BACKGROUND, rect)

        # enter key
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                found = False

                # breadth first search
                if algo_type == 'bfs':
                    # initialisation
                    q = deque()
                    q.append([start])
                    colored = []

                    while not found:
                        new_colored = []
                        path = q.popleft()
                        cur_pos = path[-1]

                        # de-color visited cells
                        for cells in colored:
                            rect = pygame.Rect((cells[0] - 1) * CELL_DIM + 2, (cells[1] - 1) * CELL_DIM + 2,
                                               CELL_DIM - 2, CELL_DIM - 2)
                            pygame.draw.rect(game_window, 'brown', rect)

                        for z in range(4):
                            new_pos = (cur_pos[0] + row[z],
                                       cur_pos[1] + col[z])

                            if new_pos in visited or new_pos in obstacles:
                                continue
                            elif new_pos[0] > GRID or new_pos[0] < 1 or new_pos[1] > GRID or new_pos[1] < 1:
                                continue

                            # checking for end
                            if new_pos == final:
                                found = True
                                break
                            else:
                                # adding the new cell to the path
                                new_path = path.copy()
                                new_path.append(new_pos)
                                q.append(new_path)
                                visited.append(new_pos)

                                # color current cell
                                rect = pygame.Rect((new_pos[0] - 1) * CELL_DIM + 2, (new_pos[1] - 1) * CELL_DIM + 2,
                                                   CELL_DIM - 2, CELL_DIM - 2)
                                pygame.draw.rect(game_window, 'blue', rect)
                                new_colored.append(new_pos)

                        colored = new_colored.copy()

                        pygame.display.update()
                        clock.tick(FRAME)

                    # bfs path
                    if found:
                        for cell in path[1:]:
                            rect = pygame.Rect((cell[0] - 1) * CELL_DIM + 2, (cell[1] - 1) * CELL_DIM + 2,
                                               CELL_DIM - 2, CELL_DIM - 2)
                            pygame.draw.rect(game_window, 'yellow', rect)
                            pygame.display.update()
                            clock.tick(SLOW_FRAME)

                # depth first search
                elif algo_type == 'dfs':
                    # initialisation
                    stack = [start]

                    while not found:
                        path = stack[-1]
                        path_found = False

                        for z in range(4):
                            new_pos = (path[0] + row[z],
                                       path[1] + col[z])

                            if new_pos in visited or new_pos in obstacles:
                                continue
                            elif new_pos[0] > GRID or new_pos[0] < 1 or new_pos[1] > GRID or new_pos[1] < 1:
                                continue

                            # checking for end
                            if new_pos == final:
                                found = True
                                path_found = True
                                break
                            else:
                                # adding the new cell to the path
                                stack.append(new_pos)
                                visited.append(new_pos)

                                # color current cell
                                rect = pygame.Rect((new_pos[0] - 1) * CELL_DIM + 2, (new_pos[1] - 1) * CELL_DIM + 2,
                                                   CELL_DIM - 2, CELL_DIM - 2)
                                pygame.draw.rect(game_window, 'blue', rect)
                                path_found = True
                                break

                        if not path_found:
                            removed_pos = stack.pop()
                            rect = pygame.Rect((removed_pos[0] - 1) * CELL_DIM + 2, (removed_pos[1] - 1) * CELL_DIM + 2,
                                               CELL_DIM - 2, CELL_DIM - 2)
                            pygame.draw.rect(game_window, 'brown', rect)

                        pygame.display.update()
                        clock.tick(FRAME)

                    if found:
                        for cell in stack[1:]:
                            rect = pygame.Rect((cell[0] - 1) * CELL_DIM + 2, (cell[1] - 1) * CELL_DIM + 2,
                                               CELL_DIM - 2, CELL_DIM - 2)
                            pygame.draw.rect(game_window, 'yellow', rect)
                            pygame.display.update()
                            clock.tick(SLOW_FRAME)

                # a* algorithm
                elif algo_type == 'a*':
                    # initialisation
                    pq = []
                    heapq.heappush(pq, (0, 0, start))

                    pq_dict = {start: 0}
                    prev = {}
                    count = 0

                    while not found:
                        path = heapq.heappop(pq)[2]

                        for z in range(4):
                            new_pos = (path[0] + row[z],
                                       path[1] + col[z])

                            if new_pos in visited or new_pos in obstacles:
                                continue
                            elif new_pos[0] > GRID or new_pos[0] < 1 or new_pos[1] > GRID or new_pos[1] < 1:
                                continue

                            # checking for end
                            if new_pos == final:
                                found = True
                                break
                            else:
                                # calculating parameters
                                g = pq_dict[path] + 1
                                f = abs(final[0] - new_pos[0]) + abs(final[1] - new_pos[1])
                                pq_dict[new_pos] = g
                                count += 1

                                # adding the new cell to the path
                                heapq.heappush(pq, (f + g, -1 * count, new_pos))
                                visited.append(new_pos)
                                prev[new_pos] = path

                                # color current cell
                                rect = pygame.Rect((new_pos[0] - 1) * CELL_DIM + 2, (new_pos[1] - 1) * CELL_DIM + 2,
                                                   CELL_DIM - 2, CELL_DIM - 2)
                                pygame.draw.rect(game_window, 'blue', rect)

                                # de-color visited cell
                                if path != start:
                                    rect = pygame.Rect((path[0] - 1) * CELL_DIM + 2, (path[1] - 1) * CELL_DIM + 2,
                                                       CELL_DIM - 2, CELL_DIM - 2)
                                    pygame.draw.rect(game_window, 'brown', rect)

                        pygame.display.update()
                        clock.tick(FRAME)

                        if found:
                            print('found')
                            while path != start:
                                rect = pygame.Rect((path[0] - 1) * CELL_DIM + 2, (path[1] - 1) * CELL_DIM + 2,
                                                   CELL_DIM - 2, CELL_DIM - 2)
                                pygame.draw.rect(game_window, 'yellow', rect)
                                pygame.display.update()
                                clock.tick(SLOW_FRAME)
                                path = prev[path]

    pygame.display.update()

pygame.quit()
