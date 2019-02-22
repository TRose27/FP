import numpy as np
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.stats import sem
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import scipy.constants as const

nu, s1, h1, s2, h2 = np.genfromtxt("data/data.csv",unpack=True,delimiter=",")

B1 = ((const.mu_0 * 8)/np.sqrt(125))*((s1*11)/0.1639 + (h1*154)/0.1579) #mT

B2 = ((const.mu_0 * 8)/np.sqrt(125))*((s2*11)/0.1639 + (h2*154)/0.1579) #mT

B1=B1*1000 #µT
B2=B2*1000 #µT

np.savetxt("data/tab.csv",np.column_stack([nu,s1,h1,B1,s2,h2,B2]),delimiter=",",fmt=["%4.0f","%3.0f","%3.0f","%3.2f","%3.0f","%3.0f","%3.2f"])

plt.grid()
plt.plot(nu,B1,"kx",label="Rubidium-85")
plt.plot(nu,B2,"k.",label="Rubidium-87")

def f(x, a, b):
    return a*x+b

params, covariance_matrix = curve_fit(f,nu ,B1 )
errors = np.sqrt(np.diag(covariance_matrix))

print('a1=', params[0], '+-', errors[0])
print('b1=', params[1], '+-', errors[1])

plt.plot(nu,f(nu,*params),'r-', label='Fit 1')
a1=ufloat(params[0],errors[0])
b1=ufloat(params[1],errors[1])

def f(x, a, b):
    return a*x+b

params, covariance_matrix = curve_fit(f,nu ,B2 )
errors = np.sqrt(np.diag(covariance_matrix))

print('a2=', params[0], '+-', errors[0])
print('b2=', params[1], '+-', errors[1])

plt.plot(nu,f(nu,*params),'b-', label='Fit 2')
a2=ufloat(params[0],errors[0])
b2=ufloat(params[1],errors[1])

plt.xlabel(r'$\nu$ / $\si{\kilo\hertz}$')
plt.ylabel(r'B / $\si{\micro\tesla}$')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.legend(loc="best")
plt.savefig('build/auswertung.pdf')

a1=a1*1e-9
a2=a2*1e-9

gf1=(4 * np.pi * const.m_e)/(const.e * a1)
gf2=(4 * np.pi * const.m_e)/(const.e * a2)

Berde = (b1+b2)/2

I1= (1/gf1)-0.5
I2= (1/gf2)-0.5

U1=gf1**2 * ((const.e * const.hbar)/(2* const.m_e ))**2 * (143.11e-6)**2 * (1+2*(I1+0.5))/2.01e-24
U2=gf2**2 * ((const.e * const.hbar)/(2* const.m_e ))**2 * (212.12e-6)**2 * (1+2*(I2+0.5))/4.53e-24

print("gf1=",gf1)
print("gf2=",gf2)
print("Berde=",Berde)
print("I1=",I1)
print("I2=",I2)
print("U1=",U1)
print("U2=",U2)
