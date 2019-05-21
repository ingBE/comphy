import numpy as np
import matplotlib.pyplot as plt

x = np.array([1.5,1.9,2.1,2.4,2.6,3.1])
y = np.array([1.06,1.39,1.54,1.73,1.84,2.03])

xar = np.linspace(1.5,3.1,20)

import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from cubicSpline import *

xData = x; yData = y
kvals = curvatures(xData,yData)

def SplineDiff(xData,yData,k,x):
    def findSegment(xData,x):
        iLeft = 0
        iRight = len(xData) - 1
        while 1:
            if (iRight-iLeft) <= 1: 
                return iLeft           
            i = round((iLeft + iRight)/2)
#            print('i ',i, 'x ',x,' xData[i]', xData[i])
            if x < xData[i] : 
                iRight = i
            else: 
                iLeft = i

    i = findSegment(xData,x)
    h = xData[i] - xData[i+1]
    y = (3*(x - xData[i+1])**2/h - h)*k[i]/6.0   \
        - (3*(x - xData[i])**2/h - h)*k[i+1]/6.0   \
        + (yData[i] - yData[i+1])/h
    return y

def SplineDiff2(xData,yData,k,x):
    def findSegment(xData,x):
        iLeft = 0
        iRight = len(xData) - 1
        while 1:
            if (iRight-iLeft) <= 1: 
                return iLeft           
            i = round((iLeft + iRight)/2)
#            print('i ',i, 'x ',x,' xData[i]', xData[i])
            if x < xData[i] : 
                iRight = i
            else: 
                iLeft = i

    i = findSegment(xData,x)
    h = xData[i] - xData[i+1]
    y = (x - xData[i+1])/h*k[i] - (x - xData[i])/h*k[i+1]
    return y

yar = []; dy = []; d2y = []
for i in range(len(xar)):
    ydata = evalSpline(xData,yData,kvals,xar[i])
    dydata = SplineDiff(xData,yData,kvals,xar[i])
    d2ydata = SplineDiff2(xData,yData,kvals,xar[i])
    yar.append(ydata)
    dy.append(dydata)
    d2y.append(d2ydata)

plt.plot(xData,yData,'o',xar,yar,'-',xar,dy,'-',xar,d2y,'-')
plt.legend(['Input Data','Cubic Spline','diff','2nd diff'])
plt.grid()
plt.savefig('fig1')
plt.show()

from polyFit import *
m = 2
coeffs = polyFit(kvals,yData,m)
print( 'Coefficients ', coeffs)
