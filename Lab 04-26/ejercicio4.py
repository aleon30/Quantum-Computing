import matplotlib.pyplot as plt
import numpy as np
# Ejercicio 4
u = np.array([1, 0, 2])
w = np.array([0, 3, 1])
resultado1 = u+w
resultado2 = 2*u-w

zeros = np.zeros(3)

fig = plt.figure(figsize=(7, 6))
ax = fig.add_subplot(111, projection="3d")

ax.quiver(*zeros, *u, color="red", label = "u", arrow_length_ratio=0.15)
ax.quiver(*zeros, *w, color="blue", label="w", arrow_length_ratio=0.15)
ax.quiver(*zeros, *resultado1, color="green", label="u+w", arrow_length_ratio=0.15)
ax.quiver(*zeros, *resultado2, color="purple", label="2*u-w", arrow_length_ratio=0.15)

ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_zlim(-5, 5)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
plt.title("Vectores 3D")
ax.legend()
plt.tight_layout()
plt.show()