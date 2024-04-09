import numpy as np
from ddaline import ddaline

class ponto:
    def __init__(self, x, y, color=0x000000):
        self.x = x
        self.y = y
        self.color = color

class criapoligono:
    def __init__(self):
        self.poligono = np.array([])

    def insereponto(self, x, y, color=0x000000):
        self.poligono = np.append(self.poligono, ponto(x, y, color))
    
    def desenhapoligono(self, matrix):
        for i in self.poligono:
            # ddaline(matrix, i.x)
            print()

# novopol = criapoligono()
# novopol.insereponto(20, 40)
# print(novopol.poligono[0].x)

