import _FIG
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
figVaryingParamString = "validityRangesPrecision"
labels = ["0.05","0.075","0.1"]


labelString = "Validity Ranges Precision "
labelStrings = []

PARAMETERS.validityRangesPrecision="("
for label in labels:
    # precisionRange+=  str(int(100*float(label))) + "_"
    # labelStrings.append(labelString + str(int(100*float(label))) + " %")
    PARAMETERS.validityRangesPrecision += label + "_"
    labelStrings.append(labelString + label)

PARAMETERS.validityRangesPrecision+=")"

xlabel = 'Learning Cycles (#)'
ylabel = 'Prediction Error (%)'

xString = "learningCycles"
PARAMETERS.learningCycles = (0, 1000)

yString = "predictionError_Average"

deviationString = "predictionErrorDeviation_Average"
minString = "predictionError_Min"
maxString = "predictionError_Max"

logXScale = False
logYScale = False



figName = PARAMETERS.figPrefix + yString + "_DepOn_" + xString + "-" + PARAMETERS.getFigName() + figEndName
print(figName)
figName= _FIG.formatFigName(figName)
print(figName)

constrains = PARAMETERS.getConstains(labels, figVaryingParamString)

PARAMETERS.colors = PARAMETERS.colors[:3]
PARAMETERS.colors.reverse()
PARAMETERS.intervalColors = PARAMETERS.intervalColors[:3]
PARAMETERS.intervalColors.reverse()

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
