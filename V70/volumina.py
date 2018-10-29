import numpy as np
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.stats import sem
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import scipy.constants as const

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


vdrehevak=b1+b2+b3+v3z+v3o+s1+b5+v3z+s2+v4
vdrehleck=b1+b2+b3+v3o+v3o+s1+b5+v3z+s2+v4
vturboevak=vdrehevak+b3+b4+v3o-v3z+v1o
vturboleck=vturboevak-v1o+v1z-v3z+v3o

print("V Drehevak in l:",vdrehevak)
print("V Drehleck in l:",vdrehleck)
print("V Turboevak in l:",vturboevak)
print("V Turboleck in l",vturboleck)
