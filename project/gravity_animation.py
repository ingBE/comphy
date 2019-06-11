import numpy as np
#import matplotlib.pyplot as plt
from time import time
from sys import exit

## distance of 2-D
## x = [ x, x', y, y']
## distance(particle 1,particle 2) = ( (x1-x2)^2 + (y1-y2)^2 )^0.5
distance = lambda x1,x2:((x1[0]-x2[0])**2+(x1[2]-x2[2])**2)**0.5

## p 	= [ x, x', y, y']
## F = dx/dt = [ v_x, a_x, v_y, a_y ]
def F(t,p):
    F = np.zeros(4)
    a_x, a_y = gravity(p,x)
    F[0] = p[1]
    F[1] = a_x
    F[2] = p[3]
    F[3] = a_y
    return F

## runge-kutta methon in many body problem
def integrate(F,t,x,h):
    def dx(F,t,x,h):
        k0 = h*F(t,x)
        k1 = h*F(t+h/2.0,x+k0/2.0)
        k2 = h*F(t+h/2.0,x+k1/2.0)
        k3 = h*F(t+h,x+k2)
        return (k0 + 2.0*k1 + 2.0*k2 + k3)/6.0
    n = len(x_init)
    # collision test
    #for i in range(n):
    #    if x[i][0] < -2 or x[i][0] > 2:
    #        x[i][1] = -x[i][1]
    #        if x[i][0] < -2: x[i][0] = -2
    #        else: x[i][0] = 2
    #    if x[i][2] < -2 or x[i][2] > 2:
    #        x[i][3] = -x[i][3]
    #        if x[i][2] < -2: x[i][2] = -2
    #        else: x[i][2] = 2
    #    for j in range(i+1,n):
    #        if distance(x[i],x[j]) < d:
    #            #print('collision',i,j,' --- ',t)
    #            collision(x[i],x[j],e)
    #print(t,x[0][0],x[0][2])
    # update particle state
    for i in range(n):
        x[i] = x[i] + dx(F,t,x[i],h)

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

def gravity(p,x):
    g = 1.0e-3
    F_x = 0.0; F_y = 0.0
    for i in range(len(x)):
        if distance(p,x[i]) >= d/2:
            F_x = F_x - g*p[0]/(p[0]**2+p[2]**2)**3
            F_y = F_y - g*p[2]/(p[0]**2+p[2]**2)**3
        else:
            F_x = F_x - g*p[0]/(d/2)**3
            F_y = F_y - g*p[2]/(d/2)**3
    return F_x,F_y

e = 1.0 # elastic collision
d = 5.0e-02
h = 0.01

def energy(x):
    E_tot = 0
    for i in range(len(x)):
        E_tot = E_tot + (x[i][1]**2 + x[i][3]**2)/2
    return E_tot

p = lambda p1,p2: [p1[1]+p2[1],p1[3]+p2[3]]
v = lambda p:[p[1],p[3]]

#x0 = np.array([-4,5,-3,3])
#x1 = np.array([2,-1,-2,2])

#x0 = np.array([1.0,-1.0,0.0,0.0])
#x1 = np.array([-1.0,1.0,0.0,0.0])

#print(v(x0),v(x1),p(x0,x1))

#x_init = [x0,x1]

n = 2
#from random import random
x_init = []
#for i in range(n):
#    x_init.append(np.array([(random()-0.5)*3.9,(random()-0.5)*2,(random()-0.5)*3.9,(random()-0.5)*2]))
#for i in range(n):
#    for j in range(n):
#        x_init.append(np.array([i,0,j,0]))
x_init = [np.array([10,0,0,40])]
x = x_init.copy()
#x.append(np.array([0,0,0,0]))

ts = [0]
Es = [energy(x)]

def changeSize(w,h):
    if h==0: h=1
    ratio = w/h

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    glViewport(0,0,w,h)

    gluPerspective(45,ratio,0.1,1000)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0.0,0.0,100.0,0.0,0.0,-1.0,0.0,1.0,0.0)

def drawSphere(x,y,z):
    glTranslatef(x,y,z)
    glutSolidSphere(1,10,10)
    glTranslatef(-x,-y,-z)

time1 = time(); time2 = time(); t = 0; ite = 0
def renderScene():
    global time1, time2, t, ite, x
    ite = ite + 1
    #if ite > 10: exit()
    #print(time(),x[0][0])
    glClearColor(0,0,0,0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()

    for i in range(len(x)):
        glColor3f(0.9,0.9,0.9)
        drawSphere(x[i][0],x[i][2],0)

    glPopMatrix()
    #fps()
    dt = time2 - time1
    glutSwapBuffers()
    if ite > -1:
        integrate(F,t,x,dt)
        #x[0][0] = x[0][0] + 0.1
        t = t + dt
        E = energy(x)
        Es.append(E)
        ts.append(t)
    if ite % 100 == 0:
        print(x[0][0],dt)
    time1 = time2
    time2 = time()
    #print(t,x[0][0])

from OpenGL._bytes import as_8_bit
ESC = as_8_bit('\033')
def exitKey(key,x,y):
    if key == ESC:
        exit()
    if key == as_8_bit('m'):
        import matplotlib.pyplot as plt
        plt.plot(ts,Es,'-')
        plt.grid()
        plt.savefig('gravity'+str(ite)+'.png')

#frame = 0; time = 0; timebase = 0
#def fps():
#    frame = frame + 1
#    time = time()
#    if time - timebase > 1:
        

## GLUT animation in main function
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

if __name__ == '__main__':
    glutInit()
    glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGBA)
    glutInitWindowPosition(0,30)
    glutInitWindowSize(1280,720)
    glutCreateWindow('gravity')
    glutDisplayFunc(renderScene)

    glutIdleFunc(renderScene)

    glutReshapeFunc(changeSize)

    glutKeyboardFunc(exitKey)

    glEnable(GL_DEPTH_TEST)
    glutMainLoop()

#ts, xs, Es = integrate(F,0.0,x_init,10.0,h)

#x0=xs[0][len(ts)-1,:]
#x1=xs[1][len(ts)-1,:]
#print(v(x0),v(x1),p(x0,x1))

#print('initial energy', Es[0])
#print('final energy  ', Es[len(ts)-1])


## plot
#legend = []
#for i in range(len(xs)):
#    plt.plot(xs[i][:,0],xs[i][:,2],'-')
#    if range(len(xs)<6): legend.append('particle '+str(i))

#plt.legend(legend)

#plt.grid()
#plt.show()

#plt.plot(ts,Es,'-')

#plt.plot(ts,xs[1][:,0],'-',ts,xs[3][:,0],'-')
#plt.grid()
#plt.show()
