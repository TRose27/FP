import numpy as np 
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt 
from scipy.stats import sem 
import scipy.constants as const

z, B = np.genfromtxt("data/Bz.csv", unpack=True, comments="#", delimiter=",")

plt.plot(z,B,"rx",label="Messwerte")
plt.legend(loc="best")
plt.xlabel(r'$z\,/\,\mathrm{mm}$')
plt.ylabel(r'$B\,/\,\mathrm{mT}$')
plt.grid()
#plt.show()
plt.savefig("build/Bz.pdf") 