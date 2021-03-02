class PARAMETERS:
    """PARAMETERS"""

    figSize = (6, 3.75)
    # figSize = (8,4.5)
    # figSize = (16,9)

    dimension = "2"
    model = "squareFixed"
    learningCycles = "500"
    exploitatingCycles = "250"
    episodes = "15"

    validityRangesPrecision = "0.1"

    isActiveLearning = "true"
    isSelfLearning = "false"

    LEARNING_WEIGHT_ACCURACY = "1.0"
    LEARNING_WEIGHT_PROXIMITY = "0.0"
    LEARNING_WEIGHT_EXPERIENCE = "1.0"
    LEARNING_WEIGHT_GENERALIZATION = "1.0"

    EXPLOITATION_WEIGHT_PROXIMITY = "1.0"
    EXPLOITATION_WEIGHT_EXPERIENCE = "1.0"
    EXPLOITATION_WEIGHT_GENERALIZATION = "1.0"

    errorMargin = "1.0"

    exogenousLearningWeight = "0.1"
    endogenousLearningWeight = "0.1"
    perceptionsGenerationCoefficient = "0.1"

    modelSimilarityThreshold = "0.001"

    bootstrapCycle = "10"

    neighborhoodRadiusCoefficient = "2.0"
    influenceRadiusCoefficient = "0.5"
    maxRangeRadiusCoefficient = "2.0"
    rangeSimilarityCoefficient = "0.375"
    minimumRangeCoefficient = "0.25"

    isConflictNCS = "true"
    isConcurenceNCS = "true"
    isIncompetenceNCS = "true"
    isSubVoidDetection = "false"
    isAmbiguityNCS = "true"
    isModelNCS = "true"

    isLearnFromNeighbors = "false"
    isDream = "false"
    isFusionResolution = "true"
    isRetructureResolution = "true"

    dreamLaunch = "1500"
    nbOfNeighborForLearningFromNeighbors = "1"
    nbOfNeighborForContexCreationWithouOracle = "7"

    isCreationFromNeighbor = "true"
    isAllContextSearchAllowedForLearning = "true"
    isAllContextSearchAllowedForExploitation = "true"
    probabilityOfRangeAmbiguity = "0.1"

    isActiveExploitation = "false"
    activeExploitationCycles = "1000"

    noise = "0.0"

    figPrefix = model + "_"



    PARAMS_STRINGS = ["dimension", "learningCycles", "exploitatingCycles", "episodes", "validityRangesPrecision",
                      "neighborhoodRadiusCoefficient", "influenceRadiusCoefficient",
                      "isActiveLearning", "isSelfLearning", "errorMargin", "bootstrapCycle",
                      "isConflictNCS", "isConcurenceNCS", "isIncompetenceNCS", "isSubVoidDetection", "isAmbiguityNCS",
                      "isModelNCS", "isLearnFromNeighbors", "isDream",
                      "isFusionResolution",    "isRetructureResolution",
                      "dreamLaunch", "nbOfNeighborForLearningFromNeighbors",
                      "nbOfNeighborForContexCreationWithouOracle",

                      "isCreationFromNeighbor", "model",
                      "exogenousLearningWeight",
                      "endogenousLearningWeight",

                      "LEARNING_WEIGHT_ACCURACY",
                      "LEARNING_WEIGHT_PROXIMITY",
                      "LEARNING_WEIGHT_EXPERIENCE",
                      "LEARNING_WEIGHT_GENERALIZATION",

                      "EXPLOITATION_WEIGHT_PROXIMITY",
                      "EXPLOITATION_WEIGHT_EXPERIENCE",
                      "EXPLOITATION_WEIGHT_GENERALIZATION",

                      "perceptionsGenerationCoefficient",
                      "modelSimilarityThreshold",

                      "maxRangeRadiusCoefficient",
                      "rangeSimilarityCoefficient",
                      "minimumRangeCoefficient",

                      "isAllContextSearchAllowedForLearning",
                      "isAllContextSearchAllowedForExploitation",
                      "probabilityOfRangeAmbiguity",
                      "isActiveExploitation",
                      "activeExploitationCycles",
                      "noise"
                      ]

    # colors = ['tab:gray', 'tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown', 'tab:pink',
    #           'tab:olive', 'tab:cyan']

    colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown', 'tab:pink','tab:gray','tab:olive','tab:cyan']
    # colors = ['tab:blue', 'tab:green', 'tab:orange', 'tab:red', 'tab:purple', 'tab:brown', 'tab:pink','tab:gray','tab:olive','tab:cyan']
    # colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple']
    # colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red']
    # colors = ['tab:blue', 'tab:orange', 'tab:green']
    # colors = ['tab:red', 'tab:purple']

    # colors = ['lightsteelblue', 'tab:blue', 'midnightblue', 'gold', 'tab:orange', 'tab:red', 'lightgreen', 'tab:green', 'darkgreen']
    # colors = ['lightsteelblue', 'tab:blue', 'gold', 'tab:orange', 'lightgreen', 'tab:green']

    # colors = ['lavender','lightsteelblue', 'tab:blue', 'midnightblue',
    #           'lightgreen', 'limegreen' ,'tab:green', 'darkgreen',
    #           'gold','tab:orange', 'sienna', 'tab:red']

    # colors = ['lavender','lightsteelblue', 'tab:blue', 'mediumblue','midnightblue',
    #           'bisque','gold','tab:orange','peru', 'sienna',
    #           'darkseagreen','lightgreen', 'limegreen' ,'tab:green', 'darkgreen']

    # colors = [ 'lightsteelblue', 'tab:blue', 'mediumblue',
    #             'tab:orange', 'peru', 'sienna',
    #            'limegreen', 'tab:green', 'darkgreen']

    # colors = ['lightcoral','tab:red', 'orangered', 'darkred',
    #           'thistle', 'violet' ,'tab:purple', 'indigo']
    # colors = ['tab:red', 'orangered', 'darkred',
    #           'violet', 'tab:purple', 'indigo']

    # colors = ['lightsteelblue', 'tab:blue', 'midnightblue', 'lightgreen', 'tab:green', 'darkgreen', 'gold', 'tab:orange', 'tab:red']
    # colors = ['lightsteelblue', 'tab:blue', 'lightgreen', 'tab:green', 'gold', 'tab:orange']

    # intervalColors = ['lightsteelblue', 'lightsalmon', 'lightgreen', 'lightcoral', 'thistle', 'wheat', 'lemonchiffon', 'lightpink']
    # intervalColors = ['lightsteelblue', 'lightgreen', 'lightsalmon', 'lightcoral', 'thistle', 'wheat', 'lemonchiffon',
    #                   'lightpink']
    intervalColors = ['lightsteelblue', 'lightsalmon', 'lightgreen', 'lightcoral', 'thistle']
    # intervalColors = ['lightsteelblue', 'lightsalmon', 'lightgreen', 'lightcoral']
    # intervalColors = ['lightsteelblue', 'lightsalmon', 'lightgreen']
    # intervalColors = ['lightcoral', 'thistle']

    # markers = ['o', 'D', 'v', 's', 'P', 'p','*']
    markers = ['o', 'D', 'v', 's', 'P']
    # markers = ['o', 'D', 'v', 's']
    # markers = ['o', 'D', 'v']
    # markers = ['o', 'D']

    @classmethod
    def getPARAMS(cls):
        return {"dimension": cls.dimension, "learningCycles": cls.learningCycles,
                "exploitatingCycles": cls.exploitatingCycles,
                "episodes": cls.episodes,
                "validityRangesPrecision": cls.validityRangesPrecision,
                "neighborhoodRadiusCoefficient": cls.neighborhoodRadiusCoefficient,
                "influenceRadiusCoefficient": cls.influenceRadiusCoefficient,
                "isActiveLearning": cls.isActiveLearning, "isSelfLearning": cls.isSelfLearning,
                "errorMargin": cls.errorMargin, "bootstrapCycle": cls.bootstrapCycle,
                "isConflictNCS": cls.isConflictNCS, "isConcurenceNCS": cls.isConcurenceNCS,
                "isIncompetenceNCS": cls.isIncompetenceNCS,
                "isSubVoidDetection": cls.isSubVoidDetection, "isAmbiguityNCS": cls.isAmbiguityNCS,
                "isModelNCS": cls.isModelNCS,
                "isLearnFromNeighbors": cls.isLearnFromNeighbors, "isDream": cls.isDream,
                "isFusionResolution": cls.isFusionResolution, "isRetructureResolution": cls.isRetructureResolution,
                "dreamLaunch": cls.dreamLaunch,
                "nbOfNeighborForLearningFromNeighbors": cls.nbOfNeighborForLearningFromNeighbors,
                "nbOfNeighborForContexCreationWithouOracle": cls.nbOfNeighborForContexCreationWithouOracle,

                "isCreationFromNeighbor": cls.isCreationFromNeighbor,
                "model": cls.model,
                "exogenousLearningWeight": cls.exogenousLearningWeight,
                "endogenousLearningWeight": cls.endogenousLearningWeight,

                "LEARNING_WEIGHT_ACCURACY": cls.LEARNING_WEIGHT_ACCURACY,
                "LEARNING_WEIGHT_PROXIMITY": cls.LEARNING_WEIGHT_PROXIMITY,
                "LEARNING_WEIGHT_EXPERIENCE": cls.LEARNING_WEIGHT_EXPERIENCE,
                "LEARNING_WEIGHT_GENERALIZATION": cls.LEARNING_WEIGHT_GENERALIZATION,

                "EXPLOITATION_WEIGHT_PROXIMITY": cls.EXPLOITATION_WEIGHT_PROXIMITY,
                "EXPLOITATION_WEIGHT_EXPERIENCE": cls.EXPLOITATION_WEIGHT_EXPERIENCE,
                "EXPLOITATION_WEIGHT_GENERALIZATION": cls.EXPLOITATION_WEIGHT_GENERALIZATION,

                "perceptionsGenerationCoefficient": cls.perceptionsGenerationCoefficient,
                "modelSimilarityThreshold": cls.modelSimilarityThreshold,

                "maxRangeRadiusCoefficient": cls.maxRangeRadiusCoefficient,
                "rangeSimilarityCoefficient": cls.rangeSimilarityCoefficient,
                "minimumRangeCoefficient": cls.minimumRangeCoefficient,

                "isAllContextSearchAllowedForLearning": cls.isAllContextSearchAllowedForLearning,
                "isAllContextSearchAllowedForExploitation": cls.isAllContextSearchAllowedForExploitation,
                "probabilityOfRangeAmbiguity": cls.probabilityOfRangeAmbiguity,
                "isActiveExploitation": cls.isActiveExploitation,
                "activeExploitationCycles" : cls.activeExploitationCycles,
                "noise": cls.noise,
                }

    @classmethod
    def getFigName(cls):
        return "_D" + str(cls.getPARAMS().get("dimension")) + \
                          "_L" + str(cls.getPARAMS().get("learningCycles")) + \
                          "_Ex" + str(cls.getPARAMS().get("exploitatingCycles")) + \
                          "_Ep" + str(cls.getPARAMS().get("episodes")) + \
                          "_R" + str(cls.getPARAMS().get("validityRangesPrecision")) + \
                          "_N" + str(cls.getPARAMS().get("neighborhoodRadiusCoefficient")) + \
                          "_I" + str(cls.getPARAMS().get("influenceRadiusCoefficient")) + \
                          "_A" + str(cls.getPARAMS().get("isActiveLearning")) + \
                          "_S" + str(cls.getPARAMS().get("isSelfLearning")) + \
                          "_E" + str(cls.getPARAMS().get("errorMargin")) + \
                          "_B" + str(cls.getPARAMS().get("bootstrapCycle")) + \
                          "_W" + str(cls.getPARAMS().get("exogenousLearningWeight")) + str(
            cls.getPARAMS().get("endogenousLearningWeight"))

    @classmethod
    def getConstains(cls,labels,figVaryingParamString):

        constrains = []

        for label in labels:
            constrainsDico = {}
            for key, value in cls.getPARAMS().items():
                if (key == figVaryingParamString):
                    constrainsDico[key] = label
                else:
                    constrainsDico[key] = value

            constrains.append(constrainsDico)

        return constrains

    @classmethod
    def getConstainsLabelsAreParams(cls, labels, figVaryingParamString, XYDevMinMax):

        constrains = []

        for label in labels:
            constrainsDico = {}
            for key, value in cls.getPARAMS().items():
                if (key == figVaryingParamString):
                    constrainsDico[key] = label
                else:
                    constrainsDico[key] = value

            fullConstain = [XYDevMinMax,constrainsDico]
            constrains.append(fullConstain)

        return constrains

    @classmethod
    def getConstainsLabelsAreYStrings(cls, labels, XYDevMinMax):

        constrains = []

        for label, xyDevmM in zip(labels,XYDevMinMax):
            constrainsDico = {}
            for key, value in cls.getPARAMS().items():
                constrainsDico[key] = value

            fullConstrain = [xyDevmM,constrainsDico]
            constrains.append(fullConstrain)

        return constrains

    @classmethod
    def getConstainsSingle(cls, XYDevMinMax):

        constrains = []

        for xyDevmM in  XYDevMinMax:
            constrainsDico = {}
            for key, value in cls.getPARAMS().items():
                constrainsDico[key] = value

            fullConstrain = [xyDevmM, constrainsDico]
            constrains.append(fullConstrain)

        return constrains

    @classmethod
    def getConstainsLabelsAreParamsWithVaryingParam(cls, labels, figVaryingParamString, XYDevMinMax, valueVarying):

        constrains = []

        for label, xyDevmM in zip(labels,XYDevMinMax):
            constrainsDico = {}
            for key, value in cls.getPARAMS().items():

                if (key == figVaryingParamString):
                    constrainsDico[key] = valueVarying
                else:
                    constrainsDico[key] = value

            fullConstrain = [xyDevmM,constrainsDico]
            constrains.append(fullConstrain)

        return constrains

    @classmethod
    def getConstainsLabelsAreParamsWithVaryingParam2(cls, labels, figVaryingParamString, XYDevMinMax, valueVarying):

        constrains = []

        for label, xyDevmM in zip(labels, XYDevMinMax):
            constrainsDico = {}
            for key, value in cls.getPARAMS().items():

                if (key == figVaryingParamString):
                    constrainsDico[key] = valueVarying
                else:
                    constrainsDico[key] = value

            fullConstrain = [xyDevmM, constrainsDico]
            constrains=fullConstrain


        return constrains
