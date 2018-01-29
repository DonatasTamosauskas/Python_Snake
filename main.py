from snake_functions import Game
from graphics_functions import Graphics

x = 10
y = 10
init_snake_length = 3
border_number = 2
snake_number = 1
food_number = 8


def main():
    global game
    game = Game(x, y, init_snake_length, snake_number, food_number, border_number)
    graphics = Graphics(x, y, snake_number, food_number, border_number)
    direction = 0

    while True:  # for i in range(10):
        graphics.display_frame(game.game_matrix)
        # Controls are WASD
        direction = graphics.read_input(direction)
        game.game_frame(direction, print_mode=1)


if __name__ == "__main__":
    main()
