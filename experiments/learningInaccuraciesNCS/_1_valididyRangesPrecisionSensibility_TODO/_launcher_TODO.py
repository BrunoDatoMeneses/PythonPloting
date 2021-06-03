#!/usr/bin/env python3
import itertools
import os


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
                else:
                    fileName += arg + "_"

                argumentsList.append(arg)

            print(arguments, "ARGS SIZE : " + str(len(argumentsList) + 1))

            arguments += fileName
            argumentsList.append(fileName)

            os.system("java -jar Jars/ELLSA.jar " + arguments)
            print("")


if __name__ == "__main__":



    dimensions = ['2']
    configFiles = ["twoDimensionsLauncher"]

    learningCycles = ["500"]
    exploitationCycles = ["250"]
    episodes = ["15"]

    # Neighborhood
    precisionRanges = ["0.1"]
    neighborhoodMultiplicators = ["2"]
    externalInfluenceRatios = ["0.5"]
    regressionPerformances = ["1.0"]

    # NCS

    setSelfModelRequest = ["true"]
    setConflictDetection = ["true"]
    setConcurrenceDetection = ["true"]
    setVoidDetection = ["true"]
    setFusionResolution = ["true"]
    setRestructureResolution = ["true"]
    setFrontierRequest = ["true"]

    setSubVoidDetection = ["false"]

    setDream = ["false"]
    setDreamCycleLaunch = ["1500"]


    nbOfNeighborForLearningFromNeighbors = ["1"]
    nbOfNeighborForContexCreationWithouOracle = ["7"]
    setCreationFromNeighbor = ["true"]

    models = ["squareFixed"]
    setbootstrapCycles = ["10"]

    exogenousLearningWeight= ["0.1"]
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

    transferRatio = ["0.0"]

    endoExploitationCycles = ["1000"]
    isActiveExploitation = ["false"]
    noiseRange = ["0.0"]

    # ACTIVE LEARNING
    activeLearning = ["true"]
    selfLearning = ["false"]
    setLearnFromNeighbors = ["false"]

    # listOfValaidityRanges = ["0.02","0.05","0.1","0.15","0.2"]
    listOfValaidityRanges = [ "0.05", "0.1", "0.15", "0.2"]
    listOfValaidityRanges = ["0.1"]

    # NCS

    setSelfModelRequest = ["true"]
    setConflictDetection = ["true"]
    setConcurrenceDetection = ["true"]
    setVoidDetection = ["true"]
    setFusionResolution = ["true"]
    setRestructureResolution = ["true"]
    setFrontierRequest = ["true"]

    for rg in listOfValaidityRanges:
        precisionRanges = [rg]
        launch()

    listOfValaidityRanges = ["0.1"]

    # NCS

    setSelfModelRequest = ["false"]
    setConflictDetection = ["false"]
    setConcurrenceDetection = ["false"]
    setVoidDetection = ["false"]
    setFusionResolution = ["false"]
    setRestructureResolution = ["false"]
    setFrontierRequest = ["false"]

    for rg in listOfValaidityRanges:
        precisionRanges = [rg]
        launch()

    # NCS

    setSelfModelRequest = ["true"]
    setConflictDetection = ["false"]
    setConcurrenceDetection = ["false"]
    setVoidDetection = ["false"]
    setFusionResolution = ["false"]
    setRestructureResolution = ["false"]
    setFrontierRequest = ["false"]

    for rg in listOfValaidityRanges:
        precisionRanges = [rg]
        launch()


    # NCS

    setSelfModelRequest = ["true"]
    setConflictDetection = ["true"]
    setConcurrenceDetection = ["false"]
    setVoidDetection = ["false"]
    setFusionResolution = ["false"]
    setRestructureResolution = ["false"]
    setFrontierRequest = ["false"]

    for rg in listOfValaidityRanges:
        precisionRanges = [rg]
        launch()


    # NCS

    setSelfModelRequest = ["true"]
    setConflictDetection = ["true"]
    setConcurrenceDetection = ["true"]
    setVoidDetection = ["false"]
    setFusionResolution = ["false"]
    setRestructureResolution = ["false"]
    setFrontierRequest = ["false"]

    for rg in listOfValaidityRanges:
        precisionRanges = [rg]
        launch()


    # NCS

    setSelfModelRequest = ["true"]
    setConflictDetection = ["true"]
    setConcurrenceDetection = ["true"]
    setVoidDetection = ["true"]
    setFusionResolution = ["false"]
    setRestructureResolution = ["false"]
    setFrontierRequest = ["false"]

    for rg in listOfValaidityRanges:
        precisionRanges = [rg]
        launch()



    # NCS

    setSelfModelRequest = ["true"]
    setConflictDetection = ["true"]
    setConcurrenceDetection = ["true"]
    setVoidDetection = ["true"]
    setFusionResolution = ["true"]
    setRestructureResolution = ["false"]
    setFrontierRequest = ["false"]

    for rg in listOfValaidityRanges:
        precisionRanges = [rg]
        launch()



    setSelfModelRequest = ["true"]
    setConflictDetection = ["true"]
    setConcurrenceDetection = ["true"]
    setVoidDetection = ["true"]
    setFusionResolution = ["true"]
    setRestructureResolution = ["true"]
    setFrontierRequest = ["false"]

    for rg in listOfValaidityRanges:
        precisionRanges = [rg]
        launch()












