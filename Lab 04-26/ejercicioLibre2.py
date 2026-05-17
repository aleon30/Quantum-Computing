# Ejercicio libre 2
import numpy as np
def suma_vectores(a: np.array, b: np.array):
    if a.shape != b.shape:
        return "Error. Los vectores deben tener la misma shape"
    return a + b

a = np.array([0, 3, 5])
b = np.array([5, 6])
c = np.array([6, -3])
d = np.array([8, 5, -7])
print(suma_vectores(a, b))
print(suma_vectores(b, c))
print(suma_vectores(a, d))