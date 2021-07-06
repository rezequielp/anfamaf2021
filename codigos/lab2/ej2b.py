# Importamos nuestra implementación de bisección
from ej1 import rbisec


def fun_lab2ej2b(x):
    """
    Función que nos devuelve la raíz cuadrada de x menos 3, para encontrar x**2 = 3.
    """
    return x ** 2 - 3


if __name__ == "__main__":
    # Obtenemos nuestro historial de puntos y evaluaciones
    hx, hf = rbisec(fun_lab2ej2b, [0, 2], 1e-5, 100)
    # Imprimimos en pantalla el último valor de x
    print(hx[-1])
