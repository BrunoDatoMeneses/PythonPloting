import _PLOT
from Utils import transpose

import os
import csv

# transpose.transposeFiles()
from _PARAMS import PARAMETERS

figEndName = "-allNCS"
# figVaryingParamString = "learningCycles"
# labels = ["250","500","1000","2000","5000","10000","20000"]
# figVaryingParamString = "dimension"
# labels = ["2"]
# figVaryingParamString = "precisionRange"
# labels = ["0.04","0.06","0.08","0.1"]
figVaryingParamString = "learningCycles"
labels = ["500"]

labelString = " Learning Cycles"
labelStrings = []

PARAMETERS.learningCycles="#"
for label in labels:
    # precisionRange+=  str(int(100*float(label))) + "_"
    # labelStrings.append(labelString + str(int(100*float(label))) + " %")
    PARAMETERS.learningCycles += label + "_"
    labelStrings.append(label + labelString)

xlabel = 'Episodes'
ylabel = 'Number of Agents (#)'

xString = "episodes"
PARAMETERS.episodes = (0, 1000)

yString = "nbAgents_Average"

deviationString = "nbAgents_Deviation"
minString = "nbAgents_Min"
maxString = "nbAgents_Max"

logXScale = False
logYScale = False



figName = PARAMETERS.figPrefix + yString + "_DepOn_" + xString + "-" + PARAMETERS.getFigName() + figEndName
print(figName)


constrains = PARAMETERS.getConstains(labels, figVaryingParamString)

_PLOT.plotWithDeviationWithFillBetween(labelStrings, PARAMETERS.colors, PARAMETERS.intervalColors, PARAMETERS.markers,
                                       figName, xlabel, ylabel, False, logYScale, xString, yString, deviationString,
                                       constrains, 1, 100, PARAMETERS.figSize)
_PLOT.plotWitMinMaxWithFillBetween(labelStrings, PARAMETERS.colors, PARAMETERS.intervalColors, PARAMETERS.markers,
                                   figName, xlabel, ylabel, False, logYScale, xString, yString, minString, maxString,
                                   constrains, 1, 100, PARAMETERS.figSize)
_PLOT.plotWithDeviationWithFillBetween(labelStrings, PARAMETERS.colors, PARAMETERS.intervalColors, PARAMETERS.markers,
                                       figName, xlabel, ylabel, True, logYScale, xString, yString, deviationString,
                                       constrains, 1, 100, PARAMETERS.figSize)
_PLOT.plotWitMinMaxWithFillBetween(labelStrings, PARAMETERS.colors, PARAMETERS.intervalColors, PARAMETERS.markers,
                                   figName, xlabel, ylabel, True, logYScale, xString, yString, minString, maxString,
                                   constrains, 1, 100, PARAMETERS.figSize)

# _PLOT.plotWithDeviation(labels, colors, markers, figName, xlabel, ylabel, logXScale, logYScale, xString, yString, deviationString, constrains, 1, 1)
