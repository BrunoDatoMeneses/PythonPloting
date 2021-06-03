import _PLOT
from Utils import transpose

import os
import csv

# transpose.transposeFiles()
from _paramsManager import PARAMETERS

figEndName = "-AllNCS"

xlabel = 'Learning Cycles (#)'
ylabel = 'Generalization Score (%)'

figVaryingParamString = "errorMargin"
varyingParamStringValues = ["0.5","1.0","1.5"]
varyingParamStrings = []
paramlabelString = "Merr "
PARAMETERS.errorMargin= "("
for value in varyingParamStringValues:
    # precisionRange+=  str(int(100*float(label))) + "_"
    # labelStrings.append(labelString + str(int(100*float(label))) + " %")
    PARAMETERS.errorMargin += value + "_"
    varyingParamStrings.append(paramlabelString + value)

PARAMETERS.errorMargin += ")"

yStrings = ["generalizationScore"]
yStringsAvg = []
yStringsDev = []
yStringsMin = []
yStringsMax = []
for string in yStrings:
    yStringsAvg.append(string+"_Average")
    yStringsDev.append(string+"_Deviation")
    yStringsMin.append(string+"_Min")
    yStringsMax.append(string+"_Max")



xString = "learningCycles"
PARAMETERS.learningCycles = (0, 2001)


logXScale = False
logYScale = False

yStringLong = yStrings[0] + "_"
for label in varyingParamStringValues:
    yStringLong += label  + "_"

XYDevMinMax = []
for y,yDev,min,max in zip(yStringsAvg, yStringsDev, yStringsMin, yStringsMax):
    XYDevMinMax.append([xString, y, yDev, min, max])

figName = PARAMETERS.figPrefix + yStringLong + "_DepOn_" + xString + "-" + PARAMETERS.getFigName() + figEndName
print(figName)

constrains = []
for varyingValue in varyingParamStringValues:
    constrains.append(PARAMETERS.getConstainsLabelsAreParamsWithVaryingParam2(varyingParamStrings,figVaryingParamString, XYDevMinMax,varyingValue))
PARAMETERS.isActiveLearning = "false"
PARAMETERS.isSelfLearning = "true"
PARAMETERS.isLearnFromNeighbors = "true"
for varyingValue in varyingParamStringValues:
    constrains.append(PARAMETERS.getConstainsLabelsAreParamsWithVaryingParam2(varyingParamStrings,figVaryingParamString, XYDevMinMax,varyingValue))

varyingParamStringsFinal=[]
for lbl in varyingParamStrings:
    varyingParamStringsFinal.append("AL "+lbl)
for lbl in varyingParamStrings:
    varyingParamStringsFinal.append("SL "+lbl)

_PLOT.plotWithDeviationWithFillBetweenConstrained(varyingParamStringsFinal, PARAMETERS.colors, PARAMETERS.intervalColors, PARAMETERS.markers,
                                       figName, xlabel, ylabel, False, logYScale,
                                       constrains, 1, 100, PARAMETERS.figSize)
_PLOT.plotWitMinMaxWithFillBetweenConstrained(varyingParamStringsFinal, PARAMETERS.colors, PARAMETERS.intervalColors, PARAMETERS.markers,
                                   figName, xlabel, ylabel, False, logYScale,
                                   constrains, 1, 100, PARAMETERS.figSize)
_PLOT.plotWithDeviationWithFillBetweenConstrained(varyingParamStringsFinal, PARAMETERS.colors, PARAMETERS.intervalColors, PARAMETERS.markers,
                                       figName, xlabel, ylabel, True, logYScale,
                                       constrains, 1, 100, PARAMETERS.figSize)
_PLOT.plotWitMinMaxWithFillBetweenConstrained(varyingParamStringsFinal, PARAMETERS.colors, PARAMETERS.intervalColors, PARAMETERS.markers,
                                   figName, xlabel, ylabel, True, logYScale,
                                   constrains, 1, 100, PARAMETERS.figSize)

# _PLOT.plotWithDeviation(labels, colors, markers, figName, xlabel, ylabel, logXScale, logYScale, xString, yString, deviationString, constrains, 1, 1)
