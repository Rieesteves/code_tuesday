#histogram
from matplotlib import pyplot as plt
import numpy as np

a = np.array([22,87,5,43,56,73,45,54,11,20,51,5,79,31,27])

plt.hist(a,bins = [0,20,40,60,80,100],color='m')

plt.title("histogram")

plt.show()
