import matplotlib.pyplot as plt
import numpy as np

# Experimental data for graduated cylinder
volume = [8.2, 19.7, 29.4, 39.7]       # mL
density = [6.38, 3.24, 2.50, 2.36]    # g/cm^3

# Error/uncertainty in density
# Replace these values with your actual experimental uncertainty if known
density_error = [0.10, 0.10, 0.10, 0.10]  # g/cm^3

# Calculate average density
average_density = np.mean(density)

# True density of water
true_density = 1.00  # g/cm^3

# Create graph
plt.figure(figsize=(9, 6))

# Bar graph with error bars
plt.bar(
    volume,
    density,
    width=6,
    yerr=density_error,
    capsize=6,
    edgecolor='black',
    alpha=0.8
)

# True density line
plt.axhline(
    y=true_density,
    linestyle=':',
    linewidth=2,
    label='True Density of Water (1.00 g/cm³)'
)

# Average experimental density line
plt.axhline(
    y=average_density,
    linestyle='--',
    linewidth=2,
    label=f'Average Density ({average_density:.2f} g/cm³)'
)

# Axis labels and title
plt.xlabel('Volume of Water in Graduated Cylinder (mL)', fontsize=12)
plt.ylabel('Density (g/cm³)', fontsize=12)
plt.title('Measured Density of Water at Different Volumes', fontsize=14)

# Make sure x-axis corresponds to the four experimental volumes
plt.xticks(volume, ['8.2', '19.7', '29.4', '39.7'])

# Legend in top-right corner
plt.legend(loc='upper right')

# Grid only along y-axis
plt.grid(axis='y', alpha=0.25)

# Make layout clean
plt.tight_layout()

# Display graph
plt.show()