
import numpy as np 
import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit 
import scipy.constants as const 

lam,phi1r,phi2r,thetar,phi1u,phi2u,thetau = np.genfromtxt("data/daten.csv",unpack=True,comments="#",delimiter=",") #lambda/mum , Winkel / Deg

def f(x, a,b):
    return -a*x+b

phi1r, phi2r, phi1u, phi2u = np.deg2rad([phi1r,phi2r,phi1u,phi2u])

thetar = 0.5*(phi1r-phi2r)
thetar = thetar / (5.11*10**(-3)) #rad/m
thetau = 0.5*(phi1u-phi2u)
thetau = thetau / (1.36*10**(-3)) #rad/m

thetanorm = thetar-thetau  #Beide Winkel voneinander abgezogen in rad/m
#thetanorm = abs(thetanorm)

np.savetxt("data/daten2.csv", np.column_stack([lam,phi1r,phi2r,thetar,phi1u,phi2u,thetau,thetanorm]), fmt="%1.2f", delimiter=",",
 header="lambda/mum, phi1,phi2,thetar,phi1,phi2,thetau,thetanorm   Winkel in Rad | erst rein zwei unrein normiert")

lam = lam * 10**(-6) #im m
lam = lam**2 #Wellenlänge quadriert

params, cm = curve_fit(f, lam, thetanorm,p0=(-2.4*10**(11),0))
errors = np.sqrt(np.diag(cm))

print("a = ",params[0]," +- ",errors[0])
print("b = ",params[1]," +- ",errors[1])

B=414*10**(-3) #in T
N=1.2*10**(18) #in 1/cm^3
N=N*10**6 #in 1/m^3
n=3.3
a=params[0]
k=(const.e**3)/(8*np.pi**2*const.epsilon_0*const.c**3)*(N*B/n)
m = np.sqrt((const.e**3)/(8*np.pi**2*const.epsilon_0*const.c**3) * (N*B/n) * (1/params[0]))
merr = np.sqrt((-0.5*(k/a)**(-0.5)*k*a**(-2))**2  * errors[0]**2)
print("m = ",m," +- ",merr)

x_plot = np.linspace(0.8*10**(-12),7.25*10**(-12),1000)
plt.xlim(0.8*10**(-12),7.25*10**(-12))
#x_plot = np.linspace(np.min(lam),np.max(lam),1000)

plt.plot(lam,thetanorm,"bx",label="Messwerte")
plt.plot(x_plot, f(x_plot, *params), "r-",label="Lineare Regression")
plt.xlabel(r'$\lambda^2\,/\,\mathrm{m^2}$')
plt.ylabel(r'$\theta\,/\,\frac{\mathrm{rad}}{\mathrm{m}}$')
plt.legend(loc="best")
plt.grid()
#plt.show()
plt.savefig("build/Messergebnisse.pdf")