from game_engine.snake_functions_old import Game
from graphics.pygame_graphics import PygameGraphics
from qlearning.agent import Agent
from models.initial_model import InitialModel

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

    initial_model_architecture = InitialModel()
    model = initial_model_architecture.get_model()

    game = Game(x, y, init_snake_length, snake_number, food_number, border_number)
    agent = Agent(model=model, memory_size=-1, nb_frames=4)

    # Modes: display - True, training - False.
    if True:
        graphics = PygameGraphics(x, y, snake_number, food_number, border_number, framerate=15)
        agent.play_graphics(game, graphics, nb_epoch=10, nb_loops=60)
    else:
        # TODO: Add dynamic weights file naming and saving
        agent.train(game, batch_size=64, nb_epoch=10, gamma=0.8, observe=0, checkpoint=None)


if __name__ == "__main__":
    main()
