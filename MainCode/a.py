import matplotlib.pyplot as plt

# Function to read data from a .dat file
def read_dat_file(filename):
    x = []
    y = []
    with open(filename, 'r') as file:
        for line in file:
            data = line.strip().split()
            x.append(float(data[0]))
            y.append(float(data[1]))
    return x, y

# Read data from analysis.dat
analysis_x, analysis_y = read_dat_file('analysis.dat')

# Read data from simulation.dat
simulation_x, simulation_y = read_dat_file('simulation.dat')

# Plotting
plt.figure(figsize=(10, 6))

# Stem plot for analysis.dat
plt.stem(analysis_x, analysis_y, linefmt='r-', markerfmt='ro', basefmt=' ')

# Scatter plot for simulation.dat
plt.scatter(simulation_x, simulation_y, color='b', label='Simulation')

plt.xlabel('X-axis label')
plt.ylabel('Y-axis label')
plt.title('Analysis vs Simulation')
plt.legend()
plt.grid(True)
plt.show()

