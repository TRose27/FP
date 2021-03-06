import numpy as np
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.stats import sem
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import scipy.constants as const

p, t1, t2, t3, t4, t5 = np.genfromtxt("data/turboevak.csv",delimiter=",",unpack=True)
V=ufloat(10.2,0.8)
pe=ufloat(1e-5,1e-6)
p0=ufloat(5e-3,5e-4)
t0=np.column_stack([t1,t2,t3,t4,t5])
t=t0.mean(axis=1)
terr=sem(t0,axis=1)
perr=0.1*p
pges=unp.uarray(p,perr)
pln=(p-pe)/(p0-pe)
lnpges=unp.log(pln)
p=p*1e+5
perr=perr*1e+5
np.savetxt("data/turboevaktab.csv",np.column_stack([p,perr,unp.nominal_values(lnpges),unp.std_devs(lnpges),t1,t2,t3,t4,t5,t,terr]),delimiter=",",fmt=["%3.2f","%3.2f","%3.2f","%3.2f","%4.2f","%4.2f","%4.2f","%4.2f","%4.2f","%4.2f","%4.2f"])
p=p*1e-5
perr=perr*1e-5


plt.grid()
plt.errorbar(t,unp.nominal_values(lnpges),xerr=terr,yerr=unp.std_devs(lnpges),fmt=".",color="k",markersize="3",elinewidth="1.5",label="Messdaten")


def f(x, a, b):
    return a*x+b

params, covariance_matrix = curve_fit(f, t[:8], unp.nominal_values(lnpges)[:8])
errors = np.sqrt(np.diag(covariance_matrix))

print('a1=', params[0], '+-', errors[0])
print('b1=', params[1], '+-', errors[1])
a1=ufloat(params[0],errors[0])
s1=-a1*V
plt.plot(t[:8], f(t[:8], *params), 'r-', label='Fit 1')

params, covariance_matrix = curve_fit(f, t[7:], unp.nominal_values(lnpges)[7:])
errors = np.sqrt(np.diag(covariance_matrix))

print('a2=', params[0], '+-', errors[0])
print('b2=', params[1], '+-', errors[1])
a2=ufloat(params[0],errors[0])
s2=-a2*V

print("S1 in l/s =",s1)
print("S2 in l/s =",s2)

plt.plot(t[7:], f(t[7:], *params), 'b-', label='Fit 2')
plt.xlabel(r't / $\si{\second}$')
plt.ylabel(r'$\ln \Bigl(\frac{p(t) - p_E}{p_0 - p_E}\Bigr)$')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.legend(loc="best")
plt.savefig('build/turboevak.pdf')
