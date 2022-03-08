#displaying 4 graphs
from matplotlib import pyplot as plt
fig,a= plt.subplots(2,2)
import numpy as np

x=np.arange(1,5) #range

a[0][0].plot(x,x*x)
a[0][0].set_title("Square")

a[0][1].plot(x,np.sqrt(x),color='r')
a[0][1].set_title("Square_root")

a[1][0].plot(x,np.exp(x))
a[1][0].set_title("Exp")

a[1][1].plot(x,np.log10(x))
a[1][1].set_title("Log")

plt.show()
