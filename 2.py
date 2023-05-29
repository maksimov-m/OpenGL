from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glBegin(GL_TRIANGLES)
    glVertex3f(-0.5, -0.5, 0.0)
    glVertex3f(0.0, 0.5, 0.0)
    glVertex3f(0.5, -0.5, 0.0)
    glEnd()

    glutSwapBuffers()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)

    glutInitWindowSize(800, 600)
    glutCreateWindow('OpenGL lesson1')

    glutDisplayFunc(display)

    glutMainLoop()

main()
