import itertools
import os

if __name__ == "__main__":


    dimensions = ["2"]
    configFiles = ["twoDimensionsLauncher"]


    learningCycles = ["1000"]
    exploitationCycles = ["250"]
    episodes = ["1"]

    # Neighborhood
    precisionRanges = ["0.08"]
    neighborhoodMultiplicators = ["2"]
    externalInfluenceRatios = ["0.25"]
    regressionPerformances = ["1"]

    # Learning
    activeLearning = ["true"]
    selfLearning = ["false"]

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

    setLearnFromNeighbors = ["false"]
    nbOfNeighborForLearningFromNeighbors = ["1"]
    nbOfNeighborForContexCreationWithouOracle = ["50000"]
    setCreationFromNeighbor = ["true"]

    # Other

    models = ["SquareFixed"]
    setbootstrapCycles = ["10"]

    for iteration in itertools.product(learningCycles, exploitationCycles, episodes, precisionRanges, neighborhoodMultiplicators,
                               externalInfluenceRatios, regressionPerformances, activeLearning, selfLearning,
                               setConflictDetection, setConcurrenceDetection, setVoidDetection, setSubVoidDetection,
                               setFrontierRequest, setSelfModelRequest, setFusionResolution, setRestructureResolution,
                               setDream, setDreamCycleLaunch,
                               setLearnFromNeighbors, nbOfNeighborForLearningFromNeighbors, nbOfNeighborForContexCreationWithouOracle,
                               setCreationFromNeighbor,
                               models, setbootstrapCycles):

        arguments = dimensions[0] + " " + configFiles[0] + " "
        fileName = ""
        for arg in iteration:
            arguments += arg + " "
            fileName += arg + "_"

        print(arguments)
        arguments+=fileName

        os.system("java -jar ELLSA.jar " + arguments)
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