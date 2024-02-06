# modules/snake_game_display.py
import pygame
from event_manager import EventManager
from snake_game_display import SnakeGameDisplay


class SnakeGameLogic:
    @staticmethod
    def update(game, clock):
        # Logique du jeu
        EventManager.handle_events(game)

        if not game.GAME_OVER_FLAG:
            if game.change_to == 'UP' and game.direction != 'DOWN':
                game.direction = 'UP'
            if game.change_to == 'DOWN' and game.direction != 'UP':
                game.direction = 'DOWN'
            if game.change_to == 'LEFT' and game.direction != 'RIGHT':
                game.direction = 'LEFT'
            if game.change_to == 'RIGHT' and game.direction != 'LEFT':
                game.direction = 'RIGHT'

        if game.direction == 'UP':
            game.snake_pos[1] -= 10
        if game.direction == 'DOWN':
            game.snake_pos[1] += 10
        if game.direction == 'LEFT':
            game.snake_pos[0] -= 10
        if game.direction == 'RIGHT':
            game.snake_pos[0] += 10

        game.snake_body.insert(0, list(game.snake_pos))
        if game.snake_pos[0] == game.food_pos[0] and game.snake_pos[1] == game.food_pos[1]:
            game.score += 1
            game.food_spawn = False
        else:
            game.snake_body.pop()

        if not game.food_spawn:
            game.food_pos = [random.randrange(1, (game.FRAME_SIZE_X // 10)) * 10,
                             random.randrange(1, (game.FRAME_SIZE_Y // 10)) * 10]
        game.food_spawn = True

        game.GAME_WINDOW.fill(game.BLACK)
        for pos in game.snake_body:
            pygame.draw.rect(game.GAME_WINDOW, game.GREEN, pygame.Rect(pos[0], pos[1], 10, 10))

        pygame.draw.rect(game.GAME_WINDOW, game.WHITE, pygame.Rect(game.food_pos[0], game.food_pos[1], 10, 10))

        if game.snake_pos[0] < 0 or game.snake_pos[0] > game.FRAME_SIZE_X-10:
            SnakeGameLogic.game_over(game)
        if game.snake_pos[1] < 0 or game.snake_pos[1] > game.FRAME_SIZE_Y-10:
            SnakeGameLogic.game_over(game)
        for block in game.snake_body[1:]:
            if game.snake_pos[0] == block[0] and game.snake_pos[1] == block[1]:
                SnakeGameLogic.game_over(game)

        SnakeGameDisplay.show_score(game, 1, game.WHITE, 'consolas', 20)
        pygame.display.update()
        clock.tick(game.DIFFICULTY)

    @staticmethod
    def game_over(game):
        game.GAME_OVER_FLAG = True

    @staticmethod
    def reset_game(game):
        game.GAME_OVER_FLAG = False
        game.snake_pos = [100, 50]
        game.snake_body = [[100, 50], [100 - 10, 50], [100 - (2 * 10), 50]]
        game.food_pos = [random.randrange(1, (game.FRAME_SIZE_X // 10)) * 10,
                         random.randrange(1, (game.FRAME_SIZE_Y // 10)) * 10]
        game.food_spawn = True
        game.direction = 'RIGHT'
        game.change_to = game.direction
        game.score = 0
