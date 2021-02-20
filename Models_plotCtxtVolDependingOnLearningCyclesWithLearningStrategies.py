import _PLOT
from Utils import transpose

import os
import csv

# transpose.transposeFiles()
from _PARAMS import PARAMETERS

figEndName = "-AllNCS"

xlabel = 'Learning Cycles (#)'
ylabel = 'Agents Volume (%)'


yStrings = ["mappingScore"]
yStringsAvg = []
yStringsDev = []
yStringsMin = []
yStringsMax = []
for string in yStrings:
    yStringsAvg.append(string+"_Average")
    yStringsDev.append(string+"_Deviation")
    yStringsMin.append(string+"_Min")
    yStringsMax.append(string+"_Max")

labelStrings = ["Active Learning","Self-Learning"]

xString = "learningCycles"
PARAMETERS.learningCycles = (0, 2000)


logXScale = False
logYScale = False

yStringLong =yStrings[0] + "_"
for label in labelStrings:
    yStringLong += label  + "_"

XYDevMinMax = []
for y,yDev,min,max in zip(yStringsAvg, yStringsDev, yStringsMin, yStringsMax):
    XYDevMinMax.append([xString, y, yDev, min, max])

figName = PARAMETERS.figPrefix + yStringLong + "_DepOn_" + xString + "-" + PARAMETERS.getFigName() + figEndName
print(figName)


constrains = PARAMETERS.getConstainsSingle(XYDevMinMax)
PARAMETERS.isActiveLearning = "false"
PARAMETERS.isSelfLearning = "true"
PARAMETERS.isLearnFromNeighbors = "true"
constrains+=PARAMETERS.getConstainsSingle(XYDevMinMax)

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
