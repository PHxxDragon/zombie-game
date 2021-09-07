from main_control import MainControl
from state.game.game import Game
from state.title.title_screen import TitleScreen
import pygame as pg


def main():
    if not pg.font:
        raise SystemExit(str("Font disabled"))
    if not pg.mixer:
        raise SystemExit(str("Sound disabled"))

    control = MainControl()
    title_state = TitleScreen()
    game_state = Game()
    state_dict = {
                title_state.name: title_state,
                game_state.name: game_state}
    control.state_machine.setup_state(state_dict, title_state.name)
    control.main()
    pg.quit()
