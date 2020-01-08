
from OpenGL.GL import *
from OpenGL.GLU import *

colors = (
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (1, 1, 0),
    (1, 1, 1),
    (0, 1, 1),
    (1, 0, 1),
    (0, 0, 0),
    (0, 0, 1),
    (1, 0, 0),
    (1, 1, 1),
    (0, 1, 1),
)


class Cube():

    verticies = (
        (1, -1, -1),
        (1, 1, -1),
        (-1, 1, -1),
        (-1, -1, -1),
        (1, -1, 1),
        (1, 1, 1),
        (-1, -1, 1),
        (-1, 1, 1)
    )

    edges = (
        (0, 1),
        (0, 3),
        (0, 4),
        (2, 1),
        (2, 3),
        (2, 7),
        (6, 3),
        (6, 4),
        (6, 7),
        (5, 1),
        (5, 4),
        (5, 7)
    )

    surfaces = (
        (0, 1, 2, 3),
        (3, 2, 7, 6),
        (6, 7, 5, 4),
        (4, 5, 1, 0),
        (1, 5, 7, 2),
        (4, 0, 3, 6)
    )

    def __init__(self):
        pass

    def draw(self, color):
        glBegin(GL_QUADS)
        for idx, surface in enumerate(self.surfaces):
            for vertex in surface:
                glColor3fv(colors[idx])
                glVertex3fv(self.verticies[vertex])
        glEnd()

        glBegin(GL_LINES)
        for edge in self.edges:
            for vertex in edge:
                glColor3fv((0, 0, 0))
                glVertex3fv(self.verticies[vertex])
        glEnd()
