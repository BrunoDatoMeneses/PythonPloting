import itertools
import os

if __name__ == "__main__":


    # dimensions = ['2','3','4','5','10']
    # configFiles = ["twoDimensionsLauncher","threeDimensionsLauncher","fourDimensionsLauncher","fiveDimensionsLauncher","tenDimensionsLauncher"]

    dimensions = ['4','5','10']
    configFiles = ["fourDimensionsLauncher","fiveDimensionsLauncher","tenDimensionsLauncher"]

    learningCycles = ["2000","5000","10000"]
    exploitationCycles = ["250"]
    episodes = ["10"]

    # Neighborhood
    precisionRanges = ["0.10"]
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

    # setConflictDetection = ["true","false"]
    # setConcurrenceDetection = ["true","false"]
    # setVoidDetection = ["true","false"]
    # setSubVoidDetection = ["false"]
    # setFrontierRequest = ["true","false"]
    # setSelfModelRequest = ["true","false"]
    # setFusionResolution = ["true","false"]
    # setRestructureResolution = ["true","false"]

    setDream = ["false"]
    setDreamCycleLaunch = ["1500"]

    setLearnFromNeighbors = ["false"]
    nbOfNeighborForLearningFromNeighbors = ["1"]
    nbOfNeighborForContexCreationWithouOracle = ["50000"]
    setCreationFromNeighbor = ["true"]

    # Other

    models = ["SquareFixed"]
    setbootstrapCycles = ["10"]

    for dimension,configFile in zip(dimensions,configFiles):
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
                                           models, setbootstrapCycles):


            fileName = dimension + "_"
            arguments = dimension + " " + configFile + " "
            argumentsList = [dimension, configFile]
            for arg in iteration:
                arguments += arg + " "
                fileName += arg + "_"
                argumentsList.append(arg)

            print(arguments, "ARGS SIZE : " + str(len(argumentsList)+1))

            arguments += fileName
            argumentsList.append(fileName)

            os.system("java -jar ELLSA.jar " + arguments)
            print("")
