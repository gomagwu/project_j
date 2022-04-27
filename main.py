import numpy as np
import scipy.interpolate as interp
import scipy.stats as stats
import matplotlib.pyplot as plt


class Distribution:

    def __init__(self, number_of_samples):
        self.number_of_samples = number_of_samples
        # Using triangular() method
        tr_array = np.random.triangular(-5, 0, 5, int(number_of_samples / 2))

        # Using normal() method
        array = np.random.normal(0.0, 1.0, int(number_of_samples / 2))

        # Concatenate
        self.cons = np.concatenate((tr_array, array))

    @staticmethod
    def salutations():
        print("Thank you for using my app")

    def plot_histogram(self):
        # the histogram of the data
        hist, bins = np.histogram(self.cons)
        plt.hist(self.cons, bins=bins)
        plt.title("histogram")
        plt.show()

    def plot_pdf(self):
        # the histogram of the data
        loc, scale = stats.norm.fit(self.cons)

        # PDF (probability density function)

        x = np.linspace(start=-5, stop=5, num=self.number_of_samples)
        pdf = stats.norm.pdf(x, loc=loc, scale=scale)
        pdf = interp.interp1d(x, pdf, bounds_error=True)

        # Visualizing
        plt.scatter(x, pdf(x))
        plt.title("Interp1d for PDF")
        plt.show()


Distribution(1000).salutations()
Distribution(1000).plot_histogram()
Distribution(1000).plot_pdf()
