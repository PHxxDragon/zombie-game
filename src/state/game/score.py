import pygame as pg
from src.common.config import *


class Score(pg.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.score = 0
        self._update_score()

    def _update_score(self):
        font = pg.font.Font(None, 60)
        self.image = font.render("Score: " + str(self.score), 1, (230, 9, 9))
        self.rect = self.image.get_rect(bottomright=(SCREEN_WIDTH - 10, SCREEN_HEIGHT - 5))

    def increase_score(self, increment):
        if self.score + increment >= 0:
            self.score += increment
            self._update_score()

    def update(self, *args):
        pass
