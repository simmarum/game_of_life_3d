import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *


def init_game():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    #  Enable depth test
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_NORMALIZE)
    glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)
    glEnable(GL_COLOR_MATERIAL)
    # Accept fragment if it closer to the camera than the former one
    glDepthFunc(GL_LESS)
