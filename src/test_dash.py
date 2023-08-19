from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

df = pd.DataFrame({
    'country': ['Canada', 'US', 'England','Canada', 'US', 'England','Canada', 'US', 'England',],
    'year': [2020,2020,2020,2021,2021,2021,2022,2022,2022,],
    'pop': [100,200,300,200,100,60,50,75,120,],
})

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='Title of Dash App', style={'textAlign':'center'}),
    dcc.Dropdown(df['country'].unique(), 'Canada', id='dropdown-selection'),
    dcc.Graph(id='graph-content')
])

@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    dff = df[df.country==value]
    return px.line(dff, x='year', y='pop')

if __name__ == '__main__':
    app.run(debug=True)