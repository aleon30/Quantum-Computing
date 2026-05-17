# Ejercicio libre 3
import numpy as np
a = np.array([1, 2])
b = np.array([1, 2, 3])
try:
    print(a+b)
except ValueError:
    print("Los vectores deben tener la misma shape.")
# El programa de un ValueError porque la shape (cantidad de elementos) de los arrays son diferentes (2 y 3)