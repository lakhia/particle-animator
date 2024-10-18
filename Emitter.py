import random
import matplotlib.pyplot as plt

from Node import Node
from ParticleCollector import ParticleCollector


class Emitter(Node):
    def __init__(self, rate, angle_variation=1.0, par_angle_offset=0.0,
                 speed=65.0, speed_variation=35.0, symbol='diamond-tall',
                 color_scale='BrBG', **kwargs):
        super().__init__(**kwargs)
        self.rate = random.gauss(rate, rate*2)
        self.angle = random.uniform(0, angle_variation)
        self.par_angle_offset = par_angle_offset
        self.speed_min = speed - speed_variation
        self.speed_max = speed + speed_variation
        self.color_scale = color_scale
        self.color_map = plt.get_cmap(color_scale)
        self.symbol = symbol
        self.collector = ParticleCollector()
        self.angle_diff = 0.4
        self.dx = 0
        self.dy = 0

    def add_particle(self):
        #hypo = random.uniform(self.speed_min, self.speed_max) / 10
        #angle_dev = self.par_angle_offset + random.normalvariate(0, self.angle_variation)
        #angle = math.radians(self.angle + angle_dev)
        #vx = math.cos(angle) * hypo
        #vy = math.sin(angle) * hypo
        # if self.angle == 0 or self.angle == 180:
        #     self.dy = math.sin(self.life/20) / 130
        # else:
        #     self.dx = math.sin(self.life/20) / 130

        self.collector.add_particle(px=self.px+self.dx,
                                    py=self.py+self.dy,
                                    vx=self.vx, vy=self.vy,
                                    size=4, color=random.normalvariate(0, 0.5))

    def run(self, frame: int):
        super().run(frame)
        if self.rate >= 1:
            for _ in range(int(self.rate)):
                self.add_particle()
        else:
            if random.uniform(0, 1) < self.rate:
                self.add_particle()
