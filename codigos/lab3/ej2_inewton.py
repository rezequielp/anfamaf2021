# Realizar una funcion en python analoga a la del ejercicio 1 pero utilizando la forma de
# Newton del polinomio interpolante, calculando los coeficientes mediante diferencias divididas.
# La funcion debe llamarse “inewton”
from codigos.lab3.ej2_matriz_coef import matriz_coef
from fun_dif_divididas import dif_divididas

def inewton(x, y, z):
    if len(x) != len(y):
        print("X e Y no tienen la misma longitud, chau")
        return None
    coefs = dif_divididas(x, y)
    # coefs = matriz_coef(x, y)

    # w = [polinomio(zj) for zj in z]
    w = [horn_newton(zj, x, coefs) for zj in z]
    return w


def horn_newton(zj, x, coefs):
    n = len(coefs)
    valor = coefs[n - 1]
    for i in range(n - 2, -1, -1):
        valor = coefs[i] + (zj - x[i]) * valor
    return valor

# c_0 + c_1 (z - x_0) + c_2 * (z - x_0) * (z - x_1) + ...
# c_0 + (z - x_0) [ c_1 + c_2 * (z - x_1) + ... ]
# c_0 + (z - x_0) [ c_1 + c_2 * (z - x_1) + c_3 * (z - x_1) * (z - x_2) + ... ]
# c_0 + (z - x_0) [ c_1 + (z - x_1) * [c_2 + c_3 * (z - x_2) + ...  ] ]

#  (z - x_{k-2}) * [ c_{k-1} + c_k * (z - x_{k-1}) ]
#  (z - x_{k-2}) * [ c_{k-1} + (z - x_{k-1}) * [c_k] ]
