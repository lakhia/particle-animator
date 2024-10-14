import cairo
import random
from matplotlib import cm, colors
import numpy as np

from Emitter import Emitter
from LineEmitter import LineEmitter

np.random.seed(1)
random.seed(1)
WIDTH = 480
HEIGHT = 270
ASPECT_RATIO = WIDTH / HEIGHT


class EmitterCollector:
    collector = []

    @staticmethod
    def add_emitter(emitter):
        EmitterCollector.collector.append(emitter)

    @staticmethod
    def run(frame: int):
        for emitter in EmitterCollector.collector:
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

        ctx.set_line_width(1 / 70)
        norm = colors.Normalize(vmin=0, vmax=1, clip=True)
        mapper = cm.ScalarMappable(norm=norm, cmap="hot")
        for emitter in EmitterCollector.collector:
            ln = len(emitter.collector.px)
            for i, (x, y, cl) in enumerate(zip(emitter.collector.px, emitter.collector.py, emitter.collector.cl)):
                ctx.line_to(x, y)
                cl = mapper.to_rgba(cl, alpha=0.4)
                ctx.set_source_rgba(cl[0], cl[1], cl[2], cl[3])
                ctx.stroke()
                if i != ln - 1:
                    ctx.move_to(x, y)
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

