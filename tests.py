from app import update_line_chart
import pandas as pd

def test_header():
    df = pd.read_csv('data/pink_morsel_sales.csv')
    assert list(df.columns) == ['sales', 'date', 'region']

def test_line_chart():
    fig = update_line_chart('all')
    assert fig.data is not None

def test_region_radio():
    options = ['all', 'north', 'south', 'east', 'west']
    for option in options:
        fig = update_line_chart(option)
        assert fig is None
