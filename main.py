from snake_functions import Game

x = 10
y = 10
init_snake_length = 3
border_number = 2
snake_number = 1
food_number = 8


def main():
    global game
    game = Game(x, y, init_snake_length, snake_number, food_number, border_number)

    for i in range(10):
        game.game_frame(print_mode=2)


if __name__ == "__main__":
    main()
