import _PLOT
from Utils import transpose

import os
import csv

# transpose.transposeFiles()
from _paramsManager import PARAMETERS

figEndName = "-AllNCS"

xlabel = 'Perceptions (#)'
ylabel = 'Episode Execution Time (s)'



yStrings = ["meanTime"]
yStringsAvg = []
yStringsDev = []
yStringsMin = []
yStringsMax = []
for string in yStrings:
    yStringsAvg.append(string)
    yStringsDev.append(string)
    yStringsMin.append(string)
    yStringsMax.append(string)



xString = "dimension"
PARAMETERS.dimension = (0, 10)


logXScale = False
logYScale = False

yStringLong =yStrings[0] + "_VarLrn"

XYDevMinMax = []
for y,yDev,min,max in zip(yStringsAvg, yStringsDev, yStringsMin, yStringsMax):
    XYDevMinMax.append([xString, y, yDev, min, max])


figName = "sca__" + yStringLong  + "_DepOn_" + xString + "-" + PARAMETERS.getFigName() + figEndName
print(figName)

PARAMETERS.learningCycles = "500"
constrains = PARAMETERS.getConstainsSingle(XYDevMinMax)

PARAMETERS.learningCycles = "2000"
constrains += PARAMETERS.getConstainsSingle(XYDevMinMax)

PARAMETERS.learningCycles = "10000"
constrains += PARAMETERS.getConstainsSingle(XYDevMinMax)



labelStrings = [r'$\mathcal{L}^N = 500$',r'$\mathcal{L}^N = 2000$',r'$\mathcal{L}^N = 10000$']

# PARAMETERS.colors.reverse()
# PARAMETERS.intervalColors.reverse()
# labelStrings.reverse()


_PLOT.plotSimple(labelStrings, PARAMETERS.colors, PARAMETERS.intervalColors, PARAMETERS.markers,
                                       figName, xlabel, ylabel, False, False,
                                       constrains, 1, 1, PARAMETERS.figSize)
# _PLOT.plotWitMinMaxWithFillBetweenConstrained(labelStrings, PARAMETERS.colors, PARAMETERS.intervalColors, PARAMETERS.markers,
#                                    figName, xlabel, ylabel, False, logYScale,
#                                    constrains, 1, 1, PARAMETERS.figSize)
#
#
# _PLOT.plotWithDeviationWithFillBetweenConstrained(labelStrings, PARAMETERS.colors, PARAMETERS.intervalColors, PARAMETERS.markers,
#                                        figName, xlabel, ylabel, True, logYScale,
#                                        constrains, 1, 1, PARAMETERS.figSize)
#
# _PLOT.plotWithDeviationWithFillBetweenConstrained(labelStrings, PARAMETERS.colors, PARAMETERS.intervalColors, PARAMETERS.markers,
#                                        figName, xlabel, ylabel, True, True,
#                                        constrains, 1, 1, PARAMETERS.figSize)
#
# _PLOT.plotWithDeviationWithFillBetweenConstrained(labelStrings, PARAMETERS.colors, PARAMETERS.intervalColors, PARAMETERS.markers,
#                                        figName, xlabel, ylabel, False, True,
#                                        constrains, 1, 1, PARAMETERS.figSize)
#
# _PLOT.plotWitMinMaxWithFillBetweenConstrained(labelStrings, PARAMETERS.colors, PARAMETERS.intervalColors, PARAMETERS.markers,
#                                    figName, xlabel, ylabel, True, logYScale,
#                                    constrains, 1, 1, PARAMETERS.figSize)
#
# _PLOT.plotWitMinMaxWithFillBetweenConstrained(labelStrings, PARAMETERS.colors, PARAMETERS.intervalColors, PARAMETERS.markers,
#                                    figName, xlabel, ylabel, True, True,
#                                    constrains, 1, 1, PARAMETERS.figSize)
#
# _PLOT.plotWitMinMaxWithFillBetweenConstrained(labelStrings, PARAMETERS.colors, PARAMETERS.intervalColors, PARAMETERS.markers,
#                                    figName, xlabel, ylabel, False, True,
#                                    constrains, 1, 1, PARAMETERS.figSize)

# _PLOT.plotWithDeviation(labels, colors, markers, figName, xlabel, ylabel, logXScale, logYScale, xString, yString, deviationString, constrains, 1, 1)
