import math
import random

from NodeCollector import NodeCollector, Node


class Emitter(Node):
    def __init__(self, angle, rate=1.0, angle_variation=10.0,
                 speed=65.0, speed_variation=35.0, **kwargs):
        super().__init__(**kwargs)
        self.angle = angle
        self.rate = rate
        self.angle_variation = angle_variation
        self.speed_min = speed - speed_variation
        self.speed_max = speed + speed_variation
        self.collector = NodeCollector()

    def run(self):
        super().run()
        self.angle += 3
        for _ in range(int(self.rate)):
            hypo = random.uniform(self.speed_min, self.speed_max)
            angle_dev = random.normalvariate(0, self.angle_variation)
            angle = math.radians(self.angle + angle_dev)
            vx = math.cos(angle) / hypo
            vy = math.sin(angle) / hypo
            sz = random.uniform(1, 4)
            self.collector.add_node(px=self.px, py=self.py, vx=vx, vy=vy,
                                    size=sz, color=angle_dev / 30)

        self.collector.run()
