import numpy as np
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.stats import sem
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import scipy.constants as const

f0,a0=np.genfromtxt("data/9/310.dat",unpack=True)
f1,a1=np.genfromtxt("data/9/313.dat",unpack=True)
f2,a2=np.genfromtxt("data/9/316.dat",unpack=True)
f3,a3=np.genfromtxt("data/9/410.dat",unpack=True)
f4,a4=np.genfromtxt("data/9/413.dat",unpack=True)
f5,a5=np.genfromtxt("data/9/416.dat",unpack=True)
f6,a6=np.genfromtxt("data/9/610.dat",unpack=True)
f7,a7=np.genfromtxt("data/9/613.dat",unpack=True)
f8,a8=np.genfromtxt("data/9/616.dat",unpack=True)



plt.figure(figsize=[12,8])

plt.subplot(3,3,1)
plt.title("a)",loc="left")
plt.grid()
plt.plot(f0,a0,"r-",lw=0.5,label="10mm Blende")
plt.ylabel(r'Amplitude')
plt.xlabel(r'f / $\si{\hertz}$')
plt.legend(loc="best")

plt.subplot(3,3,2)
plt.grid()
plt.plot(f1,a1,"k-",lw=0.5,label="13mm Blende")
plt.ylabel(r'Amplitude')
plt.xlabel(r'f / $\si{\hertz}$')
plt.legend(loc="best")

plt.subplot(3,3,3)
plt.grid()
plt.plot(f2,a2,"b-",lw=0.5,label="16mm Blende")
plt.ylabel(r'Amplitude')
plt.xlabel(r'f / $\si{\hertz}$')
plt.legend(loc="best")

plt.subplot(3,3,4)
plt.title("b)",loc="left")
plt.grid()
plt.plot(f3,a3,"r-",lw=0.5,label="10mm Blende")
plt.ylabel(r'Amplitude')
plt.xlabel(r'f / $\si{\hertz}$')
plt.legend(loc="best")

plt.subplot(3,3,5)
plt.grid()
plt.plot(f4,a4,"k-",lw=0.5,label="13mm Blende")
plt.ylabel(r'Amplitude')
plt.xlabel(r'f / $\si{\hertz}$')
plt.legend(loc="best")

plt.subplot(3,3,6)
plt.grid()
plt.plot(f5,a5,"b-",lw=0.5,label="16mm Blende")
plt.ylabel(r'Amplitude')
plt.xlabel(r'f / $\si{\hertz}$')
plt.legend(loc="best")

plt.subplot(3,3,7)
plt.title("c)",loc="left")
plt.grid()
plt.plot(f6,a6,"r-",lw=0.5,label="10mm Blende")
plt.ylabel(r'Amplitude')
plt.xlabel(r'f / $\si{\hertz}$')
plt.legend(loc="best")

plt.subplot(3,3,8)
plt.grid()
plt.plot(f7,a7,"k-",lw=0.5,label="13mm Blende")
plt.ylabel(r'Amplitude')
plt.xlabel(r'f / $\si{\hertz}$')
plt.legend(loc="best")

plt.subplot(3,3,9)
plt.grid()
plt.plot(f8,a8,"b-",lw=0.5,label="16mm Blende")
plt.ylabel(r'Amplitude')
plt.xlabel(r'f / $\si{\hertz}$')
plt.legend(loc="best")


plt.tight_layout()
plt.savefig("build/9.pdf")
