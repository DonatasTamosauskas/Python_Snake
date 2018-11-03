from random import seed, randint
from timeit import timeit

import matplotlib.pyplot as plt

from game_engine.snake_functions_old import Game
from game_engine.snake_game_numpy import SnakeGameNumpy


class SpeedTest:

    def __init__(self):
        self.x = 15
        self.y = 15
        self.init_snake_length = 3
        self.border_number = 1
        self.snake_number = 0.9
        self.food_number = 0.4
        seed(0)

    def plot_differences(self, max_x=50, step=2, loop_times=1000):
        old_results, new_results = self.compare_different_game_engines(max_x=max_x, step=step, loop_times=loop_times)

        plt.xticks(range(len(old_results.keys())), old_results.keys())
        plt.plot(old_results.values(), label="Lists game engine")
        plt.plot(new_results.values(), label="Numpy game engine")

        plt.xlabel("Size of game board in pixels")
        plt.ylabel("Time (s) to play {} games".format(loop_times))
        plt.title("Old snake game vs new engine speed")
        plt.legend()
        plt.show()

    def compare_different_game_engines(self, max_x=50, step=2, loop_times=1000):
        snake_functions_old_speed = {}
        snake_game_numpy_speed = {}

        for x in range(5, max_x, step):
            snake_functions_old_speed[x] = self.snake_old_function_speed(x, x, loop_times)
            snake_game_numpy_speed[x] = self.snake_game_numpy_speed(x, x, loop_times)

        return snake_functions_old_speed, snake_game_numpy_speed

    def get_functions_old_game(self, x, y):
        return Game(x, y, self.init_snake_length, self.snake_number, self.food_number, self.border_number)

    def get_snake_game_numpy_game(self, x, y):
        return SnakeGameNumpy(x, y, self.init_snake_length, self.snake_number, self.food_number, self.border_number)

    @staticmethod
    def play_random_game(game_engine, max_move, print_score=False):
        game_engine.reset()

        while not game_engine.is_over():
            game_engine.play(randint(0, max_move))

        if print_score: print("Game score: {}".format(game_engine.get_score()))

    @staticmethod
    def snake_old_function_speed(x, y, loop_times=1000):
        return timeit(stmt="SpeedTest.play_random_game(game, 3)",
                      setup="from game_engine.speed_testing import SpeedTest; game = SpeedTest().get_functions_old_game"
                      + "({}, {})".format(x, y),
                      number=loop_times)

    @staticmethod
    def snake_game_numpy_speed(x, y, loop_times=1000):
        return timeit(stmt="SpeedTest.play_random_game(game, 3)",
                      setup="from game_engine.speed_testing import SpeedTest; game = SpeedTest().get_snake_game_numpy_game"
                            + "({}, {})".format(x, y),
                      number=loop_times)
