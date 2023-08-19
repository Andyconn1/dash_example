from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

df = pd.DataFrame({
    'country': ['Canada', 'US', 'England','Canada', 'US', 'England','Canada', 'US', 'England',],
    'year': [str(x) for x in [2020,2020,2020,2021,2021,2021,2022,2022,2022,]],
    'pop': [100,200,300,200,100,60,50,75,120,],
    'wealth': [50,45,30,30,35,38,42,48,91,],
    'co2': [9000,10000,11000,12000,14000,15000,14500,14200,14800,],
})

app = Dash(__name__)

app.layout = html.Div([
    html.Div(
        id="sidebar",
        style={
            "position": "fixed",
            "top": 0,
            "left": 0,
            "width": "20%",
            "height": "100%",
            "background-color": "#f0f0f0",
            "padding": "20px"
        },
        children=[
            html.H1("Filters", style={"margin-bottom": "20px"}),
            dcc.Dropdown(df['country'].unique(), 'Canada', id='dropdown-selection'),
        ]
    ),
    html.Div(
        id="content",
        style={
            "margin-left": "25%",
            "padding": "20px"
        },
        children=[
            html.H1(children='Overview', style={'textAlign':'center'}),
            html.H2(children='Population:', style={'textAlign':'left'}),
            dcc.Graph(id='graph-content'),
            html.H2(children='Wealth:', style={'textAlign':'left'}),
            dcc.Graph(id='graph-content2'),
            html.H2(children='CO2 Emissions:', style={'textAlign':'left'}),
            dcc.Graph(id='graph-content3'),
        ]
    )    
])

@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    dff = df[df.country==value]
    return px.line(dff, x='year', y='pop')

@callback(
    Output('graph-content2', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph2(value):
    dff = df[df.country==value]
    return px.line(dff, x='year', y='wealth')

@callback(
    Output('graph-content3', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph3(value):
    dff = df[df.country==value]
    return px.line(dff, x='year', y='co2')

if __name__ == '__main__':
    app.run(debug=True)