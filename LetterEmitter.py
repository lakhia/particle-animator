import random

from Emitter import Emitter
from Letter import Letter


class LetterEmitter(Emitter):
    def __init__(self, rate=0, **kwargs):
        super().__init__(rate, **kwargs)
        self.letters = []

    def add_particle(self):
        dx = random.uniform(self.speed_min, self.speed_max)
        dy = random.uniform(self.speed_min, self.speed_max)
        cl = random.uniform(0, 1)
        self.letters.append(Letter(px=self.px, py=self.py,
                                   vx=dx, vy=dy,
                                   sz=0.04, cl=cl))

    def run(self, frame: int):
        super().run(frame)
        for letter in self.letters:
            letter.run(frame)

    def draw(self, ctx, frame, factor):
        ctx.select_font_face("Courier New")
        ctx.set_font_size(0.06)
        for letter in self.letters:
            if letter.letter:
                rgba = self.color_map(letter.cl)
                ctx.set_source_rgba(*rgba)
                ctx.move_to(letter.px, letter.py)
                ctx.show_text(letter.letter)
