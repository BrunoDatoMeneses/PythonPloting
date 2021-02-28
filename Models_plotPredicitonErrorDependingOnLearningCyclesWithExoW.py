import _PLOT
from Utils import transpose

import os
import csv

# transpose.transposeFiles()
from _PARAMS import PARAMETERS

figEndName = "-AllNCS"

xlabel = 'Learning Cycles (#)'
ylabel = 'Prediction Error (%)'



yStrings = ["predictionError"]
yStringsAvg = []
yStringsDev = []
yStringsMin = []
yStringsMax = []
for string in yStrings:
    yStringsAvg.append(string+"_Average")
    yStringsDev.append(string+"Deviation_Average")
    yStringsMin.append(string+"_Min")
    yStringsMax.append(string+"_Max")



xString = "learningCycles"
PARAMETERS.learningCycles = (0, 4000)


logXScale = False
logYScale = False

yStringLong =yStrings[0] + "_"

XYDevMinMax = []
for y,yDev,min,max in zip(yStringsAvg, yStringsDev, yStringsMin, yStringsMax):
    XYDevMinMax.append([xString, y, yDev, min, max])

PARAMETERS.validityRangesPrecision = "0.02"
# PARAMETERS.model = "gaussianCos2"
# PARAMETERS.errorMargin = "1.0"
PARAMETERS.model = "cosSinX"
PARAMETERS.errorMargin = "0.05"
figName = "few_2Mod_" + PARAMETERS.model + "_" + yStringLong + "_DepOn_" + xString + "-" + PARAMETERS.getFigName() + figEndName
print(figName)

PARAMETERS.isActiveLearning = "false"
PARAMETERS.isSelfLearning = "true"
PARAMETERS.isLearnFromNeighbors = "true"

PARAMETERS.exogenousLearningWeight = "0.05"

constrains = PARAMETERS.getConstainsSingle(XYDevMinMax)

PARAMETERS.isActiveLearning = "false"
PARAMETERS.isSelfLearning = "true"
PARAMETERS.isLearnFromNeighbors = "true"

PARAMETERS.exogenousLearningWeight = "0.1"

constrains+=PARAMETERS.getConstainsSingle(XYDevMinMax)

PARAMETERS.isActiveLearning = "false"
PARAMETERS.isSelfLearning = "true"
PARAMETERS.isLearnFromNeighbors = "true"

PARAMETERS.exogenousLearningWeight = "0.15"

constrains+=PARAMETERS.getConstainsSingle(XYDevMinMax)

PARAMETERS.isActiveLearning = "false"
PARAMETERS.isSelfLearning = "true"
PARAMETERS.isLearnFromNeighbors = "true"

PARAMETERS.exogenousLearningWeight = "0.2"

constrains+=PARAMETERS.getConstainsSingle(XYDevMinMax)

PARAMETERS.isActiveLearning = "false"
PARAMETERS.isSelfLearning = "true"
PARAMETERS.isLearnFromNeighbors = "true"

PARAMETERS.exogenousLearningWeight = "0.25"

constrains+=PARAMETERS.getConstainsSingle(XYDevMinMax)

labelStrings = [r'$\omega_{lrn}^{exo} = 0.05$',r'$\omega_{lrn}^{exo} = 0.1$',r'$\omega_{lrn}^{exo} = 0.15$',r'$\omega_{lrn}^{exo} = 0.2$',r'$\omega_{lrn}^{exo} = 0.25$']
labelStrings.reverse()
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
