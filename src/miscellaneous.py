import pygame

from OpenGL.GL import *
from OpenGL.GLU import *

from .utils import drawText


def show_fps(fps_counter):
    screen = pygame.display.Info()
    drawText([0, screen.current_h, 1], str(int(fps_counter)), up=True)


def show_axes(rotX, rotY, rotZ, length_axis=100):
    # save previous matrix
    glPushMatrix()
    glRotatef(rotX, 1.0, 0.0, 0.0)
    glRotatef(rotY, 0.0, 1.0, 0.0)
    glRotatef(rotZ, 0.0, 0.0, 1.0)
    # move the axes to the screen corner
    glTranslatef(0.0, 0.0, 0.0)
    # draw our axes
    glBegin(GL_LINES)
    # draw line for x axis
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(length_axis, 0.0, 0.0)
    # draw line for y axis
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, length_axis, 0.0)
    # draw line for Z axis
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, length_axis)
    glEnd()
    # load the previous matrix
    glPopMatrix()
    # apply rotations
