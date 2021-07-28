# Interpolar la tabla utilizando los metodos de Lagrange, Newton y el de la funcion interp1d,
# luego graficar los 3 polinomios juntos. ¿Cual polinomio parece mas suave?

# x   -3  -2  -1  0   1   3   2
# f   1   2   5   10  5   2   1

import matplotlib.pyplot as plt
import numpy as np
from ej1_ilagrange import ilagrange
from ej2_inewton import inewton
from scipy.interpolate import interp1d

x = [-3, -2, -1, 0, 1, 2, 3]
y = [1, 2, 5, 10, 5, 2, 1]
z = np.linspace(-3.0, 3.0, 100)
inter_lagrange = ilagrange(x, y, z)
inter_newton = inewton(x, y, z)
polinomio = interp1d(x, y, kind='cubic', fill_value='extrapolate')
inter_interp1d = polinomio(z)

# ploteo
plt.plot(x, y, label="f(x)")
plt.plot(z, inter_lagrange, label="lagrange")
plt.plot(z, inter_newton, label="newton")
plt.plot(z, inter_interp1d, label="interp1d")
plt.grid()
plt.legend()
plt.show()
