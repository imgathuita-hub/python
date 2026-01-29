import numpy as np

# Define grid
x = np.linspace(0, 1, 100)
y = np.linspace(0, 1, 100)
X, Y = np.meshgrid(x, y)
Z = X**2 + Y**2

# Calculate volume using numerical integration (trapezoidal rule)
dx = dy = 1 / 100
volume = np.sum(Z) * dx * dy
print(f"Volume under surface z = x^2 + y^2 over 0 ≤ x,y ≤ 1: {volume:.4f}")