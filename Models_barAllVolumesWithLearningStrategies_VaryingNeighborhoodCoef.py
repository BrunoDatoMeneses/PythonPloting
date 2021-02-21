import _PLOT
from Utils import transpose

import os
import csv

# transpose.transposeFiles()
from _FIG import PLOTTING
from _PARAMS import PARAMETERS

figEndName = "-AllNCS"

#xlabel = 'Learning Cycles (#)'
ylabel = 'Volumes (%)'
yStringLong ="Volumes"

# varyingParamStrings = ["Active Learning","Self-Learning"]

figVaryingParamString = "neighborhoodRadiusCoefficient"
varyingParamStringValues = ["1.5","2.0","4.0"]
varyingParamStrings = []
paramlabelString = r'$\alpha^\mathcal{N} = $'
PARAMETERS.neighborhoodRadiusCoefficient= "("
for value in varyingParamStringValues:
    # precisionRange+=  str(int(100*float(label))) + "_"
    # labelStrings.append(labelString + str(int(100*float(label))) + " %")
    PARAMETERS.neighborhoodRadiusCoefficient += value + "_"
    varyingParamStrings.append(paramlabelString + value)

PARAMETERS.neighborhoodRadiusCoefficient += ")"

PARAMETERS.figSize = (3.5, 3.75)
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
for y,yDev,min,max,yString in zip(yStringsAvg, yStringsDev, yStringsMin, yStringsMax,yStrings):
    if yString == "endogenousLearningSituations":
        XYDevMinMax.append([y, yDev, min, max,0.05])
    else:
        XYDevMinMax.append([y, yDev, min, max])

figName = PARAMETERS.figPrefix + yStringLong + "_" + figVaryingParamString + "-" + PARAMETERS.getFigName() + figEndName
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

PLOTTING.ROTATION=22.5
PLOTTING.LEGEND_IN=False

_PLOT.barWithDeviationConstrained(xLabelStrings, varyingParamStringsFinal, PARAMETERS.colors, PARAMETERS.intervalColors, PARAMETERS.markers,
                                  figName, ylabel, False, False,
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
