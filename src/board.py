import numpy as np
from OpenGL.GL import *
# from OpenGL.GLU import *
from .cube import Cube
import scipy.ndimage.filters
import pygame
from .utils import drawText


class Board():
    def __init__(self, n, to_born, to_live):
        self.n = n
        self.all_cells = n*n*n
        self.to_born = to_born
        self.to_live = to_live

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

    def _sum_small_cubes(self, a):
        a = a.reshape((3, 3, 3))
        a[1, 1, 1] = 0
        s = np.sum(a)
        return s

    def calculate_next_step(self):
        print("Step")
        small_cubes = scipy.ndimage.filters.generic_filter(
            self.board,
            self._sum_small_cubes,
            size=3,
            mode='constant'
        )

        candidate_born = np.isin(small_cubes, self.to_born)
        candidate_live = np.isin(small_cubes, self.to_live)

        arr_born = np.bitwise_and(self.board == 0, candidate_born)
        arr_live = np.bitwise_and(self.board == 1, candidate_live)

        self.board = np.bitwise_or(arr_born, arr_live).astype(int)

    def draw(self, pos3d):
        if pos3d is None:
            tmp_center = int(self.n/2)
            pos3d = (tmp_center, tmp_center, tmp_center)

        glPushMatrix()
        tmp_idx_cells = np.where(self.board == 1)
        tmp_idx_cells_pos = list(
            zip(
                tmp_idx_cells[0],
                tmp_idx_cells[1],
                tmp_idx_cells[2]
            )
        )
        tmp_live_cell = len(tmp_idx_cells_pos)
        for x, y, z in tmp_idx_cells_pos:
            self.c.draw(
                (
                    x-pos3d[0],
                    y-pos3d[1],
                    z-pos3d[2],
                ),
                (0, 0, 1)
            )

        glPopMatrix()
        screen = pygame.display.Info()
        drawText([100, 0, 0], str("{}/{}".format(tmp_live_cell, self.all_cells)))
