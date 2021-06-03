import _PLOT
from Utils import transpose

import os
import csv

# transpose.transposeFiles()
from _paramsManager import PARAMETERS

figEndName = "-AllNCS"

xlabel = 'Learning Cycles (#)'
ylabel = 'Volumes (%)'


yStrings = ["voidVol","concurrenceVol","conflictVol"]
yStringsAvg = []
yStringsDev = []
yStringsMin = []
yStringsMax = []
for string in yStrings:
    yStringsAvg.append(string+"_Average")
    yStringsDev.append(string+"_Deviation")
    yStringsMin.append(string+"_Min")
    yStringsMax.append(string+"_Max")

labelStrings = ["Incompetencies","Concurrencies","Conflicts"]

xString = "learningCycles"
PARAMETERS.learningCycles = (0, 1000)


logXScale = False
logYScale = False

yStringLong =""
for label in labelStrings:
    yStringLong += label  + "_"

XYDevMinMax = []
for y,yDev,min,max in zip(yStringsAvg, yStringsDev, yStringsMin, yStringsMax):
    XYDevMinMax.append([xString, y, yDev, min, max])

figName = PARAMETERS.figPrefix + yStringLong + "_DepOn_" + xString + "-" + PARAMETERS.getFigName() + figEndName
print(figName)


constrains = PARAMETERS.getConstainsLabelsAreYStrings(labelStrings, XYDevMinMax)
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
