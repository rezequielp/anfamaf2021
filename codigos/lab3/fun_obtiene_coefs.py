# Escriba una funcion rinterp(fun,x0,x1,x2,err,mit) que encuentre un cero de la funcion
# fun de la siguiente forma. En cada paso, sea q2 el polinomio interpolante cuadratico de los
# puntos (xn−2, f(xn−2)), (xn−1, f(xn−1)) y (xn, f(xn)). Elegir como xn+1 al cero de q2 que
# este mas cerca de xn. Comparar su performance con los metodos para encontrar raıces del
# laboratorio 2

# from ej1_ilagrange import ilagrange
from codigos.lab3.ej1_ilagrange import ilagrange
from codigos.lab3.ej2_inewton import inewton


def obtiene_coefs(x, y):
    # x = [x1, x2, x3]
    # y = [y1, y2, y3]
    z = [0, 1, -1]
    c, ab1, ab2 = ilagrange(x, y, z)
    # ab1 = a+b+c
    ab1 = ab1 - c
    # ab2 = a-b+c
    ab2 = ab2 - c
    a = (ab1 + ab2) / 2
    b = (ab2 - ab1) / 2
    return a, b, c
