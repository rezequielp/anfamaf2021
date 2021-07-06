from math import sqrt

def f(x):
    return sqrt(x ** 2 + 1) - 1


def g(x):
    return x ** 2 / (sqrt(x ** 2 + 1) + 1)

print(f"f(x)=sqrt(x**2+1) - 1")
print(f"g(x)=x ** 2 / (sqrt(x ** 2 + 1) + 1)")
for i in range(20):
    x = 8 ** -i
    print(f"{i}: f(x)={f(x)},\tg(x)={g(x)}")
