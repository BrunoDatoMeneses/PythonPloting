import Plot
from Utils import transpose

import os
import csv

transpose.transposeFiles()

labels = ['Without Orientation', 'With Orientation']
colors = ['tab:red', 'tab:blue']
markers = ['o','D']
figName = "ThetaGoalAcrossOrientation"
xlabel = 'Joints (#)'
ylabel = 'Mean Theta Error from Goal (%)'
logScale = False
xString = "joints"
yString = "goalThetaErrorAverage"
deviationString = "goalThetaErrorDeviationAverage"

constrains = [{"precisionRange": "0.02", "learningCycles": "200", "exploitatingCycles": "50", "episodes": "15", "isOrientationGoal": "false", "requestControlCycles": "10"},
              {"precisionRange": "0.02", "learningCycles": "200", "exploitatingCycles": "50", "episodes": "15", "isOrientationGoal": "true", "requestControlCycles": "10"}]



Plot.plot(labels, colors, markers, figName, xlabel, ylabel, logScale, xString, yString, deviationString, constrains)