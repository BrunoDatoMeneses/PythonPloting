import _PLOT
from Utils import transpose

import os
import csv

# transpose.transposeFiles()
from _FIG import PLOTTING
from _paramsManager import PARAMETERS

figEndName = "-AllNCS"

#xlabel = 'Learning Cycles (#)'
ylabel = 'Generalization Score (%)'
yStringLong ="generalizationScore"



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
yStrings = ["generalizationScore"]
# yStrings = ["mappingScore","imprecisionScore","conflictVol","concurrenceVol","voidVol"]
yStringsAvg = []
yStringsDev = []
yStringsMin = []
yStringsMax = []
for string in yStrings:
    yStringsAvg.append(string+"_Average")
    yStringsDev.append(string+"_Deviation")
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

varyingParamStrings = ["Active Learning","Active Learning","Active Learning","Active Learning","Self-Learning","Self-Learning","Self-Learning","Self-Learning"]


figName = "weight_3Strat_" + PARAMETERS.noise + "_" + yStringLong + "-" + PARAMETERS.getFigName() + figEndName
print(figName)

constrains = []

PARAMETERS.isActiveLearning = "true"
PARAMETERS.isSelfLearning = "false"
PARAMETERS.isLearnFromNeighbors = "false"

PARAMETERS.LEARNING_WEIGHT_ACCURACY = "1.0"
PARAMETERS.LEARNING_WEIGHT_EXPERIENCE = "1.0"
PARAMETERS.LEARNING_WEIGHT_GENERALIZATION = "1.0"

PARAMETERS.EXPLOITATION_WEIGHT_PROXIMITY = "1.0"
PARAMETERS.EXPLOITATION_WEIGHT_EXPERIENCE = "1.0"
PARAMETERS.EXPLOITATION_WEIGHT_GENERALIZATION = "1.0"

constrains.append(PARAMETERS.getConstainsLabelsAreYStrings(xLabelStrings, XYDevMinMax))

PARAMETERS.LEARNING_WEIGHT_ACCURACY = "1.0"
PARAMETERS.LEARNING_WEIGHT_EXPERIENCE = "0.5"
PARAMETERS.LEARNING_WEIGHT_GENERALIZATION = "0.5"

PARAMETERS.EXPLOITATION_WEIGHT_PROXIMITY = "1.0"
PARAMETERS.EXPLOITATION_WEIGHT_EXPERIENCE = "0.5"
PARAMETERS.EXPLOITATION_WEIGHT_GENERALIZATION = "0.5"

constrains.append(PARAMETERS.getConstainsLabelsAreYStrings(xLabelStrings, XYDevMinMax))

PARAMETERS.LEARNING_WEIGHT_ACCURACY = "0.5"
PARAMETERS.LEARNING_WEIGHT_EXPERIENCE = "1.0"
PARAMETERS.LEARNING_WEIGHT_GENERALIZATION = "0.5"

PARAMETERS.EXPLOITATION_WEIGHT_PROXIMITY = "0.5"
PARAMETERS.EXPLOITATION_WEIGHT_EXPERIENCE = "1.0"
PARAMETERS.EXPLOITATION_WEIGHT_GENERALIZATION = "0.5"

constrains.append(PARAMETERS.getConstainsLabelsAreYStrings(xLabelStrings, XYDevMinMax))

PARAMETERS.LEARNING_WEIGHT_ACCURACY = "0.5"
PARAMETERS.LEARNING_WEIGHT_EXPERIENCE = "0.5"
PARAMETERS.LEARNING_WEIGHT_GENERALIZATION = "1.0"

PARAMETERS.EXPLOITATION_WEIGHT_PROXIMITY = "0.5"
PARAMETERS.EXPLOITATION_WEIGHT_EXPERIENCE = "0.5"
PARAMETERS.EXPLOITATION_WEIGHT_GENERALIZATION = "1.0"

constrains.append(PARAMETERS.getConstainsLabelsAreYStrings(xLabelStrings, XYDevMinMax))



PARAMETERS.isActiveLearning = "false"
PARAMETERS.isSelfLearning = "true"
PARAMETERS.isLearnFromNeighbors = "true"

PARAMETERS.LEARNING_WEIGHT_ACCURACY = "1.0"
PARAMETERS.LEARNING_WEIGHT_EXPERIENCE = "1.0"
PARAMETERS.LEARNING_WEIGHT_GENERALIZATION = "1.0"

PARAMETERS.EXPLOITATION_WEIGHT_PROXIMITY = "1.0"
PARAMETERS.EXPLOITATION_WEIGHT_EXPERIENCE = "1.0"
PARAMETERS.EXPLOITATION_WEIGHT_GENERALIZATION = "1.0"

constrains.append(PARAMETERS.getConstainsLabelsAreYStrings(xLabelStrings, XYDevMinMax))

PARAMETERS.LEARNING_WEIGHT_ACCURACY = "1.0"
PARAMETERS.LEARNING_WEIGHT_EXPERIENCE = "0.5"
PARAMETERS.LEARNING_WEIGHT_GENERALIZATION = "0.5"

PARAMETERS.EXPLOITATION_WEIGHT_PROXIMITY = "1.0"
PARAMETERS.EXPLOITATION_WEIGHT_EXPERIENCE = "0.5"
PARAMETERS.EXPLOITATION_WEIGHT_GENERALIZATION = "0.5"

constrains.append(PARAMETERS.getConstainsLabelsAreYStrings(xLabelStrings, XYDevMinMax))

PARAMETERS.LEARNING_WEIGHT_ACCURACY = "0.5"
PARAMETERS.LEARNING_WEIGHT_EXPERIENCE = "1.0"
PARAMETERS.LEARNING_WEIGHT_GENERALIZATION = "0.5"

PARAMETERS.EXPLOITATION_WEIGHT_PROXIMITY = "0.5"
PARAMETERS.EXPLOITATION_WEIGHT_EXPERIENCE = "1.0"
PARAMETERS.EXPLOITATION_WEIGHT_GENERALIZATION = "0.5"

constrains.append(PARAMETERS.getConstainsLabelsAreYStrings(xLabelStrings, XYDevMinMax))

PARAMETERS.LEARNING_WEIGHT_ACCURACY = "0.5"
PARAMETERS.LEARNING_WEIGHT_EXPERIENCE = "0.5"
PARAMETERS.LEARNING_WEIGHT_GENERALIZATION = "1.0"

PARAMETERS.EXPLOITATION_WEIGHT_PROXIMITY = "0.5"
PARAMETERS.EXPLOITATION_WEIGHT_EXPERIENCE = "0.5"
PARAMETERS.EXPLOITATION_WEIGHT_GENERALIZATION = "1.0"

constrains.append(PARAMETERS.getConstainsLabelsAreYStrings(xLabelStrings, XYDevMinMax))

PLOTTING.LEGEND_IN=False
PLOTTING.LEGEND_OUT=True

PLOTTING.ROTATION = 22.5


_PLOT.barWithDeviationConstrained(xLabelStrings, varyingParamStrings, PARAMETERS.colors, PARAMETERS.intervalColors, PARAMETERS.markers,
                                  figName, ylabel, False, logYScale,
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
