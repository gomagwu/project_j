import numpy as np
import scipy.interpolate as interp
import scipy.stats as stats
import matplotlib.pyplot as plt

# Using triangular() method
tr_array = np.random.triangular(-5, 0, 5, 5000)

# Using normal() method
array = np.random.normal(0.0, 1.0, 5000)

# Concatenate
cons = np.concatenate((tr_array, array))

hist, bins = np.histogram(cons)

loc, scale = stats.norm.fit(cons)

# PDF (probability density function)

x = np.linspace(start=-5, stop=5, num=10000)
pdf = stats.norm.pdf(x, loc=loc, scale=scale)
pdf = interp.interp1d(x, pdf, bounds_error=True)

# Visualizing
plt.scatter(x, pdf(x))
plt.title("Interp1d for PDF")
plt.show()

