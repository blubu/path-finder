
import pygame
from collections import deque

pygame.init()

WIDTH = 500
HEIGHT = 500
BACKGROUND = (0, 0, 0)
running = True
q = deque()
q.append([(2, 2)])
final = (9, 9)
visited = []
colored = []
r = [-1, 0, 1, 0]
c = [0, 1, 0, -1]


window = pygame.display.set_mode((WIDTH, HEIGHT))
window.fill(BACKGROUND)
pygame.display.set_caption('My game')

rect = pygame.Rect(52, 52, 48, 48)
pygame.draw.rect(window, 'green', rect)
rect = pygame.Rect(402, 402, 48, 48)
pygame.draw.rect(window, 'red', rect)

grids = [(4, 7), (5, 6), (6, 5), (7, 4)]

for i, j in grids:
    rect = pygame.Rect((i-1)*50+2, (j-1)*50+2, 48, 48)
    pygame.draw.rect(window, 'white', rect)

for x in range(0, 500, 50):
    pygame.draw.line(window, 'white', (x, 0), (x, HEIGHT), 2)
    pygame.draw.line(window, 'white', (0, x), (WIDTH, x), 2)












while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False







        elif event.type == pygame.MOUSEBUTTONDOWN:
            found = False
            while not found:
                pos = q.popleft()
                i = pos[-1]
                visited.append(i)


                for j in range(0, 4):
                    new_r = i[0] + r[j]
                    new_c = i[1] + c[j]
                    new_pos = (new_r, new_c)


                    if new_pos in visited or new_pos in grids:
                        continue
                    elif new_r > 10 or new_c > 10:
                        continue
                    elif new_r < 1 or new_c < 1:
                        continue


                    if new_pos == final:
                        print('reached')
                        print(pos)
                        found = True
                    else:
                        old_pos = pos.copy()
                        old_pos.append(new_pos)
                        q.append(old_pos)
                        rect = pygame.Rect((new_r - 1) * 50+2, (new_c - 1) * 50+2, 48, 48)
                        pygame.draw.rect(window, 'blue', rect)
                        colored.append(new_pos)

                    pygame.display.update()
                    pygame.time.Clock().tick(200)
















    pygame.display.update()

pygame.quit()
