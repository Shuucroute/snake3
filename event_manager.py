# modules/event_manager.py
import pygame
import sys
from pygame.locals import MOUSEBUTTONDOWN
from snake_game_logic import SnakeGameLogic

class EventManager:
    @staticmethod
    def handle_events(game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                EventManager.handle_keydown(event, game)
            elif event.type == MOUSEBUTTONDOWN:
                EventManager.handle_mouse_click(event, game)

    @staticmethod
    def handle_keydown(event, game):
        if event.key == pygame.K_UP or event.key == ord('z'):
            game.change_to = 'UP'
        if event.key == pygame.K_DOWN or event.key == ord('s'):
            game.change_to = 'DOWN'
        if event.key == pygame.K_LEFT or event.key == ord('q'):
            game.change_to = 'LEFT'
        if event.key == pygame.K_RIGHT or event.key == ord('d'):
            game.change_to = 'RIGHT'
        if event.key == pygame.K_ESCAPE:
            pygame.event.post(pygame.event.Event(pygame.QUIT))

    @staticmethod
    def handle_mouse_click(event, game):
        if event.button == 1:
            if game.RESTART_BUTTON_RECT.collidepoint(event.pos):
                SnakeGameLogic.reset_game(game)
            elif game.QUIT_BUTTON_RECT.collidepoint(event.pos):
                pygame.quit()
                sys.exit()
