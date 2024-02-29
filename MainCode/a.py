import matplotlib.pyplot as plt

def read_dat_file(file_path):
    x = []
    y = []
    with open(file_path, 'r') as file:
        for line in file:
            data = line.split()
            x.append(int(data[0]))
            y.append(int(data[1]))
    return x, y

# Path to the first dat file (stem plot)
pth_stem = "analysis.dat"
x_stem, y_stem = read_dat_file(pth_stem)

# Path to the second dat file (scatter plot)
pth_scatter = "simulation.dat"
x_scatter, y_scatter = read_dat_file(pth_scatter)

# Create a new figure
plt.figure(figsize=(10, 6))

# Plot stem plot
plt.stem(x_stem, y_stem, linefmt='b-', markerfmt='bo', basefmt=' ', label='Convolution')

# Plot scatter plot
plt.scatter(x_scatter, y_scatter, color='r', label='y(n)')

# Add labels and title
plt.xlabel('Index')
plt.ylabel('Value')
# Add legend
plt.legend()

# Show plot
plt.grid(True)
plt.show()

