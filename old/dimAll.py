import numpy as np

from old import FIG


def run(log):


    colors = ['tab:brown', 'tab:olive']
    markers = ['o', 'D']
    ylabel = 'Mean Error from Goal (%)'
    xlabel = 'Joints (#)'
    logScale = log

    labelsString = ['precision_range 3%', 'precision_range 1%' ]


    x_values_dimensions = []


    x_values_dimensions.append(np.array([2, 3, 6, 10, 20, 30]))
    x_values_dimensions.append(np.array([2, 3, 6, 10, 20, 30]))

    CONTEXT_SIZE="0_01"

    figlabel = "Joints"
    jointsString = "joints_236102030"

    y_values = []
    error_values= []



    y_values.append(np.array([
        3.6,
        3.41,
        4.71,
        5.32,
        4.79,
        3.73

    ]))
    error_values.append(np.array([
        4.45,
        3.93,
        4.62,
        3.66,
        2.03,
        1.76

    ]))

    y_values.append(np.array([
        2.26,
        2.43,
        4.19,
        5.47,
        4.58,
        3.5

    ]))
    error_values.append(np.array([
        3.43,
        3.81,
        5.05,
        4.02,
        1.9,
        1.56,

    ]))

    FIG.fig(x_values_dimensions, y_values, error_values, labelsString, xlabel, ylabel, colors, markers, 'Error_' + jointsString + "_" + figlabel, logScale)



