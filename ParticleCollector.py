from dataclasses import dataclass
import math
import numpy as np


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


class ParticleCollector:
    def __init__(self):
        self.px = np.array([])
        self.py = np.array([])
        self.vx = np.array([])
        self.vy = np.array([])
        self.sz = np.array([])
        self.cl = np.array([])
        self.life = np.array([])

    def add_particle(self, px, py, vx, vy, size, color=0.2):
        self.px = np.append(self.px, px)
        self.py = np.append(self.py, py)
        self.vx = np.append(self.vx, vx)
        self.vy = np.append(self.vy, vy)
        self.sz = np.append(self.sz, size)
        self.cl = np.append(self.cl, color)
        self.life = np.append(self.life, 1)

    def run(self, frame: int):
        ln_diff = len(self.px) - 600
        if ln_diff > 0:
            self.px = self.px[ln_diff:]
            self.py = self.py[ln_diff:]
            self.vx = self.vx[ln_diff:]
            self.vy = self.vy[ln_diff:]
            self.sz = self.sz[ln_diff:]
            self.cl = self.cl[ln_diff:]
            self.life = self.life[ln_diff:]

        self.life += 1
        self.sz = 200 * (3 + 12 * np.abs(np.cos(0.15 * self.life))) / (200 + self.life)
        move_node_particles(self)

    def reflect(self):
        s = np.where(self.px > 1, -1, 1)
        s = s * np.where(self.px < 0, -1, 1)
        self.vx = self.vx * s

        s = np.where(self.py > 1, -1, 1)
        s = s * np.where(self.py < 0, -1, 1)
        self.vy = self.vy * s
