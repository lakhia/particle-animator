from dataclasses import dataclass
import math


def move_node_particles(node):
    node.px = node.px + node.vx
    node.py = node.py + node.vy


@dataclass
class Node:
    """Class for keeping track of a node"""
    px: float
    py: float
    vx: float = 0.0
    vy: float = 0.0
    sz: float = 4
    cl: float = 0.2
    ax: float = 0.0
    ay: float = 0.0
    angle: float = 0.0
    thrust: float = 0.0
    life: int = 0

    def run(self, frame: int):
        if self.thrust:
            angle = math.radians(self.angle)
            self.px += math.cos(angle) * self.thrust
            self.py += math.sin(angle) * self.thrust
        self.life += 1
        move_node_particles(self)

    def reflect(self):
        # TODO: reflection in thrust mode is hacky
        if self.px > 1 or self.px < 0:
            if self.thrust:
                self.px = 1 - math.fabs(self.px)
            else:
                self.vx = self.vx * -1
        if self.py > 1 or self.py < 0:
            if self.thrust:
                self.py = 1 - math.fabs(self.py)
            else:
                self.vy = self.vy * -1

