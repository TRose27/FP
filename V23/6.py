import numpy as np
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.stats import sem
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import scipy.constants as const

f0,a0=np.genfromtxt("data/6/overview.dat",unpack=True)



plt.figure(figsize=[4,2.5])
plt.grid()
plt.plot(f0,a0,"r-",lw=0.5,label="600mm")
plt.ylabel(r'Amplitude')
plt.xlabel(r'f / $\si{\hertz}$')
plt.legend(loc="best")
#Deltaf=3342
plt.tight_layout()

plt.savefig("build/6.pdf")
