# ¿Que ocurre si en lugar de incrementarse la variable en 0.1 lo hace en 0.5? ¿Por que?
# https://docs.python.org/3/tutorial/floatingpoint.html

print("Sumar de a 0.1 hasta llegar a 10")
print("x=0; x = x+0.1; x != 10")
x = 0
while x != 10 and x < 11:
    x = x + 0.1
    if 9.5 < x < 10.5:
        print(f"{x}")
    else:
        print(".", end='')

print("\nSumar de a 0.5 hasta llegar a 10")
print("x=0; x = x+0.5; x != 10")
x = 0
while x != 10:
    x = x + 0.5
    if x > 9:
        print(f"{x}")
    else:
        print(".", end='')

print("El valor decimal real de la aproximacion binaria almacenadara para 0.1 es\n"
      f"{0.1:0.55f}")
