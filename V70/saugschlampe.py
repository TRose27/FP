import numpy as np
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.stats import sem
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import scipy.constants as const

plt.xscale("log")
plt.grid()
x1=np.array([0.06,0.6])
y1=np.array([0.57,0.57])
x2=np.array([0.6,1013])
y2=np.array([1.04,1.04])

x3=np.array([0.1,1])
y3=np.array([0.53,0.53])
x4=np.array([0.4,4])
y4=np.array([0.92,0.92])
x5=np.array([0.8,8])
y5=np.array([1.32,1.32])
x6=np.array([1,10])
y6=np.array([1.37,1.37])

plt.plot(x1,y1,"b-",label="Evakuierungsmessung")
plt.plot(x2,y2,"b-")
plt.plot(x3,y3,"r-",label="Leckratenmessung")
plt.plot(x4,y4,"r-")
plt.plot(x5,y5,"r-")
plt.plot(x6,y6,"r-")



plt.xlabel(r'Druck / $\si{\milli\bar}$')
plt.ylabel(r'Saugvermögen / $\si{\litre\per\second}$')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.legend(loc="best")
plt.savefig('build/drehvgl.pdf')

plt.clf()

plt.xscale("log")
plt.grid()
x1=np.array([1.2e-5,3e-5])
y1=np.array([0.27,0.27])
x2=np.array([3e-5,500e-5])
y2=np.array([7,7])

x3=np.array([5e-5,100e-5])
y3=np.array([10,10])
x4=np.array([1e-4,24e-4])
y4=np.array([21.1,21.1])
x5=np.array([1.5e-4,30e-4])
y5=np.array([22.5,22.5])
x6=np.array([2e-4,30e-4])
y6=np.array([18,18])

plt.plot(x1,y1,"b-",label="Evakuierungsmessung")
plt.plot(x2,y2,"b-")
plt.plot(x3,y3,"r-",label="Leckratenmessung")
plt.plot(x4,y4,"r-")
plt.plot(x5,y5,"r-")
plt.plot(x6,y6,"r-")



plt.xlabel(r'Druck / $\si{\milli\bar}$')
plt.ylabel(r'Saugvermögen / $\si{\litre\per\second}$')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.legend(loc="best")
plt.savefig('build/turbovgl.pdf')
