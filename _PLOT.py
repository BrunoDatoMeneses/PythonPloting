import numpy as np
import os
import csv

import _FIG


def plotWithDeviation2(labels, colors, markers, figName, xlabel, ylabel, logXScale, logYScale, xString, yString, deviationString, constraints1, constraints2, xModificationCoef, yModificationCoef):

    xValues = []
    yValues = []
    yDeviationValues = []



    for dicoConstrains in constraints1:
        xValueList, yDeviationValueList, yValueList = getValuesFromFiles(deviationString, xString, yString, dicoConstrains, xModificationCoef, yModificationCoef)
        xValues.append(np.array(xValueList))
        yValues.append(np.array(yValueList))
        yDeviationValues.append(np.array(yDeviationValueList))

    for dicoConstrains in constraints2:
        xValueList, yDeviationValueList, yValueList = getValuesFromFiles(deviationString, xString, yString, dicoConstrains, xModificationCoef, yModificationCoef)
        xValues.append(np.array(xValueList))
        yValues.append(np.array(yValueList))
        yDeviationValues.append(np.array(yDeviationValueList))


    _FIG.figWithDeviation(xValues, yValues, yDeviationValues, labels, xlabel, ylabel, colors, markers, figName + "_" + yString + "_DependingOn_" + xString, logXScale, logYScale)


def plot2(labels, colors, markers, figName, xlabel, ylabel, logXScale, logYScale, xString, yString, deviationString, constraints1, constraints2, xModificationCoef, yModificationCoef):

    xValues = []
    yValues = []
    yDeviationValues = []



    for dicoConstrains in constraints1:
        xValueList, yDeviationValueList, yValueList = getValuesFromFiles(deviationString, xString, yString, dicoConstrains, xModificationCoef, yModificationCoef)
        xValues.append(np.array(xValueList))
        yValues.append(np.array(yValueList))
        yDeviationValues.append(np.array(yDeviationValueList))

    for dicoConstrains in constraints2:
        xValueList, yDeviationValueList, yValueList = getValuesFromFiles(deviationString, xString, yString, dicoConstrains, xModificationCoef, yModificationCoef)
        xValues.append(np.array(xValueList))
        yValues.append(np.array(yValueList))
        yDeviationValues.append(np.array(yDeviationValueList))


    _FIG.fig(xValues, yValues, labels, xlabel, ylabel, colors, markers, figName + "_" + yString + "_DependingOn_" + xString, logXScale, logYScale)


def plot2Diff(labels, colors, markers, figName, xlabel, ylabel, logXScale, logYScale, xString, yString, deviationString, constraints1, constraints2, xModificationCoef, yModificationCoef):

    xValues1 = []
    yValues1 = []
    yDeviationValues1 = []

    xValues2 = []
    yValues2 = []
    yDeviationValues2 = []

    yValuesdiff = []
    yDeviationValuesdiff = []



    for dicoConstrains in constraints1:
        xValueList, yDeviationValueList, yValueList = getValuesFromFiles(deviationString, xString, yString, dicoConstrains, xModificationCoef, yModificationCoef)
        xValues1.append(np.array(xValueList))
        yValues1.append(np.array(yValueList))
        yDeviationValues1.append(np.array(yDeviationValueList))

    for dicoConstrains in constraints2:
        xValueList, yDeviationValueList, yValueList = getValuesFromFiles(deviationString, xString, yString, dicoConstrains, xModificationCoef, yModificationCoef)
        xValues2.append(np.array(xValueList))
        yValues2.append(np.array(yValueList))
        yDeviationValues2.append(np.array(yDeviationValueList))

    for valy1, valy2 in zip(yValues1, yValues2):
        yValuesdiff.append(np.array(valy1-valy2))



    _FIG.fig(xValues1, yValuesdiff, labels, xlabel, ylabel, colors, markers, figName + "_" + yString + "_DependingOn_" + xString, logXScale, logYScale)



def plotMeanWithDeviation(labels, colors, markers, figName, xlabel, ylabel, logXScale, logYScale, xString, yString1, yString2, deviationString1, deviationString2, constrains, xModificationCoef, yModificationCoef):

    xValues = []
    yValues = []
    yDeviationValues = []



    for dicoConstrains in constrains:
        print(dicoConstrains)
        xValueList, yDeviationValueList, yValueList = getMeanValuesFromFiles(deviationString1, deviationString2, xString, yString1, yString2, dicoConstrains, xModificationCoef, yModificationCoef)
        xValues.append(np.array(xValueList))
        yValues.append(np.array(yValueList))
        yDeviationValues.append(np.array(yDeviationValueList))


    _FIG.figWithDeviation(xValues, yValues, yDeviationValues, labels, xlabel, ylabel, colors, markers, figName + "_" + yString1 + yString2 + "_DependingOn_" + xString, logXScale, logYScale)


def plotDifferenceWithDeviation(labels, colors, markers, figName, xlabel, ylabel, logXScale, logYScale, xString, yString1, yString2, deviationString1, deviationString2, constrains, xModificationCoef, yModificationCoef):

    xValues = []
    yValues = []
    yDeviationValues = []



    for dicoConstrains in constrains:
        print(dicoConstrains)
        xValueList, yDeviationValueList, yValueList = getDiffValuesFromFiles(deviationString1, deviationString2, xString, yString1, yString2, dicoConstrains, xModificationCoef, yModificationCoef)
        xValues.append(np.array(xValueList))
        yValues.append(np.array(yValueList))
        yDeviationValues.append(np.array(yDeviationValueList))


    _FIG.fig(xValues, yValues, labels, xlabel, ylabel, colors, markers, figName + "_" + yString1 + yString2 + "_DependingOn_" + xString, logXScale, logYScale)



def plotWithDeviation(labels, colors, markers, figName, xlabel, ylabel, logXScale, logYScale, xString, yString, deviationString, constrains, xModificationCoef, yModificationCoef):

    xValues = []
    yValues = []
    yDeviationValues = []



    for dicoConstrains in constrains:
        print(dicoConstrains)
        xValueList, yDeviationValueList, yValueList = getValuesFromFiles(deviationString, xString, yString, dicoConstrains, xModificationCoef, yModificationCoef)
        xValues.append(np.array(xValueList))
        yValues.append(np.array(yValueList))
        yDeviationValues.append(np.array(yDeviationValueList))


    _FIG.figWithDeviation(xValues, yValues, yDeviationValues, labels, xlabel, ylabel, colors, markers, figName, logXScale, logYScale)



def plotWithDeviationWithFillBetween(labels, colors, intervalColors, markers, figName, xlabel, ylabel, logXScale, logYScale, xString, yString, deviationString, constrains, xModificationCoef, yModificationCoef, size):

    xValues = []
    yValues = []
    yDeviationValues = []



    for dicoConstrains in constrains:
        print(dicoConstrains)
        xValueList, yDeviationValueList, yValueList = getValuesFromFiles(deviationString, xString, yString, dicoConstrains, xModificationCoef, yModificationCoef)
        xValues.append(np.array(xValueList))
        yValues.append(np.array(yValueList))
        yDeviationValues.append(np.array(yDeviationValueList))


    _FIG.figWithDeviationFillBetween(xValues, yValues, yDeviationValues, labels, xlabel, ylabel, colors, intervalColors, markers, figName +"-D", logXScale, logYScale, size)

def plotWitMinMaxWithFillBetween(labels, colors, intervalColors, markers, figName, xlabel, ylabel, logXScale, logYScale, xString, yString, minString, maxString, constrains, xModificationCoef, yModificationCoef, size):

    xValues = []
    yValues = []
    yMinValues = []
    yMaxValues = []


    for dicoConstrains in constrains:
        print(dicoConstrains)
        xValueList, yMinValuesList, yMaxValuesList, yValueList = getValuesFromFiles2(minString, maxString, xString, yString, dicoConstrains, xModificationCoef, yModificationCoef)
        xValues.append(np.array(xValueList))
        yValues.append(np.array(yValueList))
        yMinValues.append(np.array(yMinValuesList))
        yMaxValues.append(np.array(yMaxValuesList))


    _FIG.figWithMinMax(xValues, yValues, yMinValues, yMaxValues, labels, xlabel, ylabel, colors, intervalColors, markers, figName  +"-M", logXScale, logYScale, size)

def plot(labels, colors, markers, figName, xlabel, ylabel, logXScale, logYScale, xString, yString, deviationString, constrains, xModificationCoef, yModificationCoef):

    xValues = []
    yValues = []
    yDeviationValues = []



    for dicoConstrains in constrains:
        xValueList, yDeviationValueList, yValueList = getValuesFromFiles(deviationString, xString, yString, dicoConstrains, xModificationCoef, yModificationCoef)
        xValues.append(np.array(xValueList))
        yValues.append(np.array(yValueList))
        yDeviationValues.append(np.array(yDeviationValueList))


    _FIG.fig(xValues, yValues, labels, xlabel, ylabel, colors, markers, figName + "_" + yString + "_DependingOn_" + xString, logXScale, logYScale)

def plot3(labels, colors, markers, figName, xlabel, ylabel, logXScale, logYScale, xString, yString, deviationString, constrains, xModificationCoef, yModificationCoef, size):

    xValues = []
    yValues = []
    yDeviationValues = []



    for dicoConstrains in constrains:
        xValueList, yDeviationValueList, yValueList = getValuesFromFiles(deviationString, xString, yString, dicoConstrains, xModificationCoef, yModificationCoef)
        xValues.append(np.array(xValueList))
        yValues.append(np.array(yValueList))
        yDeviationValues.append(np.array(yDeviationValueList))


    _FIG.fig3(xValues, yValues, labels, xlabel, ylabel, colors, markers, figName, logXScale, logYScale, size)

def getValuesFromFiles(deviationString, xString, yString, dicoConstrains, xModificationCoef, yModificationCoef):
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
                    for constrainString, constrainValue in dicoConstrains.items():
                        if(constrainString==xString):
                            test = test and ( constrainValue[0] < int(row[constrainString]) <= constrainValue[1])
                        else:
                            test = test and (row[constrainString]==constrainValue)

                    if(test):
                        dicoFiles[float(row[xString])] = filename

        for joint, filename in sorted(dicoFiles.items(), key=lambda t: t[0]):



            with open("TFILES/" + filename) as csvfile:
                csv_reader = csv.DictReader(csvfile, delimiter=';')
                for row in csv_reader:
                    xValueList.append(float(row[xString])*xModificationCoef)
                    yValueList.append(float(row[yString])*yModificationCoef)
                    yDeviationValueList.append(float(row[deviationString])*yModificationCoef)
    return xValueList, yDeviationValueList, yValueList

def getValuesFromFiles2(minString,maxString, xString, yString, dicoConstrains, xModificationCoef, yModificationCoef):
    dicoFiles = {}
    xValueList = []
    yValueList = []
    yMinValueList = []
    yMaxValueList = []
    for root, dirs, files in os.walk("TFiles"):

        for filename in files:
            with open("TFILES/" + filename) as csvfile:
                csv_reader = csv.DictReader(csvfile, delimiter=';')
                for row in csv_reader:

                    test = True
                    for constrainString, constrainValue in dicoConstrains.items():
                        if (constrainString == xString):
                            test = test and (constrainValue[0] < int(row[constrainString]) <= constrainValue[1])
                        else:
                            test = test and (row[constrainString] == constrainValue)

                    if(test):
                        dicoFiles[float(row[xString])] = filename

        for joint, filename in sorted(dicoFiles.items(), key=lambda t: t[0]):



            with open("TFILES/" + filename) as csvfile:
                csv_reader = csv.DictReader(csvfile, delimiter=';')
                for row in csv_reader:
                    xValueList.append(float(row[xString])*xModificationCoef)
                    yValueList.append(float(row[yString])*yModificationCoef)
                    yMinValueList.append(float(row[minString])*yModificationCoef)
                    yMaxValueList.append(float(row[maxString]) * yModificationCoef)
    return xValueList, yMinValueList, yMaxValueList, yValueList


def getMeanValuesFromFiles(deviationString1, deviationString2, xString, yString1, yString2, dicoConstrains, xModificationCoef, yModificationCoef):
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
                    xValueList.append(float(row[xString])*xModificationCoef)
                    meanValue = (float(row[yString1]) + float(row[yString2]))/2
                    meanDeviation = (float(row[deviationString1]) + float(row[deviationString2])) / 2
                    yValueList.append(meanValue*yModificationCoef)
                    yDeviationValueList.append(meanDeviation*yModificationCoef)
    return xValueList, yDeviationValueList, yValueList


def getDiffValuesFromFiles(deviationString1, deviationString2, xString, yString1, yString2, dicoConstrains, xModificationCoef, yModificationCoef):
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
                    xValueList.append(float(row[xString])*xModificationCoef)
                    diffValue = float(row[yString1]) - float(row[yString2])
                    diffDeviation = float(row[deviationString1]) - float(row[deviationString2])
                    yValueList.append(diffValue*yModificationCoef)
                    yDeviationValueList.append(diffDeviation*yModificationCoef)
    return xValueList, yDeviationValueList, yValueList









