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
yStringLong ="SituationsPassAct"



figVaryingParamString = "validityRangesPrecision"
varyingParamStringValues = ["0.02","0.04","0.06"]
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
yStrings = ["rdmLearning","rdmExploitation","activeLearning","activeExploitation"]
yStringsAvg = []
yStringsDev = []
yStringsMin = []
yStringsMax = []
for string in yStrings:
    yStringsAvg.append(string+"_Average")
    yStringsDev.append(string+"_Deviation")
    yStringsMin.append(string+"_Min")
    yStringsMax.append(string+"_Max")

xLabelStrings = ["Passive Learning","Passive Exploitation","Active Learning","Active Exploitation"]





logXScale = False
logYScale = False


# for label in labelStrings:
#     yStringLong += label  + "_"

XYDevMinMax = []
for y,yDev,min,max,yString in zip(yStringsAvg, yStringsDev, yStringsMin, yStringsMax,yStrings):
    if(yString == "endogenousLearning"):
        XYDevMinMax.append([y, yDev, min, max,0.1])
    else:
        XYDevMinMax.append([y, yDev, min, max, 1])





figName = "noise_3Strat_" + PARAMETERS.noise + "_" + yStringLong + "-" + PARAMETERS.getFigName() + figEndName
print(figName)

constrains = []

PARAMETERS.isActiveLearning = "true"
PARAMETERS.isSelfLearning = "false"
PARAMETERS.isLearnFromNeighbors = "false"

for varyingValue in varyingParamStringValues:
    constrains.append(PARAMETERS.getConstainsLabelsAreParamsWithVaryingParam(xLabelStrings,figVaryingParamString, XYDevMinMax,varyingValue))


PARAMETERS.isActiveLearning = "true"
PARAMETERS.isSelfLearning = "false"
PARAMETERS.isLearnFromNeighbors = "true"

for varyingValue in varyingParamStringValues:
    constrains.append(PARAMETERS.getConstainsLabelsAreParamsWithVaryingParam(xLabelStrings,figVaryingParamString, XYDevMinMax,varyingValue))

PARAMETERS.isActiveLearning = "false"
PARAMETERS.isSelfLearning = "true"
PARAMETERS.isLearnFromNeighbors = "true"

for varyingValue in varyingParamStringValues:
    constrains.append(PARAMETERS.getConstainsLabelsAreParamsWithVaryingParam(xLabelStrings,figVaryingParamString, XYDevMinMax,varyingValue))

# varyingParamStrings = ["Active Learning","Active Cooperative Learning","Self-Learning"]
varyingParamStringsFinal=[]
for lbl in varyingParamStrings:
    varyingParamStringsFinal.append("AL "+lbl)
for lbl in varyingParamStrings:
    varyingParamStringsFinal.append("ACL "+lbl)
for lbl in varyingParamStrings:
    varyingParamStringsFinal.append("SL "+lbl)

PLOTTING.LEGEND_IN = False
PLOTTING.LEGEND_OUT = True
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
