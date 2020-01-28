import numpy as np
from OpenGL.GL import *
# from OpenGL.GLU import *
from .cube import Cube


class Board():
    def __init__(self, n):
        self.n = n
        self.board = np.zeros((n, n, n))
        self.c = Cube()

    def _populate_board_corner(self):
        self.board[0, 0, 0] = 1
        self.board[0, 1, 0] = 1
        self.board[0, 0, 1] = 1
        self.board[0, 1, 1] = 1

        self.board[1, 0, 0] = 1
        self.board[1, 1, 0] = 1
        self.board[1, 0, 1] = 1
        self.board[1, 1, 1] = 1

        self.board[2, 0, 0] = 1
        self.board[2, 1, 0] = 1
        self.board[2, 0, 1] = 1
        self.board[2, 1, 1] = 1

    def populate_board(self, mode):
        if mode == 'corner':
            self._populate_board_corner()

    def calculate_next_step(self):
        pass

    def draw(self, pos3d):
        if pos3d is None:
            tmp_center = int(self.n/2)
            pos3d = (tmp_center, tmp_center, tmp_center)

        glPushMatrix()
        for x in range(self.n):
            for y in range(self.n):
                for z in range(self.n):
                    if self.board[x, y, z] == 1:
                        self.c.draw(
                            (
                                x-pos3d[0],
                                y-pos3d[1],
                                z-pos3d[2],
                            ),
                            (0, 0, 1)
                        )
        glPopMatrix()
