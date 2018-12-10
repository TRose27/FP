import numpy as np
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.stats import sem
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import scipy.constants as const

f0,a0=np.genfromtxt("data/3/10mm.dat",unpack=True)
f1,a1=np.genfromtxt("data/3/13mm.dat",unpack=True)
f2,a2=np.genfromtxt("data/3/16mm.dat",unpack=True)

fk0=np.array([586,866,1134,1376,1581,1726,3462,3579,3736,3906,4070,4207,6817,6892,6986,7108,7223,7309,10230,10317,10409,10500])
k0=np.arange(1,fk0.size+1)
fk1=np.array([672,989,1303,1598,1870,2075,3459,3656,3891,4132,4359,4561,4687,6781,6903,7068,7251,7426,7574,10079,10182,10322,10476,10632,10756])
k1=np.arange(1,fk1.size+1)
fk2=np.array([723,1084,1432,1767,2090,2372,3340,3473,3739,4046,4362,4645,4910,5093,6630,6730,6929,7179,7428,7669,7893,9982,10143,10358,10583,10803,10996])
k2=np.arange(1,fk2.size+1)

np.savetxt("data/3tab0.csv",np.column_stack([k0,fk0]),delimiter=",",fmt=["%2.0f","%5.0f"])
np.savetxt("data/3tab1.csv",np.column_stack([k1,fk1]),delimiter=",",fmt=["%2.0f","%5.0f"])
np.savetxt("data/3tab2.csv",np.column_stack([k2,fk2]),delimiter=",",fmt=["%2.0f","%5.0f"])

plt.figure(figsize=[8,8])

plt.subplot(3,2,1)
plt.title("a)",loc="left")
plt.grid()
plt.plot(f0,a0,"r-",lw=0.5,label="10mm Blenden")
plt.ylabel(r'Amplitude')
plt.xlabel(r'f / $\si{\hertz}$')
plt.legend(loc="best")

plt.subplot(3,2,2)
plt.title("b)",loc="left")
plt.grid()
plt.plot(k0,fk0,"k.",ms=1.5,label="10mm Blenden")
plt.xlabel(r'k')
plt.ylabel(r'f / $\si{\hertz}$')
plt.legend(loc="best")

plt.subplot(3,2,3)
plt.grid()
plt.plot(f1,a1,"r-",lw=0.5,label="13mm Blenden")
plt.ylabel(r'Amplitude')
plt.xlabel(r'f / $\si{\hertz}$')
plt.legend(loc="best")

plt.subplot(3,2,4)
plt.grid()
plt.plot(k1,fk1,"k.",ms=1.5,label="13mm Blenden")
plt.xlabel(r'k')
plt.ylabel(r'f / $\si{\hertz}$')
plt.legend(loc="best")

plt.subplot(3,2,5)
plt.grid()
plt.plot(f2,a2,"r-",lw=0.5,label="16mm Blenden")
plt.ylabel(r'Amplitude')
plt.xlabel(r'f / $\si{\hertz}$')
plt.legend(loc="best")

plt.subplot(3,2,6)
plt.grid()
plt.plot(k2,fk2,"k.",ms=1.5,label="16mm Blenden")
plt.xlabel(r'k')
plt.ylabel(r'f / $\si{\hertz}$')
plt.legend(loc="best")

plt.tight_layout()

plt.savefig("build/3.pdf")
