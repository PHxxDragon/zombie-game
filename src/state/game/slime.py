import pygame as pg

from src.common.config import *
from src.common.resources_manager import *
from src.state.game.ai import *
from src.state.game.animation import *


class Slime(pg.sprite.Sprite):
    WALKING = 1
    DYING = 2

    def __init__(self, game, init_pos=(0, 0), spawn_time=1000, ai=None):
        super().__init__()
        self.game = game
        self.animations = None
        self.image = None
        self._init_animations()
        self.rect = self.image.get_rect(center=init_pos)
        self.state = Slime.WALKING
        self.direction = None
        self.life_span = int(spawn_time / DELTA_TIME)
        self.ai = ai
        self._init_ai()

    def _init_ai(self):
        if self.ai is None:
            ai = BaseAI(self.game)
            self.ai = ai

    def _init_animations(self):
        [front_images, back_images, left_images, right_images,
         death_images] = get_slime_surfaces()
        self.animations = {
            BaseAI.DOWN: BaseAnimation(self.game, front_images),
            BaseAI.UP: BaseAnimation(self.game, back_images),
            BaseAI.LEFT: BaseAnimation(self.game, left_images),
            BaseAI.RIGHT: BaseAnimation(self.game, right_images),
            BaseAI.STOP: BaseAnimation(self.game, front_images),
            Slime.DYING: BaseAnimation(self.game, death_images, loops=4),
        }
        self.image: pg.surface.Surface = front_images[0]

    def _change_state(self, new_state):
        self.state = new_state

    def check_and_kill(self, mouse_pos):
        if self.state != Slime.DYING and self.rect.collidepoint(mouse_pos):
            self._change_state(Slime.DYING)
            self.game.score.increase_score(1)
            self.game.sound.play_hit()
            return True

    def set_pos(self, pos):
        self.rect.center = pos

    def update(self, now, *args):
        self.life_span -= 1
        if self.state == Slime.DYING:
            if self.animations[Slime.DYING].done:
                self.kill()
            self.image = self.animations[Slime.DYING].get_next_frame(now)
        else:
            self.rect.move_ip(self.ai.get_vector_direction())

            if self.direction != self.ai.get_direction():
                self.direction = self.ai.get_direction()
                self.animations[self.direction].reset()
            self.image = self.animations[self.ai.get_direction()].get_next_frame(now)

            if self.life_span <= 0:
                self.kill()


class SlimeSpawner:
    def __init__(self, game):
        self.game = game
        self.loops_between_spawn = int(SPAWN_DURATION / DELTA_TIME)
        self.remain_loops = self.loops_between_spawn
        self.group_zombie = pg.sprite.Group()

    def kill_slime(self, mouse_pos):
        killed = False
        for zombie in self.group_zombie.sprites():
            killed = killed or zombie.check_and_kill(mouse_pos)
        if not killed:
            self.game.sound.play_miss()
            self.game.score.increase_score(-1)

    def update(self, now, *args):
        self.remain_loops -= 1
        if self.remain_loops <= 0 and len(self.group_zombie) < MAX_SPAWN:
            self.remain_loops = self.loops_between_spawn
            slime = Slime(self.game, init_pos=random.choice(SPAWN_POSITIONS), ai=self._choose_random_ai(), spawn_time=SPAWN_TIME)
            slime.add(self.game.group_all, self.group_zombie)

    def _choose_random_ai(self):
        speed = random.choice(SPEEDS)
        ai_type = random.choice([1, 2, 3, 4, 5])
        if ai_type == 1:
            return BaseAI(self.game)
        elif ai_type in [2, 3, 4, 5]:
            return OneDirectionAI(self.game, speed)
