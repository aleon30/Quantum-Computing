import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3])
y = np.array([2, 1, 5])
suma = x + y

zeros = np.zeros(3)

fig = plt.figure(figsize=(7, 6))
ax = fig.add_subplot(111, projection="3d")

ax.quiver(*zeros, *x, color="crimson", label = "x", arrow_length_ratio=0.15)
ax.quiver(*zeros, *y, color="blue", label="y", arrow_length_ratio=0.15)
ax.quiver(*zeros, *suma, color="forestgreen", label="x+y", arrow_length_ratio=0.15)

ax.set_xlim(0, 8)
ax.set_ylim(0, 8)
ax.set_zlim(0, 8)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
plt.title("Vectores 3D")
ax.legend()
plt.tight_layout()
plt.show()