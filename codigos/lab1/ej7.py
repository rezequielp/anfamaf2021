# Escribir una funcion que calcule la potencia enesima de un numero, es decir que devuelva
# xn para x real y n entero. Realice un programa que utilice la funcion e imprima en pantalla
# las primeras 5 potencias naturales de un numero ingresado

from ej7fun_potencia import potencia

x = float(input("Ingrese un número: "))

for i in range(1, 6):
    print(potencia(x, i))
