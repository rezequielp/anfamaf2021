# Italia es el paıs mas afectado por el Coronavirus,
# comenzando con 14 casos desde el 22 de febrero de
# 2020 y con una cantidad de infectados que crecio
# exponencialmente por mas de un mes.
# Obtener los datos almacenados en el archivo covid italia.csv
# y realizar un ajuste exponencial de la forma y(x) = ae^bx.
# Realizar un grafico que contenga los datos y su ajuste

import numpy as np
import matplotlib.pyplot as plt

y = np.loadtxt('../../datos/lab4/covid_italia.csv', delimiter=',', usecols=1)
x = np.arange(y.size)
# y(x) = ae^bx => ln(y) = ln(ae^bx)
#                 ln(y) = ln(a) + ln(e^bx)
#                 ln(y) = ln(a) + b*x
# y_p = ln(y)
# a_p = ln(a) =>  y_p = a_p + b*x
y_p = np.log(y)
b, a_p = np.polyfit(x, y_p, 1)
a = np.exp(a_p)

print(f'Coef. a = {a}, Coef b = {b}.')

fig, ax = plt.subplots(2, 1)

ax[0].plot(x, y_p, '.r')
ax[0].plot(x, a_p + b * x)
ax[0].legend(['Correción lineal del ajuste'])

ax[1].plot(x, y, '.r')
ax[1].plot(x, a * np.exp(b * x))
ax[1].legend(['Ajuste sobre los datos'])

plt.show()
