# modules/game.py
import pygame
import random

class Game:
    def __init__(self):
        pygame.init()
        self.FRAME_SIZE_X = 720
        self.FRAME_SIZE_Y = 480
        self.GAME_WINDOW = pygame.display.set_mode((self.FRAME_SIZE_X, self.FRAME_SIZE_Y))
        self.is_game_over = False
        self.snake_pos = [100, 50]
        self.snake_body = [[100, 50], [100 - 10, 50], [100 - (2 * 10), 50]]
        self.food_pos = [random.randrange(1, (self.FRAME_SIZE_X // 10)) * 10,
                         random.randrange(1, (self.FRAME_SIZE_Y // 10)) * 10]
        self.food_spawn = True
        self.direction = 'RIGHT'
        self.change_to = self.direction
        self.score = 0
        self.DIFFICULTY = 15
        self.GAME_OVER_FLAG = False
        self.BLACK = (0, 0, 0)
        self.GREEN = (0, 255, 0)
        self.WHITE = (255, 255, 255)
        self.RED = (255, 0, 0)
        self.FPS_CONTROLLER = pygame.time.Clock()
        self.RESTART_BUTTON_RECT = pygame.Rect(self.FRAME_SIZE_X / 4, self.FRAME_SIZE_Y / 1.5, 150, 50)
        self.QUIT_BUTTON_RECT = pygame.Rect(self.FRAME_SIZE_X / 2 + 20, self.FRAME_SIZE_Y / 1.5, 150, 50)

    def is_ended(self):
        return self.is_game_over