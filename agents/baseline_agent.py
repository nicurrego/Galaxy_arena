import numpy as np
from core.actions import Action

class BaselineAgent:
    def __init__(self):
        pass

    def act(self, obs):
        return np.random.choice([Action.UP, Action.DOWN, Action.LEFT, Action.RIGHT, Action.STAY, Action.SHOOT])