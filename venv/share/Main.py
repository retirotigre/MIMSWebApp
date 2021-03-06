#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is taken from the Dash installation guide for testing purposes:
# https://dash.plot.ly/getting-started


import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='MIMS Data'),

    html.Div(children='''
        This is a development server. Do not use it in production 
        deployment. Deployment server credits: 
        https://dash.plot.ly/getting-started
'''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name':
                    'Oxygen'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar',
                 'name': 'Argon'},
            ],
            'layout': {
                'title': 'Sample Data Visualization'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
