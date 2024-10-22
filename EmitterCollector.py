import cairo
import random
import numpy as np

from Emitter import Emitter
from LetterEmitter import LetterEmitter
from LineEmitter import LineEmitter
from ParticleCollector import ParticleCollector

np.random.seed(1)
random.seed(1)
WIDTH = 480
HEIGHT = 270
ASPECT_RATIO = WIDTH / HEIGHT


class EmitterCollector:
    emitters = []

    @staticmethod
    def add_emitter(emitter):
        EmitterCollector.emitters.append(emitter)

    @staticmethod
    def run(frame: int):
        for emitter in EmitterCollector.emitters:
            emitter.run(frame)

    @staticmethod
    def draw(frame: int, factor: int):
        s = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH * factor, HEIGHT * factor)
        ctx = cairo.Context(s)

        ctx.scale(270 * factor, 270 * factor)
        # m = cairo.Matrix(yy=-1, y0=s.get_height())
        # ctx.transform(m)

        # background
        ctx.set_source_rgb(0, 0, 0)
        ctx.paint()

        for emitter in EmitterCollector.emitters:
            emitter.draw(ctx, frame, factor)
        return s


def create_emitter_star(num=10, thrust=0.002, px=0.0, py=0.0, **kwargs):
    for x in range(0, num):
        angle = 360 * x / num + random.normalvariate(0, 7)
        EmitterCollector.add_emitter(Emitter(1, thrust=thrust + random.normalvariate(0, 0.0002),
                                             angle=angle, px=px, py=py, **kwargs))


def create_edges(num_x=6, num_y=3, **kwargs):
    diff_x = ASPECT_RATIO / num_x
    diff_y = 1 / num_y
    for _ in range(0, num_y + 1):
        # Left & Right edge
        EmitterCollector.add_emitter(LineEmitter(angle=0, px=0, py=diff_y * _,
                                                 **kwargs))
        EmitterCollector.add_emitter(LineEmitter(angle=180, px=ASPECT_RATIO, py=diff_y * _,
                                                 **kwargs))
    for _ in range(0, num_x + 1):
        # Top & bottom edge
        EmitterCollector.add_emitter(LineEmitter(angle=90, px=diff_x * _, py=0,
                                                 **kwargs))
        EmitterCollector.add_emitter(LineEmitter(angle=-90, px=diff_x * _, py=1,
                                                 **kwargs))


def create_grid(num_x=33, num_y=13, **kwargs):
    diff_x = ASPECT_RATIO / num_x
    diff_y = 1 / num_y
    for x in range(0, num_x + 1):
        for y in range(0, num_y + 1):
            EmitterCollector.add_emitter(Emitter(px=diff_x * x, py=diff_y * y, collector=ParticleCollector(),
                                                       **kwargs))
