import pygame.display

# importing modules
from data import *
from window import dialogue_window

# start game
pygame.init()

# create clock
clock = pygame.time.Clock()

# create window
window = pygame.display.set_mode((WIDTH, HEIGHT))
window.fill(BACKGROUND)
pygame.display.set_caption('My game')

# setting the window
set_window(window, grids)
# dialogue_window(run)
endpoints(window)

# game loop
while running:
    for event in pygame.event.get():
        # close button
        if event.type == pygame.QUIT:
            running = False
        # enter key
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                found = False

                # start algorithm
                while not found:

                    path = heapq.heappop(pq)[2]
                    print(path)

                    path_found = False
                    for z in range(4):
                        new_pos = (path[0] + row[z],
                                   path[1] + col[z])

                        if new_pos in visited or new_pos in grids:
                            continue
                        elif new_pos[0] > 10 or new_pos[0] < 1 or new_pos[1] > 10 or new_pos[1] < 1:
                            continue

                        # checking for end
                        if new_pos == final:
                            found = True
                            path_found = True
                            print('found')
                            break
                        else:
                            # calculating parameters
                            g = pq_dict[path] + 1
                            f = abs(final[0] - new_pos[0]) + abs(final[1] - new_pos[1])
                            pq_dict[new_pos] = g
                            count += 1
                            n_count -= 1
                            print(f"{new_pos} : {f+g}")

                            # adding the new cell to the path
                            heapq.heappush(pq, (f+g, n_count, new_pos))
                            visited.append(new_pos)
                            prev[new_pos] = path

                            # color current cell
                            rect = pygame.Rect((new_pos[0] - 1) * 50 + 2, (new_pos[1] - 1) * 50 + 2, 48, 48)
                            pygame.draw.rect(window, 'blue', rect)

                    # if not path_found:
                    #     removed_pos = stack.pop()
                    #     rect = pygame.Rect((removed_pos[0] - 1) * 50 + 2, (removed_pos[1] - 1) * 50 + 2, 48, 48)
                    #     pygame.draw.rect(window, 'grey', rect)

                    pygame.display.update()
                    clock.tick(FRAME)

            for cell in stack[1:]:
                rect = pygame.Rect((cell[0] - 1) * 50 + 2, (cell[1] - 1) * 50 + 2, 48, 48)
                pygame.draw.rect(window, 'yellow', rect)
                pygame.display.update()
                clock.tick(FRAME)

    pygame.display.update()

pygame.quit()
