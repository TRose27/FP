import numpy as np
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.stats import sem
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import scipy.constants as const

f0,a0=np.genfromtxt("data/8/10mm.dat",unpack=True)
f1,a1=np.genfromtxt("data/8/13mm.dat",unpack=True)
f2,a2=np.genfromtxt("data/8/16mm.dat",unpack=True)



plt.figure(figsize=[4,7.5])

plt.subplot(3,1,1)
plt.grid()
plt.plot(f0,a0,"r-",lw=0.5,label="10mm Blende")
plt.ylabel(r'Amplitude')
plt.xlabel(r'f / $\si{\hertz}$')
plt.legend(loc="best")

plt.subplot(3,1,2)
plt.grid()
plt.plot(f1,a1,"r-",lw=0.5,label="13mm Blende")
plt.ylabel(r'Amplitude')
plt.xlabel(r'f / $\si{\hertz}$')
plt.legend(loc="best")

plt.subplot(3,1,3)
plt.grid()
plt.plot(f2,a2,"r-",lw=0.5,label="16mm Blende")
plt.ylabel(r'Amplitude')
plt.xlabel(r'f / $\si{\hertz}$')
plt.legend(loc="best")


plt.tight_layout()
plt.savefig("build/8.pdf")
