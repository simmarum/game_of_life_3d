import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

from src.init import init_game
from src.event import check_events
from src.game_life import GameLife
from src.miscellaneous import show_fps


def main():
    init_game()
    game = GameLife()

    clock = pygame.time.Clock()
    while True:
        glLoadIdentity()
        clock.tick()
        game.set_fps(clock.get_fps())
        check_events(game)

        game.run()

        show_fps(game.fps)
        pygame.display.flip()
        pygame.time.wait(3)


if __name__ == '__main__':
    main()
