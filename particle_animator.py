import plotly.graph_objects as go
import numpy as np
from random import uniform
from Emitter import Emitter

np.random.seed(1)
FACTOR = 4
emitters = [
    Emitter(18, thrust=0, angle=90, px=0.5, py=0.10, speed=8, speed_variation=2),
    Emitter(3, thrust=0, angle=90, px=0.5, py=0.12, color_scale='reds',
            angle_variation=20.0, speed=9, speed_variation=3),
    Emitter(2, thrust=0, angle=90, px=0.5, py=0.17,
            angle_variation=5.0, speed=4, speed_variation=1),
]

for n in range(1, 300):
    fig = go.Figure(
        layout=dict(showlegend=False,
                    plot_bgcolor='#000',
                    width=960 * FACTOR,
                    height=540 * FACTOR,
                    margin=dict(l=0, r=0, t=0, b=0)
                    )
    )
    fig.update_xaxes(visible=False, zeroline=False, showgrid=False, range=[0, 1])
    fig.update_yaxes(visible=False, zeroline=False, showgrid=False, range=[0, 1])

    for emitter in emitters:
        emitter.run(n)
        fig.add_trace(go.Scatter(
            x=emitter.collector.px,
            y=emitter.collector.py,
            mode="markers",
            marker=go.scatter.Marker(
                size=emitter.collector.sz * FACTOR,
                color=emitter.collector.cl,
                symbol='circle',
                opacity=0.3,
                line=dict(
                    width=0
                ),
                colorscale=emitter.color_scale
            )
        ))

    if n % 10 == 0:
        print("Wrote %d frame" % n)

    fig.write_image('images/fig_%03d.png' % n)
