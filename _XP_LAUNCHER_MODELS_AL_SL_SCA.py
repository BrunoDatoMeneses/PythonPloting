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
    learningCycles = ["4000"]
    exploitationCycles = ["250"]


    # Neighborhood
    precisionRanges = ["0.03"]
    neighborhoodMultiplicators = ["2"]
    externalInfluenceRatios = ["0.5"]
    regressionPerformances = ["1.0"]

    # Learning
    activeLearning = ["true"]
    selfLearning = ["false"]


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

    setLearnFromNeighbors = ["false"]

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

    transferRatio = ["0.0"]

    endoExploitationCycles = ["1000"]
    isActiveExploitation = ["false"]
    noiseRange = ["0.0"]

    # listOfPrecisionRanges = ["0.02", "0.06", "0.1"]
    listOfPrecisionRanges = [ "0.1"]
    # listOfPrecisionRanges = ["0.1"]
    listOfLearningCycles = [ "2000"]

    listOfModels = ["squareFixed"]
    listOfRegressionPerf = ["1.0"]

    # listOfdimensions = ['2','3','5','10']
    # listOfconfigFiles = ["twoDimensionsLauncher","threeDimensionsLauncher","fiveDimensionsLauncher","tenDimensionsLauncher"]

    # listOfdimensions = ['5', '10']
    # listOfconfigFiles = ["fiveDimensionsLauncher",
    #                      "tenDimensionsLauncher"]

    listOfdimensions = ['10']
    listOfconfigFiles = ["tenDimensionsLauncher"]

    # listOfBoostrapCycles = ["10", "50", "100"]
    listOfBoostrapCycles = ["10"]



    listOfsetSelfModelRequest =         ["true","false","false","false","false","false","false","true"]
    listOfsetConflictDetection =        ["false","true","false","false","false","false","false","true"]
    listOfsetConcurrenceDetection =     ["false","false","true","false","false","false","false","true"]
    listOfsetVoidDetection =            ["false","false","false","true","false","false","false","true"]
    listOfsetFusionResolution =         ["false","false","false","false","true","false","false","true"]
    listOfsetRestructureResolution =    ["false","false","false","false","false","true","false","true"]
    listOfsetFrontierRequest =          ["false","false","false","false","false","false","true","true"]

    listOfisAllContextSearchAllowedForLearning = ["true","false"]
    listOfisAllContextSearchAllowedForExploitation = ["true","false"]

    # # SELF LEARNING
    # activeLearning = ["false"]
    # selfLearning = ["true"]
    # setLearnFromNeighbors = ["true"]

    # ACTIVE LEARNING
    activeLearning = ["true"]
    selfLearning = ["false"]
    setLearnFromNeighbors = ["false"]

    # for allCtxtLrn, allCtxtExpl in zip(listOfisAllContextSearchAllowedForLearning,listOfisAllContextSearchAllowedForExploitation):
    #     isAllContextSearchAllowedForLearning = [allCtxtLrn]
    #     isAllContextSearchAllowedForExploitation = [allCtxtExpl]

    listOfEpisodes = ["1","2","3","4","5","7","10"]

    for eps in listOfEpisodes:
        episodes =[eps]

        for d, conf in zip(listOfdimensions, listOfconfigFiles):
            dimensions = [d]
            configFiles = [conf]

            for mod, perf in zip(listOfModels, listOfRegressionPerf):
                models = [mod]
                regressionPerformances = [perf]

                for prRg in listOfPrecisionRanges:
                    precisionRanges = [prRg]

                    for lrnCl in listOfLearningCycles:
                        learningCycles = [lrnCl]

                        for boot in listOfBoostrapCycles:
                            setbootstrapCycles = [boot]

                            launch()









