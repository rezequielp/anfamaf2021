# Devuelve el valor de la lista mas cercano a K
import numpy


def closest(lst, k):
    lst = numpy.asarray(lst)
    idx = (numpy.abs(lst - k)).argmin()
    return lst[idx]
