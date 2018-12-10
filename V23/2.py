import numpy as np
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.stats import sem
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import scipy.constants as const

f,a=np.genfromtxt("data/2/overview.dat",unpack=True)
k=np.arange(1,39)
fk=np.array([611,1013,1454,1748,2023,2592,2896,3180,3474,3758,4023,4327,4592,4876,5170,5445,5749,6043,6328,6612,6886,7171,7465,7730,8034,8318,8602,8906,9171,9475,9760,10034,10328,10623,10907,11191,11476,11770])

np.savetxt("data/2tab.csv",np.column_stack([k,fk]),delimiter=",",fmt=["%2.0f","%5.0f"])

plt.figure(figsize=[8,3])
plt.subplot(1,2,1)
plt.title("a)",loc="left")
plt.grid()
plt.plot(f,a,"r-",lw=0.5)
plt.ylabel(r'Amplitude')
plt.xlabel(r'f / $\si{\hertz}$')
plt.legend(loc="best")

plt.subplot(1,2,2)
plt.title("b)",loc="left")
plt.grid()
plt.plot(k,fk,"k.",ms=1.5)
plt.xlabel(r'k')
plt.ylabel(r'f / $\si{\hertz}$')
plt.legend(loc="best")

plt.tight_layout()

plt.savefig("build/2.pdf")
