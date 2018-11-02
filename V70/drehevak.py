import numpy as np
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.stats import sem
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import scipy.constants as const

p, t1, t2, t3, t4, t5 = np.genfromtxt("data/drehevak.csv",delimiter=",",unpack=True)
V=ufloat(11.1,0.8)
pe=ufloat(4e-2,0.8e-2)
p0=ufloat(1013,202.6)
t0=np.column_stack([t1,t2,t3,t4,t5])
t=t0.mean(axis=1)
terr=np.std(t0,axis=1)
perr=0.2*p
pges=unp.uarray(p,perr)
pges=(p-pe)/(p0-pe)
lnpges=unp.log(pges)

np.savetxt("data/drehevaktab.csv",np.column_stack([p,perr,unp.nominal_values(lnpges),unp.std_devs(lnpges),t1,t2,t3,t4,t5,t,terr]),delimiter=",",fmt=["%3.2f","%3.2f","%3.2f","%3.2f","%4.2f","%4.2f","%4.2f","%4.2f","%4.2f","%4.2f","%4.2f"])

plt.grid()
plt.errorbar(t,unp.nominal_values(lnpges),xerr=terr,yerr=unp.std_devs(lnpges),fmt=".",color="k",markersize="3",elinewidth="1.5",label="Messdaten")


def f(x, a, b):
    return a*x+b

params, covariance_matrix = curve_fit(f, t[:11], unp.nominal_values(lnpges)[:11])
errors = np.sqrt(np.diag(covariance_matrix))

print('a1=', params[0], '+-', errors[0])
print('b1=', params[1], '+-', errors[1])

plt.plot(t[:11], f(t[:11], *params), 'r-', label='Fit 1')
a1=ufloat(params[0],errors[0])
s1=-a1*V

params, covariance_matrix = curve_fit(f, t[10:], unp.nominal_values(lnpges)[10:])
errors = np.sqrt(np.diag(covariance_matrix))

print('a2=', params[0], '+-', errors[0])
print('b2=', params[1], '+-', errors[1])
a2=ufloat(params[0],errors[0])
s2=-a2*V

print("S1 in l/s =",s1)
print("S2 in l/s =",s2)

plt.plot(t[10:], f(t[10:], *params), 'b-', label='Fit 2')
plt.xlabel(r't / $\si{\second}$')
plt.ylabel(r'$\ln(\frac{p(t) - p_E}{p_0 - p_E})$')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.legend(loc="best")
plt.savefig('build/drehevak.pdf')
