# Escriba una funcion rinterp(fun,x0,x1,x2,err,mit) que encuentre un cero de la funcion
# fun de la siguiente forma. En cada paso, sea q2 el polinomio interpolante cuadratico de los
# puntos (xn−2, f(xn−2)), (xn−1, f(xn−1)) y (xn, f(xn)). Elegir como xn+1 al cero de q2 que
# este mas cerca de xn. Comparar su performance con los metodos para encontrar raıces del
# laboratorio 2
from codigos.lab1.ej8_raices_de_cuadraticas import buena
from codigos.lab1.ej9_horn import horn
from codigos.lab2.ej1_biseccion import rbisec
from codigos.lab2.ej3_netwon import rnewton
from codigos.lab2.ej5_puntoFijo import ripf
from codigos.lab3.fun_closest import closest
from codigos.lab3.fun_obtiene_coefs import obtiene_coefs


def rinterp(fun, x0, x1, x2, err, mit):
    hx = [x0, x1, x2]
    hf = [fun(x0), fun(x1), fun(x2)]
    for _ in range(mit):
        # utilizo los ultimos 3 x para interpolarlos y obtener los coeficientes
        a, b, c = obtiene_coefs(hx[-3:], hf[-3:])
        if abs(a) < err:
            # bx + c = 0
            roots = [-c/b]
        else:
            roots = buena(a, b, c)
        # me quedo con la raiz mas cercana al ultimo x que tenga
        xn = closest(roots, hx[-1])
        fun_xn = fun(xn)
        hx.append(xn)
        hf.append(fun_xn)
        if abs(fun_xn) < err:
            break
    return hx, hf

# prueba de que funciona rinterp
def main():
    # TODO revisar por que no funciona correctamente (preguntar a lxs profes)
    # fun = lambda x: x**3 - 1
    fun = lambda x: horn([1,4,0,-10], x)
    hy, hu = rinterp(fun, 1.0, 1.5, 2.0, 1e-6, 100)
    # hy, hu = rbisec(fun, [1,2], 1e-6, 100)
    # hy, hu = ripf(fun, 2, 1e-6, 100)

    y = hy[-1]
    print(f"{len(hy)}:{y}")
    print(hy[:10])
    print(hu[:10])

if __name__ == "__main__":
    main()