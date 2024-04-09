import numpy as np

class ponto:
    def __init__(self, x, y, color=0x000000):
        self.x = x
        self.y = y
        self.color = color

poligono = np.array([])

poligono = np.append(poligono, ponto(13, 16, 0x0000ff))
poligono = np.append(poligono, ponto(80, 40, 0x00ff00))
poligono = np.append(poligono, ponto(80, 40, 0x00f300))

print(poligono)

for i in poligono:
    print(i.x)

#=============================================================================
# pontos = np.array([])

#pontos.append([175, 200])

# pontos = np.append(pontos, np.array([175, 200]))
# pontos = np.append(pontos, [80, 100])

# np.concatenate(pontos, np.array([175, 200]))

# print(pontos)