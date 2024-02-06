# main.py
import pygame
import sys
from game import Game
from event_manager import EventManager
from display_manager import DisplayManager

def main():
    game = Game()

    while not game.is_ended():
        EventManager.handle_events(game)
        DisplayManager.render(game, game.GAME_WINDOW)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()