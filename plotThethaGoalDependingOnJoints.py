import Plot
from Utils import transpose

import os
import csv

#transpose.transposeFiles()

learningCycles = "200"
exploitationCycles = "50"
precisionRange = "0.04"
episodes = "15"
controlCycles = "###"
isOrientationGoal = "true"
isLearnFromNeighbors = "true"

figParamsString = "Rg_" +  precisionRange + "_Lrn_" + learningCycles +"_Exp_" + exploitationCycles + "_Eps_" + episodes + "_Ctrl_" +  controlCycles + "_Ori_" + isOrientationGoal + "_Endo_" + isLearnFromNeighbors

figVaryingParamString = "controlCycles"
labels = ['1','5','10','20']
colors = ['tab:red', 'tab:blue', 'tab:green', 'tab:orange']
markers = ['o','D','v','s']
#figVaryingParamString = "precisionRange"
# labels = ['0.02','0.04','0.06']
# colors = ['tab:red', 'tab:blue', 'tab:green']
# markers = ['o','D','v']
#figVaryingParamString = "isLearnFromNeighbors"
# labels = ['With Endogenous Learning', 'Without Endogenous Learning']
# colors = ['tab:red', 'tab:blue']
# markers = ['o','D']
#figVaryingParamString = "isOrientationGoal"
# labels = ['With Orientation Goal', 'Without Orientation Goal']
# colors = ['tab:red', 'tab:blue']
# markers = ['o','D']
figName = "ThetaGoal-Across_" + figVaryingParamString +"_"+figParamsString
xlabel = 'Joints (#)'
ylabel = 'Mean Error from Goal (%)'
logScale = True
xString = "joints"
yString = "goalThetaErrorAverage"
deviationString = "goalThetaErrorDeviationAverage"

constrains = [{"precisionRange": precisionRange, "learningCycles": learningCycles, "exploitatingCycles": exploitationCycles, "episodes": episodes, "isOrientationGoal": isOrientationGoal, "requestControlCycles": "1", "isLearnFromNeighbors": isLearnFromNeighbors},
              {"precisionRange": precisionRange, "learningCycles": learningCycles, "exploitatingCycles": exploitationCycles, "episodes": episodes, "isOrientationGoal": isOrientationGoal, "requestControlCycles": "5", "isLearnFromNeighbors": isLearnFromNeighbors},
              {"precisionRange": precisionRange, "learningCycles": learningCycles, "exploitatingCycles": exploitationCycles, "episodes": episodes, "isOrientationGoal": isOrientationGoal, "requestControlCycles": "10", "isLearnFromNeighbors": isLearnFromNeighbors},
              {"precisionRange": precisionRange, "learningCycles": learningCycles, "exploitatingCycles": exploitationCycles, "episodes": episodes, "isOrientationGoal": isOrientationGoal, "requestControlCycles": "20", "isLearnFromNeighbors": isLearnFromNeighbors}
              ]



Plot.plotWithDeviation(labels, colors, markers, figName, xlabel, ylabel, logScale, xString, yString, deviationString, constrains)