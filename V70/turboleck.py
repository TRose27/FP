import numpy as np
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.stats import sem
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import scipy.constants as const
#Erste Messung
p,t1,t2,t3 = np.genfromtxt("data/turboleck1.csv",delimiter=",",unpack=True)
V=ufloat(11.2,0.8)
t0=np.column_stack([t1,t2,t3])
t=t0.mean(axis=1)
terr=np.std(t0,axis=1)
perr=0.1*p
p=p*1e+5
perr=perr*1e+5
np.savetxt("data/turboleck1tab.csv",np.column_stack([p,perr,t1,t2,t3,t,terr]),delimiter=",",fmt=["%3.2f","%3.2f","%4.2f","%4.2f","%4.2f","%4.2f","%4.2f"])
p=p*1e-5
perr=perr*1e-5

def f(x, a, b):
    return a*x+b

params, covariance_matrix = curve_fit(f, t, p)
errors = np.sqrt(np.diag(covariance_matrix))

print('a=', params[0], '+-', errors[0])
print('b=', params[1], '+-', errors[1])
a=ufloat(params[0],errors[0])
pg=ufloat(5e-5,5e-6)
s1=(V/pg)*a
plt.grid()
plt.errorbar(t,p,xerr=terr,yerr=perr,fmt=".",color="k",markersize="3",elinewidth="1.5",label="Messdaten")
plt.plot(t,f(t,*params), 'r-', label='Fit')
plt.xlabel(r't / $\si{\second}$')
plt.ylabel(r'p(t) / $\si{\milli\bar}$')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.legend(loc="best")
plt.savefig('build/turboleck1.pdf')
plt.clf()
#Zweite Messung
p,t1,t2,t3 = np.genfromtxt("data/turboleck2.csv",delimiter=",",unpack=True)

t0=np.column_stack([t1,t2,t3])
t=t0.mean(axis=1)
terr=np.std(t0,axis=1)
perr=0.1*p
p=p*1e+4
perr=perr*1e+4
np.savetxt("data/turboleck2tab.csv",np.column_stack([p,perr,t1,t2,t3,t,terr]),delimiter=",",fmt=["%3.2f","%3.2f","%4.2f","%4.2f","%4.2f","%4.2f","%4.2f"])
p=p*1e-4
perr=perr*1e-4


def f(x, a, b):
    return a*x+b

params, covariance_matrix = curve_fit(f, t, p)
errors = np.sqrt(np.diag(covariance_matrix))

print('a=', params[0], '+-', errors[0])
print('b=', params[1], '+-', errors[1])
a=ufloat(params[0],errors[0])
pg=ufloat(1e-4,1e-5)
s2=(V/pg)*a
plt.grid()
plt.errorbar(t,p,xerr=terr,yerr=perr,fmt=".",color="k",markersize="3",elinewidth="1.5",label="Messdaten")
plt.plot(t,f(t,*params), 'r-', label='Fit')
plt.xlabel(r't / $\si{\second}$')
plt.ylabel(r'p(t) / $\si{\milli\bar}$')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.legend(loc="best")
plt.savefig('build/turboleck2.pdf')
plt.clf()
#Dritte Messung
p,t1,t2,t3 = np.genfromtxt("data/turboleck3.csv",delimiter=",",unpack=True)

t0=np.column_stack([t1,t2,t3])
t=t0.mean(axis=1)
terr=np.std(t0,axis=1)
perr=0.1*p
p=p*1e+4
perr=perr*1e+4
np.savetxt("data/turboleck3tab.csv",np.column_stack([p,perr,t1,t2,t3,t,terr]),delimiter=",",fmt=["%3.2f","%3.2f","%4.2f","%4.2f","%4.2f","%4.2f","%4.2f"])
p=p*1e-4
perr=perr*1e-4

def f(x, a, b):
    return a*x+b

params, covariance_matrix = curve_fit(f, t, p)
errors = np.sqrt(np.diag(covariance_matrix))

print('a=', params[0], '+-', errors[0])
print('b=', params[1], '+-', errors[1])
a=ufloat(params[0],errors[0])
pg=ufloat(1.5e-4,1.5e-5)
s3=(V/pg)*a
plt.grid()
plt.errorbar(t,p,xerr=terr,yerr=perr,fmt=".",color="k",markersize="3",elinewidth="1.5",label="Messdaten")
plt.plot(t,f(t,*params), 'r-', label='Fit')
plt.xlabel(r't / $\si{\second}$')
plt.ylabel(r'p(t) / $\si{\milli\bar}$')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.legend(loc="best")
plt.savefig('build/turboleck3.pdf')
plt.clf()
#Vierte Messung
p,t1,t2,t3 = np.genfromtxt("data/turboleck4.csv",delimiter=",",unpack=True)

t0=np.column_stack([t1,t2,t3])
t=t0.mean(axis=1)
terr=np.std(t0,axis=1)
perr=0.1*p
p=p*1e+4
perr=perr*1e+4
np.savetxt("data/turboleck4tab.csv",np.column_stack([p,perr,t1,t2,t3,t,terr]),delimiter=",",fmt=["%3.2f","%3.2f","%4.2f","%4.2f","%4.2f","%4.2f","%4.2f"])
p=p*1e-4
perr=perr*1e-4

def f(x, a, b):
    return a*x+b

params, covariance_matrix = curve_fit(f, t, p)
errors = np.sqrt(np.diag(covariance_matrix))

print('a=', params[0], '+-', errors[0])
print('b=', params[1], '+-', errors[1])
a=ufloat(params[0],errors[0])
pg=ufloat(2e-4,2e-5)
s4=(V/pg)*a
print("S1 in l/s=",s1)
print("S2 in l/s=",s2)
print("S3 in l/s=",s3)
print("S4 in l/s=",s4)

plt.grid()
plt.errorbar(t,p,xerr=terr,yerr=perr,fmt=".",color="k",markersize="3",elinewidth="1.5",label="Messdaten")
plt.plot(t,f(t,*params), 'r-', label='Fit')
plt.xlabel(r't / $\si{\second}$')
plt.ylabel(r'p(t) / $\si{\milli\bar}$')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.legend(loc="best")
plt.savefig('build/turboleck4.pdf')
