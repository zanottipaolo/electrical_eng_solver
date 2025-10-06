import numpy as np

# LINEAR SYSTEM
# Define coefficient matrix A and constant vector b
# For example, solving:
#   -9x + 2y + 3z = 0
#   2x -4y + 2z + w = -12
#   3x + 2y -6z -w = 0
#   y - z = 12
A = np.array([[-9, 2, 3, 0],
              [2, -4, 2, 1], 
              [3, 2, -6, -1], 
              [0, 1, -1, 0]], dtype=float)

b = np.array([0, -12, 0, 12], dtype=float)

x_with_2_decimal = [round(i, 2) for i in np.linalg.solve(A, b)]

print("Solution:", x_with_2_decimal)