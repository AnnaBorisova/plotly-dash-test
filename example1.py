# Perform imports here:
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import plotly.express as px

app =dash.Dash()

df = pd.read_csv('data//2018WinterOlympics.csv')
fig = px.bar(df, x = 'NOC', y = ['Gold', 'Silver', 'Bronze'], barmode = 'stack')

app.layout=html.Div([
    html.H1("Dashboard"),
    html.Div("Winter Olympics 2018"),
    dcc.Graph(id = 'medals', figure = fig)
])

# Add the server clause:
if __name__ == '__main__':
    app.run_server()

