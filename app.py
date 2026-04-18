from dash import Dash, html, dcc, Input, Output, callback
import plotly.express as px
import pandas as pd

app = Dash()

df = pd.read_csv('data/pink_morsel_sales.csv')

app.layout = html.Div([
    dcc.RadioItems(
        id='region-radio',
        options=['north', 'south', 'east', 'west', 'all'],
        value='all', # default selected
        style={'color': 'white', 'padding': '10px'},
        inputStyle={'marginRight': '5px', 'accentColor': '#00b4d8'},
        labelStyle={
            'color': 'white',
            'marginRight': '20px',
            'marginTop': '30px',
            'cursor': 'pointer',
            'fontSize': '15px',
            'fontWeight': '500',
            'fontFamily': 'Inter, sans-serif',
            'letterSpacing': '0.5px'
        }
    ),
    dcc.Graph(id='line-chart', style={'max-height': '30vh'})
], style={
    'display': 'flex',
    'flex-direction': 'row',
    'gap': '20px',
    'background-color': '#1e1e1e',
    'min-height': '100vh',
    'color': 'white',
    'padding': '20px',
    'margin': '0'
})

# calls update_line_chart when the radio value changes
@callback(
    Output('line-chart', 'figure'),
    Input('region-radio', 'value')
)
def update_line_chart(selected_region):
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'] == selected_region]

    fig = px.line(filtered_df, x='date', y='sales', title='Pink Morsel Sales', height=600)

    fig.update_layout(
        paper_bgcolor='#1e1e1e',
        plot_bgcolor='#1e1e1e',
        font=dict(color='white', family='Arial'),
        title=dict(font=dict(size=18, color='white')),
        xaxis=dict(color='white', gridcolor='#333', showgrid=True, zeroline=False),
        yaxis=dict(color='white', gridcolor='#333', showgrid=True, zeroline=False),
        margin=dict(l=40, r=40, t=60, b=40),
    )

    fig.update_traces(line=dict(color='#00b4d8', width=2))
    return fig

if __name__ == '__main__':
    app.run(debug=True, port=8050)