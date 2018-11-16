from keras.models import Sequential
from keras.layers import *
from keras.optimizers import *

from models.base_model import BaseModel


class InitialModel(BaseModel):

    def __init__(self, x=10, y=10, number_of_frames=4, number_of_actions=4,
                 init_snake_length=3, load_weights=True, border=1, snake=0.9, food=0.4):
        self.x = x
        self.y = y
        self.number_of_frames = number_of_frames
        self.number_of_actions = number_of_actions
        self.init_snake_length = init_snake_length
        self.border_number = border
        self.snake_number = snake
        self.food_number = food

        self.__build_model()
        self.__compile_model()

        if load_weights:
            self.__load_weights()

    def get_model(self):
        return self.model

    def __build_model(self):
        self.model = Sequential()
        self.model.add(Conv2D(16, (3, 3),
                              activation='relu',
                              input_shape=(self.number_of_frames, self.x, self.y),
                              data_format='channels_first'))
        self.model.add(Conv2D(32, (3, 3),
                              activation='relu'))
        self.model.add(Flatten())

        self.model.add(Dense(256, activation='relu'))
        self.model.add(Dense(self.number_of_actions))

    def __compile_model(self):
        self.model.compile(RMSprop(), 'MSE')

    def __load_weights(self):
        # TODO: Check if weights file exists
        self.model.load_weights('models/weights/initial_model/x{}y{}f{}a{}.dat'
                                .format(self.x, self.y, self.number_of_frames, self.number_of_actions))
