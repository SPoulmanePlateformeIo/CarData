from app import app, server
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import data
import layouts

app.layout = html.Div([
    html.Div(layouts.header, id='header'),
    html.Div([layouts.get_simple_graph(data.car_data, 'Simple Graph')]),
    html.Div([layouts.get_linreg_graph(data.car_data, data.fittedline, 'Linear regression comparison')]),
    html.Div([layouts.get_linreg_multi(data.car_data, data.multivariate_reg[0], data.multivariate_reg[1], 'Multivariate LinReg')])
])

if __name__ == '__main__':
    app.run_server(debug=True)
