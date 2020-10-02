import numpy as np
import matplotlib.pyplot as plt


def figWithDeviation(xArrays, yArrays, errorArrays, labelsString, xlabelString, yLabelString, colors, markers, figureName, logScale):


    ls = 'dotted'
    fig, ax = plt.subplots(figsize=(5, 3))


    for x,y,error,labelString,color,marker in zip(xArrays,yArrays,errorArrays,labelsString, colors, markers):


        ax.errorbar(x, y, yerr=error, marker=marker, markersize=8, linestyle=ls, label=labelString, color = color)
        ax.errorbar(x, y + error, marker='_', markersize=12, color=color, linestyle='none')
        ax.errorbar(x, y - error, marker='_', markersize=12, color=color, linestyle='none')




    # tidy up the figure
    # ax.set_xlim((0, 5.5))
    # ax.set_ylim((0, 15.0))
    # ax.set_title(figureName)
    plt.grid()



    ax.set_xlabel(xlabelString)  # Add an x-label to the axes.
    ax.set_ylabel(yLabelString)  # Add a y-label to the axes.
    plt.legend()
    if (logScale):
        plt.xscale("log")
        plt.savefig("Figures/" + figureName + "_log.png", bbox_inches='tight')
    else:
        plt.savefig("Figures/" + figureName + ".png", bbox_inches='tight')
    # plt.show()


def fig(xArrays, yArrays, labelsString, xlabelString, yLabelString, colors, markers, figureName, logScale):




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
    if (logScale):
        plt.xscale("log")
        plt.savefig("Figures/" + figureName + "_log.png", bbox_inches='tight')
    else:
        plt.savefig("Figures/" + figureName + ".png", bbox_inches='tight')
    # plt.show()

