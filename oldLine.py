import numpy as np

def line(matrix, xi, xf, yi, yf, color=0):

    if(xf < xi):
        # aux = xf
        # xf = xi
        # xi = aux
        # aux = yf
        # yf = yi
        # yi = aux

        xf, xi = xi, xf
        yf, yi = yi, yf
    
    dx = abs(xf - xi)
    dy = abs(yf - yi)

    aux = 0
    if(dy > dx):
        # aux = dx
        # dx = dy
        # dy = aux
        # aux = 1

        dx, dy = dy, dx
        aux = 1

    y = 0

    dy2 = 2*dy
    dy2dx2 = dy2 - 2*dx
    s = np.sign(yf-yi)

    p = dx - dy2

    for x in range(0, dx):

        if(p < 0):
            p = p - dy2dx2
            y = y + 1
        else:
            p = p - dy2
    
        if aux == 0:
            for i in range(0, 3):
                matrix[xi+x][yi+s*y][i] = color
        else:
            for i in range(0, 3):
                matrix[xi+y][yi+s*x][i] = color