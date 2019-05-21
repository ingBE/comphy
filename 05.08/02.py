import numpy as np

func = lambda x: np.sqrt(x)*np.cos(x)

## Recursive Trapezoidal Rule
from trapezoid import *

Iold    = 0.0
a       = 0.0
b       = np.pi

for k in range(1,10):
    Inew = trapezoid(func,a,b,Iold,k)
    Iold = Inew

    print('Inew : ', Inew, '    Panel : ', 2**(k-1))

## Romberg Integration
from romberg import *
print(romberg(func,a,b,tol = 1.0e-06))
