import _PLOT
from Utils import transpose

import os
import csv

# transpose.transposeFiles()
from _PARAMS import PARAMETERS

figEndName = "-TEST"
# figVaryingParamString = "learningCycles"
# labels = ["250","500","1000","2000","5000","10000","20000"]
# figVaryingParamString = "dimension"
# labels = ["2"]
# figVaryingParamString = "precisionRange"
# labels = ["0.04","0.06","0.08","0.1"]
figVaryingParamString = "dimension"
labels = ["2","3"]

labelString = " dimensions"
dimension = "#"
labelStrings = []

PARAMETERS.dimension="#"
for label in labels:
    # precisionRange+=  str(int(100*float(label))) + "_"
    # labelStrings.append(labelString + str(int(100*float(label))) + " %")
    PARAMETERS.dimension += label + "_"
    labelStrings.append(label + labelString)

xlabel = 'Learning Cycles'
ylabel = 'Volume of Agents (%)'

xString = "learningCycles"
PARAMETERS.learningCycles = (0, 10000)

yString = "mappingScore_Average"

deviationString = "mappingScore_Deviation"
minString = "mappingScore_Min"
maxString = "mappingScore_Max"

logXScale = False
logYScale = False



figName = PARAMETERS.figPrefix + yString + "_DepOn_" + xString + "-" + PARAMETERS.getFigName() + figEndName
print(figName)


constrains = PARAMETERS.getConstainsLabelsAreParams(labels, figVaryingParamString, [xString, yString, deviationString, minString, maxString])
print(constrains)


_PLOT.plotWithDeviationWithFillBetweenConstrained(labelStrings, PARAMETERS.colors, PARAMETERS.intervalColors, PARAMETERS.markers,
                                       figName, xlabel, ylabel, False, logYScale,
                                       constrains, 1, 100, PARAMETERS.figSize)
_PLOT.plotWitMinMaxWithFillBetweenConstrained(labelStrings, PARAMETERS.colors, PARAMETERS.intervalColors, PARAMETERS.markers,
                                   figName, xlabel, ylabel, False, logYScale,
                                   constrains, 1, 100, PARAMETERS.figSize)
_PLOT.plotWithDeviationWithFillBetweenConstrained(labelStrings, PARAMETERS.colors, PARAMETERS.intervalColors, PARAMETERS.markers,
                                       figName, xlabel, ylabel, True, logYScale,
                                       constrains, 1, 100, PARAMETERS.figSize)
_PLOT.plotWitMinMaxWithFillBetweenConstrained(labelStrings, PARAMETERS.colors, PARAMETERS.intervalColors, PARAMETERS.markers,
                                   figName, xlabel, ylabel, True, logYScale,
                                   constrains, 1, 100, PARAMETERS.figSize)

# _PLOT.plotWithDeviation(labels, colors, markers, figName, xlabel, ylabel, logXScale, logYScale, xString, yString, deviationString, constrains, 1, 1)
