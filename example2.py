# Perform imports here:
#https://plotly.com/python/bar-charts/
#https://docs.google.com/document/d/1DjWL2DxLiRaBrlD3ELyQlCBRu7UQuuWfgjv9LncNp_M/edit#

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output

app =dash.Dash()

df = pd.read_csv('data//2018WinterOlympics.csv')
fig = px.bar(df, x = 'NOC', y = ['Gold', 'Silver', 'Bronze'], barmode = 'stack')

app.layout=html.Div([
    html.H1("Dashboard"),
    html.Div("Winter Olympics 2018"),

    html.H1(""), 
    html.Label('Dropdown'),
    dcc.Dropdown(id ='medals_id', options=[{'label':'Gold', 'value' : 'Gold'}, {'label':'Silver', 'value' : 'Silver'}, {'label':'Bronze', 'value' : 'Bronze'}], value =['Gold', 'Silver'], multi = True),

    dcc.Graph(id = 'medals_graph', figure = fig)
])



@app.callback(Output(component_id ='medals_graph', component_property='figure'), Input(component_id ='medals_id', component_property='value'))
def update_graph(med):
    fig = px.bar(df, x = 'NOC', y = med, barmode = 'stack')
    return fig

# Add the server clause:
if __name__ == '__main__':
    app.run_server()