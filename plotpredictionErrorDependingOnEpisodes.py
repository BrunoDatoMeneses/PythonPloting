import _PLOT
from Utils import transpose

import os
import csv

#transpose.transposeFiles()

learningCycles = "1000"


figVaryingParamString = "learningCycles"
labels = ['1000']
colors = ['tab:red']
markers = ['o']


#Varying variable for labels
# for label in labels:
#     learningCycles += "-"+label

figParamsString = "_Lrn_" + learningCycles

figName = "predictionError_Average-"+figParamsString
xlabel = 'Episodes'
ylabel = 'Prediction Error'
logXScale = False
logYScale = False
xString = "episodes"
yString = "predictionError_Average"
deviationString = "predictionErrorDeviation_Average"



constrains = [{"learningCycles":learningCycles },
              ]


_PLOT.plotWithDeviationWithFillBetween(labels, colors, markers, figName, xlabel, ylabel, logXScale, logYScale, xString, yString, deviationString, constrains, 1, 1)
#_PLOT.plotWithDeviation(labels, colors, markers, figName, xlabel, ylabel, logXScale, logYScale, xString, yString, deviationString, constrains, 1, 1)