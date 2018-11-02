from random import randint
from numpy import array


class Game:

    def __init__(self, x, y, init_snake_length=3, snake_number=0.7, food_number=0.4, border_number=1):
        self.x = x
        self.y = y
        self.init_snake_length = init_snake_length
        self.border_number = border_number
        self.snake_number = snake_number
        self.food_number = food_number
        self.score = 0
        self.game_over = False

        self.game_matrix = [[0 for _ in range(self.y)] for _ in range(self.x)]
        self.snake = Snake(x, y, init_snake_length)
        self.food = Food(x, y)

    def draw_game_field(self):
        for i in range(self.x):
            for j in range(self.y):
                if i == 0:
                    self.game_matrix[0][j] = self.border_number
                elif j == 0 or j == self.y - 1:
                    self.game_matrix[i][j] = self.border_number
                elif i == self.x - 1:
                    self.game_matrix[i][j] = self.border_number
                else:
                    self.game_matrix[i][j] = 0

    def zero_matrix(self):
        for i in range(self.x):
            for j in range(self.y):
                self.game_matrix[i][j] = 0

    def reset(self):
        self.draw_game_field()
        self.score = 0
        self.game_over = False
        self.snake.spawn()
        self.food.spawn()
        self.snake.draw(self.game_matrix, self.snake_number)
        self.food.draw(self.game_matrix, self.food_number)
        self.snake.dir = 0
        # print("Game resetting")

    def game_frame(self, direction=0, print_mode=1):
        if abs(self.snake.dir - direction) != 2:
            self.snake.dir = direction
        self.snake.move()

        if self.snake.hit_border() or self.snake.hit_snake():
            self.reset()

        self.draw_game_field()
        self.food.draw(self.game_matrix, self.food_number)
        self.snake.draw(self.game_matrix, self.snake_number)

        if print_mode == 2:
            self.print_game()
        elif print_mode == 1:
            self.print_score()

        self.score = self.snake.eats(self.score, self.food)
        return self.game_matrix

    def print_score(self):
        print("Score is: " + str(self.score) + "\n")

    def print_game(self):
        for i in range(self.x):
            print(self.game_matrix[i])
        self.print_score()

    # Adaptation functions for agent.py

    def get_frame(self):
        return array(self.game_matrix)

    def play(self, direction):
        if abs(self.snake.dir - direction) != 2:
            self.snake.dir = direction
        self.snake.move()

        if self.snake.hit_border() or self.snake.hit_snake():
            self.game_over = True
            self.score = -1
            # print("Game over")
        else:
            self.score = self.snake.eats(self.score, self.food)

        self.draw_game_field()
        self.food.draw(self.game_matrix, self.food_number)
        self.snake.draw(self.game_matrix, self.snake_number)

    def get_score(self):
        return self.score

    def is_over(self):
        return self.game_over

    def is_won(self):
        if self.snake.length > self.init_snake_length:
            return True
        else:
            return False

    @property
    def nb_actions(self):
        return 4


class Food:

    def __init__(self, x, y, spawn_x=0, spawn_y=0):
        self.x = x
        self.y = y
        if spawn_x != 0 and spawn_y != 0:
            self.pos = [spawn_x, spawn_y]
        else:
            self.spawn()

    def spawn(self):
        self.pos = [randint(1, self.x - 2), randint(1, self.y - 2)]

    def draw(self, matrix, food_numb):
        matrix[self.pos[0]][self.pos[1]] = food_numb


class Snake:

    def __init__(self, x, y, init_length):
        self.x = x
        self.y = y
        self.init_length = init_length
        self.length = init_length
        self.dir = 0
        """
          3
        2   0
          1
        """
        self.pos = [[0 for _ in range(2)] for _ in range(20)]

        self.spawn()

    def spawn(self):
        self.length = self.init_length
        for i in range(self.init_length):
            self.pos[i][0] = self.x // 2
            self.pos[i][1] = self.y // 2 + i

    def move(self):
        for i in range(self.length, 0, -1):
            self.pos[i][0] = self.pos[i - 1][0]
            self.pos[i][1] = self.pos[i - 1][1]

        if self.dir == 0:
            self.pos[0][0] += 1
        elif self.dir == 1:
            self.pos[0][1] += 1
        elif self.dir == 2:
            self.pos[0][0] -= 1
        elif self.dir == 3:
            self.pos[0][1] -= 1

    def eats(self, input_score, input_food):
        if self.pos[0] == input_food.pos:
            self.length += 1
            input_food.spawn()
            return input_score + 5
        else:
            return input_score

    def draw(self, matrix, snake_numb):
        for i in range(self.length):
            matrix[self.pos[i][0]][self.pos[i][1]] = snake_numb

    def hit_border(self):
        if self.pos[0][0] == 0 or self.pos[0][1] == 0 or self.pos[0][0] == self.y - 1 or self.pos[0][1] == self.x - 1:
            return True
        else:
            return False

    def hit_snake(self):
        for i in range(1, self.length):
            if self.pos[0] == self.pos[i]:
                return True
        return False

