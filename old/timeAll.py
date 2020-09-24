import numpy as np

from old import FIG


def run(log):


    labelsString = ['30 joints', '20 joints', '10 joints','6 joints','3 joints','2 joints']
    colors = ['tab:red', 'tab:olive', 'tab:purple','tab:blue', 'tab:orange', 'tab:green']
    markers = ['*','p','s','o','v','D']


    ylabel = 'Mean ExecutionTime (s)'
    logScale = log
    globalLabel = "Time_"


    x_values_neighborhoods = []
    for i in range(6):
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
    jointsString = "joints_302010632"

    y_values001 = []



    #30joints
    y_values001.append(np.array([
        10,
    10,
    10,
    10,
    10,
    11,
    11,
    11,
    10


    ]))

    #20joints
    y_values001.append(np.array([
        4,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    4



    ]))

    #10joints
    y_values001.append(np.array([
        1,
    1,
    1,
    1,
    1,
    1,
    1,
    2,
    2


    ]))



    #6joints
    y_values001.append(np.array([
        1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1



    ]))


    #3joints
    y_values001.append(np.array([
        1,
    1,
    1,
    1,
    1,
    1,
    1,
    2,
    3



    ]))


    #2joints
    y_values001.append(np.array([
        1,
    1,
    1,
    1,
    1,
    2,
    2,
    3,
    4


    ]))








    FIG.fig(x_values_neighborhoods, y_values001, labelsString, xlabel, ylabel, colors, markers, globalLabel + CONTEXT_SIZE + "_" + jointsString + "_" + figlabel, logScale)

    CONTEXT_SIZE="0_03" #######################################################################################################################################################


    y_values003 = []



    #30joints
    y_values003.append(np.array([
        10,
    10,
    11,
    11,
    11,
    11,
    20,
    108,
    589

    ]))

    #20joints
    y_values003.append(np.array([
        4,
    4,
    4,
    4,
    5,
    6,
    29,
    167,
    631



    ]))


    #10joints
    y_values003.append(np.array([
        1,
    1,
    2,
    2,
    4,
    15,
    68,
    210,
    542


    ]))


    #6joints
    y_values003.append(np.array([
        1,
    1,
    1,
    2,
    7,
    22,
    66,
    163,
    377


    ]))



    #3joints
    y_values003.append(np.array([
        1,
    1,
    2,
    6,
    15,
    31,
    63,
    117,
    216


    ]))



    #2joints
    y_values003.append(np.array([
        1,
    1,
    2,
    5,
    11,
    20,
    39,
    68,
    119

    ]))












    FIG.fig(x_values_neighborhoods, y_values003, labelsString, xlabel, ylabel, colors, markers, globalLabel + CONTEXT_SIZE + "_" + jointsString + "_" + figlabel, logScale)



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



    CONTEXT_SIZE="0_01"

    x_values_request = []



    #30joints
    x_values_request.append(np.array([
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

    #20joints
    x_values_request.append(np.array([
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


    #10joints
    x_values_request.append(np.array([
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



    #6joints
    x_values_request.append(np.array([
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




    #3joints
    x_values_request.append(np.array([
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




    #2joints
    x_values_request.append(np.array([
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

    x_values_request.reverse()
    y_values001.reverse()
    labelsString.reverse()
    colors.reverse()
    markers.reverse()







    FIG.fig(x_values_request, y_values001, labelsString, xlabel, ylabel, colors, markers, globalLabel + CONTEXT_SIZE + "_" + jointsString + "_" + figlabel, logScale)

    CONTEXT_SIZE="0_03" ######################################################################################################################################################

    x_values_request = []


    #30joints
    x_values_request.append(np.array([
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


    #20joints
    x_values_request.append(np.array([
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

    #10joints
    x_values_request.append(np.array([
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














    #6joints

    x_values_request.append(np.array([
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




    #3joints
    x_values_request.append(np.array([
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





    #2joints
    x_values_request.append(np.array([
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

    x_values_request.reverse()
    y_values003.reverse()





    FIG.fig(x_values_request, y_values003, labelsString, xlabel, ylabel, colors, markers, globalLabel + CONTEXT_SIZE + "_" + jointsString + "_" + figlabel, logScale)

