import numpy as np
import os
import csv

from old import FIG

def plot(labels, colors, markers, figName, xlabel, ylabel, logScale, xString, yString, deviationString, constrains):

    xValues = []
    yValues = []
    yDeviationValues = []



    for dicoConstrains in constrains:
        xValueList, yDeviationValueList, yValueList = getValuesFromFiles(deviationString, xString, yString, dicoConstrains)
        xValues.append(np.array(xValueList))
        yValues.append(np.array(yValueList))
        yDeviationValues.append(np.array(yDeviationValueList))


    FIG.figWithDeviation(xValues, yValues, yDeviationValues, labels, xlabel, ylabel, colors, markers, figName + "_" + yString + "_DependingOn_" + xString, logScale)


def plot2(labels, colors, markers, figName, xlabel, ylabel, logScale, xString, yString, deviationString, constrains):

    xValues = []
    yValues = []
    yDeviationValues = []



    for dicoConstrains in constrains:
        xValueList, yDeviationValueList, yValueList = getValuesFromFiles(deviationString, xString, yString, dicoConstrains)
        xValues.append(np.array(xValueList))
        yValues.append(np.array(yValueList))
        yDeviationValues.append(np.array(yDeviationValueList))


    FIG.fig(xValues, yValues, labels, xlabel, ylabel, colors, markers, figName + "_" + yString + "_DependingOn_" + xString, logScale)


def getValuesFromFiles(deviationString, xString, yString, dicoConstrains):
    dicoFiles = {}
    xValueList = []
    yValueList = []
    yDeviationValueList = []
    for root, dirs, files in os.walk("TFiles"):

        for filename in files:
            with open("TFILES/" + filename) as csvfile:
                csv_reader = csv.DictReader(csvfile, delimiter=';')
                for row in csv_reader:

                    test = True
                    for k, v in dicoConstrains.items():
                        test = test and (row[k]==v)

                    if(test):
                        dicoFiles[float(row[xString])] = filename

        for joint, filename in sorted(dicoFiles.items(), key=lambda t: t[0]):



            with open("TFILES/" + filename) as csvfile:
                csv_reader = csv.DictReader(csvfile, delimiter=';')
                for row in csv_reader:
                    xValueList.append(float(row[xString]))
                    yValueList.append(float(row[yString]))
                    yDeviationValueList.append(float(row[deviationString]))
    return xValueList, yDeviationValueList, yValueList









