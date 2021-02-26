from utils.const import WHITE_REWARD


class State:
    def __init__(self, reward=WHITE_REWARD):
        self.reward = reward
        self.is_wall = False

    def __repr__(self):
        if self.is_wall:
            return 'W'.format(self.reward)
        return '{}'.format(self.reward)

    def __str__(self):
        return self.__repr__()
