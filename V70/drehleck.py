import numpy as np
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.stats import sem
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import scipy.constants as const
#Erste Messung
p,t1,t2,t3 = np.genfromtxt("data/drehleck1.csv",delimiter=",",unpack=True)
V=ufloat(11.1,0.8)
t0=np.column_stack([t1,t2,t3])
t=t0.mean(axis=1)
terr=np.std(t0,axis=1)
perr=0.2*p

np.savetxt("data/drehleck1tab.csv",np.column_stack([p,perr,t1,t2,t3,t,terr]),delimiter=",",fmt=["%4.2f","%4.2f","%4.2f","%4.2f","%4.2f","%4.2f","%4.2f"])


def f(x, a, b):
    return a*x+b

params, covariance_matrix = curve_fit(f, t, p)
errors = np.sqrt(np.diag(covariance_matrix))

print('a=', params[0], '+-', errors[0])
print('b=', params[1], '+-', errors[1])
a=ufloat(params[0],errors[0])
s1=(V/0.1)*a

plt.grid()
plt.errorbar(t,p,xerr=terr,yerr=perr,fmt=".",color="k",markersize="3",elinewidth="1.5",label="Messdaten")
plt.plot(t,f(t,*params), 'r-', label='Fit')
plt.xlabel(r't / $\si{\second}$')
plt.ylabel(r'p(t) / $\si{\milli\bar}$')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.legend(loc="best")
plt.savefig('build/drehleck1.pdf')
plt.clf()
#Zweite Messung
p,t1,t2,t3 = np.genfromtxt("data/drehleck2.csv",delimiter=",",unpack=True)

t0=np.column_stack([t1,t2,t3])
t=t0.mean(axis=1)
terr=np.std(t0,axis=1)
perr=0.2*p

np.savetxt("data/drehleck2tab.csv",np.column_stack([p,perr,t1,t2,t3,t,terr]),delimiter=",",fmt=["%4.2f","%4.2f","%4.2f","%4.2f","%4.2f","%4.2f","%4.2f"])


def f(x, a, b):
    return a*x+b

params, covariance_matrix = curve_fit(f, t, p)
errors = np.sqrt(np.diag(covariance_matrix))

print('a=', params[0], '+-', errors[0])
print('b=', params[1], '+-', errors[1])
a=ufloat(params[0],errors[0])
s2=(V/0.4)*a
plt.grid()
plt.errorbar(t,p,xerr=terr,yerr=perr,fmt=".",color="k",markersize="3",elinewidth="1.5",label="Messdaten")
plt.plot(t,f(t,*params), 'r-', label='Fit')
plt.xlabel(r't / $\si{\second}$')
plt.ylabel(r'p(t) / $\si{\milli\bar}$')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.legend(loc="best")
plt.savefig('build/drehleck2.pdf')
plt.clf()
#Dritte Messung
p,t1,t2,t3 = np.genfromtxt("data/drehleck3.csv",delimiter=",",unpack=True)

t0=np.column_stack([t1,t2,t3])
t=t0.mean(axis=1)
terr=np.std(t0,axis=1)
perr=0.2*p

np.savetxt("data/drehleck3tab.csv",np.column_stack([p,perr,t1,t2,t3,t,terr]),delimiter=",",fmt=["%4.2f","%4.2f","%4.2f","%4.2f","%4.2f","%4.2f","%4.2f"])


def f(x, a, b):
    return a*x+b

params, covariance_matrix = curve_fit(f, t, p)
errors = np.sqrt(np.diag(covariance_matrix))

print('a=', params[0], '+-', errors[0])
print('b=', params[1], '+-', errors[1])
a=ufloat(params[0],errors[0])
s3=(V/0.8)*a
plt.grid()
plt.errorbar(t,p,xerr=terr,yerr=perr,fmt=".",color="k",markersize="3",elinewidth="1.5",label="Messdaten")
plt.plot(t,f(t,*params), 'r-', label='Fit')
plt.xlabel(r't / $\si{\second}$')
plt.ylabel(r'p(t) / $\si{\milli\bar}$')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.legend(loc="best")
plt.savefig('build/drehleck3.pdf')
plt.clf()
#Vierte Messung
p,t1,t2,t3 = np.genfromtxt("data/drehleck4.csv",delimiter=",",unpack=True)

t0=np.column_stack([t1,t2,t3])
t=t0.mean(axis=1)
terr=np.std(t0,axis=1)
perr=0.2*p

np.savetxt("data/drehleck4tab.csv",np.column_stack([p,perr,t1,t2,t3,t,terr]),delimiter=",",fmt=["%4.2f","%4.2f","%4.2f","%4.2f","%4.2f","%4.2f","%4.2f"])


def f(x, a, b):
    return a*x+b

params, covariance_matrix = curve_fit(f, t, p)
errors = np.sqrt(np.diag(covariance_matrix))

print('a=', params[0], '+-', errors[0])
print('b=', params[1], '+-', errors[1])
a=ufloat(params[0],errors[0])
s4=(V/1)*a


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
plt.savefig('build/drehleck4.pdf')
