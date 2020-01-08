
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


class Cube():

    def __init__(self):
        pass

    def draw(self, position, color):
        glColor3f(*color)
        glPushMatrix()
        glTranslatef(*position)
        glutSolidCube(1)
        glPopMatrix()
