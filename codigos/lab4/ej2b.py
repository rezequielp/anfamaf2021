# Para las siguientes funciones generar un conjunto de datos
# (xi, yi), i = 1, . . . , 50 y realizar
# un ajuste polinomial de grado n con n = 0, . . . , 5:
# (a) f(x) = arcsen(x), x ∈ [0, 1],
# (b) g(x) = cos(x), x ∈ [0, 4π].
# Estudiar en cada caso la suma de los residuos

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# funcion
fun = lambda x: np.cos(x)

# Generamos 50 puntos en el intervalo [0, 1]
x = np.linspace(0, 1, 50)
y = fun(x)

# Hacemos un ajuste polinomial de grado n = 0,...,5
polinomios = []
residuos = []

fig = plt.figure()
axes = []
color = iter(cm.rainbow(np.linspace(0, 1, 6)))
for n in range(6):
    # ajuste
    polinomios.append(np.polyfit(x, y, n))
    # evaluamos el polinomio n en los x
    y_pol = np.polyval(polinomios[n], x)
    # calculamos el residuo (error cuadrático)
    residuos.append(sum((y - y_pol) ** 2))
    # para graficar el polinomio
    axes.append(fig.add_subplot(3, 2, n + 1))  # fila, columna, idx
    axes[-1].plot(x, y, color="black", linestyle='dashed')
    axes[-1].plot(x, y_pol, color=next(color), label=f"p{n}")
    axes[-1].grid()

# mostramos los residuos para compararlos visualmente
print(residuos)
# plot
fig.suptitle('Lab4 - Ejercicio 2b', fontsize=12)
fig.legend()
plt.show()
