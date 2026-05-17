# Vector normalizado a vector cuántico
import numpy as np
estado = np.array([3.0, 4.0])
psi = estado/np.linalg.norm(estado)
alpha, beta = psi
print(f"Estado normalizado: {alpha**2:.4f}, {beta**2:4f}")
print(f"Verificación: {alpha**2:.4f} + {beta**2:.4f} = {alpha**2+beta**2:4f}") 