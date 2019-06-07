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
	F[3] = 0
	return F

## runge-kutta methon in many body problem
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
                    collision(x[i],x[j],e)
        for i in range(n):
            x[i] = x[i] + dx(F,t,x[i],h)
            xs[i].append(x[i])
        t = t + h
        ts.append(t)
    for i in range(n):
        xs[i] = np.array(xs[i])
    return np.array(ts),xs

### 1-D collision
#def collision(p1,p2):
#    temp = p1[1]; p1[1] = p2[1]; p2[1] = temp
#    return 0

## 2-D collision
## e is coefficient of restitution
## p = [ x, x', y, y']
def collision(p1,p2,e):
    tan = (p2[2] - p1[2])/(p2[0] - p1[0])
    cos = 1/(tan**2+1)**0.5
    sin = (1-cos**2)**0.5
    
    u1 = p1.copy()
    u2 = p2.copy()

    p1[1] = e*((u2[1]*cos*cos - u2[3]*sin*cos) + u1[1]*sin*sin + u1[3]*sin*cos)
    p1[3] = e*(u1[1]*sin*cos + u1[3]*cos*cos - (u2[1]*sin*cos - u2[3]*sin*sin))

    p2[1] = e*((u1[1]*cos*cos - u1[3]*sin*cos) + u2[1]*sin*sin + u2[3]*sin*cos)
    p2[3] = e*(u2[1]*sin*cos + u2[3]*cos*cos - (u1[1]*sin*cos - u1[3]*sin*sin))
    return 0

e = 1.0 # elastic collision
d = 1.0e-03
h = 0.01

p = lambda p1,p2: [p1[1]+p2[1],p1[3]+p2[3]]
v = lambda p:[p[1],p[3]]

x0 = np.array([-4,5,-3,3])
x1 = np.array([2,-1,-2,2])

#x0 = np.array([1,-1,0,0])
#x1 = np.array([-2,2,0,0])

print(v(x0),v(x1),p(x0,x1))

x_init = [x0,x1]

ts, xs = integrate(F,0.0,x_init,2.0,h)

x0=xs[0][len(ts)-1,:]
x1=xs[1][len(ts)-1,:]
print(v(x0),v(x1),p(x0,x1))

## plot
legend = []
for i in range(len(xs)):
    plt.plot(xs[i][:,0],xs[i][:,2],'-')
    legend.append('particle '+str(i))

plt.legend(legend)

#plt.plot(ts,xs[1][:,0],'-',ts,xs[3][:,0],'-')
plt.grid()
plt.show()
