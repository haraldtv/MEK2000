import numpy as np

#Oppg 4
A = np.array([
    [1, 1],
    [1, 1.5],
    [1, 2.5],
    [1, 4]
    ])

y = np.array([3, 3.2, 5, 6]).T

ainv = np.linalg.inv(np.matmul(A.T, A))
print( np.matmul(np.matmul(ainv, A.T), y))



#Oppg 2-b fra ukesoppgavene
a2 = np.array([
    [1, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 1],
    [0, 0, 0, 1, 2, 4],
    [0, 1, 2, 0, -1, -2],
    [0, 0, 1, 0, 0, 0]
    ])
b2 = np.array([0, 2, 2, 2, 0, 0])

print("")
print("Oppgave 2 b:")
print(np.linalg.solve(a2,b2))
