# Example file showing a basic pygame "game loop"
import pygame
import numpy as np
from bresenhamline import bresenhamline
from ddaline import ddaline
from poligono import criapoligono

# pygame setup
pygame.init()

matrix = np.ndarray(shape=(600, 480), dtype=int) # 600 columns and 400 lines
matrix.fill(0x8AE2EC) #preencher a tela com uma cor

screen = pygame.display.set_mode((len(matrix), len(matrix[0]))) # (largura, altura) (x, y) (colunas, linhas)
clock = pygame.time.Clock()
running = True

quadrado = criapoligono()
quadrado.insereponto(30, 30)
quadrado.insereponto(80, 30)
quadrado.insereponto(80, 80)
quadrado.insereponto(30, 80)
quadrado.desenhapoligono(matrix)

triangulo = criapoligono()
triangulo.insereponto(250, 300)
triangulo.insereponto(350, 100)
triangulo.insereponto(450, 300)
triangulo.desenhapoligono(matrix)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Aqui iremos fazer nosso cenário etc... ------------------------------------------------------------------------------------------

    # bresenhamline(matrix, 200, 0, 0, 202, 0xff0000)
    # ddaline(matrix, 0, 100, 300, 0, 0xffffff)

    # Fim do cenário-------------------------------------------------------------------------------------------------------------------

    #copy matrix to framebuffer
    pygame.pixelcopy.array_to_surface(screen, matrix)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(30)  # limits FPS to 60

pygame.quit()