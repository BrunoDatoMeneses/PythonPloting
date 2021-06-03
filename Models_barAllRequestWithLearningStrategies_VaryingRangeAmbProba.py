import _PLOT
from Utils import transpose

import os
import csv

# transpose.transposeFiles()
from _paramsManager import PARAMETERS

figEndName = "-AllNCS"

#xlabel = 'Learning Cycles (#)'
ylabel = 'Situations (#)'
yStringLong ="Situations"

# varyingParamStrings = ["Active Learning","Self-Learning"]

figVaryingParamString = "probabilityOfRangeAmbiguity"
varyingParamStringValues = ["0.01","0.05","0.1"]
varyingParamStrings = []
paramlabelString = "PBdisc "
PARAMETERS.probabilityOfRangeAmbiguity= "("
for value in varyingParamStringValues:
    # precisionRange+=  str(int(100*float(label))) + "_"
    # labelStrings.append(labelString + str(int(100*float(label))) + " %")
    PARAMETERS.probabilityOfRangeAmbiguity += value + "_"
    varyingParamStrings.append(paramlabelString + value)

PARAMETERS.probabilityOfRangeAmbiguity += ")"

yStrings = ["modelRequests","conflictRequests","concurrenceRequests","voidRequests","fusionRequests","restructureRequests","frontierRequests"]
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

xLabelStrings = ["Model Ambiguities", "Conflicts", "Concurrencies", "Incompetencies", "Complete Redundancy", "Partial Redundancy","Range Ambiguities"]
# xLabelStrings = ["Model Ambiguities", "Conflicts", "Concurrencies", "Incompetencies", "Complete Redundancy", "Partial Redundancy","Neighbors"]
# xLabelStrings = ["Passive","Active","Self-Generated"]
# xLabelStrings = ["Passive","Active","Self-Generated","Model Ambiguities", "Conflicts", "Concurrencies", "Incompetencies", "Complete Redundancy", "Partial Redundancy"]




logXScale = False
logYScale = False


# for label in labelStrings:
#     yStringLong += label  + "_"

XYDevMinMax = []
for y,yDev,min,max in zip(yStringsAvg, yStringsDev, yStringsMin, yStringsMax):
    XYDevMinMax.append([y, yDev, min, max])

figName = PARAMETERS.figPrefix + yStringLong + "-" + PARAMETERS.getFigName() + figEndName
print(figName)

constrains = []
for varyingValue in varyingParamStringValues:
    constrains.append(PARAMETERS.getConstainsLabelsAreParamsWithVaryingParam(xLabelStrings,figVaryingParamString, XYDevMinMax,varyingValue))

PARAMETERS.isActiveLearning = "false"
PARAMETERS.isSelfLearning = "true"
PARAMETERS.isLearnFromNeighbors = "true"

for varyingValue in varyingParamStringValues:
    constrains.append(PARAMETERS.getConstainsLabelsAreParamsWithVaryingParam(xLabelStrings,figVaryingParamString, XYDevMinMax,varyingValue))


varyingParamStringsFinal=[]
for lbl in varyingParamStrings:
    varyingParamStringsFinal.append("AL "+lbl)
for lbl in varyingParamStrings:
    varyingParamStringsFinal.append("SL "+lbl)

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
