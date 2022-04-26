import numpy as np
import matplotlib.pyplot as plt

# Using triangular() method
tr_array = np.random.triangular(-5, 0, 5, 5000)

# Using normal() method
array = np.random.normal(0.0, 1.0, 5000)

# Concatenate
cons = np.concatenate((tr_array, array))

hist, bins = np.histogram(cons)

# Visualizing
plt.hist(cons, bins=bins)
plt.title("histogram")
plt.show()
