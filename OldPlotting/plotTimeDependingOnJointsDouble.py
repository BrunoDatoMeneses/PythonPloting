import _PLOT
from Utils import transpose

import os
import csv

#transpose.transposeFiles()

learningCycles = "200"
exploitationCycles = "50"
precisionRange = "0.04"
episodes = "15"
controlCycles = ""
isOrientationGoal = "true"
isLearnFromNeighbors = ""


# figVaryingParamString = "controlCycles"
# labels = ['1','5','10','20']
# colors = ['tab:red', 'tab:blue', 'tab:green', 'tab:orange']
# markers = ['o','D','v','s']
# figVaryingParamString = "precisionRange"
# labels = ['0.02','0.04','0.06']
# colors = ['tab:red', 'tab:blue', 'tab:green']
# markers = ['o','D','v']
figVaryingParamString = "learningCyclesAndIsLearnFromNeighbors"
labels = ['1','5','10','20','1 with CNL','5 with CNL','10 with CNL','20 with CNL']
colors = ['darkred', 'tab:red', 'indianred', 'lightcoral', 'darkblue', 'b', 'tab:blue', 'skyblue']
markers = ['o','D','v','s','P','p','*','X']
#figVaryingParamString = "isOrientationGoal"
# labels = ['With Orientation Goal', 'Without Orientation Goal']
# colors = ['tab:red', 'tab:blue']
# markers = ['o','D']



figParamsString = "Rg_" +  precisionRange + "_Lrn_" + learningCycles +"_Exp_" + exploitationCycles + "_Eps_" + episodes + "_Ctrl_" +  controlCycles + "_Ori_" + isOrientationGoal + "_Endo_" + isLearnFromNeighbors

figName = "TimeDoubleParams-"+figParamsString

xlabel = 'Joints (#)'
ylabel = 'Mean Time Execution (s)'
logXScale = False
logYScale = False
xString = "joints"
yString = "meanTime"
deviationString = "meanTime"

constraints1 = [{"precisionRange": precisionRange, "learningCycles": learningCycles, "exploitatingCycles": exploitationCycles, "episodes": episodes, "isOrientationGoal": isOrientationGoal, "requestControlCycles": "1", "isLearnFromNeighbors": "false"},
              {"precisionRange": precisionRange, "learningCycles": learningCycles, "exploitatingCycles": exploitationCycles, "episodes": episodes, "isOrientationGoal": isOrientationGoal, "requestControlCycles": "5", "isLearnFromNeighbors": "false"},
              {"precisionRange": precisionRange, "learningCycles": learningCycles, "exploitatingCycles": exploitationCycles, "episodes": episodes, "isOrientationGoal": isOrientationGoal, "requestControlCycles": "10", "isLearnFromNeighbors": "false"},
              {"precisionRange": precisionRange, "learningCycles": learningCycles, "exploitatingCycles": exploitationCycles, "episodes": episodes, "isOrientationGoal": isOrientationGoal, "requestControlCycles": "20", "isLearnFromNeighbors": "false"}
              ]

constraints2 = [{"precisionRange": precisionRange, "learningCycles": learningCycles, "exploitatingCycles": exploitationCycles, "episodes": episodes, "isOrientationGoal": isOrientationGoal, "requestControlCycles": "1", "isLearnFromNeighbors": "true"},
              {"precisionRange": precisionRange, "learningCycles": learningCycles, "exploitatingCycles": exploitationCycles, "episodes": episodes, "isOrientationGoal": isOrientationGoal, "requestControlCycles": "5", "isLearnFromNeighbors": "true"},
              {"precisionRange": precisionRange, "learningCycles": learningCycles, "exploitatingCycles": exploitationCycles, "episodes": episodes, "isOrientationGoal": isOrientationGoal, "requestControlCycles": "10", "isLearnFromNeighbors": "true"},
              {"precisionRange": precisionRange, "learningCycles": learningCycles, "exploitatingCycles": exploitationCycles, "episodes": episodes, "isOrientationGoal": isOrientationGoal, "requestControlCycles": "20", "isLearnFromNeighbors": "true"}
              ]



_PLOT.plot2(labels, colors, markers, figName, xlabel, ylabel, logXScale, logYScale, xString, yString, deviationString, constraints1, constraints2, 1, 1)