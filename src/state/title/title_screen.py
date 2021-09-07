import pygame as pg

from src.state.state_machine import State
from src.state.title.title import Title
from src.state.title.background import Background


class TitleScreen(State):
    def __init__(self):
        super().__init__()
        self.name = "TITLE"
        self.next_state_name = "GAME"
        self.title = Title()
        self.background = Background()

    def accept_events(self, events):
        for event in events:
            if event.type == pg.MOUSEBUTTONDOWN:
                self.done = True
    
    def update(self, now, mouse_pos):
        pass

    def draw(self, surface, interpolate):
        surface.blit(self.background.image, self.background.rect)
        surface.blit(self.title.image, self.title.rect)
