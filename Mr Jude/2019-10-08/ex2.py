import matplotlib.pyplot as plt
import numpy as np
import smoothcurve
import csv

file = open("csv/activity.csv", "r")
csvReader = csv.reader(file)


def getPerInterval(file, reader):
    next(reader)
    stepsPerInterval = [0]*288
    totalDays = 61
    acc = 0
    while True:
        try:
            step = next(reader)[0]
            stepsPerInterval[acc] += int(step) if step != "NA" else 0
            acc += 1
            if acc == 288:
                acc = 0
        except StopIteration:
            break
    stepsPerIntervalAverage = []
    for steps in stepsPerInterval:
        stepsPerIntervalAverage.append(steps/totalDays)
    file.seek(0)
    return stepsPerInterval, stepsPerIntervalAverage


def makePlot(perInterval, perIntervalAverage):
    x = [x+1 for x in range(len(perInterval))]
    fig, axs = plt.subplots(2)
    axs[0].set_title("Per Interval")
    axs[0].plot(*smoothcurve.make(x, perInterval))
    axs[1].set_title("Per Interval (Average)")
    axs[1].plot(*smoothcurve.make(x, perIntervalAverage))
    plt.tight_layout()
    plt.show()


makePlot(*getPerInterval(file, csvReader))
