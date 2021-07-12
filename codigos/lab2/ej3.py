# Escribir una funcion que implemente el metodo de Newton para hallar una raiz de
# f : R → R partiendo de un punto inicial x0.
# La funcion debe llamarse “rnewton”, y tener como entrada (fun,x0,err,mit) donde:
#   fun es una funcion que dado x retorna f(x) y f′(x),
#   x0 es un punto inicial en R,
#   err es la tolerancia deseada del error,
#   mit es el numero maximo de iteraciones permitidas.
# El algoritmo debe finalizar en la k-esima iteracion si se cumple alguna de las siguientes condiciones:
#   |xk − xk−1|/|xk|< err
#   |f(xk)| < err,
#   k ≥ mit.
# La salida debe ser (hx,hf) donde hx= [x1, . . . , xN] es una lista que representa el historico de puntos generados
# y hf= [f(x1), . . . , f(xN)] el historico de los respectivos valores funcionales.

def rnewton(fun, x0, err, mit):
    hx = []
    hf = []
    f, df = fun(x0)

    for _ in range(mit):
        if df == 0:
            print("la derivada en el punto es nula")
            break

        xn = x0 - f / df
        f, df = fun(xn)

        hx.append(xn)
        hf.append(f)

        if abs(xn - x0) / abs(xn) < err or abs(f) < err:
            break

        x0 = xn

    return hx, hf
