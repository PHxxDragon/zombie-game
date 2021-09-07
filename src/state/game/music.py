from pygame import mixer

from src.common.resources_manager import *


class Music:
    def __init__(self):
        mixer.init()
        mixer.music.load(get_music_filename())

    def start(self):
        mixer.music.play(loops=-1)

