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





def plotSeveralYWithDeviationWithFillBetween(labels, colors, intervalColors, markers, figName, xlabel, ylabel, logXScale, logYScale, xString, yString, deviationString, constrains, xModificationCoef, yModificationCoef, size):

    xValues = []
    yValues = []
    yDeviationValues = []



    for dicoConstrains in constrains:
        print(dicoConstrains)
        xValueList, yDeviationValueList, yValueList = getValuesFromFilesSeveralY(dicoConstrains[1], xString, dicoConstrains[0], dicoConstrains[4], xModificationCoef, yModificationCoef)
        xValues.append(np.array(xValueList))
        yValues.append(np.array(yValueList))
        yDeviationValues.append(np.array(yDeviationValueList))


    _FIG.figWithDeviationFillBetween(xValues, yValues, yDeviationValues, labels, xlabel, ylabel, colors, intervalColors, markers, figName +"-D", logXScale, logYScale, size)

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

def plotWithDeviationWithFillBetweenConstrained(labels, colors, intervalColors, markers, figName, xlabel, ylabel, logXScale, logYScale, constrains, xModificationCoef, yModificationCoef, size):

    xValues = []
    yValues = []
    yDeviationValues = []



    for dicoConstrains in constrains:
        print(dicoConstrains)
        xValueList, yDeviationValueList, yValueList = getValuesFromFilesAndConstrains(dicoConstrains, xModificationCoef, yModificationCoef)
        xValues.append(np.array(xValueList))
        yValues.append(np.array(yValueList))
        yDeviationValues.append(np.array(yDeviationValueList))


    _FIG.figWithDeviationFillBetween(xValues, yValues, yDeviationValues, labels, xlabel, ylabel, colors, intervalColors, markers, figName +"-D", logXScale, logYScale, size)


def plotSimple(labels, colors, intervalColors, markers, figName, xlabel, ylabel, logXScale, logYScale, constrains, xModificationCoef, yModificationCoef, size):

    xValues = []
    yValues = []
    yDeviationValues = []



    for dicoConstrains in constrains:
        print(dicoConstrains)
        xValueList, yDeviationValueList, yValueList = getValuesFromFilesAndConstrains(dicoConstrains, xModificationCoef, yModificationCoef)
        xValues.append(np.array(xValueList))
        yValues.append(np.array(yValueList))
        yDeviationValues.append(np.array(yDeviationValueList))


    _FIG.figSimple(xValues, yValues, yDeviationValues, labels, xlabel, ylabel, colors, intervalColors, markers, figName +"-D", logXScale, logYScale, size)

def barWithDeviationConstrained(XLabels, legendLabels, colors, intervalColors, markers, figName, ylabel, logXScale, logYScale, allConstrains, xModificationCoef, yModificationCoef, size):

    yAllValues = []
    yAllDeviationValues = []

    for constrains in allConstrains:
        yValues = []
        yDeviationValues = []

        for dicoConstrains in constrains:
            print(dicoConstrains)
            yDeviationValue, yValue = getBarValuesFromFilesAndConstrains(dicoConstrains, yModificationCoef)
            yValues.append(yValue)
            yDeviationValues.append(yDeviationValue)

        yAllValues.append(yValues)
        yAllDeviationValues.append(yDeviationValues)


    # del yAllValues[3]
    # del yAllDeviationValues[3]
    # del legendLabels[3]
    # del colors[3]


    _FIG.barWithDeviation(yAllValues, yAllDeviationValues, XLabels, ylabel, legendLabels, colors, intervalColors, figName + "-D", logXScale, logYScale, size)


def barWithDeviationConstrainedModded(XLabels, legendLabels, colors, intervalColors, markers, figName, ylabel, logXScale,
                                logYScale, allConstrains, xModificationCoef, yModificationCoef, size):

    yAllValues = []
    yAllDeviationValues = []

    for constrains in allConstrains:
        yValues = []
        yDeviationValues = []

        for dicoConstrains in constrains:
            print(dicoConstrains)
            yDeviationValue, yValue = getBarValuesFromFilesAndConstrains(dicoConstrains, yModificationCoef)
            yValues.append(yValue)
            yDeviationValues.append(yDeviationValue)

        yAllValues.append(yValues)
        yAllDeviationValues.append(yDeviationValues)

    print(yAllValues)
    yAllValuesModed = []
    yAllDeviationValuesModed = []
    for i in range( len(yAllValues)):
        yAllValuesModed.append([])
        yAllDeviationValuesModed.append([])
        for j in range( len(yAllValues[0])):

            if (i == 1 or i==3 or i==4):
                yAllValuesModed[i].append( yAllValues[i][j] - yAllValues[i - 1][j])
                yAllDeviationValuesModed[i].append( min(yAllDeviationValues[i][j], yAllDeviationValues[i - 1][j]))
            else:
                yAllValuesModed[i].append(yAllValues[i][j])
                yAllDeviationValuesModed[i].append(yAllDeviationValues[i][j])

    # del yAllValuesModed[3]
    # del yAllDeviationValuesModed[3]
    # del legendLabels[3]
    # del colors[3]


    _FIG.barWithDeviation(yAllValuesModed, yAllDeviationValuesModed, XLabels, ylabel, legendLabels, colors, intervalColors,
                          figName + "-D", logXScale, logYScale, size)

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

def plotWitMinMaxWithFillBetweenConstrained(labels, colors, intervalColors, markers, figName, xlabel, ylabel, logXScale, logYScale, constrains, xModificationCoef, yModificationCoef, size):

    xValues = []
    yValues = []
    yMinValues = []
    yMaxValues = []


    for dicoConstrains in constrains:
        print(dicoConstrains)
        xValueList, yMinValuesList, yMaxValuesList, yValueList = getValuesFromFilesMinMaxConstrained( dicoConstrains, xModificationCoef, yModificationCoef)
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


def getValuesFromFilesSeveralY(deviationString, xString, yString, dicoConstrains, xModificationCoef, yModificationCoef):
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
                            test = test and ( constrainValue[0] <= int(row[constrainString]) <= constrainValue[1])
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
                            test = test and ( constrainValue[0] <= int(row[constrainString]) <= constrainValue[1])
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

def getValuesFromFilesAndConstrains(dicoConstrains, xModificationCoef, yModificationCoef):
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
                    for constrainString, constrainValue in dicoConstrains[1].items():
                        if(constrainString==dicoConstrains[0][0]):

                            if(constrainString=="neighborhoodRadiusCoefficient" or constrainString=="influenceRadiusCoefficient" or constrainString=="nbAgents_Average"):
                                test = test and (constrainValue[0] <= float(row[constrainString]) <= constrainValue[1])
                            else:
                                test = test and (constrainValue[0] <= int(row[constrainString]) <= constrainValue[1])

                        else:
                            test = test and (row[constrainString]==constrainValue)

                    if(test):
                        dicoFiles[float(row[dicoConstrains[0][0]])] = filename

        for joint, filename in sorted(dicoFiles.items(), key=lambda t: t[0]):



            with open("TFILES/" + filename) as csvfile:
                csv_reader = csv.DictReader(csvfile, delimiter=';')
                for row in csv_reader:
                    xValueList.append(float(row[dicoConstrains[0][0]])*xModificationCoef)
                    # yValueList.append(float(row[dicoConstrains[0][1]])*yModificationCoef)
                    # yDeviationValueList.append(float(row[dicoConstrains[0][2]])*yModificationCoef)

                    if len(dicoConstrains[0]) == 6:
                        yValueList.append( (float(row[dicoConstrains[0][1]]) * dicoConstrains[0][5]))
                        yDeviationValueList.append( (float(row[dicoConstrains[0][2]]) * dicoConstrains[0][5]))
                    else:
                        yValueList.append( (float(row[dicoConstrains[0][1]]) * yModificationCoef))
                        yDeviationValueList.append( (float(row[dicoConstrains[0][2]]) * yModificationCoef))
    return xValueList, yDeviationValueList, yValueList

def getBarValuesFromFilesAndConstrains(dicoConstrains, yModificationCoef):
    file = ""
    for root, dirs, files in os.walk("TFiles"):

        for filename in files:
            with open("TFILES/" + filename) as csvfile:
                csv_reader = csv.DictReader(csvfile, delimiter=';')
                for row in csv_reader:

                    test = True
                    for constrainString, constrainValue in dicoConstrains[1].items():

                        test = test and (row[constrainString]==constrainValue)

                    if(test):
                        file = filename


    with open("TFILES/" + file) as csvfile:
        csv_reader = csv.DictReader(csvfile, delimiter=';')
        for row in csv_reader:
            print(dicoConstrains[0])
            if len(dicoConstrains[0])==5:
                yValue = (float(row[dicoConstrains[0][0]]) * dicoConstrains[0][4])
                yDeviationValue = (float(row[dicoConstrains[0][1]]) * dicoConstrains[0][4])
            else:
                yValue = (float(row[dicoConstrains[0][0]]) * yModificationCoef)
                yDeviationValue = (float(row[dicoConstrains[0][1]]) * yModificationCoef)

    return  yDeviationValue, yValue

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
                            test = test and (constrainValue[0] <= int(row[constrainString]) <= constrainValue[1])
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

def getValuesFromFilesMinMaxConstrained(dicoConstrains, xModificationCoef, yModificationCoef):
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
                    for constrainString, constrainValue in dicoConstrains[1].items():
                        if (constrainString == dicoConstrains[0][0]):
                            if(constrainString=="neighborhoodRadiusCoefficient" or constrainString=="influenceRadiusCoefficient" or constrainString=="nbAgents_Average"):
                                test = test and (constrainValue[0] <= float(row[constrainString]) <= constrainValue[1])
                            else:
                                test = test and (constrainValue[0] <= int(row[constrainString]) <= constrainValue[1])
                        else:
                            test = test and (row[constrainString] == constrainValue)

                    if(test):
                        dicoFiles[float(row[dicoConstrains[0][0]])] = filename

        for joint, filename in sorted(dicoFiles.items(), key=lambda t: t[0]):



            with open("TFILES/" + filename) as csvfile:
                csv_reader = csv.DictReader(csvfile, delimiter=';')
                for row in csv_reader:
                    xValueList.append(float(row[dicoConstrains[0][0]])*xModificationCoef)
                    yValueList.append(float(row[dicoConstrains[0][1]])*yModificationCoef)
                    yMinValueList.append(float(row[dicoConstrains[0][3]])*yModificationCoef)
                    yMaxValueList.append(float(row[dicoConstrains[0][4]]) * yModificationCoef)
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









