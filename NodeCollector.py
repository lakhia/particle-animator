from dataclasses import dataclass
import numpy as np


def move_nodes(node):
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
    r: float = 0.0

    def run(self):
        move_nodes(self)


class NodeCollector:
    def __init__(self):
        self.px = np.array([])
        self.py = np.array([])
        self.vx = np.array([])
        self.vy = np.array([])
        self.sz = np.array([])
        self.cl = np.array([])
        self.ax = np.array([])
        self.ay = np.array([])
        self.r = np.array([])

    def add_nodes(self, *nodes):
        for node in nodes:
            self.px = np.append(self.px, node.px)
            self.py = np.append(self.py, node.py)
            self.vx = np.append(self.vx, node.vx)
            self.vy = np.append(self.vy, node.vy)
            self.sz = np.append(self.sz, node.sz)
            self.cl = np.append(self.cl, node.cl)
            self.ax = np.append(self.ax, node.ax)
            self.ay = np.append(self.ay, node.ay)
            self.r = np.append(self.r, node.r)

    def add_node(self, px, py, vx, vy, size=4, color=0.2,
                 ax=0.0, ay=0.0, r=0.0):
        self.px = np.append(self.px, px)
        self.py = np.append(self.py, py)
        self.vx = np.append(self.vx, vx)
        self.vy = np.append(self.vy, vy)
        self.sz = np.append(self.sz, size)
        self.cl = np.append(self.cl, color)
        self.ax = np.append(self.ax, ax)
        self.ay = np.append(self.ay, ay)
        self.r = np.append(self.r, r)

    def run(self):
        ln_diff = len(self.px) - 540
        if ln_diff > 0:
            self.px = self.px[ln_diff:]
            self.py = self.py[ln_diff:]
            self.vx = self.vx[ln_diff:]
            self.vy = self.vy[ln_diff:]
            self.sz = self.sz[ln_diff:]
            self.cl = self.cl[ln_diff:]
            self.ax = self.ax[ln_diff:]
            self.ay = self.ay[ln_diff:]
            self.r = self.r[ln_diff:]

        move_nodes(self)

    def reflect(self):
        s = np.where(self.px > 1, -1, 1)
        s = s * np.where(self.px < 0, -1, 1)
        self.vx = self.vx * s

        s = np.where(self.py > 1, -1, 1)
        s = s * np.where(self.py < 0, -1, 1)
        self.vy = self.vy * s
