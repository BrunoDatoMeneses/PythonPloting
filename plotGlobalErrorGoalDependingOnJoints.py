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
isLearnFromNeighbors = "true"


figVaryingParamString = "controlCycles"
labels = ['1','2','5','10','20']
colors = ['tab:red', 'tab:blue', 'tab:green', 'tab:orange', 'tab:purple']
markers = ['o','D','v','s','P']
#figVaryingParamString = "precisionRange"
#labels = ['2%','4%','6%']
#colors = ['tab:red', 'tab:blue', 'tab:green']
#markers = ['o','D','v']
#figVaryingParamString = "learningCycles"
#labels = ['10','25','50','100','200','500']
#colors = ['tab:red', 'tab:blue', 'tab:green', 'tab:orange', 'tab:purple', 'tab:brown']
#markers = ['o','D','v','s','P','p']
# figVaryingParamString = "isLearnFromNeighbors"
# labels = ['With Endogenous Learning', 'Without Endogenous Learning']
# colors = ['tab:red', 'tab:blue']
# markers = ['o','D']
#figVaryingParamString = "isOrientationGoal"
# labels = ['With Orientation Goal', 'Without Orientation Goal']
# colors = ['tab:red', 'tab:blue']
# markers = ['o','D']

for label in labels:
    controlCycles += "-"+label
figParamsString = "Rg_" +  precisionRange + "_Lrn_" + learningCycles +"_Exp_" + exploitationCycles + "_Eps_" + episodes + "_Ctrl_" +  controlCycles + "_Ori_" + isOrientationGoal + "_Endo_" + isLearnFromNeighbors

figName = "XYAndThetaErrorGoal-"+figParamsString
xlabel = 'Joints (#)'
ylabel = 'Mean Position and Orientation Error (%)'
logXScale = True
logYScale = False
xString = "joints"
yString1 = "goalXYErrorAverage"
deviationString1 = "goalXYErrorDeviationAverage"
yString2 = "goalThetaErrorAverage"
deviationString2 = "goalThetaErrorDeviationAverage"



constrains = [{"precisionRange": precisionRange, "learningCycles": learningCycles, "exploitatingCycles": exploitationCycles, "episodes": episodes, "isOrientationGoal": isOrientationGoal, "requestControlCycles": "1", "isLearnFromNeighbors": isLearnFromNeighbors},
              {"precisionRange": precisionRange, "learningCycles": learningCycles, "exploitatingCycles": exploitationCycles, "episodes": episodes, "isOrientationGoal": isOrientationGoal, "requestControlCycles": "2", "isLearnFromNeighbors": isLearnFromNeighbors},
              {"precisionRange": precisionRange, "learningCycles": learningCycles, "exploitatingCycles": exploitationCycles, "episodes": episodes, "isOrientationGoal": isOrientationGoal, "requestControlCycles": "5", "isLearnFromNeighbors": isLearnFromNeighbors},
              {"precisionRange": precisionRange, "learningCycles": learningCycles, "exploitatingCycles": exploitationCycles, "episodes": episodes, "isOrientationGoal": isOrientationGoal, "requestControlCycles": "10", "isLearnFromNeighbors": isLearnFromNeighbors},
              {"precisionRange": precisionRange, "learningCycles": learningCycles, "exploitatingCycles": exploitationCycles, "episodes": episodes, "isOrientationGoal": isOrientationGoal, "requestControlCycles": "20", "isLearnFromNeighbors": isLearnFromNeighbors},
              #{"precisionRange": precisionRange, "learningCycles": "200", "exploitatingCycles": exploitationCycles, "episodes": episodes, "isOrientationGoal": isOrientationGoal, "requestControlCycles": controlCycles, "isLearnFromNeighbors": isLearnFromNeighbors},
              #{"precisionRange": precisionRange, "learningCycles": "500", "exploitatingCycles": exploitationCycles, "episodes": episodes, "isOrientationGoal": isOrientationGoal, "requestControlCycles": controlCycles, "isLearnFromNeighbors": isLearnFromNeighbors},
              #{"precisionRange": precisionRange, "learningCycles": "1000", "exploitatingCycles": exploitationCycles, "episodes": episodes, "isOrientationGoal": isOrientationGoal, "requestControlCycles": controlCycles, "isLearnFromNeighbors": isLearnFromNeighbors}

              ]


_PLOT.plotMeanWithDeviation(labels, colors, markers, figName, xlabel, ylabel, logXScale, logYScale, xString, yString1, yString2, deviationString1, deviationString2, constrains, 1, 1)