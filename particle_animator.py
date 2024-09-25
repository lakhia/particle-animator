import plotly.graph_objects as go
import numpy as np
from Emitter import Emitter

np.random.seed(1)
FACTOR = 4
emitters = [
    Emitter(1, thrust=0.0033, angle=90, px=(0.1 + x / 100), py=-0.01, speed=0, speed_variation=0)
    for x in range(1, 10)
]
emitters.extend([
    Emitter(1, thrust=0.0033, angle=180, py=(0.1 + 1.7 * x / 100), px=1.01, speed=0, speed_variation=0)
    for x in range(1, 10)]
)
emitters.extend([
    Emitter(1, thrust=0.0033, angle=-90, px=(0.8 + x / 100), py=1.01, speed=0, speed_variation=0)
    for x in range(1, 10)]
)
emitters.extend([
    Emitter(1, thrust=0.0033, angle=0, py=(0.72 + 1.7 * x / 100), px=-0.01, speed=0, speed_variation=0)
    for x in range(1, 10)]
)

for n in range(1, 360):
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
            line_shape='linear',
            x=emitter.collector.px,
            y=emitter.collector.py,
            mode="lines",
            line=dict(
                color="rgba(255,0,0,0.75)",
                width=4*FACTOR
            ),
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
