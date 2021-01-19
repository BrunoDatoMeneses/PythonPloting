import itertools
import os

if __name__ == "__main__":


    dimensions = ["2",'3','4','5','10']
    configFiles = ["twoDimensionsLauncher","threeDimensionsLauncher","fourDimensionsLauncher","fiveDimensionsLauncher","tenDimensionsLauncher"]

    learningCycles = ["50"]
    exploitationCycles = ["10"]
    #episodes = ["2","5","10","20"]
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

    # Other

    models = ["SquareFixed"]
    setbootstrapCycles = ["10"]

    for dimension,configFile in zip(dimensions,configFiles):
        for iteration in itertools.product(learningCycles, exploitationCycles, episodes, precisionRanges,
                                       neighborhoodMultiplicators,
                                       externalInfluenceRatios, regressionPerformances, activeLearning, selfLearning,
                                       setConflictDetection, setConcurrenceDetection, setVoidDetection,
                                       setSubVoidDetection,
                                       setFrontierRequest, setSelfModelRequest, setFusionResolution,
                                       setRestructureResolution,
                                       setDream, setDreamCycleLaunch,
                                       setLearnFromNeighbors, nbOfNeighborForLearningFromNeighbors,
                                       nbOfNeighborForContexCreationWithouOracle,
                                       models, setbootstrapCycles):


            fileName = dimension + "_"
            arguments = dimension + " " + configFile + " "
            for arg in iteration:
                arguments += arg + " "
                fileName += arg + "_"

            print(arguments)
            arguments += fileName

            os.system("java -jar ELLSA.jar " + arguments)
            print("")
