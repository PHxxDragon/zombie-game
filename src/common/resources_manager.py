import os.path
import pygame as pg
import pygame.compat
import functools

PROJECT_DIR = os.path.abspath(os.path.join(__file__, "..", "..", ".."))
RESOURCE_DIR = os.path.join(PROJECT_DIR, "resources")

_DEFAULT_COLOR_KEY = -1
_BACKGROUND_SURFACE = None
_ZOMBIE_SURFACE = None
_SLIME_BACK = None
_SLIME_FRONT = None
_SLIME_RIGHT = None
_SLIME_LEFT = None
_SLIME_DEATH = None
_POINTER_SURFACE = None


def _load_image(name, alpha=False, color_key=None):
    file_path = os.path.join(RESOURCE_DIR, name)
    try:
        image = pg.image.load(file_path)
    except pg.error:
        print("Cannot load image: ", file_path)
        raise SystemExit(str(pg.compat.geterror()))
    if alpha:
        image = image.convert_alpha()
    else:
        image = image.convert()
        if color_key is not None:
            if color_key == _DEFAULT_COLOR_KEY:
                color_key = image.get_at((0, 0))
            image.set_colorkey(color_key, pg.RLEACCEL)
    return image


def _load_background():
    global _BACKGROUND_SURFACE

    image_name = "background.png"
    scale = 0.8

    image = _load_image(image_name)
    image = pg.transform.scale(image, (int(image.get_width() * scale), int(image.get_height() * scale)))

    _BACKGROUND_SURFACE = image


def _load_zombie():
    global _ZOMBIE_SURFACE
    image_name = "zombie.png"
    scale = 0.1

    image = _load_image(image_name, alpha=True)
    image = pg.transform.scale(image, (int(image.get_width() * scale), int(image.get_height() * scale)))

    _ZOMBIE_SURFACE = image


def _load_slime():
    global _SLIME_FRONT
    global _SLIME_BACK
    global _SLIME_RIGHT
    global _SLIME_DEATH
    global _SLIME_LEFT

    color_key = -1
    scale = 0.5

    slime_back_0000 = _load_image("slime/slime_back_0000.png", alpha=True)
    slime_back_0001 = _load_image("slime/slime_back_0001.png", alpha=True)
    slime_back_0002 = _load_image("slime/slime_back_0002.png", alpha=True)
    slime_back_0003 = _load_image("slime/slime_back_0003.png", alpha=True)

    slime_front_0000 = _load_image("slime/slime_front_0000.png", alpha=True)
    slime_front_0001 = _load_image("slime/slime_front_0001.png", alpha=True)
    slime_front_0002 = _load_image("slime/slime_front_0002.png", alpha=True)
    slime_front_0003 = _load_image("slime/slime_front_0003.png", alpha=True)

    slime_right_0000 = _load_image("slime/slime_right_0000.png", alpha=True)
    slime_right_0001 = _load_image("slime/slime_right_0001.png", alpha=True)
    slime_right_0002 = _load_image("slime/slime_right_0002.png", alpha=True)
    slime_right_0003 = _load_image("slime/slime_right_0003.png", alpha=True)

    slime_death_0000 = _load_image("slime/slime_death_0000.png", alpha=True)

    _SLIME_FRONT = [slime_front_0000, slime_front_0001, slime_front_0002, slime_front_0003]
    _SLIME_BACK = [slime_back_0000, slime_back_0001, slime_back_0002, slime_back_0003]
    _SLIME_RIGHT = [slime_right_0000, slime_right_0001, slime_right_0002, slime_right_0003]
    _SLIME_DEATH = [slime_death_0000]

    def scale_func(image):
        return pg.transform.scale(image, (int(image.get_width() * scale), int(image.get_height() * scale)))

    def flip_func(image):
        return pg.transform.flip(image, True, False)

    _SLIME_FRONT = list(map(scale_func, _SLIME_FRONT))
    _SLIME_BACK = list(map(scale_func, _SLIME_BACK))
    _SLIME_RIGHT = list(map(scale_func, _SLIME_RIGHT))
    _SLIME_DEATH = list(map(scale_func, _SLIME_DEATH))
    _SLIME_LEFT = list(map(flip_func, _SLIME_RIGHT))


def _load_pointer():
    global _POINTER_SURFACE
    image_name = "pointer.png"
    scale = 1
    image = _load_image(image_name, alpha=True)
    image = pg.transform.scale(image, (int(image.get_width() * scale), int(image.get_height() * scale)))
    _POINTER_SURFACE = image


def init_resources():
    _load_background()
    _load_zombie()
    _load_pointer()


def get_background_surface():
    global _BACKGROUND_SURFACE
    if _BACKGROUND_SURFACE is None:
        _load_background()
    return _BACKGROUND_SURFACE


def get_zombie_surface():
    global _ZOMBIE_SURFACE
    if _ZOMBIE_SURFACE is None:
        _load_zombie()
    return _ZOMBIE_SURFACE


def get_pointer_surface():
    global _POINTER_SURFACE
    if _POINTER_SURFACE is None:
        _load_pointer()
    return _POINTER_SURFACE


def get_slime_surfaces():
    if None in [_SLIME_FRONT, _SLIME_BACK, _SLIME_LEFT, _SLIME_RIGHT, _SLIME_DEATH]:
        _load_slime()
    return [_SLIME_FRONT, _SLIME_BACK, _SLIME_LEFT, _SLIME_RIGHT, _SLIME_DEATH]

