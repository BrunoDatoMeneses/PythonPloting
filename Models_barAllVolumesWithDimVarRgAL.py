import _PLOT
from Utils import transpose

import os
import csv

# transpose.transposeFiles()
from _FIG import PLOTTING
from _paramsManager import PARAMETERS

figEndName = "-AllNCS"

#xlabel = 'Learning Cycles (#)'
ylabel = 'Volumes (%)'
yStringLong ="Volumes"

figVaryingParamString = "validityRangesPrecision"
varyingParamStringValues = ["0.02", "0.06", "0.1"]
varyingParamStrings = []
paramlabelString = r'$p^\mathcal{R} = $'
PARAMETERS.validityRangesPrecision= "("
for value in varyingParamStringValues:
    # precisionRange+=  str(int(100*float(label))) + "_"
    # labelStrings.append(labelString + str(int(100*float(label))) + " %")
    PARAMETERS.validityRangesPrecision += value + "_"
    varyingParamStrings.append(paramlabelString + value)

PARAMETERS.validityRangesPrecision += ")"

PARAMETERS.figSize = (4.5, 3.75)
yStrings = ["conflictVol","concurrenceVol","voidVol"]
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

xLabelStrings = ["Conflicts", "Concurrencies", "Incompetencies"]
# xLabelStrings = ["Agents", "Innacuracies", "Conflicts", "Concurrencies", "Incompetencies"]




logXScale = False
logYScale = False


# for label in labelStrings:
#     yStringLong += label  + "_"

XYDevMinMax = []
for y,yDev,min,max in zip(yStringsAvg, yStringsDev, yStringsMin, yStringsMax):
    XYDevMinMax.append([y, yDev, min, max])


PARAMETERS.figSize = (4.5, 3.75)

figName = "sca_23510_ELLSA_" + yStringLong + "-" + PARAMETERS.getFigName() + figEndName
print(figName)
#
# PARAMETERS.isActiveLearning = "false"
# PARAMETERS.isSelfLearning = "true"
# PARAMETERS.isLearnFromNeighbors = "true"

constrains = []
PARAMETERS.dimension = "2"
for varyingValue in varyingParamStringValues:
    constrains.append(PARAMETERS.getConstainsLabelsAreParamsWithVaryingParam(xLabelStrings,figVaryingParamString, XYDevMinMax,varyingValue))
PARAMETERS.dimension = "3"
for varyingValue in varyingParamStringValues:
    constrains.append(PARAMETERS.getConstainsLabelsAreParamsWithVaryingParam(xLabelStrings,figVaryingParamString, XYDevMinMax,varyingValue))
PARAMETERS.dimension = "5"
for varyingValue in varyingParamStringValues:
    constrains.append(
        PARAMETERS.getConstainsLabelsAreParamsWithVaryingParam(xLabelStrings, figVaryingParamString, XYDevMinMax,
                                                               varyingValue))
# PARAMETERS.dimension = "10"
# for varyingValue in varyingParamStringValues:
#     constrains.append(
#         PARAMETERS.getConstainsLabelsAreParamsWithVaryingParam(xLabelStrings, figVaryingParamString, XYDevMinMax,
#                                                                varyingValue))


varyingParamStringsFinal=[]
for lbl in varyingParamStrings:
    varyingParamStringsFinal.append("n = 2"+ " " +lbl)
for lbl in varyingParamStrings:
    varyingParamStringsFinal.append("n = 3"+ " " +lbl)
for lbl in varyingParamStrings:
    varyingParamStringsFinal.append("n = 5" + " " + lbl)
for lbl in varyingParamStrings:
    varyingParamStringsFinal.append("n = 10" + " " + lbl)

PLOTTING.LEGEND_IN = False
PLOTTING.LEGEND_OUT = True

PLOTTING.ROTATION = 0

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
