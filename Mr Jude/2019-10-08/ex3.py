import re
import csv
import pygal
import statistics

file = open("csv/activity.csv", "r")
csvReader = csv.reader(file)


def findNAs(file, reader):
    next(reader)
    NAs = 0
    while True:
        try:
            if "NA" == next(reader)[0]:
                NAs += 1
        except StopIteration:
            break
    file.seek(0)
    return NAs


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


def replaceCSV(file, stringFind, stringReplace):
    data = file.read()
    csvString = re.sub(stringFind, stringReplace, data)
    file.seek(0)
    return csvString


def writeToCSV(filename, data):
    try:
        with open(filename, "w") as fp:
            fp.write(data)
        return True
    except Exception:
        return False


def makeHistogram(median, mean):
    histogram = pygal.Bar()
    histogram.title = "Activity per Day (Mean)"
    days = [str(x+1) for x in range(len(mean))]
    for index, day in enumerate(days):
        histogram.add(day, mean[index])
    histogram.render_in_browser()


print(f"NAs in the file: {findNAs(file, csvReader)}")
newCSV = replaceCSV(file, "NA", "0")
print("File written successfully") if writeToCSV(
    "csv/activity_fixed.csv", newCSV) else print("Something's wrong")
makeHistogram(*getMedianMeanPerDay(file, csvReader))
