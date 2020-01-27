import pygame
import math

from OpenGL.GL import *
from OpenGL.GLU import *

from .cube import Cube
from .miscellaneous import show_axes


class GameLife():

    def __init__(self):
        self.c = Cube()
        self.fps = 60
        self.can_run = False

        self.pi = 3.1415
        self.ca_theta = self.pi/2
        self.ca_phi = self.pi/2
        self.angle_step = self.pi/10

        self.cr = 20.0

        self.cx = 0.0
        self.cy = 0.0
        self.cz = 20.0

        self.rotX = 0
        self.rotY = 0
        self.rotZ = 0

        pygame.key.set_repeat(200, 100)

    def set_fps(self, new_fps):
        self.can_run = True if new_fps > 0 else False
        self.fps = new_fps

    def process_key_press(self, events):
        tmp_cy_max = 0.75*self.cr
        tmp_old_ca_theta = self.ca_theta
        tmp_old_ca_phi = self.ca_phi
        tmp_old_cx = self.cx
        tmp_old_cy = self.cy
        tmp_old_cz = self.cz
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_q]:
                    self.cr += 1
                    if self.cr > 50:
                        self.cr = 50
                if event.key in [pygame.K_e]:
                    self.cr -= 1
                    if self.cr < 20:
                        self.cr = 20
                if event.key in [pygame.K_LEFT, pygame.K_a]:
                    self.ca_phi += self.angle_step
                    if self.ca_phi > 2*self.pi:
                        self.ca_phi -= 2*self.pi
                    if self.ca_phi < 0:
                        self.ca_phi += 2*self.pi
                if event.key in [pygame.K_RIGHT, pygame.K_d]:
                    self.ca_phi -= self.angle_step
                    if self.ca_phi > 2*self.pi:
                        self.ca_phi -= 2*self.pi
                    if self.ca_phi < 0:
                        self.ca_phi += 2*self.pi
                if event.key in [pygame.K_UP, pygame.K_w]:
                    self.ca_theta -= self.angle_step
                    if self.ca_theta > 0.75*self.pi:
                        self.ca_theta = 0.75*self.pi
                    if self.ca_theta < 0.25*self.pi:
                        self.ca_theta = 0.25*self.pi
                if event.key in [pygame.K_DOWN, pygame.K_s]:
                    self.ca_theta += self.angle_step
                    if self.ca_theta > 0.75*self.pi:
                        self.ca_theta = 0.75*self.pi
                    if self.ca_theta < 0.25*self.pi:
                        self.ca_theta = 0.25*self.pi
                self.cx = self.cr*math.sin(self.ca_theta)*math.cos(self.ca_phi)
                self.cz = self.cr*math.sin(self.ca_theta)*math.sin(self.ca_phi)
                self.cy = self.cr*math.cos(self.ca_theta)
                if abs(self.cy) > tmp_cy_max:
                    self.cx = tmp_old_cx
                    self.cy = tmp_old_cy
                    self.cz = tmp_old_cz

    def run(self):
        if not self.can_run:
            return

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        screen = pygame.display.Info()
        gluPerspective(45, (screen.current_w/screen.current_h), 0.1, 50.0)

        gluLookAt(self.cx, self.cy,  self.cz,
                  0, 0,  0,
                  0.0, 1.0,  0.0)

        glPushMatrix()
        self.c.draw((1, 0, 0), (0, 1, 0))
        self.c.draw((0, 0, 1), (1, 0, 0))
        glPopMatrix()

        show_axes(self.rotX, self.rotY, self.rotZ)
