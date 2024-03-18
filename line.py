def line(matrix, xi, xf, yi, yf, color=0): # lembre-se que x não pode ultrapassar o tamanho da largura
                                           # assim como y não pode ultrapassar o tamanho da altura
    xmax = len(matrix) - 1
    ymax = len(matrix[0]) - 1

    if(xi < 0 or xi > xmax or yi < 0 or yi > ymax or xf < 0 or xf > xmax or yf < 0 or yf > ymax):
        return
    
    dx = abs(xf - xi)
    dy = abs(yf - yi)

    slope = dy > dx

    if(dy > dx): # if line greater 45 degrees
        xi, yi = yi, xi
        xf, yf = yf, xf
    
    if(xi > xf): # the breseham algorithm only works from left to right
        xi, xf = xf, xi
        yi, yf = yf, yi

    # now that we normalize coordinates according to breseham we will get the new dx dy
    dx = abs(xf - xi)
    dy = abs(yf - yi)

    error = dx // 2
    y = yi
    ystep = 1 if yi < yf else -1

    for x in range(xi, xf + 1):
        coord = (y, x) if slope else (x, y)

        if slope:
            matrix[y][x] = 0x000000
        else:
            matrix[x][y] = 0x000000

        error -= dy
        if error < 0:
            y += ystep
            error += dx