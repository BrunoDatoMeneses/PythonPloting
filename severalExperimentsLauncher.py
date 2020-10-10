import os

"""Launcher for several experiments, result are written in CSV file in the directory XP"""

if __name__ == "__main__":

    # Fixed experimental parameters in the article
    neighborhoodSizes = ["2"]
    precisionRanges = ["4"]
    episodes = ["15"]
    exploitationCycles = ["50"]

    # Varying experimental parameters in the article
    joints = ["3","6","10","20","30","50","100"]
    learningCycles = ["10","25","50","100","200","500","1000"]
    propagationCycles = ["1","2","5","10","20"]
    isOrientationGoal = ["true","false"]
    isCooperativeNeighborhoodLearning = ["true", "false"]

    for neighborhoodSize in neighborhoodSizes:
        for precision in precisionRanges:
            for learning in learningCycles:
                for exploitation in exploitationCycles:
                    for episode in episodes:
                        for propagation in propagationCycles:
                            for joint in joints:
                                for orientation in isOrientationGoal:
                                    for neighborhoodLearning in isCooperativeNeighborhoodLearning:

                                        arguments = joint + " " + learning + " " + exploitation + " " + propagation + " " + episode + " " + precision + " " + neighborhoodSize + " " + orientation + " " + neighborhoodLearning
                                        os.system("java -jar ELLSA.jar "+ arguments)
                                        print("")