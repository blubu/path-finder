
import pygame

pygame.init()

WIDTH = 500
HEIGHT = 500
BACKGROUND = (0, 0, 0)
running = True

window = pygame.display.set_mode((WIDTH, HEIGHT))
window.fill(BACKGROUND)
pygame.display.set_caption('My game')

for x in range(0, 500, 50):
    pygame.draw.line(window, 'white', (x, 0), (x, HEIGHT))
    pygame.draw.line(window, 'white', (0, x), (WIDTH, x))


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            x = mouse_x//50 + 1
            y = mouse_y//50 + 1
            pos = (x, y)
            print(pos)
    pygame.display.update()

pygame.quit()
