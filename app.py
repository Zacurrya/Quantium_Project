from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash()

df = pd.read_csv('data/pink_morsel_sales.csv')

line_chart = px.line(df, x='date', y='sales', title='Pink Morsel Sales', height=800)

app.layout = html.Div([
    dcc.Graph(figure=line_chart)
])

app.run(debug=True, port=8050)