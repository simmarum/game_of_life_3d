import pygame
from .utils import drawText


def show_fps(fps_counter):
    screen = pygame.display.Info()
    drawText([0, screen.current_h, 1], str(int(fps_counter)), up=True)
