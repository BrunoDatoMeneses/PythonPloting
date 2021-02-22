import _PLOT
from Utils import transpose

import os
import csv

# transpose.transposeFiles()
from _FIG import PLOTTING
from _PARAMS import PARAMETERS

figEndName = "-AllNCS"

#xlabel = 'Learning Cycles (#)'
ylabel = 'Situations (#)'
yStringLong ="RequestsAllNCSwithNeighbors"



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

xLabelStrings = ["Model Ambiguities", "Conflicts", "Concurrencies", "Incompetencies", "Complete Redundancy", "Partial Redundancy","Range Ambiguity"]
# xLabelStrings = ["Model Ambiguities", "Conflicts", "Concurrencies", "Incompetencies", "Complete Redundancy", "Partial Redundancy","Neighbors"]
# xLabelStrings = ["Passive","Active","Self-Generated"]
# xLabelStrings = ["Passive","Active","Self-Generated","Model Ambiguities", "Conflicts", "Concurrencies", "Incompetencies", "Complete Redundancy", "Partial Redundancy"]




logXScale = False
logYScale = False


# for label in labelStrings:
#     yStringLong += label  + "_"

PLOTTING.ROTATION = 45

XYDevMinMax = []
for y,yDev,min,max,yString in zip(yStringsAvg, yStringsDev, yStringsMin, yStringsMax,yStrings):
    if(yString == "endogenousLearningSituations"):
        XYDevMinMax.append([y, yDev, min, max,0.1])
    else:
        XYDevMinMax.append([y, yDev, min, max])

figName = "transfer_"  + yStringLong + "-" + PARAMETERS.getFigName() + figEndName
print(figName)


varyingParamStrings = ["Diagonal","Disc","Square","Square, Diagonal","Square, Diagonal, Disc"]


constrains = []
listOfModels = ["triangle", "disc", "squareFixed", "squareDiag", "squareDiagCircle"]
listOfLearningCycles = ["1000", "1000", "1000", "2000", "3000"]

for mod,cycl in zip(listOfModels,listOfLearningCycles):
    PARAMETERS.model = mod
    PARAMETERS.learningCycles = cycl
    constrains.append(PARAMETERS.getConstainsLabelsAreYStrings(xLabelStrings, XYDevMinMax))


_PLOT.barWithDeviationConstrainedModded(xLabelStrings, varyingParamStrings, PARAMETERS.colors, PARAMETERS.intervalColors, PARAMETERS.markers,
                                  figName, ylabel, False, False,
                                  constrains, 1, 1, PARAMETERS.figSize)

_PLOT.barWithDeviationConstrainedModded(xLabelStrings, varyingParamStrings, PARAMETERS.colors, PARAMETERS.intervalColors, PARAMETERS.markers,
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
