import _PLOT
from Utils import transpose

import os
import csv

#transpose.transposeFiles()

learningCycles = "200"
exploitationCycles = "50"
precisionRange = "0.04"
episodes = "15"
controlCycles = "10"
isOrientationGoal = "true"
isLearnFromNeighbors = ""

figParamsString = "Rg_" +  precisionRange + "_Lrn_" + learningCycles +"_Exp_" + exploitationCycles + "_Eps_" + episodes + "_Ctrl_" +  controlCycles + "_Ori_" + isOrientationGoal + "_Endo_" + isLearnFromNeighbors


#figVaryingParamString = "controlCycles"
#labels = ['1','5','10','20']
#colors = ['tab:red', 'tab:blue', 'tab:green', 'tab:orange']
#markers = ['o','D','v','s']
# figVaryingParamString = "learningCycles"
# labels = ['10','25','50','100','200','500','1000']
# colors = ['tab:red', 'tab:blue', 'tab:green', 'tab:orange', 'tab:purple', 'tab:brown' ,'tab:pink']
# markers = ['o','D','v','s','P','p','*']
#figVaryingParamString = "precisionRange"
#labels = ['2%','4%','6%']
#colors = ['tab:red', 'tab:blue', 'tab:green']
#markers = ['o','D','v']
figVaryingParamString = "isLearnFromNeighbors"
labels = ['With Endogenous Learning', 'Without Endogenous Learning']
colors = ['tab:red', 'tab:blue']
markers = ['o','D']
#figVaryingParamString = "isOrientationGoal"
# labels = ['With Orientation Goal', 'Without Orientation Goal']
# colors = ['tab:red', 'tab:blue']
# markers = ['o','D']

for label in labels:
    isLearnFromNeighbors += "-"+label
figParamsString = "Rg_" +  precisionRange + "_Lrn_" + learningCycles +"_Exp_" + exploitationCycles + "_Eps_" + episodes + "_Ctrl_" +  controlCycles + "_Ori_" + isOrientationGoal + "_Endo_" + isLearnFromNeighbors

figName = "Time-"+figParamsString

xlabel = 'Joints (#)'
ylabel = 'Mean Time Execution (s)'
logXScale = False
logYScale = False
xString = "joints"
yString = "meanTime"
deviationString = "meanTime"

constrains = [{"precisionRange": precisionRange, "learningCycles": learningCycles, "exploitatingCycles": exploitationCycles, "episodes": episodes, "isOrientationGoal": isOrientationGoal, "requestControlCycles": controlCycles, "isLearnFromNeighbors": "true"},
              {"precisionRange": precisionRange, "learningCycles": learningCycles, "exploitatingCycles": exploitationCycles, "episodes": episodes, "isOrientationGoal": isOrientationGoal, "requestControlCycles": controlCycles, "isLearnFromNeighbors": "false"},
              #{"precisionRange": precisionRange, "learningCycles": "50", "exploitatingCycles": exploitationCycles, "episodes": episodes, "isOrientationGoal": isOrientationGoal, "requestControlCycles": controlCycles, "isLearnFromNeighbors": isLearnFromNeighbors},
              #{"precisionRange": precisionRange, "learningCycles": "100", "exploitatingCycles": exploitationCycles, "episodes": episodes, "isOrientationGoal": isOrientationGoal, "requestControlCycles": controlCycles, "isLearnFromNeighbors": isLearnFromNeighbors},
              #{"precisionRange": precisionRange, "learningCycles": "200", "exploitatingCycles": exploitationCycles, "episodes": episodes, "isOrientationGoal": isOrientationGoal, "requestControlCycles": controlCycles, "isLearnFromNeighbors": isLearnFromNeighbors},
              #{"precisionRange": precisionRange, "learningCycles": "500", "exploitatingCycles": exploitationCycles, "episodes": episodes, "isOrientationGoal": isOrientationGoal, "requestControlCycles": controlCycles, "isLearnFromNeighbors": isLearnFromNeighbors},
              #{"precisionRange": precisionRange, "learningCycles": "1000", "exploitatingCycles": exploitationCycles, "episodes": episodes, "isOrientationGoal": isOrientationGoal, "requestControlCycles": controlCycles, "isLearnFromNeighbors": isLearnFromNeighbors}

              ]



_PLOT.plot(labels, colors, markers, figName, xlabel, ylabel, logXScale, logYScale, xString, yString, deviationString, constrains, 1, 1)