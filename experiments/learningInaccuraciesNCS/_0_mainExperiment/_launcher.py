#!/usr/bin/env python3
import itertools
import os

import experiments
from Utils import transpose
from experiments.learningInaccuraciesNCS._0_mainExperiment import a_barPlot_passiveAndActiveLearningSituations, \
    b_barplot_inaccuraciesVolumes, c_barPlot_nbAgents, d_barPlot_generalizationScore, e_barPlot_predictionError, \
    f_barPlot_learningInaccuraciesNCSCounts

from experiments.learningInaccuraciesNCS._0_mainExperiment._PARAMS import PARAMETERS


def launch():
    for dimension, configFile in zip(dimensions, configFiles):
        for iteration in itertools.product(learningCycles, exploitationCycles, episodes, precisionRanges,
                                           neighborhoodMultiplicators,
                                           externalInfluenceRatios, regressionPerformances, activeLearning,
                                           selfLearning,
                                           setConflictDetection, setConcurrenceDetection, setVoidDetection,
                                           setSubVoidDetection,
                                           setFrontierRequest, setSelfModelRequest, setFusionResolution,
                                           setRestructureResolution,
                                           setDream, setDreamCycleLaunch,
                                           setLearnFromNeighbors, nbOfNeighborForLearningFromNeighbors,
                                           nbOfNeighborForContexCreationWithouOracle,
                                           setCreationFromNeighbor,
                                           models, setbootstrapCycles,
                                           exogenousLearningWeight, endogenousLearningWeight,
                                           LEARNING_WEIGHT_ACCURACY, LEARNING_WEIGHT_PROXIMITY,
                                           LEARNING_WEIGHT_EXPERIENCE, LEARNING_WEIGHT_GENERALIZATION,
                                           EXPLOITATION_WEIGHT_PROXIMITY, EXPLOITATION_WEIGHT_EXPERIENCE,
                                           EXPLOITATION_WEIGHT_GENERALIZATION,
                                           perceptionsGenerationCoefficient, modelSimilarityThreshold,
                                           maxRangeRadiusCoefficient, rangeSimilarityCoefficient,
                                           minimumRangeCoefficient,
                                           isAllContextSearchAllowedForLearning,
                                           isAllContextSearchAllowedForExploitation,
                                           probabilityOfRangeAmbiguity, transferRatio,
                                           endoExploitationCycles,isActiveExploitation,
                                           noiseRange
                                           ):

            fileName = dimension + "_"
            arguments = dimension + " " + configFile + " "
            argumentsList = [dimension, configFile]
            for arg in iteration:
                arguments += arg + " "
                if arg == "true":
                    fileName += "t" + "_"
                elif arg == "false":
                    fileName += "f" + "_"
                elif '.' in arg:
                    newArg=""
                    for char in arg:
                        if char != '.':
                            newArg+=char
                    fileName += newArg + "_"
                else:
                    fileName += arg + "_"

                argumentsList.append(arg)

            print(arguments, "ARGS SIZE : " + str(len(argumentsList) + 1))

            arguments += fileName
            argumentsList.append(fileName)

            os.system("java -jar ../../../Jars/_ELLSA.jar " + arguments)
            print("")


if __name__ == "__main__":


    dimensions = [PARAMETERS.dimension]
    configFiles = [PARAMETERS.configFile]

    learningCycles = [PARAMETERS.learningCycles]
    exploitationCycles = [PARAMETERS.exploitatingCycles]
    episodes = [PARAMETERS.episodes]

    # Neighborhood
    precisionRanges = [PARAMETERS.validityRangesPrecision]
    neighborhoodMultiplicators = [PARAMETERS.neighborhoodRadiusCoefficient]
    externalInfluenceRatios = [PARAMETERS.influenceRadiusCoefficient]
    regressionPerformances = [PARAMETERS.errorMargin]

    # NCS

    setSelfModelRequest = [PARAMETERS.isModelNCS]
    setConflictDetection = [PARAMETERS.isConflictNCS]
    setConcurrenceDetection = [PARAMETERS.isConcurenceNCS]
    setVoidDetection = [PARAMETERS.isIncompetenceNCS]
    setFusionResolution = [PARAMETERS.isFusionResolution]
    setRestructureResolution = [PARAMETERS.isRetructureResolution]
    setFrontierRequest = [PARAMETERS.isAmbiguityNCS]

    setSubVoidDetection = [PARAMETERS.isSubVoidDetection]

    setDream = [PARAMETERS.isDream]
    setDreamCycleLaunch = [PARAMETERS.dreamLaunch]


    nbOfNeighborForLearningFromNeighbors = [PARAMETERS.nbOfNeighborForLearningFromNeighbors]
    nbOfNeighborForContexCreationWithouOracle = [PARAMETERS.nbOfNeighborForContexCreationWithouOracle]
    setCreationFromNeighbor = [PARAMETERS.isCreationFromNeighbor]

    models = [PARAMETERS.model]
    setbootstrapCycles = [PARAMETERS.bootstrapCycle]

    exogenousLearningWeight= [PARAMETERS.exogenousLearningWeight]
    endogenousLearningWeight = [PARAMETERS.endogenousLearningWeight]

    LEARNING_WEIGHT_ACCURACY = [PARAMETERS.LEARNING_WEIGHT_ACCURACY]
    LEARNING_WEIGHT_PROXIMITY = [PARAMETERS.LEARNING_WEIGHT_PROXIMITY]
    LEARNING_WEIGHT_EXPERIENCE = [PARAMETERS.LEARNING_WEIGHT_EXPERIENCE]
    LEARNING_WEIGHT_GENERALIZATION = [PARAMETERS.LEARNING_WEIGHT_GENERALIZATION]

    EXPLOITATION_WEIGHT_PROXIMITY = [PARAMETERS.EXPLOITATION_WEIGHT_PROXIMITY]
    EXPLOITATION_WEIGHT_EXPERIENCE = [PARAMETERS.EXPLOITATION_WEIGHT_EXPERIENCE]
    EXPLOITATION_WEIGHT_GENERALIZATION = [PARAMETERS.EXPLOITATION_WEIGHT_GENERALIZATION]

    perceptionsGenerationCoefficient = [PARAMETERS.perceptionsGenerationCoefficient]
    modelSimilarityThreshold = [PARAMETERS.modelSimilarityThreshold]

    maxRangeRadiusCoefficient = [PARAMETERS.maxRangeRadiusCoefficient]
    rangeSimilarityCoefficient = [PARAMETERS.rangeSimilarityCoefficient]
    minimumRangeCoefficient = [PARAMETERS.minimumRangeCoefficient]

    isAllContextSearchAllowedForLearning = [PARAMETERS.isAllContextSearchAllowedForLearning]
    isAllContextSearchAllowedForExploitation = [PARAMETERS.isAllContextSearchAllowedForExploitation]
    probabilityOfRangeAmbiguity = [PARAMETERS.probabilityOfRangeAmbiguity]

    transferRatio = [PARAMETERS.transferRatio]

    endoExploitationCycles = [PARAMETERS.activeExploitationCycles]
    isActiveExploitation = [PARAMETERS.isActiveExploitation]
    noiseRange = [PARAMETERS.noise]

    # ACTIVE LEARNING
    activeLearning = [PARAMETERS.isActiveLearning]
    selfLearning = [PARAMETERS.isSelfLearning]
    setLearnFromNeighbors = [PARAMETERS.isLearnFromNeighbors]


    # no NCS

    setSelfModelRequest = ["false"]
    setConflictDetection = ["false"]
    setConcurrenceDetection = ["false"]
    setVoidDetection = ["false"]
    setFusionResolution = ["false"]
    setRestructureResolution = ["false"]
    setFrontierRequest = ["false"]

    launch()

    # add Model Ambiguity NCS

    setSelfModelRequest = ["true"]
    setConflictDetection = ["false"]
    setConcurrenceDetection = ["false"]
    setVoidDetection = ["false"]
    setFusionResolution = ["false"]
    setRestructureResolution = ["false"]
    setFrontierRequest = ["false"]

    launch()


    # add Conflict NCS

    setSelfModelRequest = ["true"]
    setConflictDetection = ["true"]
    setConcurrenceDetection = ["false"]
    setVoidDetection = ["false"]
    setFusionResolution = ["false"]
    setRestructureResolution = ["false"]
    setFrontierRequest = ["false"]

    launch()


    # add Concurrence NCS

    setSelfModelRequest = ["true"]
    setConflictDetection = ["true"]
    setConcurrenceDetection = ["true"]
    setVoidDetection = ["false"]
    setFusionResolution = ["false"]
    setRestructureResolution = ["false"]
    setFrontierRequest = ["false"]

    launch()


    # add Incompetence NCS

    setSelfModelRequest = ["true"]
    setConflictDetection = ["true"]
    setConcurrenceDetection = ["true"]
    setVoidDetection = ["true"]
    setFusionResolution = ["false"]
    setRestructureResolution = ["false"]
    setFrontierRequest = ["false"]

    launch()



    # add Complete Redundancy NCS

    setSelfModelRequest = ["true"]
    setConflictDetection = ["true"]
    setConcurrenceDetection = ["true"]
    setVoidDetection = ["true"]
    setFusionResolution = ["true"]
    setRestructureResolution = ["false"]
    setFrontierRequest = ["false"]

    launch()

    # add PartialRedundancy NCS

    setSelfModelRequest = ["true"]
    setConflictDetection = ["true"]
    setConcurrenceDetection = ["true"]
    setVoidDetection = ["true"]
    setFusionResolution = ["true"]
    setRestructureResolution = ["true"]
    setFrontierRequest = ["false"]

    launch()

    # add Range Ambiguity NCS

    setSelfModelRequest = ["true"]
    setConflictDetection = ["true"]
    setConcurrenceDetection = ["true"]
    setVoidDetection = ["true"]
    setFusionResolution = ["true"]
    setRestructureResolution = ["true"]
    setFrontierRequest = ["true"]

    launch()

    transpose.transposeFilesWithPaths("XP", "TFiles")

    a_barPlot_passiveAndActiveLearningSituations.generateFigures()
    b_barplot_inaccuraciesVolumes.generateFigures()
    c_barPlot_nbAgents.generateFigures()
    d_barPlot_generalizationScore.generateFigures()
    e_barPlot_predictionError.generateFigures()
    f_barPlot_learningInaccuraciesNCSCounts.generateFigures()













