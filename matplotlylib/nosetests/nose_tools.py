from .. mplexporter import Exporter
from .. import PlotlyRenderer
from numbers import Number as Num


def compare_dict(dict1, dict2, equivalent=True, msg='', tol=10e-8):
    for key in dict1:
        if key not in dict2:
            return False, "{} not {}".format(dict1.keys(), dict2.keys())
    for key in dict1:
        if isinstance(dict1[key], dict):
            equivalent, msg = compare_dict(dict1[key],
                                           dict2[key],
                                           tol=tol)
        elif isinstance(dict1[key], Num) and isinstance(dict2[key], Num):
            if not comp_nums(dict1[key], dict2[key], tol):
                return False, "['{}'] = {} not {}".format(key,
                                                          dict1[key],
                                                          dict2[key])
        elif is_num_list(dict1[key]) and is_num_list(dict2[key]):
            if not comp_num_list(dict1[key], dict2[key], tol):
                return False, "['{}'] = {} not {}".format(key,
                                                          dict1[key],
                                                          dict2[key])
        elif not (dict1[key] == dict2[key]):
                return False, "['{}'] = {} not {}".format(key,
                                                          dict1[key],
                                                          dict2[key])
        if not equivalent:
            return False, "['{}']".format(key) + msg
    return equivalent, msg


def comp_nums(num1, num2, tol=10e-8):
    return abs(num1-num2) < tol


def comp_num_list(list1, list2, tol=10e-8):
    for item1, item2 in zip(list1, list2):
        if not comp_nums(item1, item2, tol):
            return False
    return True


def is_num_list(item):
    try:
        for thing in item:
            if not isinstance(thing, Num):
                raise TypeError
    except TypeError:
        return False
    return True


def run_fig(fig):
    renderer = PlotlyRenderer()
    exporter = Exporter(renderer)
    exporter.run(fig)
    return renderer
