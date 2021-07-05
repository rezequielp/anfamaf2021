# Comprobar que el ´epsilon-maquina es 2^−52 = 2.2204 × 10−16, escribiendo y comparando
# las siguientes dos lıneas de comando

print("a = 1 + 2**-53; b = a-1")
a = 1 + 2 ** -53
b = a - 1
print(f"a={a:0.55f}\nb={b:0.55f}")

print("a = 1 + 2**-52; b = a-1")
a = 1 + 2 ** -52
b = a - 1
print(f"a={a:0.55f}\nb={b}")
