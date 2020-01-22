from scipy.interpolate import *
import matplotlib.pyplot as plt
import numpy as numpy

x_0 = np.linspace(0, 10, 10)
y_0 = np.cos(x_0**2.0 / 8.0)

x_1 = np.linspace(0, 10, 1000)
y_1 = np.cos(x_1**2.0 / 8.0)

plt.plot(x_0, y_0, "ro,", label="Points")
plt.plot(x_1, y_1, ":,", label="Origin")
plt.title("Interpolacion 1D")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend(loc="best")
plt.show()
