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
yStringLong ="Situations"



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

PARAMETERS.figSize = (8, 3.75)
yStrings = ["rdmLearning","activeLearning","activeExploitation","exogenousLearning","endogenousLearning","endogenousExploitation"]
yStringsAvg = []
yStringsDev = []
yStringsMin = []
yStringsMax = []
for string in yStrings:
    yStringsAvg.append(string+"_Average")
    yStringsDev.append(string+"_Deviation")
    yStringsMin.append(string+"_Min")
    yStringsMax.append(string+"_Max")

xLabelStrings = ["Passive Learning","Active Learning","Active Exploitation","Exo. Learning","Endo. Learning /20","Endo. Exploitation"]





logXScale = False
logYScale = False


# for label in labelStrings:
#     yStringLong += label  + "_"

XYDevMinMax = []
for y,yDev,min,max,yString in zip(yStringsAvg, yStringsDev, yStringsMin, yStringsMax,yStrings):
    if(yString == "endogenousLearning"):
        XYDevMinMax.append([y, yDev, min, max,0.05])
    else:
        XYDevMinMax.append([y, yDev, min, max, 1])

PARAMETERS.isActiveLearning = "false"
PARAMETERS.isSelfLearning = "true"
PARAMETERS.isLearnFromNeighbors = "true"

figName = "transfer_"  + yStringLong + "-" + PARAMETERS.getFigName() + figEndName
print(figName)

constrains = []
varyingParamStrings = ["Disc",r'$\mathrm{Square} \rightarrow \mathrm{Disc}$',"Rhombus",r'$\mathrm{Square} \rightarrow \mathrm{Disc}$',r'$\mathrm{Square} \rightarrow \mathrm{Disc} \rightarrow \mathrm{Rhombus}$']
listOfModels = ["disc", "squareDisc","los", "squareDisc", "squareDiscLos"]
# listOfLearningCycles = ["1000", "1000", "1000", "1750", "2500"]
listOfLearningCycles = [ "2000", "3500","2000", "3500", "5000"]

for mod,cycl in zip(listOfModels,listOfLearningCycles):
    PARAMETERS.model = mod
    PARAMETERS.learningCycles = cycl
    constrains.append(PARAMETERS.getConstainsLabelsAreYStrings(xLabelStrings, XYDevMinMax))

PLOTTING.ROTATION = 22.5

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
