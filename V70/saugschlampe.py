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
error1=0.06
y1err=np.array([0.06,0.06])
x2=np.array([0.6,1013])
y2=np.array([1.04,1.04])
error2=0.08
y2err=np.array([0.08,0.08])

x3=0.1
y3=0.53
y3err=0.12
x4=0.4
y4=0.92
y4err=0.2
x5=0.8
y5=1.32
y5err=0.28
x6=1
y6=1.37
y6err=0.29
plt.errorbar(x1,y1,yerr=y1err,linestyle="-",capsize=5,marker="o",color="b",label="Evakuierungsmessung",markersize=3)
plt.fill_between(x1,y1-error1,y1+error1,color="b",alpha=0.3)
plt.errorbar(x2,y2,yerr=y2err,linestyle="-",capsize=5,marker="o",color="b",markersize=3)
plt.fill_between(x2,y2-error2,y2+error2,color="b",alpha=0.3)
plt.errorbar(x3,y3,yerr=y3err,fmt="o",color="r",capsize=5,label="Leckratenmessung",markersize=3)
plt.errorbar(x4,y4,yerr=y4err,fmt="o",color="r",capsize=5,markersize=3)
plt.errorbar(x5,y5,yerr=y5err,fmt="o",color="r",capsize=5,markersize=3)
plt.errorbar(x6,y6,yerr=y6err,fmt="o",color="r",capsize=5,markersize=3)



plt.xlabel(r'Druck / $\si{\milli\bar}$')
plt.ylabel(r'Saugvermögen / $\si{\litre\per\second}$')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.legend(loc="best")
plt.savefig('build/drehvgl.pdf')

plt.clf()

plt.xscale("log")
plt.grid()
x1=np.array([1.2e-5,3e-5])
y1=np.array([0.245,0.245])
error1=0.04
y1err=np.array([0.04,0.04])
x2=np.array([3e-5,500e-5])
y2=np.array([6.4,6.4])
error2=0.8
y2err=np.array([0.8,0.8])

x3=5e-5
y3=9.1
y3err=1.2
x4=1e-4
y4=19.2
y4err=2.5
x5=1.5e-4
y5=20.5
y5err=2.6
x6=2e-4
y6=16.4
y6err=2.1

plt.errorbar(x1,y1,yerr=y1err,linestyle="-",capsize=5,marker="o",color="b",label="Evakuierungsmessung",markersize=3)
plt.fill_between(x1,y1-error1,y1+error1,color="b",alpha=0.3)
plt.errorbar(x2,y2,yerr=y2err,linestyle="-",capsize=5,marker="o",color="b",markersize=3)
plt.fill_between(x2,y2-error2,y2+error2,color="b",alpha=0.3)
plt.errorbar(x3,y3,yerr=y3err,fmt="o",color="r",capsize=5,label="Leckratenmessung",markersize=3)
plt.errorbar(x4,y4,yerr=y4err,fmt="o",color="r",capsize=5,markersize=3)
plt.errorbar(x5,y5,yerr=y5err,fmt="o",color="r",capsize=5,markersize=3)
plt.errorbar(x6,y6,yerr=y6err,fmt="o",color="r",capsize=5,markersize=3)



plt.xlabel(r'Druck / $\si{\milli\bar}$')
plt.ylabel(r'Saugvermögen / $\si{\litre\per\second}$')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.legend(loc="best")
plt.savefig('build/turbovgl.pdf')
