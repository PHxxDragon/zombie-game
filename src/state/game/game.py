from typing import Dict

from src.state.state_machine import State
from src.common.resources_manager import *

from src.state.game.pointer import Pointer
from src.state.game.score import Score
from src.state.game.slime import SlimeSpawner
from src.state.game.background import Background
from src.state.game.music import Music
from src.state.game.sound import PlaySound


class Game(State):
    def __init__(self):
        super().__init__()
        self.name = "GAME"
        self.group_all = pg.sprite.Group()
        self.UI = pg.sprite.Group()
        self.background = Background(self)
        self.pointer = Pointer(self)
        self.score = Score(self)
        self.group_all.add(self.background)
        self.UI.add(self.score, self.pointer)
        self.slime_spawner = SlimeSpawner(self)
        self.music = Music()
        self.sound = PlaySound()

    def startup(self, now, to_persist: Dict):
        pg.mouse.set_visible(False)
        self.music.start()

    def accept_events(self, events):
        for event in events:
            if event.type == pg.MOUSEBUTTONDOWN:
                self.slime_spawner.kill_slime(event.pos)

    def update(self, now, mouse_pos):
        self.group_all.update(now, mouse_pos)
        self.slime_spawner.update(now, mouse_pos)
        self.UI.update(now, mouse_pos)

    def draw(self, surface: pg.Surface, interpolate):
        self.group_all.draw(surface)
        self.UI.draw(surface)
