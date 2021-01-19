import _PLOT
from Utils import transpose

import os
import csv

#transpose.transposeFiles()

learningCycles = ""
exploitationCycles = "50"
precisionRange = "0.04"
episodes = "15"
controlCycles = "10"
isOrientationGoal = "false"
isLearnFromNeighbors = "true"
joints = ""


# figVaryingParamString = "controlCycles"
# labels = ['1','5','10','20']
# colors = ['tab:red', 'tab:blue', 'tab:green', 'tab:orange']
# markers = ['o','D','v','s']
#figVaryingParamString = "precisionRange"
#labels = ['2%','4%','6%']
#colors = ['tab:red', 'tab:blue', 'tab:green']
#markers = ['o','D','v']
#figVaryingParamString = "learningCycles"
#labels = ['10','25','50','100','200','500']
#colors = ['tab:red', 'tab:blue', 'tab:green', 'tab:orange', 'tab:purple', 'tab:brown']
#markers = ['o','D','v','s','P','p']
#figVaryingParamString = "joints"
#labels = ['3','6','10','20']
#colors = ['tab:red', 'tab:blue', 'tab:green', 'tab:orange']
#markers = ['o','D','v','s']
figVaryingParamString = "joints"
labels = ['3','6','10','20','30','50','100']
colors = ['tab:red', 'tab:blue', 'tab:green', 'tab:orange','tab:purple', 'tab:brown', 'tab:pink']
markers = ['o','D','v','s','P','p','*']
#figVaryingParamString = "joints"
#labels = ['30','50','100']
#colors = ['tab:purple', 'tab:brown', 'tab:pink']
#markers = ['P','p','*']
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
figParamsString = "Rg_" +  precisionRange + "_Lrn_" + learningCycles +"_Exp_" + exploitationCycles + "_Eps_" + episodes + "_Ctrl_" +  controlCycles + "_Jts_" +  joints + "_Ori_" + isOrientationGoal + "_Endo_" + isLearnFromNeighbors

figName = "XYGoal-"+figParamsString
xlabel = 'Endogenous Learning Situations (#)'
ylabel = 'Mean Position Error (%)'
logXScale = True
logYScale = False
xString = "endogenousLearningSituationsAverage"
yString = "goalXYErrorAverage"
deviationString = "goalXYErrorDeviationAverage"

"""constrains = [{"precisionRange": precisionRange, "learningCycles": "25", "exploitatingCycles": exploitationCycles, "episodes": episodes, "isOrientationGoal": isOrientationGoal, "requestControlCycles": controlCycles, "isLearnFromNeighbors": isLearnFromNeighbors},
              {"precisionRange": precisionRange, "learningCycles": "25", "exploitatingCycles": exploitationCycles, "episodes": episodes, "isOrientationGoal": isOrientationGoal, "requestControlCycles": controlCycles, "isLearnFromNeighbors": isLearnFromNeighbors},
              {"precisionRange": precisionRange, "learningCycles": "50", "exploitatingCycles": exploitationCycles, "episodes": episodes, "isOrientationGoal": isOrientationGoal, "requestControlCycles": controlCycles, "isLearnFromNeighbors": isLearnFromNeighbors},
              {"precisionRange": precisionRange, "learningCycles": "100", "exploitatingCycles": exploitationCycles, "episodes": episodes, "isOrientationGoal": isOrientationGoal, "requestControlCycles": controlCycles, "isLearnFromNeighbors": isLearnFromNeighbors},
              {"precisionRange": precisionRange, "learningCycles": "200", "exploitatingCycles": exploitationCycles, "episodes": episodes, "isOrientationGoal": isOrientationGoal, "requestControlCycles": controlCycles, "isLearnFromNeighbors": isLearnFromNeighbors},
              {"precisionRange": precisionRange, "learningCycles": "500", "exploitatingCycles": exploitationCycles, "episodes": episodes, "isOrientationGoal": isOrientationGoal, "requestControlCycles": controlCycles, "isLearnFromNeighbors": isLearnFromNeighbors},
              {"precisionRange": precisionRange, "learningCycles": "1000", "exploitatingCycles": exploitationCycles, "episodes": episodes, "isOrientationGoal": isOrientationGoal, "requestControlCycles": controlCycles, "isLearnFromNeighbors": isLearnFromNeighbors}

              ]"""

"""constrains = [{"precisionRange": precisionRange, "learningCycles": "10", "exploitatingCycles": exploitationCycles, "episodes": episodes, "isOrientationGoal": isOrientationGoal, "requestControlCycles": controlCycles, "isLearnFromNeighbors": isLearnFromNeighbors, "joints": joints},
              {"precisionRange": precisionRange, "learningCycles": "25", "exploitatingCycles": exploitationCycles, "episodes": episodes, "isOrientationGoal": isOrientationGoal, "requestControlCycles": controlCycles, "isLearnFromNeighbors": isLearnFromNeighbors, "joints": joints},
              {"precisionRange": precisionRange, "learningCycles": "50", "exploitatingCycles": exploitationCycles, "episodes": episodes, "isOrientationGoal": isOrientationGoal, "requestControlCycles": controlCycles, "isLearnFromNeighbors": isLearnFromNeighbors, "joints": joints},
              {"precisionRange": precisionRange, "learningCycles": "100", "exploitatingCycles": exploitationCycles, "episodes": episodes, "isOrientationGoal": isOrientationGoal, "requestControlCycles": controlCycles, "isLearnFromNeighbors": isLearnFromNeighbors, "joints": joints},
              {"precisionRange": precisionRange, "learningCycles": "200", "exploitatingCycles": exploitationCycles, "episodes": episodes, "isOrientationGoal": isOrientationGoal, "requestControlCycles": controlCycles, "isLearnFromNeighbors": isLearnFromNeighbors, "joints": joints},
              {"precisionRange": precisionRange, "learningCycles": "500", "exploitatingCycles": exploitationCycles, "episodes": episodes, "isOrientationGoal": isOrientationGoal, "requestControlCycles": controlCycles, "isLearnFromNeighbors": isLearnFromNeighbors, "joints": joints},
              #{"precisionRange": precisionRange, "learningCycles": "1000", "exploitatingCycles": exploitationCycles, "episodes": episodes, "isOrientationGoal": isOrientationGoal, "requestControlCycles": controlCycles, "isLearnFromNeighbors": isLearnFromNeighbors}

              ]"""

constrains = [{"precisionRange": precisionRange, "exploitatingCycles": exploitationCycles, "episodes": episodes, "isOrientationGoal": isOrientationGoal, "requestControlCycles": controlCycles, "isLearnFromNeighbors": isLearnFromNeighbors, "joints": "3"},
              {"precisionRange": precisionRange, "exploitatingCycles": exploitationCycles, "episodes": episodes, "isOrientationGoal": isOrientationGoal, "requestControlCycles": controlCycles, "isLearnFromNeighbors": isLearnFromNeighbors, "joints": "6"},
              {"precisionRange": precisionRange, "exploitatingCycles": exploitationCycles, "episodes": episodes, "isOrientationGoal": isOrientationGoal, "requestControlCycles": controlCycles, "isLearnFromNeighbors": isLearnFromNeighbors, "joints": "10"},
              {"precisionRange": precisionRange, "exploitatingCycles": exploitationCycles, "episodes": episodes, "isOrientationGoal": isOrientationGoal, "requestControlCycles": controlCycles, "isLearnFromNeighbors": isLearnFromNeighbors, "joints": "20"},
              {"precisionRange": precisionRange, "exploitatingCycles": exploitationCycles, "episodes": episodes, "isOrientationGoal": isOrientationGoal, "requestControlCycles": controlCycles, "isLearnFromNeighbors": isLearnFromNeighbors, "joints": "30"},
              {"precisionRange": precisionRange, "exploitatingCycles": exploitationCycles, "episodes": episodes, "isOrientationGoal": isOrientationGoal, "requestControlCycles": controlCycles, "isLearnFromNeighbors": isLearnFromNeighbors, "joints": "50"},
              {"precisionRange": precisionRange, "exploitatingCycles": exploitationCycles, "episodes": episodes, "isOrientationGoal": isOrientationGoal, "requestControlCycles": controlCycles, "isLearnFromNeighbors": isLearnFromNeighbors, "joints": "100"}

              ]



_PLOT.plotWithDeviation(labels, colors, markers, figName, xlabel, ylabel, logXScale, logYScale, xString, yString, deviationString, constrains, 0.01, 1)