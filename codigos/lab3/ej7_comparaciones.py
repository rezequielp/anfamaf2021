# Para la comparacion de performance vamos a utilizar el ejercicio 7 del practico 2
import math

import numpy as np
from matplotlib import pyplot as plt

from codigos.lab2 import ej7
from codigos.lab3.ej7_rinterp import rinterp


def lab3ej7interp(x):
    # calcula u(x) = y
    fun = lambda y: y - math.exp(-(1 - x * y) ** 2)
    hy, hu = rinterp(fun, 0.0, 1.0, 1.5, 1e-6, 100)
    y = hy[-1]
    return y


def main():
    x = np.linspace(0.0, 1.5, 100)
    # h = 1.5/99
    # x = [i*h for i in range(100)]

    y_bisec = [ej7.lab2ej7bisec(xi) for xi in x]
    y_newton = [ej7.lab2ej7newton(xi) for xi in x]
    y_ipf = [ej7.lab2ej7ipf(xi) for xi in x]
    y_interp = [lab3ej7interp(xi) for xi in x]

    # fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
    fig = plt.figure()
    gs = fig.add_gridspec(1, 4, hspace=0, wspace=0)
    ax1, ax2, ax3, ax4 = gs.subplots(sharex='col', sharey='row')
    ax1.plot(x, y_bisec, 'g')
    ax2.plot(x, y_newton, 'r')
    ax3.plot(x, y_ipf, 'b')
    ax4.plot(x, y_interp, 'y')
    ax1.set_title('biseccion')
    ax2.set_title('newton')
    ax3.set_title('punto fijo')
    ax4.set_title('interpolacion')
    fig.suptitle('Lab3 - Ejercicio 7', fontsize=14)

    for ax in fig.get_axes():
        ax.set(xlabel='x-label', ylabel='y-label')
    # Hide x labels and tick labels for top plots and y ticks for right plots.
    for ax in fig.get_axes():
        ax.label_outer()

    plt.show()


if __name__ == "__main__":
    main()