# Example file showing a basic pygame "game loop"
import pygame
import numpy as np
from math import sin
from bresehamline import bresehamline
from ddaline import ddaline

# pygame setup
pygame.init()

matrix = np.ndarray(shape=(600, 480), dtype=int) # 600 columns and 400 lines
matrix.fill(0x8AE2EC)

screen = pygame.display.set_mode((len(matrix), len(matrix[0]))) # (largura, altura) (x, y) (colunas, linhas)
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    line(matrix, 200, 0, 0, 202)
    ddaline(matrix, 0, 100, 300, 0, 0xffffff)
    pygame.pixelcopy.array_to_surface(screen, matrix)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(30)  # limits FPS to 60

pygame.quit()