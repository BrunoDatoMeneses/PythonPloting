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
    precisionRanges = ["0.02"]
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
    setVoidDetection = ["true"]
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
    isActiveExploitation = ["true"]

    noiseRange = ["0.0"]



    # listOfLearningCycles = ["500", "1000","2000"]
    # ListOfPrecisionRanges = ["0.03", "0.04","0.05"]

    listOfEndoExploitationCycles = ["0", "1000", "10000", "20000", "100000"]
    listOfLearningCycles = ["2000"]

    ListOfEndoLeanringWeight = ["0.05","0.1","0.2","0.5"]
    listOfNeighboords = ["2", "4", "6", "8"]
    listOfInfluences = ["0.5","1.0", "2.0", "4.0"]

    listOfPrecisionRanges = ["0.02","0.04","0.06"]




    perceptionsGenerationCoefficient = ["0.1"]

    # SELF LEARNING
    activeLearning = ["false"]
    selfLearning = ["true"]
    setLearnFromNeighbors = ["true"]

    # for endoXP in listOfEndoExploitationCycles:
    #     endoExploitationCycles = [endoXP]
    #
    #     for rg in listOfPrecisionRanges:
    #         precisionRanges = [rg]
    #         launch()


    endoExploitationCycles = ["10000"]
    precisionRanges = ["0.02"]

    ListOfEndoLeanringWeight = ["0.05", "0.1", "0.2", "0.5"]
    listOfNeighboords = ["2", "4", "6", "8"]
    listOfInfluences = ["0.5", "1.0", "2.0", "4.0"]


    endogenousLearningWeight = ["0.1"]
    neighborhoodMultiplicators = ["2"]
    externalInfluenceRatios = ["0.5"]

    for endoW in ListOfEndoLeanringWeight:
        endogenousLearningWeight = [endoW]
        launch()

    endogenousLearningWeight = ["0.1"]
    neighborhoodMultiplicators = ["2"]
    externalInfluenceRatios = ["0.5"]

    for nh in listOfNeighboords:
        neighborhoodMultiplicators = [nh]
        launch()

    endogenousLearningWeight = ["0.1"]
    neighborhoodMultiplicators = ["2"]
    externalInfluenceRatios = ["0.5"]

    for infl in listOfInfluences:
        externalInfluenceRatios = [infl]
        launch()


