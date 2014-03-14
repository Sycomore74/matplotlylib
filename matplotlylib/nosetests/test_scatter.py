from . nose_tools import compare_dict, run_fig
from . data.scatter import *
import matplotlib.pyplot as plt


def test_simple_scatter():
    fig, ax = plt.subplots()
    ax.scatter(D['x1'], D['y1'])
    renderer = run_fig(fig)
    for data_no, data_dict in enumerate(renderer.data):
        equivalent, msg = compare_dict(data_dict,
                                       SIMPLE_SCATTER['data'][data_no])
        assert equivalent, msg
    equivalent, msg = compare_dict(renderer.layout, SIMPLE_SCATTER['layout'])
    assert equivalent, msg


def test_double_scatter():
    fig, ax = plt.subplots()
    ax.scatter(D['x1'], D['y1'], color='red', s=121, marker='^', alpha=0.5)
    ax.scatter(D['x2'], D['y2'], color='purple', s=64, marker='s', alpha=0.5)
    renderer = run_fig(fig)
    for data_no, data_dict in enumerate(renderer.data):
        equivalent, msg = compare_dict(data_dict,
                                       DOUBLE_SCATTER['data'][data_no])
        assert equivalent, msg
    equivalent, msg = compare_dict(renderer.layout, DOUBLE_SCATTER['layout'])
    assert equivalent, msg