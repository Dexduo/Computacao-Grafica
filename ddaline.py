def ddaline(matrix, xi, yi, xf, yf, color=0x000000):
    xmax = len(matrix) - 1
    ymax = len(matrix[0]) - 1

    if(xi < 0 or xi > xmax or yi < 0 or yi > ymax or xf < 0 or xf > xmax or yf < 0 or yf > ymax):
        return
    
    dx = xf - xi
    dy = yf - yi

    if abs(dx) > abs(dy):
        steps = abs(dx)
    else:
        steps = abs(dy)

    xsteps = dx/steps
    ysteps = dy/steps

    x = xi
    y = yi

    matrix[round(x)][round(y)] = color

    for s in range(steps):
        x = x + xsteps
        y = y + ysteps
        
        matrix[round(x)][round(y)] = color