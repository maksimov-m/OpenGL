from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import time
import sys


def display():
    while True:
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glPushMatrix()
        color = [1.0, 0., 0., 1.]
        glMaterialfv(GL_FRONT, GL_DIFFUSE, color)
        glutSolidSphere(2, 20, 20)
        glTranslate(1, 1, 1)
        color = [1.0, 1.0, 0., 1.]
        glMaterialfv(GL_FRONT, GL_DIFFUSE, color)
        glutSolidCube(2)
        glPopMatrix()
        glRotate(1, 0, 1, 1)
        glutSwapBuffers()

        time.sleep(0.01)


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(700,700)
    glutCreateWindow(b'Cube')
    glClearColor(0.,0.,0.,1.)

    #shader
    glShadeModel(GL_SMOOTH)
    glEnable(GL_CULL_FACE)
    glEnable(GL_DEPTH_TEST)

    #light
    glEnable(GL_LIGHTING)
    lightZeroPosition = [10., 4., 10., 1.]
    glLightfv(GL_LIGHT0, GL_POSITION, lightZeroPosition)
    glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.1)
    glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.05)
    glEnable(GL_LIGHT0)


    glutDisplayFunc(display)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(50.,1.,1.,40.)
    glMatrixMode(GL_MODELVIEW)
    gluLookAt(0,0,10,
              0,0,0,
              0,1,0)
    glPushMatrix()
    glutMainLoop()
    return
main()
