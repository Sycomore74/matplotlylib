"""
plotly_words
============

A module that contains language data for plotly. There is not meant to be
functionality here, only some definitions for use with the plotly_words module.

"""

INFO = dict(

    base=dict(
        kind='base',
        safe=[],
        valid=[],
        repair_vals=dict(),
        repair_keys=dict()
    ),

    data=dict(
        kind='data',
        safe=['name',
              'mode',
              'y',
              'x',
              'type',
              'bardir',
              'xaxis',
              'yaxis'],
        valid=['textfont',
               'name',
               'marker',
               'mode',
               'y',
               'x',
               'line',
               'type',
               'error_y',
               'opacity',
               'bardir',
               'showlegend',
               'xaxis',
               'yaxis'],
        repair_vals=dict(xaxis=['x1', None],
                         yaxis=['y1', None]),
        repair_keys=dict()
    ),

    layout=dict(
        kind='layout',
        safe=['title',
              'width',
              'height',
              'autosize'],
        valid=['title',
               'xaxis',
               'yaxis',
               'legend',
               'width',
               'height',
               'autosize',
               'margin',
               'paper_bgcolor',
               'plot_bgcolor',
               'barmode',
               'bargap',
               'bargroupgap',
               'boxmode',
               'boxgap',
               'boxgroupgap',
               'font',
               'titlefont',
               'dragmode',
               'hovermode',
               'separators',
               'hidesources',
               'showlegend',
               'annotations'],
        repair_vals=dict(),
        repair_keys=dict(xaxis1='xaxis',
                         yaxis1='yaxis')
    ),

    xaxis=dict(
        kind='xaxis',
        safe=['range',
              'type',
              'showticklabels',
              'exponentformat',
              'zeroline',
              'overlaying',
              'domain',
              'position',
              'anchor',
              'title'],
        valid=['range',
               'type',
               'showline',
               'mirror',
               'linecolor',
               'linewidth',
               'tick0',
               'dtick',
               'ticks',
               'ticklen',
               'tickcolor',
               'nticks',
               'showticklabels',
               'tickangle',
               'exponentformat',
               'showexponent',
               'showgrid',
               'gridcolor',
               'gridwidth',
               'autorange',
               'rangemode',
               'autotick',
               'zeroline',
               'zerolinecolor',
               'zerolinewidth',
               'titlefont',
               'tickfont',
               'overlaying',
               'domain',
               'position',
               'anchor',
               'title'],
        repair_vals=dict(anchor=['y1', 'y']),
        repair_keys=dict()
    ),

    yaxis=dict(
        kind='yaxis',
        safe=['range',
              'type',
              'showticklabels',
              'exponentformat',
              'zeroline',
              'overlaying',
              'domain',
              'position',
              'anchor',
              'title'],
        valid=['range',
               'type',
               'showline',
               'mirror',
               'linecolor',
               'linewidth',
               'tick0',
               'dtick',
               'ticks',
               'ticklen',
               'tickcolor',
               'nticks',
               'showticklabels',
               'tickangle',
               'exponentformat',
               'showexponent',
               'showgrid',
               'gridcolor',
               'gridwidth',
               'autorange',
               'rangemode',
               'autotick',
               'zeroline',
               'zerolinecolor',
               'zerolinewidth',
               'titlefont',
               'tickfont',
               'overlaying',
               'domain',
               'position',
               'anchor',
               'title'],
        repair_vals=dict(anchor=['x1', 'x']),
        repair_keys=dict()
    ),

    marker=dict(
        kind='marker',
        safe=['symbol',
              'size'],
        valid=['symbol',
               'line',
               'size',
               'color',
               'opacity'],
        repair_vals=dict(),
        repair_keys=dict()
    ),

    legend=dict(
        kind='legend',
        safe=['traceorder'],
        valid=['bgcolor',
               'bordercolor',
               'font',
               'traceorder'],
        repair_vals=dict(),
        repair_keys=dict()
    ),

    line=dict(
        kind='line',
        safe=['dash'],
        valid=['dash',
               'color',
               'width',
               'opacity'],
        repair_vals=dict(),
        repair_keys=dict()
    ),

    margin=dict(
        kind='margin',
        safe=['l',
               'r',
               'b',
               't',
               'pad'],
        valid=['l',
               'r',
               'b',
               't',
               'pad'],
        repair_vals=dict(),
        repair_keys=dict()
    ),

    font=dict(
        kind='font',
        safe=[],
        valid=['color',
               'size',
               'family'],
        repair_vals=dict(),
        repair_keys=dict()
    ),

    annotation=dict(
        kind='annotation',
        safe=['text',
              'xref',
              'yref',
              'showarrow',
              'align',
              'xanchor',
              'yanchor',
              'ay',
              'ax',
              'y',
              'x'],
        valid=['text',
               'bordercolor',
               'borderwidth',
               'borderpad',
               'bgcolor',
               'xref',
               'yref',
               'showarrow',
               'arrowwidth',
               'arrowcolor',
               'arrowhead',
               'arrowsize',
               'tag',
               'font',
               'opacity',
               'align',
               'xanchor',
               'yanchor',
               'ay',
               'ax',
               'y',
               'x'],
        repair_vals=dict(xref=['x1', 'x'],
                         yref=['y1', 'y']),
        repair_keys=dict()
    )

)