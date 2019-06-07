from OpenGL.GL import *
from OpenGL.GLUT import *

def MyDisplay():
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_POLYGON)

    glVertex3f(-0.5, -0.5, 0.0)
    glVertex3f(0.5, -0.5, 0.0)
    glVertex3f(0.5, 0.5, 0.0)
    glVertex3f(-0.5, 0.0, 0.0)

    glEnd()
    glFlush()

glutInit()
glutCreateWindow('OpenGL Drawing Example')
glutDisplayFunc(MyDisplay)
glutMainLoop()
