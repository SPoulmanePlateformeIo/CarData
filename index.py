from app import app, server
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import data
import layouts
from comments import *

layouts.tab_contents['SP']['content'] = html.Div([my_comments['SP'], layouts.get_simple_graph(data.car_data, 'Simple Graph')])
layouts.tab_contents['LRC']['content'] = html.Div([my_comments['LRC'], layouts.get_linreg_graph(data.car_data, data.fittedline, 'Linear regression comparison')])
layouts.tab_contents['MLR']['content'] = html.Div([my_comments['MLR'], layouts.get_linreg_multi(data.car_data, data.multivariate_reg, 'Multivariate LinReg')])
layouts.tab_contents['TC']['content'] = html.Div([my_comments['TC'], layouts.get_times_table(data.time_linreg)])

layouts.menu.children = [dcc.Tab(label=w['name'], children=w['content']) for k, w in layouts.tab_contents.items()]

app.layout = html.Div([
    html.Div(layouts.header, id='header'),
    layouts.menu,
])

if __name__ == '__main__':
    app.run_server(debug=True)
