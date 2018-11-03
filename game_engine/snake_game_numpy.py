import numpy as np

from game_engine.base_game import BaseGame


class SnakeGameNumpy(BaseGame):

    def __init__(self, x, y, init_snake_length=3, snake_number=0.7, food_number=0.4, border_number=1,
                 score_increment=5):
        BaseGame.__init__(self)

        self.x = x
        self.y = y
        self.init_snake_length = init_snake_length
        self.border_number = border_number
        self.snake_number = snake_number
        self.food_number = food_number
        self.score_increment = score_increment

        self.nb_actions = 5
        self.score = 0
        self.game_is_over = False
        self.last_move = 2

        self.frame = self.__create_game_field(self.x, self.y, self.border_number)
        self.snake = self.__create_snake(self.x, self.y, self.init_snake_length)
        self.food = self.__spawn_food(self.x, self.y)

    def get_frame(self):
        """Method return array of how the current game board looks."""
        frame = self.__add_snake_to_frame(self.frame, self.snake, self.snake_number)
        return self.__add_food_to_frame(frame, self.food, self.food_number)

    def get_score(self):
        """Method returns the current score of the game."""
        return self.score

    def play(self, move):
        """Method takes move integer as a parameter and advances the game state using that move.
            Available moves:   3
                             2 4 0
                               1
        """
        if self.__move_changes_direction(self.last_move, move):
            self.snake = self.__move_and_grow_snake_when_needed(self.snake, self.food, move)
            self.last_move = move
        else:
            self.snake = self.__move_and_grow_snake_when_needed(self.snake, self.food, self.last_move)

        if self.__snake_is_on_food(self.snake, self.food):
            self.food = self.__spawn_food(self.x, self.y)
            self.score += self.score_increment

    def is_over(self):
        """Method returns boolean whether game is currently lost."""
        self.game_is_over = self.__snake_has_died(self.snake, self.x, self.y)
        return self.game_is_over

    def is_won(self):
        """Method returns boolean whether game is currently won."""
        pass

    def reset(self):
        """Method ends the current game and starts a new one."""
        self.score = 0
        self.game_is_over = False
        self.snake = self.__create_snake(self.x, self.y, self.init_snake_length)
        self.food = self.__spawn_food(self.x, self.y)

    @staticmethod
    def __create_game_field(x, y, border_number):
        game_field = np.ones((x, y))
        if border_number != 1:
            game_field.fill(border_number)

        game_field[1:-1, 1:-1] = 0
        return game_field

    @staticmethod
    def __add_food_to_frame(frame, food, food_number):
        new_frame = np.array(frame)
        new_frame[food[0], food[1]] = food_number
        return new_frame

    @staticmethod
    def __add_snake_to_frame(frame, snake, snake_number):
        new_frame = np.array(frame)

        for block in snake:
            new_frame[block[0], block[1]] = snake_number
        return new_frame

    @staticmethod
    def __create_snake(x, y, initial_snake_length):
        return np.array([[x//2 + i, y//2] for i in range(initial_snake_length)])

    @staticmethod
    def __move_changes_direction(previous_move, move):
        if move == 4:
            return False
        if previous_move == 0 and move == 2:
            return False
        if previous_move == 2 and move == 0:
            return False
        if previous_move == 1 and move == 3:
            return False
        if previous_move == 3 and move == 1:
            return False
        return True

    @staticmethod
    def __move_snake(snake, move, grow=False, snake_head=None):
        if snake_head is None:
            snake_head = SnakeGameNumpy.__get_snake_head_after_move(snake, move)

        if not grow:
            return np.concatenate((np.atleast_2d(snake_head), snake[0:-1, :]))
        else:
            return np.concatenate((np.atleast_2d(snake_head), snake))

    @staticmethod
    def __get_snake_head_after_move(snake, move):
        if move == 0:
            snake_head = [snake[0, 0] + 1, snake[0, 1]]
        elif move == 1:
            snake_head = [snake[0, 0], snake[0, 1] + 1]
        elif move == 2:
            snake_head = [snake[0, 0] - 1, snake[0, 1]]
        elif move == 3:
            snake_head = [snake[0, 0], snake[0, 1] - 1]
        else:
            raise Exception("Move argument must be between 0 and 3, was {}".format(move))
        return np.array(snake_head)

    @staticmethod
    def __move_and_grow_snake_when_needed(snake, food, move):
        snake_head_after_move = SnakeGameNumpy.__get_snake_head_after_move(snake, move)

        if np.array_equal(snake_head_after_move, food):
            return SnakeGameNumpy.__move_snake(snake, move, grow=True, snake_head=snake_head_after_move)
        else:
            return SnakeGameNumpy.__move_snake(snake, move, grow=False, snake_head=snake_head_after_move)

    @staticmethod
    def __snake_is_on_food(snake, food):
        return np.array_equal(snake[0, :], food)

    @staticmethod
    def __snake_has_died(snake, x, y):
        if snake.min() < 1:
            return True
        if snake[0, 0] > (x - 1):
            return True
        if snake[0, 1] > (y - 1):
            return True
        if np.unique(snake, axis=0, return_counts=True)[1].max() > 1:
            return True
        return False

    @staticmethod
    def __spawn_food(x, y):
        if x == y:
            return np.random.randint(low=1, high=(x - 1), size=(2))
        else:
            return np.array([np.random.randint(1, x - 1), np.random.randint(1,  y - 1)])
