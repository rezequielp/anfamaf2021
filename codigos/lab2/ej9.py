# La generacion de energıa de un molino de viento depende del diametro de la circunferencia
# generada por sus aspas y la velocidad del viento de la zona. Una buena estimacion de la
# energıa generada esta dada por la formula:
# E = 0.01328D^2V^3, donde
# E es la energıa generada,
# D es el diametro en metros y
# V es la velocidad del viento en m/s.
# Usar el metodo de Newton para determinar el diametro del molino si se desea generar
# 500W de energıa electrica cuando la velocidad del viento es de 24 km/h.

from codigos.lab2.ej3_netwon import rnewton


def fun_lab2ej9(x):
    # 500 = 0.01328 * diametro^2 * (24/3.6) ** 3
    # 1 watt is equal to 1 newton meter/second.
    # 1 W = 1 N.s (newton-second)
    # 1 km/h = 1/3.6 m/s
    return 0.01328 * x ** 2 * 24**3 / 3.6 ** 3

def fun_resolver_lab2ej9(x):
    fx = fun_lab2ej9(x) - 500
    dfx = 7.86963 * x
    return fx, dfx


def main():
    # diametro = √(500 / (0.01328 * 24^3) = +-1.65032
    # diametro = math.sqrt(500 / (0.01328 * 24**3))

    hx, hf = rnewton(fun_resolver_lab2ej9, 1, 1e-5, 100)
    x = hx[-1]
    print(f"Se generarán {fun_lab2ej9(x):0.0f} Watts con una vel de viento de 24km/h")
    print(f"Si el diametro del molino es de al menos {x:0.2f} metros")


if __name__ == "__main__":
    main()
