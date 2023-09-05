#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 22:39:24 2023

@author: harald
"""

import numpy as np
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 5, 4, 7, 8]


N = 50
XMIN = 1
XMAX = 5

xv = np.vander(x)
p = np.linalg.solve(xv, y)

xx = np.linspace(XMIN, XMAX, N)
yy = np.zeros(N)

#yy = p[0] * xx**3 + p[1] * xx**2 + p[2] * xx + p[3]
for i in range(len(p)):
    for j in range(len(xx)):
        yy[j] += p[i] * xx[j]**(len(p)-i-1)

plt.scatter(x, y)
plt.plot(xx, yy)
