import matplotlib.pyplot as plt
import numpy as np
#Ejercicio 2
v1 = np.array([1, 3])
v2 = np.array([-2, 1])
resultado = 2*v1 + v2

zeros = np.zeros(2)

plt.quiver(*zeros, *v1, angles="xy", scale_units="xy", scale = 1, color="red", label = "v1", width=0.012)
plt.quiver(*zeros, *v2, angles="xy", scale_units="xy", scale = 1, color="blue", label="v1", width=0.012)
plt.quiver(*zeros, *resultado, angles="xy", scale_units="xy", scale = 1, color="green", label="2*v1+v2", width=0.012)

plt.axhline(0, color="black", lw=1)
plt.axvline(0, color="black", lw=1)
plt.grid(True, linestyle="--", alpha=0.6)

plt.xlim(-3, 10)
plt.ylim(-3, 10)
plt.gca().set_aspect("equal")
plt.title("Vectores 2D")
plt.legend()
plt.show()