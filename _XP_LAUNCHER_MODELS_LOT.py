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
    learningCycles = ["2000"]
    exploitationCycles = ["250"]
    episodes = ["15"]

    # Neighborhood
    precisionRanges = ["0.04"]
    neighborhoodMultiplicators = ["2"]
    externalInfluenceRatios = ["0.5"]
    regressionPerformances = ["0.05"]

    # Learning
    activeLearning = ["false"]
    selfLearning = ["true"]
    setLearnFromNeighbors = ["true"]


    # NCS

    setSelfModelRequest = ["true"]
    setConflictDetection = ["true"]
    setConcurrenceDetection = ["true"]
    setVoidDetection = ["false"]
    setFusionResolution = ["true"]
    setRestructureResolution = ["true"]
    setFrontierRequest = ["true"]



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



    # listOfLearningCycles = ["500", "1000","2000"]
    # ListOfPrecisionRanges = ["0.03", "0.04","0.05"]
    # listOfEndoExploitationCycles = ["500", "1000", "2000", "4000", "6000"]

    listOfPrecisionRanges = ["0.02","0.04","0.06"]
    listOfExogenousLearningW = ["0.05", "0.15","0.2"]
    listOfLearningCycles = ["250","500","1000","2000","4000"]

    listOfModels = ["gaussianCos2","cosSinX"]
    listOfRegressionPerf = ["1.0","0.05"]

    neighborhoodMultiplicators = ["2"]
    externalInfluenceRatios = ["0.5"]
    endogenousLearningWeight = ["0.1"]

    # SELF LEARNING
    activeLearning = ["false"]
    selfLearning = ["true"]
    setLearnFromNeighbors = ["true"]

    for mod,perf in zip(listOfModels,listOfRegressionPerf):
        models = [mod]
        regressionPerformances = [perf]

        for exoW in listOfExogenousLearningW:
            exogenousLearningWeight=[exoW]

            for prRg in listOfPrecisionRanges:
                precisionRanges=[prRg]

                for lrnCl in listOfLearningCycles:
                    learningCycles = [lrnCl]

                    launch()

    # # ACTIVE LEARNING
    # activeLearning = ["true"]
    # selfLearning = ["false"]
    # setLearnFromNeighbors = ["false"]
    #
    # for mod, perf in zip(listOfModels, listOfRegressionPerf):
    #     models = [mod]
    #     regressionPerformances = [perf]
    #
    #     for exoW in listOfExogenousLearningW:
    #         exogenousLearningWeight = [exoW]
    #
    #         for prRg in listOfPrecisionRanges:
    #             precisionRanges = [prRg]
    #
    #             for lrnCl in listOfLearningCycles:
    #                 learningCycles = [lrnCl]
    #
    #                 launch()





