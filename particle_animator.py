import plotly.graph_objects as go
import numpy as np

from Emitter import Emitter

np.random.seed(1)
N = 5
FACTOR = 4
emitter1 = Emitter(0.5, 0.5, -135, 18)
emitter2 = Emitter(0.5, 0.5, 135, 18)
emitter3 = Emitter(0.5, 0.5, -45, 18)
emitter4 = Emitter(0.5, 0.51, 45, 18)

for n in range(1, 360):
    emitter1.run()
    emitter2.run()
    emitter3.run()
    emitter4.run()

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=emitter1.collector.px,
        y=emitter1.collector.py,
        mode="markers",
        marker=go.scatter.Marker(
            size=emitter1.collector.sz * FACTOR,
            color=emitter1.collector.cl,
            opacity=0.6,
            line=dict(
                width=0
            ),
            colorscale="Viridis"
        )
    ))
    fig.add_trace(go.Scatter(
        x=emitter2.collector.px,
        y=emitter2.collector.py,
        mode="markers",
        marker=go.scatter.Marker(
            size=emitter2.collector.sz * FACTOR,
            color=emitter2.collector.cl,
            opacity=0.6,
            line=dict(
                width=0
            ),
            colorscale="Viridis"
        )
    ))
    fig.add_trace(go.Scatter(
        x=emitter3.collector.px,
        y=emitter3.collector.py,
        mode="markers",
        marker=go.scatter.Marker(
            size=emitter3.collector.sz * FACTOR,
            color=emitter3.collector.cl,
            opacity=0.6,
            line=dict(
                width=0
            ),
            colorscale="Viridis"
        )
    ))
    fig.add_trace(go.Scatter(
        x=emitter4.collector.px,
        y=emitter4.collector.py,
        mode="markers",
        marker=go.scatter.Marker(
            size=emitter4.collector.sz * FACTOR,
            color=emitter4.collector.cl,
            opacity=0.6,
            line=dict(
                width=0
            ),
            colorscale="Viridis"
        )
    ))

    fig.update_xaxes(visible=False, zeroline=False, showgrid=False, range=[0, 1])
    fig.update_yaxes(visible=False, zeroline=False, showgrid=False, range=[0, 1])
    fig.update_layout(
        showlegend=False,
        plot_bgcolor='#000',
        width=960 * FACTOR,
        height=540 * FACTOR,
        margin=dict(l=0, r=0, t=0, b=0)
    )
    if n % 10 == 0:
        print("Wrote %d frame" % n)

    fig.write_image('fig_%03d.png' % n)
