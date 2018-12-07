import numpy as np
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.stats import sem
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import scipy.constants as const

f0,a0=np.genfromtxt("data/1/75mm.dat",unpack=True)
f1,a1=np.genfromtxt("data/1/150mm.dat",unpack=True)
f2,a2=np.genfromtxt("data/1/225mm.dat",unpack=True)
f3,a3=np.genfromtxt("data/1/300mm.dat",unpack=True)
f4,a4=np.genfromtxt("data/1/375mm.dat",unpack=True)
f5,a5=np.genfromtxt("data/1/450mm.dat",unpack=True)
f6,a6=np.genfromtxt("data/1/525mm.dat",unpack=True)
f7,a7=np.genfromtxt("data/1/600mm.dat",unpack=True)

df=np.array([2250,1140,767,569,453,381,328,287])
d=np.array([75,150,225,300,375,450,525,600])
dfit=1/d


def f(x, a, b):
    return a*x+b

params, covariance_matrix = curve_fit(f, dfit, df)
errors = np.sqrt(np.diag(covariance_matrix))

print('a=', params[0], '+-', errors[0])
print('b=', params[1], '+-', errors[1])

plt.grid()
plt.plot(dfit,df,"k.",label="Daten")
plt.plot(dfit, f(dfit, *params), 'r-', label='Fit')
plt.xlabel(r'$\frac{1}{d}$ / $\si{\per\milli\metre}$')
plt.ylabel(r'$\Delta f$ / $\si{\hertz}$')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.legend(loc="best")
plt.savefig('build/vschall.pdf')
plt.clf()

plt.figure(figsize=[8,10])

plt.subplot(4,2,1)
plt.grid()
plt.plot(f0,a0,"r-",lw=0.5,label="75mm")
plt.ylabel(r'Amplitude')
plt.xlabel(r'f / $\si{\hertz}$')
plt.legend(loc="best")

plt.subplot(4,2,2)
plt.grid()
plt.plot(f1,a1,"g-",lw=0.5,label="150mm")
plt.ylabel(r'Amplitude')
plt.xlabel(r'f / $\si{\hertz}$')
plt.legend(loc="best")

plt.subplot(4,2,3)
plt.grid()
plt.plot(f2,a2,"b-",lw=0.5,label="225mm")
plt.ylabel(r'Amplitude')
plt.xlabel(r'f / $\si{\hertz}$')
plt.legend(loc="best")

plt.subplot(4,2,4)
plt.grid()
plt.plot(f3,a3,"k-",lw=0.5,label="300mm")
plt.ylabel(r'Amplitude')
plt.xlabel(r'f / $\si{\hertz}$')
plt.legend(loc="best")

plt.subplot(4,2,5)
plt.grid()
plt.plot(f4,a4,"c-",lw=0.5,label="375mm")
plt.ylabel(r'Amplitude')
plt.xlabel(r'f / $\si{\hertz}$')
plt.legend(loc="best")

plt.subplot(4,2,6)
plt.grid()
plt.plot(f5,a5,"y-",lw=0.5,label="450mm")
plt.ylabel(r'Amplitude')
plt.xlabel(r'f / $\si{\hertz}$')
plt.legend(loc="best")

plt.subplot(4,2,7)
plt.grid()
plt.plot(f6,a6,"m-",lw=0.5,label="525mm")
plt.ylabel(r'Amplitude')
plt.xlabel(r'f / $\si{\hertz}$')
plt.legend(loc="best")

plt.subplot(4,2,8)
plt.grid()
plt.plot(f7,a7,ls="-",lw=0.5,color="orange",label="600mm")
plt.ylabel(r'Amplitude')
plt.xlabel(r'f / $\si{\hertz}$')
plt.legend(loc="best")

plt.tight_layout()
plt.savefig('build/1.pdf')
