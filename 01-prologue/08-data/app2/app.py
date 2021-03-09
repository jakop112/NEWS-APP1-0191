from flask import Flask, render_template
import json
import plotly
import plotly.graph_objs as go
import pandas as pd
import numpy as np
import requests

app = Flask(__name__)


@app.route('/bar-plot')
def bar_plot():
    n = 15
    x = np.linspace(-1, 1, n)
    y = np.random.randn(n)
    df = pd.DataFrame({'x': x, 'y': y})

    trace = [
        go.Bar(
            x=df['x'],
            y=df['y']
        )
    ]

    graphJSON = json.dumps(trace, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('graph.html', description='Bar-graph', plot=graphJSON)


