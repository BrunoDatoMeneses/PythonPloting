import _PLOT
from Utils import transpose
from _FIG import PLOTTING
from experiments.learningInaccuraciesNCS._0_mainExperiment._PARAMS import PARAMETERS

transpose.transposeFilesWithPaths("XP","TFiles")


figEndName = "-IncrementalNCS"
ylabel = 'Prediction Error (%)'
yStringLong ="predictionError"



yStrings = ["predictionError"]

yStringsAvg = []
yStringsDev = []
yStringsMin = []
yStringsMax = []
for string in yStrings:
    yStringsAvg.append(string+"_Average")
    yStringsDev.append(string+"Deviation_Average")
    yStringsMin.append(string+"_Min")
    yStringsMax.append(string+"_Max")

xLabelStrings = [""]


XYDevMinMax = []
for y,yDev,min,max in zip(yStringsAvg, yStringsDev, yStringsMin, yStringsMax):
    XYDevMinMax.append([y, yDev, min, max])


figName = "e_" + yStringLong + "-" + PARAMETERS.getFigName() + figEndName
print(figName)



constrains = []

PARAMETERS.isModelNCS = "false"
PARAMETERS.isConflictNCS = "false"
PARAMETERS.isConcurenceNCS = "false"
PARAMETERS.isIncompetenceNCS = "false"
PARAMETERS.isFusionResolution = "false"
PARAMETERS.isRetructureResolution = "false"
PARAMETERS.isAmbiguityNCS = "false"

constrains.append(PARAMETERS.getConstainsLabelsAreYStrings(xLabelStrings, XYDevMinMax))

PARAMETERS.isModelNCS = "true"
PARAMETERS.isConflictNCS = "false"
PARAMETERS.isConcurenceNCS = "false"
PARAMETERS.isIncompetenceNCS = "false"
PARAMETERS.isFusionResolution = "false"
PARAMETERS.isRetructureResolution = "false"
PARAMETERS.isAmbiguityNCS = "false"

constrains.append(PARAMETERS.getConstainsLabelsAreYStrings(xLabelStrings, XYDevMinMax))

PARAMETERS.isModelNCS = "true"
PARAMETERS.isConflictNCS = "true"
PARAMETERS.isConcurenceNCS = "false"
PARAMETERS.isIncompetenceNCS = "false"
PARAMETERS.isFusionResolution = "false"
PARAMETERS.isRetructureResolution = "false"
PARAMETERS.isAmbiguityNCS = "false"

constrains.append(PARAMETERS.getConstainsLabelsAreYStrings(xLabelStrings, XYDevMinMax))

PARAMETERS.isModelNCS = "true"
PARAMETERS.isConflictNCS = "true"
PARAMETERS.isConcurenceNCS = "true"
PARAMETERS.isIncompetenceNCS = "false"
PARAMETERS.isFusionResolution = "false"
PARAMETERS.isRetructureResolution = "false"
PARAMETERS.isAmbiguityNCS = "false"

constrains.append(PARAMETERS.getConstainsLabelsAreYStrings(xLabelStrings, XYDevMinMax))

PARAMETERS.isModelNCS = "true"
PARAMETERS.isConflictNCS = "true"
PARAMETERS.isConcurenceNCS = "true"
PARAMETERS.isIncompetenceNCS = "true"
PARAMETERS.isFusionResolution = "false"
PARAMETERS.isRetructureResolution = "false"
PARAMETERS.isAmbiguityNCS = "false"

constrains.append(PARAMETERS.getConstainsLabelsAreYStrings(xLabelStrings, XYDevMinMax))

PARAMETERS.isModelNCS = "true"
PARAMETERS.isConflictNCS = "true"
PARAMETERS.isConcurenceNCS = "true"
PARAMETERS.isIncompetenceNCS = "true"
PARAMETERS.isFusionResolution = "true"
PARAMETERS.isRetructureResolution = "false"
PARAMETERS.isAmbiguityNCS = "false"

constrains.append(PARAMETERS.getConstainsLabelsAreYStrings(xLabelStrings, XYDevMinMax))

PARAMETERS.isModelNCS = "true"
PARAMETERS.isConflictNCS = "true"
PARAMETERS.isConcurenceNCS = "true"
PARAMETERS.isIncompetenceNCS = "true"
PARAMETERS.isFusionResolution = "true"
PARAMETERS.isRetructureResolution = "true"
PARAMETERS.isAmbiguityNCS = "false"

constrains.append(PARAMETERS.getConstainsLabelsAreYStrings(xLabelStrings, XYDevMinMax))

PARAMETERS.isModelNCS = "true"
PARAMETERS.isConflictNCS = "true"
PARAMETERS.isConcurenceNCS = "true"
PARAMETERS.isIncompetenceNCS = "true"
PARAMETERS.isFusionResolution = "true"
PARAMETERS.isRetructureResolution = "true"
PARAMETERS.isAmbiguityNCS = "true"

constrains.append(PARAMETERS.getConstainsLabelsAreYStrings(xLabelStrings, XYDevMinMax))

PARAMETERS.colors = ['tab:gray', 'tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown', 'tab:pink',
     'tab:olive', 'tab:cyan']

varyingParamStrings=["No NCS","Model Ambiguity", "Conflicts", "Concurrencies", "Incompetencies", "Complete Redundancy", "Partial Redundancy", "Range Ambiguity"]

PARAMETERS.figSize = (4, 3.75)

PLOTTING.ROTATION = 0
PLOTTING.LEGEND_IN = False
PLOTTING.LEGEND_OUT = True

logXScale = False
logYScale = False

_PLOT.barWithDeviationConstrained(xLabelStrings, varyingParamStrings, PARAMETERS.colors, PARAMETERS.intervalColors, PARAMETERS.markers,
                                  figName, ylabel, False, logYScale,
                                  constrains, 1, 100, PARAMETERS.figSize)

_PLOT.barWithDeviationConstrained(xLabelStrings, varyingParamStrings, PARAMETERS.colors, PARAMETERS.intervalColors, PARAMETERS.markers,
                                  figName, ylabel, False, True,
                                  constrains, 1, 100, PARAMETERS.figSize)


