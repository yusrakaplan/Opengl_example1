from math import cos, sin, pi
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
from math import radians, cos, sin
import OpenGL.GLUT as glut
x, y = -0.5, -0.0

radius = -0.25
angle=0
angle_increment = 2.0


def init():
    glClearColor(0.7, 0.7, 1.0, 1.0)
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)


def draw_ball():
    # yuvarlağı çizmek için 360 derece döngü yaparız
    glBegin(GL_POLYGON)
    for i in range(360):
        angle = radians(i)
        glVertex2f(x + cos(angle)*0.05, y + sin(angle)*0.05)
    glEnd()

def drawOrbit():
    glColor3f(0.0, 0.0, 1.0)  # rengi mavi yap
    glBegin(GL_LINES)  # line çizmeye başla
    for i in range(38):
        angle = i * 5
        x = 0.5 * cos(angle * pi / 180)  # x koordinatı hesaplanır
        y = 0.5 * sin(angle * pi / 180)  # y hesaplanır
        glVertex2f(x, y)  #
    glEnd()
    glColor3f(0.0, 0.0, 1.0)
    glPointSize(3.0)
    glBegin(GL_POINTS)
    for angle in range(0, 180, 8):
        x = 0.5 * cos(angle * pi / 180)
        y = 0.5 * sin(angle * pi / 180)
        glVertex2f(x, y)
    glEnd()

def mouse(button, state, x, y):

    global angle_increment,angle
    if button == glut.GLUT_LEFT_BUTTON and state == glut.GLUT_DOWN:
        angle-=angle_increment
    elif button == glut.GLUT_RIGHT_BUTTON and state == glut.GLUT_DOWN:
        angle+=angle_increment
    glut.glutPostRedisplay()

def display():
    global x,y,angle,radius
    glClear(GL_COLOR_BUFFER_BIT)  # clear screen
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)  # set orthographic projection
    drawOrbit()  # draw orbit
    glColor3f(1.0, 0, 0.0)
    x = radius * cos(radians(angle))
    y = radius * sin(radians(angle))
    glTranslatef(x, y, 0.0)
    draw_ball()
    glutSwapBuffers()  # swap buffers




def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(50, 50)
    glutCreateWindow(b"yorunge")
    glutDisplayFunc(display)
    glMatrixMode(GL_PROJECTION)
    glOrtho(-1, 1, -1, 1, -1, 1)
    glut.glutMouseFunc(mouse)
    init()
    glutMainLoop()


main()

