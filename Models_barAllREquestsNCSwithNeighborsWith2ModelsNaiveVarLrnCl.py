import _PLOT
from Utils import transpose

import os
import csv

# transpose.transposeFiles()
from _FIG import PLOTTING
from _paramsManager import PARAMETERS

figEndName = "-AllNCS"

#xlabel = 'Learning Cycles (#)'
ylabel = 'Situations (#)'
yStringLong ="RequestsAllNCSwithNeighbors"


figVaryingParamString = "learningCycles"
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


yStrings = ["modelRequests","conflictRequests","concurrenceRequests","voidRequests","fusionRequests","restructureRequests","frontierRequests","neighborsRequest"]
# yStrings = ["modelRequests","conflictRequests","concurrenceRequests","voidRequests","fusionRequests","restructureRequests","endogenousLearningSituations"]
# yStrings = ["rdmRequests","activeRequests","selfRequests","modelRequests","conflictRequests","concurrenceRequests","voidRequests","fusionRequests","restructureRequests"]
# yStrings = ["rdmRequests","activeRequests","selfRequests"]
yStringsAvg = []
yStringsDev = []
yStringsMin = []
yStringsMax = []
for string in yStrings:
    yStringsAvg.append(string+"_Average")
    yStringsDev.append(string+"_Deviation")
    yStringsMin.append(string+"_Min")
    yStringsMax.append(string+"_Max")

xLabelStrings = ["Model Amb. /10", "Conflicts", "Concurrencies", "Incompetencies", "Complete Redund.", "Partial Redund.","Range Amb.","Coop. Neighbors"]
# xLabelStrings = ["Model Ambiguities", "Conflicts", "Concurrencies", "Incompetencies", "Complete Redundancy", "Partial Redundancy","Neighbors"]
# xLabelStrings = ["Passive","Active","Self-Generated"]
# xLabelStrings = ["Passive","Active","Self-Generated","Model Ambiguities", "Conflicts", "Concurrencies", "Incompetencies", "Complete Redundancy", "Partial Redundancy"]




logXScale = False
logYScale = False






XYDevMinMax = []
for y,yDev,min,max,yString in zip(yStringsAvg, yStringsDev, yStringsMin, yStringsMax,yStrings):
    if(yString == "modelRequests"):
        XYDevMinMax.append([y, yDev, min, max,0.1])
    else:
        XYDevMinMax.append([y, yDev, min, max, 1])

PARAMETERS.figSize = (12, 3.75)

figName = "few_2Mod_" + "_" + yStringLong + "-" + PARAMETERS.getFigName() + figEndName
print(figName)

constrains = []


PARAMETERS.isActiveLearning = "false"
PARAMETERS.isSelfLearning = "true"

PARAMETERS.model = "gaussianCos2"
PARAMETERS.errorMargin = "1.0"

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

PLOTTING.ROTATION = 22.5

_PLOT.barWithDeviationConstrained(xLabelStrings, varyingParamStringsFinal, PARAMETERS.colors, PARAMETERS.intervalColors, PARAMETERS.markers,
                                  figName, ylabel, False, False,
                                  constrains, 1, 1, PARAMETERS.figSize)

_PLOT.barWithDeviationConstrained(xLabelStrings, varyingParamStringsFinal, PARAMETERS.colors, PARAMETERS.intervalColors, PARAMETERS.markers,
                                  figName, ylabel, False, True,
                                  constrains, 1, 1, PARAMETERS.figSize)

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
