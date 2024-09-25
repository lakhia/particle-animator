import math
import random
from ParticleCollector import ParticleCollector, Node


class Emitter(Node):
    def __init__(self, rate, angle_variation=1.0, par_angle_offset=0.0,
                 speed=65.0, speed_variation=35.0, color_scale='inferno',
                 **kwargs):
        super().__init__(**kwargs)
        self.rate = rate
        self.angle_variation = angle_variation
        self.par_angle_offset = par_angle_offset
        self.speed_min = speed - speed_variation
        self.speed_max = speed + speed_variation
        self.color_scale = color_scale
        self.collector = ParticleCollector()
        if self.angle == 90 or self.angle == -90:
            self.angle_diff = 40
        else:
            self.angle_diff = 50

    def add_particle(self):
        hypo = random.uniform(self.speed_min, self.speed_max) / 1000
        angle_dev = self.par_angle_offset + random.normalvariate(0, self.angle_variation)
        angle = math.radians(self.angle + angle_dev)
        vx = math.cos(angle) * hypo
        vy = math.sin(angle) * hypo
        sz = random.uniform(3, 11)
        self.collector.add_particle(px=self.px,
                                    py=self.py,
                                    vx=vx, vy=vy,
                                    size=sz, color=random.normalvariate(0, 0.03))

    def run(self, frame: int):
        if frame == 90:
            self.angle -= self.angle_diff
        if frame == 130:
            self.angle += self.angle_diff
        super().run(frame)
        if self.rate >= 1:
            for _ in range(int(self.rate)):
                self.add_particle()
        else:
            if random.uniform(0, 1) < self.rate:
                self.add_particle()

        self.collector.run(frame)
