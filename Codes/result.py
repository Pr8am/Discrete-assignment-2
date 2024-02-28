import numpy as np
import matplotlib.pyplot as plt

# Define the function y(n)
def y(n):
    return (n**4 + 6*n**3 + 11*n**2 + 6*n) / 4

# Generate positive values for n
n_values = np.arange(0, 11)  # Range of n from 0 to 10

# Calculate y(n) for each n
y_values = y(n_values)

# Plot y(n) vs n using stem plot
plt.stem(n_values, y_values, linefmt='b-', markerfmt='bo', basefmt=' ')
plt.title('$y(n) = \\frac{n^4 + 6n^3 + 11n^2 + 6n}{4}$')
plt.xlabel('n')
plt.ylabel('y(n)')
plt.grid(True)

# Add crosses over the points marked
plt.scatter(n_values, y_values, color='r', marker='x', zorder=3)

plt.show()

