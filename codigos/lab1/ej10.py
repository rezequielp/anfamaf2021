import random
from ej10fun_sonReciprocos import sonReciprocos

for _ in range(1000):
    x = 1 + random.random()
    y = 1 / x
    if not sonReciprocos(x, y):
        print(x)
