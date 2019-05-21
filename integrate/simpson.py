import numpy as np

func = lambda x: np.sqrt(x)*np.cos(x)

## Composite Trapezoidal Rule
def trapint(f,a,b,k):
    n = 2**(k-1)
    h = (b - a)/n
    nodes = n + 1
    wts = np.zeros(nodes)
    wts[:] = h; wts[0] = h/2.0; wts[n] = h/2.0

    sum = 0.0; x = a
    for i in range(nodes):
        sum += f(x)*wts[i]
        x += h

    return sum

result = trapint(func,0,np.pi,11)
print('Composite Trapezoidal Rule : ', result)

## Simpson's rule
def simpson(f,a,b,k):
    n = 2**(k-1)
    h = (b - a)/n
    nodes = n + 1
    wts = np.zeros(nodes)
    for i in range(n):
        if i%2 == 0:    wts[i] = 4*h/3
        else:           wts[i] = 2*h/3
    wts[0] = h/3;   wts[n] = h/3

    sum = 0.0; x = a
    for i in range(nodes):
        sum += f(x)*wts[i]
        x += h

    return sum

resurt = simpson(func,0,np.pi,11)
print('Simpson\'s Rule             : ', resurt)
