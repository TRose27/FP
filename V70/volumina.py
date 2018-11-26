import numpy as np
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.stats import sem
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import scipy.constants as const


num=np.arange(1,11)
b1=ufloat(9.5,0.8)
b2=ufloat(0.177,0.09)
v3z=ufloat(0.005,0.001)
v3o=ufloat(0.015,0.002)
s1=ufloat(0.087,0.011)
s2=ufloat(0.8,0.1)
v4=ufloat(0.025,0.005)
b4=ufloat(0.067,0.004)
v1o=ufloat(0.044,0.004)
v1z=ufloat(0.022,0.002)

#b5 Volumen berechnen
di=ufloat(10,0.5)
l1=ufloat(80,0.5)
l2=ufloat(30,1)

b5=np.pi*((di/2)**2)*l1+2*np.pi*((di/2)**2)*l2
b5=b5*1e-6
print("Vol B5 in l:",b5)
b5a=ufloat(0.016,0.002)
print("B5 aus Anleitung:",b5a)
#b3 Volumen berechnen

di2=ufloat(40,0.5)
l12=ufloat(128.2,0.5)
l22=ufloat(45,2)

b3=np.pi*((di2/2)**2)*l12+np.pi*((di2/2)**2)*l22
b3=b3*1e-6
print("Vol B3 in l:",b3)
b3a=ufloat(0.25,0.01)
print("B3 aus Anleitung",b3a)


volo=np.array([b1,b3,b2,v3o,s1,v1o,b4,b5,s2,v4])
np.savetxt("data/voltab.csv",np.column_stack([num,unp.nominal_values(volo),unp.std_devs(volo)]),delimiter=",",fmt=["%4.0f","%4.3f","%4.3f"])


vdrehevak=b1+b3+b3+b2+v3o+v3z+v3z+s1+v1z+b5+s2+v4
vturboevak=b1+b3+b3+b2+v3z+v3z+v1o+b4

print("V Drehevak in l:",vdrehevak)
print("V Turboevak in l:",vturboevak)
