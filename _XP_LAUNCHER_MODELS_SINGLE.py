#!/usr/bin/env python3
import itertools
import os

if __name__ == "__main__":


    dimensions = ["2"]
    configFiles = ["twoDimensionsLauncher"]


    learningCycles = ["1000"]
    exploitationCycles = ["250"]
    episodes = ["1"]

    # Neighborhood
    precisionRanges = ["0.05"]
    neighborhoodMultiplicators = ["2"]
    externalInfluenceRatios = ["0.25"]
    regressionPerformances = ["0.05"]

    # Learning
    activeLearning = ["false"]
    selfLearning = ["true"]
    setLearnFromNeighbors = ["true"]

    # NCS
    setConflictDetection = ["true"]
    setConcurrenceDetection = ["true"]
    setVoidDetection = ["true"]
    setSubVoidDetection = ["false"]
    setFrontierRequest = ["true"]
    setSelfModelRequest = ["true"]
    setFusionResolution = ["true"]
    setRestructureResolution = ["true"]


    setDream = ["false"]
    setDreamCycleLaunch = ["1500"]


    nbOfNeighborForLearningFromNeighbors = ["1"]
    nbOfNeighborForContexCreationWithouOracle = ["7"]
    setCreationFromNeighbor = ["true"]

    # Other

    models = ["cosSinX"]
    setbootstrapCycles = ["10"]

    exogenousLearningWeight = ["0.1"]
    endogenousLearningWeight = ["0.1"]

    LEARNING_WEIGHT_ACCURACY = ["1.0"]
    LEARNING_WEIGHT_PROXIMITY = ["0.0"]
    LEARNING_WEIGHT_EXPERIENCE = ["1.0"]
    LEARNING_WEIGHT_GENERALIZATION = ["1.0"]

    EXPLOITATION_WEIGHT_PROXIMITY = ["1.0"]
    EXPLOITATION_WEIGHT_EXPERIENCE = ["1.0"]
    EXPLOITATION_WEIGHT_GENERALIZATION = ["1.0"]

    perceptionsGenerationCoefficient = ["0.1"]
    modelSimilarityThreshold = ["0.001"]

    maxRangeRadiusCoefficient = ["2.0"]
    rangeSimilarityCoefficient = ["0.375"]
    minimumRangeCoefficient = ["0.25"]

    isAllContextSearchAllowedForLearning = ["true"]
    isAllContextSearchAllowedForExploitation = ["true"]
    probabilityOfRangeAmbiguity = ["0.1"]

    transferRatio = ["0.333"]

    endoExploitationCycles = ["1000"]
    isActiveExploitation = ["true"]
    noiseRange = ["0.0"]

    for iteration in itertools.product(learningCycles, exploitationCycles, episodes, precisionRanges, neighborhoodMultiplicators,
                               externalInfluenceRatios, regressionPerformances, activeLearning, selfLearning,
                               setConflictDetection, setConcurrenceDetection, setVoidDetection, setSubVoidDetection,
                               setFrontierRequest, setSelfModelRequest, setFusionResolution, setRestructureResolution,
                               setDream, setDreamCycleLaunch,
                               setLearnFromNeighbors, nbOfNeighborForLearningFromNeighbors, nbOfNeighborForContexCreationWithouOracle,
                               setCreationFromNeighbor,
                               models, setbootstrapCycles,
                               exogenousLearningWeight, endogenousLearningWeight,
                               LEARNING_WEIGHT_ACCURACY, LEARNING_WEIGHT_PROXIMITY, LEARNING_WEIGHT_EXPERIENCE,
                               LEARNING_WEIGHT_GENERALIZATION,
                               EXPLOITATION_WEIGHT_PROXIMITY, EXPLOITATION_WEIGHT_EXPERIENCE,
                               EXPLOITATION_WEIGHT_GENERALIZATION,
                               perceptionsGenerationCoefficient, modelSimilarityThreshold,
                               maxRangeRadiusCoefficient, rangeSimilarityCoefficient, minimumRangeCoefficient,
                               isAllContextSearchAllowedForLearning, isAllContextSearchAllowedForExploitation,
                                       probabilityOfRangeAmbiguity, transferRatio,
                                           endoExploitationCycles,isActiveExploitation,
                                           noiseRange
                               ):

        arguments = dimensions[0] + " " + configFiles[0] + " "
        argumentsList = [dimensions[0], configFiles[0]]

        fileName = dimensions[0] + "_"

        for arg in iteration:
            arguments += arg + " "
            if arg == "true":
                fileName += "t" + "_"
            elif arg == "false":
                fileName += "f" + "_"
            else:
                fileName += arg + "_"

            argumentsList.append(arg)

        print(arguments, "ARGS SIZE : " + str(len(argumentsList) + 1))
        print(fileName)

        arguments += fileName
        argumentsList.append(fileName)

        os.system("java -jar Jars/ELLSA.jar " + arguments)
        print("")



    # arguments = dimensions + " " \
    #             + learningCycles + " " \
    #             + exploitationCycles + " " \
    #             + episodes + " " \
    #             + precisionRanges + " " \
    #             + neighborhoodMultiplicators + " " \
    #             + externalInfluenceRatios + " " \
    #             + regressionPerformances + " " \
    #             + activeLearning + " " \
    #             + selfLearning + " " \
    #             + setConflictDetection + " " \
    #             + setConcurrenceDetection + " " \
    #             + setVoidDetection + " " \
    #             + setSubVoidDetection + " " \
    #             + setFrontierRequest + " " \
    #             + setSelfModelRequest + " " \
    #             + setFusionResolution + " " \
    #             + setRestructureResolution + " " \
    #             + setDream + " " \
    #             + setDreamCycleLaunch + " " \
    #             + setLearnFromNeighbors + " " \
    #             + nbOfNeighborForLearningFromNeighbors + " " \
    #             + nbOfNeighborForContexCreationWithouOracle + " " \
    #             + configFiles + " " \
    #             + models + " " \
    #             + extensions + " " \
    #             + setbootstrapCycles + " "
    #
    #
    # os.system("java -jar ELLSA.jar "+ arguments)
    # print("")