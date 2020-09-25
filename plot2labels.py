import Plot
from Utils import transpose

import os
import csv

transpose.transposeFiles()

learningCycles = "200"
exploitationCycles = "50"
precisionRange = "0.02"
episodes = "15"
controlCycles = "1"
isOrientationGoal = "true"
isLearnFromNeighbors = "###"

figParamsString = "Rg_" +  precisionRange + "_Lrn_" + learningCycles +"_Exp_" + exploitationCycles + "_Eps_" + episodes + "_Ctrl_" +  controlCycles + "_Ori_" + isOrientationGoal + "_Endo_" + isLearnFromNeighbors
figVaryingParamString = "isLearnFromNeighbors"


labels = ['With Endogenous Learning', 'Without Endogenous Learning']
colors = ['tab:red', 'tab:blue']
markers = ['o','D']
figName = "XYGoalAcross_" + figVaryingParamString +"_"+figParamsString
xlabel = 'Joints (#)'
ylabel = 'Mean Error from Goal (%)'
logScale = True
xString = "joints"
yString = "goalXYErrorAverage"
deviationString = "goalXYErrorDeviationAverage"

constrains = [{"precisionRange": precisionRange, "learningCycles": learningCycles, "exploitatingCycles": exploitationCycles, "episodes": episodes, "isOrientationGoal": isOrientationGoal, "requestControlCycles": controlCycles, "isLearnFromNeighbors": isLearnFromNeighbors},
              {"precisionRange": precisionRange, "learningCycles": learningCycles, "exploitatingCycles": exploitationCycles, "episodes": episodes, "isOrientationGoal": isOrientationGoal, "requestControlCycles": controlCycles, "isLearnFromNeighbors": isLearnFromNeighbors}]



Plot.plotWithDeviation(labels, colors, markers, figName, xlabel, ylabel, logScale, xString, yString, deviationString, constrains)
#Plot.plot(labels, colors, markers, figName, xlabel, ylabel, logScale, xString, yString, deviationString, constrains)