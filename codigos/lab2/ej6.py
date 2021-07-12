# Se quiere usar la formula de iteracion x_n+1_ = 2^x_n−1_ para resolver la ecuacion 2x = 2^x.
# Utilizar la funcion del ejercicio anterior para investigar si converge; y en caso afirmativo,
# estudiar hacia que valores lo hace para distintas elecciones de x0, tomando un numero
# maximo de 100 iteraciones y un error menor a 10^−5. Usar la siguiente sintaxis:
# hx = ripf(fun_lab2ej6, x0, 1e-5, 100)


import math
import argparse

from ej5_puntoFijo import ripf


def fun_lab2ej6(x):
    # 2x = 2^x <=> x = 2^x-1
    try:
        fx = math.pow(2, x - 1)
    except OverflowError:
        fx = float('inf')
    return fx


def main(x0s):
    for x0 in x0s:
        hx = ripf(fun_lab2ej6, x0, 1e-5, 100)
        print(f"x0 = {x0}:\t{hx[-1]}")


if __name__ == "__main__":
    # La ecuacion x=2^x-1 tiene 2 puntos fijos p1 = 1 y p2 = 2
    # Vamos a ver que pasas en los casos
    # x0 < 1,  ejemplo: [0.75, 0, -1, -5 ]
    # 1 < x0 < 2, ejemplo: [1.25, 1.5, 1.75, 1.9]
    # x0 > 2, ejemplo: [2.1, 2.25, 2.85, 4, 7]
    # se correran por default estos ejemplos, pero se pueden probar por argumentos (linea de comando) los valores que
    # se quieran (ver help -h)
    parser = argparse.ArgumentParser()
    parser.add_argument("-x0", nargs="*",
                        help="Los x0 iniciales para estudiar sus convergencias. Ej -x0 2 3.1 4 5.5 ", type=float,
                        default=[0.75, 0.0, -1, -5, 1.25, 1.5, 1.75, 1.9, 2.1, 2.25, 2.85, 4, 7])
    print(parser.parse_args().x0)
    main(parser.parse_args().x0)
