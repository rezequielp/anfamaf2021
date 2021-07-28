# calculo de coeficientes de newton con el metodo de diferencias divididas
# https://youtu.be/_LLTqw6GToE
# Un ejemplo con n = 4 puntos
# x0 | f[x0]    f[x0,x1]    f[x0,x1,x2] f[x0,x1,x2,x3]
# x1 | f[x1]    f[x1,x2]    f[x1,x2,x3]
# x2 | f[x2]    f[x2,x3]
# x3 | f[x3]
# Iniciamos con los valores de y en coefs (serìan los f[xi])
# coefs = [f[x0], f[x1], f[x2], f[x3]]
# Entonces en cada iteracion (n-1 iteraciones) se obtiene
# i = 0 : coefs = [f[x0], f[x0,x1], f[x1,x2] , f[x2,x3]]
# i = 1 : coefs = [f[x0], f[x0,x1], f[x0,x1,x2] , f[x1,x2,x3]]
# i = 2 : coefs = [f[x0], f[x0,x1], f[x0,x1,x2] , f[x0,x1,x2,x3]]


def dif_divididas(x, y):
    n_coef = len(x)
    coefs = y.copy()

    for i in range(n_coef - 1):
        for j in reversed(range(i + 1, n_coef)):
            coefs[j] = (coefs[j] - coefs[j - 1]) / (x[j] - x[j - i - 1])
    return coefs
