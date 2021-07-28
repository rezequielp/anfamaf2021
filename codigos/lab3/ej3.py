# Considerar la funcion f tal que f(x) = 1/x.
# Utilizando el ejercicio anterior, graficar en una misma figura f y
# p que interpole {(i, f(i))} i=1..5, usando para ambas los puntos equiespaciados
# zj = 24/25 + j/25, j = 1, . . . , 101

from ej2_inewton import inewton
from ej1_ilagrange import ilagrange
import matplotlib.pyplot as plt

f = lambda x: 1 / x

# {(i, f(i))} i=1..5
lista_i = list(range(1, 6))
lista_f = [f(i) for i in lista_i]

# zj = 24/25 + j/25, j = 1, . . . , 101
lista_z = [24 / 25 + j / 25 for j in range(1, 102)]
f_plot = [f(z) for z in lista_z]

# p_plot = ilagrange(lista_i, lista_f, lista_z)
p_plot = inewton(lista_i, lista_f, lista_z)

plt.plot(lista_z, f_plot, label="funcion f")
plt.plot(lista_z, p_plot, label="polinomio interpolante")
plt.grid()
plt.legend()

plt.show()