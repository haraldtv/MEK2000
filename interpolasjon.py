#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 15:05:46 2023

@author: harald
"""

import numpy as np
import matplotlib.pyplot as plt

#
# Skript for eksempel i starten av kapittel 1.3 på side 20
#

"""
Original data:
    
    x, y
    
    0, 1
    1, 20
    2, 10
    3, 25
    4, 40
"""

#Matrise for likningssystemet
V = np.array(
    [[0, 0, 0, 0, 1, 1],
     [1, 1, 1, 1, 1, 20],
     [16, 8, 4, 2, 1, 10],
     [81, 27, 9, 3, 1, 25],
     [256, 64, 16, 4, 1, 40]]
    )

#Endrer matrisen til formen Ax = B
A = V[0:5, :-1]
B = V[0:5, -1]

#Løser for x
x = np.linalg.solve(A, B)

print(x)

#Funkson for polynomet fra ligningssystemet
def polynomial(x_inp, x):
    return (x[0] * x_inp**4 + x[1] * x_inp**3+ x[2] * x_inp**2 + x[3] * x_inp + x[4])

xx = np.linspace(0, 4.6, 100)
yy = np.zeros(100)

#Gjør utregningen for hver verdi i xx
for i in range(0, 100):
    yy[i] = polynomial(xx[i], x)
    
plt.plot(xx, yy, 'k-', label = "Polynom")



#Lag matrisene ved hjelp av numpy sin "vander()" funksjon
a2 = np.array([0, 1, 2, 3, 4])
b2 = np.array([1, 20, 10, 25, 40])

a2 = np.vander(a2)

x2 = np.linalg.solve(a2, b2)

print(x2)

