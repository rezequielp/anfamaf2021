# Obtener los datos almacenados en los archivos datos3a.dat y datos3b.dat para realizar
# el ajuste de los siguientes modelos, es decir, determinar los coeficientes de cada modelo:
# a) y(x) = Cx^A,
# b) y(x) = x /( Ax + B )
# Ayuda: Transformar en cada caso la expresion dada a un modelo lineal, y obtener una recta que
# mejor ajusta los datos (transformados) en el sentido de mınimos cuadrados.

import numpy as np
import matplotlib.pyplot as plt

datos = np.loadtxt('../../datos/lab4/datos3b.dat')
# se quita el primer elemento porque arruina el ejercicio
x = datos[0, 1:]
y = datos[1, 1:]
# y = x /( Ax + B ) =>   1/y = (Ax + B)/x
#                        1/y = A + B*1/x
# y_p = 1/y
# x_p = 1/x         => y_p = B * x_p + A

# se utiliza np.divide para que sea una division precisa
y_p = np.divide(1, y)
x_p = np.divide(1, x)

B, A = np.polyfit(x_p, y_p, 1)

print(f'Coef. A = {A}, Coef B = {B}.')

fig, ax = plt.subplots(2, 1)

ax[0].plot(x_p, y_p, '.r')
ax[0].plot(x_p, A + B * x_p)
ax[0].legend(['Correción lineal del ajuste'])

ax[1].plot(x, y, '.r')
ax[1].plot(x, np.divide(x, A * x + B))
ax[1].legend(['Ajuste sobre los datos'])

plt.show()