import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2])
y = np.array([2, 1])
suma = x + y

zeros = np.zeros(2)

plt.quiver(*zeros, *x, angles="xy", scale_units="xy", scale = 1, color="crimson", label = "x", width=0.012)
plt.quiver(*zeros, *y, angles="xy", scale_units="xy", scale = 1, color="blue", label="y", width=0.012)
plt.quiver(*zeros, *suma, angles="xy", scale_units="xy", scale = 1, color="forestgreen", label="x+y", width=0.012)

plt.axhline(0, color="black", lw=1)
plt.axvline(0, color="black", lw=1)
plt.grid(True, linestyle="--", alpha=0.6)

plt.xlim(-1, 5)
plt.ylim(-1, 5)
plt.gca().set_aspect("equal")
plt.title("Vectores 2D")
plt.legend()
plt.show()