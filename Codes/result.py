import matplotlib.pyplot as plt

# Function to calculate the nth term of the sequence
def term_n(n):
    return n * (n + 1) * (n + 2)

# Function to calculate y(n), the sum of n terms of the sequence
def y_n(n):
    return sum(term_n(i) for i in range(1, n + 1))

# Calculate y(n) for n = 1 to 10
n_values = list(range(1, 11))
y_values = [y_n(n) for n in n_values]

# Read values from code.dat
with open("code.dat", "r") as file:
    given_values = [int(line.strip()) for line in file]

# Create a stem plot
plt.stem(n_values, y_values, linefmt='-b', markerfmt='ob', basefmt=' ')

# Plot the values from code.dat
plt.scatter(range(1, 11), given_values, marker='x', color='r', label='Given Values', zorder=10)

plt.title('Sum of n terms of the sequence (Stem Plot with Scatter)')
plt.xlabel('n')
plt.ylabel('y(n)')
plt.legend()
plt.grid(True)
plt.show()

