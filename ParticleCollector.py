import numpy as np

from Node import move_node_particles


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
        ln_diff = len(self.px) - 130
        if ln_diff > 0:
            self.px = self.px[ln_diff:]
            self.py = self.py[ln_diff:]
            self.vx = self.vx[ln_diff:]
            self.vy = self.vy[ln_diff:]
            self.sz = self.sz[ln_diff:]
            self.cl = self.cl[ln_diff:]
            self.life = self.life[ln_diff:]

        self.life += 1
        move_node_particles(self)
        self.vx /= 1.02
        self.vy /= 1.02

    def reflect(self):
        s = np.where(self.px > 1, -1, 1)
        s = s * np.where(self.px < 0, -1, 1)
        self.vx = self.vx * s

        s = np.where(self.py > 1, -1, 1)
        s = s * np.where(self.py < 0, -1, 1)
        self.vy = self.vy * s
