# El polinomio interpolante se puede ver afectado por el conjunto de puntos elegidos.
# Considerar la funcion f tal que f(x) = 1/(1 + 25x^2).
# Graficar f, pn y qn en una misma figura usando 200 puntos igualmente espaciados en el
# intervalo [−1, 1], donde:
#
# (a) pn es el polinomio que interpola los pares {(xi, f(xi))} i=1...n+1 con
# xi = (2(i − 1)/n) − 1, para i = 1, . . . , n + 1.
#
# (b) qn es el polinomio que interpola los pares {(xi, f(xi))} i=0...n con
# xi = cos((2i + 1)/(2n + 2) * π) para i = 0, ..., n. Estos puntos son conocidos como nodos de Tchebychev.
# Varıe n entre 1 y 15. Implementar la resolucion de este ejercicio en el script “lab3ej4”.
# Al ejecutarlo debe mostrar 15 graficos

from ej2_inewton import inewton
from math import cos, pi
import matplotlib.pyplot as plt

f = lambda x: 1 / (1 + 25 * x ** 2)

# -1,-0.5,0,0.5,1 -> (b-a)=1-(-1) = 2 -> 2/(n-1) = 2/4 = 1/2
a = -1
b = 1
n = 200
# (b-a)/n-1
h = (b - a) / (n - 1)
x_plot = [-1 + i * h for i in range(200)]

f_plot = [f(x) for x in x_plot]

fig = plt.figure()

axes = []

for n in range(1, 16):
    # interpolación de p
    x_inter_p = [(2 * (i - 1) / n) - 1 for i in range(1, n + 2)]
    f_inter_p = [f(x) for x in x_inter_p]
    p_plot = inewton(x_inter_p, f_inter_p, x_plot)

    # interpolación de q
    x_inter_q = [cos(pi * (2 * i + 1) / (2 * n + 2)) for i in range(n + 1)]
    f_inter_q = [f(x) for x in x_inter_q]
    q_plot = inewton(x_inter_q, f_inter_q, x_plot)

    axes.append(fig.add_subplot(5, 3, n))  # fila, columna, idx
    axes[-1].plot(x_plot, f_plot, 'g')
    axes[-1].plot(x_plot, p_plot, 'r')
    axes[-1].plot(x_plot, q_plot, 'b')
    axes[-1].grid()

fig.suptitle('Lab3 - Ejercicio 4', fontsize=12)
fig.legend("fpq")
plt.show()
