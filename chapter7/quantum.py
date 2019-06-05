import numpy as np
import matplotlib.pyplot as plt
from newtonRaphson2 import *

vpot = lambda _:0.0
#def vpot(x):
#    if x < 5*angstr: return -3*13.6*eV
#    else: return 0.0

def Eval():
    return 5*6.0246672615979e-20

def F(x,y):
    
    hbar =  1.054571800*1e-34   # Joules*second.   6.582119514*1e-16   # eV*second
    me   =  9.1093837015*1e-31  # Kg.   0.51099895000       # MeV/c^2  
    eV   =  1.602176634*1e-19   # Electron volts in Joules
    
    C    = hbar*hbar/(2.0*me)   # Pending unit conversion
    F    = np.zeros(2)
    F[0] = y[1]
    F[1] = ((vpot(x) - Eval())/C)*y[0]
    return F


hbar =  1.054571800*1e-34   # Joules*second.   6.582119514*1e-16   # eV*second
me   =  9.1093837015*1e-31  # Kg.   0.51099895000       # MeV/c^2  
eV   =  1.602176634*1e-19   # Electron volts in Joules

# Define the box
angstr = 1e-10
x      = 0.0
xStop  = 10*angstr   # 10 angstroms.

L = xStop - x 
# Analytical quantized energy values E_n= hbar^2 n^2 / (2*m* L^2) *n^2
#  
E1 = hbar**2.0 *np.pi**2.0 / (2.0*me*L**2.0)

from ridder import *
from run_kut4 import *

h = 0.01*angstr
def r(u):
    xs,ys = integrate(F,x,initCond(u),xStop,h)
    y = ys[len(ys)-1]
    r= y[0]
    return r

initCond = lambda u:np.array([0.0, u])



xs, ys = integrate(F,x,initCond(2),xStop,h)
plt.plot(xs,ys[:,0],'o')
plt.grid()
plt.show()
