# Escribir un programa que pida dos numeros reales e imprima en la pantalla el mayor de ellos. ç
# El programa debe indicar si los numeros son iguales.

import math

print("Ingrese dos numeros reales.")
x = float(input("x = "))
y = float(input("y = "))
if math.isclose(x, y, rel_tol=1e-52):
    print("Son iguales")
elif x < y:
    print("x < y")
else:
    print("y < x")
