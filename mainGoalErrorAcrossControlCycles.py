import Plot
from Utils import transpose

import os
import csv

transpose.transposeFiles()

labels = ['1', '5','10']
colors = ['tab:red', 'tab:blue', 'tab:green']
markers = ['o', 'v', 'D']
figName = "XYGoalAcrossControlCycles"
xlabel = 'Joints (#)'
ylabel = 'Mean Error from Goal (%)'
logScale = False
xString = "joints"
yString = "goalXYErrorAverage"
deviationString = "goalXYErrorDeviationAverage"

constraints = [{"precisionRange": "0.02", "learningCycles": "200", "exploitatingCycles": "50", "episodes": "15", "isOrientationGoal": "false", "requestControlCycles": "1"},
               {"precisionRange": "0.02", "learningCycles": "200", "exploitatingCycles": "50", "episodes": "15", "isOrientationGoal": "false", "requestControlCycles": "5"},
               {"precisionRange": "0.02", "learningCycles": "200", "exploitatingCycles": "50", "episodes": "15", "isOrientationGoal": "false", "requestControlCycles": "10"}]



Plot.plot(labels, colors, markers, figName, xlabel, ylabel, logScale, xString, yString, deviationString, constraints)