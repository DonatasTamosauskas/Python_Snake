from game_engine.snake_functions_old import Game
from game_engine.snake_game_numpy import SnakeGameNumpy
from graphics.pygame_graphics import PygameGraphics

x = 10
y = 10
init_snake_length = 3
border_number = 1
snake_number = 0.9
food_number = 0.4


def read_keyboard():
    keypress = input()
    if keypress == 'w':
        return 3
    elif keypress == 'd':
        return 0
    elif keypress == 's':
        return 1
    elif keypress == 'a':
        return 2


def human_play(game, graphics):
    direction = 0
    while not game.is_over():
        graphics.display_frame(game.get_frame())
        # Controls are WASD
        direction = graphics.read_input(direction)
        # direction = read_keyboard()
        game.play(direction)


if __name__ == "__main__":
    # print(SpeedTest.snake_old_function_speed())
    snake_numpy = SnakeGameNumpy(x, y, init_snake_length, snake_number, food_number, border_number)
    snake_old = Game(x, y, init_snake_length, snake_number, food_number, border_number)
    graphics = PygameGraphics(x, y, snake_number, food_number, border_number, framerate=5)

    human_play(snake_numpy, graphics)
