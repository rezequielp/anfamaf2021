def sonReciprocos(x, y):
    #	if x*y == 1:
    tol = 1e-10
    if abs(x * y - 1) < tol:
        return True
