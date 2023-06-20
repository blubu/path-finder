
# importing modules
from data import *
from window import dialogue_window

# start game
pygame.init()

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
                    new_colored = []
                    path = q.popleft()
                    cur_pos = path[-1]

                    for z in range(4):
                        new_pos = (cur_pos[0] + row[z],
                                   cur_pos[1] + col[z])
                        print(new_pos)
                    break



    # update display
    pygame.display.update()

pygame.quit()
