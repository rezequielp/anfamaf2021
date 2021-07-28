def horn(coefs, x):
    """
        Funcion para evaluar polinomios en un punto utilizando
        el algoritmo de Horner.
        """
    # horner ---> p(x) = 3+(2+x(1))
    # coefs = [1, 2, 3] --->  p(x) = x^2 + 2x + 3
    # coefs = [a_n, a_{n-1}, ... , a_1, a_0]
    #  0    1              n-1  , n
    # n = len(coefs) - 1  # n = grado del polinomio
    #	for k in range(1,n+1):
    #		# p <- a_k + x * p
    #		p = coefs[k] + x*p

    # p = a_n
    p = coefs[0]
    for coef in coefs[1:]:
        p = coef + x * p

    return p
