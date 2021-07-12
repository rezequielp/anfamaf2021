# c) Graficar conjuntamente f y los pares (xk, f(xk)) para las dos funciones anteriores y
# con al menos dos intervalos iniciales distintos para cada una.

# Importamos el módulo de gráficos de matplotlib
import matplotlib.pyplot as plt
from ej2a import *
from ej2b import *


def graficar_ej2a():
    ahx, ahf = rbisec(fun_lab2ej2a, [0.8, 1.4], 1e-5, 100)
    # Graficamos el historial de puntos con marcador estrella
    ax[0].plot(ahx, ahf, '*')
    ax[0].axhline(y=0, color='gray', linestyle='--', linewidth=1)
    ax[0].axvline(x=ahx[-1], color='gray', linestyle='--', linewidth=1)
    # Creamos una lista de 7 puntos equiespaciados entre 0.8 y 1.4 y sus valores:
    # puntos = [0.8, 0.9, 1.0, ... , 1.3, 1.4]
    # evals = [f(0.8), f(0.9), ..., f(1.3), f(1.4)]
    puntos = []
    evals = []
    for idx in range(0, 13):
        puntos.append(0.8 + idx * 0.05)
        evals.append(fun_lab2ej2a(0.8 + idx * 0.05))
    # Graficamos puntos en X y evals en Y
    ax[0].plot(puntos, evals, label="tan(x) - 2x")
    ax[0].legend()


def graficar_ej2b():
    bhx, bhf = rbisec(fun_lab2ej2b, [0, 2], 1e-5, 100)
    # Graficamos el historial de puntos con marcador estrella
    ax[1].plot(bhx, bhf, '*')
    ax[1].axhline(y=0, color='gray', linestyle='--', linewidth=1)
    ax[1].axvline(x=bhx[-1], color='gray', linestyle='--', linewidth=1)
    # Creamos una lista de 21 puntos equiespaciados entre 0 y 2 y sus valores:
    # puntos = [0, 0.1, 0.2, ... , 1.9, 2]
    # evals = [f(0), f(0.1), ..., f(1.9), f(2)]
    puntos = []
    evals = []
    for idx in range(0, 21):
        puntos.append(idx * 0.1)
        evals.append(fun_lab2ej2b(idx * 0.1))

    # Graficamos puntos en X y evals en Y
    ax[1].plot(puntos, evals, label="x^2 - 3")
    ax[1].legend()


if __name__ == "__main__":
    fig, ax = plt.subplots(2, 1)
    graficar_ej2a()
    graficar_ej2b()
    # Mostramos ambos gráficos al mismo tiempo
    plt.show()
