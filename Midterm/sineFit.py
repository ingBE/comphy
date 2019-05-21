'''
Fitting sine graph form
f(x;a,b,omega) = a*sin(omega*x) + b*cos(omega*x)
'''

import numpy as np

## sineFit :: coef -> (x -> a*sin(omega*x)+b*cos(omega*x))
sineFit = lambda coef:\
        lambda x:coef[1]*np.sin(coef[0]*x)+coef[2]*np.cos(coef[0]*x)

## Using module newtonRaphson2 from comphy2019 github
from newtonRaphson2 import newtonRaphson2

## f is function for using newtonRaphson2
## f :: (xData,yData)->((a,b,omega)->[dS/da,dS/db,dS/d(omega)])
def f(xData,yData):
    n = len(xData)
    ## xsol[0] = omega, xsol[1] = a, xsol[2] = b
    def aa(xsol):
        omega = xsol[0]; a = xsol[1]; b = xsol[2]
        ## Calculate sum of combination of sine, cosine and y values.
        ys, yc, ss, cc, sc = 0, 0, 0, 0, 0
        for i in range(n):
            ys += yData[i]*np.sin(omega*xData[i])
            yc += yData[i]*np.cos(omega*xData[i])
            ss += np.sin(omega*xData[i])*np.sin(omega*xData[i])
            cc += np.cos(omega*xData[i])*np.cos(omega*xData[i])
            sc += np.sin(omega*xData[i])*np.cos(omega*xData[i])

        ## aa[0] = dS/da, aa[1] = dS/db, aa[2] = dS/d(omega)
        aa = np.zeros(3)
        aa[0] = ys - a*ss - b*sc
        aa[1] = yc - a*sc - b*cc
        aa[2] = a*yc - b*ys - (a*a-b*b)*sc - a*b*(cc-ss)
        return aa
    return aa

## sineCoef :: (xData, yData) -> ((xsol = initial x value) -> coefficients)
sineCoef = lambda xData, yData:\
        lambda xsol:newtonRaphson2(f(xData,yData),xsol)
'''
####################  TEST  #########################
mapli = lambda f,x:list(map(f,x))

def readData( dataName ):
    x = open( dataName, 'r')
    temp = []
    for ii in x.readlines():
        temp.append(ii)
    return mapli( float, temp )

## data[0] = xdata, data[1] = ydata1, data[2] = ydata2
dataName = ['xdata.dat','ydata1.dat','ydata2.dat']
data = mapli( readData, dataName )

g = sineCoef(data[0],data[1])

print(g([1,1,1]))

root = [0.5,1,1]
root = sineCoef(data[0],data[1])(root)
print(root)
print(sineFit(root)(np.pi/2/root[0]))
'''
