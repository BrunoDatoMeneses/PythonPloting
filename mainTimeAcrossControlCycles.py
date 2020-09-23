import Plot
from Utils import transpose

import os
import csv

transpose.transposeFiles()

labels = ['1', '5','10']
colors = ['tab:red', 'tab:blue', 'tab:green']
markers = ['o', 'v', 'D']
figName = "TimeExecutionAccrosControlCycles"
xlabel = 'Joints (#)'
ylabel = 'Mean Time Execution (s)'
logScale = False
xString = "joints"
yString = "meanTime"
deviationString = "meanTime"

constrains = [{"precisionRange": "0.02", "learningCycles": "200", "exploitatingCycles": "50", "episodes": "15", "isOrientationGoal": "false", "requestControlCycles": "1"},
              {"precisionRange": "0.02", "learningCycles": "200", "exploitatingCycles": "50", "episodes": "15", "isOrientationGoal": "false", "requestControlCycles": "5"},
              {"precisionRange": "0.02", "learningCycles": "200", "exploitatingCycles": "50", "episodes": "15", "isOrientationGoal": "false", "requestControlCycles": "10"}]


Plot.plot2(labels, colors, markers, figName, xlabel, ylabel, logScale, xString, yString, deviationString, constrains)