x = int(input("ingrese un número: "))
y = int(input("ingrese un número: "))


def print_mat(x, y):
    for idx in range(1, x + 1):
        for jdx in range(1, y + 1):
            if idx == jdx:
                print(f"0.0", end=' ')
            else:
                print(f"{10 / (idx + jdx):1.3f}", end=' ')
        print('')


print_mat(x, y)
