
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


class Cube():

    def __init__(self):
        pass

    def draw(self, position, color):
        glPushMatrix()
        glTranslatef(*position)
        glColor3f(*color)
        glutSolidCube(1)
        glPopMatrix()
