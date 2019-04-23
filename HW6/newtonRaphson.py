import numpy as np

def newtonRaphson(f,x,dx = 0.1,ite = 10):
    for i in range(ite):
        diff = (f(x+dx)-f(x))/dx
        x -= f(x)/diff
    return x

