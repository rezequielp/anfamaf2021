import ej7
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.0, 1.5, 100)
# h = 1.5/99
# x = [i*h for i in range(100)]

y_bisec = [ej7.lab2ej7bisec(xi) for xi in x]
y_newton = [ej7.lab2ej7newton(xi) for xi in x]
y_ipf = [ej7.lab2ej7ipf(xi) for xi in x]

# fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
fig = plt.figure()
gs = fig.add_gridspec(1, 3, hspace=0, wspace=0)
ax1, ax2, ax3 = gs.subplots(sharex='col', sharey='row')
ax1.plot(x, y_bisec, 'g')
ax2.plot(x, y_newton, 'r')
ax3.plot(x, y_ipf, 'b')
ax1.set_title('biseccion')
ax2.set_title('newton')
ax3.set_title('punto fijo')
fig.suptitle('Lab2 - Ejercicio 7', fontsize=14)

for ax in fig.get_axes():
    ax.set(xlabel='x-label', ylabel='y-label')
# Hide x labels and tick labels for top plots and y ticks for right plots.
for ax in fig.get_axes():
    ax.label_outer()

plt.show()