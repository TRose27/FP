import numpy as np 
import scipy.constants as const

ve, I = np.genfromtxt("data/data.csv", delimiter=",", unpack=True) #ve in MHz, I in mA
B = 8/np.sqrt(125) * const.mu_0 * 156/0.1 * I # in mT
g = const.h * ve*10**6 / (B*10**(-3) * const.value("Bohr magneton"))

np.savetxt("data/datatab.csv",np.column_stack([ve,I,B,g]),delimiter=",",fmt=["%2.3f","%3.1f","%1.2f","%1.2f"],header="ve/MHz,I/mA,B/mT,g")