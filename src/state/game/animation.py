class BaseAnimation:
    def __init__(self, game, frames, fps=24, loops=-1):
        self.game = game
        self.fps = fps
        self.frame = 0
        self.loops = loops
        self.loop_count = 0
        self.frames = frames
        self.time = None
        self.done = False

    def reset(self):
        self.frame = 0
        self.loop_count = 0
        self.done = False
        self.time = None

    def get_next_frame(self, now):
        if not self.time:
            self.time = now
        if now - self.time > 1000.0 / self.fps:
            self.frame = (self.frame + 1) % len(self.frames)
            if self.frame == 0:
                self.loop_count += 1
                if self.loops != -1 and self.loop_count >= self.loops:
                    self.done = True
                    self.frame = (self.frame - 1) % len(self.frames)
            self.time = now
        return self.frames[self.frame]
