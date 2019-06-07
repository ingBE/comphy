from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

angle = 0.0

def renderScene():
    global angle
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    glRotatef(angle,0.0,1.0,0.0)

    glBegin(GL_TRIANGLES)
    glVertex3f(-0.5, -0.5, 0.0)
    glVertex3f(0.5, 0.0, 0.0)
    glVertex3f(0.0, 0.5, 0.0)
    glEnd()

    glPopMatrix()
    glutSwapBuffers()

    angle = angle + 0.5

def changeSize(w,h):
    if h == 0: h = 1
    ratio = w / h
    glViewport(0,0,w,h)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()


    gluPerspective(45,ratio,1,1000)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0.0,0.0,5.0,0.0,0.0,-1.0,0.0,1.0,0.0)

glutInit()
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGBA)
glutInitWindowPosition(100,100)
glutInitWindowSize(640,480)
glutCreateWindow('Rain Water')


glutDisplayFunc(renderScene)

glutIdleFunc(renderScene)

glutReshapeFunc(changeSize)

glEnable(GL_DEPTH_TEST)
glutMainLoop()
