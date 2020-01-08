import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

from src.init import init_game
from src.event import check_events
from src.game_life import GameLife


def main():
    init_game()
    game = GameLife()
    while True:
        check_events()
        game.run()

        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == '__main__':
    main()
