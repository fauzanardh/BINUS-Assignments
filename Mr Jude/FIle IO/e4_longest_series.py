import re


def indexOfNameStartsWith(lastChar, nameslist):
    for index in range(len(nameslist)):
        if nameslist[index].startswith(lastChar):
            return index
    return -1


def findLongestSeries(filename):
    with open(filename, "r") as handler:
        names = re.findall("[a-z]+", handler.read())
    longestSeries = []
    currentSeries = []

    for name in names:
        cName = name
        currentSeries.append(cName)

        nameslist = names[:]
        nameslist.pop(nameslist.index(cName))
        index = indexOfNameStartsWith(cName[-1], nameslist)
        while index != -1:
            cName = nameslist[index]
            currentSeries.append(cName)
            nameslist.pop(index)
            index = indexOfNameStartsWith(cName[-1], nameslist)

        if len(longestSeries) < len(currentSeries):
            longestSeries = currentSeries

        currentSeries = []

    return longestSeries


print(findLongestSeries("pokemons.txt"))
