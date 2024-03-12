import numpy

matrix = numpy.ndarray(shape=(4, 6, 3), dtype=int)
matrix.fill(255)

#print(matrix)
print(matrix.shape)
print(len(matrix[0]))

for x in range(0, 6): # we get the number of columns, that is the same as our width
     for j in range(0, 3):
        matrix[2][x][j] = 0

print(matrix)