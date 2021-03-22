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



figVaryingParamString = "learningCycles"
# varyingParamStringValues = ["75","150","250","500"]
# varyingParamStringValues = ["50","75","150"]
varyingParamStringValues = ["200"]
varyingParamStrings = []
paramlabelString = r'$\mathcal{L}^N = $'
PARAMETERS.learningCycles= "("
for value in varyingParamStringValues:
    # precisionRange+=  str(int(100*float(label))) + "_"
    # labelStrings.append(labelString + str(int(100*float(label))) + " %")
    PARAMETERS.learningCycles += value + "_"
    varyingParamStrings.append(paramlabelString + value)

PARAMETERS.learningCycles += ")"

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




figName = "few_2Mod_" + "_" + yStringLong + "-" + PARAMETERS.getFigName() + figEndName
print(figName)

constrains = []


PARAMETERS.isActiveLearning = "false"
PARAMETERS.isSelfLearning = "true"

PARAMETERS.model = "gaussianCos2"
PARAMETERS.errorMargin = "1.0"

PARAMETERS.isLearnFromNeighbors = "false"
PARAMETERS.isCreationFromNeighbor = "false"

PARAMETERS.isModelNCS = "true"
PARAMETERS.isConflictNCS = "false"
PARAMETERS.isConcurenceNCS = "false"
PARAMETERS.isIncompetenceNCS = "false"
PARAMETERS.isFusionResolution = "false"
PARAMETERS.isRetructureResolution = "false"
PARAMETERS.isAmbiguityNCS = "false"


for varyingValue in varyingParamStringValues:
    constrains.append(PARAMETERS.getConstainsLabelsAreParamsWithVaryingParam(xLabelStrings,figVaryingParamString, XYDevMinMax,varyingValue))


PARAMETERS.isLearnFromNeighbors = "true"
PARAMETERS.isCreationFromNeighbor = "true"

PARAMETERS.isModelNCS = "true"
PARAMETERS.isConflictNCS = "true"
PARAMETERS.isConcurenceNCS = "true"
PARAMETERS.isIncompetenceNCS = "false"
PARAMETERS.isFusionResolution = "true"
PARAMETERS.isRetructureResolution = "true"
PARAMETERS.isAmbiguityNCS = "true"

for varyingValue in varyingParamStringValues:
    constrains.append(PARAMETERS.getConstainsLabelsAreParamsWithVaryingParam(xLabelStrings,figVaryingParamString, XYDevMinMax,varyingValue))


PARAMETERS.model = "cosSinX" # "cosSinX"
PARAMETERS.errorMargin = "0.05" # "0.05"

PARAMETERS.isLearnFromNeighbors = "false"
PARAMETERS.isCreationFromNeighbor = "false"

PARAMETERS.isModelNCS = "true"
PARAMETERS.isConflictNCS = "false"
PARAMETERS.isConcurenceNCS = "false"
PARAMETERS.isIncompetenceNCS = "false"
PARAMETERS.isFusionResolution = "false"
PARAMETERS.isRetructureResolution = "false"
PARAMETERS.isAmbiguityNCS = "false"

for varyingValue in varyingParamStringValues:
    constrains.append(PARAMETERS.getConstainsLabelsAreParamsWithVaryingParam(xLabelStrings,figVaryingParamString, XYDevMinMax,varyingValue))



PARAMETERS.isLearnFromNeighbors = "true"
PARAMETERS.isCreationFromNeighbor = "true"

PARAMETERS.isModelNCS = "true"
PARAMETERS.isConflictNCS = "true"
PARAMETERS.isConcurenceNCS = "true"
PARAMETERS.isIncompetenceNCS = "false"
PARAMETERS.isFusionResolution = "true"
PARAMETERS.isRetructureResolution = "true"
PARAMETERS.isAmbiguityNCS = "true"



for varyingValue in varyingParamStringValues:
    constrains.append(PARAMETERS.getConstainsLabelsAreParamsWithVaryingParam(xLabelStrings,figVaryingParamString, XYDevMinMax,varyingValue))


# varyingParamStrings = ["Active Learning","Active Cooperative Learning","Self-Learning"]
varyingParamStringsFinal=["NLC Naive","NLC SL","NLD Naive","NLD SL"]
# for lbl in varyingParamStrings:
#     varyingParamStringsFinal.append("NLC naive "+lbl)
# for lbl in varyingParamStrings:
#     varyingParamStringsFinal.append("NLC SL "+lbl)
# for lbl in varyingParamStrings:
#     varyingParamStringsFinal.append("NLD naive "+lbl)
# for lbl in varyingParamStrings:
#     varyingParamStringsFinal.append("NLD SL "+lbl)

PLOTTING.LEGEND_IN=False
PLOTTING.LEGEND_OUT=False

_PLOT.barWithDeviationConstrained(xLabelStrings, varyingParamStringsFinal, PARAMETERS.colors, PARAMETERS.intervalColors, PARAMETERS.markers,
                                  figName, ylabel, False, logYScale,
                                  constrains, 1, 100, PARAMETERS.figSize)

_PLOT.barWithDeviationConstrained(xLabelStrings, varyingParamStringsFinal, PARAMETERS.colors, PARAMETERS.intervalColors, PARAMETERS.markers,
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
