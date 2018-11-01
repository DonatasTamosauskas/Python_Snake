from random import seed, randint
from timeit import timeit

from game_engine.snake_functions_old import Game


class SpeedTest:

    @staticmethod
    def play_random_game(game_engine, max_move, set_seed=0):
        seed(set_seed)
        game_engine.reset()

        while not game_engine.is_over():
            game_engine.play(randint(0, max_move))

    @staticmethod
    def play_snake_functions_old():
        x = 10
        y = 10
        init_snake_length = 3
        border_number = 1
        snake_number = 0.9
        food_number = 0.4

        game = Game(x, y, init_snake_length, snake_number, food_number, border_number)
        SpeedTest.play_random_game(game, 4)

    @staticmethod
    def snake_old_function_speed():
        return timeit(stmt="SpeedTest.play_snake_functions_old()",
                      setup="from game_engine.speed_testing import SpeedTest")
