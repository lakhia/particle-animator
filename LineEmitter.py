import random

from Emitter import Emitter
from ParticleCollector import ParticleCollector


class LineEmitter(Emitter):
    def __init__(self, angle_variation=1.0, symbol='circle',
                 speed=65.0, speed_variation=35.0,
                 color_scale='greens', **kwargs):
        super().__init__(**kwargs, collector=ParticleCollector())
        self.angle_variation = angle_variation
        self.speed_min = speed - speed_variation
        self.speed_max = speed + speed_variation
        self.color_scale = color_scale
        self.symbol = symbol
        self.angle_diff = 0.4
        self.dx = 0
        self.dy = 0

    def add_particle(self):
        dx = random.uniform(-0.0006, 0.0006)
        dy = random.uniform(-0.0006, 0.0006)
        cl = random.normalvariate(0, 0.4)
        self.collector.add_particle(px=self.px, py=self.py,
                                    vx=dx, vy=dy,
                                    size=4, color=cl)

    def run(self, frame: int):
        super().run(frame)
        self.collector.sz = 150 / (50 + self.collector.life)

