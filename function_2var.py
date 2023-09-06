# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 16:14:40 2023

@author: Harald
"""

import numpy as np
import matplotlib.pyplot as plt

N = 50
XMIN = -5
XMAX = 5


x = np.outer(np.linspace(XMIN, XMAX, N), np.ones(N))
y = x.copy().T
z = np.sin(x) * y

fig = plt.figure(figsize =(14, 9))
ax = plt.axes(projection ='3d')
 
ax.plot_surface(x, y, z)
