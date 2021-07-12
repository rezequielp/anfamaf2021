# Encontrar el mınimo de la funcion f(x) = (tan x) / x^2 en el intervalo (0, π/2 ).
# Para ello calcular la raız de su derivada usando el metodo de Newton

from ej3_netwon import rnewton
import math


def fun_lab2ej8(x):
    tan_x = math.tan(x)
    cos_x = math.cos(x)
    sec2_x = 1 / cos_x ** 2

    # fx = tan_x / x ** 2
    # para calcular la raiz de la derivada de f(x) necesito la derivada segunda para el metodo de newton
    dfx = (x * sec2_x - 2 * tan_x) / x ** 3
    d2fx = ((6 * tan_x) + 2 * x * sec2_x * (-2 + x * tan_x)) / x ** 4
    return dfx, d2fx

def main():
    """"
    https://www.wolframalpha.com/input/?i=local+minimum+calculator&assumption=%7B%22F%22%2C+%22LocalMinimizeCalculator%22%2C+%22curvefunction%22%7D+-%3E%22tan%28x%29%2Fx%5E2%22&assumption=%7B%22F%22%2C+%22LocalMinimizeCalculator%22%2C+%22domain%22%7D+-%3E%220%3Cx%3Cpi%2F2%22
    """
    hx, hf = rnewton(fun_lab2ej8, 1, 1e-10, 100)
    dfx_root = hx[-1]
    min_fx = math.tan(dfx_root) / dfx_root ** 2
    print(f"La raiz de la derivada de f(x) es {hx[-1]}")
    print(f"El minimo f(x) en el intervalo (0, π/2 ) es {min_fx}")


if __name__ == "__main__":
    main()


