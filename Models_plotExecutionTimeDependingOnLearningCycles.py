import _PLOT
from Utils import transpose

import os
import csv

#transpose.transposeFiles()
figSize = (6,3.75)
# figSize = (8,4.5)
# figSize = (16,9)

dimension = "2"
learningCycles = "1000"
exploitatingCycles = "250"
episodes = "10"

precisionRange = "0.1"
neighborhoodSize = "2"
influenceRatio = "0.25"

isActiveLearning = "true"
isSelfLearning = "false"
errorMargin = "1.0"
bootstrapCycle = "15"

isConflictNCS = "true"
isConcurenceNCS = "true"
isIncompetenceNCS = "true"
isSubVoidDetection = "false"
isAmbiguityNCS = "true"
isModelNCS = "true"
isLearnFromNeighbors = "false"
isDream = "false"

dreamLaunch = "1500"
nbOfNeighborForLearningFromNeighbors = "1"
nbOfNeighborForContexCreationWithouOracle = "50000"


figPrefix = "SquareFix_"
figEndName = "-AllNCS"
# figVaryingParamString = "learningCycles"
# labels = ["250","500","1000","2000","5000","10000","20000"]
# figVaryingParamString = "dimension"
# labels = ["2"]
figVaryingParamString = "precisionRange"
labels = ["0.04","0.06","0.08","0.1"]


labelString = "precisionRange "
precisionRange="#"
labelStrings = []

for label in labels:
    precisionRange+=  str(int(100*float(label))) + "_"
    labelStrings.append(labelString + str(int(100*float(label))) + " %")




xlabel = 'Learning Cycles'
ylabel = 'Execution Time (s)'

xString = "learningCycles"
learningCycles = (0,10000)

yString = "meanTime"

deviationString = "meanTime"
# minString = "nbAgents_Min"
# maxString = "nbAgents_Max"

logXScale = True
logYScale = False


colors = ['tab:red', 'tab:blue', 'tab:green', 'tab:orange', 'tab:purple', 'tab:brown']
intervalColors = ['lightcoral', 'lightsteelblue', 'lightgreen', 'lightsalmon', 'thistle', 'wheat']
markers = ['o','D','v','s','P','p']

PARAMS = {"dimension":dimension,"learningCycles":learningCycles,"exploitatingCycles":exploitatingCycles,"episodes":episodes,
          "precisionRange":precisionRange,"neighborhoodSize":neighborhoodSize,"influenceRatio":influenceRatio,
          "isActiveLearning":isActiveLearning,"isSelfLearning":isSelfLearning,
          "errorMargin":errorMargin,"bootstrapCycle":bootstrapCycle,
          "isConflictNCS":isConflictNCS,"isConcurenceNCS":isConcurenceNCS,"isIncompetenceNCS":isIncompetenceNCS,
          "isSubVoidDetection":isSubVoidDetection,"isAmbiguityNCS":isAmbiguityNCS,"isModelNCS":isModelNCS,"isLearnFromNeighbors":isLearnFromNeighbors,"isDream":isDream,
          "dreamLaunch":dreamLaunch,"nbOfNeighborForLearningFromNeighbors":nbOfNeighborForLearningFromNeighbors,
          "nbOfNeighborForContexCreationWithouOracle":nbOfNeighborForContexCreationWithouOracle}

PARAMS_STRINGS = ["dimension","learningCycles","exploitatingCycles","episodes","precisionRange","neighborhoodSize","influenceRatio",
                  "isActiveLearning","isSelfLearning","errorMargin","bootstrapCycle",
                  "isConflictNCS","isConcurenceNCS","isIncompetenceNCS","isSubVoidDetection","isAmbiguityNCS","isModelNCS","isLearnFromNeighbors","isDream",
                  "dreamLaunch","nbOfNeighborForLearningFromNeighbors","nbOfNeighborForContexCreationWithouOracle"]



figParamsString = "_D_" + str(PARAMS.get("dimension")) + \
                  "_L_" + str(PARAMS.get("learningCycles")) + \
                  "_Ex_ " + str(PARAMS.get("exploitatingCycles")) + \
                  "_Ep_ " + str(PARAMS.get("episodes")) + \
                  "_R_" + str(PARAMS.get("precisionRange")) + \
                  "_N_" + str(PARAMS.get("neighborhoodSize")) + \
                  "_I_" + str(int(100*float(PARAMS.get("influenceRatio"))) )+ \
                  "_Ac_" + str(PARAMS.get("isActiveLearning")) + \
                  "_Sf_" + str(PARAMS.get("isSelfLearning")) + \
                  "_Er_" + str(int(100*float(PARAMS.get("errorMargin")))) + \
                  "_Bt_" + str(PARAMS.get("bootstrapCycle"))


figName = figPrefix + yString + "_DepOn_" + xString + "-"+ figParamsString + figEndName




constrains = []
for label in labels:
    constrainsDico={}
    for key, value in PARAMS.items():
        if(key == figVaryingParamString):
            constrainsDico[key]=label
        else:
            constrainsDico[key] = value

    constrains.append(constrainsDico)




# _PLOT.plotWithDeviationWithFillBetween(labelStrings, colors, intervalColors, markers, figName, xlabel, ylabel, False, logYScale, xString, yString, deviationString, constrains, 1, 1, figSize)
# _PLOT.plotWitMinMaxWithFillBetween(labelStrings, colors, intervalColors, markers, figName, xlabel, ylabel, False, logYScale, xString, yString, minString, maxString, constrains, 1, 1, figSize)
# _PLOT.plotWithDeviationWithFillBetween(labelStrings, colors, intervalColors, markers, figName, xlabel, ylabel, True, logYScale, xString, yString, deviationString, constrains, 1, 1, figSize)
# _PLOT.plotWitMinMaxWithFillBetween(labelStrings, colors, intervalColors, markers, figName, xlabel, ylabel, True, logYScale, xString, yString, minString, maxString, constrains, 1, 1, figSize)

_PLOT.plot3(labelStrings, colors, markers, figName, xlabel, ylabel, True, logYScale, xString, yString, deviationString, constrains, 1, 1, figSize)
_PLOT.plot3(labelStrings, colors, markers, figName, xlabel, ylabel, False, logYScale, xString, yString, deviationString, constrains, 1, 1, figSize)