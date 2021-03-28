import _PLOT
from Utils import transpose

import os
import csv

# transpose.transposeFiles()
from _FIG import PLOTTING
from _PARAMS import PARAMETERS

figEndName = "-AllNCS"


ylabel = 'Prediction Error (%)'
yStringLong ="predictionError"

varyingParamStrings = ["Active Learning","Self-Learning"]

# figVaryingParamString = "learningCycles"
# varyingParamStringValues = ["500","1000","1500","2000"]
# varyingParamStrings = []
# paramlabelString = " Learning Cycles"
# PARAMETERS.learningCycles= "("
# for value in varyingParamStringValues:
#     # precisionRange+=  str(int(100*float(label))) + "_"
#     # labelStrings.append(labelString + str(int(100*float(label))) + " %")
#     PARAMETERS.learningCycles += value + "_"
#     varyingParamStrings.append(value + paramlabelString)
#
# PARAMETERS.learningCycles += ")"
PARAMETERS.figSize = (1.5, 3.75)
yStrings = ["predictionError"]
# yStrings = ["mappingScore","imprecisionScore","conflictVol","concurrenceVol","voidVol"]
yStringsAvg = []
yStringsDev = []
yStringsMin = []
yStringsMax = []
for string in yStrings:
    yStringsAvg.append(string+"_Average")
    yStringsDev.append(string+"Deviation_Average")
    yStringsMin.append(string+"_Min")
    yStringsMax.append(string+"_Max")

xLabelStrings = [""]
# xLabelStrings = ["Agents", "Innacuracies", "Conflicts", "Concurrencies", "Incompetencies"]




logXScale = False
logYScale = False


# for label in labelStrings:
#     yStringLong += label  + "_"

XYDevMinMax = []
for y,yDev,min,max in zip(yStringsAvg, yStringsDev, yStringsMin, yStringsMax):
    XYDevMinMax.append([y, yDev, min, max])

figName = PARAMETERS.figPrefix + yStringLong + "-" + PARAMETERS.getFigName() + figEndName
print(figName)

varyingParamStrings = ["Naive Learning","Active Learning","Self-Learning"]

constrains = []

# NAIVE
PARAMETERS.isActiveLearning = "false"
PARAMETERS.isSelfLearning = "true"
PARAMETERS.isLearnFromNeighbors = "false"

PARAMETERS.isCreationFromNeighbor = "false"

PARAMETERS.isModelNCS = "false"
PARAMETERS.isConflictNCS = "false"
PARAMETERS.isConcurenceNCS = "false"
PARAMETERS.isIncompetenceNCS = "false"
PARAMETERS.isFusionResolution = "false"
PARAMETERS.isRetructureResolution = "false"
PARAMETERS.isAmbiguityNCS = "false"

constrains.append(PARAMETERS.getConstainsLabelsAreYStrings(xLabelStrings, XYDevMinMax))

# ACTIVE
PARAMETERS.isActiveLearning = "true"
PARAMETERS.isSelfLearning = "false"
PARAMETERS.isLearnFromNeighbors = "false"

PARAMETERS.isCreationFromNeighbor = "true"

PARAMETERS.isModelNCS = "true"
PARAMETERS.isConflictNCS = "true"
PARAMETERS.isConcurenceNCS = "true"
PARAMETERS.isIncompetenceNCS = "true"
PARAMETERS.isFusionResolution = "true"
PARAMETERS.isRetructureResolution = "true"
PARAMETERS.isAmbiguityNCS = "true"

constrains.append(PARAMETERS.getConstainsLabelsAreYStrings(xLabelStrings, XYDevMinMax))

# SELF
PARAMETERS.isActiveLearning = "false"
PARAMETERS.isSelfLearning = "true"
PARAMETERS.isLearnFromNeighbors = "true"

PARAMETERS.isCreationFromNeighbor = "true"

PARAMETERS.isModelNCS = "true"
PARAMETERS.isConflictNCS = "true"
PARAMETERS.isConcurenceNCS = "true"
PARAMETERS.isIncompetenceNCS = "true"
PARAMETERS.isFusionResolution = "true"
PARAMETERS.isRetructureResolution = "true"
PARAMETERS.isAmbiguityNCS = "true"

constrains.append(PARAMETERS.getConstainsLabelsAreYStrings(xLabelStrings, XYDevMinMax))


PLOTTING.LEGEND_IN=False

_PLOT.barWithDeviationConstrained(xLabelStrings, varyingParamStrings, PARAMETERS.colors, PARAMETERS.intervalColors, PARAMETERS.markers,
                                  figName, ylabel, False, logYScale,
                                  constrains, 1, 100, PARAMETERS.figSize)

_PLOT.barWithDeviationConstrained(xLabelStrings, varyingParamStrings, PARAMETERS.colors, PARAMETERS.intervalColors, PARAMETERS.markers,
                                  figName, ylabel, False, True,
                                  constrains, 1, 100, PARAMETERS.figSize)

# _PLOT.plotWitMinMaxWithFillBetweenConstrained(labelStrings, PARAMETERS.colors, PARAMETERS.intervalColors, PARAMETERS.markers,
#                                    figName, xlabel, ylabel, False, logYScale,
#                                    constrains, 1, 1, PARAMETERS.figSize)
# _PLOT.plotWithDeviationWithFillBetweenConstrained(labelStrings, PARAMETERS.colors, PARAMETERS.intervalColors, PARAMETERS.markers,
#                                        figName, xlabel, ylabel, True, logYScale,
#                                        constrains, 1, 1, PARAMETERS.figSize)
# _PLOT.plotWitMinMaxWithFillBetweenConstrained(labelStrings, PARAMETERS.colors, PARAMETERS.intervalColors, PARAMETERS.markers,
#                                    figName, xlabel, ylabel, True, logYScale,
#                                    constrains, 1, 1, PARAMETERS.figSize)

# _PLOT.plotWithDeviation(labels, colors, markers, figName, xlabel, ylabel, logXScale, logYScale, xString, yString, deviationString, constrains, 1, 1)
