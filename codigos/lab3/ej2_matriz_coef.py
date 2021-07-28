# calculo de coeficientes de newton con una matriz de coeficientes
# x0    | c00   c01 c02 c03 ... c0,n−1 c0,n
# x1    | c10   c11 c12 c13 ... c1,n−1
# x2    | c20   c21 c22 c23 ...
# ... ... ... ... ...
# ... ... ... ...
# xn−1  | cn−1,0 cn−1,1
# xn    | cn,0

def matriz_coef(x, y):
    n = len(y)  # cantidad de puntos a interpolar

    matriz_coefs = [[0.0] * m for m in range(n, 0, -1)]

    for i in range(n):
        matriz_coefs[i][0] = y[i]

    for j in range(1, n):
        for i in range(0, n - j):
            matriz_coefs[i][j] = (matriz_coefs[i + 1][j - 1] - matriz_coefs[i][j - 1]) / (x[i + j] - x[i])

    return matriz_coefs[0]
