import pygame

from OpenGL.GL import *
from OpenGL.GLU import *


def drawText(position, textString, right=False, up=False, ):
    font = pygame.font.Font(None, 32)
    textSurface = font.render(textString, True, (255, 255, 255, 255), (0, 0, 0, 255))
    textData = pygame.image.tostring(textSurface, "RGBA", True)
    if right:
        position[0] = position[0] - textSurface.get_height()
    if up:
        position[1] = position[1] - textSurface.get_width()
    glWindowPos3d(*position)
    glDrawPixels(textSurface.get_width(), textSurface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, textData)
