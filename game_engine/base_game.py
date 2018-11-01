class BaseGame:

    def __init__(self):
        nb_actions = 4

    def get_frame(self):
        """Method return array of how the current game board looks."""
        pass

    def get_score(self):
        """Method returns the current score of the game."""
        pass

    def play(self, move):
        """Method takes move integer as a parameter and advances the game state using that move."""
        pass

    def is_over(self):
        """Method returns boolean whether game is currently lost."""
        pass

    def is_won(self):
        """Method returns boolean whether game is currently lost."""
        pass

    def reset(self):
        """Method ends the current game and starts a new one."""
        pass
