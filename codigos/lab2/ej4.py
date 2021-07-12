# Escribir una funcion que, ingresando a > 0, retorne una aproximacion de 3√a (raiz cubica de a).
# La aproximacion debe realizarse usando el metodo de Newton del ejercicio anterior para resolver
# x^3 − a = 0 con un error menor a 10^−6 mediante el uso de la funcion x → x3 − a
import sys

from ej3_netwon import rnewton
from functools import partial


def fun_lab2ej4(x, a):
    fx = (x ** 3) - a
    dfx = 3 * (x ** 2)
    return fx, dfx


def resolver_ej4(aValued):
    funej4 = partial(fun_lab2ej4, a=aValued)
    # funej4 = lambda x: fun_ej4(x, aValued)
    hx, hf = rnewton(funej4, 0.1, 1e-6, 200)
    # Imprimimos en pantalla el último valor de x
    print(f"Usando el método de Netwon, la aproximación a 3√{aValued} es {hx[-1]}")


def main(argv):
    a = float(input("ingrese el valor de a > 0: "))
    if a <= 0:
        print("a no es mayor a 0")
        return None
    resolver_ej4(a)


if __name__ == "__main__":
    main(sys.argv[1:])
