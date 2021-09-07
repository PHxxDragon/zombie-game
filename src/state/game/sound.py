import pygame

from src.common.resources_manager import *


class PlaySound:
    def __init__(self):
        pygame.mixer.init()
        self.hit = get_hit_sound()
        self.miss = get_miss_sound()

    def play_hit(self):
        self.hit.play()

    def play_miss(self):
        self.miss.play()