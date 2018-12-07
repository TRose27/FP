import numpy as np
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.stats import sem
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import scipy.constants as const

f0,a0=np.genfromtxt("data/4/10.dat",unpack=True)
f1,a1=np.genfromtxt("data/4/12.dat",unpack=True)


plt.figure(figsize=[8,2.5])
plt.subplot(1,2,1)
plt.grid()
plt.plot(f0,a0,"r-",lw=0.5,label="500mm")
plt.ylabel(r'Amplitude')
plt.xlabel(r'f / $\si{\hertz}$')
plt.legend(loc="best")

plt.subplot(1,2,2)
plt.grid()
plt.plot(f1,a1,"k-",lw=0.5,label="600mm")
plt.ylabel(r'Amplitude')
plt.xlabel(r'f / $\si{\hertz}$')
plt.legend(loc="best")

plt.tight_layout()

plt.savefig("build/4.pdf")
