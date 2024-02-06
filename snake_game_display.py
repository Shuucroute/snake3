# modules/display_manager.py
import pygame
from snake_game_logic import SnakeGameLogic

class SnakeGameDisplay:
    @staticmethod
    def show_score(game, choice, color, font, size):
        score_font = pygame.font.SysFont(font, size)
        score_surface = score_font.render('Score : ' + str(game.score), True, color)
        score_rect = score_surface.get_rect()
        if choice == 1:
            score_rect.midtop = (game.FRAME_SIZE_X / 10, 15)
        else:
            score_rect.midtop = (game.FRAME_SIZE_X / 2, game.FRAME_SIZE_Y / 1.25)
        game.GAME_WINDOW.blit(score_surface, score_rect)