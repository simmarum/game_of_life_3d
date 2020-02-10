
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from .objloader import *


class Cube():

    def __init__(self):
        tmp_path = os.path.join(os.path.dirname(__file__), 'models')
        self.obj = OBJ(os.path.join(tmp_path, "cube.obj"), swapyz=True)

    def draw(self, position, color):
        glPushMatrix()
        glTranslatef(*position)
        glCallList(self.obj.gl_list)
        glPopMatrix()
