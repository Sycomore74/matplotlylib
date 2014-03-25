D = dict(
    x1=[1, 2, 2, 4, 5, 6, 1, 7, 8, 5 ,3],
    y1=[5, 3, 7, 2, 9, 7, 8, 4, 5, 9, 2],
    x2=[-1, 1, -0.3, -0.6, 0.4, 0.8, -0.1, 0.7],
    y2=[-0.5, 0.4, 0.7, -0.6, 0.3, -1, 0, 0.3]
)

SIMPLE_SCATTER = {
    'data': [{'marker': {'color': 'rgb(0,0,255)',
                         'line': {'color': 'rgb(0,0,0)', 'width': 1.0},
                         'opacity': 1.0,
                         'size': 4.4721359549995796,
                         'symbol': 'dot'},
              'mode': 'markers',
              'showlegend': False,
              'x': [1.0, 2.0, 2.0, 4.0, 5.0, 6.0, 1.0, 7.0, 8.0, 5.0, 3.0],
              'y': [5.0, 3.0, 7.0, 2.0, 9.0, 7.0, 8.0, 4.0, 5.0, 9.0, 2.0]}],
    'layout': {'autosize': False,
               'hovermode': 'closest',
               'height': 480,
               'margin': {'b': 47, 'l': 80, 'pad': 0, 'r': 63, 't': 47},
               'showlegend': False,
               'width': 640,
               'xaxis': {'anchor': 'y',
                         'domain': [0.0, 1.0],
                         'range': (0.0, 9.0),
                         'showgrid': False,
                         'zeroline': False},
               'yaxis': {'anchor': 'x',
                         'domain': [0.0, 1.0],
                         'range': (1.0, 10.0),
                         'showgrid': False,
                         'zeroline': False}}}

DOUBLE_SCATTER = {
    'data': [{'marker': {'color': 'rgb(255,0,0)',
                         'line': {'color': 'rgb(255,0,0)', 'width': 1.0},
                         'opacity': 0.5,
                         'size': 11.0,
                         'symbol': 'triangle-up'},
              'mode': 'markers',
              'showlegend': False,
              'x': [1.0, 2.0, 2.0, 4.0, 5.0, 6.0, 1.0, 7.0, 8.0, 5.0, 3.0],
              'y': [5.0, 3.0, 7.0, 2.0, 9.0, 7.0, 8.0, 4.0, 5.0, 9.0, 2.0]},
             {'marker': {'color': 'rgb(128,0,128)',
                         'line': {'color': 'rgb(128,0,128)', 'width': 1.0},
                         'opacity': 0.5,
                         'size': 8.0,
                         'symbol': 'square'},
              'mode': 'markers',
              'showlegend': False,
              'x': [-1.0,
                    1.0,
                    -0.29999999999999999,
                    -0.59999999999999998,
                    0.40000000000000002,
                    0.80000000000000004,
                    -0.10000000000000001,
                    0.69999999999999996],
                    'y': [-0.5,
                    0.40000000000000002,
                    0.69999999999999996,
                    -0.59999999999999998,
                    0.29999999999999999,
                    -1.0,
                    0.0,
                    0.29999999999999999]}],
    'layout': {'autosize': False,
               'hovermode': 'closest',
               'height': 480,
               'margin': {'b': 47, 'l': 80, 'pad': 0, 'r': 63, 't': 47},
               'showlegend': False,
               'width': 640,
               'xaxis': {'anchor': 'y',
                         'domain': [0.0, 1.0],
                         'range': (-2.0, 10.0),
                         'showgrid': False,
                         'zeroline': False},
               'yaxis': {'anchor': 'x',
                         'domain': [0.0, 1.0],
                         'range': (-2.0, 10.0),
                         'showgrid': False,
                         'zeroline': False}}}
