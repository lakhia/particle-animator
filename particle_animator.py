import plotly.graph_objects as go
import numpy as np
from random import uniform
from Emitter import Emitter

np.random.seed(1)
FACTOR = 4
emitters = [
    Emitter(0.5, thrust=0.006, angle=180+uniform(-10,10), px=1, py=0.20,
            par_angle_offset=-90+uniform(-10,10), speed=0, speed_variation=0),
    Emitter(0.5, thrust=0.006, angle=uniform(-10,10), px=0, py=0.80,
            par_angle_offset=-90+uniform(-10,10), speed=0, speed_variation=0),
    Emitter(0.5, thrust=0.006, angle=180+uniform(-10,10), px=1, py=0.60,
            par_angle_offset=90+uniform(-10,10), speed=0, speed_variation=0),
    Emitter(0.5, thrust=0.006, angle=uniform(-10,10), px=0, py=0.40,
            par_angle_offset=90+uniform(-10,10), speed=0, speed_variation=0),

    Emitter(0.5, thrust=0.006, angle=-90+uniform(-10,10), px=0.2, py=1,
            par_angle_offset=-90+uniform(-10,10), speed=0, speed_variation=0),
    Emitter(0.5, thrust=0.006, angle=90+uniform(-10,10), px=0.8, py=0,
            par_angle_offset=-90+uniform(-10,10), speed=0, speed_variation=0),
    Emitter(0.5, thrust=0.006, angle=-90+uniform(-10,10), px=0.60, py=1,
            par_angle_offset=90+uniform(-10,10), speed=0, speed_variation=0),
    Emitter(0.5, thrust=0.006, angle=90+uniform(-10,10), px=0.40, py=0,
            par_angle_offset=90+uniform(-10,10), speed=0, speed_variation=0),
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
                symbol='star-diamond',
                opacity=0.6,
                line=dict(
                    width=0
                ),
                colorscale="greens"
            )
        ))

    if n % 10 == 0:
        print("Wrote %d frame" % n)

    fig.write_image('images/fig_%03d.png' % n)
