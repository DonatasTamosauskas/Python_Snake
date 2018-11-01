from keras.models import Sequential
from keras.layers import *
from keras.optimizers import *

from snake_functions import Game
from graphics.pygame_graphics import PygameGraphics
from qlearning.agent import Agent

x = 10
y = 10
init_snake_length = 3
border_number = 1
snake_number = 0.9
food_number = 0.4


def human_play(game, graphics):
    direction = 0
    while True:
        graphics.display_frame(game.game_matrix)
        # Controls are WASD
        direction = graphics.read_input(direction)
        game.play(direction)


def main():

    model = Sequential()
    model.add(Conv2D(16, (3, 3), activation='relu', input_shape=(4, x, y),
                     data_format='channels_first'))
    model.add(Conv2D(32, (3, 3), activation='relu'))
    model.add(Flatten())
    model.add(Dense(256, activation='relu'))
    model.add(Dense(4))  # actions number
    model.compile(RMSprop(), 'MSE')

    model.load_weights('ModelWeights/my_weights.dat')

    game = Game(x, y, init_snake_length, snake_number, food_number, border_number)
    agent = Agent(model=model, memory_size=-1, nb_frames=4)

    # Modes: display - True, training - False.
    if True:
        graphics = PygameGraphics(x, y, snake_number, food_number, border_number, framerate=15)
        agent.play_graphics(game, graphics, nb_epoch=10, nb_loops=60)
    else:
        agent.train(game, batch_size=64, nb_epoch=10, gamma=0.8, observe=0, checkpoint=None)


if __name__ == "__main__":
    main()
