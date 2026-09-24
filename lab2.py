import numpy as np
import matplotlib.pyplot as plt

# Data
X = np.array([24, 35, 64, 20, 33, 27, 42, 41, 22, 50, 36, 31])
Y = np.array([90, 65, 30, 60, 60, 80, 45, 45, 80, 35, 50, 45])

# Calculate regression coefficients
slope, intercept = np.polyfit(X, Y, 1)

# Predicted Y values
Y_pred = slope * X + intercept

# Calculate R²
r = np.corrcoef(X, Y)[0, 1]
r_squared = r ** 2

# Scatter plot
plt.scatter(X, Y, label="Observed Data")

# Regression line
plt.plot(X, Y_pred, label="Regression Line")

# Labels and title
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Scatter Plot with Linear Regression")

# Display equation and R²
equation = f"Y = {intercept:.4f} {slope:+.4f}X"
plt.text(
    0.05, 0.95,
    f"{equation}\nR² = {r_squared:.4f}",
    transform=plt.gca().transAxes,
    verticalalignment="top"
)

plt.legend()
plt.grid(True)

plt.show()
