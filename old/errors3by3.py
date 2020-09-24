import numpy as np

from old import FIG


def run(log):


    labelsString632 = ['6 joints', '3 joints', '2 joints']
    colors632 = ['tab:blue', 'tab:orange', 'tab:green']
    labelsString102030 = ['10 joints', '20 joints', '30 joints']
    colors102030 = ['tab:purple', 'tab:olive', 'tab:red']
    markers632 = ['o','v','D']
    markers102030 = [ 's', 'p', '*']

    ylabel = 'Mean Error from Goal (%)'
    logScale = log


    x_values_neighborhoods = []
    for i in range(3):
        x_values_neighborhoods.append(np.array([
            0,
        2,
        4,
        6,
        8,
        10,
        12,
        14,
        16
                      ]))


    CONTEXT_SIZE="0_01"
    xlabel = 'Neihborhood Sizes'
    figlabel = "Neighborshoods"
    jointsString = "joints_632"

    y_values632 = []
    error_values236= []

    #6joints
    y_values632.append(np.array([
        4.19,
    4.3,
    4.26,
    4.32,
    4.41,
    4.29,
    4.06,
        4.35,
    4.5
    ]))
    error_values236.append( np.array([
        5.05,
    5.12,
    5.09,
    5.08,
    5.19,
    5.06,
    4.99,
        5.14,
    5.29
    ]))

    #3joints
    y_values632.append(np.array([
        2.43,
    2.64,
    2.41,
    2.3,
    2.55,
    2.25,
    2.15,
        1.96,
    1.68

    ]))
    error_values236.append( np.array([
        3.81,
    4.34,
    3.54,
    3.37,
    4.06,
    3.73,
    3.55,
        3.33,
    2.39

    ]))

    #2joints
    y_values632.append(np.array([
        2.26,
    2.18,
    2.05,
    1.91,
    1.61,
    1.39,
    1.31,
        1.23,
    1.24
    ]))
    error_values236.append( np.array([
        3.43,
    3.54,
    3.41,
    3.37,
    2.47,
    1.79,
    1.54,
        1.24,
    1.41
    ]))


    FIG.figWithDeviation(x_values_neighborhoods, y_values632, error_values236, labelsString632, xlabel, ylabel, colors632, markers632, 'Error_' + CONTEXT_SIZE + "_" + jointsString + "_" + figlabel, logScale)


    jointsString = "joints_102030"
    y_values102030 = []
    error_values102030= []

    #10joints
    y_values102030.append(np.array([
        5.47,
    5.71,
    5.42,
    5.51,
    5.52,
    5.29,
    5.6,
        5.48,

    5.52
    ]))
    error_values102030.append( np.array([
        4.02,
    4.03,
    3.94,
    4.01,
    4.04,
    3.93,
    4.01,
    4.05,
    3.96
    ]))

    #20joints
    y_values102030.append(np.array([
        4.58,
    4.65,
    4.55,
    4.63,
    4.58,
    4.61,
    4.63,
    4.59,
    4.59

    ]))
    error_values102030.append( np.array([
        1.9,
    1.95,
    1.93,
    1.85,
    1.91,
    1.89,
    1.96,
    1.9,
    1.91

    ]))

    #30joints
    y_values102030.append(np.array([
        3.5,
    3.54,
    3.49,
    3.43,
    3.49,
    3.46,
    3.48,
    3.42,
    3.5
    ]))
    error_values102030.append( np.array([
        1.56,
    1.51,
    1.56,
    1.51,
    1.55,
    1.48,
    1.53,
    1.45,
    1.55
    ]))


    FIG.figWithDeviation(x_values_neighborhoods, y_values102030, error_values102030, labelsString102030, xlabel, ylabel, colors102030, markers102030, 'Error_' + CONTEXT_SIZE + "_" + jointsString + "_" + figlabel, logScale)

    CONTEXT_SIZE="0_03" #######################################################################################################################################################

    jointsString = "joints_632"
    y_values632 = []
    error_values236= []

    #6joints
    y_values632.append(np.array([
        4.71,
    4.66,
    4.64,
    4.84,
    4.16,
    3.45,
    3.38,
    3.34,
    3.33
    ]))
    error_values236.append( np.array([
        4.62,
    4.66,
    4.52,
    4.71,
    4.1,
    3.3,
    3.05,
    2.85,
    2.89
    ]))

    #3joints
    y_values632.append(np.array([
        3.41,
    3.41,
    2.78,
    2.21,
    2.16,
    2.23,
    2.37,
    2.72,
    3.14

    ]))
    error_values236.append( np.array([
        3.93,
    4.06,
    3.32,
    2.03,
    1.68,
    1.56,
    1.46,
    1.73,
    2.11

    ]))

    #2joints
    y_values632.append(np.array([
        3.6,
    2.45,
    1.95,
    1.94,
    2.15,
    2.54,
    3.15,
        3.86,
    4.42
    ]))
    error_values236.append( np.array([
        4.45,
    2.87,
    1.91,
    1.33,
    1.39,
    1.49,
    2.27,
    2.67,
    3.4
    ]))


    FIG.figWithDeviation(x_values_neighborhoods, y_values632, error_values236, labelsString632, xlabel, ylabel, colors632, markers632, 'Error_' + CONTEXT_SIZE + "_" + jointsString + "_" + figlabel, logScale)


    jointsString = "joints_102030"
    y_values102030 = []
    error_values102030= []

    #10joints
    y_values102030.append(np.array([
        5.32,
    5.53,
    5.39,
    5.45,
    5.46,
    4.98,
    4.37,
        4.38,
    4.08
    ]))
    error_values102030.append( np.array([
        3.66,
    3.68,
    3.71,
    3.67,
    3.67,
    3.53,
    3.29,
    3.31,
    3.14
    ]))

    #20joints
    y_values102030.append(np.array([
        4.79,
    4.7,
    4.79,
    4.72,
    4.77,
    4.82,
    5.05,
    5.04,
    4.9

    ]))
    error_values102030.append( np.array([
        2.03,
    2.09,
    2.03,
    2.07,
    2.08,
    2.09,
    2.16,
    2.33,
    2.36


    ]))

    #30joints
    y_values102030.append(np.array([
        3.73,
    3.77,
    3.73,
    3.75,
    3.72,
    3.8,
    3.88,
    4.04,
    4.05
    ]))
    error_values102030.append( np.array([
        1.76,
    1.76,
    1.76,
    1.76,
    1.78,
    1.77,
    1.83,
    2.01,
    2.02

    ]))


    FIG.figWithDeviation(x_values_neighborhoods, y_values102030, error_values102030, labelsString102030, xlabel, ylabel, colors102030, markers102030, 'Error_' + CONTEXT_SIZE + "_" + jointsString + "_" + figlabel, logScale)



    ##################################################################
    ##################################################################
    ##################################################################
    ##################################################################
    ##################################################################
    ##################################################################
    ##################################################################
    ##################################################################




    xlabel = 'Mean Endogenous Learning Situations (#)'
    figlabel = "Requests"
    jointsString = "joints_632"



    CONTEXT_SIZE="0_01"

    x_values_request632 = []
    y_values632 = []
    error_values236= []

    #6joints
    x_values_request632.append(np.array([
        0,
    0.07,
    0.93,
    7.67,
    30,
    108,
    266,
    576,
    1138

    ]))

    y_values632.append(np.array([
        4.19,
    4.3,
    4.26,
    4.32,
    4.41,
    4.29,
    4.06,
        4.35,
    4.5
    ]))
    error_values236.append( np.array([
        5.05,
    5.12,
    5.09,
    5.08,
    5.19,
    5.06,
    4.99,
        5.14,
    5.29
    ]))

    #3joints
    x_values_request632.append(np.array([
        0,
    50,
    239,
    646,
    1358,
    2555,
    4285,
    6627,
    9726


    ]))

    y_values632.append(np.array([
        2.43,
    2.64,
    2.41,
    2.3,
    2.55,
    2.25,
    2.15,
        1.96,
    1.68

    ]))
    error_values236.append( np.array([
        3.81,
    4.34,
    3.54,
    3.37,
    4.06,
    3.73,
    3.55,
        3.33,
    2.39

    ]))

    #2joints
    x_values_request632.append(np.array([
        0,
    867,
    2484,
    4778,
    7897,
    11684,
    16177,
    21132,
    27026



    ]))


    y_values632.append(np.array([
        2.26,
    2.18,
    2.05,
    1.91,
    1.61,
    1.39,
    1.31,
        1.23,
    1.24
    ]))
    error_values236.append( np.array([
        3.43,
    3.54,
    3.41,
    3.37,
    2.47,
    1.79,
    1.54,
        1.24,
    1.41
    ]))


    FIG.figWithDeviation(x_values_request632, y_values632, error_values236, labelsString632, xlabel, ylabel, colors632, markers632, 'Error_' + CONTEXT_SIZE + "_" + jointsString + "_" + figlabel, logScale)

    x_values_request102030=[]
    y_values102030 = []
    error_values102030= []
    jointsString = "joints_102030"

    #10joints
    x_values_request102030.append(np.array([
        0,
    0,
    0,
    0,
    0.2,
    1.67,
    6.2,
    32,
    90

    ]))

    y_values102030.append(np.array([
        5.47,
    5.71,
    5.42,
    5.51,
    5.52,
    5.29,
    5.6,
        5.48,

    5.52
    ]))
    error_values102030.append( np.array([
        4.02,
    4.03,
    3.94,
    4.01,
    4.04,
    3.93,
    4.01,
    4.05,
    3.96
    ]))

    #20joints
    x_values_request102030.append(np.array([
        0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0


    ]))

    y_values102030.append(np.array([
        4.58,
    4.65,
    4.55,
    4.63,
    4.58,
    4.61,
    4.63,
    4.59,
    4.59

    ]))
    error_values102030.append( np.array([
        1.9,
    1.95,
    1.93,
    1.85,
    1.91,
    1.89,
    1.96,
    1.9,
    1.91

    ]))

    #30joints
    x_values_request102030.append(np.array([
        0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0


    ]))


    y_values102030.append(np.array([
        3.5,
    3.54,
    3.49,
    3.43,
    3.49,
    3.46,
    3.48,
    3.42,
    3.5
    ]))
    error_values102030.append( np.array([
        1.56,
    1.51,
    1.56,
    1.51,
    1.55,
    1.48,
    1.53,
    1.45,
    1.55
    ]))


    FIG.figWithDeviation(x_values_request102030, y_values102030, error_values102030, labelsString102030, xlabel, ylabel, colors102030, markers102030, 'Error_' + CONTEXT_SIZE + "_" + jointsString + "_" + figlabel, logScale)

    CONTEXT_SIZE="0_03" ######################################################################################################################################################

    jointsString = "joints_632"
    x_values_request632 = []
    y_values632 = []
    error_values236= []

    #6joints

    x_values_request632.append(np.array([
        0,
    25,
    517,
    3339,
    12698,
    34692,
    72665,
    128232,
    194713



    ]))

    y_values632.append(np.array([
        4.71,
    4.66,
    4.64,
    4.84,
    4.16,
    3.45,
    3.38,
    3.34,
    3.33
    ]))
    error_values236.append( np.array([
        4.62,
    4.66,
    4.52,
    4.71,
    4.1,
    3.3,
    3.05,
    2.85,
    2.89
    ]))

    #3joints
    x_values_request632.append(np.array([
        0,
    1877,
    9940,
    26169,
    51344,
    90120,
    147360,
    222384,
    322725




    ]))


    y_values632.append(np.array([
        3.41,
    3.41,
    2.78,
    2.21,
    2.16,
    2.23,
    2.37,
    2.72,
    3.14

    ]))
    error_values236.append( np.array([
        3.93,
    4.06,
    3.32,
    2.03,
    1.68,
    1.56,
    1.46,
    1.73,
    2.11

    ]))

    #2joints
    x_values_request632.append(np.array([
        0,
    7879,
    20474,
    39195,
    68894,
    111861,
    170000,
    255998,
    376259





    ]))


    y_values632.append(np.array([
        3.6,
    2.45,
    1.95,
    1.94,
    2.15,
    2.54,
    3.15,
        3.86,
    4.42
    ]))
    error_values236.append( np.array([
        4.45,
    2.87,
    1.91,
    1.33,
    1.39,
    1.49,
    2.27,
    2.67,
    3.4
    ]))


    FIG.figWithDeviation(x_values_request632, y_values632, error_values236, labelsString632, xlabel, ylabel, colors632, markers632, 'Error_' + CONTEXT_SIZE + "_" + jointsString + "_" + figlabel, logScale)

    jointsString = "joints_102030"
    x_values_request102030=[]
    y_values102030 = []
    error_values102030= []

    #10joints
    x_values_request102030.append(np.array([
        0,
    0.07,
    23.67,
    438,
    2860,
    12642,
    37443,
    77551,
    130806






    ]))


    y_values102030.append(np.array([
        5.32,
    5.53,
    5.39,
    5.45,
    5.46,
    4.98,
    4.37,
        4.38,
    4.08
    ]))
    error_values102030.append( np.array([
        3.66,
    3.68,
    3.71,
    3.67,
    3.67,
    3.53,
    3.29,
    3.31,
    3.14
    ]))

    #20joints
    x_values_request102030.append(np.array([
        0,
    0,
    0,
    1.67,
    59.47,
    512,
    1682,
    4082,
    8903


    ]))


    y_values102030.append(np.array([
        4.79,
    4.7,
    4.79,
    4.72,
    4.77,
    4.82,
    5.05,
    5.04,
    4.9

    ]))
    error_values102030.append( np.array([
        2.03,
    2.09,
    2.03,
    2.07,
    2.08,
    2.09,
    2.16,
    2.33,
    2.36


    ]))

    #30joints
    x_values_request102030.append(np.array([
        0,
    0,
    0,
    0,
    2.53,
    67.33,
    476,
    1049,
    2021



    ]))

    y_values102030.append(np.array([
        3.73,
    3.77,
    3.73,
    3.75,
    3.72,
    3.8,
    3.88,
    4.04,
    4.05
    ]))
    error_values102030.append( np.array([
        1.76,
    1.76,
    1.76,
    1.76,
    1.78,
    1.77,
    1.83,
    2.01,
    2.02

    ]))


    FIG.figWithDeviation(x_values_request102030, y_values102030, error_values102030, labelsString102030, xlabel, ylabel, colors102030, markers102030, 'Error_' + CONTEXT_SIZE + "_" + jointsString + "_" + figlabel, logScale)

    jointsString = "joints_2030"
    x_values_request2030=[]
    y_values2030 = []
    error_values2030= []
    markers = ['p','*']


    #20joints
    x_values_request2030.append(np.array([
        0,
    0,
    0,
    1.67,
    59.47,
    512,
    1682,
    4082,
    8903


    ]))


    y_values2030.append(np.array([
        4.79,
    4.7,
    4.79,
    4.72,
    4.77,
    4.82,
    5.05,
    5.04,
    4.9

    ]))
    error_values2030.append( np.array([
        2.03,
    2.09,
    2.03,
    2.07,
    2.08,
    2.09,
    2.16,
    2.33,
    2.36


    ]))

    #30joints
    x_values_request2030.append(np.array([
        0,
    0,
    0,
    0,
    2.53,
    67.33,
    476,
    1049,
    2021



    ]))

    y_values2030.append(np.array([
        3.73,
    3.77,
    3.73,
    3.75,
    3.72,
    3.8,
    3.88,
    4.04,
    4.05
    ]))
    error_values2030.append( np.array([
        1.76,
    1.76,
    1.76,
    1.76,
    1.78,
    1.77,
    1.83,
    2.01,
    2.02

    ]))


    FIG.figWithDeviation(x_values_request2030, y_values2030, error_values2030, labelsString102030, xlabel, ylabel, colors102030, markers, 'Error_' + CONTEXT_SIZE + "_" + jointsString + "_" + figlabel, logScale)