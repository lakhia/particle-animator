import random
import numpy as np
import plotly.graph_objects as go

from Emitter import Emitter

np.random.seed(1)
random.seed(1)


class EmitterCollector:
    collector = []

    @staticmethod
    def add_emitter(emitter):
        EmitterCollector.collector.append(emitter)

    @staticmethod
    def spawn(emitter, **kwargs):
        EmitterCollector.add_emitter(Emitter(emitter.__dict__, **kwargs))

    @staticmethod
    def run(frame: int):
        for emitter in EmitterCollector.collector:
            emitter.run(frame)

    @staticmethod
    def draw(frame: int, factor: int):
        fig = go.Figure(
            layout=dict(showlegend=False,
                        plot_bgcolor='#000',
                        width=480 * factor,
                        height=270 * factor,
                        margin=dict(l=0, r=0, t=0, b=0)
                        )
        )
        fig.update_xaxes(visible=False, zeroline=False, showgrid=False, range=[0, 1])
        fig.update_yaxes(visible=False, zeroline=False, showgrid=False, range=[0, 1])
        for emitter in EmitterCollector.collector:
            fig.add_trace(go.Scatter(
                x=emitter.collector.px,
                y=emitter.collector.py,
                mode="markers",
                line=dict(
                    color="rgba(255,0,0,0.75)",
                    width=4 * factor
                ),
                marker=go.scatter.Marker(
                    size=emitter.collector.sz * factor,
                    color=emitter.collector.cl,
                    symbol=emitter.symbol,
                    opacity=0.3,
                    line=dict(
                        width=0
                    ),
                    colorscale=emitter.color_scale
                )
            ))
        return fig


def create_emitter_star(num=10, thrust=0.002, px=0.0, py=0.0, **kwargs):
    for x in range(0, num):
        angle = 360 * x / num + random.normalvariate(0, 7)
        EmitterCollector.add_emitter(Emitter(1, thrust=thrust + random.normalvariate(0, 0.0002),
                                             angle=angle, px=px, py=py, **kwargs))


def create_edges(num_x=10, num_y=10, **kwargs):
    for x in range(0, num_x + 1):
        for y in range(0, num_y + 1):
            if x < 1:
                EmitterCollector.add_emitter(Emitter(1, angle=0, px=x / num_x, py=-0.05 + y / num_y,
                                                     symbol='diamond-wide', **kwargs))
            elif x >= num_x:
                EmitterCollector.add_emitter(Emitter(1, angle=180, px=x / num_x, py=0.05 + y / num_y,
                                                     symbol='diamond-wide', **kwargs))
            elif y < 1:
                EmitterCollector.add_emitter(Emitter(1, angle=90, px=-0.008 + x / num_x, py=y / num_y,
                                                     **kwargs))
            elif y >= num_y:
                EmitterCollector.add_emitter(Emitter(1, angle=-90, px=0.008 + x / num_x, py=y / num_y,
                                                     **kwargs))
