import numpy as np

# QUADRATIC EQUATION

# Insert here the coefficients of the quadratic equation
# 120x^2 - 1000x + 1498 = 0
coeff = [120, -1000, 1498]
roots = np.roots(coeff)
roots_with_2_decimal = [round(root, 2) for root in roots]
print("Roots of the quadratic equation:", roots_with_2_decimal)