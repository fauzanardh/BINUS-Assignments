import re
import pygal


def makeBar(dataDict):
    chart = pygal.Bar()
    chart.title = "Words count in certain literature"
    for key, value in dataDict.items():
        chart.add(key, value)
    chart.render_in_browser()


def countWords(userInput):
    counts = {}
    for word in re.findall("[a-z]+", userInput.lower()):
        counts[word] = counts.get(word, 0) + 1
    return dict(sorted(counts.items(), reverse=True, key=lambda x: x[1]))


def getTextFromFile(filename):
    with open(filename, "r") as fp:
        text = fp.read()
    return text


makeBar(countWords(getTextFromFile("pride_and_prejudice.txt")))
