import numpy as np
import matplotlib.pyplot as plt

## distance of 2-D
## x = [ x, x', y, y']
## distance(particle 1,particle 2) = ( (x1-x2)^2 + (y1-y2)^2 )^0.5
distance = lambda x1,x2:((x1[0]-x2[0])**2+(x1[2]-x2[2])**2)**0.5

## x 	= [ x, x', y, y']
## F = dx/dt = [ v_x, a_x, v_y, a_y ]
def F(t,x):
	g = -9.8 # m/sec^2
	F = np.zeros(4)
	F[0] = x[1]
	F[1] = 0
	F[2] = x[3]
	F[3] = g
	return F

# 2-body problem
def integrate(F,tStart,x_init,tStop,h):
    def dx(F,t,x,h):
        k0 = h*F(t,x)
        k1 = h*F(t+h/2.0,x+k0/2.0)
        k2 = h*F(t+h/2.0,x+k1/2.0)
        k3 = h*F(t+h,x+k2)
        return (k0 + 2.0*k1 + 2.0*k2 + k3)/6.0
    n = len(x_init)
    t = tStart
    x = x_init
    ts = []
    ts.append(t)
    xs = []
    for i in range(n):
        xs.append([])
        xs[i].append(x[i])
    while t < tStop:
        # collision test
        for i in range(n):
            for j in range(i+1,n):
                if distance(x[i],x[j]) < d:
                    print('collision',i,j,' --- ',t)
                    temp = x[i][1]; x[i][1] = x[j][1]; x[j][1] = temp
        for i in range(n):
            x[i] = x[i] + dx(F,t,x[i],h)
            xs[i].append(x[i])
        t = t + h
        ts.append(t)
    for i in range(n):
        xs[i] = np.array(xs[i])
    return np.array(ts),xs

d = 1.0e-03
h = 0.01

x0 = np.array([1.5,-0.5,0.0,9.8])
x1 = np.array([-1 ,2   ,9.8,0.0])
x2 = np.array([0.5,-1  ,9.8,0.0])
x3 = np.array([6.4599999999,-5  ,2.499,4.9])
x_init = [x0,x1,x2,x3]
#x_init = [x0,x1,x2]

ts, xs = integrate(F,0.0,x_init,2.0,h)

legend = []
for i in range(len(xs)):
    plt.plot(xs[i][:,0],xs[i][:,2],'-')
    legend.append('particle '+str(i))

plt.legend(legend)

#plt.plot(ts,xs[1][:,0],'-',ts,xs[3][:,0],'-')
plt.grid()
plt.show()
