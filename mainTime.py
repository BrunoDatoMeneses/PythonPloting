import Plot
from Utils import transpose

import os
import csv

transpose.transposeFiles()

labels = ['precision_range 2%', 'precision_range 4%']
colors = ['tab:red', 'tab:blue']
markers = ['o','D']
figName = "TimeExecutionWithoutOrientation"
xlabel = 'Joints (#)'
ylabel = 'Mean Time Execution (s)'
logScale = False
xString = "joints"
yString = "meanTime"
deviationString = "meanTime"

constrains = [{"precisionRange": "0.02"}, {"precisionRange": "0.04"}]


Plot.plot2(labels, colors, markers, figName, xlabel, ylabel, logScale, xString, yString, deviationString, constrains)