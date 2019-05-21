## Gauss-Legendre quadrature
print('')

import numpy as np
mapli = lambda f, xs:list(map(f,xs))

########################################
## f(x) = x^2
func0 = lambda x:x**2

## n = 1
x = [ 0, 1 ]; weight = [ 1, 1 ]
fs = mapli(func0,x)

I = ((1-0)/2)*np.dot(weight,fs)
print('Integral x=0 to x=1  x^2          dx = ', I)

########################################
## f(x) = x^2 + 0.3x^6
func1 = lambda x:x**2 + 0.3*x**6

a = 0; b = 10; m = 5

## x, A = gaussNodes(m, tol=10e-9)
from gaussNodes import gaussNodes 

xs, ys = gaussNodes(m)
xsp = ((b+a)/2) + ((b-a)/2)*xs
fs = mapli(func1,xsp)

I = ((b-a)/2)*np.dot(fs,ys)
print('Integral x=0 to x=10 x^2 + 0.3x^6 dx = ',I)

########################################
print('\nsame two integral')
## f(x) = sqrt(x)*cos(x)
func2 = lambda x:np.sqrt(x)*np.cos(x)

a = 0; b = np.pi; m = 15

xs, ys = gaussNodes(m)
xsp = (b+a)/2 + ((b-a)/2)*xs
f = mapli(func1,xsp)

I = ((b-a)/2)*np.dot(f,ys)
print('Integral x=0 to x=pi       sqrt(x)*cos(x) dx = ',I)

## f(x) = 2x^2*cos(x^2)
func2 = lambda x:2*x**2*np.cos(x*x)

a = 0; b = np.sqrt(np.pi); m = 15

xs, ys = gaussNodes(m)
xsp = (b+a)/2 + ((b-a)/2)*xs
fs = mapli(func2,xsp)

I = ((b-a)/2)*np.dot(fs,ys)
print('Integral x=0 to x=sqrt(pi) 2x^2 cos(x^2)  dx = ',I)

########################################
## Integral = gauss_legendre(f,a,b,m)
def gauss_legendre(f,a,b,m):
    xs, ys = gaussNodes(m)
    xsp = ((b+a)/2) + ((b-a)/2)*xar
    fs = mapli(f,xsp)

    I = ((b-a)/2)*np.dot(fs,ys)
    return I

########################################
## 2-Dimension
print('\n2-Dimension integrate')
func = lambda x, y: x*x*y*y*y

from gaussQuad2 import gaussQuad2

xs = [0,1,1,1]; ys = [0,0,1,1]; m = 5

I = gaussQuad2(func,xs,ys,m)
print('         Integral    ',I)

from triangleQuad import triangleQuad

xs = [0,1,1]; ys = [0,0,1]

I = triangleQuad(func,xs,ys)
print('Triangle Integral    ',I)

########################################
def intfun():
    pass

