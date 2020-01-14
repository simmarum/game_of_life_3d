import pygame


def check_events(game):
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    game.process_key_press(events)
