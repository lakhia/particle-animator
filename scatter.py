import plotly.graph_objects as go
import numpy as np

from NodeCollector import NodeCollector

np.random.seed(1)

N = 5
collector = NodeCollector()
collector.px = np.random.rand(N)
collector.py = np.random.rand(N)
collector.vx = (np.random.rand(N) - 0.5) / 12
collector.vy = (np.random.rand(N) - 0.5) / 12
colors = np.random.rand(N)
sz = np.random.rand(N) * 30

fig = go.Figure()
for n in range(1, 55):
    fig.add_trace(go.Scatter(
        x=collector.px,
        y=collector.py,
        mode="markers",
        marker=go.scatter.Marker(
            size=sz,
            color=colors,
            opacity=0.6,
            # colorscale="Viridis"
        )
    ))
    if len(fig.data) > 3:
        new_data = list(fig.data)
        new_data.pop(0)
        fig.data = new_data
    fig.data[0].marker.opacity *= 0.5

    fig.update_xaxes(visible=False, zeroline=False, showgrid=False, range=[0, 1])
    fig.update_yaxes(visible=False, zeroline=False, showgrid=False, range=[0, 1])
    fig.update_layout(
        showlegend=False,
        width=960,
        height=540,
        margin=dict(l=0, r=0, t=0, b=0)
    )
    collector.run()
    if n % 10 == 0:
        print("Wrote %d frame" % n)

    fig.write_image('fig__%03d.png' % n)
