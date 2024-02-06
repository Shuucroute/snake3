# modules/display_manager.py
import pygame
from snake_game_logic import SnakeGameLogic
from snake_game_display import SnakeGameDisplay

class DisplayManager:
    @staticmethod
    def render(game, surface):
        if game.GAME_OVER_FLAG:
            DisplayManager.display_game_over(game, surface)
        else:
            SnakeGameLogic.update(game, game.FPS_CONTROLLER)
            DisplayManager.display_game(game, surface)
        pygame.display.flip()

    @staticmethod
    def display_game(game, surface):
        surface.fill(game.BLACK)
        for pos in game.snake_body:
            pygame.draw.rect(surface, game.GREEN, pygame.Rect(pos[0], pos[1], 10, 10))

        pygame.draw.rect(surface, game.WHITE, pygame.Rect(game.food_pos[0], game.food_pos[1], 10, 10))
        SnakeGameDisplay.show_score(game, 1, game.WHITE, 'consolas', 20)

    @staticmethod
    def display_game_over(game, surface):
        my_font = pygame.font.SysFont('times new roman', 90)
        game_over_surface = my_font.render('YOU DIED', True, game.RED)
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (game.FRAME_SIZE_X / 2, game.FRAME_SIZE_Y / 4)
        surface.fill(game.BLACK)
        surface.blit(game_over_surface, game_over_rect)
        SnakeGameDisplay.show_score(game, 0, game.RED, 'times new roman', 20)
        game_over_text_surface = pygame.font.SysFont('times new roman', 30).render('Click to restart or QUIT', True, game.WHITE)
        game_over_text_rect = game_over_text_surface.get_rect()
        game_over_text_rect.midtop = (game.FRAME_SIZE_X / 2, game.FRAME_SIZE_Y / 1.5)
        surface.blit(game_over_text_surface, game_over_text_rect)