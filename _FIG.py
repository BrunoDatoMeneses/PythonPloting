import numpy as np
import matplotlib.pyplot as plt

ALPHA_FILL = 1.0
ROTATION = 0
# ROTATION = 22.5
# ROTATION = 45
# ROTATION = 67.5
# ROTATION = 90

def figWithDeviation(xArrays, yArrays, errorArrays, labelsString, xlabelString, yLabelString, colors, markers, figureName, logXScale, logYScale):

    ls = 'dotted'
    fig, ax = plt.subplots(figsize=(5, 3))


    for x,y,error,labelString,color,marker in zip(xArrays,yArrays,errorArrays,labelsString, colors, markers):


        ax.errorbar(x, y, yerr=error, marker=marker, markersize=8, linestyle=ls, label=labelString, color = color)
        ax.errorbar(x, y + error, marker='_', markersize=12, color=color, linestyle='none')
        ax.errorbar(x, y - error, marker='_', markersize=12, color=color, linestyle='none')




    # tidy up the figure
    # ax.set_xlim((0, 5.5))
    #ax.set_ylim((-1.5, 10))
    # ax.set_title(figureName)
    plt.grid()



    ax.set_xlabel(xlabelString)  # Add an x-label to the axes.
    ax.set_ylabel(yLabelString)  # Add a y-label to the axes.
    plt.legend()
    if (logXScale):
        plt.xscale("log")
        figureName+="_xlog"
    if (logYScale):
        plt.yscale("log")
        figureName+="_ylog"

    plt.savefig("Figures/" + formatFigName(figureName) + ".png", bbox_inches='tight')
    # plt.show()

def figWithDeviationFillBetween(xArrays, yArrays, errorArrays, labelsString, xlabelString, yLabelString, colors, intervalColors, markers, figureName, logXScale, logYScale, size):

    # ls = 'dotted'
    ls = (0,(1,5))
    fig, ax = plt.subplots(figsize=(size[0], size[1]))



    for x,y,error,labelString,color, intervalColor, marker in zip(xArrays,yArrays,errorArrays,labelsString, colors, intervalColors, markers):


        ax.errorbar(x, y, marker=marker, markersize=8, linestyle=ls, label=labelString, color = color)
        ax.fill_between(x, (y - error), (y + error), color=intervalColor, alpha=ALPHA_FILL)
        #ax.errorbar(x, y + error, marker='_', markersize=12, color=color, linestyle='none')
        #ax.errorbar(x, y - error, marker='_', markersize=12, color=color, linestyle='none')




    # tidy up the figure
    # ax.set_xlim((0, 5.5))
    #ax.set_ylim((-1.5, 10))
    # ax.set_title(figureName)
    plt.grid()



    ax.set_xlabel(xlabelString)  # Add an x-label to the axes.
    ax.set_ylabel(yLabelString)  # Add a y-label to the axes.
    plt.legend()
    if (logXScale):
        plt.xscale("log")
        figureName+="_xlog"
    if (logYScale):
        plt.yscale("log")
        figureName+="_ylog"

    plt.savefig("Figures/" + formatFigName(figureName) + ".png", bbox_inches='tight')
    # plt.show()

def figWithMinMax(xArrays, yArrays, minArrays, maxArrays, labelsString, xlabelString, yLabelString, colors, intervalColors, markers, figureName, logXScale, logYScale, size):

    # ls = 'dotted'
    ls = (0, (1, 5))
    fig, ax = plt.subplots(figsize=(size[0], size[1]))


    for x,y,min,max,labelString,color, intervalColor, marker in zip(xArrays,yArrays,minArrays,maxArrays ,labelsString, colors, intervalColors, markers):


        ax.errorbar(x, y, marker=marker, markersize=8, linestyle=ls, label=labelString, color = color)
        #ax.errorbar(x, min, marker=marker, markersize=4, linestyle=ls, label=labelString, color=intervalColor)
        #ax.errorbar(x, max, marker=marker, markersize=4, linestyle=ls, label=labelString, color=intervalColor)
        ax.fill_between(x, (min), (max), color=intervalColor, alpha=ALPHA_FILL)
        #ax.errorbar(x, y + error, marker='_', markersize=12, color=color, linestyle='none')
        #ax.errorbar(x, y - error, marker='_', markersize=12, color=color, linestyle='none')




    # tidy up the figure
    # ax.set_xlim((0, 5.5))
    #ax.set_ylim((-1.5, 10))
    # ax.set_title(figureName)
    plt.grid()



    ax.set_xlabel(xlabelString)  # Add an x-label to the axes.
    ax.set_ylabel(yLabelString)  # Add a y-label to the axes.
    plt.legend()
    if (logXScale):
        plt.xscale("log")
        figureName+="_xlog"
    if (logYScale):
        plt.yscale("log")
        figureName+="_ylog"

    plt.savefig("Figures/" + formatFigName(figureName) + ".png", bbox_inches='tight')
    # plt.show()

def barWithDeviation(yArrays, errorArrays, xLabelsString, yLabelString, legendLabel, colors, intervalColors, figureName, logXScale, logYScale, size):

    # ls = 'dotted'
    ls = (0,(1,5))
    fig, ax = plt.subplots(figsize=(size[0], size[1]))
    x = np.arange(len(xLabelsString))  # the label locations
    width = 0.75

    n = len(legendLabel)
    i=0
    for yArray, errorArray,legend,color in zip(yArrays,errorArrays,legendLabel,colors):
        ax.bar(x -(width/2) + (width/(2*n))  +  i*(width/n), yArray, width/n, yerr=errorArray, label=legend,color=color)
        i+=1

    #ax.bar(x, yArrays, width, yerr=errorArrays, label='Test', color=colors)

        #ax.errorbar(x, y + error, marker='_', markersize=12, color=color, linestyle='none')
        #ax.errorbar(x, y - error, marker='_', markersize=12, color=color, linestyle='none')




    # tidy up the figure
    # ax.set_xlim((0, 5.5))
    #ax.set_ylim((-1.5, 10))
    # ax.set_title(figureName)
    plt.grid()

    ax.set_xticks(x)
    ax.set_xticklabels(xLabelsString, rotation=ROTATION)



    ax.set_ylabel(yLabelString)  # Add a y-label to the axes.
    #plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
    # plt.legend()

    if (logYScale):
        plt.yscale("log")
        figureName+="_ylog"

    plt.savefig("Figures/" + formatFigName(figureName) + ".png", bbox_inches='tight')
    # plt.show()


def fig(xArrays, yArrays, labelsString, xlabelString, yLabelString, colors, markers, figureName, logXScale, logYScale):




    ls = 'dotted'
    fig, ax = plt.subplots(figsize=(5, 3))


    for x,y,labelString,color,marker in zip(xArrays,yArrays,labelsString, colors, markers):


        ax.errorbar(x, y, marker=marker, markersize=8, linestyle=ls, label=labelString, color = color)





    # tidy up the figure
    # ax.set_xlim((0, 5.5))
    # ax.set_ylim((0, 10.0))
    # ax.set_title(figureName)
    plt.grid()



    ax.set_xlabel(xlabelString)  # Add an x-label to the axes.
    ax.set_ylabel(yLabelString)  # Add a y-label to the axes.
    plt.legend()
    if (logXScale):
        plt.xscale("log")
        figureName += "_xlog"
    if (logYScale):
        plt.yscale("log")
        figureName += "_ylog"

    plt.savefig("Figures/" + formatFigName(figureName) + ".png", bbox_inches='tight')
    # plt.show()

def fig3(xArrays, yArrays, labelsString, xlabelString, yLabelString, colors, markers, figureName, logXScale, logYScale, size):




    ls = 'dotted'
    fig, ax = plt.subplots(figsize=size)


    for x,y,labelString,color,marker in zip(xArrays,yArrays,labelsString, colors, markers):


        ax.errorbar(x, y, marker=marker, markersize=8, linestyle=ls, label=labelString, color = color)





    # tidy up the figure
    # ax.set_xlim((0, 5.5))
    # ax.set_ylim((0, 10.0))
    # ax.set_title(figureName)
    plt.grid()



    ax.set_xlabel(xlabelString)  # Add an x-label to the axes.
    ax.set_ylabel(yLabelString)  # Add a y-label to the axes.
    plt.legend()
    if (logXScale):
        plt.xscale("log")
        figureName += "_xlog"
    if (logYScale):
        plt.yscale("log")
        figureName += "_ylog"


    plt.savefig("Figures/" + formatFigName(figureName) + ".png", bbox_inches='tight')
    # plt.show()




def formatFigName(figureName):
    newFigName=""
    for char in figureName:
        if(char != "." and char != "#" and char != " "):
            newFigName+=char

    return newFigName