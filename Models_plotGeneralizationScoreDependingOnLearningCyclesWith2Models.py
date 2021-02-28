import _PLOT
from Utils import transpose

import os
import csv

# transpose.transposeFiles()
from _PARAMS import PARAMETERS

figEndName = "-AllNCS"

xlabel = 'Learning Cycles (#)'
ylabel = 'Generalization Score (%)'



yStrings = ["generalizationScore"]
yStringsAvg = []
yStringsDev = []
yStringsMin = []
yStringsMax = []
for string in yStrings:
    yStringsAvg.append(string+"_Average")
    yStringsDev.append(string+"_Deviation")
    yStringsMin.append(string+"_Min")
    yStringsMax.append(string+"_Max")

labelStrings = ["NLC Models","NLD Model"]

xString = "learningCycles"
PARAMETERS.learningCycles = (0, 500)


logXScale = False
logYScale = False

yStringLong = yStrings[0] + "_"
for label in labelStrings:
    yStringLong += label  + "_"

XYDevMinMax = []
for y,yDev,min,max in zip(yStringsAvg, yStringsDev, yStringsMin, yStringsMax):
    XYDevMinMax.append([xString, y, yDev, min, max])

figName = "few_2Mod_" + yStringLong + "_DepOn_" + xString + "-" + PARAMETERS.getFigName() + figEndName
print(figName)

PARAMETERS.isActiveLearning = "false"
PARAMETERS.isSelfLearning = "true"
PARAMETERS.isLearnFromNeighbors = "true"
PARAMETERS.model = "gaussianCos2"
PARAMETERS.errorMargin = "1.0"

constrains = PARAMETERS.getConstainsSingle(XYDevMinMax)

PARAMETERS.isActiveLearning = "false"
PARAMETERS.isSelfLearning = "true"
PARAMETERS.isLearnFromNeighbors = "true"
PARAMETERS.model = "cosSinX" # "cosSinX"
PARAMETERS.errorMargin = "0.05" # "0.05"

constrains+=PARAMETERS.getConstainsSingle(XYDevMinMax)

constrains.reverse()
PARAMETERS.colors.reverse()
PARAMETERS.intervalColors.reverse()
PARAMETERS.markers.reverse()


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
