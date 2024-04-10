import numpy as np
from ddaline import ddaline # ddaline(matrix, xi, yi, xf, yf, color=0x000000)
from setpixel import setpixel

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
        poligono = self.poligono
        tamanho = len(poligono)-1

        for i in range(0, tamanho):
            ddaline(matrix, poligono[i].x, poligono[i].y, poligono[i+1].x, poligono[i+1].y)
            # print(poligono[i].x, poligono[i].y)
            # print(poligono[i+1].x, poligono[i+1].y)

        ddaline(matrix, poligono[tamanho].x, poligono[tamanho].y, poligono[0].x, poligono[0].y)
        # print(poligono[tamanho].x, poligono[tamanho].y)
        # print(poligono[0].x, poligono[0].y)

        # print(poligono[tamanho].x, poligono[tamanho].y)


# novopol = criapoligono()
# novopol.insereponto(20, 40)
# print(novopol.poligono[0].x)