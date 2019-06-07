from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import numpy as np

U = False; D = False; L = False; R = False
phi = np.pi; theta = np.pi/2; d_phi = 0; d_theta = 0
width = 0; height = 0; mx = 0; my = 0
x = -0.1; y = 0.1; dx = 0; dy = 0
vx = 10.0; vy = 0.0; vz = 0.0
dvx = 0; dvy = 0; dvz = 0
lx = -1.0; ly = 0.0; lz = 0.0
red = 1.0; green = 1.0; blue = 1.0

def changeSize(w,h):
    global width,height,vx,vy,vz,lx,ly,lz
    
    width = w; height = h

    if h == 0: h = 1
    ratio = w/h

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    glViewport(0,0,w,h)

    gluPerspective(45,ratio,0.1,1000)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(vy,vz,vx,vy+ly,vz+lz,vx+lx,0.0,1.0,0.0)

def move(phi,theta):
    global dvx,dvy,dvz
    dvx = np.sin(theta)*np.cos(phi)
    dvy = np.sin(theta)*np.sin(phi)
    dvz = np.cos(theta)

def stop(): global dvx,dvy,dvz; dvx = 0; dvy = 0; dvz = 0

def cameraMove(dt):
    global vx,vy,vz,lx,ly,lz,theta,phi
    lx = np.sin(theta)*np.cos(phi)
    ly = np.sin(theta)*np.sin(phi)
    lz = np.cos(theta)

    phi = phi + d_phi
    theta = theta + d_theta

    vx = vx + dvx*dt
    vy = vy + dvy*dt
    vz = vz + dvz*dt

    glLoadIdentity()
    gluLookAt(vy,vz,vx,vy+ly,vz+lz,vx+lx,0.0,1.0,0.0)

def renderScene():
    global x,y
    cameraMove(0.01)

    x = x+dx
    y = y+dy

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    glColor3f(red,green,blue)

    glBegin(GL_POLYGON)
    glVertex3f(x,y,0.0)
    glVertex3f(x+0.2,y,0.0)
    glVertex3f(x+0.2,y-0.2,0.0)
    glVertex3f(x,y-0.2,0.0)
    glEnd()

    glPopMatrix()
    glutSwapBuffers()

from OpenGL._bytes import as_8_bit

kk = as_8_bit

def pressKeys(key,x,y):
    global red,blue,green
    if key == kk('r'): red = 1.0; blue = 0.0; green = 0.0
    elif key == kk('b'): red = 0.0; blue = 1.0; green = 0.0
    elif key == kk('g'): red = 0.0; blue = 0.0; green = 1.0
    if key == kk('w'): move(phi,theta)
    if key == kk('s'): move(phi+np.pi,theta)
    if key == kk('a'): move(phi+np.pi/2,theta)
    if key == kk('d'): move(phi-np.pi/2,theta)
    if key == kk('\033'): sys.exit()
    else: return
    glutPostRedisplay()

def releaseKeys(key,x,y):
    if key == kk('w') or key == kk('s') or key == kk('a') or key == kk('d'): stop()

def pressSpecialKeys(key,x,y):
    global U,D,L,R,dx,dy
    if key == GLUT_KEY_UP: U = True; dy = 0.005
    if key == GLUT_KEY_DOWN: D = True; dy = -0.005
    if key == GLUT_KEY_LEFT: L = True; dx = -0.005
    if key == GLUT_KEY_RIGHT: R = True; dx = 0.005

def releaseSpecialKeys(key,x,y):
    global U,D,L,R,dx,dy
    if key == GLUT_KEY_UP:
        U = False
        if D == False: dy = 0
        else: dy = -0.005
    if key == GLUT_KEY_DOWN:
        D = False
        if U == False: dy = 0
        else: dy = 0.005
    if key == GLUT_KEY_LEFT:
        L = False
        if R == False: dx = 0
        else: dx = -0.005
    if key == GLUT_KEY_RIGHT:
        R = False
        if L == False: dx = 0
        else: dx = 0.005

def mouseMotion(x,y):
    global d_phi,d_theta,mx,my
    if (0 < x < width) and (0 < y < height):
        d_phi = (x - mx)*0.00015
        d_theta = (my - y)*0.00015

        mx = x; my = y

def mousePassiveMotion(x,y):
    global d_phi,d_theta,mx,my
    if (0 < x < width) and (0 < y < height):
        d_phi = 0.0; d_theta = 0.0
        mx = x; my = y

if __name__ == '__main__':
    glutInit()
    glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGBA)
    glutInitWindowPosition(100,100)
    glutInitWindowSize(640,480)
    glutCreateWindow('Rain Water')
    glutDisplayFunc(renderScene)

    glutIdleFunc(renderScene)

    glutReshapeFunc(changeSize)

    glutKeyboardFunc(pressKeys)
    glutKeyboardUpFunc(releaseKeys)
    glutSpecialFunc(pressSpecialKeys)
    glutSpecialUpFunc(releaseSpecialKeys)
    glutMotionFunc(mouseMotion)
    glutPassiveMotionFunc(mousePassiveMotion)

    glEnable(GL_DEPTH_TEST)
    glutMainLoop()
