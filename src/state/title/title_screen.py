from src.state.state_machine import State


class TitleScreen(State):
    def __init__(self):
        super().__init__()
        self.name = "TITLE"
        self.done = True
        self.next_state_name = "GAME"

    def accept_events(self, events):
        pass
    
    def update(self, now, mouse_pos):
        pass

    def draw(self, surface, interpolate):
        pass
