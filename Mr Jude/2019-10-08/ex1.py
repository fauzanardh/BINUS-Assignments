import matplotlib.pyplot as plt
import numpy as np
import smoothcurve
import statistics
import csv

file = open("csv/activity.csv", "r")
csvReader = csv.reader(file)


def getStepsPerDay(file, reader):
    next(reader)
    steps = []
    stepsToday = 0
    acc = 0
    while True:
        try:
            acc += 1
            step = next(reader)[0]
            stepsToday += int(step) if step != "NA" else 0
            if acc % 288 == 0:
                steps.append(stepsToday)
                stepsToday = 0
        except StopIteration:
            break
    file.seek(0)
    return steps


def getMedianMeanPerDay(file, reader):
    next(reader)
    medianPerDay = []
    meanPerDay = []
    stepToday = []
    acc = 0
    while True:
        try:
            acc += 1
            step = next(reader)[0]
            stepToday.append(int(step) if step != "NA" else 0)
            if acc % 288 == 0:
                stepToday.sort()
                medianPerDay.append(statistics.median(stepToday))
                meanPerDay.append(statistics.mean(stepToday))
                stepToday = []
        except StopIteration:
            break
    file.seek(0)
    return medianPerDay, meanPerDay


def makePlot(steps, median, mean):
    x = [x+1 for x in range(len(steps))]
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
    fig.suptitle('Activity')
    ax1.set_title("Steps")
    ax1.plot(*smoothcurve.make(x, steps))
    ax2.set_title("Median")
    ax2.plot(*smoothcurve.make(x, median))
    ax3.set_title("Mean")
    ax3.plot(*smoothcurve.make(x, mean))
    plt.tight_layout()
    plt.show()


steps = getStepsPerDay(file, csvReader)
median, mean = getMedianMeanPerDay(file, csvReader)
# print(mean)

makePlot(steps, median, mean)
