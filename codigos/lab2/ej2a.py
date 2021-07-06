# Importamos nuestra implementación de bisección
from ej1 import rbisec
from math import tan


# a) Encontrar la menor solucion positiva de la ecuacion
# 2x = tan(x) con un error menor a 10−5 en menos de 100 iteraciones.
# ¿Cuantas iteraciones son necesarias cuando comenzamos con el intervalo [0.8, 1.4]?
# Usar la siguiente sintaxis:
# hx, hy = rbisec(fun_lab2ej2a, [0.8, 1.4], 1e-5, 100)
def fun_lab2ej2a(x):
    """
    Funcion que nos devuelve
    """
    return tan(x) - 2 * x


if __name__ == "__main__":
    hx, hy = rbisec(fun_lab2ej2a, [0.8, 1.4], 1e-5, 100)
    # Imprimimos en pantalla el último valor de x
    print(f"x = {hx[-1]}. Hicieron falta {len(hx)} iteraciones")
