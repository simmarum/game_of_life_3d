
from OpenGL.GL import *
from OpenGL.GLU import *

from .cube import Cube


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

        glRotatef(60/self.fps, 180/self.fps, 60/self.fps, 60/self.fps)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        self.c.draw()
