import re


def calcAverage(filename):
    # using dict to make it use less memory,
    # rather than using list with thousands of elements
    counts = {}
    with open(filename, "r") as handler:
        for y in re.findall("[a-z]+", handler.read().lower()):
            counts[y] = counts.get(y, 0) + 1
    total = 0
    totalWords = 0
    for key, val in counts.items():
        total += len(key)*val
        totalWords += val
    return total/totalWords


print(calcAverage("pride_and_prejudice.txt"))
