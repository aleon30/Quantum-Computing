# Ejercicio libre 1
import numpy as np
import matplotlib.pyplot as plt

v1 = np.array([3, 6])
v2 = np.array([5, 4])
suma = v1 + v2
resta = v1 - v2
comb1 = 3*v1 -2*v2
comb2 = v2 - 2*v1
vectores = [v1, v2, suma, resta, comb1, comb2]
labels = ["v1", "v2", "v1+v2", "v1-v2", "3*v1-2*v2", "v2-2*v1"]
colores = ["red", "blue", "green", "purple", "yellow", "pink"]
zeros = np.zeros(2)

for i in range(0, 6):
    plt.quiver(*zeros, *vectores[i], angles="xy", scale_units="xy", scale=1, color=colores[i], label=labels[i], width=0.012)

plt.axhline(0, color="black", lw=1)
plt.axvline(0, color="black", lw=1)
plt.grid(True, linestyle="--", alpha=0.6)

plt.xlim(-5, 15)
plt.ylim(-10, 10)
plt.gca().set_aspect("equal")
plt.legend()
plt.show()