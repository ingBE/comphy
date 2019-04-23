'''
Roots class exercise

 1. Newton Raphson method for roots.
 Find the cubic root of 70 up to three iterations
 and give the answers with rational numbers. 

 2. Find the smallest root of  x**3 - 20.0*x**2 + 5*x +3 = 0
 using any method. 
'''

'''
1.
import numpy as np
f = lambda x:x**3 - 70
f' = lambda x:3*x**2

x_n = x_(n-1) - f(x_(n-1))/f'(x_(n-1))

x_0 = 4
x_1 = 4 + 6/48 = 4.125
x_2 = 4.121288644015917
x_3 = 4.12128529981127
'''

## 2.
## newton-raphson algorithm

from bisection00 import bisection
from newtonRaphson import newtonRaphson

f = lambda x:x**3 - 20.0*x**2 + 5.0*x +3

root, error = bisection(f)
print(root,f(root),error)
print(newtonRaphson(f,0,dx=0.001,ite=100),f(newtonRaphson(f,0,dx=0.001,ite=100)))
