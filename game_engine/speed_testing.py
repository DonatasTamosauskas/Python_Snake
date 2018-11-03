from random import seed, randint
from timeit import timeit

from game_engine.snake_functions_old import Game
from game_engine.snake_game_numpy import SnakeGameNumpy


class SpeedTest:

    def __init__(self):
        x = 10
        y = 10
        init_snake_length = 3
        border_number = 1
        snake_number = 0.9
        food_number = 0.4

        self.old_game = Game(x, y, init_snake_length, snake_number, food_number, border_number)
        self.new_game = SnakeGameNumpy(x, y, init_snake_length, snake_number, food_number, border_number)

    @staticmethod
    def play_random_game(game_engine, max_move, set_seed=0):
        seed(set_seed)
        game_engine.reset()

        while not game_engine.is_over():
            game_engine.play(randint(0, max_move))

    @staticmethod
    def play_snake_functions_old(game):
        SpeedTest.play_random_game(game, 4)

    @staticmethod
    def play_snake_game_numpy(game):
        SpeedTest.play_random_game(game, 4)

    @staticmethod
    def snake_old_function_speed():
        return timeit(stmt="SpeedTest.play_random_game(game.old_game, 4)",
                      setup="from game_engine.speed_testing import SpeedTest; game = SpeedTest()",
                      number=10000)

    @staticmethod
    def snake_game_numpy_speed():
        return timeit(stmt="SpeedTest.play_random_game(game.new_game, 4)",
                      setup="from game_engine.speed_testing import SpeedTest; game = SpeedTest()",
                      number=10000)
