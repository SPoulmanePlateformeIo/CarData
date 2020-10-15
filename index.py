from app import app, server
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd

car_data = pd.read_csv('data/carData.csv')
print(car_data)

app.layout = html.Div(('Hello Word!'))

if __name__ == '__main__':
    app.run_server(debug=True)
