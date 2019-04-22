'''
find a suitable interpolating function and calculate numerically
the nonzero root of y(x) = 0. 
'''

import numpy as np
import matplotlib.pyplot as plt
from polyFit import *
from newtonRaphson import newtonRaphson

xData = [0,0.25,0.50,0.75,1.0,1.25,1.5]
yData = [0,-1.2233,-2.2685,-2.8420,-2.2130,2.5478,55.507]

def mapar(f,ar):
    return np.array(list(map(f,ar)))

coef = polyFit(xData,yData,len(xData)-1)

def y(x,coef):
    p = 0
    for i in range(len(coef)):
        p += coef[i]*(x**i)
    return p

f = lambda x:y(x,coef)

root = newtonRaphson(f,1.1,dx=0.01)
print(root)

x = np.linspace(min(xData),max(xData))

plt.plot(xData,yData,'o',x,mapar(lambda x:y(x,coef),x),'-')
plt.grid()
plt.savefig("HW6_3_1")

plt.xlim(root-0.05,root+0.05)
plt.savefig("HW6_3_2")
