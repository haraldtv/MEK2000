import numpy as np

A = np.array([
    [1, 1],
    [1, 1.5],
    [1, 2.5],
    [1, 4]
    ])

y = np.array([3, 3.2, 5, 6]).T

ainv = np.linalg.inv(np.matmul(A.T, A))
print( np.matmul(np.matmul(ainv, A.T), y))
