import _PLOT
from Utils import transpose

import os
import csv

#transpose.transposeFiles()

joints = ""
exploitationCycles = "50"
precisionRange = "0.04"
episodes = "15"
controlCycles = "10"
isOrientationGoal = "false"
isLearnFromNeighbors = "false"


# figVaryingParamString = "controlCycles"
# labels = ['1','5','10','20']
# colors = ['tab:red', 'tab:blue', 'tab:green', 'tab:orange']
# markers = ['o','D','v','s']
#figVaryingParamString = "precisionRange"
#labels = ['0.02','0.04','0.06']
#colors = ['tab:red', 'tab:blue', 'tab:green']
#markers = ['o','D','v']
figVaryingParamString = "joints"
labels = ['3','6','10','20','30','50','100']
colors = ['tab:red', 'tab:blue', 'tab:green', 'tab:orange', 'tab:purple', 'tab:brown',  'tab:pink']
markers = ['o','D','v','s','P','p','*']
#figVaryingParamString = "joints"
#labels = ['3','30','100']
#colors = ['tab:red', 'tab:blue', 'tab:green']
#markers = ['o','D','v']
# figVaryingParamString = "isLearnFromNeighbors"
# labels = ['With Endogenous Learning', 'Without Endogenous Learning']
# colors = ['tab:red', 'tab:blue']
# markers = ['o','D']
#figVaryingParamString = "isOrientationGoal"
# labels = ['With Orientation Goal', 'Without Orientation Goal']
# colors = ['tab:red', 'tab:blue']
# markers = ['o','D']
for label in labels:
    joints += "-"+label
figParamsString = "Rg_" +  precisionRange + "_Jts_" + joints +"_Exp_" + exploitationCycles + "_Eps_" + episodes + "_Ctrl_" +  controlCycles + "_Ori_" + isOrientationGoal + "_Endo_" + isLearnFromNeighbors


figName = "EndoData-" +figParamsString
xlabel = 'Learning Cycles (#)'
ylabel = 'Mean Endogenous Learning Situations (#)'
logXScale = False
logYScale = False
xString = "learningCycles"
yString = "endogenousLearningSituationsAverage"
deviationString = "endogenousLearningSituationsDeviation"



constrains = [{"precisionRange": precisionRange, "joints": "3", "exploitatingCycles": exploitationCycles, "episodes": episodes, "isOrientationGoal": isOrientationGoal, "requestControlCycles": controlCycles, "isLearnFromNeighbors": isLearnFromNeighbors},
              {"precisionRange": precisionRange, "joints": "6", "exploitatingCycles": exploitationCycles, "episodes": episodes, "isOrientationGoal": isOrientationGoal, "requestControlCycles": controlCycles, "isLearnFromNeighbors": isLearnFromNeighbors},
              {"precisionRange": precisionRange, "joints": "10", "exploitatingCycles": exploitationCycles, "episodes": episodes, "isOrientationGoal": isOrientationGoal, "requestControlCycles": controlCycles, "isLearnFromNeighbors": isLearnFromNeighbors},
              {"precisionRange": precisionRange, "joints": "20", "exploitatingCycles": exploitationCycles, "episodes": episodes, "isOrientationGoal": isOrientationGoal, "requestControlCycles": controlCycles, "isLearnFromNeighbors": isLearnFromNeighbors},
              {"precisionRange": precisionRange, "joints": "30", "exploitatingCycles": exploitationCycles, "episodes": episodes, "isOrientationGoal": isOrientationGoal, "requestControlCycles": controlCycles, "isLearnFromNeighbors": isLearnFromNeighbors},
              {"precisionRange": precisionRange, "joints": "50", "exploitatingCycles": exploitationCycles, "episodes": episodes, "isOrientationGoal": isOrientationGoal, "requestControlCycles": controlCycles, "isLearnFromNeighbors": isLearnFromNeighbors},
              {"precisionRange": precisionRange, "joints": "100", "exploitatingCycles": exploitationCycles, "episodes": episodes, "isOrientationGoal": isOrientationGoal, "requestControlCycles": controlCycles, "isLearnFromNeighbors": isLearnFromNeighbors}

              ]



_PLOT.plotWithDeviation(labels, colors, markers, figName, xlabel, ylabel, logXScale, logYScale, xString, yString, deviationString, constrains, 1, 0.01)