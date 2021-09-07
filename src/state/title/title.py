import pygame as pg
from src.common.config import *


class Title(pg.sprite.Sprite):
    def __init__(self):
        font = pg.font.Font(None, 40)
        self.image = font.render("Press your mouse button to start", 1, (255, 255, 255))
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH/2, 4*SCREEN_HEIGHT/5))
