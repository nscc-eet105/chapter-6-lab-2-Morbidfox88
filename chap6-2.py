#Chad Collard
#Lab 6-2
#6/30/2025

import matplotlib.pyplot as plt

m = float(input("Enter the slope (m): "))
b = float(input("Enter the y-intercept (b): "))

x_min = -20
x_max = 20
num_points = 100
x_values = []
y_values = []


step_size = (x_max - x_min) / (num_points - 1) 


for i in range(num_points):
    x = x_min + i * step_size
    x_values.append(x)
    y_values.append(m * x + b) 

plt.plot(x_values, y_values)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title(f"Line: y = {m}x + {b}")
plt.xlim(x_min, x_max)
plt.grid(True)
plt.show()
