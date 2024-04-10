import sys
sys.path.insert(0, '..')
from poligono import criapoligono
import numpy as np

matrix = np.ndarray(shape=(600, 480), dtype=int) # 600 columns and 400 lines
matrix.fill(0x8AE2EC) #preencher a tela com uma cor

quadrado = criapoligono()
quadrado.insereponto(30, 30)
quadrado.insereponto(80, 30)
quadrado.insereponto(80, 80)
quadrado.insereponto(30, 80)
quadrado.desenhapoligono(matrix)