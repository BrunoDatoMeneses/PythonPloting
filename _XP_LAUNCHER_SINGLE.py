import os

if __name__ == "__main__":

    # neighborhoods = ["2"]
    # joints = ["2","3","6","10","20","30","50","100"]
    # learningCycles = ["200"]
    # exploitationCycles = ["50"]
    # episodes = ["15"]
    # controlCycles = ["1", "5", "10", "20"]
    # precisionRanges = ["2","4","6"]
    # isOrientationGoal = ["true","false"]
    # isNeighborhoodLearning = ["true", "false"]

    neighborhoods = ["2"]
    joints = ["6"]
    learningCycles = ["200"]
    exploitationCycles = ["50"]
    episodes = ["1"]
    controlCycles = ["1"]
    precisionRanges = ["6"]
    isOrientationGoal = ["false"]
    isNeighborhoodLearning = ["true"]

    for neighborhoodSize in neighborhoods:
        for precision in precisionRanges:
            for learning in learningCycles:
                for exploitation in exploitationCycles:
                    for episode in episodes:
                        for control in controlCycles:
                            for joint in joints:
                                for orientation in isOrientationGoal:
                                    for neighborhoodLearning in isNeighborhoodLearning:

                                        arguments = joint + " " + learning + " " + exploitation + " " + control + " " + episode + " " + precision + " " + neighborhoodSize + " " + orientation + " " + neighborhoodLearning
                                        os.system("java -jar AMOEBA-parent.jar "+ arguments)
                                        print("")