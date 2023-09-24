import numpy as np
import matplotlib.pyplot as plt

#Oppgave 3

years = np.arange(0,6,1)
saldo = [5000, 5275, 5592, 5910, 6206, 6553]
plt.plot(years, saldo, color="black", marker="o", label="Cashmoney")
plt.grid()
plt.legend()
plt.show()