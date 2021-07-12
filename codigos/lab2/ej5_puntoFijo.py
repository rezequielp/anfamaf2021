# Escribir una funcion que implemente el metodo de iteracion de punto fijo para hallar un
# punto fijo de ϕ : R → R, partiendo de un punto inicial x0.
# La funcion debe llamarse “ripf”, y tener como entrada (fun,x0,err,mit) donde
# fun es una funcion que dado x retorna ϕ(x),
# x0 es un punto en R,
# err es la tolerancia deseada del error y mit es el numero maximo de iteraciones permitidas.
# El algoritmo debe finalizar en la k-´esima iteracion si |xk − xk−1| < err o bien k ≥ mit.
# La salida debe ser hx donde hx= [x1, . . . , xN] es una lista del historico de puntos generados

def ripf(fun, x0, err, mit):
    hx = [x0]
    for _ in range(mit):
        xn = fun(x0)
        hx.append(xn)
        if abs(xn - x0) < err:
            # El error es
            break
        x0 = xn
    return hx
