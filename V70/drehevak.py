import numpy as np
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.stats import sem
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import scipy.constants as const

p, t1, t2, t3, t4, t5 = np.genfromtxt("data/drehevak.csv",delimiter=",",unpack=True)

t0=np.column_stack([t1,t2,t3,t4,t5])
print(t0)
t=t0.mean(axis=1)
terr=np.std(t0,axis=1)
print(t)
print(terr)
