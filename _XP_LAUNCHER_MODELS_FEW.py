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

    # dimensions = ['2', '3', '4', '5']
    # configFiles = ["twoDimensionsLauncher", "threeDimensionsLauncher", "fourDimensionsLauncher",
    #                "fiveDimensionsLauncher"]

    # dimensions = ['2','3','4','5','10']
    # configFiles = ["twoDimensionsLauncher","threeDimensionsLauncher","fourDimensionsLauncher","fiveDimensionsLauncher","tenDimensionsLauncher"]

    dimensions = ['2']
    configFiles = ["twoDimensionsLauncher"]

    # learningCycles = []
    # for i in range(1,5):
    #     learningCycles.append(""+ str(i*500))
    # print(learningCycles)
    # learningCycles = ["50","100","150","500","1000","2000","5000","10000"]
    learningCycles = ["200"]
    exploitationCycles = ["250"]
    episodes = ["15"]

    # Neighborhood
    precisionRanges = ["0.02"]
    neighborhoodMultiplicators = ["2"]
    externalInfluenceRatios = ["0.5"]
    regressionPerformances = ["0.05"]




    # NCS

    setSelfModelRequest = ["true"]
    setConflictDetection = ["true"]
    setConcurrenceDetection = ["true"]
    setVoidDetection = ["false"]
    setFusionResolution = ["true"]
    setRestructureResolution = ["true"]
    setFrontierRequest = ["true"]

    # NCS

    # setSelfModelRequest = ["true"]
    # setConflictDetection = ["false"]
    # setConcurrenceDetection = ["false"]
    # setVoidDetection = ["false"]
    # setFusionResolution = ["false"]
    # setRestructureResolution = ["false"]
    # setFrontierRequest = ["false"]



    setSubVoidDetection = ["false"]

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



    nbOfNeighborForLearningFromNeighbors = ["1"]
    nbOfNeighborForContexCreationWithouOracle = ["7"]
    setCreationFromNeighbor = ["true"]

    # Other
# squareFixed, triangle, disc, squareDiag, squareDiagCircle
# // PARAMS.model = "multi";
# // PARAMS.model = "disc";
# // PARAMS.model = "square";
# // PARAMS.model = "squareFixed";
# // PARAMS.model = "triangle";
# // PARAMS.model = "gaussian";
# // PARAMS.model = "polynomial";
# // PARAMS.model = "gaussianCos2";
# // PARAMS.model = "cosX";
# // PARAMS.model = "cosSinX";
# // PARAMS.model = "rosenbrock";
# // PARAMS.model = "squareSplitTriangle";
# // PARAMS.model = "squareSplitFixed";

    models = ["cosSinX"]
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

    transferRatio = ["0.333"]

    endoExploitationCycles = ["0"]
    isActiveExploitation = ["false"]

    noiseRange = ["0.0"]

    listOfPrecisionRg = ["0.02","0.04","0.06"]
    listOfNeighboords = ["2", "6", "8","10" ]
    listOfInfluences = ["0.5", "1.0", "2.0", "4.0"]
    listOfEndogenousLearningW = ["0.05","0.1", "0.25","0.5"]
    listOfExogenousLearningW = ["0.05", "0.1", "0.15", "0.2"]



    listOfModels = ["gaussianCos2","cosSinX"]
    listOfRegressionPerf = ["1.0","0.05"]

    learningCycles = ["50"]
    precisionRanges = ["0.02"]
    neighborhoodMultiplicators = ["2"]
    externalInfluenceRatios = ["0.5"]
    endogenousLearningWeight = ["0.1"]
    exogenousLearningWeight = ["0.1"]


    for mod,perf in zip(listOfModels,listOfRegressionPerf):
        models = [mod]
        regressionPerformances = [perf]

        learningCycles = ["50"]
        precisionRanges = ["0.02"]
        neighborhoodMultiplicators = ["2"]
        externalInfluenceRatios = ["0.5"]
        endogenousLearningWeight = ["0.1"]
        exogenousLearningWeight = ["0.1"]

        # # SELF LEARNING
        # activeLearning = ["false"]
        # selfLearning = ["true"]
        # setLearnFromNeighbors = ["true"]
        #
        # setSelfModelRequest = ["true"]
        # setConflictDetection = ["true"]
        # setConcurrenceDetection = ["true"]
        # setVoidDetection = ["false"]
        # setFusionResolution = ["true"]
        # setRestructureResolution = ["true"]
        # setFrontierRequest = ["true"]
        #
        # setCreationFromNeighbor = ["true"]
        #
        # launch()

        # NAIVE LEARNING
        activeLearning = ["false"]
        selfLearning = ["true"]
        setLearnFromNeighbors = ["false"]

        setSelfModelRequest = ["false"]
        setConflictDetection = ["false"]
        setConcurrenceDetection = ["false"]
        setVoidDetection = ["false"]
        setFusionResolution = ["false"]
        setRestructureResolution = ["false"]
        setFrontierRequest = ["false"]

        setCreationFromNeighbor = ["false"]

        launch()

        # # SELF LEARNING
        # activeLearning = ["false"]
        # selfLearning = ["true"]
        # setLearnFromNeighbors = ["true"]
        #
        # listOfPrecisionRg = ["0.02", "0.04", "0.06"]
        # listOfNeighboords = ["2", "6", "8", "10"]
        # listOfInfluences = ["0.5", "1.0", "2.0", "4.0"]
        # listOfEndogenousLearningW = ["0.05", "0.1", "0.25", "0.5"]
        # listOfExogenousLearningW = ["0.05", "0.1", "0.15", "0.2"]
        # learningCycles = ["200"]
        # precisionRanges = ["0.02"]
        # neighborhoodMultiplicators = ["2"]
        # externalInfluenceRatios = ["0.5"]
        # endogenousLearningWeight = ["0.1"]
        # exogenousLearningWeight = ["0.1"]
        #
        # for rg in listOfPrecisionRg:
        #     precisionRanges = [rg]
        #     launch()
        #
        # listOfPrecisionRg = ["0.02", "0.04", "0.06"]
        # listOfNeighboords = ["2", "6", "8", "10"]
        # listOfInfluences = ["0.5", "1.0", "2.0", "4.0"]
        # listOfEndogenousLearningW = ["0.05", "0.1", "0.25", "0.5"]
        # listOfExogenousLearningW = ["0.05", "0.1", "0.15", "0.2"]
        # learningCycles = ["200"]
        # precisionRanges = ["0.02"]
        # neighborhoodMultiplicators = ["2"]
        # externalInfluenceRatios = ["0.5"]
        # endogenousLearningWeight = ["0.1"]
        # exogenousLearningWeight = ["0.1"]
        #
        # for nh in listOfNeighboords:
        #     neighborhoodMultiplicators = [nh]
        #     launch()
        #
        # listOfPrecisionRg = ["0.02", "0.04", "0.06"]
        # listOfNeighboords = ["2", "6", "8", "10"]
        # listOfInfluences = ["0.5", "1.0", "2.0", "4.0"]
        # listOfEndogenousLearningW = ["0.05", "0.1", "0.25", "0.5"]
        # listOfExogenousLearningW = ["0.05", "0.1", "0.15", "0.2"]
        # learningCycles = ["200"]
        # precisionRanges = ["0.02"]
        # neighborhoodMultiplicators = ["2"]
        # externalInfluenceRatios = ["0.5"]
        # endogenousLearningWeight = ["0.1"]
        # exogenousLearningWeight = ["0.1"]
        #
        # for infl in listOfInfluences:
        #     externalInfluenceRatios = [infl]
        #     launch()
        #
        # listOfPrecisionRg = ["0.02", "0.04", "0.06"]
        # listOfNeighboords = ["2", "6", "8", "10"]
        # listOfInfluences = ["0.5", "1.0", "2.0", "4.0"]
        # listOfEndogenousLearningW = ["0.05", "0.1", "0.25", "0.5"]
        # listOfExogenousLearningW = ["0.05", "0.1", "0.15", "0.2"]
        # learningCycles = ["200"]
        # precisionRanges = ["0.02"]
        # neighborhoodMultiplicators = ["2"]
        # externalInfluenceRatios = ["0.5"]
        # endogenousLearningWeight = ["0.1"]
        # exogenousLearningWeight = ["0.1"]
        #
        # for endoW in listOfEndogenousLearningW:
        #     endogenousLearningWeight = [endoW]
        #     launch()
        #
        # listOfPrecisionRg = ["0.02", "0.04", "0.06"]
        # listOfNeighboords = ["2", "6", "8", "10"]
        # listOfInfluences = ["0.5", "1.0", "2.0", "4.0"]
        # listOfEndogenousLearningW = ["0.05", "0.1", "0.25", "0.5"]
        # listOfExogenousLearningW = ["0.05", "0.1", "0.15", "0.2"]
        # learningCycles = ["4000"]
        # precisionRanges = ["0.02"]
        # neighborhoodMultiplicators = ["2"]
        # externalInfluenceRatios = ["0.5"]
        # endogenousLearningWeight = ["0.1"]
        # exogenousLearningWeight = ["0.1"]
        #
        # for exoW in listOfExogenousLearningW:
        #     exogenousLearningWeight = [exoW]
        #     launch()











