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
yStringLong ="Situations"



# figVaryingParamString = "activeExploitationCycles"
# varyingParamStringValues = ["0","1000","10000","20000","100000"]
# varyingParamStrings = []
# paramlabelString = r'$\mathcal{E}^N_{lifelong} = $'
# PARAMETERS.activeExploitationCycles= "("
# for value in varyingParamStringValues:
#     # precisionRange+=  str(int(100*float(label))) + "_"
#     # labelStrings.append(labelString + str(int(100*float(label))) + " %")
#     PARAMETERS.activeExploitationCycles += value + "_"
#     varyingParamStrings.append(value + paramlabelString)
#
# PARAMETERS.activeExploitationCycles += ")"


yStrings = ["rdmLearning","rdmExploitation","exogenousLearning","endogenousLearning","endogenousExploitation"]
yStringsAvg = []
yStringsDev = []
yStringsMin = []
yStringsMax = []
for string in yStrings:
    yStringsAvg.append(string+"_Average")
    yStringsDev.append(string+"_Deviation")
    yStringsMin.append(string+"_Min")
    yStringsMax.append(string+"_Max")

xLabelStrings = ["Passive Learning","Passive Exploitation","Exo. Learning","Endo. Learning /10","Endo. Exploitation"]





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



PARAMETERS.figSize = (10, 3.75)
PARAMETERS.learningCycles = "2000"
figName = "lifelongSL_Var_" + yStringLong + "-" + PARAMETERS.getFigName() + figEndName
print(figName)
varyingParamValues = ["0","1000","10000","20000","100000"]
# varyingParamValues = ["0","500","1000","2000","4000","6000","10000","20000","50000","100000"]


varyingParamStrings = []
for val in varyingParamValues:
    varyingParamStrings.append(r'$\mathcal{E}_{\#}^{lifelong} = $' + val)



PARAMETERS.isActiveLearning = "false"
PARAMETERS.isSelfLearning = "true"
PARAMETERS.isLearnFromNeighbors = "true"
PARAMETERS.isActiveExploitation = "true"
PARAMETERS.activeExploitationCycles = "0"

constrains = []
constrains.append(PARAMETERS.getConstainsLabelsAreYStrings(xLabelStrings, XYDevMinMax));



for val in varyingParamValues[1:]:
    PARAMETERS.activeExploitationCycles = val
    constrains.append(PARAMETERS.getConstainsLabelsAreYStrings(xLabelStrings, XYDevMinMax));


PLOTTING.ROTATION = 22.5

_PLOT.barWithDeviationConstrained(xLabelStrings, varyingParamStrings, PARAMETERS.colors, PARAMETERS.intervalColors, PARAMETERS.markers,
                                  figName, ylabel, False, False,
                                  constrains, 1, 1, PARAMETERS.figSize)

_PLOT.barWithDeviationConstrained(xLabelStrings, varyingParamStrings, PARAMETERS.colors, PARAMETERS.intervalColors, PARAMETERS.markers,
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
