import _PLOT
from Utils import transpose

import os
import csv

# transpose.transposeFiles()
from _PARAMS import PARAMETERS

figEndName = "-AllNCS"

xlabel = 'Number Of Agents (#)'
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



xString = "nbAgents_Average"
PARAMETERS.nbAgents = (0, 10000)


logXScale = False
logYScale = False

yStringLong =yStrings[0] + "_"

XYDevMinMax = []
for y,yDev,min,max in zip(yStringsAvg, yStringsDev, yStringsMin, yStringsMax):
    XYDevMinMax.append([xString, y, yDev, min, max])


figName = "sca__" + yStringLong + str(PARAMETERS.nbAgents) + "_DepOn_" + xString + "-" + PARAMETERS.getFigName() + figEndName
print(figName)

PARAMETERS.dimension = "10"
constrains = PARAMETERS.getConstainsSingle(XYDevMinMax)

PARAMETERS.dimension = "5"
constrains += PARAMETERS.getConstainsSingle(XYDevMinMax)

PARAMETERS.dimension = "3"
constrains += PARAMETERS.getConstainsSingle(XYDevMinMax)

PARAMETERS.dimension = "2"
constrains += PARAMETERS.getConstainsSingle(XYDevMinMax)

labelStrings = [r'$n = 2$',r'$n = 3$',r'$n = 5$',r'$n = 10$']

PARAMETERS.colors.reverse()
PARAMETERS.intervalColors.reverse()
labelStrings.reverse()


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
