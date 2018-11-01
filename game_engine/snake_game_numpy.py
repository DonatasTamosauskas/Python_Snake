import numpy as np

from game_engine.base_game import BaseGame


class SnakeGameNumpy(BaseGame):

    def __init__(self, x, y, init_snake_length=3, snake_number=0.7, food_number=0.4, border_number=1):
        BaseGame.__init__(self)

        self.x = x
        self.y = y
        self.init_snake_length = init_snake_length
        self.border_number = border_number
        self.snake_number = snake_number
        self.food_number = food_number

        self.nb_actions = 5
        self.score = 0
        self.game_over = False
        self.frame = self.__create_game_field(self.x, self.y, self.border_number)
        self.snake = self.__create_snake(self.x, self.y, self.init_snake_length)

    def get_frame(self):
        """Method return array of how the current game board looks."""
        return self.frame

    def get_score(self):
        """Method returns the current score of the game."""
        return self.score

    def play(self, move):
        """Method takes move integer as a parameter and advances the game state using that move."""
        pass

    def is_over(self):
        """Method returns boolean whether game is currently lost."""
        return self.game_over

    def is_won(self):
        """Method returns boolean whether game is currently won."""
        pass

    def reset(self):
        """Method ends the current game and starts a new one."""
        self.score = 0
        self.game_over = False

    @staticmethod
    def __create_game_field(x, y, border_number):
        game_field = np.ones((x, y))
        if border_number != 1:
            game_field.fill(border_number)

        game_field[1:-1, 1:-1] = 0
        return game_field

    @staticmethod
    def __create_snake(x, y, initial_snake_length):
        return np.array([[x//2, y//2 + i] for i in range(initial_snake_length)])

    @staticmethod
    def __add_snake_to_frame(frame, snake):
        pass

