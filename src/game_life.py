
from OpenGL.GL import *
from OpenGL.GLU import *

from .cube import Cube
from .miscellaneous import show_axes


class GameLife():

    def __init__(self):
        self.c = Cube()
        self.fps = 60
        self.can_run = False

    def set_fps(self, new_fps):
        self.can_run = True if new_fps > 0 else False
        self.fps = new_fps

    def run(self):
        if not self.can_run:
            return

        rotX = 60/self.fps
        rotY = 60/self.fps
        rotZ = 0
        glRotatef(rotX, 1, 0, 0)
        glRotatef(rotY, 0, 1, 0)
        self.c.draw((1, 0, 0), (0, 1, 0))
        self.c.draw((0, 0, 1), (1, 0, 0))

        show_axes(rotX, rotY, rotZ)
