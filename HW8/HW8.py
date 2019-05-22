import numpy as np

## Integral module from comphy2019 github
from gaussQuad2   import *
from triangleQuad import *

## Problem 1

print("\n            #### Problem 1. ####")

def printIntegral(f,xs,ys,m=5):
    gauss = gaussQuad2(f,xs,ys,m)
    triangle = triangleQuad(f,xs[:2]+xs[3:4],ys[:2]+ys[3:4])\
            + triangleQuad(f,xs[1:4],ys[1:4])
    print(" Gauss    Integral    ",gauss)
    print(" Triangle Integral    ",triangle)
    return gauss, triangle

print(" 1) f(x,y) = (1 - x^2)(1 - y^2)")
f = lambda x,y:(1 - x**2)*(1 - y**2)
printIntegral(f,[-1, 1, 1,-1],[-1,-1, 1, 1])

print("\n 2) f(x,y) = x^2 y^2")
f = lambda x,y:x**2*y**2
printIntegral(f,[0,3,3,0],[0,0,2,2])

print("\n 3) f(x,y) = exp(-(x^2+y^2))")
f = lambda x,y:np.exp(-(x**2+y**2))
printIntegral(f,[-1, 1, 1,-1],[-1,-1, 1, 1])

print("\n 4) f(x,y) = cos(pi(x-y)/2")
f = lambda x,y:np.cos(np.pi*(x-y)/2)
printIntegral(f,[-1, 1, 1,-1],[-1,-1, 1, 1])


## Problem 2
print("\n\n            #### Problem 2. ####")
f = lambda x,y:x
printIntegral(f,[-1, 1, 4, 0],[ 0, 0, 4, 4])


## Problem 3
print("\n\n            #### Problem 3. ####")
f = lambda x,y:x**2
printIntegral(f,[ 0, 3, 0, 0],[-2, 0, 4, 4])

## Problem 4
print("\n\n            #### Problem 4. ####")

xs = [-3, 1, 3,-1]; ys = [-2,-2, 2, 2]

print(" 1) f(x,y) = (2 - x^2)(2 - x*y)")
f = lambda x,y:(2-x**2)*(2-x*y)
printIntegral(f,xs,ys)

print("\n 2) f(x,y) = xy exp(-x^2)")
f = lambda x,y:x*y*np.exp(-x**2)
printIntegral(f,xs,ys)
