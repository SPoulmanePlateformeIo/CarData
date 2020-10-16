import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go


header = html.H1('Car Data Analysis')

def get_simple_graph(data, title=''):
    return dcc.Graph(
        id='simple-graph',
        figure={
            'data': [
                go.Scatter(
                    x=data['Year'],
                    y=data['Selling_Price'],
                    text=data['Car_Name'],
                    mode='markers',
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                )
            ],
            'layout': go.Layout(
                xaxis={'title': 'Year'},
                yaxis={'title': 'Selling Price'},
                hovermode='closest',
                title=title,
            )
        }
    )


def get_linreg_graph(data, dict_fittedline, title=''):
    plot_data = [go.Scatter(
        x=data['Year'],
        y=data['Selling_Price'],
        name='Cars',
        text=data['Car_Name'],
        mode='markers',
        marker={
            'size': 5,
            'line': {'width': 0.5, 'color': 'white'}
        },
    )]
    dmin, dmax = data['Year'].min(), data['Year'].max()
    for k, w in dict_fittedline.items():
        plot_data += [go.Scatter(
            x=[dmin, dmax],
            y=[w[0]*dmin+w[1], w[0]*dmax+w[1]],
            name=k,
            opacity=0.75,
        )]
    return dcc.Graph(
        id='linreg-graph',
        figure={
            'data': plot_data,
            'layout': go.Layout(
                xaxis={'title': 'Year'},
                yaxis={'title': 'Selling Price'},
                hovermode='closest',
                title=title,
            )
        }
    )

def get_linreg_multi(data, coefs, intercept):
    plot_data = [go.Scatter(
        x=data['Year'],
        y=data['Selling_Price'],
        name='Cars',
        text=data['Car_Name'],
        mode='markers',
        marker={
            'size': 5,
            'line': {'width': 0.5, 'color': 'white'}
        },
    )]
    dmin, dmax = data['Year'].min(), data['Year'].max()
    plot_data += [go.Scatter(
            x=[dmin, dmax],
            y=[w[0]*dmin+w[1], w[0]*dmax+w[1]],
            name=k,
            opacity=0.75,
    )]
    return dcc.Graph(
        id='linreg-graph',
        figure={
            'data': plot_data,
            'layout': go.Layout(
                xaxis={'title': 'Year'},
                yaxis={'title': 'Selling Price'},
                hovermode='closest',
                title=title,
            )
        }
    )
