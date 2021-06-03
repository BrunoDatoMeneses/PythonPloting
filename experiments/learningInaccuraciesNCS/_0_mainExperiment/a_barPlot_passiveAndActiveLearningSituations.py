import _PLOT
from Utils import transpose
from _FIG import PLOTTING
from experiments.learningInaccuraciesNCS._0_mainExperiment._PARAMS import PARAMETERS


def generateFigures():
    #transpose.transposeFilesWithPaths("XP", "TFiles")

    figEndName = "-IncrementalNCS"
    ylabel = 'Situations (#)'
    yStringLong = "PassActLrnSituations"
    yStrings = ["rdmLearning", "activeLearning"]
    yStringsAvg = []
    yStringsDev = []
    yStringsMin = []
    yStringsMax = []
    for string in yStrings:
        yStringsAvg.append(string + "_Average")
        yStringsDev.append(string + "_Deviation")
        yStringsMin.append(string + "_Min")
        yStringsMax.append(string + "_Max")
    xLabelStrings = ["Passive Learning", "Active Learning"]
    XYDevMinMax = []
    for y, yDev, min, max, yString in zip(yStringsAvg, yStringsDev, yStringsMin, yStringsMax, yStrings):
        if (yString == "endogenousLearning"):
            XYDevMinMax.append([y, yDev, min, max, 0.1])
        else:
            XYDevMinMax.append([y, yDev, min, max, 1])
    figName = "a_" + yStringLong + "-" + PARAMETERS.getFigName() + figEndName
    print(figName)
    PARAMETERS.figSize = (4.5, 3.75)
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
    PARAMETERS.colors = ['tab:gray', 'tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown',
                         'tab:pink',
                         'tab:olive', 'tab:cyan']
    varyingParamStrings = ["No NCS", "Model Ambiguity", "Conflicts", "Concurrencies", "Incompetencies",
                           "Complete Redundancy", "Partial Redundancy", "Range Ambiguity"]
    PLOTTING.ROTATION = 0
    PLOTTING.LEGEND_IN = False
    PLOTTING.LEGEND_OUT = True
    logXScale = False
    logYScale = False
    _PLOT.barWithDeviationConstrained(xLabelStrings, varyingParamStrings, PARAMETERS.colors, PARAMETERS.intervalColors,
                                      PARAMETERS.markers,
                                      figName, ylabel, False, False,
                                      constrains, 1, 1, PARAMETERS.figSize)
    _PLOT.barWithDeviationConstrained(xLabelStrings, varyingParamStrings, PARAMETERS.colors, PARAMETERS.intervalColors,
                                      PARAMETERS.markers,
                                      figName, ylabel, False, True,
                                      constrains, 1, 1, PARAMETERS.figSize)


#generateFigures()

