import os

"""Launcher for single experiment, result are written in CSV file in the directory XP"""

if __name__ == "__main__":

    # Fixed experimental parameters in the article
    neighborhoodSize = "2"
    precisionRange = "4"
    episodes = "15"
    exploitationCycles = "50"

    # Varying parameters in the article
    joints = "3"
    learningCycles = "200"
    propagationCycles = "5"
    isOrientationGoal = "true"
    isCooperativeNeighborhoodLearning = "true"

    arguments = joints + " " + learningCycles + " " + exploitationCycles + " " + propagationCycles + " " + episodes + " " + precisionRange + " " + neighborhoodSize + " " + isOrientationGoal + " " + isCooperativeNeighborhoodLearning
    os.system("java -jar ELLSA.jar "+ arguments)
    print("")