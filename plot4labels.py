import Plot
from Utils import transpose

import os
import csv

transpose.transposeFiles()

learningCycles = "200"
exploitationCycles = "50"
precisionRange = "0.02"
episodes = "15"
controlCycles = "###"
isOrientationGoal = "true"
isLearnFromNeighbors = "true"

figParamsString = "Rg_" +  precisionRange + "_Lrn_" + learningCycles +"_Exp_" + exploitationCycles + "_Eps_" + episodes + "_Ctrl_" +  controlCycles + "_Ori_" + isOrientationGoal + "_Endo_" + isLearnFromNeighbors
figVaryingParamString = "controlCycles"


labels = ['1','5','10','20']
colors = ['tab:red', 'tab:blue', 'tab:green', 'tab:orange']
markers = ['o','D','v','s']
figName = "TimeAcross_" + figVaryingParamString +"_"+figParamsString
xlabel = 'Joints (#)'
ylabel = 'Mean Execution (s)'
logScale = True
xString = "joints"
yString = "meanTime"
deviationString = "meanTime"

constrains = [{"precisionRange": precisionRange, "learningCycles": learningCycles, "exploitatingCycles": exploitationCycles, "episodes": episodes, "isOrientationGoal": isOrientationGoal, "requestControlCycles": controlCycles, "isLearnFromNeighbors": isLearnFromNeighbors},
              {"precisionRange": precisionRange, "learningCycles": learningCycles, "exploitatingCycles": exploitationCycles, "episodes": episodes, "isOrientationGoal": isOrientationGoal, "requestControlCycles": controlCycles, "isLearnFromNeighbors": isLearnFromNeighbors},
              {"precisionRange": precisionRange, "learningCycles": learningCycles, "exploitatingCycles": exploitationCycles, "episodes": episodes, "isOrientationGoal": isOrientationGoal, "requestControlCycles": controlCycles, "isLearnFromNeighbors": isLearnFromNeighbors},
              {"precisionRange": precisionRange, "learningCycles": learningCycles, "exploitatingCycles": exploitationCycles, "episodes": episodes, "isOrientationGoal": isOrientationGoal, "requestControlCycles": controlCycles, "isLearnFromNeighbors": isLearnFromNeighbors}
              ]



Plot.plot(labels, colors, markers, figName, xlabel, ylabel, logScale, xString, yString, deviationString, constrains)