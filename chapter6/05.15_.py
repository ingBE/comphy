import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

''' x,A = gaussNodes(m,tol=10e-9)
    Returns nodal abscissas {x} and weights {A} of
    Gauss-Legendre m-point quadrature.
'''
import math
import numpy as np
def gaussNodes(m,tol=10e-9):
    def legendre(t,m):
        p0 = 1.0; p1 = t
        for k in range(1,m):
            p = ((2.0*k + 1.0)*t*p1 - k*p0)/(1.0 + k )
            p0 = p1; p1 = p
        dp = m*(p0 - t*p1)/(1.0 - t**2)
        return p,dp
    A = np.zeros(m)
    x = np.zeros(m)
    nRoots = int((m + 1)/2)         # Number of non-neg. roots
    for i in range(nRoots):
        t = math.cos(math.pi*(i + 0.75)/(m + 0.5))# Approx. root
        for j in range(30):
            p,dp = legendre(t,m)    # Newton-Raphson
            dt = -p/dp; t = t + dt  # method
            if abs(dt) < tol:
                x[i] = t; x[m-i-1] = -t
                A[i] = 2.0/(1.0 - t**2)/(dp**2) # Eq.(6.25)
                A[m-i-1] = A[i]
                break
    return x,A




## module gaussQuad
'''  I = gaussQuad(f,a,b,m).
    Computes the integral of f(x) from x = a to b
    with Gauss-Legendre quadrature using m nodes.
'''

#from gaussNodes import *
def gaussQuad(f,a,b,m):
    c1 = (b + a)/2.0
    c2 = (b - a)/2.0
    x,A = gaussNodes(m)
    sum = 0.0
    for i in range(len(x)):
        sum = sum + A[i]*f(c1 + c2*x[i])
    return c2*sum






## module gaussQuad2
''' I = gaussQuad2(f,xc,yc,m).
    Gauss-Legendre integration of f(x,y) over a
    quadrilateral using integration order m.
    {xc},{yc} are the corner coordinates of the quadrilateral.
'''

#from gaussNodes import *
import numpy as np
def gaussQuad2(f,x,y,m):
    def jac(x,y,s,t):
        J = np.zeros((2,2))
        J[0,0] = -(1.0 - t)*x[0] + (1.0 - t)*x[1]  \
                + (1.0 + t)*x[2] - (1.0 + t)*x[3]
        J[0,1] = -(1.0 - t)*y[0] + (1.0 - t)*y[1]  \
                + (1.0 + t)*y[2] - (1.0 + t)*y[3]
        J[1,0] = -(1.0 - s)*x[0] - (1.0 + s)*x[1]  \
                + (1.0 + s)*x[2] + (1.0 - s)*x[3]
        J[1,1] = -(1.0 - s)*y[0] - (1.0 + s)*y[1]  \
                + (1.0 + s)*y[2] + (1.0 - s)*y[3]
        return (J[0,0]*J[1,1] - J[0,1]*J[1,0])/16.0
    
    
    
    def map(x,y,s,t):
        N = np.zeros(4)
        N[0] = (1.0 - s)*(1.0 - t)/4.0
        N[1] = (1.0 + s)*(1.0 - t)/4.0
        N[2] = (1.0 + s)*(1.0 + t)/4.0
        N[3] = (1.0 - s)*(1.0 + t)/4.0
        xCoord = np.dot(N,x)
        yCoord = np.dot(N,y)
        return xCoord,yCoord



    s,A = gaussNodes(m)
    sum = 0.0
    for i in range(m):
        for j in range(m):
            xCoord,yCoord = map(x,y,s[i],s[j])
            sum = sum + A[i]*A[j]*jac(x,y,s[i],s[j])  \
            *f(xCoord,yCoord)
    return sum




## module triangleQuad
''' integral = triangleQuad(f,xc,yc).
    Integration of f(x,y) over a triangle using
    the cubic formula.
    {xc},{yc} are the corner coordinates of the triangle.
'''
import numpy as np
def triangleQuad(f,xc,yc):
    alpha = np.array([[1/3., 1/3., 1/3.],  \
                      [0.2, 0.2, 0.6],            \
                      [0.6, 0.2, 0.2],            \
                      [0.2, 0.6, 0.2]])
    W = np.array([-27/48.,25/48.,25/48.,25/48.])
    x = np.dot(alpha,xc)
    y = np.dot(alpha,yc)
    A = (xc[1]*yc[2] - xc[2]*yc[1]      \
       - xc[0]*yc[2] + xc[2]*yc[0]      \
       + xc[0]*yc[1] - xc[1]*yc[0])/2.0
    sum = 0.0
    for i in range(4):
        sum = sum + W[i] * f(x[i],y[i])
    return A*sum



## 1 - (1)
def f1(x,y):
    return (1-x**2)*(1-y**2)

x = [-1,  1,  1, -1]
y = [-1, -1,  1,  1]
m = 4

print(gaussQuad2(f1,x,y,m))

## 1 - (2)
def f2(x,y):
    return (x**2)*(y**2)

x = [0,3,3,0]
y = [0,0,2,2]
m = 4

print(gaussQuad2(f2,x,y,m))

## 1 - (3)
def f3(x,y):
    return np.exp(-((x**2)+(y**2)))

x = [-1, 1, 1, -1]
y = [-1,-1, 1,  1]
m = 4

print(gaussQuad2(f3,x,y,m))

## 1 - (4)
def f4(x,y):
    return np.cos((np.pi*(x-y))/2)

print(gaussQuad2(f4,x,y,m))


## 2
def f5(x,y):
    return (1/2)*(x*x*y*y)-(1/6)*(x*x*x-3*x*y*y)-2/3

# quadratic
xar = [-1,-1,2]
yar = [np.sqrt(3),-np.sqrt(3),0]

alpha = np.array([[1/2.,   0., 1/2.],  \
                  [1/2., 1/2.,    0],            \
                  [   0, 1/2., 1/2.]])

xnew = np.dot(alpha,xar)
ynew = np.dot(alpha,yar)

wts = [1/3, 1/3, 1/3]

tmat = np.array([[1,1,1],xar,yar])
area = np.linalg.det(tmat) / 2

print(area)

suma = 0.
for i in range(3):
    suma += wts[i]*area*f5(xnew[i],ynew[i])

print(suma)

# cubic
xc = [-1,-1,2]
yc = [np.sqrt(3),-np.sqrt(3),0]
print(triangleQuad(f5,xc,yc))


filex = open("Kgrid_x.dat")
filey = open("Kgrid_y.dat")
filez = open("Curv_z.dat")

for i in filex:
    xx = i
    xdata = xx.split(',')

for i in filey:
    yy = i
    ydata = yy.split(',')

zarr = []
for i in filez:
    zz = i
    zdata = zz.split(',')
    zdatap = list(map(float,zdata))
    zarr.append(zdatap)

nzarr = np.array(zarr)

xxdata = list(map(float,xdata))
yydata = list(map(float,ydata))

'''
plt.plot(xxdata,yydata,'o')
colors = (0,0,1)
plt.axes().set_aspect(aspect='equal')
plt.axis([-5,5,-5,5])
plt.show()
'''

zzdata = nzarr[:,17]

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.scatter3D(xxdata,yydata,zzdata,c=zzdata)
ax.view_init(30,30)
plt.show()
