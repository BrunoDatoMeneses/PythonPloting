import itertools
import os

if __name__ == "__main__":


    dimensions = ["2",'3','4','5','10']
    configFiles = ["twoDimensionsLauncher","threeDimensionsLauncher","fourDimensionsLauncher","fiveDimensionsLauncher","tenDimensionsLauncher"]

    learningCycles = ["250","500","1000","2000","5000","10000","20000"]
    exploitationCycles = ["250"]
    episodes = ["5","10","20","50"]

    # Neighborhood
    precisionRanges = ["0.04", "0.06", "0.08" ,"0.10"]
    neighborhoodMultiplicators = ["2"]
    externalInfluenceRatios = ["0.25"]
    regressionPerformances = ["1"]

    # Learning
    activeLearning = ["true"]
    selfLearning = ["false"]

    # NCS
    setConflictDetection = ["true","false"]
    setConcurrenceDetection = ["true","false"]
    setVoidDetection = ["true","false"]
    setSubVoidDetection = ["false"]
    setFrontierRequest = ["true","false"]
    setSelfModelRequest = ["true","false"]
    setFusionResolution = ["true","false"]
    setRestructureResolution = ["true","false"]

    setDream = ["false"]
    setDreamCycleLaunch = ["1500"]

    setLearnFromNeighbors = ["false"]
    nbOfNeighborForLearningFromNeighbors = ["1"]
    nbOfNeighborForContexCreationWithouOracle = ["50000"]

    # Other

    models = ["SquareFixed"]
    setbootstrapCycles = ["10","50","100","200"]

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
