import numpy as np

# Iremos definir nossa matrix largura x altura x 3 (rgb)
# Temos que nos atentar que a quantidade de linhas irá definir a altura, e as colunas a largura
def matrix(linhas, colunas){

    return np.ndarray(shape=(linhas, colunas, 3), dtype=int)

}