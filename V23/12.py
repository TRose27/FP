import numpy as np
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.stats import sem
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import scipy.constants as const

f0,a0=np.genfromtxt("data/12/752vl.dat",unpack=True)
f1,a1=np.genfromtxt("data/12/757vl.dat",unpack=True)
f2,a2=np.genfromtxt("data/12/753vr.dat",unpack=True)
f3,a3=np.genfromtxt("data/12/62_53vr.dat",unpack=True)
f4,a4=np.genfromtxt("data/12/37_53vr.dat",unpack=True)
f5,a5=np.genfromtxt("data/12/253vr.dat",unpack=True)



plt.figure(figsize=[8,8])

plt.subplot(3,2,1)
plt.title("a)",loc="left")
plt.grid()
plt.plot(f0,a0,"r-",lw=0.5)
plt.ylabel(r'Amplitude')
plt.xlabel(r'f / $\si{\hertz}$')
plt.legend(loc="best")

plt.subplot(3,2,2)
plt.title("b)",loc="left")
plt.grid()
plt.plot(f3,a3,"k-",lw=0.5)
plt.ylabel(r'Amplitude')
plt.xlabel(r'f / $\si{\hertz}$')
plt.legend(loc="best")

plt.subplot(3,2,3)
plt.grid()
plt.plot(f1,a1,"r-",lw=0.5)
plt.ylabel(r'Amplitude')
plt.xlabel(r'f / $\si{\hertz}$')
plt.legend(loc="best")

plt.subplot(3,2,4)
plt.grid()
plt.plot(f4,a4,"k-",lw=0.5)
plt.ylabel(r'Amplitude')
plt.xlabel(r'f / $\si{\hertz}$')
plt.legend(loc="best")

plt.subplot(3,2,5)
plt.grid()
plt.plot(f2,a2,"r-",lw=0.5)
plt.ylabel(r'Amplitude')
plt.xlabel(r'f / $\si{\hertz}$')
plt.legend(loc="best")

plt.subplot(3,2,6)
plt.grid()
plt.plot(f5,a5,"k-",lw=0.5)
plt.ylabel(r'Amplitude')
plt.xlabel(r'f / $\si{\hertz}$')
plt.legend(loc="best")








plt.tight_layout()
#plt.show()
plt.savefig("build/12.pdf")
