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
bootstrapCycle = "10"

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
figVaryingParamString = "learningCycles"
labels = ["250","500","1000","2000","5000","10000","20000"]
colors = ['tab:red', 'tab:blue', 'tab:green', 'tab:orange', 'tab:purple', 'tab:brown','tab:pink']
intervalColors = ['lightcoral', 'lightsteelblue', 'lightgreen', 'lightsalmon', 'thistle', 'wheat','pink']
markers = ['o','D','v','s','P','p','*']
# labels = ["500","1000","2000","5000","10000","20000"]
# colors = ['tab:red', 'tab:blue', 'tab:green', 'tab:orange', 'tab:purple', 'tab:brown']
# intervalColors = ['lightcoral', 'lightsteelblue', 'lightgreen', 'lightsalmon', 'thistle', 'wheat']
# markers = ['o','D','v','s','P','p']

# labels = ["1000"]
# colors = ['tab:red']
# intervalColors = ['lightcoral']
# markers = ['o']

# learningCycles = "250_500_1000_2000_5000_10000_20000"
learningCycles="#"
for label in labels:
    learningCycles+= label + "_"
episodes = "#"
xKey = "episodes"

xlabel = 'Episodes'
ylabel = 'Prediction Error'
logXScale = False
logYScale = False
xString = "episodes"
yString = "predictionError_Average"
deviationString = "predictionErrorDeviation_Average"
minString = "predictionError_Min"
maxString = "predictionError_Max"

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


figParamsString = "_D_" + PARAMS.get("dimension") + \
                  "_L_" + PARAMS.get("learningCycles") + \
                  "_Ex_ " + PARAMS.get("exploitatingCycles") + \
                  "_Ep_ " + PARAMS.get("episodes") + \
                  "_R_" + str(int(100*float(PARAMS.get("precisionRange")))) + \
                  "_N_" + PARAMS.get("neighborhoodSize") + \
                  "_I_" + str(int(100*float(PARAMS.get("influenceRatio"))) )+ \
                  "_Ac_" + PARAMS.get("isActiveLearning") + \
                  "_Sf_" + PARAMS.get("isSelfLearning") + \
                  "_Er_" + str(int(100*float(PARAMS.get("errorMargin")))) + \
                  "_Bt_" + PARAMS.get("bootstrapCycle")


figName = figPrefix + "predictionError_Average-"+ figParamsString + figEndName




constrains = []
for label in labels:
    constrainsDico={}
    for key, value in PARAMS.items():
        if(key != xKey):
            if(key == figVaryingParamString):
                constrainsDico[key]=label
            else:
                constrainsDico[key] = value
    constrains.append(constrainsDico)





_PLOT.plotWithDeviationWithFillBetween(labels, colors, intervalColors, markers, figName, xlabel, ylabel, logXScale, logYScale, xString, yString, deviationString, constrains, 1, 1, figSize)
_PLOT.plotWitMinMaxWithFillBetween(labels, colors, intervalColors, markers, figName, xlabel, ylabel, logXScale, logYScale, xString, yString, minString, maxString, constrains, 1, 1, figSize)

#_PLOT.plotWithDeviation(labels, colors, markers, figName, xlabel, ylabel, logXScale, logYScale, xString, yString, deviationString, constrains, 1, 1)