# Obtener los datos almacenados en los archivos datos3a.dat y datos3b.dat para realizar
# el ajuste de los siguientes modelos, es decir, determinar los coeficientes de cada modelo:
# a) y(x) = Cx^A,
# b) y(x) = x /( Ax + B )
# Ayuda: Transformar en cada caso la expresion dada a un modelo lineal, y obtener una recta que
# mejor ajusta los datos (transformados) en el sentido de mınimos cuadrados.

import numpy as np
import matplotlib.pyplot as plt

datos = np.loadtxt('../../datos/lab4/datos3a.dat')
x = datos[0]
y = datos[1]

# y = C * x ** A => ln(y) = ln(C * x ** A)
#                   ln(y) = ln(C) + A * ln(x)
# y_p = ln(y)
# x_p = ln(x)
# B = ln(C)      => y_p = A * x_p + B
y_p = np.log(y)
x_p = np.log(x)

A, B = np.polyfit(x_p, y_p, 1)
C = np.exp(B)

print(f'Coef. A = {A}, Coef C = {C}.')

fig, ax = plt.subplots(2, 1)

ax[0].plot(x_p, y_p, '.r')
ax[0].plot(x_p, A * x_p + B)
ax[0].legend(['Correción lineal del ajuste'])

ax[1].plot(x, y, '.r')
ax[1].plot(x, C * x ** A)
ax[1].legend(['Ajuste sobre los datos'])

plt.show()

