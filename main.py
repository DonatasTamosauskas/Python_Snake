import sys

from game_engine.snake_game_numpy import SnakeGameNumpy
from qlearning.tensorlayer_agent import TensorlayerAgent

x = 10
y = 10
init_snake_length = 3
border_number = 1
snake_number = 0.9
food_number = 0.4
score_increment = 1


def human_play(game, graphics):
    direction = 0
    while True:
        graphics.display_frame(game.get_frame())
        # Controls are WASD
        direction = graphics.read_input(direction)
        print(direction)
        game.play(direction)


def get_script_mode():
    for i, arg in enumerate((sys.argv[i] for i in range(len(sys.argv)))):
        if arg == "--mode":
            if sys.argv[i + 1] in ["test", "display", "train"]:
                return sys.argv[i + 1]
            else:
                print("No such mode: {}".format(sys.argv[i + 1]))
                raise ValueError("No such mode: {}".format(sys.argv[i + 1]))


def main():
    mode = get_script_mode()

    if mode == "train":
        pass
    elif mode == "test":
        pass
    else:
        from graphics.pygame_graphics import PygameGraphics

    game = SnakeGameNumpy(x, y, init_snake_length, snake_number, food_number, border_number, score_increment=score_increment)       
    tensorlayer_agent = TensorlayerAgent(game, action_space=4)

    if mode == "train":
        # TODO: Add dynamic weights file naming and saving
        # agent.train(game, batch_size=64, nb_epoch=20, gamma=0.8, observe=0, checkpoint=None)
        tensorlayer_agent.train()

    elif mode == "test":
        tensorlayer_agent.test()

    else:
        raise NotImplementedError()
        # graphics = PygameGraphics(x, y, snake_number, food_number, border_number, framerate=15)
        # agent.play_graphics(game, graphics, nb_epoch=10, nb_loops=60)

if __name__ == "__main__":
    main()
