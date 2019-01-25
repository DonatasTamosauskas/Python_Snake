class BaseModel:

    def __init__(self, x, y, number_of_actions, number_of_frames, load_weights=True):
        """
        Every model uses the following parameters for model creation:
        :param x: The number of pixels in the game boards x axis
        :param y: The number of pixels in the game boards y axis
        :param number_of_frames: The number of frames a model is given for prediction
        :param number_of_actions: Number of actions possible to make in the game
        :param load_weights: Boolean should the weights be loaded from a previous run
        """
        self.x = x
        self.y = y
        self.number_of_actions = number_of_actions
        self.number_of_frames = number_of_frames
        self.load_weights = load_weights
        pass

    def get_model(self):
        """
        Returns the created model
        :return: Created Keras model
        """
        pass

    def get_weights_filename(self, appendix=''):
        filename = 'x{}y{}f{}a{}{}.dat'\
            .format(self.x, self.y, self.number_of_frames, self.number_of_actions, appendix)
        return filename
