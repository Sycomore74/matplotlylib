from . nose_tools import compare_dict, run_fig
from . data.lines import *
import matplotlib.pyplot as plt


def test_simple_line():
    fig, ax = plt.subplots()
    ax.plot(D['x1'], D['y1'])
    renderer = run_fig(fig)
    for data_no, data_dict in enumerate(renderer.data):
        equivalent, msg = compare_dict(data_dict, SIMPLE_LINE['data'][data_no])
        assert equivalent, msg
    equivalent, msg = compare_dict(renderer.layout, SIMPLE_LINE['layout'])
    assert equivalent, msg


def test_complicated_line():
    fig, ax = plt.subplots()
    ax.plot(D['x1'], D['y1'], 'ro', markersize=10, alpha=.5)
    ax.plot(D['x1'], D['y1'], '-b', linewidth=2, alpha=.7)
    ax.plot(D['x2'], D['y2'], 'b+', markeredgewidth=2, markersize=10, alpha=.6)
    ax.plot(D['x2'], D['y2'], '--r', linewidth=2, alpha=.8)
    renderer = run_fig(fig)
    for data_no, data_dict in enumerate(renderer.data):
        equivalent, msg = compare_dict(data_dict,
                                       COMPLICATED_LINE['data'][data_no])
        assert equivalent, msg
    equivalent, msg = compare_dict(renderer.layout, COMPLICATED_LINE['layout'])
    assert equivalent, msg