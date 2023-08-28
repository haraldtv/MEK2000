import numpy as np
A = np.array([
    [1, 0, 0],
    [2, 4, 5],
    [3, 1, 2]])

B = np.array([1, 2, 0])

print(np.linalg.solve(A, B))
