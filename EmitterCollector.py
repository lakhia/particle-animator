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
                        width=960 * factor,
                        height=540 * factor,
                        margin=dict(l=0, r=0, t=0, b=0)
                        )
        )
        fig.update_xaxes(visible=False, zeroline=False, showgrid=False, range=[0, 1])
        fig.update_yaxes(visible=False, zeroline=False, showgrid=False, range=[0, 1])
        for emitter in EmitterCollector.collector:
            fig.add_trace(go.Scatter(
                line_shape='linear',
                x=emitter.collector.px,
                y=emitter.collector.py,
                mode="lines",
                line=dict(
                    color="rgba(255,0,0,0.75)",
                    width=4 * factor
                ),
                marker=go.scatter.Marker(
                    size=emitter.collector.sz * factor,
                    color=emitter.collector.cl,
                    symbol='circle',
                    opacity=0.3,
                    line=dict(
                        width=0
                    ),
                    colorscale=emitter.color_scale
                )
            ))
        return fig


def create_emitter_star(num=10, thrust=0.0006, px=0.0, py=0.0, **kwargs):
    for x in range(0, num):
        angle = 360 * x / num + random.normalvariate(0, 7)
        EmitterCollector.add_emitter(Emitter(3, thrust=thrust + random.normalvariate(0, 0.0002),
                                             angle=angle, px=px, py=py, **kwargs))
