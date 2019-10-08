import re


def findHapax(filename):
    counts = {}
    with open(filename, "r") as handler:
        for y in re.findall("[a-z]+", handler.read().lower()):
            counts[y] = counts.get(y, 0) + 1
    return [key for key, value in counts.items() if value == 1]


print(findHapax("pride_and_prejudice.txt"))
