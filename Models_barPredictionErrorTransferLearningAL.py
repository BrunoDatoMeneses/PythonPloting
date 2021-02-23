import _PLOT
from Utils import transpose

import os
import csv

# transpose.transposeFiles()
from _FIG import PLOTTING
from _PARAMS import PARAMETERS

figEndName = "-AllNCS"

#xlabel = 'Learning Cycles (#)'
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
PARAMETERS.figSize = (2.5, 3.75)
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

figName = "transfer_" + yStringLong + "-" + PARAMETERS.getFigName() + figEndName
print(figName)

constrains = []
varyingParamStrings = ["Rhombus","Disc","Square","Square, Disc","Square, Disc, Rhombus"]
listOfModels = ["los", "disc", "squareFixed", "squareDisc", "squareDiscLos"]
listOfLearningCycles = ["2000", "2000", "2000", "3500", "5000"]
# listOfLearningCycles = ["1000", "1000", "1000", "1750", "2500"]

for mod,cycl in zip(listOfModels,listOfLearningCycles):
    PARAMETERS.model = mod
    PARAMETERS.learningCycles = cycl
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
