# Example file showing a basic pygame "game loop"
import pygame
import numpy as np
from math import sin
from line import line

# pygame setup
pygame.init()

matrix = np.ndarray(shape=(600, 400, 3), dtype=int) # 600 columns and 400 lines
matrix.fill(255)

screen = pygame.display.set_mode((600, 400)) # (largura, altura)
clock = pygame.time.Clock()
running = True

animation = 5
sign = 1

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    #screen.fill("white")

    # RENDER YOUR GAME HERE

    #animation+=sign

    #if(animation==40):
     #   sign*=-1
  #  if(animation==5):
    #    sign*=-1

    #for x in range(0, 600): # we get the number of columns, that is the same as our width
    #    value = int(199+(sin(x/animation)*199))
    #    for j in range(0, 3):
      #      matrix[x][value][j] = 0

    line(matrix, 100, 200, 100, 500)
    pygame.pixelcopy.array_to_surface(screen, matrix)

    matrix.fill(255)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(30)  # limits FPS to 60

pygame.quit()