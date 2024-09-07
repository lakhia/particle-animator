import plotly.graph_objects as go
import numpy as np

from Emitter import Emitter

np.random.seed(1)
FACTOR = 4
emitters = [Emitter(3, thrust=0.01, angle=90, px=0.75, py=0.5,
                    par_angle_offset=-90, speed=3, speed_variation=2),
            Emitter(3, thrust=0.01, angle=90, px=0.75, py=0.5,
                    par_angle_offset=90, speed=3, speed_variation=2)]

for n in range(1, 300):
    fig = go.Figure()
    fig.update_xaxes(visible=False, zeroline=False, showgrid=False, range=[0, 1])
    fig.update_yaxes(visible=False, zeroline=False, showgrid=False, range=[0, 1])
    fig.update_layout(
        showlegend=False,
        plot_bgcolor='#000',
        width=960 * FACTOR,
        height=540 * FACTOR,
        margin=dict(l=0, r=0, t=0, b=0)
    )

    for emitter in emitters:
        emitter.run()
        fig.add_trace(go.Scatter(
            x=emitter.collector.px,
            y=emitter.collector.py,
            mode="markers",
            marker=go.scatter.Marker(
                size=emitter.collector.sz * FACTOR,
                color=emitter.collector.cl,
                symbol='star',
                opacity=0.6,
                line=dict(
                    width=0
                ),
                colorscale="oranges"
            )
        ))

    if n % 10 == 0:
        print("Wrote %d frame" % n)

    fig.write_image('images/fig_%03d.png' % n)
