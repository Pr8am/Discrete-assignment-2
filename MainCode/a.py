import matplotlib.pyplot as plt

# Read data from the dat file
with open("analysis.dat", "r") as file:
    data = file.readlines()

# Extract the values from the data
values = [int(value.split()[1]) for value in data]

# Plot the values as a stem plot
plt.stem(values, linefmt='b-', markerfmt='bo', basefmt=' ')

# Calculate the sum of the series for each value of n
sum_series = [sum(range(i, i+3)) for i in range(1, 10)]

# Plot the sum of the series as a scatter plot overlaid on top of the stem plot
plt.scatter(range(1, 10), sum_series, color='r', label='Sum of series')

plt.xlabel('Index')
plt.ylabel('Value / Sum')
plt.grid(True)
plt.legend()
plt.show()

