import numpy as np
from core.actions import Action

class BaselineAgent:
    def __init__(self):
        pass

    def act(self, obs):
        # Example: always shoot, otherwise move up/down randomly
        if np.random.rand() < 0.3:
            return Action.SHOOT
        return np.random.choice([Action.UP, Action.DOWN, Action.LEFT, Action.RIGHT])