from app import app, server
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import data
import layouts

layouts.tab_contents['SP']['content'] = html.Div([layouts.get_simple_graph(data.car_data, 'Simple Graph')])
layouts.tab_contents['LRC']['content'] = html.Div([layouts.get_linreg_graph(data.car_data, data.fittedline, 'Linear regression comparison')])
layouts.tab_contents['MLR']['content'] = html.Div([layouts.get_linreg_multi(data.car_data, data.multivariate_reg, 'Multivariate LinReg')])
layouts.tab_contents['TC']['content'] = html.Div('Coming soon')

layouts.menu.children = [dcc.Tab(label=w['name'], children=w['content']) for k, w in layouts.tab_contents.items()]

app.layout = html.Div([
    html.Div(layouts.header, id='header'),
    layouts.menu,
])

if __name__ == '__main__':
    app.run_server(debug=True)
