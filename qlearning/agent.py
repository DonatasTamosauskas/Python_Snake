# Most of the code taken from https://github.com/farizrahman4u/qlearning4k

from qlearning.memory import ExperienceReplay
import numpy as np


class Agent:

    def __init__(self, model, memory=None, memory_size=1000, nb_frames=None):
        assert len(model.output_shape) == 2, "Model's output shape should be (nb_samples, nb_actions)."
        if memory:
            self.memory = memory
        else:
            self.memory = ExperienceReplay(memory_size)
        if not nb_frames and not model.input_shape[1]:
            raise Exception("Missing argument : nb_frames not provided")
        elif not nb_frames:
            nb_frames = model.input_shape[1]
        elif model.input_shape[1] and nb_frames and model.input_shape[1] != nb_frames:
            raise Exception("Dimension mismatch : time dimension of model should be equal to nb_frames.")
        self.model = model
        self.nb_frames = nb_frames
        self.frames = None

    @property
    def memory_size(self):
        return self.memory.memory_size

    @memory_size.setter
    def memory_size(self, value):
        self.memory.memory_size = value

    def reset_memory(self):
        self.exp_replay.reset_memory()

    def check_game_compatibility(self, game):
        # game.get_frame() needs to be in snake_functions -----------------
        game_output_shape = (1, None) + game.get_frame().shape

        if len(game_output_shape) != len(self.model.input_shape):
            raise Exception('Dimension mismatch. Input shape of the model should be compatible with the game.')
        else:
            for i in range(len(self.model.input_shape)):
                if self.model.input_shape[i] and game_output_shape[i] and self.model.input_shape[i] != \
                        game_output_shape[i]:
                    raise Exception('Dimension mismatch. Input shape of the model should be compatible with the game.')
        if len(self.model.output_shape) != 2 or self.model.output_shape[1] != game.nb_actions:
            raise Exception('Output shape of model should be (nb_samples, nb_actions).')

    def get_game_data(self, game):
        frame = game.get_frame()
        if self.frames is None:
            self.frames = [frame] * self.nb_frames
        else:
            # as far as I understand this adds the new frame to self.frames array
            self.frames.append(frame)
            # and this deletes the oldest frame from the array
            self.frames.pop(0)
        return np.expand_dims(self.frames, 0)

    def clear_frames(self):
        self.frames = None

    def train(self, game, nb_epoch=1000, batch_size=50, gamma=0.9, epsilon=[1., .1], epsilon_rate=0.5,
              reset_memory=False, observe=0, checkpoint=None, nb_loops=100):
        # checks game compatibility by calling game.get_frame() and comparing to model.input_shape
        self.check_game_compatibility(game)

        if type(epsilon) in {tuple, list}:
            delta = ((epsilon[0] - epsilon[1]) / (nb_epoch * epsilon_rate))
            final_epsilon = epsilon[1]
            epsilon = epsilon[0]
        else:
            final_epsilon = epsilon

        model = self.model
        nb_actions = model.output_shape[-1]
        win_count = 0

        for epoch in range(nb_epoch):
            loss = 0.
            # another call to game object, need to analyze
            game.reset()
            # frames array is deleted
            self.clear_frames()

            if reset_memory:
                self.reset_memory()
            game_over = False

            # S stands for the current game state, and get_game_data returns self.frames array as np array
            S = self.get_game_data(game)
            loop_protect = 0

            while not game_over:
                # I assume this is the algorithm for exploration vs exploitation decision
                if np.random.random() < epsilon or epoch < observe:  # still no clue what observe does
                    a = int(np.random.randint(game.nb_actions))
                    # print("The action: {} was random.".format(a))
                else:
                    # model.predict gets model output q for given input S
                    q = model.predict(S)
                    # q[0] is array of all possible actions, and argmax function returns the one with the
                    # highest value, I believe
                    a = int(np.argmax(q[0]))
                    # print("The action: {}".format(a))
                r_previous = game.get_score()
                game.play(a)
                r = game.get_score()

                if r == r_previous:
                    loop_protect += 1
                else:
                    loop_protect = 0

                # this is the new state after action a (S')
                S_prime = self.get_game_data(game)
                # one more game specific function to check if game is over
                game_over = game.is_over()
                if not game_over and loop_protect >= nb_loops:
                    game_over = True

                # something with Experience replay probably
                transition = [S, a, r, S_prime, game_over]
                self.memory.remember(*transition)

                # S = S'
                S = S_prime

                if epoch >= observe:  # what is observe?
                    batch = self.memory.get_batch(model=model, batch_size=batch_size, gamma=gamma)
                    if batch:
                        inputs, targets = batch
                        loss += float(model.train_on_batch(inputs, targets))
                if checkpoint and ((epoch + 1 - observe) % checkpoint == 0 or epoch + 1 == nb_epoch):
                    model.save_weights('my_weights.dat')

            # another call to game object
            if game.is_won():
                win_count += 1
            if epsilon > final_epsilon and epoch >= observe:
                epsilon -= delta
            print("Epoch {:03d}/{:03d} | Loss {:.4f} | Epsilon {:.2f} | Win count {}".format(epoch + 1, nb_epoch, loss,
                                                                                             epsilon, win_count))

    def play_graphics(self, game, graphics, nb_epoch=10, nb_loops=50):
        model = self.model
        win_count = 0

        for epoch in range(nb_epoch):
            game.reset()
            self.clear_frames()
            game_over = False
            # S stands for the current game state, and get_game_data returns self.frames array as np array
            S = self.get_game_data(game)
            loop_protect = 0

            while not game_over and loop_protect < nb_loops:
                q = model.predict(S)
                a = int(np.argmax(q[0]))
                print("The action: {}".format(a))
                graphics.display_frame(game.get_frame())
                r = game.get_score()
                game.play(a)
                r1 = game.get_score()
                if r == r1:
                    loop_protect += 1
                else:
                    loop_protect = 0
                # this is the new state after action a (S')
                S = self.get_game_data(game)
                game_over = game.is_over()

            if game.is_won():
                win_count += 1
            print("Epoch {:03d}/{:03d} | Win count {}".format(epoch + 1, nb_epoch, win_count))

