import pygame as pg
from src.common.resources_manager import *


class Background(pg.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.image = get_background_surface()
        self.rect = self.image.get_rect(topleft=(0, 0))

    def update(self, *args):
        pass
