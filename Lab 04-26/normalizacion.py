# Normalización
import numpy as np
v = np.array([3, 4])
v_norm = v / np.linalg.norm(v)
print(v_norm)