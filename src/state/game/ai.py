import random
from src.state.game.slime import *


class BaseAI:
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)
    STOP = (0, 0)

    def __init__(self, game):
        self.game = game
        self.speed = 1
        self.direction = BaseAI.STOP

    def get_direction(self):
        return self.direction

    def get_vector_direction(self):
        return self.speed * self.direction[0], self.speed * self.direction[1]


class OneDirectionAI(BaseAI):
    def __init__(self, game, speed=2, direction=None):
        super().__init__(game)
        self.direction = direction
        self.speed = speed
        if self.direction is None:
            self.direction = random.choice([BaseAI.UP, BaseAI.DOWN, BaseAI.LEFT, BaseAI.RIGHT, BaseAI.STOP])
