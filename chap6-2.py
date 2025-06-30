#Chad Collard
#Lab 6-2
#6/30/2025

import matplotlib.pyplot as plt
import numpy as np

m = float(input("Enter the slope (m): "))
b = float(input("Enter the y-intercept (b): "))

x_min = -20
x_max = 20
x_values = np.linspace(x_min, x_max, 100)

y_values = m * x_values + b

plt.plot(x_values, y_values)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title(f"Line: y = {m}x + {b}")
plt.xlim(x_min, x_max)
plt.grid(True)
plt.show()
