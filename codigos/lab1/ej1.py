# Dadas 3 variables numericas x, y, z notar las diferencias entre:
# a) x/y + z y x/(y + z)
# b) x/y*z y x/(y*z).

x = int(input("ingrese el valor de x: "))
y = int(input("ingrese el valor de y: "))
z = int(input("ingrese el valor de z: "))

# a)
print(f"x/y + z = {x}/{y} + {z} = ", x/y + z)
print(f"x/(y + z) = {x}/({y}+{z}) = ", x/(y + z))

# b)
print(f"x/y*z = {x}/{y}*{z} = ", x/y*z)
print(f"x/(y*z) = {x}/({y}*{z}) = ", x/(y*z))
