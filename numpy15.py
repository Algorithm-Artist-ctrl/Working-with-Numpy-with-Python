import numpy as np
A = np.array([[2, 1], [1, 2]])
values, vectors = np.linalg.eig(A)
print("Eigenvalues:", values)
print("Eigenvectors:\n", vectors)