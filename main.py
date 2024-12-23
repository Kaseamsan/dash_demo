# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 11:19:22 2024

@author: chaiwana
"""
"""
Dash is running on http://127.0.0.1:8050/

 * Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:8050 (Press CTRL+C to quit)
"""

from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
import os
import config

csv_path = os.path.join(os.path.dirname(__file__), config.csv_file)
df = pd.read_csv(csv_path)

app = Dash()

app.layout = [
    html.H1(children='ETL jobs on Blendata', style={'textAlign':'center'}),
    dcc.Dropdown(df['table_name'].unique(), 'table_name', id='dropdown-selection'),
    dcc.Graph(id='graph-content')
]

@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    dff = df[df['table_name']==value]
    fig = px.line(dff, x='date_time', y='count', color='region', markers=True)
    #fig = px.line(dff, x='date_time', y='count', color='region', markers=True, text='count')
    #fig.update_traces(textposition="top center")
    return fig

if __name__ == '__main__':
    app.run(debug=True, port=config.port)
