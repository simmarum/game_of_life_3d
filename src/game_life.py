
from OpenGL.GL import *
from OpenGL.GLU import *

from .cube import Cube


class GameLife():

    def __init__(self):
        self.c = Cube()

    def run(self):
        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        self.c.draw()
